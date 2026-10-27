(function(root) {
  'use strict';
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const cite = value => '<button class="citation-button" data-citation="'+esc(value)+'">'+esc(value)+'</button>';
  function answerNotice(result) {
    if (result.response_status === 'incomplete' && result.claims?.length)
      return 'This answer may be incomplete. Evidence checks found a possible gap in support, scope or qualifications; inspect the sources and the details below.';
    if (result.response_status === 'draft' && result.claims?.length)
      return 'AI-generated answer with source citations. Check the evidence before relying on it for a decision.';
    return result.answer || '';
  }
  function checkLabel(status) {
    return {
      issues_flagged:'Possible evidence gaps or conflicting qualifications found.',
      no_additional_issue_flagged:'No additional issue flagged in the supplied evidence. This does not establish completeness.',
      unavailable:'Completeness check unavailable; omissions have not been checked.',
      invalid_output:'Completeness check returned invalid output; no conclusion is available.',
      disabled:'Completeness check disabled.',
      not_needed_for_simple_scope:'Additional cross-document check not needed for this scope.',
      not_run:'Completeness check not run.'
    }[status] || (status ? 'Completeness check status unknown; inspect diagnostics.' : 'No completeness check is recorded.');
  }
  function progressLabel(stage) {
    return {'Preparing cited draft':'Preparing answer', 'Reviewing scope and omissions':'Checking evidence coverage'}[stage] || stage;
  }
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
      html += '<details class="notice" open><summary>Evidence limitations — possible gaps or conflicting qualifications</summary><p>Automatic checks flagged these points. Compare them with the sources; this is not a request sent to a human reviewer.</p>'+(review.findings || []).map(f=>'<p><b>'+esc(f.kind.replaceAll('_',' '))+':</b> '+esc(f.reason)+'</p>'+f.quotes.map(q=>'<blockquote>'+cite(q.citation)+' '+esc(q.quote)+'</blockquote>').join('')).join('')+'</details>';
    } else if (review) {
      html += '<p class="micro">'+esc(checkLabel(review.status))+'</p>';
      if (review.failure_reason) html += '<details class="trace-box"><summary>Why the check could not complete</summary><p>'+esc(review.failure_reason)+'</p><p>An unsuccessful check does not establish completeness.</p></details>';
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
      text += '\nAutomated completeness check: '+review.status+'\n';
      if (review.failure_reason) text += '\nCheck failure: '+review.failure_reason+'\n';
      for (const f of review.findings || []) text += '\nPOSSIBLE ISSUE ('+f.kind+'): '+f.reason+'\n'+f.quotes.map(q=>q.citation+': '+q.quote).join('\n')+'\n';
    }
    return text;
  }
  const api = {render, markdown, answerNotice, checkLabel, progressLabel};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.ResearchView = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
