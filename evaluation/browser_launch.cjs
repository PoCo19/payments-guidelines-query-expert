/* Real Chromium smoke test, isolated synthetic database. No live workspace mutations. */
const path=require('path'),fs=require('fs'),assert=require('assert'),{spawn}=require('child_process');
const root=path.resolve(__dirname,'..'),out=path.join(root,'output','launch-validation');
const {chromium}=require(path.join(process.env.USERPROFILE,'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright'));
const base='http://127.0.0.1:8767',errors=[];
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
 fs.mkdirSync(out,{recursive:true});
 const server=spawn(path.join(root,'.venv/Scripts/python.exe'),['-B','-X','utf8','launch_app.py','--port','8767','--db',path.join(out,'browser-'+Date.now()+'.sqlite3')],{cwd:root,windowsHide:true,stdio:['ignore','pipe','pipe']});
 let logs='';server.stderr.on('data',d=>logs+=d);
 let browser;
 try{
  for(let n=0;n<30;n++){try{if((await fetch(base+'/api/launches')).ok)break;}catch{}await sleep(300);}
  browser=await chromium.launch({headless:true,channel:'msedge'});const page=await browser.newPage({viewport:{width:1440,height:1000}});
  page.on('pageerror',e=>errors.push(e.message));page.setDefaultTimeout(15000);
  await page.goto(base);await page.getByRole('heading',{name:'One shared baseline.' ,exact:false}).waitFor();
  await page.evaluate(() => window.scrollTo(0,0));await page.screenshot({path:path.join(out,'01-welcome.png'),fullPage:true});
  await page.getByRole('button',{name:'Create simulated UPI LITE pilot',exact:true}).click();
  await page.getByRole('heading',{name:'UPI LITE · simulated pilot',exact:true}).waitFor();
  const tab=async name=>{await page.getByRole('button',{name,exact:true}).first().click();};
  await tab('Feature facts');let form=page.locator('form[data-action="facts_approve"]');
  await form.getByLabel('Review note / evidence').fill('Browser test: simulated facts reviewed against the fixture.');await form.getByRole('button').click();
  await page.getByText('Approved baseline',{exact:true}).waitFor();
  await tab('Team deliverables');
  for(const team of ['cs','marketing','bd','risk']){
   await page.locator('#team-select').selectOption(team);
   await page.getByRole('button',{name:'Generate template demo',exact:true}).click();
   await page.locator('form[data-action="artifact_review"]').waitFor({timeout:20000});
   form=page.locator('form[data-action="artifact_review"]');await form.getByLabel('Review rationale and evidence').fill('Browser test review of synthetic template content.');await form.getByRole('button',{name:'Record review'}).click();
   await page.getByText('Reviewed by Demo owner',{exact:false}).waitFor();
  }
  assert((await page.locator('.metric').nth(1).innerText()).includes('4 / 4'));
  await page.evaluate(() => window.scrollTo(0,0));await page.screenshot({path:path.join(out,'02-risk-deliverable.png'),fullPage:true});
  await tab('Readiness');
  for(const team of ['risk','cs','marketing','bd']){
   form=page.locator(`form[data-action="task_save"][data-team="${team}"][data-id]:not([data-id=""])`);
   await form.locator('xpath=..').locator('summary').click();
   await form.getByLabel('Owner',{exact:true}).fill('Synthetic '+team+' owner');
   await form.getByLabel('Completion evidence / blocker details').fill('Synthetic completion evidence recorded during browser validation.');
   await form.locator('[name="status"]').selectOption('done');await form.getByRole('button',{name:'Save task'}).click();
   await page.waitForFunction(()=>document.querySelector('#message').textContent.startsWith('Saved.')&&!document.querySelector('details[open] form[data-action="task_save"]'));
  }
  await page.getByText('All configured gates are satisfied.',{exact:true}).waitFor();
  form=page.locator('form[data-action="launch_decide"]');await form.getByLabel('Review note / evidence').fill('Synthetic launch decision for the capstone browser test.');await form.getByRole('button').click();
  await page.getByText('Human decision recorded',{exact:true}).waitFor();
  await page.evaluate(() => window.scrollTo(0,0));await page.screenshot({path:path.join(out,'03-readiness.png'),fullPage:true});
  await tab('History & export');const download=page.waitForEvent('download');await page.getByRole('button',{name:'Download launch pack (.md)'}).click();
  await (await download).saveAs(path.join(out,'browser-launch-pack.md'));
  assert(fs.readFileSync(path.join(out,'browser-launch-pack.md'),'utf8').includes('SIMULATED CAPSTONE'));
  await tab('Evidence & inputs');
  form=page.locator('form[data-action="control_save"]').first();await form.locator('xpath=..').locator('summary').click();
  await form.getByLabel('Applicability / scope').fill('Changed synthetic pilot assurance scope.');await form.getByRole('button',{name:'Save control'}).click();
  await page.getByText('Launch decision pending',{exact:true}).waitFor();
  let launches=await (await fetch(base+'/api/launches')).json();let w=await(await fetch(base+'/api/launches/'+launches[0].id)).json();
  assert.equal(w.artifacts.risk.status,'stale');assert.equal(w.artifacts.marketing.status,'approved');assert.equal(w.tasks.find(t=>t.team==='bd').status,'todo');assert.equal(w.decision.status,'requires_review');
  await tab('Readiness');await page.evaluate(() => window.scrollTo(0,0));await page.screenshot({path:path.join(out,'04-change-impact.png'),fullPage:true});
  await tab('Evidence & inputs');await page.getByLabel('Search circular passages').fill('UPI lite');await page.getByRole('button',{name:'Search local collection',exact:true}).click();
  await page.locator('#evidence-results details').first().waitFor({timeout:60000});await page.locator('#evidence-results summary').first().click();await page.getByRole('button',{name:'Import this passage'}).first().click();
  await page.getByText('Evidence snapshot imported with document and page provenance.',{exact:false}).waitFor();
  w=await(await fetch(base+'/api/launches/'+launches[0].id)).json();assert(w.sources.some(s=>s.provenance?.document_id));assert(!w.facts_approved);
  await page.setViewportSize({width:390,height:844});await page.evaluate(() => window.scrollTo(0,0));await page.screenshot({path:path.join(out,'05-mobile.png'),fullPage:true});
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));assert.deepEqual(errors,[]);
  fs.writeFileSync(path.join(out,'browser-report.json'),JSON.stringify({passed:true,checks:['Create demo','Approve facts','Generate and approve four template packs','Complete tasks in dependency order','Record launch decision','Export Markdown','Change control and reopen dependent tasks','Search real UPI corpus and import provenance','390px responsive layout','No browser JavaScript errors'],errors},null,2));
  console.log('PASS: complete browser journey, export, change propagation, corpus import and responsive layout.');
 }catch(e){console.error(e);fs.writeFileSync(path.join(out,'browser-failure.log'),String(e)+'\n'+logs);process.exitCode=1;}
 finally{if(browser)await browser.close();server.kill();}
})();

