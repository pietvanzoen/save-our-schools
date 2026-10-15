"""Grades 6-8 and K-8 reconciliation for the class-crowding model.
6-8 class size = average students per core-course section (math, ELA/English, science, social studies)
from the staffing workbook's '6-8 Course Loads 26-27' tab. PPS staffs grades 6-8 by student ratio,
so a receiving middle school's class size is assumed unchanged; a moving student's class size becomes
the receiving school's average."""
import os, sys, csv, re, collections
sys.path.insert(0, os.path.dirname(__file__))
from metrics import summarize, added as added_k5
ROOT=os.path.join(os.path.dirname(__file__),"..","..")+"/"
CL=ROOT+"sources/staffing/2026-09-22_board-request/tabs/02_6_8_Course_Loads_26_27.csv"
def core_sizes():
    by=collections.defaultdict(list)
    for r in csv.DictReader(open(CL)):
        c=r["CourseName"]
        if not re.search(r"math|language arts|english|science|social|humanities|literacy|ela\b",c,re.I): continue
        if re.search(r"aide|support|lab assist|intervention|sped|resource|esl|eld|tutorial|advisory",c,re.I): continue
        for p in ["Period%d"%i for i in range(1,9)]+["PeriodOther"]:
            v=r[p].strip()
            if v.isdigit() and int(v)>=5: by[r["School"]].append(int(v))
    avg={s:sum(v)/len(v) for s,v in by.items()}
    allv=[x for v in by.values() for x in v]
    return avg, sum(allv)/len(allv)
CS, COMFORT68 = core_sizes()
# workbook short names
N={"César Chávez":"Chavez","Faubion":"Faubion","Vernon":"Vernon","Beverly Cleary":"BevCleary","Laurelhurst":"Laurelhrst",
   "Bridger Creative Science":"Bridger","Sunnyside Environmental":"SunnysideE","Ockley Green":"OckleyGrMS","Beaumont":"Beaumont",
   "Sellwood":"Sellwood","George":"George","Harriet Tubman":"Tubman","Mt Tabor":"Mt Tabor","Harrison Park":"HarrisonPk",
   "Hosford":"Hosford","Lane (Brentwood)":"Lane","Roseway Heights":"RosewayHts","Odyssey":"Odyssey"}
# (from, students Sept 2026 or noted, to, share, source note)
MOVES68=[("César Chávez",137,"George",1,"6-8 at K-8 (Sept 22 count)"),("Faubion",195,"Ockley Green",1,"6-8 at K-8 (Sept 22 count)"),
 ("Vernon",169,"Harriet Tubman",1,"6-8 at K-8 (Sept 22 count)"),("Beverly Cleary",193,"Beaumont",1,"6-8 at K-8 (Sept 22 count)"),
 ("Laurelhurst",233,"Mt Tabor",1,"6-8 at K-8 (Sept 22 count)"),("Bridger Creative Science",114,"Harrison Park",1,"6-8 at K-8 (Sept 22 count)"),
 ("Sunnyside Environmental",189,"Hosford",1,"6-8 at K-8 (Sept 22 count)"),
 ("Ockley Green",64,"George",1,"Spanish DLI 6-8 (PSU 2026-27 forecast)"),("Beaumont",101,"Roseway Heights",1,"Spanish DLI 6-8 (PSU 2026-27 forecast)"),
 ("Sellwood",537,"Hosford",0.5,"closes 2028; split not published, 50/50 assumed (spring staffing count)"),
 ("Sellwood",537,"Lane (Brentwood)",0.5,"closes 2028; split not published, 50/50 assumed (spring staffing count)")]
# middle-school students already there (spring staffing count, minus programs leaving)
RECV68={"George":374,"Ockley Green":436-64,"Harriet Tubman":438,"Beaumont":413-101,"Mt Tabor":415,"Harrison Park":440,"Hosford":519,"Lane (Brentwood)":427,"Roseway Heights":560}
ODYSSEY=209   # whole program moves to the MLC site; classes move intact
# PPS published K-8 movers [BB:14511742 p.44] and K-8 denominator (Oct 2025 district K-8, all schools)
PPS_MOVED={"A":7981,"B":6988}; PPS_K8=29448
# Oct 1, 2025 (PPS's basis) bottom-up for reconciliation: PSU 2026-27 report y2025-26 actuals and PPS Oct 2025 grade report
OCT25={"K-5 school closures":{"A":3694,"B":2737},"K-5 language-program moves (Atkinson, Clark, MLK, Scott, Sitton DLI; Chávez non-DLI)":{"A":900,"B":900},
       "Hayhurst boundary portion to Rieke (~20%, assumed)":{"A":58,"B":58},"Grades 6-8 leaving K-8 schools":{"A":1361,"B":1361},
       "Middle-school Spanish DLI moves (Ockley Green, Beaumont)":{"A":164,"B":164},"Sellwood MS closure (2028)":{"A":564,"B":564},"Odyssey move to MLC site":{"A":217,"B":217}}
def added68(b,a): return max(0.0,a-max(b,COMFORT68))
def summarize_k8(sc):
    S=summarize(sc)
    mov68=[]
    for f,n,t,sh,note in MOVES68:
        b=CS[N[f]]; a=CS[N[t]]
        mov68.append(dict(frm=f,to=t,n=n*sh,before=b,after=a,score=added68(b,a),note=note))
    m68n=sum(m["n"] for m in mov68)+ODYSSEY
    m68c=sum(m["n"] for m in mov68 if m["score"]>=2); m68s=sum(m["n"] for m in mov68 if m["score"]>=5)
    k5c=S["mb"]["mod"]+S["mb"]["sev"]; k5s=S["mb"]["sev"]
    scored=S["mov_n"]+m68n
    rec68=sum(RECV68.values())
    recon={k:v[sc] for k,v in OCT25.items()}
    recon["Other boundary and pathway changes in PPS's count (not broken out by PPS)"]=PPS_MOVED[sc]-sum(recon.values())
    return dict(S=S,mov68=mov68,moved_pps=PPS_MOVED[sc],scored=scored,
                moved_crowded=k5c+m68c,moved_severe=k5s+m68s,moved_little=scored-(k5c+m68c),moved_unscored=PPS_MOVED[sc]-scored,
                recv_k5=S["rec_n"],recv_68=rec68,recv_crowded=S["rb"]["mod"]+S["rb"]["sev"],recv_severe=S["rb"]["sev"],
                recv_little=S["rec_n"]-(S["rb"]["mod"]+S["rb"]["sev"])+rec68,recon=recon)
if __name__=="__main__":
    print("6-8 comfort",round(COMFORT68,1))
    for sc in "AB":
        R=summarize_k8(sc); print(sc,{k:(round(v) if isinstance(v,float) else v) for k,v in R.items() if k not in("S","mov68","recon")})
        print(" recon",R["recon"])
        for m in R["mov68"]: print("  ",m["frm"],"->",m["to"],round(m["n"]),round(m["before"],1),round(m["after"],1),round(m["score"],1))
