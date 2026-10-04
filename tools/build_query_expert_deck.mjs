import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const ROOT=process.cwd(), BUILD=path.join(ROOT,'tmp/midsem'), OUT=path.join(ROOT,'output/midsem');
const DEP=path.join(process.env.USERPROFILE,'.cache/codex-runtimes/codex-primary-runtime/dependencies');
process.env.RUNTIME_NODE_MODULES=path.join(DEP,'node/node_modules');
const SKILL=path.join(process.env.USERPROFILE,'.codex/plugins/cache/openai-primary-runtime/presentations/26.909.12148/skills/presentations');
const {Presentation,PresentationFile}=await import(pathToFileURL(path.join(DEP,'node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs')));
const {finalizePresentation}=await import(pathToFileURL(path.join(SKILL,'container_tools/artifact_tool_utils.mjs')));
const d=JSON.parse(await fs.readFile(path.join(BUILD,'query_expert_content.json'),'utf8'));
const p=Presentation.create({slideSize:{width:1280,height:720}});
const navy='#101A2E',teal='#117D79',muted='#596C84',light='#F4F7F8';
function rect(s,x,y,w,h,fill,stroke='none'){return s.shapes.add({geometry:'rect',position:{left:x,top:y,width:w,height:h},fill,line:{fill:stroke,width:stroke==='none'?0:1}})}
function text(s,t,x,y,w,h,size=24,color=navy,bold=false,font='Inter',align='left'){
 const sh=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 sh.text=t;sh.text.style={typeface:font,fontSize:size,color,bold,alignment:align,verticalAlignment:'top',autoFit:'none',insets:{left:0,right:0,top:0,bottom:0}};return sh;
}
function base(i,title,kicker){const s=p.slides.add();s.background.fill='#FFFFFF';rect(s,0,0,1280,6,teal);text(s,title,76,56,1130,75,42,navy,false,'Georgia');if(kicker)text(s,kicker,78,141,1115,40,20,muted);text(s,'Payments Guidelines Query Expert   /   Midterm capstone',78,673,1010,22,14,muted);text(s,String(i+1).padStart(2,'0'),1160,673,50,25,16,teal,true);s.speakerNotes.textFrame.setText(d.notes[i]+'\n\nEvidence: '+d.source_paths.join('; ')+'.\nInitial corpus: NPCI circulars. Evaluation: AI-assisted UPI cases, independent review pending.');return s;}
function card(s,x,y,w,num,title,body){rect(s,x,y,w,310,light);text(s,num,x+24,y+23,w-48,40,29,teal,true);text(s,title,x+24,y+87,w-48,75,27,navy,true);text(s,body,x+24,y+175,w-48,116,23,muted);}
let s=base(0,'','');
text(s,'AI/ML in Practice  /  Midterm',80,130,1120,40,22,teal,true,'Inter','center');
text(s,'Payments Guidelines\nQuery Expert',85,218,1110,164,61,navy,false,'Georgia','center');
text(s,d.subtitle,90,424,1100,76,27,muted,false,'Inter','center');
text(s,'Initial corpus: NPCI circulars',90,508,1100,35,22,teal,true,'Inter','center');
text(s,d.team+'  |  '+d.members,90,583,1100,58,18,muted,false,'Inter','center');

s=base(1,d.titles[1],'The Why  /  For product, operations and compliance teams in banks and fintechs');
card(s,80,230,352,'01','Find the requirement','One question may span\nseveral circulars and\nlater clarifications.');
card(s,464,230,352,'02','Understand conditions','A relevant passage can\nstill omit a qualification\nelsewhere in the source.');
card(s,848,230,352,'03','Verify the answer','Users need to see which\nguideline supports each\nimportant statement.');
text(s,'Goal: reduce research effort while keeping source checking part of the task.',80,588,1120,52,25,teal);

s=base(2,d.titles[2],'A plain-language question, a cited answer and a source the user can inspect');
text(s,'QUESTION ASKED',80,196,1120,26,16,teal,true);
text(s,"Can I use UPI Tap & Pay at a shop’s card machine?",80,229,1120,49,29,navy,true);
s.images.add({blob:new Uint8Array(await fs.readFile(path.join(OUT,'evidence/simple-demo/slide-answer.png'))),contentType:'image/png',alt:'Unedited application rendering of the recorded answer with S1, S4 and S10 citations',fit:'contain',position:{left:80,top:285,width:930,height:357}});
text(s,'Follow S1',1040,311,167,40,25,teal,true);
text(s,'UPI OC 186A\nPage 1\n\nNFC means\ncontactless\ntap technology.',1040,369,167,190,21,muted);
text(s,'Also available: guideline search and inspection, summaries and document comparisons.',80,645,1120,24,17,muted);

s=base(3,d.titles[3],'The How  /  An attributed knowledge base, starting with NPCI');
rect(s,80,215,510,391,light);rect(s,634,215,566,391,light);
text(s,'From circulars to search indexes',105,239,460,77,29,teal,true);
text(s,'1  Split by page, heading and clause\n2  Long blocks: ≤220 words; 35 overlap\n3  Keep document ID, page and links\n4  Index text in BM25; vectors in Chroma',105,338,461,191,22,muted);
text(s,'Chunks never mix different circulars.',105,553,458,45,21,navy,true);
text(s,'Local model and storage stack',661,246,510,76,30,navy,true);
text(s,'Qwen3.5 9B  /  answer generation\nQwen3 embeddings  /  semantic search\nMiniLM  /  candidate reranking\nChroma + SQLite  /  vectors + metadata',661,347,512,205,23,muted);
text(s,'Imported snapshot. Missing text and uncertain dates remain visible to users.',80,627,1120,30,20,muted);

s=base(4,d.titles[4],'The How  /  Retrieval brings source evidence into the model’s context');
function flow(y,labels){labels.forEach((label,i)=>{const x=80+i*224;rect(s,x,y,190,85,light,teal);text(s,label,x+10,y+17,170,64,21,navy,true,'Inter','center');if(i<labels.length-1)s.shapes.add({geometry:'rightArrow',position:{left:x+197,top:y+31,width:22,height:20},fill:teal,line:{fill:'none',width:0}});});}
text(s,'Prepare',80,203,1120,36,24,teal,true);
flow(250,['Source text\nand inventory','Preserve document\nand page identity','Split into\nfocused chunks','Build keyword\nand vector indexes','Store metadata\nand source links']);
text(s,'Answer',80,382,1120,36,24,teal,true);
flow(429,['Question\nand filters','Retrieve and\nrank passages','Select evidence\nwithin limits','Generate answer\nand check support','Display answer\nand source links']);
text(s,'Exact search finds references; semantic search finds similar meanings.',80,553,1120,36,24,navy);
text(s,'Pretrained local models; no fine-tuning. Automated checks still need human review.',80,611,1120,32,21,muted);

s=base(5,d.titles[5],'Purpose: does more complex search find better evidence? Same 50 UPI cases and corpus.');
const values=[['Search method','Evidence found','Negatives with no result','Search time (ms)'],...d.table.slice(1)];
const t=s.tables.add({rows:5,columns:4,left:80,top:200,width:1120,height:246,columnWidths:[330,255,290,245],values});
for(let r=0;r<5;r++)for(let c=0;c<4;c++){const cell=t.getCell(r,c);cell.fill=r===0?teal:r%2?light:'#FFFFFF';cell.text.style={typeface:'Inter',fontSize:22,color:r===0?'#FFFFFF':navy,bold:r===0,verticalAlignment:'middle',insets:{left:12,right:8,top:8,bottom:8}};}
t.borders.assign({fill:'#DCE5E8',width:1,style:'solid'});
text(s,'55/55 = all expected passages found. 6/6 = no passages returned for all negative cases.',80,464,1120,33,18,muted);
text(s,'Here, BM25 found the same evidence, rejected all six negatives and was fastest.',80,510,1120,39,24,navy,true);
text(s,'Next: test harder questions to see whether hybrid search and reranking justify their cost.',80,561,1120,52,23,teal);
text(s,'Not answer accuracy. AI-assisted set; independent review pending. Many queries name circulars.\n15 coverage routes bypass reranking. Times are medians from one warmed pass, excluding answer generation.',80,618,1120,43,16,muted);

s=base(6,d.titles[6],'From a working prototype to an evaluated, repeatable local demonstration');
rect(s,80,203,1120,69,light);text(s,'NOW  ·  Cited Q&A, source reader, summaries and comparisons implemented',101,224,1080,35,23,navy,true);
const stages=[['Weeks 1–2','Validate answers','Review the 50 cases.\nFreeze unseen questions.','Reviewed test set +\nanswer-quality scorecard'],['Weeks 3–5','Improve reliability','Fix source and answer failures.\nShorten long summaries.\nCompare search settings.','Tested revision +\nquality / latency comparison'],['Weeks 6–8','Test with users','Observe research tasks.\nPackage setup and final demo.','User-task results +\nrepeatable demonstration']];
stages.forEach((v,i)=>{const x=80+i*384;text(s,v[0],x,299,355,33,20,teal,true);text(s,v[1],x,343,355,44,28,navy,true);text(s,v[2],x,411,355,119,22,muted);text(s,'DELIVERABLE',x,541,355,25,15,teal,true);text(s,v[3],x,573,355,57,22,navy);});
text(s,'Indicative weeks after midterm; reviewer access is a dependency. Another payments source is an optional later extension.',80,644,1120,25,15,muted);

s=base(7,d.titles[7],'Feedback requested on the next stage of this capstone');
const questions=[['01','Scope','Is the question-to-source workflow useful and manageable?'],['02','Evaluation','Which multi-document and missing-evidence cases should come first?'],['03','Usefulness','What task outcomes would demonstrate value to payments teams?']];
questions.forEach((q,i)=>{const y=218+i*137;text(s,q[0],80,y,70,48,33,teal,true);text(s,q[1],172,y,1020,40,28,navy,true);text(s,q[2],172,y+50,1000,59,24,muted);});
text(s,'Immediate priority: validate answers and improve failures before expanding coverage.',80,633,1120,30,21,teal);

const candidate=path.join(BUILD,'query-expert-candidate.pptx');await(await PresentationFile.exportPptx(p)).save(candidate);
const final=path.join(OUT,'Payments_Guidelines_Query_Expert_Slides.pptx');
await finalizePresentation({workspaceDir:ROOT,candidatePath:candidate,finalPath:final,
 pythonExecutable:path.join(DEP,'python/python.exe'),integrityValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_layout_geometry.py'),
 explicitTotalSlideCount:8,requiredNativeTableOwnerSlides:[6],layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit','--require-native-table-slide','6'],fontPolicy:{basis:'design',families:['Inter','Georgia']},verifyArtifactToolImport:true,receiptPath:path.join(BUILD,'query-expert.validation.json')});
console.log(final);
