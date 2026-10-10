"use strict";
const Intake = (() => {
  let uploads=[],busy=false,pendingAction=null;
  const value=id=>$('#intake-'+id).value.trim();
  const progress=(message,seconds)=>{const p=$('#intake-progress');p.hidden=false;p.textContent=message+(seconds===undefined?'':' · '+Math.round(seconds)+'s');};
  async function operation(fn){
    if(busy)return;busy=true;clearError();
    $('#intake').querySelectorAll('button').forEach(b=>b.disabled=true);
    try{await fn();}catch(e){showError(e.message);progress('Stopped. Your active library has not been replaced by a failed build.');}
    finally{busy=false;$('#intake').querySelectorAll('button').forEach(b=>b.disabled=false);}
  }
  function renderUploads(){
    $('#intake-uploads').innerHTML=uploads.map(u=>'<article class="intake-item"><h3>'+esc(u.metadata.title)+'</h3><p>'+esc(u.metadata.issuer)+' · '+u.page_count+' '+(u.physical_pages?'PDF pages':'logical text pages')+'</p><p>'+esc(u.note)+'</p>'+(u.thin_pages.length?'<p class="notice">Thin or empty pages: '+u.thin_pages.join(', ')+'. '+(u.metadata.allow_partial?'Partial extraction accepted; warnings retained.':'This document will be quarantined.')+'</p>':'')+(u.duplicates.length?'<p class="notice">Duplicate source: '+u.duplicates.map(d=>esc(d.title)).join(', ')+'. Remove it from this batch.</p>':'')+u.pages.map(p=>'<details><summary>Preview page '+p.page+' · '+p.characters+' characters</summary><pre class="intake-preview">'+esc(p.text)+'</pre></details>').join('')+'<button data-remove-upload="'+u.token+'">Remove from batch</button></article>').join('');
    $('#intake-prepare-controls').hidden=!uploads.length;
    $('#intake-reviewed').checked=false;
  }
  function candidate(p){
    $('#intake-candidate').innerHTML='<article class="intake-item"><h2>Candidate library</h2><p>'+esc(p.release)+' · '+esc(p.status)+'</p>'+p.documents.map(d=>'<p>'+esc(d.subject)+' — '+esc(d.availability.replaceAll('_',' '))+'</p>').join('')+(p.validation?'<p>Validated '+p.validation.chunks+' chunks. New embeddings: '+p.validation.embeddings.computed+'; reused: '+p.validation.embeddings.cache_hits+'. Structural checks are not answer-accuracy checks.</p>':'')+(['prepared','validated'].includes(p.status)?'<button data-build-release="'+esc(p.release)+'">'+(p.status==='validated'?'Rebuild candidate':'Build index')+'</button> ':'')+(p.status==='validated'?'<button class="primary" data-activate-release="'+esc(p.release)+'">Activate reviewed version</button>':'')+'</article>';
  }
  async function refresh(){
    try{const releases=await api('/api/intake/releases');$('#intake-releases').innerHTML=releases.map(r=>'<p><button data-preview-release="'+esc(r.release)+'">'+esc(r.release)+'</button> · '+esc(r.status==='active' && !r.can_rollback?'previous activation':r.status)+(r.can_rollback?' <button data-rollback-release="'+esc(r.release)+'">Roll back this activation</button>':'')+'</p>').join('') || '<p>No intake releases yet.</p>';}
    catch(e){showError(e.message);}
  }
  $('#intake-retrieved').value=new Date().toLocaleDateString('en-CA');
  $('#intake-form').addEventListener('submit',event=>{event.preventDefault();operation(async()=>{
    const file=$('#intake-file').files[0];if(!file)throw Error('Choose a file.');
    if(uploads.length>=10)throw Error('Prepare the current batch before adding more files.');
    if(file.size>10*1024*1024)throw Error('File exceeds 10 MB.');
    const metadata={title:value('title'),issuer:value('issuer'),document_type:value('type'),reference:value('reference'),products:[...new Set(value('products').split(',').map(s=>s.trim()).filter(Boolean))],source_url:value('url'),retrieved_on:value('retrieved'),allow_partial:$('#intake-partial').checked};
    if(value('issued'))metadata.issue_date=value('issued');if(value('updated'))metadata.updated_on=value('updated');
    if(value('notes'))metadata.source_notes=[value('notes')];
    progress('Uploading and extracting preview');
    const encoded=await new Promise((resolve,reject)=>{const reader=new FileReader();reader.onload=()=>resolve(reader.result.split(',')[1]);reader.onerror=reject;reader.readAsDataURL(file);});
    uploads.push(await api('/api/intake/upload',{filename:file.name,data_base64:encoded,metadata}));renderUploads();progress('Review the extracted text below.');
  });});
  $('#intake-prepare').addEventListener('click',()=>operation(async()=>{
    if(!$('#intake-reviewed').checked)throw Error('Review the preview and check the confirmation box first.');
    const result=await LocalJob.run('/api/intake/prepare',{tokens:uploads.map(u=>u.token)},progress);
    candidate(result.preview);uploads=[];renderUploads();await refresh();progress('Candidate prepared. Build its index next.');
  }));
  $('#intake-refresh').addEventListener('click',refresh);
  $('#intake').addEventListener('click',event=>{
    const b=event.target.closest('button');if(!b)return;
    if(b.dataset.removeUpload){uploads=uploads.filter(u=>u.token!==b.dataset.removeUpload);renderUploads();}
    if(b.dataset.previewRelease)operation(async()=>candidate(await api('/api/intake/preview?release='+encodeURIComponent(b.dataset.previewRelease))));
    if(b.dataset.buildRelease)operation(async()=>{candidate(await LocalJob.run('/api/intake/build',{release:b.dataset.buildRelease},progress));await refresh();progress('Build passed. Review the result before activation.');});
    const action=b.dataset.activateRelease?'activate':b.dataset.rollbackRelease?'rollback':null;
    if(action){
      pendingAction={action,release:b.dataset.activateRelease || b.dataset.rollbackRelease};
      $('#intake-confirmation').hidden=false;
      $('#intake-confirmation').innerHTML='<p>'+(action==='activate'?'Load this validated library version for new questions?':'Restore the previous library version? Both versions will be retained.')+'</p><p>'+esc(pendingAction.release)+'</p><button class="primary" data-confirm-intake>Confirm '+action+'</button> <button data-cancel-intake>Cancel</button>';
      $('#intake-confirmation').scrollIntoView({block:'center',behavior:'smooth'});
    }
    if(b.hasAttribute('data-cancel-intake')){pendingAction=null;$('#intake-confirmation').hidden=true;}
    if(b.hasAttribute('data-confirm-intake') && pendingAction)operation(async()=>{
      const selected=pendingAction;pendingAction=null;$('#intake-confirmation').hidden=true;
      await LocalJob.run('/api/intake/'+selected.action,{release:selected.release},progress);
      window.location.reload();
    });
  });
  return {refresh};
})();
