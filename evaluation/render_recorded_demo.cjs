// Render the saved genuine response at a readable width. No response text is edited.
const fs=require('fs'),path=require('path');
const {chromium}=require(path.join(process.env.USERPROFILE,'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright'));
(async()=>{
 const out=path.resolve('output/midsem/evidence/simple-demo');
 const saved=JSON.parse(fs.readFileSync(path.join(out,'answer.json'),'utf8'));
 const browser=await chromium.launch({headless:true,channel:'msedge'});
 const page=await browser.newPage({viewport:{width:900,height:1000},deviceScaleFactor:2});
 try{
  await page.goto('http://127.0.0.1:8765');await page.locator('#mode option[value="generate"]:not([disabled])').waitFor({state:'attached'});
  await page.route('**/api/answer',route=>route.fulfill({status:200,contentType:'application/json',body:JSON.stringify(saved.response)}));
  await page.locator('#question').fill(saved.query);await page.locator('#series').selectOption('UPI');await page.locator('#mode').selectOption('generate');
  await page.locator('#search-button').click();await page.locator('.answer-card').waitFor();
  await page.locator('#question').screenshot({path:path.join(out,'slide-question.png')});
  await page.locator('.answer-card').screenshot({path:path.join(out,'slide-answer.png')});
  fs.writeFileSync(path.join(out,'capture.json'),JSON.stringify({description:'App rendering of saved genuine local response at 900px viewport; no question, answer or citations edited.',source:'answer.json',captured_at:new Date().toISOString()},null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
