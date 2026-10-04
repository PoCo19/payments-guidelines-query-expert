const fs=require('fs'),path=require('path'),assert=require('assert');
const {chromium}=require(path.join(process.env.USERPROFILE,'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright'));
const out=path.resolve('output/midsem/evidence/simple-demo-friend');fs.mkdirSync(out,{recursive:true});
(async()=>{
 const browser=await chromium.launch({headless:true,channel:'msedge'});
 const page=await browser.newPage({viewport:{width:1000,height:1000},deviceScaleFactor:2});
 try {
  await page.goto('http://127.0.0.1:8765');
  await page.locator('#mode option[value="generate"]:not([disabled])').waitFor({state:'attached'});
  const query="Can I use UPI Tap & Pay to send money to a friend?";
  await page.locator('#question').fill(query);await page.locator('#series').selectOption('UPI');await page.locator('#mode').selectOption('generate');
  const response=page.waitForResponse(r=>r.url().endsWith('/api/answer')&&r.request().method()==='POST',{timeout:650000});
  await page.locator('#search-button').click();const r=await response;const data=await r.json();
  fs.writeFileSync(path.join(out,'answer.json'),JSON.stringify({captured_at:new Date().toISOString(),query,http_status:r.status(),response:data},null,2));
  await page.waitForFunction(()=>!document.querySelector('#search-button').disabled);
  await page.screenshot({path:path.join(out,'full-page.png'),fullPage:true});
  assert(r.ok());assert(data.claims?.length>0,'Demo produced no retained claims');
  await page.locator('#question').screenshot({path:path.join(out,'question.png')});
  await page.locator('.answer-card').screenshot({path:path.join(out,'answer.png')});
  await page.locator('.source-card').first().screenshot({path:path.join(out,'source.png')});
  console.log(JSON.stringify({query,claims:data.claims,source:data.sources[0],elapsed_ms:data.elapsed_ms},null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
