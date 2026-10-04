"""Question-aware retrieval with explicit coverage accounting."""
import collections,re,time
from pathlib import Path

def mentions(query):
    values=re.findall(r'\b(?:OC|circular)\s*(?:no\.?\s*)?[-:]?\s*(\d+[A-Z]*)\b',query,re.I)
    if values:
        values+=re.findall(r'\b(?:and|versus|vs\.?|with)\s+(?:OC\s*)?(\d{2,3}[A-Z]*)\b',query,re.I)
    return list(dict.fromkeys(x.upper() for x in values))

def route_question(query,route='auto'):
    if route not in ('auto','clause','summary','compare'):raise ValueError('Unknown question type')
    if route!='auto':return route
    if re.search(r'\b(?:compare|comparison|difference|versus|vs\.?|changed between)\b',query,re.I):return 'compare'
    if re.search(r'\b(?:summari[sz]e|summary|overview|all (?:the )?(?:requirements|responsibilities)|comprehensive)\b',query,re.I):return 'summary'
    return 'clause'

def assemble(engine,query,method,series='',cutoff='',feature='',scope='strict',route='auto',rerank=None,fiscal_year='',document_ids=None):
    from app import validate_date
    from reranker import get_reranker
    if not query.strip() or len(query)>2000:raise ValueError('Enter a question between 1 and 2000 characters.')
    if scope not in ('strict','related'):raise ValueError('Unknown context scope')
    if method not in ('bm25','vector','hybrid'):raise ValueError('Unknown retrieval method')
    validate_date(cutoff)
    if feature and feature not in {r['id'] for r in engine.registry.rules}:raise ValueError('Unknown feature')
    budget=int(engine.config.get('context_char_budget',18000))
    if not 2000<=budget<=18000:raise ValueError('context_char_budget must be between 2000 and 18000')
    route=route_question(query,route);numbers=mentions(query)
    selected=[];seen=set();notes=[];used=0;seed_ids=[];rerank_ms=0;ranked_count=0;coverage={};reranker_model=None
    do_rerank=engine.config.get('reranker_enabled',False) if rerank is None else rerank
    if not isinstance(do_rerank,bool):raise ValueError('rerank must be true or false')
    def allowed(doc_id):
        d=engine.by_id[doc_id]
        return d['availability']=='converted' and engine.eligible(d,series,cutoff) and (not feature or feature in engine.registry.features[doc_id])
    def add(p,reason,via='',relation=None):
        nonlocal used
        if p['id'] in seen:return False
        cost=len(p['text'])+len(p['title'])+350
        if used+cost>budget or len(selected)>=(48 if route in ('summary','compare') else 18):
            notes.append('Some evidence was omitted by the passage/character budget. Coverage is partial.');return False
        selected.append(dict(p,citation=f'S{len(selected)+1}',retrieval_reason=reason,via_document_id=via,relation=relation));seen.add(p['id']);used+=cost;return True
    requested=[];missing=[];resolution=None
    if engine.config.get('multi_product'):
        from product_scope import resolve
        resolution=resolve(engine,query,numbers,series,cutoff,feature,fiscal_year,document_ids)
        series=resolution['series'];notes.extend(resolution['notes'])
        if resolution['ambiguous'] or resolution['missing']:
            return [],dict(route=route,scope=scope,seed_chunk_ids=[],included_chunk_ids=[],evidence_characters=0,character_budget=budget,max_reference_hops=1,notes=notes,document_coverage={},requested_circulars=numbers,ambiguities=resolution['ambiguous'],reranker={'enabled':False,'model':None,'candidate_count':0,'elapsed_ms':0})
        requested=resolution['requested']
        def allowed(doc_id):return doc_id in resolution['eligible_ids']
    for number in ([] if resolution else numbers):
        found=[d['id'] for d in engine.docs if str(d['circular_number']).upper()==number and allowed(d['id'])]
        if len(found)!=1:missing.append(number)
        else:requested.extend(found)
    blocked=False
    if route in ('summary','compare'):
        required=2 if route=='compare' else 1
        if len(requested if resolution else numbers)<required:
            notes.append('Name '+('at least two circular numbers for comparison.' if route=='compare' else 'the circular number to summarise.'));blocked=True
        if missing:
            notes.append('Required circulars are missing, excluded by filters, or ambiguous: '+', '.join(missing)+'. No complete answer was attempted.');blocked=True
        if not blocked:
            # Round-robin across sections and documents preserves breadth under a cap.
            queues={}
            for doc in requested:
                groups=collections.defaultdict(list)
                for p in engine.parts_by_doc[doc]:groups[p.get('section_id','')].append(p)
                queue=[]
                while any(groups.values()):
                    for group in groups.values():
                        if group:queue.append(group.pop(0))
                queues[doc]=queue
            while any(queues.values()):
                for doc,queue in queues.items():
                    if queue:add(queue.pop(0),'document_coverage')
            for doc in requested:
                total=len(engine.parts_by_doc[doc]);included=sum(p['document_id']==doc for p in selected)
                coverage[doc]={'included_chunks':included,'total_chunks':total,'complete':included==total}
                if resolution:
                    from product_scope import source_coverage
                    source=source_coverage(engine,doc);coverage[doc].update(source,available_text_complete=included==total)
                    coverage[doc]['complete']=included==total and not source['empty_pages'] and source['page_count_verified']
                    if source['empty_pages']:notes.append(doc+': missing extracted text on source pages '+', '.join(map(str,source['empty_pages']))+'. Full-source coverage is incomplete.')
                    if not source['page_count_verified']:notes.append(doc+': original PDF page count is unverified. Coverage refers only to available Markdown text.')
            if route=='compare' and any(not v['included_chunks'] for v in coverage.values()):
                selected=[];seen=set();used=0;notes.append('Budget did not permit evidence from every requested document; comparison withheld.')
            seed_ids=[p['id'] for p in selected]
    else:
        candidate_ids=set(requested) if resolution and requested else resolution['eligible_ids'] if resolution else None
        candidates=engine.search(query,method,series,cutoff,32,feature,candidate_mode=True,document_ids=candidate_ids)
        if numbers and not resolution:candidates=[p for p in candidates if str(p['circular_number']).upper() in numbers]
        if do_rerank and candidates:
            ranker=get_reranker(Path(__file__).parent/engine.config.get('reranker_path','models/reranker'))
            start=time.perf_counter();candidates=ranker.rank(query,candidates);rerank_ms=round((time.perf_counter()-start)*1000);ranked_count=len(candidates);reranker_model=ranker.model
        seeds=[];counts=collections.Counter()
        for p in candidates:
            cap=8 if len(numbers)==1 else 3
            if counts[p['document_id']]>=cap:continue
            seeds.append(p);counts[p['document_id']]+=1
            if len(seeds)>=8:break
        seed_ids=[p['id'] for p in seeds]
        for p in seeds:add(p,'direct_match')
        if scope=='related' and seeds:
            seed_docs=list(dict.fromkeys(p['document_id'] for p in seeds));expanded=set(seed_docs)
            terms=set(engine.query_terms(query))
            def relevance(p):return len(terms.intersection(engine.query_terms(p['text'])))
            links=0
            for doc in seed_docs[:2]:
                for edge in engine.registry.edges:
                    if edge['from_id']==doc and edge['status']!='resolved':notes.append(f"Unresolved reference {edge['reference']}: {edge['status']}; no text inferred.")
                for target,direction,edge in engine.registry.neighboring_documents(doc):
                    if target in expanded or not allowed(target):continue
                    if links>=2:notes.append('Additional reference documents omitted by expansion limit.');continue
                    choices=engine.parts_by_doc[target]
                    if choices:
                        best=max(choices,key=relevance)
                        if add(best,'recorded_reference',doc,dict(edge,direction=direction)):expanded.add(target);links+=1
            query_features={r['id'] for r in engine.registry.rules if re.search(r['pattern'],query,re.I)}
            choices=[p for p in engine.parts if p['document_id'] not in expanded and allowed(p['document_id']) and query_features.intersection(p.get('feature_ids',[])) and relevance(p)>0]
            if choices:add(max(choices,key=relevance),'same_feature')
            neighbors=0
            for seed in seeds:
                for key in ('previous_chunk_id','next_chunk_id'):
                    p=engine.parts_by_id.get(seed.get(key))
                    if p and p['document_id']==seed['document_id'] and p.get('section_id')==seed.get('section_id') and neighbors<6 and add(p,'adjacent_context',seed['document_id']):neighbors+=1
    if resolution:
        for doc in dict.fromkeys(p['document_id'] for p in selected):
            info=engine.by_id[doc]
            if info.get('metadata_quality')=='inventory_unverified':notes.append('Imported document metadata and extraction remain unverified; consult the original PDFs. Unknown issue dates are excluded when using an issue-date cutoff.')
            if info.get('source_coverage',{}).get('empty_pages'):notes.append(doc+': some source pages have no extracted text. The answer may omit requirements.')
    return selected,dict(route=route,scope=scope,seed_chunk_ids=seed_ids,included_chunk_ids=[p['id'] for p in selected],
        evidence_characters=used,character_budget=budget,max_reference_hops=1,notes=list(dict.fromkeys(notes)),
        document_coverage=coverage,requested_circulars=numbers,reranker={'enabled':bool(do_rerank and route=='clause'),'model':reranker_model,'candidate_count':ranked_count,'elapsed_ms':rerank_ms})
