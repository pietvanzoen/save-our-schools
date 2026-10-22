#!/usr/bin/env python3
"""Housing units and K-5 student estimate for the Hayhurst -> Rieke boundary shift (Scenarios A and B).

The area moved from Hayhurst to Rieke is Hayhurst's southeast "panhandle": SW Vermont St / SW Capitol Hwy on the
north, SW 25th Ave on the east, SW Capitol Hwy on the west and SW Troy St on the south
(maps: [PPS:pps_net/rightsizing/school_impact/hayhurst.pdf p.4], [PPS:pps_net/rightsizing/school_impact/rieke.pdf p.4]).

Usage (from the repo root):
  python3 tools/hayhurst_rieke_shift.py --fetch   # re-pull Portland Maps layers into sources/gis/ (needs network)
  python3 tools/hayhurst_rieke_shift.py           # rebuild analysis/data/hayhurst_to_rieke_shift_*.csv from the archive

Stdlib only. A parcel is counted when an interior point of its polygon falls inside the study polygon
(boundary streets are centerlines, so parcels across the street fall outside).
"""
import argparse, csv, datetime, hashlib, json, os, subprocess, sys, urllib.parse
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "sources", "gis", "portlandmaps", "hayhurst_rieke_shift")
DATA = os.path.join(ROOT, "analysis", "data")
AREA = os.path.join(DATA, "hayhurst_to_rieke_shift_area.geojson")
BASE = "https://www.portlandmaps.com/arcgis/rest/services/Public"

LAYERS = {
    "taxlots.json": (f"{BASE}/Taxlots/MapServer/0/query",
        "STATE_ID,RNO,PROPERTYID,OWNER1,SITEADDR,PROP_CODE,PRPCD_DESC,LANDUSE,YEARBUILT,BLDGSQFT,BEDROOMS,FLOORS,UNITS,A_T_ACRES", True),
    "addresses.json": (f"{BASE}/BDS_Address/MapServer/0/query",
        "ADDRESS_FULL,ADDRESS_NUMBER,STREETNAME,UNIT,UNIT_TYPE,ADDR_TYPE,STATUS,TAXLOT_R_NUMBER,BLDG_ID,ADD_DATE", True),
}


def ring():
    return json.load(open(AREA))["features"][0]["geometry"]["coordinates"][0]


# ---------- geometry (stdlib) ----------
def pip(x, y, poly):
    inside = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            inside = not inside
    return inside


def area_centroid(p):
    a = cx = cy = 0.0
    for i in range(len(p) - 1):
        x1, y1 = p[i]; x2, y2 = p[i + 1]
        c = x1 * y2 - x2 * y1
        a += c; cx += (x1 + x2) * c; cy += (y1 + y2) * c
    if abs(a) < 1e-18:
        xs, ys = zip(*p); return sum(xs) / len(xs), sum(ys) / len(ys)
    return cx / (3 * a), cy / (3 * a)


def interior_point(p):
    cx, cy = area_centroid(p)
    if pip(cx, cy, p):
        return cx, cy
    xs, ys = zip(*p)
    best = None
    for i in range(1, 20):
        for j in range(1, 20):
            x = min(xs) + (max(xs) - min(xs)) * i / 20; y = min(ys) + (max(ys) - min(ys)) * j / 20
            if pip(x, y, p):
                d = (x - cx) ** 2 + (y - cy) ** 2
                if best is None or d < best[0]:
                    best = (d, x, y)
    return (best[1], best[2]) if best else (cx, cy)


# ---------- fetch ----------
def fetch():
    os.makedirs(SRC, exist_ok=True)
    geom = json.dumps({"rings": [ring()], "spatialReference": {"wkid": 4326}})
    manifest = []
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    for fname, (url, fields, geomflag) in LAYERS.items():
        params = {"where": "1=1", "geometry": geom, "geometryType": "esriGeometryPolygon", "inSR": "4326",
                  "spatialRel": "esriSpatialRelIntersects", "outFields": fields,
                  "returnGeometry": "true" if fname == "taxlots.json" else "false", "outSR": "4326", "f": "json"}
        out = subprocess.run(["curl", "-s", "--max-time", "180", "-X", "POST", "-d", urllib.parse.urlencode(params), url],
                             capture_output=True, text=True, check=True).stdout
        d = json.loads(out)
        if "error" in d or d.get("exceededTransferLimit"):
            sys.exit(f"{fname}: {d.get('error') or 'exceededTransferLimit'}")
        path = os.path.join(SRC, fname)
        open(path, "w").write(out)
        manifest.append({"path": os.path.relpath(path, os.path.join(ROOT, "sources")), "url": url, "method": "POST",
                         "params": {k: v for k, v in params.items() if k != "geometry"},
                         "geometry": "rings of analysis/data/hayhurst_to_rieke_shift_area.geojson (WGS84)",
                         "features": len(d.get("features", [])), "fetched_at": now,
                         "sha256": hashlib.sha256(out.encode()).hexdigest()})
        print(fname, len(d.get("features", [])))
    mpath = os.path.join(SRC, "_manifest.json")
    old = json.load(open(mpath)) if os.path.exists(mpath) else []
    keep = [m for m in old if m["path"] not in {x["path"] for x in manifest}]
    json.dump(keep + manifest, open(mpath, "w"), indent=1)


# ---------- unit estimates ----------
# Overrides where the assessor UNITS field is missing or implausible. Low/high are dwelling units.
# Evidence keys: HF = Home Forward property page (sources/housing/homeforward/), BDS = BDS address points in this
# archive (addresses.json), ASR = assessor record (taxlots.json).
OVERRIDES = {
    "6715 SW 26TH AVE": (122, 122, "Stephens Creek Crossing (Home Forward public housing, built 2013). HF: 122 units; ASR lists 150 here + 47 on 6803 SW 26th (197), inconsistent with HF, so 122 is used and 6803 is counted here."),
    "6803 SW 26TH AVE": (0, 0, "Second Stephens Creek Crossing parcel; its units are counted on 6715 SW 26th Ave."),
    "6630-6640 SW CAPITOL HWY": (18, 54, "ASR: 54 units on 15,470 sq ft (~290 sq ft/unit, implausible); BDS: 18 APT address points. Range."),
    "2724 SW CUSTER ST": (11, 22, "Apartments on parcel coded IMPROVED LAND AS VACANT. ASR: 22 units on 5,663 sq ft; BDS: 11 APT address points. Range."),
    "2747-2757 SW TROY ST": (6, 18, "Class 5-8 UNIT MULTI-FAMILY; ASR: 18 units on 7,688 sq ft; BDS: 6 address points. Range."),
    "2805-2817 SW TROY ST": (5, 12, "Class 5-8 UNIT MULTI-FAMILY; ASR: 12 units on 6,568 sq ft; BDS: 4 address points. Range."),
    "2907-2921 SW CANBY CT": (6, 9, "Class 5-8 UNIT MULTI-FAMILY; ASR: 9 units; BDS: 6 address points. Range."),
    "2831-2837 SW TROY ST": (4, 4, "Class 2-4 UNIT MULTI-FAMILY with ASR units=1; address range 2831-2837 and 4 BDS address points: 4 units."),
    "7638-7646 SW CAPITOL HWY": (3, 3, "Store with apartments over; BDS: 3 APT address points."),
    "SW CAPITOL HWY": (8, 8, "Multnomah Heights Condominiums (common-elements parcel; unit parcels have no polygon). BDS: 9 address points at 6682 SW Capitol Hwy incl. the base address: ~8 units."),
    "SW MILES ST": (7, 7, "Miles Street Condominiums (common-elements parcel). BDS: 8 address points at 2937 SW Miles St incl. the base address: ~7 units."),
}

CATEGORY = {
    "RESIDENTIAL IMPROVED": "single_family_detached",
    "ROW/ATTACHED HOUSING": "single_family_attached",
    "2-4 UNIT MULTI-FAMILY": "plex_2_4",
    "5-8 UNIT MULTI-FAMILY": "apartments_market",
    "9-20 UNIT MULTI-FAMILY": "apartments_market",
    "CT APT 21-100 W/AMENITIES": "apartments_market",
    "CT APT SUBSIDIZED GARDEN": "affordable_stephens_creek",
    "RESIDENTIAL CONDO": "condo",
    "STORE W/APT OR OFFICE OVER": "mixed_use",
    "RESIDENTIAL, COMMERCIAL USE": "mixed_use",
    "GENERIC COMMERCIAL USE": "mixed_use",
    "IMPROVED LAND AS VACANT": "apartments_market",  # only 2724 SW Custer (apartments) carries units
}


def build():
    poly = ring()
    tl = json.load(open(os.path.join(SRC, "taxlots.json")))["features"]
    addr = [f["attributes"] for f in json.load(open(os.path.join(SRC, "addresses.json")))["features"]]
    addr_by_rno = Counter(a["TAXLOT_R_NUMBER"] for a in addr)
    rows = []
    for f in tl:
        a = f["attributes"]
        x, y = interior_point(f["geometry"]["rings"][0])
        if not pip(x, y, poly):
            continue
        desc = (a.get("PRPCD_DESC") or "").strip()
        site = (a.get("SITEADDR") or "").strip()
        units = a.get("UNITS")
        cat = CATEGORY.get(desc, "non_residential_or_vacant")
        if site in OVERRIDES and (desc in CATEGORY):
            lo, hi, note = OVERRIDES[site]
        elif cat == "non_residential_or_vacant":
            lo = hi = 0; note = ""
            if desc == "" and not site:
                note = "Parcel with no assessor attributes (right-of-way or common area)."
        elif units is None:
            lo = hi = 0; note = "No unit count in assessor record."
        else:
            lo = hi = int(units); note = ""
        if cat == "single_family_detached" and lo == 2:
            note = "House plus second unit (ADU or duplex) per assessor UNITS=2."
        rows.append({
            "state_id": a.get("STATE_ID"), "rno": a.get("RNO"), "site_address": site, "owner": (a.get("OWNER1") or "").strip(),
            "property_class": desc, "landuse": a.get("LANDUSE"), "year_built": a.get("YEARBUILT"), "bldg_sqft": a.get("BLDGSQFT"),
            "acres": round(a["A_T_ACRES"], 3) if a.get("A_T_ACRES") is not None else "",
            "assessor_units": "" if units is None else int(units), "category": cat,
            "units_est_low": lo, "units_est_high": hi, "property_id": a.get("PROPERTYID"), "bds_address_points": addr_by_rno.get(a.get("PROPERTYID"), 0),
            "lon": round(x, 6), "lat": round(y, 6), "note": note,
            "source": "sources/gis/portlandmaps/hayhurst_rieke_shift/taxlots.json (Multnomah County assessor via Portland Maps, Public/Taxlots layer 0)"
                      + ("; sources/housing/homeforward/stephens-creek-crossing.html" if "Stephens Creek" in note else ""),
        })
    rows.sort(key=lambda r: (r["category"], r["site_address"]))
    out = os.path.join(DATA, "hayhurst_to_rieke_shift_parcels.csv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    # ---- summary by category ----
    agg = defaultdict(lambda: [0, 0, 0])
    for r in rows:
        g = agg[r["category"]]; g[0] += 1; g[1] += r["units_est_low"]; g[2] += r["units_est_high"]
    sfd = [r for r in rows if r["category"] == "single_family_detached"]
    houses = len(sfd); second = sum(1 for r in sfd if r["units_est_low"] == 2)
    attached = agg["single_family_attached"][0]
    mkt = ["plex_2_4", "apartments_market", "condo", "mixed_use"]
    mkt_lo = sum(agg[c][1] for c in mkt); mkt_hi = sum(agg[c][2] for c in mkt)
    scc = agg["affordable_stephens_creek"][1]

    # ---- K-5 estimate ----
    PSU = "[PPS:pps_net/data-and-reporting/2026-27/psu_prc_enrollment_forecast_2026-27_to_2035-36.pdf p.16]"
    PSU41 = "[PPS:pps_net/data-and-reporting/2026-27/psu_prc_enrollment_forecast_2026-27_to_2035-36.pdf p.25]"
    k5_share = 6 / 13  # K-5 = 6 of the 13 grades in a 5-17 age span
    # Stephens Creek unit mix (Home Forward): 1BR 19, 2BR 21, 3BR 79, 4BR 5
    scc_lo = 105 * 0.265
    scc_hi = (19 * 0.07 + 21 * 0.42 + 84 * 0.91) * (0.265 / 0.516)
    est = [
        ("single_family (detached + attached)", houses + attached, houses + attached, 0.12, round(0.45 * k5_share, 2),
         f"High: PSU single-family yield 0.45 PPS students age 5-17 per unit x 6/13 K-5 share {PSU}. Low: Analysis: judgment discount for an established neighborhood (older households); not a PSU figure."),
        ("secondary units on house lots (ADU/duplex)", second, second, 0.0, round(0.04 * k5_share, 2),
         f"PSU multi-family studio/1BR yield 0.04 x 6/13 {PSU}."),
        ("market-rate multifamily (plexes, apartments, condos, units over shops)", mkt_lo, mkt_hi, 0.05, 0.08,
         f"Analysis: blend of PSU multi-family yields (1BR 0.04, 2BR 0.26 students age 5-17) x 6/13 {PSU}, assuming mostly 1-2 bedroom units."),
        ("Stephens Creek Crossing (affordable, 105 of 124 listed units are 2+ BR)", scc, scc, None, None,
         f"Low: PSU affordable K-5 rate 0.265 per regulated 2+ BR unit at 5+ years x 105 units {PSU41}. High: PSU affordable yields by bedroom (1BR 0.07, 2BR 0.42, 3+BR 0.91) x unit mix, x K-5 share 0.265/0.516 {PSU} {PSU41}. Unit mix: sources/housing/homeforward/stephens-creek-crossing.html"),
    ]
    out2 = os.path.join(DATA, "hayhurst_to_rieke_shift_k5_estimate.csv")
    tot_lo = tot_hi = 0
    with open(out2, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["component", "units_low", "units_high", "k5_per_unit_low", "k5_per_unit_high", "k5_public_school_residents_low", "k5_public_school_residents_high", "basis"])
        for name, ulo, uhi, ylo, yhi, basis in est:
            if ylo is None:
                klo, khi = scc_lo, scc_hi; ylo_s = round(scc_lo / scc, 3); yhi_s = round(scc_hi / scc, 3)
            else:
                klo, khi = ulo * ylo, uhi * yhi; ylo_s, yhi_s = ylo, yhi
            tot_lo += klo; tot_hi += khi
            w.writerow([name, ulo, uhi, ylo_s, yhi_s, round(klo), round(khi), basis])
        w.writerow(["TOTAL K-5 public-school residents", "", "", "", "", round(tot_lo), round(tot_hi), "Sum of rows above"])
        cap = 262 / 354
        w.writerow(["Attending Hayhurst today (x 74% neighborhood capture)", "", "", "", "", round(tot_lo * cap), round(tot_hi * cap),
                    "Hayhurst neighborhood: 262 of 354 PPS K-5 residents attend Hayhurst (74%), Oct 2025 [PPS:pps_net/data-and-reporting/2025-26/neighborhood_capture_rate_metrics.pdf p.1]. Analysis: assumes the shift area matches the Hayhurst-wide rate."])

    print(f"parcels inside: {len(rows)}")
    print(f"single-family: {houses} detached houses ({second} with a second unit) + {attached} attached")
    for c in mkt + ["affordable_stephens_creek"]:
        print(f"  {c}: parcels {agg[c][0]}, units {agg[c][1]}-{agg[c][2]}")
    print(f"total dwelling units: {houses + second + attached + mkt_lo + scc}-{houses + second + attached + mkt_hi + scc}")
    print(f"K-5 public-school residents: {tot_lo:.0f}-{tot_hi:.0f}; at Hayhurst (74%): {tot_lo*cap:.0f}-{tot_hi*cap:.0f}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fetch", action="store_true", help="re-pull the Portland Maps layers into sources/gis/ first")
    args = ap.parse_args()
    if args.fetch:
        fetch()
    build()
