(function(root) {
  'use strict';
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const cite = value => '<button class="citation-button" data-citation="'+esc(value)+'">'+esc(value)+'</button>';
  function render(trace, review) {
    if (!trace.query_plan) return '';
    const plan = trace.query_plan;
    const coverage = trace.aspect_coverage || [];
    let html = '<details class="trace-box evidence-coverage"><summary>Scope and evidence coverage</summary><p>Researching for: '+esc(plan.entity || 'No specific entity selected')+'. '+esc(plan.product_filter ? 'Product filter: '+plan.product_filter+'.' : 'Searching across available products and sources.')+'</p>';
    html += '<div class="evidence-table-wrap"><table><thead><tr><th>Question aspect</th><th>Evidence located</th></tr></thead><tbody>'+coverage.map(a=>'<tr><td>'+esc(a.label)+'</td><td>'+(a.citations.length ? a.citations.map(cite).join(' ') : 'Not located — answer may be partial')+'</td></tr>').join('')+'</tbody></table></div>';
    html += '<p class="micro">These are passage-matching hints, not a completeness score or a decision about legal applicability.</p>';
    const documents = new Map();
    for (const s of trace.evidence_map || []) {
      const key = s.document_id || s.title;
      if (!documents.has(key)) documents.set(key,{...s,citations:[]});
      documents.get(key).citations.push(s.citation);
    }
    html += '<ul>'+Array.from(documents.values()).map(s=>'<li>'+esc(s.title)+' · '+esc(s.source_group)+(s.document_type && s.document_type!=='Unrecorded' ? ' · '+esc(s.document_type) : '')+'<br>'+s.citations.map(cite).join(' ')+'</li>').join('')+'</ul></details>';
    if (review?.status === 'issues_flagged') {
      html += '<details class="notice" open><summary>Possible gaps or conflicting qualifications — review needed</summary><p>These automated findings are separate from the answer and need source review.</p>'+(review.findings || []).map(f=>'<p><b>'+esc(f.kind.replaceAll('_',' '))+':</b> '+esc(f.reason)+'</p>'+f.quotes.map(q=>'<blockquote>'+cite(q.citation)+' '+esc(q.quote)+'</blockquote>').join('')).join('')+'</details>';
    } else if (review) {
      const labels = {no_additional_issue_flagged:'No additional issue flagged in the supplied evidence. This does not establish completeness.', unavailable:'Additional coverage review unavailable.', disabled:'Additional coverage review disabled.', not_needed_for_simple_scope:'Additional cross-document review not needed for this simple scope.', not_run:'Additional coverage review not run.'};
      html += '<p class="micro">'+esc(labels[review.status] || 'Coverage review status unknown.')+'</p>';
      if (review.status === 'unavailable' && review.failure_reason) html += '<details class="trace-box"><summary>Why the review was unavailable</summary><p>'+esc(review.failure_reason)+'</p><p>The failed review is not a successful completeness check.</p></details>';
    }
    return html;
  }
  function markdown(trace, review) {
    if (!trace.query_plan) return '';
    let text = '\n## Scope and evidence coverage\n\nResearching for: '+(trace.query_plan.entity || 'Unspecified')+'\n\n';
    for (const a of trace.aspect_coverage || []) text += '- '+a.label+': '+(a.citations.join(', ') || 'Not located')+'\n';
    text += '\nHeuristic passage coverage, not proof of completeness or applicability.\n';
    for (const s of trace.evidence_map || []) text += '\n'+s.citation+': '+s.title+' | '+s.source_group+' | '+s.document_type+' | page '+s.page+'\n';
    if (review) {
      text += '\nAutomated coverage review: '+review.status+'\n';
      if (review.failure_reason) text += '\nReview failure: '+review.failure_reason+'\n';
      for (const f of review.findings || []) text += '\nPOSSIBLE ISSUE ('+f.kind+'): '+f.reason+'\n'+f.quotes.map(q=>q.citation+': '+q.quote).join('\n')+'\n';
    }
    return text;
  }
  const api = {render, markdown};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.ResearchView = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
