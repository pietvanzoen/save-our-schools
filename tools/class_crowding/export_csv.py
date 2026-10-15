"""Class-crowding model for PPS rightsizing (Oct 2026).
Moves Sept 22, 2026 K-5 students per Scenarios A/B (school_impact.csv shares), re-staffs each receiving
grade with PPS's K-5 maximum-class-size formula [BB:3997160 p.213], and writes
analysis/data/class_crowding_model_2026.csv (one row per scenario x receiving school/program x grade).
Run: python3 tools/class_crowding/export_csv.py"""
import os, sys, csv; sys.path.insert(0, os.path.dirname(__file__))
from metrics import *
out=os.path.join(os.path.dirname(__file__),"..","..","analysis/data/class_crowding_model_2026.csv")
with open(out,"w",newline="") as fh:
    w=csv.writer(fh); w.writerow(["scenario","receiving_school","group","grade","students_staying","students_arriving","total","homerooms_after","avg_class_before","avg_class_after","crowding_score_staying","note"])
    for sc in "AB":
        rows,mov,flows=run(sc)
        for r in rows:
            b=r["before_home"]
            w.writerow([sc,r["school"],r["group"],r["grade"],round(r["home"],1),round(r["incoming"],1),round(r["total"],1),r["sections"],
                        "" if b is None else round(b,1),round(r["after"],1),"" if b is None else round(added(b,r["after"]),1),
                        "new program at receiver" if r["group"].startswith("new:") else ""])
print("wrote",out)
