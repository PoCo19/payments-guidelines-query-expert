const assert = require('node:assert/strict');
const {escapeWork,workDate,filterWork,renderDraft,nextAction,automatedSummary,hasCitedDraft,humanState,savedState} = require('../web/work.js');
assert.equal(escapeWork('<img onerror="x">&\''),'&lt;img onerror=&quot;x&quot;&gt;&amp;&#39;');
assert.equal(workDate(null),'Date not recorded');assert.equal(workDate('not a date'),'Date not recorded');
const rows=[{title:'Who qualifies?',kind:'query',state:'Draft'},{title:'Changed rule',kind:'impact',state:'Approved',disposition:'archived'},{title:'Old query',kind:'query',state:'Draft',disposition:'trash'}];
assert.equal(filterWork(rows,'query','WHO','Draft','active').length,1);
assert.equal(filterWork(rows,'','', '', 'archived')[0].title,'Changed rule');
assert.equal(filterWork(rows,'impact','', '', 'active').length,0);
const html=renderDraft('<script>alert(1)</script> Rule [S1].\n\nAnother [S99].',[{citation:'S1'}]);
assert(!html.includes('<script>'));assert(html.includes('data-cite="S1"'));assert(!html.includes('data-cite="S99"'));assert.equal((html.match(/<p>/g)||[]).length,2);
assert.match(nextAction({disposition:'trash'}),/Restore/);
assert.match(nextAction({state:'Needs revalidation',draft:{}}),/Regenerate/);
assert.match(nextAction({state:'Draft',draft:{text:''}}),/Generate/);
assert(automatedSummary({coverage_check:{status:'unavailable'}}).some(s=>s.includes('unavailable')));
assert(automatedSummary({coverage_check:{status:'invalid_output'}}).some(s=>s.includes('invalid output')));
assert(automatedSummary({}).some(s=>s.includes('No completeness check')));
assert(automatedSummary({warnings:['Inspect the evidence review below.']}).some(s=>s.includes('Open Technical diagnostics')));
console.log('Workbench: safe rendering, citation links, filters, dates and advisory states passed.');

assert.equal(hasCitedDraft({text:'Model unavailable',result:{sources:[{citation:'S1'}]}}),false);
assert.equal(hasCitedDraft({text:'Claim [S1]',result:{sources:[{citation:'S1'}]}}),true);
assert.equal(hasCitedDraft({text:'Claim [S1, S99]',result:{sources:[{citation:'S1'}]}}),false);
assert.match(nextAction({state:'Draft',draft:{text:'Model unavailable',result:{response_status:'model_unavailable'}}}),/Restore the model service/);

assert.equal(savedState('Draft'),'Saved');
assert.equal(humanState('Needs review'),'Awaiting human review');
assert.equal(humanState('Approved'),'Human sign-off recorded');
assert.match(nextAction({state:'Draft',draft:{text:'Claim [S1]',result:{sources:[{citation:'S1'}]}}}),/Human sign-off is optional/);
assert.match(nextAction({state:'Needs review',draft:{}}),/No one has been notified or assigned/);
assert.match(nextAction({state:'Approved',draft:{}}),/Editing clears the sign-off/);
assert.match(nextAction({state:'Needs revalidation',draft:{result:{response_status:'model_unavailable'}}}),/Sources or model settings changed/);
const fs=require('node:fs');
const htmlPage=fs.readFileSync(require('node:path').join(__dirname,'../web/work.html'),'utf8');
const optional=htmlPage.slice(htmlPage.indexOf('<details id="human-review"'),htmlPage.indexOf('<details><summary>History'));
assert(optional.includes('id="submit-work"')&&optional.includes('id="review-panel"'));
assert(optional.includes('50-case benchmark')&&optional.includes('does not notify or assign anyone'));
assert(!optional.slice(0,optional.indexOf('>')).includes(' open'));
assert(!htmlPage.slice(htmlPage.indexOf('<article id="work-detail"'),htmlPage.indexOf('<div class="detail-grid"')).includes('id="submit-work"'));
console.log('Optional human sign-off: distinct labels, preserved stale-source warning and collapsed controls passed.');

const {renderSavedDraft}=require('../web/work.js');
const savedClaim={text:'Supported fact.',sources:['S1']};
const savedResult={claims:[savedClaim],sources:[{citation:'S1'}],answer_blocks:[{type:'bullets',claims:[savedClaim]}]};
assert.match(renderSavedDraft({text:'Supported fact. [S1]',result:savedResult}),/<ul/);
assert.doesNotMatch(renderSavedDraft({text:'Human edit [S1]',result:savedResult}),/<ul/);
assert.match(renderSavedDraft({text:'Human edit [S1]',result:savedResult}),/Human edit/);
const {productNavigation}=require('../web/navigation.js');
const {defaultChangeQuestion}=require('../web/work.js');
for(const workbench of [true,false]){
 const nav=productNavigation(workbench);
 for(const label of ['Ask a question','Understand a change','Saved work','Document library','Manage library &amp; tools'])assert(nav.includes(label));
 assert(!nav.includes('Query Desk')&&!nav.includes('Overview'));
}
assert(defaultChangeQuestion().length<1000);
assert.match(defaultChangeQuestion(),/conditions and dates/);
assert(htmlPage.includes('Prepare change summary'));
assert(!htmlPage.includes('New query request'));
console.log('Product navigation and bounded default change question passed.');
