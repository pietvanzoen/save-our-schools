import csv, collections, math
import os
ROOT=os.path.join(os.path.dirname(__file__),"..","..")+"/"
MAX_T1={"KG":28,"1":30,"2":30,"3":30,"4":33,"5":33}
MAX_OT={"KG":29,"1":31,"2":32,"3":33,"4":34,"5":34}
G=["KG","1","2","3","4","5"]
def title1():
    t={}
    for row in csv.reader(open(ROOT+"sources/staffing/2026-09-22_board-request/tabs/00_School_Detail_wo_ESL_or_SPED_or.csv")):
        if len(row)>5 and row[4] and row[0] in ("Title 1","Not Title 1","Title I","Not Title I"):
            t[row[4].strip()]= row[0].startswith("Title")
    return t
def load():
    d=collections.defaultdict(dict)  # (school,sub) -> grade -> dict
    for r in csv.DictReader(open(ROOT+"analysis/data/enrollment_2026-27_sept_by_grade.csv")):
        if r["grade"] not in G: continue
        d[(r["school"],r["subgroup"])][r["grade"]]=dict(n=int(r["enrollment_count_2026_09"]),proj=int(r["projected_enrollment_2026_27"] or 0),
           unit=r["unit"],sec=float(r["initial_sections"] or 0),extra=float(r["school_funded_homerooms"] or 0),src=r["source"])
    return d
def cur_class_sizes(grades):
    """grade -> current avg class size, using units (blends share sections)"""
    units=collections.defaultdict(lambda:[0,0.0])
    for g,x in grades.items():
        units[x["unit"]][0]+=x["n"]; units[x["unit"]][1]+=x["sec"]+x["extra"]
    out={}
    for g,x in grades.items():
        n,s=units[x["unit"]]; out[g]=n/s if s else None
    return out
