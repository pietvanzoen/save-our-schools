"""Parse Table C5 (Total K-12 Enrollment by School, pp.110-113) from the 2007-08 PSU PRC report.
Usage: python3 parse_2007_report.py sources/psu_prc/psu_prc_enrollment_forecast_2007-08_base_oct2006.pdf.txt out.json
Zeros (closed schools) are dropped."""
import re,json,sys
IN=sys.argv[1]; OUT=sys.argv[2]
pages=open(IN).read().split('\f')
years=list(range(2004,2016)); out=[]
for p in (110,111,112,113):
    for line in pages[p-1].splitlines():
        m=re.match(r'^\s*(\d{3,4}(?:/\d{3,4})?)\s+(.+?)\s+((?:[\d,]+\s+){11}[\d,]+)\s*$',line)
        if not m: continue
        name=m.group(2).strip(); g=None
        gm=re.search(r'\s+(ES|MS|HS|K-8|K-6)\d?$',name)
        if gm: g=gm.group(1); name=name[:gm.start()]
        name=re.sub(r'(\D)\d$',r'\1',name).strip()
        vals=[int(x.replace(',','')) for x in m.group(3).split()]
        keep=[(y,v) for y,v in zip(years,vals) if v>0]
        out.append(dict(v='2007-08',name=name,grade=g or '?',years=[y for y,_ in keep],vals=[v for _,v in keep],page=p,raw=line.strip()[:50]))
json.dump(out,open(OUT,'w'),ensure_ascii=False)
print(len(out)); print([ (r['name'],r['grade']) for r in out])
