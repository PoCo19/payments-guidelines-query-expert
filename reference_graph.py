"""Candidate corpus reference graph. Families/topics are navigation, not precedence."""
import collections
import hashlib
import json
import re
from pathlib import Path
from product_scope import ALIASES, number, feature_applies

VERSION=1
SCANNER_VERSION=4
OC=re.compile(r'\b(?:OC|0C|Operating\s+Circular)\s*\.?\s*(?:No\.?\s*)?[-/:]?\s*(\d{1,4})(?:\s*[-(]?\s*([A-Z])\b\)?)?(?![\w])',re.I)
FULL=re.compile(r'\b[A-Z]{2,}(?:/[A-Za-z0-9.()-]+){2,}')


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False).encode()).hexdigest()


def corpus_hash(docs,pages,rules):
    return digest(dict(documents=sorted(docs,key=lambda d:d['id']),
                       pages=sorted(pages,key=lambda p:(p['document_id'],p['source_page'])),rules=rules))


def identity(doc):
    # Missing issuer stays unknown; no authority is inferred from a product.
    return (str(doc.get('issuer') or '').casefold(),str(doc.get('series') or '').casefold())


def scan_page(page,doc,rules):
    text=page['text'];references=[];mentions=[]
    for m in OC.finditer(text):
        ref=number(m[1]+(m[2] or ''))
        prefix=text[max(0,m.start()-55):m.start()]
        product=next((p for p in ALIASES if re.search(re.escape(p)+r'(?:/[\w-]+)*/\s*$',prefix,re.I)),None)
        tail=text[m.end():m.end()+20]
        year=re.match(r'/((?:19|20)\d{2})-(\d{2}|\d{4})(?!\d)',tail)
        references.append(dict(reference=ref,kind='partial_identifier' if re.match(r'-\d',tail) else 'numbered_reference',product=product or doc.get('series'),
            explicit_product=bool(product),fiscal_year=(year[1]+'-'+year[2][-2:]) if year else None,
            start=m.start(),end=m.end()))
    for m in FULL.finditer(text):
        # Full external identifiers remain recorded even if their target is absent.
        if re.search(r'/(?:OC|0C)(?:/|-|\d)',m[0],re.I):continue
        if any(c.isdigit() for c in m[0]):
            references.append(dict(reference=m[0].rstrip('.'),kind='full_identifier' if any(c.isdigit() for c in m[0].split('/')[-1]) else 'partial_identifier',start=m.start(),end=m.end()))
    for rule in rules:
        # A generic product-specific pattern (e.g. "issuer") must not label
        # every regulator document as that product. Across products, require
        # the explicit primary topic name; this still permits UPI Lite in RBI.
        pattern=rule['pattern']
        if not feature_applies(rule,doc):
            label=rule.get('label','').split(' / ')[0].strip()
            if not label:continue
            pattern=r'\b'+re.escape(label).replace(r'\ ',r'\s+')+r'\b'
        for m in list(re.finditer(pattern,text,re.I))[:1]:
            mentions.append(dict(topic_id=rule['id'],label=rule.get('label',rule['id']),
                                 start=m.start(),end=m.end(),basis='literal_pattern_mention'))
    return dict(references=references,mentions=mentions)


def build_graph(docs,pages,rules,previous=None):
    by_id={d['id']:d for d in docs};cache={};edges=[];mentions=[];families=collections.defaultdict(list)
    prior=(previous or {}).get('page_cache',{}) if (previous or {}).get('schema_version')==VERSION else {}
    reused=0;orphans=[]
    for d in docs:
        n=number(d.get('circular_number'));m=re.fullmatch(r'(\d+)[A-Z]*',n)
        if m:families[json.dumps([*identity(d),m[1]])].append(d['id'])
    for page in sorted(pages,key=lambda p:(p['document_id'],p['source_page'])):
        doc=by_id.get(page['document_id'])
        if not doc:
            orphans.append(dict(document_id=page['document_id'],page=page['source_page']));continue
        if doc.get('availability')!='converted':continue
        key=json.dumps([doc['id'],page['source_page']]);text=page['text']
        fingerprint=digest([text,identity(doc),rules,SCANNER_VERSION])
        if prior.get(key,{}).get('fingerprint')==fingerprint:
            scanned=prior[key]['scan'];reused+=1
        else:scanned=scan_page(page,doc,rules)
        cache[key]=dict(fingerprint=fingerprint,scan=scanned)
        def anchor(item):
            return dict(document_id=doc['id'],page=page['source_page'],start=item['start'],end=item['end'],
                quote=text[item['start']:item['end']],context=text[max(0,item['start']-120):item['end']+220],
                page_sha256=hashlib.sha256(text.encode()).hexdigest())
        for item in scanned['references']:
            if item['kind']=='numbered_reference':
                targets=[d for d in docs if number(d.get('circular_number'))==item['reference']
                         and str(d.get('series','')).casefold()==str(item['product']).casefold()
                         and (item.get('explicit_product') or identity(d)[0]==identity(doc)[0])]
                if item.get('fiscal_year'):
                    from product_scope import fiscal_year
                    targets=[d for d in targets if fiscal_year(d)==item['fiscal_year']]
                if item['reference']==number(doc.get('circular_number')) and str(item['product']).casefold()==str(doc.get('series')).casefold():continue
            else:
                targets=[d for d in docs if item['kind']=='full_identifier' and item['reference'].casefold() in
                         {str(d.get(k) or '').casefold() for k in ('circular_number','reference_label')}]
                if any(d['id']==doc['id'] for d in targets):continue
            target=targets[0] if len(targets)==1 else None
            status=('resolved' if target['availability']=='converted' else 'unavailable') if target else 'ambiguous' if targets else 'missing'
            if item['kind']=='partial_identifier':status='incomplete_identifier'
            proof=anchor(item)
            edge=dict(from_id=doc['id'],to_id=target['id'] if target else None,relation='references',
                reference=item['reference'],status=status,candidate_ids=sorted(d['id'] for d in targets),
                basis=item['kind'],review_status='machine_extracted_unreviewed',evidence=proof)
            edge['id']=digest([doc['id'],page['source_page'],item])[:24];edges.append(edge)
        for item in scanned['mentions']:
            mentions.append(dict(document_id=doc['id'],topic_id=item['topic_id'],label=item['label'],
                                 basis=item['basis'],evidence=anchor(item)))
    return dict(schema_version=VERSION,corpus_fingerprint=corpus_hash(docs,pages,rules),
        status='candidate_not_activated',edges=edges,topic_mentions=mentions,orphan_pages=orphans,
        numbering_families=[dict(key=json.loads(k),document_ids=sorted(v),basis='number_pattern_only_not_amendment_proof')
                           for k,v in sorted(families.items()) if len(v)>1],page_cache=cache,
        summary=dict(documents=len(docs),pages_scanned=len(cache),pages_reused=reused,
                     references=len(edges),statuses=dict(collections.Counter(e['status'] for e in edges)),
                     topic_mentions=len(mentions),topic_documents=len({m['document_id'] for m in mentions})),
        limitations=['Explicit identifiers only; unrecognised OCR/aliases and implicit links can be missed.',
                     'Number families and shared topics do not establish amendments, applicability or supersession.',
                     'Candidate relationships require review; no document is excluded for lacking a family/topic.'])


def build_release(directory,previous_path=None):
    from quality import apply_reviews,load_reviews
    directory=Path(directory)
    docs=json.loads((directory/'index.json').read_text(encoding='utf-8-sig'))
    pages=[json.loads(x) for x in (directory/'all_circular_pages.jsonl').read_text(encoding='utf-8-sig').split('\n') if x.strip()]
    docs,pages=apply_reviews(docs,pages,load_reviews(directory))
    rules=json.loads((directory/'feature_rules.json').read_text(encoding='utf-8-sig')) if (directory/'feature_rules.json').exists() else []
    previous=json.loads(Path(previous_path).read_text(encoding='utf-8')) if previous_path and Path(previous_path).exists() else None
    return build_graph(docs,pages,rules,previous)


class ReferenceGraph:
    def __init__(self,path,engine):
        self.data=json.loads(Path(path).read_text(encoding='utf-8'))
        if self.data.get('schema_version')!=VERSION or self.data['corpus_fingerprint']!=corpus_hash(engine.docs,engine.pages,engine.registry.rules):
            raise ValueError('Candidate reference graph is stale; rebuild and review it.')
        pages={(p['document_id'],p['source_page']):p for p in engine.pages}
        docs={d['id']:d for d in engine.docs}
        for record in self.data['edges']+self.data['topic_mentions']:
            proof=record['evidence'];page=pages.get((proof['document_id'],proof['page']))
            if (not page or hashlib.sha256(page['text'].encode()).hexdigest()!=proof['page_sha256']
                or page['text'][proof['start']:proof['end']]!=proof['quote']
                or not proof['quote']):raise ValueError('Reference graph anchor does not match its source.')
            if 'from_id' in record:
                if record['relation']!='references' or record['from_id']!=proof['document_id']:
                    raise ValueError('Invalid reference relationship provenance.')
                if record['status']=='resolved' and (record['to_id'] not in docs or
                    record['to_id'] not in record['candidate_ids'] or docs[record['to_id']]['availability']!='converted'):
                    raise ValueError('Resolved graph target is unavailable.')
        self.engine=engine

    def expand(self,query,seeds,allowed):
        """Candidate-only one-hop expansion. Never follows family/topic memberships."""
        seed_ids={s['document_id'] for s in seeds};terms=set(self.engine.query_terms(query))
        choices={};used=[]
        for edge in self.data['edges']:
            if edge['status']!='resolved':continue
            a,b=edge['from_id'],edge['to_id']
            target=b if a in seed_ids else a if b in seed_ids else None
            if not target or target in seed_ids or not allowed(target):continue
            candidates=self.engine.parts_by_doc.get(target,[])
            ranked=sorted(candidates,key=lambda p:(-len(terms & set(self.engine.query_terms(p['text']))),p['id']))
            if ranked and len(terms & set(self.engine.query_terms(ranked[0]['text'])))>=2:
                p=ranked[0];score=len(terms & set(self.engine.query_terms(p['text'])))
                if p['id'] not in choices:choices[p['id']]=(score,p,edge)
        selected=sorted(choices.values(),key=lambda v:(-v[0],v[1]['id']))[:4]
        return [(p,e) for _,p,e in selected]
