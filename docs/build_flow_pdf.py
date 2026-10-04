"""Reproducible illustrated colleague flow guide. Requires bundled ReportLab."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor,white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf/Circular_Intelligence_Project_Flow_v04.pdf'
pdfmetrics.registerFont(TTFont('Arial',r'C:\Windows\Fonts\arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold',r'C:\Windows\Fonts\arialbd.ttf'))
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='ArialBold')
W,H=595.28,841.89
INK=HexColor('#20342e');MUTED=HexColor('#566b63');ACCENT=HexColor('#dce7b4');BG=HexColor('#f4f6ef');LINE=HexColor('#d7ded5')
c=canvas.Canvas(str(OUT),pagesize=(W,H));c.setTitle('Circular Intelligence - Project Flow v0.4');c.setAuthor('Circular Intelligence capstone project')
def para(text,x,y,w=499,size=10.4,color=INK,bold=False):
 style=ParagraphStyle('body',fontName='ArialBold' if bold else 'Arial',fontSize=size,leading=size*1.4,textColor=color,spaceAfter=0)
 p=Paragraph(text,style);pw,ph=p.wrap(w,1000);p.drawOn(c,x,y-ph);return y-ph

def start(n,label,title,sub):
 c.setFillColor(BG);c.rect(0,0,W,H,fill=1,stroke=0)
 c.setFillColor(INK);c.rect(0,H-10,W,10,fill=1,stroke=0)
 para('CIRCULAR INTELLIGENCE  /  PROJECT FLOW',48,800,size=9,bold=True)
 para(label.upper(),48,764,size=9,color=MUTED,bold=True)
 y=para(title,48,741,size=25,bold=True)
 y=para(sub,48,y-12,size=10.6,color=MUTED)
 c.setStrokeColor(LINE);c.line(48,45,W-48,45)
 para('AI capstone prototype  |  v0.4.0  |  25 September 2026',48,32,size=8,color=MUTED)
 para(f'{n} / 5',W-80,32,w=40,size=8,color=MUTED)
 return y-22

def box(x,y,w,h,title,body,fill=white):
 c.setFillColor(fill);c.setStrokeColor(LINE);c.roundRect(x,y-h,w,h,9,fill=1,stroke=1)
 yy=para(title,x+14,y-12,w-28,11,bold=True)
 para(body,x+14,yy-7,w-28,9.4,color=MUTED)

def arrow(x,y1,y2):
 c.setStrokeColor(MUTED);c.setFillColor(MUTED);c.line(x,y1,x,y2+4)
 p=c.beginPath();p.moveTo(x-3,y2+7);p.lineTo(x,y2);p.lineTo(x+3,y2+7);p.close();c.drawPath(p,fill=1,stroke=0)

def shot(name,y,maxh=375):
 img=ImageReader(str(ROOT/'docs/screenshots'/name));iw,ih=img.getSize();w=min(499,maxh*iw/ih);h=w*ih/iw
 c.drawImage(img,48+(499-w)/2,y-h,width=w,height=h,mask='auto');return y-h

y=start(1,'01 / Local research flow','From circulars to cited answers','A colleague guide to how the project works, what changed, and how to assess its output.')
box(48,y,155,67,'107 circulars','251 source pages',ACCENT);box(220,y,155,67,'916 chunks','Each retains its circular and page',ACCENT);box(392,y,155,67,'22 gaps','Missing or unavailable text',ACCENT)
y-=93
steps=[('1  Preserve and review sources','Imported register and page text + original PDFs. Accepted source-hash-bound overlays correct effective text; raw extraction stays intact.'),('2  Build attributed indexes','Clause/page-aware chunks feed BM25, local Qwen embeddings in Chroma, and a SQLite document / feature / reference registry.'),('3  Choose evidence for the question','Specific questions use candidate search and CPU reranking. Summaries cover document sections; comparisons balance each named circular.'),('4  Generate and check claims','Local Qwen creates cited claims. Citation, number and quoted-support checks keep supported drafts and separate uncertain claims for review.'),('5  Inspect, export and evaluate','Open source pages and PDFs, inspect coverage and support checks, export notes, and review results using the frozen evaluation set.')]
for i,(title,body) in enumerate(steps):
 box(48,y,499,69,title,body)
 if i<4:arrow(W/2,y-70,y-84)
 y-=87
para('The model is not trained on this collection. It receives selected evidence for each question. Generation and checking run locally after model setup.',48,y+3,size=9.7,color=MUTED)
c.showPage()
y=start(2,'02 / Retrieval and chunking','Ask differently. Retrieve differently.','Circular ownership remains explicit through every retrieval path.')
for title,body in [('Specific question','Up to 32 candidates -> optional MiniLM reranker -> eight direct seeds. Related scope adds bounded references, feature hints and neighbours.'),('Circular summary','Name the circular. Select across sections and report included/total chunks. OC 186A fits completely: 14 of 14 chunks.'),('Circular comparison','Name at least two circulars. Balance sections across them. Withhold the comparison if a required circular is missing, ambiguous or filtered out.')]:
 y=para(title,48,y,size=11,bold=True)-5;y=para(body,48,y,size=10)-12
para('Example: summary evidence with explicit coverage',48,y,size=9,bold=True);y-=19
y=shot('v04-summary.png',y,330)-10
para('Chunking: recognized headings and numbered clauses; maximum 220 words, with 35-word overlap only for long blocks. Chunks stay within a page and link to neighbours in the same circular. The shared evidence budget is 18,000 characters; larger documents may have partial coverage.',48,y,size=9.5)
c.showPage()
y=start(3,'03 / Source quality and relationships','Review without losing the original','A correction is a traceable annotation, not an overwrite of the imported extraction.')
y=para('The workbench flags currency symbols, OCR numbers, table layouts and original priority pages. It also exposes metadata gaps. A reviewer can propose or accept OCR corrections, dates, feature/participant labels and source-anchored circular relationships.',48,y,size=10.5)-15
y=shot('v04-review.png',y,330)-12
y=para('Initial source checks',48,y,size=11,bold=True)-6
y=para('Ten annotations were seeded after assistant inspection of PDF images: five currency fixes on three pages, one date check, three feature/role mappings and one reference check. For example, OC 186A\'s OCR "$5000" is corrected to "₹5000" while the original remains visible.',48,y,size=10)-12
y=para('What remains for human review',48,y,size=11,bold=True)-6
y=para('213 pages are flagged as review candidates and 21 register entries have metadata gaps. These are not confirmed error counts. Bootstrap annotations are labelled assistant_source_checked; no full-corpus expert approval is claimed.',48,y,size=10)-12
para('After accepted changes: stop the app -> run.cmd embed -> restart. References connect circulars; they do not automatically establish supersession or current applicability.',48,y,size=9.7,color=MUTED)
c.showPage()
y=start(4,'04 / Answer support','See why a claim was kept','The supported draft, evidence and withheld claims are separate and inspectable.')
y=para('1. Validate cited source IDs and numerical support.<br/>2. Ask local Qwen whether each claim follows from its cited excerpts.<br/>3. Match supporting quotations to the cited text, allowing typography/whitespace differences only.<br/>4. Keep supported claims; withhold unsupported, uncertain or malformed checks.',48,y,size=10.5)-17
y=shot('v04-answer.png',y,350)-12
y=para('Live example: Remitter Bank responsibility',48,y,size=11,bold=True)-6
y=para('The answer identifies the Remitter Bank, cites OC 186A, and shows the supporting source quotation in the expanded check details. Source cards retain the document, page and retrieval reason.',48,y,size=10)-12
y=para('A filter, not an independent verifier',48,y,size=11,bold=True)-6
para('Generation and checking use the same model, so both can share mistakes. One plausible currency claim was withheld in the final test because its quotation did not match. Review important statements and omissions against the original PDF. Complete retrieved text does not guarantee a complete answer.',48,y,size=10)
c.showPage()
y=start(5,'05 / Validation and getting started','Measured results, with clear limits','Use the evidence below to demonstrate the capstone responsibly.')
box(48,y,155,70,'59 tests passed','Routing, reviews, storage and claim guards',ACCENT);box(220,y,155,70,'50 draft questions','All await independent review',ACCENT);box(392,y,155,70,'55 source anchors','Found by all three v0.4 runs',ACCENT)
y-=90
y=para('What the comparison shows',48,y,size=12,bold=True)-7
y=para('Saved v0.3 BM25 found 44/55 anchors. Adaptive v0.4 BM25, reranked BM25 and reranked hybrid each found 55/55. Reranking did not add aggregate recall on this set. Wider budgets and different retrieval routes also changed, so this is not a reranker-only experiment.',48,y,size=10)-11
y=para('Hybrid returned unrelated evidence for one negative question, but generation abstained. Six live cases covered a clause, currency limits, a summary, a comparison, a missing circular and an unrelated topic. An injected contradictory claim was withheld. The summary and comparison took roughly 60 and 71 seconds with per-claim checks.',48,y,size=10)-14
box(48,y,499,74,'Do not present this as 100% answer accuracy','This is an AI-assisted development set, not independently authored gold. Human reviewers still need to check expected answers, citation support and missing requirements.',ACCENT)
y-=92
y=para('Run and demonstrate',48,y,size=12,bold=True)-7
y=para('Open Ollama. In the project folder, double-click <b>run.cmd</b> and keep its terminal open. Visit <b>http://127.0.0.1:8765</b>. In PowerShell use <b>.\\run.cmd</b>; no execution-policy change is needed.',48,y,size=10)-12
y=para('Try: <b>Summarise OC 186A</b>, then <b>Compare OC 186 and OC 186A</b>. Inspect coverage, citations and supporting quotations. Choose Source excerpts for a faster evidence-only demonstration.',48,y,size=10)-12
y=para('Files for the project owner',48,y,size=12,bold=True)-6
y=para('<b>HOW_IT_WORKS.md</b>: detailed flow and chunking.<br/><b>docs/REVIEW_GUIDE.md</b>: OCR and evaluation review.<br/><b>docs/VALIDATION_V04.md</b>: measured results and caveats.<br/><b>evaluation/independent_review.csv</b>: review worksheet.<br/><b>run.cmd test / validate / live-check</b>: reproduce checks.',48,y,size=9.7)-14
para('Model references: <link href="https://huggingface.co/cross-encoder/ms-marco-MiniLM-L6-v2" color="#24564b">MiniLM cross-encoder</link>; <link href="https://huggingface.co/Xenova/ms-marco-MiniLM-L-6-v2" color="#24564b">pinned ONNX conversion</link>. Primary evidence is the saved circular PDFs and the source links in the app. This prototype covers an imported snapshot, primarily UPI; it is not a live rulebook.',48,y,size=9,color=MUTED)
c.save();print(OUT)
