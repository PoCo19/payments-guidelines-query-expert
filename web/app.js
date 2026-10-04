"use strict";
const $ = selector => document.querySelector(selector);
const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const pct = value => (value * 100).toFixed(0) + "%";
const availabilityName = value => ({converted:"Text available",no_public_pdf:"No public PDF",cancelled:"Cancelled",cancelled_as_listed:"Cancelled",public_link_failed:"Download failed",download_failed:"Download failed",failed_download:"Download failed"}[value] || value.replaceAll("_"," "));
const sourceURL = value => {try {const u = new URL(value); return u.protocol === "https:" ? u.href : "#";} catch {return "#";}};
let lastResult = null, stats = null, selectedDocuments = [], libraryDocs = [], libraryPage = 0;
const refLabel = d => d.reference_label || (d.circular_number ? "Reference "+d.circular_number : "Reference not verified");
function sourceNotices(warnings) {
  const standard = ["Coverage is limited to the imported snapshot.", "Imported document metadata and extraction remain unverified;", "Claims are automatically checked against cited excerpts.", "Citation IDs are validated."];
  const general = warnings.filter(w => standard.some(prefix => w.startsWith(prefix)));
  const specific = warnings.filter(w => !standard.some(prefix => w.startsWith(prefix)));
  return (specific.length ? '<div class="notice">'+specific.map(esc).join('<br>')+'</div>' : '') +
    (general.length ? '<details class="source-limitations"><summary>Source limitations — verify important details against the original</summary><p>'+general.map(esc).join('<br>')+'</p></details>' : '');
}
async function api(path, body) {
  const response = await fetch(path, body ? {method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(body)} : {});
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || "The request could not be completed.");
  return data;
}
function showError(message) {$("#global-error").textContent = message; $("#global-error").hidden = false;}
function clearError() {$("#global-error").hidden = true;}
function setView(view) {
  document.querySelectorAll(".view").forEach(el => el.hidden = el.id !== view);
  document.querySelectorAll(".nav").forEach(el => {el.classList.toggle("active", el.dataset.view === view); el.setAttribute("aria-current", el.dataset.view === view ? "page" : "false");});
  $("#view-label").textContent = {explore:"Ask a question",library:"Guideline library",experiments:"Experiments",about:"About this project",review:"Source review"}[view];
  if(view === "library") loadLibrary();
  if(view === "review") loadReview();
}
document.querySelectorAll(".nav").forEach(button => button.addEventListener("click", () => {clearError();setView(button.dataset.view);}));
const reasonLabel = value => ({document_coverage:"Document section coverage",direct_match:"Direct match",recorded_reference:"Recorded circular reference",same_feature:"Same feature (reviewed or heuristic)",adjacent_context:"Surrounding passage"}[value] || value || "Direct match");
function sourceCard(s) {
  return '<article class="source-card" id="citation-'+esc(s.citation)+'"><div class="source-top"><span class="tag">'+esc(s.citation)+' · '+esc(s.series)+' · '+esc(refLabel(s))+'</span><span>'+esc(s.issue_date || "Date unknown")+'</span></div><h3>'+esc(s.title)+'</h3><p class="retrieval-reason">'+esc(reasonLabel(s.retrieval_reason))+(s.via_document_id ? ' · via '+esc(s.via_document_id) : '')+'</p><p class="micro">'+esc(s.section_heading || 'Source passage')+(s.clause_label ? ' · clause marker '+esc(s.clause_label) : '')+'</p><blockquote>'+esc(s.text)+'</blockquote><div class="source-actions"><button data-document="'+esc(s.document_id)+'" data-page="'+s.page+'">Read page '+s.page+' ↗</button><a target="_blank" rel="noopener" href="'+esc(sourceURL(s.source_url))+'#page='+s.page+'">Official PDF ↗</a><button data-document="'+esc(s.document_id)+'">Related circulars ↗</button></div><p class="quality">'+(s.needs_priority_review ? "Priority review · " : "")+esc(s.method || "Extraction")+" · "+esc((s.review_status || "Not verified word for word").replaceAll("_"," "))+'</p></article>';
}
$("#search-form").addEventListener("submit", async event => {
  event.preventDefault(); clearError();
  const button = $("#search-button"); button.disabled = true;
  const started = Date.now();
  const updateProgress = () => {button.textContent = ($("#mode").value === "generate" ? "Preparing local AI draft" : "Finding evidence") + " · " + Math.round((Date.now()-started)/1000) + "s";};
  updateProgress();
  const progressTimer = setInterval(updateProgress, 1000);
  const query = $("#question").value.trim();
  const request = {query,answer_style:$("#answer-style").value,fiscal_year:$("#fiscal-year").value,document_ids:selectedDocuments.map(d=>d.id),method:$("#method").value,series:$("#series").value,cutoff:$("#cutoff").value,mode:$("#mode").value,scope:$("#scope").value,feature:$("#feature").value,route:$("#route").value,rerank:$("#rerank").value === "true"};
  const methodLabel = $("#method").selectedOptions[0].textContent;
  $("#results").innerHTML = ""; lastResult = null;
  $("#empty-state").hidden = true;
  try {
    const result = await api("/api/answer", request);
    lastResult = {...request,...result};
    const formattedAnswer = AnswerFormat.renderHTML(result);
    $("#results").innerHTML = '<div class="results-head"><h2>'+(result.mode === "generate" ? "Answer and sources" : "Source passages")+'</h2><button class="subtle-button" id="export">Export notes ↓</button></div><p class="micro">'+result.sources.length+' excerpts · '+esc(methodLabel)+' · '+result.elapsed_ms+' ms</p><div class="answer-card"><p>'+esc(result.answer)+'</p>'+formattedAnswer+'</div>'+sourceNotices(result.warnings)+'<details class="trace-box"><summary>How evidence was selected</summary><p>'+esc(result.retrieval_trace.scope)+' · '+result.retrieval_trace.seed_chunk_ids.length+' direct matches · '+result.retrieval_trace.included_chunk_ids.length+' included passages · '+result.retrieval_trace.evidence_characters+'/'+result.retrieval_trace.character_budget+' budgeted characters</p><p>Reference expansion is limited to one hop. Heading and feature labels are heuristic.</p></details><div class="source-grid">'+result.sources.map(sourceCard).join("")+"</div>";
    const trace=result.retrieval_trace;
    if(trace.ambiguities?.length) $('#results .source-grid').insertAdjacentHTML('beforebegin','<div class="notice"><b>Choose the intended circular</b>'+trace.ambiguities.map(d=>'<p>'+esc(d.series)+' · '+esc(d.fiscal_year || 'Year unknown')+' · '+esc(d.title)+' <button data-document="'+esc(d.id)+'">Inspect and select</button></p>').join('')+'</div>');
    const coverage=Object.entries(trace.document_coverage || {}).map(([id,c])=>esc(id)+': '+c.included_chunks+'/'+c.total_chunks+' chunks '+(c.complete?'(all indexed text included; page count checked)':'(partial or unverified source coverage)')+(c.empty_pages?.length ? ' · Missing source pages: '+c.empty_pages.join(', ') : '')).join('<br>');
    $('#results .source-grid').insertAdjacentHTML('beforebegin','<details class="trace-box"><summary>Routing, coverage & claim checks</summary><p>Route: '+esc(trace.route || 'legacy')+' · Reranked candidates: '+(trace.reranker?.candidate_count || 0)+' · '+(trace.reranker?.elapsed_ms || 0)+' ms</p><p>'+coverage+'</p><p>Claim checker: '+result.claim_checks.length+' claims checked. Automated support is not expert verification.</p>'+result.claim_checks.map(c=>'<p>Draft claim '+(c.claim_index+1)+' · '+esc(c.status)+'<br>'+c.reasons.map(esc).join('; ')+'</p>'+c.quotes.map(q=>'<blockquote>'+esc(q.citation)+': '+esc(q.quote)+'</blockquote>').join('')).join('')+'</details>');
    if(result.flagged_claims.length) $('#results .source-grid').insertAdjacentHTML('beforebegin','<details class="notice"><summary>'+result.flagged_claims.length+' draft claims withheld for review</summary><p>These statements are not part of the supported answer.</p>'+result.flagged_claims.map(c=>'<p><b>'+esc(c.support_status)+'</b>: '+esc(c.text)+'<br>'+c.review_reasons.map(esc).join('; ')+'</p>').join('')+'</details>');
    $("#export").addEventListener("click", exportNotes);
  } catch (err) {showError(err.message); $("#empty-state").hidden = false;}
  finally {clearInterval(progressTimer);button.disabled = false; updateAskButton();}
});
document.querySelectorAll("[data-question]").forEach(button => button.addEventListener("click", () => {selectedDocuments=[];renderSelection();$("#question").value = button.dataset.question;$("#search-form").requestSubmit();}));
function updateAskButton() { $("#search-button").innerHTML = ($("#mode").value === "generate" ? "Ask question" : "Find passages") + ' <span>↗</span>'; }
$("#mode").addEventListener("change", () => {updateAskButton();$("#answer-style").disabled = $("#mode").value !== "generate";$("#mode-tag").textContent = $("#mode").value === "generate" ? "DRAFT AI ANSWER" : "SOURCE SEARCH";});
function exportNotes() {
  if (!lastResult) return;
  let output = "# Payments Guidelines Query Expert — research notes\n\nQuestion: "+lastResult.query+"\n\nMode: "+lastResult.mode+"; retrieval: "+lastResult.method+"\nProduct: "+(lastResult.series || "All")+"; issued by: "+(lastResult.cutoff || "No cutoff")+"\nEvidence scope: "+lastResult.scope+"; feature: "+(lastResult.feature || "All")+"\nCorpus fingerprint: "+stats.fingerprint+"\n\n"+lastResult.answer+"\n\n";
  output += "Fiscal year: "+(lastResult.fiscal_year || "All")+"\nSelected document IDs: "+(lastResult.document_ids || []).join(", ")+"\n\n";
  output += "Answer style: "+lastResult.answer_style+"\n\n"+AnswerFormat.toMarkdown(lastResult)+"\n";
  output += "\nQuestion route: "+(lastResult.retrieval_trace.route || "legacy")+"\nClaim checks: "+lastResult.claim_checks.length+" (automated, not expert verification)\n";
  for(const c of lastResult.flagged_claims) output += "\nWITHHELD FOR REVIEW: "+c.text+" — "+c.review_reasons.join("; ")+"\n";
  output += "\nCoverage: "+JSON.stringify(lastResult.retrieval_trace.document_coverage || {})+"\n\n## Automated support checks\n\n"+lastResult.claim_checks.map(c=>"Draft claim "+(c.claim_index+1)+": "+c.status+"\n"+c.reasons.join("; ")+"\n"+c.quotes.map(q=>q.citation+": "+q.quote).join("\n")).join("\n\n");
  output += "\n## Limitations\n\n"+lastResult.warnings.map(x=>"- "+x).join("\n")+"\n\n## Evidence\n\n";
  for(const s of lastResult.sources) output += "### "+s.citation+": "+s.series+" "+refLabel(s)+", page "+s.page+"\n\n"+s.title+"\n\nIncluded because: "+reasonLabel(s.retrieval_reason)+(s.via_document_id ? "; via "+s.via_document_id : "")+"\nSection: "+(s.section_heading || "Source passage")+"; chunk ID: "+s.id+"\n\nIssued: "+s.issue_date+"; extraction: "+s.method+"; review: "+s.review_status+"\n\n"+s.text+"\n\nSource: "+s.source_url+"#page="+s.page+"\n\n";
  const url = URL.createObjectURL(new Blob([output],{type:"text/markdown;charset=utf-8"}));
  const link = document.createElement("a"); link.href = url; link.download = "circular-research-notes.md"; link.click();
  setTimeout(()=>URL.revokeObjectURL(url), 1000);
}
async function loadLibrary() {
  try {
    libraryPage=0;
    const params = new URLSearchParams({series:$("#library-product").value,fiscal_year:$("#library-year").value,query:$("#library-query").value,availability:$("#availability").value});
    const docs = await api("/api/library?"+params);
    libraryDocs=docs;renderLibrary();
  } catch(err) {showError(err.message);}
}
function renderLibrary(){
    $("#library-count").textContent = libraryDocs.length+" entries · sorted by issue date · unknown dates appear last";
    $("#library-list").innerHTML = libraryDocs.slice(libraryPage*50,libraryPage*50+50).map(d=>'<article class="library-row"><span class="library-number">'+esc(d.series)+'<br>'+esc(refLabel(d))+'</span><div class="library-detail"><h3>'+esc(d.subject)+'</h3><p>'+esc(d.issue_date || "Issue date unknown")+(d.listed_update_date ? " · Public version updated "+esc(d.listed_update_date) : "")+'</p></div><span class="tag '+(d.availability !== "converted" ? "warn" : "")+'">'+esc(availabilityName(d.availability))+'</span><button class="subtle-button" data-document="'+esc(d.id)+'">Open ↗</button></article>').join("") || '<div class="notice">No entries match this search.</div>';

 $('#library-page').textContent='Page '+(libraryPage+1)+' of '+Math.max(1,Math.ceil(libraryDocs.length/50));
 $('#library-prev').disabled=libraryPage===0;$('#library-next').disabled=(libraryPage+1)*50>=libraryDocs.length;
}
$('#library-prev').addEventListener('click',()=>{libraryPage--;renderLibrary();});
$('#library-next').addEventListener('click',()=>{libraryPage++;renderLibrary();});
$("#library-form").addEventListener("submit", event => {event.preventDefault();clearError();loadLibrary();});
let readerRequest = 0;
async function readDocument(id, page) {
  const request = ++readerRequest;
  $("#reader-content").textContent = "Loading source…";
  if(!$("#reader").open) $("#reader").showModal();
  try {
    const data = await api("/api/document?id="+encodeURIComponent(id));
    if(request !== readerRequest) return;
    const d = data.document;
    const missing = data.relationships.links.filter(l=>!l.available);
    const references = data.relationships.links.map(l => '<div class="source-actions"><span>'+esc(l.from_id)+' references '+esc(l.reference)+'</span>'+l.target_ids.map(target => '<button data-document="'+esc(target)+'">Open '+esc(target)+' ↗</button>').join("")+(!l.target_ids.length ? '<span class="missing">Not in this register</span>' : "")+'</div>').join("");
    $("#reader-content").innerHTML = '<h2 class="reader-title">'+esc(d.series)+' · '+esc(refLabel(d))+' — '+esc(d.subject)+'</h2><div class="reader-meta">Issued '+esc(d.issue_date || "date unknown")+' · '+esc(availabilityName(d.availability))+'<br>Public version update: '+esc(d.listed_update_date || "Not separately recorded")+' · Effective date: '+esc(d.effective_date || 'Not reviewed / extracted')+'</div>'+
      '<p class="micro">Products: '+esc((d.product_memberships || [d.series]).join(', '))+' · Fiscal year: '+esc(d.fiscal_year || 'Not recorded')+' · '+esc(d.metadata_quality || 'Existing metadata')+'</p>'+
      (d.availability==='converted' ? '<div class="source-actions"><button data-select-circular="'+esc(d.id)+'" data-selection-mode="summary">Summarise this circular</button><button data-select-circular="'+esc(d.id)+'" data-selection-mode="compare">Add to comparison</button></div>' : '')+
      (data.source_coverage.empty_pages.length ? '<div class="notice">Missing extracted text on source pages: '+data.source_coverage.empty_pages.join(', ')+'. Full-source coverage is incomplete.</div>' : '')+
      (!data.source_coverage.page_count_verified ? '<p class="notice">Original PDF page count is unverified.</p>' : '')+
      (d.source_pdf ? '<div class="source-actions"><a href="'+esc(sourceURL(d.source_pdf))+'" target="_blank" rel="noopener">Official PDF ↗</a>'+(d.local_pdf ? '<a href="/api/pdf?id='+encodeURIComponent(d.id)+'" target="_blank" rel="noopener">Saved original PDF ↗</a>' : '<span>Original PDF not saved locally</span>')+'</div>' : "")+
      '<h3>Related-document timeline</h3><p class="micro">'+esc(data.relationships.note)+'</p><div class="timeline">'+data.relationships.documents.map(x=>'<button class="'+(x.id===d.id?"current":"")+'" data-document="'+esc(x.id)+'">'+esc(x.series)+' · '+esc(refLabel(x))+'<small>'+esc(x.issue_date || "Date unknown")+'</small><small>'+esc(availabilityName(x.availability))+'</small></button>').join("")+'</div>'+
      (references ? '<details><summary>Recorded references</summary>'+references+'</details>' : "")+
      (missing.length ? '<p class="missing">Referenced text unavailable in this collection: '+missing.map(l=>esc(l.reference)).join(", ")+".</p>" : "")+
      '<details class="index-audit"><summary>Indexed chunks & reference provenance ('+data.chunks.length+' chunks)</summary><p class="micro">Features: '+esc(data.features.join(', ') || 'No title-derived label')+'. See each chunk for label review provenance. Word offsets are zero-based, end-exclusive within a source page.</p>'+data.reference_edges.map(e=>'<p class="micro">'+esc(e.from_id)+' '+esc(e.relation)+' '+esc(e.reference)+' → '+esc(e.target_id || 'Unresolved')+' · '+esc(e.status)+' · '+esc(e.evidence_status)+' · '+esc(e.basis)+' · evidence pages: '+esc(e.evidence_pages.join(', ') || 'none')+'</p>').join('')+data.chunks.map(c=>'<details><summary>Page '+c.page+' · '+esc(c.section_heading || 'Source passage')+' · clause '+esc(c.clause_label || 'unlabelled')+' · '+c.text.split(/\s+/).length+' words</summary><p class="micro">'+esc(c.id)+'<br>Words '+c.start_word+'–'+c.end_word+' · section '+esc(c.section_id)+'<br>Features: '+esc(c.feature_ids.join(', '))+' · '+esc(c.feature_basis)+'<br>Participants: '+esc((c.roles || []).join(', '))+' · '+esc(c.role_basis)+'<br>Previous: '+esc(c.previous_chunk_id || 'none')+'<br>Next: '+esc(c.next_chunk_id || 'none')+'</p><pre>'+esc(c.text)+'</pre></details>').join('')+'</details>'+
      (d.notes?.length ? '<div class="notice">'+d.notes.map(esc).join("<br>")+"</div>" : "")+
      (data.pages.length ? data.pages.map(p=>'<section class="reader-page" id="reader-page-'+p.source_page+'"><h3>Source page '+p.source_page+' <span class="tag '+(p.needs_priority_review?"warn":"")+'">'+esc(p.method)+(p.needs_priority_review?" · Priority review":"")+'</span></h3><p class="micro">'+esc((p.review_status || "Not verified word for word").replaceAll("_"," "))+'</p><pre>'+esc(p.text || '[No extracted text for this source page]')+'</pre>'+(p.corrections?.length ? '<details><summary>'+p.corrections.length+' source-checked corrections — original text</summary><p>'+p.corrections.map(r=>esc(r.before)+' → '+esc(r.after)+' · '+esc(r.reviewer_kind)).join('<br>')+'</p><pre>'+esc(p.original_text)+'</pre></details>' : '')+'</section>').join("") : '<div class="notice">This entry has no converted text. Its requirements cannot be inferred from the title or related circulars.</div>');
    $("#reader").scrollTop = 0;
    if(page) $("#reader-page-"+page)?.scrollIntoView({block:"start"});
  } catch(err) {$("#reader-content").textContent = err.message;}
}
document.addEventListener("click", event => {
  const documentButton = event.target.closest("[data-document]");
  if(documentButton) readDocument(documentButton.dataset.document, documentButton.dataset.page);
  const citation = event.target.closest("[data-citation]");
  if(citation) $("#citation-"+citation.dataset.citation)?.scrollIntoView({block:"center",behavior:"smooth"});
});
$("#close-reader").addEventListener("click", () => $("#reader").close());
$("#evaluate").addEventListener("click", async () => {
  clearError(); $("#evaluate").disabled = true; $("#evaluation").textContent = "Running checks…";
  try {
    const result = await api("/api/evaluation?method="+encodeURIComponent($("#evaluation-method").value));
    $("#evaluation").innerHTML = '<div class="metrics"><div class="metric"><strong>'+pct(result.hit_rate)+'</strong><span>Smoke checks passed</span></div><div class="metric"><strong>'+result.mrr.toFixed(2)+'</strong><span>Mean reciprocal rank</span></div><div class="metric"><strong>'+pct(result.mean_document_recall)+'</strong><span>Expected-document recall</span></div></div><p class="micro">'+result.cases+' cases · up to '+result.k+' chunks · normally max 2 chunks per document (single-circular queries can use all six) · positive cases only for recall and MRR</p><div class="table-wrap"><table><thead><tr><th>Question</th><th>Expected</th><th>Outcome</th></tr></thead><tbody>'+result.rows.map(r=>'<tr><td>'+esc(r.query)+(r.cutoff?"<br>Issued by "+esc(r.cutoff):"")+'</td><td>'+esc(r.expected_documents.join(", ") || "No retrieved evidence")+'</td><td class="'+(r.hit?"pass":"fail")+'">'+(r.hit?"Pass":"Review")+'</td></tr>').join("")+'</tbody></table></div>';
  } catch(err) {$("#evaluation").textContent = "";showError(err.message);}
  finally {$("#evaluate").disabled = false;}
});
async function init() {
  try {
    stats = await api("/api/stats");
    $("#nav-count").textContent = stats.documents;
    $("#collection-snapshot").textContent = stats.snapshot+". "+stats.window;
    $("#stats").innerHTML = '<div class="stat"><strong>'+stats.converted+'</strong><p><b>Source documents</b><br>Converted & indexed</p></div><div class="stat"><strong>'+stats.pages+'</strong><p><b>Source pages</b><br>Traceable evidence</p></div><div class="stat"><strong>'+(stats.documents-stats.converted)+'</strong><p><b>Collection gaps</b><br>Explicitly recorded</p></div>';
    for(const feature of (stats.features || [])) $("#feature").add(new Option(feature.label,feature.id));
    for(const name of Object.keys(stats.series).sort()) {$("#series").add(new Option(name,name));$("#library-product").add(new Option(name,name));}
    for(const year of (stats.fiscal_years || [])) {$("#fiscal-year").add(new Option(year,year));$("#library-year").add(new Option(year,year));}
    $("#availability").replaceChildren(new Option("All entries", ""));
    for(const value of Object.keys(stats.availability).sort()) $("#availability").add(new Option(availabilityName(value),value));
    if(stats.vector_ready) {for(const method of ["vector","hybrid"]) {const option = $('#method option[value="'+method+'"]');option.disabled = false;option.textContent = method === "vector" ? "Neural · embeddings" : "Hybrid · RRF";}}
    if(stats.generation_configured) {const option = $('#mode option[value="generate"]');option.disabled = false;option.textContent = "Cited AI answer";}
    if(stats.vector_ready) {
      $("#method").value = "hybrid";
      for(const option of $("#evaluation-method").options) option.disabled = false;
    }
    if(stats.generation_configured) {$("#mode").value = "generate";$("#mode-tag").textContent = "DRAFT AI ANSWER";}
    updateAskButton();
    $("#answer-style").disabled = $("#mode").value !== "generate";
    $("#rerank").value = stats.reranker_enabled ? "true" : "false";
    $("#model-status").textContent = "Generation model: "+(stats.generation_model || "Not configured")+". Storage: "+stats.vector_backend+". Chunking: "+stats.chunker_version+". Neural index: "+stats.vector_status+". "+stats.chunks+" page-bounded chunks.";
  } catch(err) {showError(err.message);}
}
init();

let reviewHash = '', reviewLoaded = '';
async function loadReview() {
  try {
    const data=await api('/api/review');
    $('#review-summary').textContent=data.pages.length+' pages flagged · '+data.metadata_gaps.length+' register entries with missing metadata · '+data.annotations.length+' annotations';
    $('#review-queue').innerHTML='<details open><summary>Page review queue</summary>'+data.pages.map(p=>'<p>'+esc(p.document_id)+' · page '+p.page+' · '+p.reasons.map(esc).join(', ')+' · '+p.corrections+' corrections <button class="subtle-button" data-document="'+esc(p.document_id)+'" data-page="'+p.page+'">Inspect source</button></p>').join('')+'</details>';
    $('#review-queue').insertAdjacentHTML('beforeend','<details><summary>Register metadata gaps</summary>'+data.metadata_gaps.map(g=>'<p>'+esc(g.document_id)+' · '+g.fields.map(esc).join(', ')+'</p>').join('')+'</details>');
    $('#review-records').innerHTML=data.annotations.map(r=>'<p><b>'+esc(r.kind)+' / '+esc(r.status)+'</b> · '+esc(r.document_id)+' p'+r.page+' · '+esc(r.reviewer_kind)+'<br>'+esc(r.before || r.anchor || '')+' → '+esc(r.after || r.value || r.relation || (r.feature_ids || []).join(', '))+'</p>').join('');
  } catch(err){showError(err.message);}
}
$('#refresh-review').addEventListener('click',loadReview);
$('#load-review-source').addEventListener('click',async()=>{
  reviewHash='';reviewLoaded='';
  try {
    const id=$('#review-doc').value.trim(),page=Number($('#review-page').value);
    const data=await api('/api/document?id='+encodeURIComponent(id));
    const p=data.pages.find(p=>p.source_page===page);if(!p)throw new Error('Page not found');
    const bytes=new TextEncoder().encode(p.original_text || p.text);
    reviewHash=Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',bytes))).map(x=>x.toString(16).padStart(2,'0')).join('');reviewLoaded=id+':'+page;
    $('#review-source-status').textContent='Loaded '+reviewLoaded+'. Inspect its PDF before accepting a correction. Source hash: '+reviewHash;
  }catch(err){showError(err.message);}
});
$('#review-form').addEventListener('submit',async event=>{
  event.preventDefault();clearError();
  try {
    const kind=$('#review-kind').value,document_id=$('#review-doc').value.trim(),page=Number($('#review-page').value);
    if(!reviewHash || reviewLoaded!==document_id+':'+page)throw new Error('Load the selected source first.');
    const split=value=>value.split(',').map(s=>s.trim()).filter(Boolean);
    const payload={kind,document_id,page,source_hash:reviewHash,status:$('#review-status').value,reviewer:$('#reviewer').value.trim(),note:$('#review-note').value,anchor:$('#review-anchor').value};
    if(kind==='correction')Object.assign(payload,{before:payload.anchor,after:$('#review-after').value});
    if(kind==='metadata')Object.assign(payload,{field:$('#review-field').value,value:$('#review-date').value});
    if(kind==='feature')Object.assign(payload,{feature_ids:split($('#review-features').value),roles:split($('#review-roles').value)});
    if(kind==='relationship')Object.assign(payload,{target_id:$('#review-target').value.trim(),relation:$('#review-relation').value});
    const saved=await api('/api/review',payload);$('#review-result').textContent=saved.message;await loadReview();
  }catch(err){showError(err.message);}
});

function reviewFields(){
 const k=$('#review-kind').value;
 for(const [id,kind] of Object.entries({'review-after':'correction','review-field':'metadata','review-date':'metadata','review-features':'feature','review-roles':'feature','review-target':'relationship','review-relation':'relationship'})) $("#"+id).closest('label').hidden=k!==kind;
}
$('#review-kind').addEventListener('change',reviewFields);reviewFields();

function renderSelection(){
 $('#selected-documents').hidden=!selectedDocuments.length;
 $('#selected-documents').innerHTML='<b>Selected circulars</b><p>'+selectedDocuments.map(d=>esc(d.series)+' · '+esc(d.subject)).join('<br>')+'</p><button id="clear-selection">Clear selection</button>';
 $('#clear-selection')?.addEventListener('click',()=>{selectedDocuments=[];renderSelection();});
}
$('#question').addEventListener('input',()=>{selectedDocuments=[];renderSelection();});
document.addEventListener('click',async event=>{
 const button=event.target.closest('[data-select-circular]');if(!button)return;
 try{
  const data=await api('/api/document?id='+encodeURIComponent(button.dataset.selectCircular));
  if(button.dataset.selectionMode==='summary')selectedDocuments=[data.document];
  else if(!selectedDocuments.some(d=>d.id===data.document.id)) {
   if(selectedDocuments.length>=4)throw new Error('Select up to four circulars.');selectedDocuments.push(data.document);
  }
  $('#reader').close();setView('explore');$('#series').value='';$('#fiscal-year').value='';$('#cutoff').value='';$('#feature').value='';$('#route').value='auto';
  $('#question').value=selectedDocuments.length>1?'Compare the selected circulars and attribute each requirement to its source.':'Summarise the selected circular, covering its sections.';
  renderSelection();
 }catch(err){showError(err.message);}
});
