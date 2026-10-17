"""Parse school total tables (K-5, 6-8, 9-12) from the 2003-04..2006-07 PSU PRC forecast reports in sources/psu_prc/.
Run from the repo root; writes old_rows.json. These rows were merged with the 2008-09..2026-27 editions and matched to
later reports' history columns (horizons 1-10) to build analysis/data/psu_forecast_vs_actual_by_school.csv."""
import re,json,sys
IN='sources/psu_prc/'
SETS={'2003-04':('psu_prc_enrollment_forecast_2003-04_base_oct2002',{'K5':[21,22],'MS':[23],'HS':[24]}),
      '2004-05':('psu_prc_enrollment_forecast_2004-05_base_oct2003',{'K5':[57,58],'MS':[61],'HS':[64]}),
      '2005-06':('psu_prc_enrollment_forecast_2005-06_base_oct2004',{'K5':[56,57],'MS':[58],'HS':[59]}),
      '2006-07':('psu_prc_enrollment_forecast_2006-07_base_oct2005',{'K5':[63,64],'MS':[65],'HS':[66]})}
TOK=r'(?:\d{1,3}(?:,\d{3})+|\d+|Closed|NA|N/A|-{1,2})'
out=[];bad=[]
for v,(f,tabs) in SETS.items():
    pages=open(IN+f+'.pdf.txt').read().split('\f')
    for lvl,pp in tabs.items():
        years=None
        for p in pp:
            hdr=False
            for line in pages[p-1].splitlines():
                ys=re.findall(r'\b(19\d\d|20\d\d)\b',line)
                if len(ys)>=8 and not hdr: years=[int(y) for y in ys]; hdr=True; continue
                if years is None: continue
                m=re.match(r'^\s*(\d{3,5}|-|[\d,]{4,6})?\s*([A-Za-z][A-Za-z.\'/&()\-* ]*?)\s+((?:\d|Closed|NA\b|N/A).*)$',line)
                if not m: 
                    if line.strip(): bad.append((v,p,line.strip()[:80]))
                    continue
                name=m.group(2).strip(); rest=m.group(3)
                if name in('Page',) or 'Total' in name or name.startswith(('Spec.','Gr.')): continue
                toks=re.findall(TOK,rest)
                if not toks or len(toks)>len(years): bad.append((v,p,line.strip()[:90])); continue
                ys=years[-len(toks):]  # right-align when leading blanks
                vals={}
                for y,t in zip(ys,toks):
                    if re.match(r'^[\d,]+$',t): vals[y]=int(t.replace(',',''))
                out.append(dict(v=v,lvl=lvl,name=name,no=(m.group(1) or '').strip(),years=years,vals=vals,ntok=len(toks),page=p,file=f,raw=line.strip()[:60]))
json.dump(out,open('old_rows.json','w'),indent=0)
print(len(out))
for b in bad: print('BAD',b)
for r in out:
    if r['ntok']!=len(r['years']): print('SHORT',r['v'],r['page'],r['name'],r['ntok'],len(r['years']))
