"""Verify and package the current midterm files without rewriting their content."""
import hashlib,json,re,zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'output/midsem'
names=['Payments_Guidelines_Query_Expert_Slides.pptx','Payments_Guidelines_Query_Expert_Slides.pdf','Payments_Guidelines_Query_Expert_Report.docx','Payments_Guidelines_Query_Expert_Report.pdf','Narration_and_Recording_Checklist.md','Submission_Checklist.md','CURRENT_SCOPE.md','START_HERE.md','team_details.json']
for name,count in [('Payments_Guidelines_Query_Expert_Slides.pdf',8),('Payments_Guidelines_Query_Expert_Report.pdf',3)]:
 pdf=PdfReader(OUT/name);assert len(pdf.pages)==count
 text='\n'.join(p.extract_text() for p in pdf.pages)
 assert 'Payments Guidelines Query Expert' in text
 for v in ['55/55','6/6','5/6','160.5']:assert v in text
data=json.loads((ROOT/'tmp/midsem/query_expert_content.json').read_text(encoding='utf-8'))
with zipfile.ZipFile(OUT/names[0]) as z:
 ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
 for i,note in enumerate(data['notes'],1):
  root=ET.fromstring(z.read(f'ppt/notesSlides/notesSlide{i}.xml'))
  assert note in ''.join(x.text or '' for x in root.findall('.//a:t',ns))
record=dict(revision='Slide refinements 4 October 2026',slide_count=8,report_pages=3,narration_words=sum(len(re.findall(r'\b[\w’]+\b',n)) for n in data['notes']),checks=['matching recorded retrieval metrics','all eight speaker notes','package links','PDF page counts','PPTX package integrity'],files={name:hashlib.sha256((OUT/name).read_bytes()).hexdigest() for name in names})
(OUT/'evidence/deliverable-checks.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
for name in ['START_HERE.md','CURRENT_SCOPE.md','Submission_Checklist.md','evidence/README.md']:
 p=OUT/name
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
  if not target.startswith(('http://','https://')):assert (p.parent/target).exists(),(p,target)
files=[OUT/name for name in names]+[OUT/'evidence/README.md',OUT/'evidence/unit-tests.txt',OUT/'evidence/deliverable-checks.json']
for folder in ['20261003T172349Z','browser-query-expert','simple-demo','simple-demo-friend']:
 files.extend(p for p in (OUT/'evidence'/folder).rglob('*') if p.is_file())
bundle=OUT/'Payments_Guidelines_Query_Expert_Midterm.zip'
with zipfile.ZipFile(bundle,'w',zipfile.ZIP_DEFLATED) as z:
 for p in files:z.write(p,p.relative_to(OUT).as_posix())
with zipfile.ZipFile(bundle) as z:assert z.testzip() is None
print('Verified 8 slides, 3 report pages, notes, metrics, links and ZIP integrity.')
