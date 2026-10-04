const fs=require('fs'),path=require('path'),assert=require('assert'),{spawn}=require('child_process');
const {chromium}=require(path.join(process.env.USERPROFILE,'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright'));
const root=path.resolve(__dirname,'..'),out=path.join(root,'output/launch-v2'),base='http://127.0.0.1:8767';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
 fs.mkdirSync(out,{recursive:true});const server=spawn(path.join(root,'.venv/Scripts/python.exe'),['-B','-X','utf8','launch_app.py','--port','8767','--db',path.join(out,'browser-'+Date.now()+'.sqlite3')],{cwd:root,windowsHide:true,stdio:['ignore','pipe','pipe']});
 let browser,page,logs='',errors=[];server.stderr.on('data',d=>logs+=d);
 try{
  for(let i=0;i<30;i++){try{if((await fetch(base+'/api/launches')).ok)break;}catch{}await sleep(200);}
  browser=await chromium.launch({headless:true,channel:'msedge'});page=await browser.newPage({viewport:{width:1440,height:1000}});page.setDefaultTimeout(15000);page.on('pageerror',e=>errors.push(e.message));
  await page.goto(base);await page.getByRole('heading',{name:'Your workspaces',exact:true}).waitFor();
  const shot=async name=>{await page.evaluate(()=>window.scrollTo(0,0));await page.screenshot({path:path.join(out,name+'.png'),fullPage:false});};
  const nav=async name=>{await page.locator('#navigation').getByRole('button',{name,exact:false}).click();};
  const dialog=()=>page.locator('#modal');
  await page.getByRole('button',{name:'New workspace',exact:true}).click();await dialog().getByLabel('Workspace name',{exact:true}).fill('Existing feature — browser test');await dialog().getByLabel('What do you want to achieve?').fill('Review feature guidance and transaction-rule applicability using synthetic evidence.');await dialog().getByRole('button',{name:'Create workspace',exact:true}).click();
  await page.getByRole('heading',{name:'Sources',exact:true}).waitFor();
  await nav('Team work');await page.getByRole('button',{name:'Review feature brief',exact:true}).waitFor();await page.getByRole('button',{name:'Review feature brief',exact:true}).click();await page.getByRole('button',{name:'Add sources',exact:true}).click();
  await page.getByRole('button',{name:'Upload document',exact:true}).click();
  const quote='Review support guidance and the applicability of transaction rules to this existing UPI feature.';
  await page.locator('#upload-file').setInputFiles({name:'feature-brief.md',mimeType:'text/markdown',buffer:Buffer.from(quote)});
  await page.getByLabel('Text to use',{exact:true}).waitFor();assert.equal(await page.getByLabel('Text to use',{exact:true}).inputValue(),quote);
  await page.getByRole('button',{name:'Add to workspace',exact:true}).click();await page.locator('.source-item summary').filter({hasText:'feature-brief.md'}).waitFor();
  await shot('01-sources');await nav('Feature brief');await page.getByRole('button',{name:'Add a fact',exact:true}).click();
  await dialog().getByLabel('Fact title',{exact:true}).fill('Review objective');await dialog().getByLabel('Fact',{exact:true}).fill(quote);await dialog().getByLabel('Exact quotation from the source').fill('An invented quotation');await dialog().getByRole('button',{name:'Save fact'}).click();
  await dialog().getByRole('alert').waitFor();assert(await dialog().getByRole('alert').isVisible());assert.equal(await dialog().getByLabel('Fact title',{exact:true}).inputValue(),'Review objective');await shot('02-inline-error');
  await dialog().getByLabel('Exact quotation from the source').fill(quote);await dialog().getByRole('button',{name:'Save fact'}).click();await dialog().waitFor({state:'hidden'});
  await page.locator('form[data-action="facts_approve"]').getByLabel('Review note').fill('Synthetic source reviewed during browser validation.');await page.getByRole('button',{name:'Approve brief & continue'}).click();await page.getByRole('heading',{name:'Team work',exact:true}).waitFor();
  await page.locator('#draft-mode').selectOption('template');await page.getByRole('button',{name:'Prepare all team drafts'}).click();await page.waitForFunction(()=>document.querySelectorAll('.team-switcher .status.draft').length===4,{},{timeout:20000});
  for(const label of ['Customer Success','Marketing','Partners & BD','Transaction Risk']){
   await page.locator('.team-switcher').getByRole('button',{name:label,exact:false}).click();
   if(label==='Transaction Risk')await page.getByRole('button',{name:'Assessment',exact:false}).click();
   const review=page.locator('form[data-action="artifact_review"]');await review.getByLabel('Review note').fill('Reviewed synthetic template output.');await review.getByRole('button',{name:'Record team review'}).click();await page.getByRole('heading',{name:'Team review recorded'}).waitFor();
  }
  await shot('03-team-work');await nav('Actions & review');
  let state=(await(await fetch(base+'/api/launches')).json())[0];let w=await(await fetch(base+'/api/launches/'+state.id)).json();
  for(const task of w.tasks){await page.locator(`[data-edit-task="${task.id}"]`).click();await dialog().getByLabel('Owner',{exact:true}).fill('Synthetic reviewer');await dialog().getByLabel('Completion evidence or blocker details').fill('Synthetic completed review evidence.');await dialog().getByLabel('Status',{exact:true}).selectOption('done');await dialog().getByRole('button',{name:'Save action'}).click();await dialog().waitFor({state:'hidden'});}
  await page.getByLabel('Decision and rationale').fill('Synthetic existing-feature review completed; no production deployment.');await page.getByRole('button',{name:'Complete review',exact:true}).click();await page.getByText('Review complete',{exact:true}).waitFor();await shot('04-completed-review');
  const download=page.waitForEvent('download');await page.getByRole('button',{name:'Export review pack',exact:true}).click();await(await download).saveAs(path.join(out,'browser-review.md'));
  await nav('Overview');await shot('05-overview');
  // Add a transaction rule from internal evidence and verify workflow reopening.
  await nav('Sources');await page.getByRole('button',{name:'Paste text',exact:true}).click();
  await page.getByLabel('Document title').fill('Internal example rule');await page.getByLabel('Use this document for').selectOption('risk');await page.getByLabel('Text to use').fill('Repeated attempts by the same payer are sent for review. This example rule is documented only.');await page.getByRole('button',{name:'Add to workspace',exact:true}).click();
  await nav('Team work');await page.locator('.team-switcher').getByRole('button',{name:'Transaction Risk',exact:false}).click();await page.getByRole('button',{name:'Transaction rules',exact:false}).click();await page.getByRole('button',{name:'Add transaction rule',exact:true}).click();
  await dialog().getByLabel('Rule name').fill('Payer attempt review');await dialog().getByLabel('Applies to').fill('Payer transactions for review');await dialog().getByLabel('Transaction condition').fill('Repeated payer attempts exceed the configured threshold');await dialog().getByLabel('Rule action').selectOption('review');await dialog().getByLabel('Reported status').selectOption('documented');await dialog().getByLabel('Rule owner').fill('Synthetic transaction risk team');
  w=await(await fetch(base+'/api/launches/'+state.id)).json();const ruleSource=w.sources.find(s=>s.title==='Internal example rule');await dialog().getByLabel('Supporting rule evidence').selectOption(ruleSource.id);await dialog().getByLabel('Exact quotation supporting this rule').fill(ruleSource.text);await dialog().getByRole('button',{name:'Save transaction rule'}).click();await dialog().waitFor({state:'hidden'});await page.getByRole('heading',{name:'Payer attempt review'}).waitFor();await shot('06-transaction-rules');
  await page.getByRole('button',{name:'Prepare new draft',exact:true}).first().click();await page.locator('#confirm-button').click();await page.waitForFunction(()=>document.querySelector('.team-switcher button.active .status')?.classList.contains('draft'),{},{timeout:20000});await page.getByRole('button',{name:'Assessment',exact:false}).click();await page.getByRole('heading',{name:'Rule-by-rule assessment'}).waitFor();await shot('07-rule-assessment');
  w=await(await fetch(base+'/api/launches/'+state.id)).json();assert.equal(w.decision.status,'requires_review');assert.equal(w.artifacts.risk.rule_assessments.length,1);
  // KB search/import still works after the UI redesign.
  await nav('Sources');await page.getByRole('button',{name:'UPI circulars',exact:true}).click();await page.getByLabel('Search the UPI collection').fill('UPI lite');await page.getByRole('button',{name:'Find circulars'}).click();await page.locator('.source-result').first().waitFor({timeout:60000});await page.locator('.source-result').first().getByRole('button',{name:'Add to workspace'}).click();await page.locator('.source-result').first().getByRole('button',{name:'Added to workspace'}).waitFor();
  await page.setViewportSize({width:390,height:844});await shot('08-mobile');assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  await page.setViewportSize({width:1440,height:1000});await page.getByRole('button',{name:'All workspaces',exact:true}).click();await page.getByRole('heading',{name:'Your workspaces'}).waitFor();await shot('09-workspaces');
  await page.getByRole('button',{name:'Delete',exact:true}).click();await dialog().getByLabel('Type the workspace name to confirm').fill('wrong name');await dialog().getByRole('button',{name:'Delete workspace permanently'}).click();await dialog().getByRole('alert').waitFor();await dialog().getByLabel('Type the workspace name to confirm').fill('Existing feature — browser test');await dialog().getByRole('button',{name:'Delete workspace permanently'}).click();await page.getByRole('heading',{name:'Start with a feature'}).waitFor();assert.deepEqual(await(await fetch(base+'/api/launches')).json(),[]);
  for(const purpose of ['change','new_launch']){
   const title='Purpose test '+purpose;
   await page.getByRole('button',{name:'New workspace',exact:true}).click();await dialog().locator('input[name=workspace_type][value='+purpose+']').check();await dialog().getByLabel('Workspace name',{exact:true}).fill(title);await dialog().getByLabel('What do you want to achieve?').fill('Synthetic purpose-selection validation.');await dialog().getByRole('button',{name:'Create workspace',exact:true}).click();await page.getByRole('heading',{name:'Sources',exact:true}).waitFor();
   if(purpose==='change'){
    await nav('Feature brief');await page.locator('#account-button').click();await dialog().getByLabel('Working as').selectOption('cs');await dialog().getByRole('button',{name:'Save reviewer'}).click();await page.getByRole('button',{name:'Change review role'}).click();await dialog().getByLabel('Working as').selectOption('product');await dialog().getByRole('button',{name:'Save reviewer'}).click();
   }
   await nav('Overview');await page.getByRole('button',{name:'Workspace settings'}).click();await dialog().getByRole('button',{name:'Delete workspace',exact:true}).click();
   if(purpose==='change'){
    const current=(await(await fetch(base+'/api/launches')).json())[0];
    await fetch(base+'/api/launches/'+current.id+'/actions',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({actor:'Concurrent test',role:'product',revision:current.revision,action:'brief_save',title,brief:'Changed by another tab'})});
    await dialog().getByLabel('Type the workspace name to confirm').fill(title);await dialog().getByRole('button',{name:'Delete workspace permanently'}).click();await dialog().getByRole('button',{name:'Reload delete confirmation'}).click();
   }
   await dialog().getByLabel('Type the workspace name to confirm').fill(title);await dialog().getByRole('button',{name:'Delete workspace permanently'}).click();await page.getByRole('heading',{name:'Start with a feature'}).waitFor();
  }
  assert.deepEqual(errors,[]);fs.writeFileSync(path.join(out,'browser-report.json'),JSON.stringify({passed:true,checks:['Existing-feature creation','Guided navigation to actual missing step','Markdown upload and preview','Inline quote error preserves form','Brief approval advances to team work','Atomic batch drafting','Four team reviews','Actions and final review','Export','Internal rule evidence and rule register','Rule-by-rule assessment','Change reopens review','UPI KB import','390px layout','Wrong-name deletion error and confirmed deletion','Change and new-launch creation','Role guidance leads to reviewer control','Stale deletion recovery control','No JavaScript errors'],errors},null,2));
  console.log('PASS: V2 end-to-end UI, errors, uploads, transaction rules, change propagation, corpus import and deletion.');
 }catch(e){if(page){await page.screenshot({path:path.join(out,'failure.png'),fullPage:true}).catch(()=>{});fs.writeFileSync(path.join(out,'failure-dom.txt'),await page.locator('body').innerText().catch(()=>''));}fs.writeFileSync(path.join(out,'failure.log'),String(e)+'\n'+logs);console.error(e);process.exitCode=1;}
 finally{if(browser)await browser.close();server.kill();}
})();
