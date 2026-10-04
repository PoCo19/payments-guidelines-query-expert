const fs=require('fs'),path=require('path');
const {chromium}=require(path.join(process.env.USERPROFILE,'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright'));
(async()=>{const out=path.resolve('output/launch-v2/audit');fs.mkdirSync(out,{recursive:true});const b=await chromium.launch({headless:true,channel:'msedge'});try{
const p=await b.newPage({viewport:{width:1440,height:1000}});await p.goto('http://127.0.0.1:8766');await p.locator('#launch-list button').first().waitFor();await p.locator('#launch-list button').first().click();await p.getByRole('heading',{name:'UPI LITE · simulated pilot',exact:true}).waitFor();
for(const [name,file] of [['Overview','01-overview'],['Evidence & inputs','02-evidence'],['Readiness','03-readiness']]){await p.getByRole('button',{name,exact:true}).first().click();await p.evaluate(()=>window.scrollTo(0,0));await p.screenshot({path:path.join(out,file+'.png'),fullPage:false});}
fs.writeFileSync(path.join(out,'visible-text.txt'),await p.locator('body').innerText());
}finally{await b.close();}})().catch(e=>{console.error(e);process.exitCode=1});
