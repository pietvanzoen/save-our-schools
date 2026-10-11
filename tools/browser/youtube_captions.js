// YouTube caption capture for PPS meeting videos. Paste into the DevTools console (or run via a browser-automation
// javascript tool) on any https://www.youtube.com/ page, in a FOREGROUND tab (background tabs throttle timers).
//
// It fetches the full timed English caption track (fmt=json3) for each video without playing the whole video:
// it navigates the YouTube SPA to the video, triggers the captions module so the player issues a signed /api/timedtext
// request (with the `pot` token), captures that URL from performance entries, forces lang=en (strips any `tlang`
// auto-translation), and re-requests it as json3.
//
// Records are stored in IndexedDB ('pps_capture') as they complete, so a page crash or reload doesn't lose work.
// Export: window.__next() returns one record per call as 'REC|<videoId>|<base64 gzip JSON>'. Save these lines to a
// text file and run: python3 tools/ingest_transcript_exports.py <file>...
//
// Usage:
//   window.__queue([["zOUH2Jq7Owo","2026-10-06|769955"], ...]);   // [videoId, "date|boardbookMeetingId"]
//   window.__q   -> progress ({running, done:[...]})
//   await window.__next()   // repeat until it returns 'NONE'
//
// Known pitfalls:
//   - Only English tracks are accepted. captionTracks[0] can be an auto-translated language (this happened once and
//     produced Arabic text), so the code explicitly picks languageCode 'en' and deletes 'tlang'.
//   - A full page reload wipes window.* helpers but not IndexedDB; re-paste this file and continue.
//   - Some videos have no captions (e.g. the Jan 30, 2026 retreat). Those are recorded with an `error` field.
(function(){
window.__sleep = ms => new Promise(r=>setTimeout(r,ms));
window.__db = () => new Promise((res,rej)=>{ const q=indexedDB.open('pps_capture',1); q.onupgradeneeded=()=>q.result.createObjectStore('t',{keyPath:'id'}); q.onsuccess=()=>res(q.result); q.onerror=()=>rej(q.error); });
window.__put = async rec => { const db=await window.__db(); await new Promise((res,rej)=>{ const tx=db.transaction('t','readwrite'); tx.objectStore('t').put(rec); tx.oncomplete=res; tx.onerror=()=>rej(tx.error); }); };
window.__all = async () => { const db=await window.__db(); return await new Promise((res,rej)=>{ const q=db.transaction('t').objectStore('t').getAll(); q.onsuccess=()=>res(q.result); q.onerror=()=>rej(q.error); }); };
window.__curVid = ()=>{ try{ return new URL(location.href).searchParams.get('v'); }catch(e){return null} };

window.__cap = async (vid) => {
  const out={id:vid, fetched_at:new Date().toISOString()};
  const app=document.querySelector('ytd-app');
  if(window.__curVid()!==vid){ app.resolveCommand({commandMetadata:{webCommandMetadata:{url:'/watch?v='+vid,webPageType:'WEB_PAGE_TYPE_WATCH',rootVe:3832}},watchEndpoint:{videoId:vid}}); }
  let mp, pr;
  for(let i=0;i<45;i++){ await window.__sleep(1000); mp=document.querySelector('#movie_player'); pr=mp?.getPlayerResponse?.(); if(window.__curVid()===vid && pr?.videoDetails?.videoId===vid) break; }
  const vd=pr?.videoDetails||{}; const mf=pr?.microformat?.playerMicroformatRenderer||{};
  const tracks=(pr?.captions?.playerCaptionsTracklistRenderer?.captionTracks||[]);
  out.meta={videoId:vd.videoId,title:vd.title,lengthSeconds:vd.lengthSeconds,author:vd.author,channelId:vd.channelId,publishDate:mf.publishDate,uploadDate:mf.uploadDate,description:vd.shortDescription,
    captionTracks:tracks.map(t=>({lang:t.languageCode,kind:t.kind||'manual',name:t.name?.simpleText,vssId:t.vssId}))};
  if(vd.videoId!==vid){ out.error='player did not load video'; return out; }
  const en=tracks.find(t=>t.languageCode==='en' && !t.kind) || tracks.find(t=>t.languageCode==='en') || tracks.find(t=>t.languageCode.startsWith('en'));
  if(!en){ out.error='no English caption track'; return out; }
  const find=()=>performance.getEntriesByType('resource').map(e=>e.name).filter(u=>u.includes('/api/timedtext')&&u.includes('v='+vid)&&u.includes('pot='));
  let urls=find();
  try{ mp.mute(); mp.loadModule('captions'); mp.setOption('captions','track',{languageCode:'en', kind:en.kind}); }catch(e){}
  for(let i=0;i<60 && !urls.length;i++){ try{ mp.mute(); }catch(e){}
    if(i%6===0){ try{ mp.seekTo(30+i*5,true); mp.playVideo(); }catch(e){}
      const cc=document.querySelector('.ytp-subtitles-button'); if(cc){ if(cc.getAttribute('aria-pressed')==='true' && i>0){ cc.click(); await window.__sleep(300);} cc.click(); }
      try{ mp.setOption('captions','track',{languageCode:'en', kind:en.kind}); }catch(e){} }
    await window.__sleep(1000); urls=find(); }
  try{ mp.pauseVideo(); }catch(e){}
  if(!urls.length){ out.error='no timedtext request captured'; return out; }
  const u=new URL(urls[urls.length-1]); u.searchParams.set('lang','en'); if(en.kind) u.searchParams.set('kind',en.kind); else u.searchParams.delete('kind'); u.searchParams.delete('tlang'); u.searchParams.set('fmt','json3');
  out.caption_kind=en.kind||'manual'; out.caption_lang='en';
  const j=await (await fetch(u.toString())).json();
  const lines=[]; for(const e of j.events||[]){ if(!e.segs) continue; const t=e.segs.map(s=>s.utf8).join('').replace(/\n/g,' ').trim(); if(!t) continue; lines.push(e.tStartMs+'\t'+(e.dDurationMs||0)+'\t'+t); }
  out.n_lines=lines.length; out.tsv=lines.join('\n');
  return out;
};

// Run a list sequentially, storing each result (success or error) in IndexedDB.
window.__queue = (list) => { window.__q={running:true, done:[]};
  (async()=>{ for(const [v,m] of list){ let r; try{ r=await window.__cap(v);}catch(e){ r={id:v,error:String(e)} }
      r.meetings=m; await window.__put(r); window.__q.done.push(v+': '+(r.error||(r.caption_lang+' '+r.n_lines+' lines'))); }
    window.__q.running=false; })();
  return 'started '+list.length; };

// Export one not-yet-exported record per call (keeps tool outputs small). Returns 'NONE' when finished.
window.__exported = window.__exported || new Set();
window.__next = async () => { const all=await window.__all(); const rec=all.find(r=>!window.__exported.has(r.id) && (r.tsv||r.error)); if(!rec) return 'NONE';
  const cs=new Blob([JSON.stringify(rec)]).stream().pipeThrough(new CompressionStream('gzip')); const buf=new Uint8Array(await new Response(cs).arrayBuffer());
  let s=''; for(let i=0;i<buf.length;i+=0x8000) s+=String.fromCharCode.apply(null,buf.subarray(i,i+0x8000));
  window.__exported.add(rec.id); return 'REC|'+rec.id+'|'+btoa(s); };
})();
