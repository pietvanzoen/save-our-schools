// BoardBook crawler for PPS (organization 915). Paste tools/browser/zipdl.js first, then this file, into the DevTools
// console on a https://meetings.boardbook.org/ page (same origin, so fetches work without CORS issues).
//
//   const idx = await window.__bbIndex('2025-01-01');   // meeting list with videos and agenda attachments
//   window.__bbSaveIndex(idx);                          // downloads boardbook_index.zip -> boardbook_index_2025_2026.json
//   await window.__bbFetch(idx, {only:['770670']});     // download one or more meetings (omit `only` for all)
//   window.__bbstat                                     // progress
//
// Each zip unpacks into sources/ as boardbook/meetings/<YYYY-MM-DD>_<meetingId>_<slug>/{agenda,minutes,
// supplementals,public_notice}.html + attachments/<docId>_<name>.pdf + minutes_<docId>.pdf + public_notice_<docId>.pdf,
// plus a _manifest_*.json with URL, status, bytes and fetch time for provenance. Then run the processing steps in RUNBOOK.md.
//
// Notes:
//  - BoardBook serves every attachment as a PDF at /Documents/DownloadPDF/<docId>?org=915 (Office originals aren't available).
//  - Minutes and public notices are viewer shells; the real PDF id is in <input id="NewDocumentViewerDocumentID">.
//  - Chrome must allow automatic multiple downloads from meetings.boardbook.org (it asks once).
(function(){
const ORG='/public/Organization/915';
const mon={January:1,February:2,March:3,April:4,May:5,June:6,July:7,August:8,September:9,October:10,November:11,December:12};
window.__bbDir=(head,id)=>{const x=head.match(/(January|February|March|April|May|June|July|August|September|October|November|December) (\d+), (20\d\d)/);
  const d=x?`${x[3]}-${String(mon[x[1]]).padStart(2,'0')}-${String(x[2]).padStart(2,'0')}`:'unknown';
  const slug=head.replace(/^Cancelled /,'').split(' - ').slice(1).join(' ').replace(/Cancelled$/,'').trim().toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'').slice(0,50);
  return `${d}_${id}_${slug}`;};
const dateOf=head=>{const x=head.match(/(January|February|March|April|May|June|July|August|September|October|November|December) (\d+), (20\d\d)/); return x?`${x[3]}-${String(mon[x[1]]).padStart(2,'0')}-${String(x[2]).padStart(2,'0')}`:''; };
const safe=s=>s.replace(/[\\/:*?"<>|]+/g,'').replace(/\s+/g,'_').slice(0,120);

window.__bbIndex = async (since='2025-01-01') => {
  const doc=new DOMParser().parseFromString(await fetch(ORG).then(r=>r.text()),'text/html');
  const meetings=[...doc.querySelectorAll('#PublicMeetingsTable tbody tr')].map(tr=>{ const tds=tr.querySelectorAll('td');
    const head=tds[0].querySelector('div').innerText.trim().replace(/\s+/g,' ');
    return { id:(tr.innerHTML.match(/meeting=(\d+)/)||[])[1], head,
      type:(tds[0].innerText.match(/Meeting Type:\s*(.+)/)||[])[1]?.trim(),
      loc:(tds[1].querySelector('span[id$=description]')||{}).textContent?.trim(),
      vids:[...tds[1].querySelectorAll('a')].map(a=>a.getAttribute('href')).filter(h=>/watch\?v=|youtu\.be\//.test(h||'')),
      det:[...tds[2].querySelectorAll('a')].map(a=>({t:a.innerText.trim(),h:a.getAttribute('href')})) }; })
    .filter(m=>m.id && dateOf(m.head)>=since);
  let i=0; async function work(){ while(i<meetings.length){ const m=meetings[i++]; m.items=[];
    try{ const ad=new DOMParser().parseFromString(await fetch('/Public/Agenda/915?meeting='+m.id).then(r=>r.text()),'text/html');
      for(const a of ad.querySelectorAll('a[data-documentid], a[href*="FileViewerOrPublic"]')){
        const file=a.getAttribute('data-documentid')||((a.getAttribute('href')||'').match(/file=(\d+)/)||[])[1]; if(!file) continue;
        const row=a.closest('tr'); const t=row?.querySelector('.form-check');
        m.items.push({file, name:a.innerText.trim(), item:(t?t.innerText:'').replace(/\s+/g,' ').trim().slice(0,200)}); }
    }catch(e){ m.err=String(e); } } }
  await Promise.all([work(),work(),work(),work()]);
  return {generated:new Date().toISOString(), source:location.origin+ORG, meetings};
};

window.__bbSaveIndex = (idx) => window.__zipdl3([{url:'data:application/json,'+encodeURIComponent(JSON.stringify(idx,null,1)), save_as:'boardbook/boardbook_index_2025_2026.json'}], 'boardbook_index.zip', 1);

window.__bbFetch = async (idx, opts={}) => {
  window.__bbstat={running:true, res:[]};
  const ms=idx.meetings.filter(m=>!opts.only || opts.only.includes(m.id));
  for(const m of ms){
    const dir='boardbook/meetings/'+window.__bbDir(m.head,m.id)+'/'; const items=[];
    items.push({url:'/Public/Agenda/915?meeting='+m.id, save_as:dir+'agenda.html', title:'agenda'});
    for(const [kind,path] of [['minutes','/Public/Minutes/915?meeting='],['public_notice','/Public/PublicNotice/915?meeting='],['supplementals','/Meeting/Supplementals/915?meeting=']]){
      if(!m.det.some(d=>(d.h||'').toLowerCase().includes(path.split('/')[2].toLowerCase()))) continue;
      const h=await fetch(path+m.id).then(r=>r.text());
      items.push({url:path+m.id, save_as:dir+kind+'.html', title:kind});
      const dm=h.match(/id="NewDocumentViewerDocumentID" value="(\d+)"/);
      if(dm && kind!=='supplementals') items.push({url:'/Documents/DownloadPDF/'+dm[1]+'?org=915', save_as:dir+kind+'_'+dm[1]+'.pdf', title:kind+' pdf'});
      if(kind==='supplementals'){ const sd=new DOMParser().parseFromString(h,'text/html');
        for(const a of sd.querySelectorAll('a[href]')){ const f=((a.getAttribute('href')||'').match(/file=(\d+)/)||(a.getAttribute('href')||'').match(/\/Documents\/\w+\/(\d+)/)||[])[1];
          if(f) items.push({url:'/Documents/DownloadPDF/'+f+'?org=915', save_as:dir+'supplemental/'+f+'_'+safe(a.innerText.trim()||f)+'.pdf', title:a.innerText.trim()}); } }
    }
    for(const it of m.items) items.push({url:'/Documents/DownloadPDF/'+it.file+'?org=915', save_as:dir+'attachments/'+it.file+'_'+safe(it.name)+'.pdf', title:it.name, found_on:it.item});
    try{ window.__bbstat.res.push(await window.__zipdl3(items, 'bb_'+m.id+'.zip', 3)); }catch(e){ window.__bbstat.res.push({id:m.id, err:String(e)}); }
    await new Promise(r=>setTimeout(r,1500));
  }
  window.__bbstat.running=false; return window.__bbstat;
};
})();
