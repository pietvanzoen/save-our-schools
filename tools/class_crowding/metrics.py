import sys; sys.path.insert(0,__import__('os').path.dirname(__file__))
from model import *
COMFORT=17040/724.5
def added(before,after): return max(0.0, after-max(before,COMFORT))
def summarize(sc):
    rows,mov,flows=run(sc)
    R=[w for w in rows if w["home"]>0]
    rec_n=sum(w["home"] for w in R)
    rec_up=sum(w["home"] for w in R if w["after"]-w["before_home"]>=0.5)
    rec_add=sum(w["home"]*added(w["before_home"],w["after"]) for w in R)
    mov_n=sum(m["n"] for m in mov)
    mov_add=sum(m["n"]*added(m["before"],m["after"]) for m in mov)
    def band(lst,key_b,key_a,ncol):
        b={"none":0,"mod":0,"sev":0}
        for x in lst:
            a=added(x[key_b],x[key_a]); n=x[ncol]
            b["none" if a<2 else "mod" if a<5 else "sev"]+=n
        return b
    rb=band(R,"before_home","after","home"); mb=band(mov,"before","after","n")
    ge30_before=sum(w["home"] for w in R if w["before_home"]>=30)+sum(m["n"] for m in mov if m["before"]>=30)
    ge30_after=sum(w["home"] for w in R if w["after"]>=30)+sum(m["n"] for m in mov if m["after"]>=30)
    # per school
    sch=collections.defaultdict(lambda: dict(home=0,inc=0,bsum=0,asum=0,add=0,maxafter=0,worst="",grades=[]))
    for w in rows:
        if w["group"].startswith("new:"): continue
        s=sch[w["school"]]; s["home"]+=w["home"]; s["inc"]+=w["incoming"]
        if w["home"]>0:
            s["bsum"]+=w["home"]*w["before_home"]; s["asum"]+=w["home"]*w["after"]; s["add"]+=w["home"]*added(w["before_home"],w["after"])
        if w["after"]>s["maxafter"]: s["maxafter"]=w["after"]; s["worst"]=w["grade"]
        s["grades"].append(w)
    for m in mov:
        k=m["receiver"]
        if k in sch: sch[k]["add"]+=m["n"]*added(m["before"],m["after"])
    return dict(rows=rows,mov=mov,rec_n=rec_n,rec_up=rec_up,rec_add=rec_add,mov_n=mov_n,mov_add=mov_add,rb=rb,mb=mb,ge30=(ge30_before,ge30_after),sch=sch)
if __name__=="__main__":
    print("comfort",COMFORT)
    for sc in "AB":
        S=summarize(sc)
        print("==",sc,"movers",round(S["mov_n"]),"recv",round(S["rec_n"]),"recv up",round(S["rec_up"]),"bands recv",{k:round(v) for k,v in S["rb"].items()},"bands mov",{k:round(v) for k,v in S["mb"].items()},"ge30",[round(x) for x in S["ge30"]])
        print("added per student recv",S["rec_add"]/S["rec_n"],"movers",S["mov_add"]/S["mov_n"])
        for s,v in sorted(S["sch"].items(),key=lambda kv:-kv[1]["add"]):
            if v["home"]: print(f"  {s:24s} home {v['home']:5.0f} inc {v['inc']:5.0f} before {v['bsum']/v['home']:5.1f} after {v['asum']/v['home']:5.1f} max {v['maxafter']:5.1f} ({v['worst']}) strain {v['add']:6.0f}")
