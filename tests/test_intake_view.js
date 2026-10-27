const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const elements=new Map();
function $(id){
  if(!elements.has(id))elements.set(id,{value:'',innerHTML:'',hidden:false,listeners:{},
    addEventListener(event,fn){this.listeners[event]=fn;},querySelectorAll(){return [];}});
  return elements.get(id);
}
let preview;
const errors=[];
const context=vm.createContext({$,Date,console,
  esc:value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])),
  api:async()=>preview,clearError(){},showError(message){errors.push(message);}});
vm.runInContext(fs.readFileSync(require.resolve('../web/intake.js'),'utf8'),context);
async function render(quality,validation){
  preview={release:'test-only',status:'prepared',validation,documents:[{subject:'Test document',availability:'needs_source_review',intake_quality:quality}]};
  $('#intake').listeners.click({target:{closest:()=>({dataset:{previewRelease:'test-only'},hasAttribute:()=>false})}});
  await new Promise(resolve=>setImmediate(resolve));
  assert.deepEqual(errors,[]);
  return $('#intake-candidate').innerHTML;
}
(async()=>{
  const html=await render({blocked_pages:[1],pages:[{page:1,findings:[{detail:'Damaged <script>unsafe()</script> table'}]}]});
  assert(html.includes('Quarantined pages: 1'));
  assert(html.includes('Source review: 1 flagged page(s)'));
  assert(!html.includes('<script>') && html.includes('&lt;script&gt;'));
  const reviewed=await render({blocked_pages:[],pages:[{page:2,findings:[{detail:'Verify amount'}]}]});
  assert(reviewed.includes('flags do not necessarily indicate errors'));
  assert(!(await render(undefined)).includes('Source review:'));
  const degraded=await render(undefined,{chunks:1,embeddings:{computed:1,cache_hits:0},graph_assistance:{status:'degraded',warning:'Source changed <review>'}});
  assert(degraded.includes('Graph-assisted retrieval: degraded'));
  assert(degraded.includes('Source changed &lt;review&gt;'));
  console.log('Intake UI: flagged candidate, quarantine notice, escaping and legacy candidate passed.');
})().catch(error=>{console.error(error);process.exitCode=1;});
