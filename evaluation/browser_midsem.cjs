const fs=require('fs'),path=require('path'),assert=require('assert');
const {chromium}=require(path.join(process.env.USERPROFILE,'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright'));
const out=path.resolve(process.env.MIDSEM_BROWSER_OUT || 'output/midsem/evidence/browser-query-expert');fs.mkdirSync(out,{recursive:true});
(async()=>{
 const browser=await chromium.launch({headless:true,channel:'msedge'});
 const page=await browser.newPage({viewport:{width:1440,height:1000},acceptDownloads:true});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));const checks=[];
 const shot=async(name)=>page.screenshot({path:path.join(out,name+'.png'),fullPage:false});
 async function ask(query,series='UPI',mode='evidence'){
  await page.locator('[data-view="explore"]').click();
  await page.locator('#question').fill(query);await page.locator('#series').selectOption(series);
  await page.locator('#mode').selectOption(mode);
  const response=page.waitForResponse(r=>r.url().endsWith('/api/answer')&&r.request().method()==='POST',{timeout:650000});
  await page.locator('#search-button').click();const r=await response;const data=await r.json();
  await page.waitForFunction(()=>!document.querySelector('#search-button').disabled);
  return data;
 }
 try{
 await page.goto('http://127.0.0.1:8765');await page.locator('#method option[value="hybrid"]:not([disabled])').waitFor({state:'attached'});
 assert((await page.locator('.intro').first().innerText()).includes('Initial corpus: NPCI'));
 assert.equal(await page.title(),'Payments Guidelines Query Expert');
 assert(await page.locator('#search-button').isVisible());
 assert.equal(await page.locator('#search-button').innerText(),'Ask question ↗');
 assert(!(await page.locator('#stats').isVisible()));
 assert(!(await page.locator('#method').isVisible()));
 await page.locator('.advanced-settings summary').click();
 assert(await page.locator('#method').isVisible());
 await page.locator('.advanced-settings summary').click();
 assert.equal(await page.locator('a[href*="8766"]').count(),0);await shot('01-home');checks.push('payments positioning and separate scope');
 let r=await ask('Under UPI OC 186A, who checks enablement before each transaction? Answer briefly.','UPI','generate');
 assert(r.claims.length>0);assert(r.sources.every(s=>s.product_memberships.includes('UPI')));
 fs.writeFileSync(path.join(out,'answer.json'),JSON.stringify(r,null,2));
 await page.locator('#results').scrollIntoViewIfNeeded();await shot('02-answer');checks.push('actual local answer and UPI filter');
 await page.locator('.source-actions button[data-page]').first().click();await page.locator('.reader-title').waitFor();await shot('03-source');
 assert((await page.locator('#reader-content').innerText()).includes('Source page'));await page.locator('#close-reader').click();checks.push('source reader');
 const download=page.waitForEvent('download');await page.locator('#export').click();const d=await download;await d.saveAs(path.join(out,'research-notes.md'));
 assert(fs.readFileSync(path.join(out,'research-notes.md'),'utf8').includes('S1'));checks.push('Markdown export retains citations');
 r=await ask('Summarise UPI OC 186A');assert.equal(r.retrieval_trace.route,'summary');assert(r.sources.length);checks.push('summary');
 r=await ask('Compare UPI OC 186 and OC 186A');assert.equal(r.retrieval_trace.route,'compare');assert.equal(new Set(r.sources.map(s=>s.document_id)).size,2);checks.push('comparison includes both documents');
 r=await ask('What does OC 13 require?','');assert(r.retrieval_trace.ambiguities.length);checks.push('ambiguous reference selection');
 r=await ask('What does UPI OC 999 require?');assert(r.abstained&&!r.sources.length);checks.push('unavailable evidence abstention');
 r=await ask('Summarise AePS OC 33 FY 2018-19','AePS');assert(Object.values(r.retrieval_trace.document_coverage).some(c=>!c.complete));checks.push('partial extraction warning');
 // Simulate the documented HTTP outage contract, without stopping the user's Ollama service.
 await page.route('**/api/answer',route=>route.fulfill({status:503,contentType:'application/json',body:JSON.stringify({error:'Local model unavailable or timed out. Check Ollama and the configured model. Evidence search remains available.'})}));
 await ask('UPI OC 186A consent','UPI','generate');assert(await page.locator('#global-error').isVisible());assert(!(await page.locator('#search-button').isDisabled()));
 await page.unroute('**/api/answer');r=await ask('UPI OC 186A consent','UPI','evidence');assert(r.sources.length);checks.push('simulated model outage and actual evidence-search recovery');
 await page.locator('[data-view="library"]').click();await page.locator('.library-row').first().waitFor();checks.push('library loading');
 await page.locator('[data-view="about"]').click();assert(await page.locator('#stats').isVisible());checks.push('collection details in About');
 await page.locator('[data-view="explore"]').click();await page.setViewportSize({width:390,height:844});
 assert(await page.locator('#question').isVisible());
 assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
 await shot('04-mobile');checks.push('mobile layout without horizontal overflow');
 assert.equal(errors.length,0);fs.writeFileSync(path.join(out,'report.json'),JSON.stringify({passed:true,checks,errors,outage:'HTTP 503 simulated in browser; recovery used real server'},null,2));
 console.log(JSON.stringify({passed:true,checks}));
 }catch(e){await shot('failure');throw e}finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
