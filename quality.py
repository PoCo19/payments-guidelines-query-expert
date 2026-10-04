"""Source-bound review overlays. Raw imported files are never overwritten."""
import copy,datetime,hashlib,json,re,threading,uuid
from pathlib import Path
from product_scope import feature_applies
ROLES={'payee_psp':r'payee\s+psp','payer_psp':r'payer\s+psp','remitter_bank':r'remitter\s+bank',
 'issuer_bank':r'issuer\s+bank','beneficiary_bank':r'beneficiary\s+bank','upi_app':r'upi\s+(?:app|application)',
 'primary_user':r'primary\s+user','secondary_user':r'secondary\s+user','acquiring_bank':r'acquiring\s+bank'}
def digest(text):return hashlib.sha256(text.encode()).hexdigest()
def norm(text):return ' '.join(text.split())

def load_reviews(directory):
    path=Path(directory)/'review_annotations.json'
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else []

def apply_reviews(docs,pages,records):
    docs,pages=copy.deepcopy(docs),copy.deepcopy(pages)
    by_id={d['id']:d for d in docs};by_page={(p['document_id'],p['source_page']):p for p in pages}
    for record in records:
        if record.get('status')!='accepted':continue
        d=by_id.get(record['document_id']);p=by_page.get((record['document_id'],record['page']))
        if not d or not p or digest(p.get('original_text',p['text']))!=record['source_hash']:
            raise ValueError('Stale review annotation: '+record['id'])
        if record['kind']=='correction':
            p.setdefault('original_text',p['text'])
            if p['text'].count(record['before'])!=1:raise ValueError('Correction anchor must occur exactly once: '+record['id'])
            p['text']=p['text'].replace(record['before'],record['after'],1)
            p.setdefault('corrections',[]).append(record)
        elif record['kind'] in ('metadata','feature','relationship') and norm(record.get('anchor','')) not in norm(p['text']):
            raise ValueError('Review anchor no longer matches: '+record['id'])
        elif record['kind']=='metadata':
            d[record['field']]=record['value'];d.setdefault('metadata_reviews',[]).append(record)
    return docs,pages

def enrich(parts,registry,records):
    documents={d['id']:d for d in registry.docs}
    for p in parts:
        p['feature_ids']=sorted(set(registry.features[p['document_id']]+[r['id'] for r in registry.rules if feature_applies(r,documents[p['document_id']]) and re.search(r['pattern'],p['text'],re.I)]))
        p['feature_basis']='title_and_clause_regex_unreviewed'
        p['roles']=[key for key,pattern in ROLES.items() if re.search(pattern,p['text']+' '+p.get('section_heading',''),re.I)]
        p['role_basis']='text_regex_unreviewed'
        for r in records:
            if r.get('status')=='accepted' and r['kind']=='feature' and r['document_id']==p['document_id'] and r['page']==p['page'] and norm(r['anchor']) in norm(p['text']):
                p['feature_ids']=r['feature_ids'];p['roles']=r.get('roles',p['roles']);p['feature_basis']=r['reviewer_kind'];p['role_basis']=r['reviewer_kind'];p['review_id']=r['id']

def scan(docs,pages):
    queue=[]
    for p in pages:
        reasons=[]
        if not p['text'].strip():reasons.append('missing_extracted_page_text')
        if p.get('source_text_status')=='thin':reasons.append('thin_extracted_page_text')
        if p.get('needs_priority_review'):reasons.append('source_priority_review')
        if '$' in p['text']:reasons.append('currency_symbol_check')
        if p.get('method')=='ocr' and re.search(r'\d',p['text']):reasons.append('ocr_numbers_or_dates')
        if re.search(r'\b(?:table|annexure|format)\b',p['text'],re.I):reasons.append('table_or_annexure_layout')
        if reasons:queue.append(dict(document_id=p['document_id'],page=p['source_page'],reasons=reasons,source_hash=digest(p.get('original_text',p['text'])),corrections=len(p.get('corrections',[]))))
    missing=[dict(document_id=d['id'],fields=[f for f in ('issue_date','source_pdf') if not d.get(f)]) for d in docs if not d.get('issue_date') or not d.get('source_pdf')]
    return dict(pages=sorted(queue,key=lambda x:('currency_symbol_check' not in x['reasons'],'source_priority_review' not in x['reasons'],x['document_id'])),metadata_gaps=missing,note='Flags are review candidates, not proof of errors. Accepted local reviews remain distinct from expert approval.')

class ReviewStore:
    def __init__(self,directory):self.path=Path(directory)/'review_annotations.json';self.lock=threading.Lock()
    def save(self,payload,engine):
        record=dict(payload)
        kind=record.get('kind');status=record.get('status')
        if kind not in ('correction','metadata','feature','relationship') or status not in ('proposed','accepted','rejected'):raise ValueError('Invalid review kind/status')
        if not isinstance(record.get('reviewer'),str) or not record['reviewer'].strip():raise ValueError('Reviewer name is required')
        record['reviewer_kind']='human_local_review'
        p=engine.page_lookup.get((record.get('document_id'),record.get('page')))
        if not p or record.get('source_hash')!=digest(p.get('original_text',p['text'])):raise ValueError('Source hash mismatch; refresh the review page')
        if kind=='correction':
            if not isinstance(record.get('before'),str) or not record['before'] or p['text'].count(record['before'])!=1 or not isinstance(record.get('after'),str) or not record['after'].strip():raise ValueError('Provide a unique exact original phrase and replacement')
        else:
            if not record.get('anchor') or norm(record['anchor']) not in norm(p['text']):raise ValueError('An exact source anchor is required')
        if kind=='metadata':
            if record.get('field') not in ('issue_date','listed_update_date','effective_date'):raise ValueError('Unsupported metadata field')
            datetime.date.fromisoformat(record.get('value',''))
        if kind=='feature':
            allowed={r['id'] for r in engine.registry.rules}
            if not isinstance(record.get('feature_ids'),list) or not set(record['feature_ids']).issubset(allowed):raise ValueError('Invalid feature IDs')
            if not isinstance(record.get('roles',[]),list) or not set(record.get('roles',[])).issubset(ROLES):raise ValueError('Invalid roles')
        if kind=='relationship':
            if record.get('target_id') not in engine.by_id or record['target_id']==record['document_id']:raise ValueError('Invalid relationship target')
            if record.get('relation') not in ('references','amends','clarifies','supersedes'):raise ValueError('Invalid relationship type')
        with self.lock:
            records=load_reviews(self.path.parent)
            record['id']=uuid.uuid4().hex;record['created_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
            records.append(record)
            raw_pages=copy.deepcopy(engine.pages)
            for source in raw_pages:
                source['text']=source.pop('original_text',source['text']);source.pop('corrections',None)
            apply_reviews(engine.docs,raw_pages,records)
            temp=self.path.with_suffix('.tmp');temp.write_text(json.dumps(records,indent=2,ensure_ascii=False),encoding='utf-8');temp.replace(self.path)
        return dict(record=record,message='Saved. Accepted changes take effect after rebuilding the index and restarting. Raw sources are preserved.')
