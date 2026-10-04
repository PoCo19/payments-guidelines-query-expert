"""Read-only source audit; writes reports only, never changes the active corpus."""
import argparse,collections,hashlib,json,re,sys
from pathlib import Path
from urllib.parse import urlsplit,urlunsplit
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from ingestion import clause_chunks

def urlkey(value):
 if not value:return None
 u=urlsplit(value);return urlunsplit((u.scheme.lower(),u.netloc.lower(),u.path,'',''))

def split_pages(text):
 matches=list(re.finditer(r'<!--\s*Page\s+(\d+)\s*-->',text,re.I))
 return [(int(m.group(1)),text[m.end():matches[i+1].start() if i+1<len(matches) else len(text)].strip()) for i,m in enumerate(matches)]

def audit(source,output):
 source=Path(source).resolve();output=Path(output);output.mkdir(parents=True,exist_ok=True)
 old=json.loads((ROOT/'data/index.json').read_text(encoding='utf-8-sig'))
 old_urls=collections.defaultdict(list)
 for d in old:
  if d.get('source_pdf'):old_urls[urlkey(d['source_pdf'])].append(d['id'])
 rows=[];products=[];urlgroups=collections.defaultdict(list);hashgroups=collections.defaultdict(list);referenced=set()
 for invpath in sorted((source/'inventory').glob('*inventory.json')):
  inv=json.loads(invpath.read_text(encoding='utf-8-sig'));product=inv.get('product') or urlsplit(inv['source_page']).path.rstrip('/').split('/')[-1]
  directory=(source/'circulars'/product).resolve();items=inv['items'];productrows=[]
  for i,item in enumerate(items):
   key=f"npci:{product}:{item.get('id',i)}";filename=item.get('output_filename');path=(directory/filename).resolve() if filename else None
   safe=path is not None and path.is_relative_to(directory)
   exists=bool(safe and path.is_file());url=urlkey(item.get('pdf_url') or item.get('file_url'))
   row=dict(key=key,product=product,inventory_id=item.get('id'),inventory_file=invpath.name,inventory_generated_at=inv.get('generated_at'),title=item.get('title'),circular_number=item.get('circular_number'),fiscal_year=item.get('fy'),year=item.get('year'),category=item.get('category'),extraction_status=item.get('extraction_status'),source_url=url,markdown_file=str(path) if safe else None,file_exists=exists,declared_pages=item.get('page_count'),declared_markdown_pages=item.get('markdown_pages'),is_scanned=item.get('is_scanned'),existing_document_ids=old_urls.get(url,[]),flags=[])
   if url:urlgroups[url].append(key)
   if filename and not safe:row['flags'].append('unsafe_output_path')
   if item.get('extraction_status')=='extracted' and not exists:row['flags'].append('extracted_file_missing')
   if exists:
    referenced.add(path);raw=path.read_bytes();text=raw.decode('utf-8-sig');pages=split_pages(text)
    row.update(markdown_sha256=hashlib.sha256(raw).hexdigest(),page_markers=len(pages),empty_pages=[n for n,t in pages if not t.strip()],thin_pages=[n for n,t in pages if len(re.findall(r'\w+',t))<15],words=sum(len(t.split()) for n,t in pages))
    if not pages:row['flags'].append('no_page_markers')
    if [n for n,t in pages]!=list(range(1,len(pages)+1)):row['flags'].append('nonsequential_page_markers')
    if row['empty_pages']:row['flags'].append('empty_source_pages')
    if row['thin_pages']:row['flags'].append('thin_source_pages')
    if item.get('page_count') is not None and item['page_count']!=len(pages):row['flags'].append('pdf_page_count_mismatch')
    if item.get('markdown_pages') is not None and item['markdown_pages']!=len(pages):row['flags'].append('markdown_page_count_mismatch')
    if item.get('page_count') is None:row['flags'].append('pdf_page_count_unverified')
    row['prospective_chunks']=len(clause_chunks([dict(document_id=key,source_page=n,text=t) for n,t in pages if t]))
    body=' '.join(' '.join(t.split()) for n,t in pages)
    if body:hashgroups[hashlib.sha256(body.encode()).hexdigest()].append(key)
   rows.append(row);productrows.append(row)
  products.append(dict(product=product,generated_at=inv.get('generated_at'),listed=len(items),declared_item_count=inv.get('item_count'),markdown_files=len(list(directory.glob('*.md'))),available_markdown=sum(r['file_exists'] for r in productrows),statuses=dict(collections.Counter(r['extraction_status'] for r in productrows)),pages=sum(r.get('page_markers',0) for r in productrows),empty_pages=sum(len(r.get('empty_pages',[])) for r in productrows),thin_pages=sum(len(r.get('thin_pages',[])) for r in productrows),prospective_chunks=sum(r.get('prospective_chunks',0) for r in productrows),existing_url_matches=sum(bool(r['existing_document_ids']) for r in productrows),missing_number=sum(not r['circular_number'] for r in productrows)))
 allfiles=list((source/'circulars').rglob('*'));allmd=[p.resolve() for p in allfiles if p.suffix.lower()=='.md'];matchedold={x for r in rows for x in r['existing_document_ids']}
 result=dict(source=str(source),note='Local filesystem audit only. Inventory timestamp is not proof of live website completeness. Empty/thin-page flags require source review. Prospective chunks are before deduplication and quality gating.',products=products,totals=dict(listed=len(rows),markdown_files=len(allmd),inventory_rows_with_markdown=sum(r['file_exists'] for r in rows),pages=sum(r.get('page_markers',0) for r in rows),empty_pages=sum(len(r.get('empty_pages',[])) for r in rows),thin_pages=sum(len(r.get('thin_pages',[])) for r in rows),prospective_chunks=sum(r.get('prospective_chunks',0) for r in rows),statuses=dict(collections.Counter(r['extraction_status'] for r in rows)),missing_circular_number=sum(not r['circular_number'] for r in rows),pdf_files=sum(p.suffix.lower()=='.pdf' for p in allfiles),existing_documents_matched_by_url=len(matchedold),existing_documents_not_url_matched=len(old)-len(matchedold)),flags=dict(collections.Counter(f for r in rows for f in r['flags'])),duplicate_urls={k:v for k,v in urlgroups.items() if len(v)>1},identical_body_groups={k:v for k,v in hashgroups.items() if len(v)>1},duplicate_inventory_keys={k:v for k,v in collections.Counter(r['key'] for r in rows).items() if v>1},unreferenced_markdown=[str(p) for p in allmd if p not in referenced],existing_not_url_matched=[dict(id=d['id'],title=d['subject'],availability=d['availability'],url=d.get('source_pdf')) for d in old if d['id'] not in matchedold],rows=rows)
 (output/'all_products_audit.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
 print(json.dumps({k:result[k] for k in ['totals','flags','products']},indent=2));print('Duplicate URL groups',len(result['duplicate_urls']),'identical body groups',len(result['identical_body_groups']),'unreferenced MD',len(result['unreferenced_markdown']))
 return result
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--source',default=r'C:\Users\Admin\Downloads\circulars');parser.add_argument('--output',default=str(ROOT/'reports'));args=parser.parse_args();audit(args.source,args.output)
