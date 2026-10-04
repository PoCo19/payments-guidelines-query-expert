"""Build a separate multi-product corpus; never overwrite the active baseline."""
import argparse,collections,hashlib,json,re,shutil,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from tools.audit_product_pack import audit,split_pages,urlkey
LABELS={'aeps':'AePS','bhim-aadhaar':'BHIM Aadhaar','cts':'CTS','e-kyc-setu-system':'e-KYC Setu','e-rupi':'e-RUPI','imps':'IMPS','nach':'NACH','netc':'NETC','nfs':'NFS','others':'Others','rupay':'RuPay','upi':'UPI'}
QUARANTINE={'npci:rupay:726':'Listing title/date conflicts with extracted body; original-PDF review required.','npci:imps:533':'Circular number and fiscal-year fields conflict with body; original-PDF review required.'}
def sha(data):return hashlib.sha256(data).hexdigest()
def write(path,value):path.write_text(json.dumps(value,indent=2,ensure_ascii=False),encoding='utf-8')
def build(source,destination):
 source=Path(source).resolve();dest=Path(destination).resolve()
 if not dest.is_relative_to((ROOT/'data').resolve()):raise ValueError('Destination must be a new directory inside project data/')
 if dest.exists():raise ValueError('Destination exists; choose a new release directory. Existing corpora are never overwritten.')
 report=audit(source,ROOT/'reports');rows=report['rows']
 baseline=ROOT/'data';docs=json.loads((baseline/'index.json').read_text(encoding='utf-8-sig'))
 pages=[json.loads(line) for line in (baseline/'all_circular_pages.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()]
 byid={d['id']:d for d in docs};groups=collections.defaultdict(list);listings={};input_hashes={}
 for invpath in sorted((source/'inventory').glob('*inventory.json')):
  raw=invpath.read_bytes();inv=json.loads(raw.decode('utf-8-sig'));product=inv.get('product') or inv['source_page'].rstrip('/').split('/')[-1]
  input_hashes['inventory/'+invpath.name]=sha(raw)
  for item in inv['items']:listings[f"npci:{product}:{item['id']}"]=dict(item,inventory_product=product,inventory_generated_at=inv['generated_at'])
 for row in rows:groups[row['source_url'] or row['key']].append(row)
 stage=dest.with_name(dest.name+'.building')
 if stage.exists():raise ValueError('Incomplete staging directory exists; inspect it or choose another release name.')
 stage.mkdir(parents=True);(stage/'sources/inventory').mkdir(parents=True)
 for invpath in (source/'inventory').glob('*.json'):shutil.copy2(invpath,stage/'sources/inventory'/invpath.name)
 oldpages=collections.defaultdict(list)
 for p in pages:oldpages[p['document_id']].append(p)
 for d in docs:
  d['product_memberships']=[d['series']];d['source_listings']=[];d['reference_label']=str(d.get('official_reference') or ('OC '+str(d['circular_number'])))
  d['source_root']='legacy';d['fiscal_year']=None
  d['source_coverage']=dict(total_pages=len(oldpages[d['id']]),empty_pages=[],thin_pages=[],page_count_verified=bool(d.get('page_count')),origin='existing_v04')
  d['metadata_quality']='existing_source_metadata'
 variants=[];actions=collections.Counter()
 for key,entries in sorted(groups.items()):
  existing=sorted({i for row in entries for i in row['existing_document_ids']})
  if len(existing)>1:raise ValueError('Ambiguous existing identity: '+key)
  candidates=[row for row in entries if row['file_exists']]
  for row in candidates:
   p=Path(row['markdown_file']).resolve()
   if not p.is_relative_to(source/'circulars'):raise ValueError('Source escaped circular directory')
   raw=p.read_bytes()
   if sha(raw)!=row['markdown_sha256']:raise ValueError('Source changed after audit: '+str(p))
   rel=p.relative_to(source);target=stage/'sources'/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw);input_hashes[str(rel).replace('\\','/')]=sha(raw)
  memberships=sorted({LABELS[row['product']] for row in entries})
  if existing:
   d=byid[existing[0]];d['product_memberships']=sorted(set(d['product_memberships']+memberships));d['source_listings']=[listings[row['key']] for row in entries]
   d['import_variants']=[dict(key=row['key'],markdown='sources/'+str(Path(row['markdown_file']).relative_to(source)).replace('\\','/'),sha256=row['markdown_sha256']) for row in candidates]
   if d['availability']=='converted':actions['preserved_existing']+=1;continue
   if candidates:
    d['import_review_note']='Candidate Markdown exists but the previously unavailable source requires original-PDF verification before indexing.';actions['existing_gap_candidate']+=1
   continue
  selected=min(candidates,key=lambda row:(len(row.get('empty_pages',[])),row['key'])) if candidates else entries[0]
  item=listings[selected['key']];docid='npci-source-'+sha(key.encode())[:24]
  num=str(item.get('circular_number') or '').strip();native=LABELS[selected['product']]
  if item.get('category')=='pcomp':native='Product Compliance'
  if item.get('category')=='rupay':native='RuPay'
  has_pdf=bool(item.get('pdf_url'))
  status='converted' if candidates else {'skipped_no_pdf':'no_public_pdf','skipped_zip':'attachment_not_extracted','extract_failed':'extraction_failed'}.get(item.get('extraction_status'),'text_unavailable')
  notes=[QUARANTINE[row['key']] for row in entries if row['key'] in QUARANTINE]
  if notes:status='needs_source_review'
  selectedpages=split_pages(Path(selected['markdown_file']).read_text(encoding='utf-8-sig')) if candidates else []
  empty=[n for n,t in selectedpages if not t];thin=[n for n,t in selectedpages if len(re.findall(r'\w+',t))<15]
  title=item.get('title') or 'Untitled inventory entry'
  d=dict(id=docid,archive_year=item.get('year'),circular_number=num,reference_label=('Reference '+num if num else 'Reference not verified'),subject=title,listing_title=title,series=native,product_memberships=memberships,fiscal_year=item.get('fy'),issue_date=None,listed_update_date=None,date_basis='Issue date not verified; inventory fiscal year retained separately',source_listing=item.get('source_url'),source_pdf=item.get('pdf_url'),attachment_url=item.get('file_url') if not has_pdf else None,availability=status,family='',related_circulars=[],notes=notes,local_pdf=None,source_root='imported',page_count=item.get('page_count'),source_listings=[listings[row['key']] for row in entries],source_archive_retrieved_on=selected['inventory_generated_at'][:10],metadata_quality='inventory_unverified',source_coverage=dict(total_pages=len(selectedpages),empty_pages=empty,thin_pages=thin,page_count_verified=item.get('page_count') is not None,origin='imported_markdown'),import_variants=[dict(key=row['key'],markdown='sources/'+str(Path(row['markdown_file']).relative_to(source)).replace('\\','/'),sha256=row['markdown_sha256']) for row in candidates])
  if candidates:d['markdown_file']='sources/'+str(Path(selected['markdown_file']).relative_to(source)).replace('\\','/');d['markdown_sha256']=selected['markdown_sha256']
  docs.append(d);byid[docid]=d;actions[status]+=1
  for n,t in selectedpages:
   pages.append(dict(document_id=docid,source_page=n,text=t,method='imported_markdown',is_scanned=item.get('is_scanned'),review_status='imported_text_not_verified',needs_priority_review=n in thin,source_text_status='empty' if not t else 'thin' if n in thin else 'unverified',source_markdown=d['markdown_file'],markdown_sha256=d['markdown_sha256']))
 shutil.copy2(ROOT/'product_feature_rules.json',stage/'feature_rules.json')
 shutil.copy2(baseline/'review_annotations.json',stage/'review_annotations.json')
 write(stage/'index.json',docs)
 (stage/'all_circular_pages.jsonl').write_text('\n'.join(json.dumps(p,ensure_ascii=False) for p in pages)+'\n',encoding='utf-8')
 write(stage/'source_manifest.json',dict(hashes=input_hashes,origin=str(source),policy='Immutable local copies; preserve raw Markdown and inventory metadata.'))
 metadata=dict(schema_version=1,release=dest.name,baseline='v0.4',documents=len(docs),pages=len(pages),source_inventory_rows=len(rows),actions=dict(actions),snapshot='Inventories 2026-09-09 to 2026-09-15; retained UPI source snapshot through 2026-09-22',window='Inventory archive years 2009-2026; issue dates largely unverified',status='staged_not_active')
 write(stage/'corpus.json',metadata)
 assert len({d['id'] for d in docs})==len(docs)
 assert len({(p['document_id'],p['source_page']) for p in pages})==len(pages)
 assert sum(len(d['source_listings']) for d in docs)==len(rows)
 stage.rename(dest)
 config=json.loads((ROOT/'config.json').read_text(encoding='utf-8-sig'));config.update(data_dir=str(dest.relative_to(ROOT)),multi_product=True,embedding_cache='data/embedding_cache.sqlite3')
 configpath=ROOT/'config.products.json';write(configpath,config)
 print(json.dumps(metadata,indent=2));return dest
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',default=r'C:\Users\Admin\Downloads\circulars');p.add_argument('--destination',default=str(ROOT/'data/all-products-v1'));a=p.parse_args();build(a.source,a.destination)
