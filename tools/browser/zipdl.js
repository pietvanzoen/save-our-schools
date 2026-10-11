// Browser-side batch downloader used to archive public files into zip batches (run in a page on the source site).
// window.__runBatch(manifestUrl, hostList, start, count, zipName) fetches manifest entries [start, start+count)
// whose host is in hostList, and downloads one zip containing the files plus a _manifest_*.json with provenance.
(function(){
window.__crcT=(()=>{const t=new Uint32Array(256);for(let n=0;n<256;n++){let c=n;for(let k=0;k<8;k++)c=c&1?0xEDB88320^(c>>>1):c>>>1;t[n]=c>>>0;}return t;})();
window.__crc32=(u)=>{let c=0xFFFFFFFF;const t=window.__crcT;for(let i=0;i<u.length;i++)c=t[(c^u[i])&0xFF]^(c>>>8);return (c^0xFFFFFFFF)>>>0;};
window.__EXT={'application/pdf':'pdf','text/html':'html','text/csv':'csv','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':'xlsx','application/vnd.ms-excel':'xls','application/vnd.openxmlformats-officedocument.wordprocessingml.document':'docx','application/msword':'doc','application/vnd.openxmlformats-officedocument.presentationml.presentation':'pptx','image/png':'png','image/jpeg':'jpg','application/zip':'zip','text/plain':'txt','application/json':'json'};
window.__zipdl3=async(items,zipName,conc=3)=>{const enc=new TextEncoder();const results=new Array(items.length);let idx=0;
 async function worker(){while(idx<items.length){const i=idx++;const it=items[i];let path=it.save_as;
  try{const r=await fetch(it.url);const buf=new Uint8Array(await r.arrayBuffer());const ct=(r.headers.get('content-type')||'').split(';')[0].trim();const ext=window.__EXT[ct];
   if(ext){ path=path.replace(/\.[A-Za-z0-9]{1,5}$/,'')+'.'+ext; }
   results[i]={path,data:buf,status:r.status,type:ct,final:r.url,err:''};}
  catch(e){results[i]={path:path+'.FETCH_ERROR.txt',data:enc.encode('FETCH_ERROR '+e),status:-1,type:'error',final:'',err:String(e)};}}}
 await Promise.all(Array.from({length:conc},worker));
 const manifest=results.map((r,i)=>({path:r.path,url:items[i].url,final_url:r.final,status:r.status,content_type:r.type,bytes:r.data.length,error:r.err,fetched_at:new Date().toISOString(),title:items[i].title,found_on:items[i].found_on,topic:items[i].topic,priority:items[i].priority}));
 results.push({path:'_manifest_'+zipName.replace(/\.zip$/,'')+'.json',data:enc.encode(JSON.stringify(manifest,null,1))});
 const parts=[];const central=[];let off=0;
 for(const f of results){const name=enc.encode(f.path);const crc=window.__crc32(f.data);const sz=f.data.length;
  const lh=new DataView(new ArrayBuffer(30));lh.setUint32(0,0x04034b50,true);lh.setUint16(4,20,true);lh.setUint16(6,0x0800,true);lh.setUint32(14,crc,true);lh.setUint32(18,sz,true);lh.setUint32(22,sz,true);lh.setUint16(26,name.length,true);
  parts.push(new Uint8Array(lh.buffer),name,f.data);
  const ch=new DataView(new ArrayBuffer(46));ch.setUint32(0,0x02014b50,true);ch.setUint16(4,20,true);ch.setUint16(6,20,true);ch.setUint16(8,0x0800,true);ch.setUint32(16,crc,true);ch.setUint32(20,sz,true);ch.setUint32(24,sz,true);ch.setUint16(28,name.length,true);ch.setUint32(42,off,true);
  central.push(new Uint8Array(ch.buffer),name);off+=30+name.length+sz;}
 const cdSize=central.reduce((a,b)=>a+b.length,0);const end=new DataView(new ArrayBuffer(22));end.setUint32(0,0x06054b50,true);end.setUint16(8,results.length,true);end.setUint16(10,results.length,true);end.setUint32(12,cdSize,true);end.setUint32(16,off,true);
 const blob=new Blob([...parts,...central,new Uint8Array(end.buffer)],{type:'application/zip'});
 const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=zipName;document.body.appendChild(a);a.click();setTimeout(()=>URL.revokeObjectURL(a.href),120000);
 return {zip:zipName,files:results.length,mb:Math.round(blob.size/1e6),errors:manifest.filter(m=>m.status!==200).map(m=>m.url.slice(-40)+':'+m.status+':'+m.error.slice(0,60))};};
window.__runBatch=async(manifestUrl,hosts,start,count,zipName,kinds)=>{
 window.__bstat={running:true,zip:zipName};
 try{ const man=(await fetch(manifestUrl).then(r=>r.text())).split('\n').filter(Boolean).map(JSON.parse);
  const items=man.filter(x=>hosts.includes(new URL(x.url).host) && (!kinds || kinds.includes(x.kind)) && x.kind!=='external');
  window.__bstat.total=items.length;
  const r=await window.__zipdl3(items.slice(start,start+count),zipName,3); Object.assign(window.__bstat,r);
 }catch(e){ window.__bstat.err=String(e); }
 window.__bstat.running=false; return window.__bstat; };
})();
