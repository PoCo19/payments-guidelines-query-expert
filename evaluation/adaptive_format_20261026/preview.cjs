// Synthetic presentation fixture, never used as payments evidence.
const fs=require('node:fs'),path=require('node:path');
const {renderHTML,toMarkdown}=require('../../web/answer_format.js');
const claims=[
 {text:'This is a presentation test showing an explanation, comparison and follow-up points together.',sources:['S1']},
 {text:'Example document A describes the first option and its conditions.',sources:['S1']},
 {text:'Example document B describes the second option and its conditions.',sources:['S2']},
 {text:'Check any qualifications in the original source before using the comparison.',sources:['S1','S2']}
];
const result={claims,answer_blocks:[{type:'paragraph',claims:[claims[0]]},{type:'table',columns:['Evidence 1','Evidence 2'],claims:claims.slice(1,3)},{type:'bullets',claims:[claims[3]]}]};
const root=path.resolve(__dirname,'../../data/qa26/format-preview');
fs.mkdirSync(root,{recursive:true});
fs.copyFileSync(path.resolve(__dirname,'../../web/style.css'),path.join(root,'style.css'));
fs.writeFileSync(path.join(root,'index.html'),'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Adaptive answer presentation test</title><link rel="stylesheet" href="style.css"><body style="display:block;padding:28px"><main style="max-width:850px;margin:auto;background:white;padding:24px"><h1>Adaptive answer presentation</h1><p>Presentation fixture — not a payments answer or a model-quality result.</p>'+renderHTML(result)+'<p>Source buttons are visual fixtures; actual source navigation is tested in Query Desk.</p></main></body></html>');
fs.writeFileSync(path.join(__dirname,'fixture-export.md'),toMarkdown(result));
