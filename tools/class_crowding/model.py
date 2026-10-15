import sys, math, collections, csv, json
sys.path.insert(0,__import__('os').path.dirname(__file__))
from load import *
D=load(); T1=title1()
P,C="Program","Co-located"
# (sender, subgroup) -> list of (receiver, subgroup or None for a new standalone program, share, note)
BOTH=[
 ("Beach",P,"Chief Joseph",P,1.0,""),("Beach",C,"César Chávez",C,1.0,"Spanish DLI"),
 ("Buckman",P,"Abernethy",P,0.5,"PPS: ~50%"),("Buckman",P,"Sunnyside Environmental",P,0.5,"PPS: ~50%"),
 ("Creston",P,"Atkinson",P,1.0,"DHH program to Glencoe not modeled"),
 ("Atkinson",C,"Lent",C,1.0,"Spanish DLI"),
 ("Irvington",P,"Beverly Cleary",P,1.0,""),
 ("James John",P,"Sitton",P,1.0,""),("James John",C,"César Chávez",C,1.0,"Spanish DLI"),
 ("Sitton",C,"César Chávez",C,1.0,"Spanish DLI"),
 ("César Chávez",P,"Rosa Parks",P,1.0,"non-DLI K-5"),
 ("Maplewood",P,"Hayhurst",P,0.7,"PPS: 70%"),("Maplewood",P,"Rieke",P,0.3,"PPS: 30%"),
 ("Hayhurst",P,"Rieke",P,0.2,"share not published; ~20% assumed (Stephens Creek Crossing area)"),
 ("Marysville",P,"Arleta",P,1.0,"merge from 2028-29; Kelly share not published, all assigned to Arleta"),
 ("Peninsula",P,"Rosa Parks",P,1.0,""),
 ("Sabin",P,"MLK Jr",P,1.0,""),("MLK Jr",C,"Boise-Eliot/Humboldt",None,1.0,"Mandarin DLI, new program at receiver"),
 ("Clark",C,"Woodstock",C,1.0,"Mandarin DLI"),
 ("Scott",C,"Rigler",C,1.0,"Spanish DLI"),
 ("Woodmere",P,"Whitman",P,1.0,""),
]
ONLY={"A":[("Lewis",P,"Duniway",P,1.0,""),("Rose City Park",P,"Scott",P,1.0,""),("Rose City Park",C,"Vestal",None,1.0,"Vietnamese DLI, new program at receiver"),
           ("Stephenson",P,"Markham",P,0.7,"PPS: 70%"),("Stephenson",P,"Capitol Hill",P,0.3,"PPS: 30%")],
      "B":[]}
def mx(school,g): return (MAX_T1 if T1.get(school) else MAX_OT)[g]
def run(sc):
    flows=BOTH+ONLY[sc]
    senders={(s,sg) for s,sg,*_ in flows}
    # incoming per receiver group
    inc=collections.defaultdict(lambda: collections.defaultdict(float)); newprog=collections.defaultdict(lambda: collections.defaultdict(float))
    movers_detail=[]
    for s,sg,r,rg,sh,note in flows:
        for g in G:
            x=D[(s,sg)].get(g)
            if not x: continue
            k=(r,rg) if rg else (r,"new:"+s)
            inc[k][g]+=x["n"]*sh
    cur={k:cur_class_sizes(v) for k,v in D.items()}
    rows=[]   # one row per (group, grade, origin) with students, before, after
    for k,gi in inc.items():
        r,rg=k
        base=D.get(k,{}) if not rg.startswith("new:") else {}
        # receiving group stays only if it is not itself a sender
        out_share=sum(f[4] for f in flows if (f[0],f[1])==k)
        stays = k in D and out_share<1
        for g in G:
            n_home = base.get(g,{}).get("n",0)*(1-out_share) if stays else 0
            n_in = gi.get(g,0)
            tot=n_home+n_in
            if tot==0: continue
            secs=max(1,math.ceil(tot/mx(r,g)-1e-9))
            after=tot/secs
            rows.append(dict(school=r,group=rg,grade=g,home=n_home,incoming=n_in,total=tot,sections=secs,after=after,
                             before_home=cur[k][g] if stays and g in cur.get(k,{}) else None))
    # movers: before from sender group
    for s,sg,r,rg,sh,note in flows:
        k=(r,rg) if rg else (r,"new:"+s)
        for g in G:
            x=D[(s,sg)].get(g)
            if not x: continue
            after=[w for w in rows if (w["school"],w["group"])==k and w["grade"]==g][0]["after"]
            movers_detail.append(dict(sender=s,sgroup=sg,receiver=r,grade=g,n=x["n"]*sh,before=cur[(s,sg)][g],after=after,note=note))
    return rows,movers_detail,flows
