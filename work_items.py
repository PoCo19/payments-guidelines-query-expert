"""Local, versioned research work. Human review is attribution, not authentication."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import uuid
import time
import urllib.parse
import urllib.request
from contextlib import contextmanager
from answer_format import answer_markdown


def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def runtime_models(engine, force=False):
    """Bounded localhost metadata check; never download or load model weights."""
    base=engine.config.get('ollama_url')
    if not base:
        return dict(status='not_configured',digests={})
    cached=getattr(engine,'_workflow_models',None)
    if not force and cached and time.monotonic()-cached[0]<30:
        return cached[1]
    try:
        parsed=urllib.parse.urlsplit(base)
        if parsed.scheme!='http' or parsed.hostname not in ('127.0.0.1','localhost','::1'):
            raise ValueError('Local model metadata only')
        with urllib.request.build_opener(urllib.request.ProxyHandler({})).open(base.rstrip('/')+'/api/tags',timeout=2) as reply:
            models=json.load(reply)['models']
        selected={engine.config.get(k) for k in ('generation_model','embedding_model')} - {None,''}
        found={m['name']:m['digest'] for m in models if m.get('name') in selected}
        value=dict(status='available' if set(found)==selected else 'missing_model',digests=found)
    except (OSError,ValueError,KeyError,TypeError):
        value=dict(status='unavailable',digests={})
    engine._workflow_models=(time.monotonic(),value)
    return value


def snapshot(engine, result):
    ids = sorted({s['document_id'] for s in result.get('sources', [])})
    return dict(corpus=engine.fingerprint,
        sources={key: digest(dict(document=engine.by_id.get(key),
            pages=[p for p in engine.pages if p['document_id'] == key])) for key in ids},
        models={k: engine.config.get(k) for k in ('generation_model', 'embedding_model', 'context_length', 'max_output_tokens')},
        installed_models=runtime_models(engine),
        graph=getattr(getattr(engine, 'evidence_graph', None), 'fingerprint', None))


def check_text(text, sources):
    if not isinstance(text, str) or not text.strip() or len(text) > 24000:
        raise ValueError('Provide an answer of 1–24,000 characters.')
    ids = {s['citation'] for s in sources}
    cited = set(re.findall(r'\bS\d+\b', text))
    if not cited <= ids:
        raise ValueError('Answer contains an unknown citation: ' + ', '.join(sorted(cited - ids)))
    if not cited:
        raise ValueError('Include at least one source citation, for example [S1].')


def finding_labels(value, result):
    """Analyst classification of immutable accepted claims, not a new AI verdict."""
    if not isinstance(value, dict): raise ValueError('Invalid finding labels.')
    allowed = {'change', 'retained', 'unresolved'}
    keys = {str(i) for i, _ in enumerate(result.get('claims', []))}
    if any(k not in keys or v not in allowed for k, v in value.items()):
        raise ValueError('Choose a valid finding and classification.')
    return value


def request_payload(kind, payload, engine):
    if kind not in ('query', 'impact'):
        raise ValueError('Choose Query Desk or Change-Impact Brief.')
    query = payload.get('query', '')
    limit = 1000 if kind == 'impact' else 2000
    if not isinstance(query, str) or not 1 <= len(query.strip()) <= limit:
        raise ValueError(f'Enter a question of 1–{limit:,} characters.')
    context = payload.get('operating_context', '')
    if not isinstance(context, str) or len(context) > 4000:
        raise ValueError('Operating context must be at most 4,000 characters.')
    ids = payload.get('document_ids', [])
    if not isinstance(ids, list) or not all(isinstance(x, str) for x in ids) or len(set(ids)) != len(ids) or len(ids) > 6:
        raise ValueError('Choose up to six distinct documents.')
    if any(x not in engine.by_id or engine.by_id[x]['availability'] != 'converted' for x in ids):
        raise ValueError('Selected document is unavailable.')
    if kind == 'impact' and len(ids) < 2:
        raise ValueError('Choose the changed document first and at least one earlier source.')
    series = payload.get('series', '')
    if not isinstance(series, str) or len(series) > 80:
        raise ValueError('Invalid product.')
    cutoff = payload.get('cutoff', '')
    if cutoff:
        try: dt.date.fromisoformat(cutoff)
        except (ValueError, TypeError): raise ValueError('Use an ISO date for the issue cutoff.')
    audience = payload.get('audience', '')
    if not isinstance(audience, str) or len(audience) > 120:
        raise ValueError('Audience must be at most 120 characters.')
    result = dict(query=query.strip(), operating_context=context, document_ids=ids, series=series, cutoff=cutoff)
    if audience: result['audience'] = audience.strip()
    return result


def related_sources(engine, key):
    """Navigation candidates only: never infer amendment or legal precedence."""
    if key not in engine.by_id: raise ValueError('Document not found.')
    seed = engine.by_id[key]
    reasons = {}
    registry = getattr(engine, 'registry', None)
    if registry:
        for target, direction, edge in registry.neighboring_documents(key):
            reason = 'Selected source references this document' if direction == 'referenced_by_seed' else 'This document references the selected source'
            evidence = {'source_anchor_reviewed':'source-anchored link reviewed',
                        'number_occurrence_only':'reference metadata; number found in extracted text',
                        'metadata_only':'reference metadata; source text not verified'}.get(edge.get('evidence_status'),'relationship evidence requires review')
            reasons.setdefault(target, []).append(reason + ' (' + evidence + ')')
    for target, doc in engine.by_id.items():
        if target != key and seed.get('family') and doc.get('family') == seed['family'] and doc.get('series') == seed.get('series'):
            reasons.setdefault(target, []).append('Same numbering family; relationship requires verification')
    rows = []
    for target, why in reasons.items():
        doc = engine.by_id.get(target)
        if not doc or target == key or doc.get('availability') != 'converted': continue
        date, seed_date = doc.get('issue_date'), seed.get('issue_date')
        chronology = ('earlier' if date < seed_date else 'same date' if date == seed_date else 'later') if date and seed_date else 'date not established'
        rows.append(dict(document=doc, reasons=why, chronology=chronology))
    return sorted(rows, key=lambda r: (r['chronology'] != 'earlier', r['document']['id']))[:30]


class WorkStore:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript("""
            CREATE TABLE IF NOT EXISTS work_items(
              id TEXT PRIMARY KEY, kind TEXT NOT NULL, title TEXT NOT NULL,
              state TEXT NOT NULL, version INTEGER NOT NULL, revision INTEGER NOT NULL,
              busy INTEGER NOT NULL DEFAULT 0, created TEXT NOT NULL, updated TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS work_versions(
              item_id TEXT NOT NULL, version INTEGER NOT NULL, body TEXT NOT NULL,
              PRIMARY KEY(item_id,version));
            CREATE TABLE IF NOT EXISTS work_events(
              id INTEGER PRIMARY KEY, item_id TEXT NOT NULL, version INTEGER NOT NULL,
              at TEXT NOT NULL, action TEXT NOT NULL, reviewer TEXT NOT NULL, note TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS work_visibility(
              item_id TEXT PRIMARY KEY, disposition TEXT NOT NULL);
            """)
            for row in db.execute('SELECT * FROM work_items WHERE busy=1').fetchall():
                db.execute("UPDATE work_items SET busy=0,state='Draft',revision=revision+1,updated=? WHERE id=?", (stamp(),row['id']))
                self.event(db, row, 'interrupted', '', 'Generation interrupted by server restart; retry. Previous versions preserved.')

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=15)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def event(self, db, item, action, reviewer='', note=''):
        db.execute('INSERT INTO work_events(item_id,version,at,action,reviewer,note) VALUES(?,?,?,?,?,?)',
                   (item['id'],item['version'],stamp(),action,reviewer,note))

    def row(self, db, key):
        row = db.execute('SELECT * FROM work_items WHERE id=?', (key,)).fetchone()
        if not row: raise ValueError('Work item not found.')
        item = dict(row)
        disposition = db.execute('SELECT disposition FROM work_visibility WHERE item_id=?', (key,)).fetchone()
        item['disposition'] = disposition[0] if disposition else 'active'
        return item

    def body(self, db, item):
        return json.loads(db.execute('SELECT body FROM work_versions WHERE item_id=? AND version=?',
                                    (item['id'], item['version'])).fetchone()[0])

    def fresh(self, db, item, engine):
        # A reader must not change the optimistic revision while a replacement
        # is being generated. The result gets a fresh snapshot before saving.
        if item['busy']:
            return item
        body = self.body(db, item)
        if body.get('snapshot') and snapshot(engine, body.get('result', {})) != body['snapshot']:
            if item['state'] != 'Needs revalidation':
                db.execute("UPDATE work_items SET state='Needs revalidation',revision=revision+1,updated=? WHERE id=?",(stamp(),item['id']))
                self.event(db,item,'source_or_configuration_changed',note='Source corpus or model/graph configuration changed. Regenerate before approval.')
                item = self.row(db,item['id'])
        return item

    def expected(self, item, revision, allow_hidden=False):
        if type(revision) is not int or revision != item['revision']:
            raise ValueError('This work item changed. Reload before continuing.')
        if item['busy']: raise ValueError('Generation is running. Wait before editing or reviewing.')
        if not allow_hidden and item.get('disposition', 'active') != 'active':
            raise ValueError('Restore this work item before editing, generating or reviewing.')

    def get(self, key, engine):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            item = self.fresh(db,self.row(db,key),engine)
            item['draft'] = self.body(db,item)
            item['history'] = [dict(r) for r in db.execute('SELECT * FROM work_events WHERE item_id=? ORDER BY id', (key,))]
            item['versions'] = [dict(version=r['version'], **json.loads(r['body'])) for r in db.execute('SELECT * FROM work_versions WHERE item_id=? ORDER BY version',(key,))]
            return item

    def list(self, engine):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            return [self.fresh(db,self.row(db,r['id']),engine) for r in db.execute('SELECT id FROM work_items ORDER BY updated DESC').fetchall()]

    def visibility(self, key, payload, engine):
        value = payload.get('disposition')
        if value not in ('active', 'archived', 'trash'): raise ValueError('Choose archive, trash or restore.')
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            item = self.fresh(db,self.row(db,key),engine)
            self.expected(item,payload.get('revision'),allow_hidden=True)
            db.execute('INSERT OR REPLACE INTO work_visibility VALUES(?,?)',(key,value))
            db.execute('UPDATE work_items SET revision=revision+1,updated=? WHERE id=?',(stamp(),key))
            self.event(db,item,'restored' if value=='active' else value,note='All versions and review history retained.')
        return self.get(key,engine)

    def import_answer(self, job, engine):
        """Import only a completed server-owned research job, never browser evidence."""
        if job.get('status') != 'completed' or not job.get('research_snapshot'):
            raise ValueError('No completed research answer is available in this server session.')
        response = job['result']
        original = job['research_request']
        if original.get('mode') != 'generate' or not response.get('claims') or not response.get('sources'):
            raise ValueError('Generate a cited answer before saving it to Query Desk.')
        if job['research_snapshot'] != snapshot(engine,response):
            raise ValueError('Sources or model settings changed. Run the research question again before saving.')
        request = request_payload('query', original, engine)
        text = '\n\n'.join(c['text']+' ['+', '.join(c['sources'])+']' for c in response['claims'])
        check_text(text,response['sources'])
        key = uuid.uuid4().hex
        body = dict(request=request,origin_request=original,result=response,text=text,actions='',reviewer_questions='',
                    snapshot=job['research_snapshot'],created=stamp(),edited_by_human=False)
        with self.connect() as db:
            db.execute('INSERT INTO work_items VALUES(?,?,?,?,?,?,?,?,?)',(key,'query',request['query'][:140],'Draft',1,1,0,stamp(),stamp()))
            db.execute('INSERT INTO work_versions VALUES(?,?,?)',(key,1,json.dumps(body,ensure_ascii=False)))
            self.event(db,self.row(db,key),'research_answer_saved',note='Question, retrieval settings, cited answer and source snapshot copied from completed local research job.')
        return self.get(key,engine)

    def create(self, payload, engine):
        kind = payload.get('kind', 'query')
        request = request_payload(kind,payload,engine)
        key = uuid.uuid4().hex
        body = dict(request=request, result={}, text='', actions='', reviewer_questions='', snapshot=None, created=stamp())
        with self.connect() as db:
            db.execute("INSERT INTO work_items VALUES(?,?,?,?,?,?,?,?,?)",(key,kind,request['query'][:140],'Draft',1,1,0,stamp(),stamp()))
            db.execute('INSERT INTO work_versions VALUES(?,?,?)',(key,1,json.dumps(body,ensure_ascii=False)))
            self.event(db,self.row(db,key),'created')
        return self.get(key,engine)

    def append(self, db, item, body, state, action):
        version = item['version']+1
        body['created'] = stamp()
        db.execute('INSERT INTO work_versions VALUES(?,?,?)',(item['id'],version,json.dumps(body,ensure_ascii=False)))
        db.execute('UPDATE work_items SET version=?,revision=revision+1,state=?,busy=0,updated=?,title=? WHERE id=?',
                   (version,state,stamp(),body['request']['query'][:140],item['id']))
        self.event(db,self.row(db,item['id']),action)

    def generate(self, key, revision, engine):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            item = self.row(db,key); self.expected(item,revision)
            body = self.body(db,item)
            request = request_payload(item['kind'],body['request'],engine)
            db.execute("UPDATE work_items SET busy=1,state='Draft',revision=revision+1 WHERE id=?",(key,))
            self.event(db,item,'generation_started')
        try:
            query = request['query']
            if item['kind'] == 'impact':
                query = ('Compare the selected sources to answer: '+query+
                    '\nUser-designated changed source: '+engine.by_id[request['document_ids'][0]].get('subject',request['document_ids'][0])[:200]+
                    '\nThe first selected document is the proposed changed source; do not assume it supersedes the others. '
                    'Explain documented changes, retained requirements, conditions, dates and unresolved evidence. '
                    'Distinguish a new requirement from a later reference to an earlier requirement. '
                    'Do not assert institution-specific impact or implementation actions.')
            answer_request = dict(query=query, mode='generate', method='hybrid', rerank=True,
                scope='related', route='compare' if item['kind']=='impact' else 'auto',
                document_ids=request['document_ids'], series=request['series'], cutoff=request['cutoff'], answer_style='auto')
            if body.get('origin_request'):
                answer_request.update(body['origin_request'])
                answer_request.update(query=query,document_ids=request['document_ids'],series=request['series'],cutoff=request['cutoff'],mode='generate')
            response = engine.answer(answer_request)
            text = '\n\n'.join(c['text']+' ['+', '.join(c['sources'])+']' for c in response.get('claims',[]))
            if not text: text = response.get('answer','')
            actions = ('Review checklist suggestions, not inferred institutional impacts:\n'
                '- Product and operations: assess whether the documented change affects your processes.\n'
                '- Compliance or policy owner: verify applicability, dates and retained obligations.\n'
                '- Customer support: review whether approved guidance needs updating.\n'
                '- Transaction risk owner: assess whether internal rules need review; no live rule configuration is inferred.'
                if item['kind']=='impact' else '')
            questions = ('Are the selected earlier sources a complete baseline? Which obligations are retained? '
                'What effective dates and exceptions need original-source verification? '
                'Which internal process or rule evidence establishes institution-specific impact?'
                if item['kind']=='impact' else '')
            updated = dict(request=request,result=response,text=text,actions=actions,reviewer_questions=questions,
                snapshot=snapshot(engine,response), edited_by_human=False)
            if body.get('origin_request'): updated['origin_request'] = body['origin_request']
            with self.connect() as db:
                db.execute('BEGIN IMMEDIATE')
                current = self.row(db,key)
                if not current['busy'] or current['revision'] != revision+1:
                    raise ValueError('Work changed during generation; result not saved.')
                self.append(db,current,updated,'Draft','generated')
        except Exception:
            with self.connect() as db:
                db.execute("UPDATE work_items SET busy=0,revision=revision+1,updated=? WHERE id=?",(stamp(),key))
                self.event(db,self.row(db,key),'generation_failed',note='No generated result saved; retry or inspect earlier versions.')
            raise
        return self.get(key,engine)

    def edit(self, key, payload, engine):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            item = self.fresh(db,self.row(db,key),engine);self.expected(item,payload.get('revision'))
            old = self.body(db,item)
            request = request_payload(item['kind'],payload.get('request',old['request']),engine)
            if request != old['request']:
                body = dict(request=request,result={},text='',actions='',reviewer_questions='',snapshot=None)
                if old.get('origin_request'): body['origin_request'] = old['origin_request']
            else:
                if item['state']=='Needs revalidation': raise ValueError('Regenerate with the current sources before editing.')
                text = payload.get('text',old['text'])
                check_text(text,old.get('result',{}).get('sources',[]))
                body = dict(old,text=text,edited_by_human=True)
                for field in ('actions','reviewer_questions'):
                    value = payload.get(field,old.get(field,''))
                    if not isinstance(value,str) or len(value)>8000:raise ValueError('Notes must be at most 8,000 characters.')
                    body[field]=value
                if item['kind']=='impact':
                    labels = finding_labels(payload.get('finding_labels',old.get('finding_labels',{})),old.get('result',{}))
                    # Labels describe generated claims, never silently attach to edited prose.
                    generated_text = '\n\n'.join(c['text']+' ['+', '.join(c['sources'])+']' for c in old.get('result',{}).get('claims',[]))
                    body['finding_labels'] = labels if text == generated_text else {}
            self.append(db,item,body,'Draft','edited')
        return self.get(key,engine)

    def review(self,key,payload,engine):
        decision=payload.get('decision')
        if decision not in ('submit','approve','reject'):raise ValueError('Choose submit, approve or reject.')
        reviewer=payload.get('reviewer','');note=payload.get('note','')
        if not isinstance(reviewer,str) or len(reviewer)>120 or not isinstance(note,str) or len(note)>4000:
            raise ValueError('Invalid reviewer or note.')
        if decision=='approve':runtime_models(engine,force=True)
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            item=self.fresh(db,self.row(db,key),engine);self.expected(item,payload.get('revision'))
            body=self.body(db,item)
            if decision=='submit':
                if item['state']!='Draft':raise ValueError('Only a draft can be submitted.')
                check_text(body['text'],body.get('result',{}).get('sources',[]))
                state='Needs review'
            else:
                if item['state']!='Needs review':raise ValueError('Submit this version for review first.')
                if not reviewer.strip() or not note.strip():raise ValueError('Record reviewer name and review rationale.')
                if decision=='approve':
                    if payload.get('sources_verified') is not True or payload.get('qualifications_verified') is not True:
                        raise ValueError('Verify original sources and material qualifications before approval.')
                    check_text(body['text'],body['result'].get('sources',[]))
                    if not body['snapshot'] or body['snapshot']!=snapshot(engine,body['result']):
                        raise ValueError('Sources changed; regenerate before approval.')
                    if body['snapshot']['installed_models']['status'] not in ('available','not_configured'):
                        raise ValueError('Model fingerprints are unavailable; restore the configured models and regenerate before approval.')
                state='Approved' if decision=='approve' else 'Rejected'
            db.execute('UPDATE work_items SET state=?,revision=revision+1,updated=? WHERE id=?',(state,stamp(),key))
            attest = ' Original sources/citations and material qualifications attested by reviewer.' if decision=='approve' else ''
            self.event(db,item,decision,reviewer.strip(),note.strip()+attest)
        return self.get(key,engine)

    def export(self,key,engine):
        runtime_models(engine,force=True)
        item=self.get(key,engine);body=item['draft']
        result=body.get('result',{})
        generated='\n\n'.join(c['text']+' ['+', '.join(c['sources'])+']' for c in result.get('claims',[]))
        presented=answer_markdown(result) if result.get('claims') and body['text']==generated else body['text']
        lines=['# '+item['title'],'Status: '+item['state']+' | Version: '+str(item['version']),
            'Location: '+item.get('disposition','active'),
            'Local reviewer attribution is not authentication. Imported snapshots do not certify current applicability.',
            '## Question',body['request']['query'],'## Documented findings',presented]
        if body['request'].get('audience'): lines+=['## Intended audience',body['request']['audience']]
        if body.get('origin_request'): lines+=['## Original research settings',json.dumps(body['origin_request'],indent=2,ensure_ascii=False)]
        if item['kind']=='impact':
            lines+=['## Supplied operating context (not independently verified)',body['request'].get('operating_context') or 'Not supplied; institution-specific impact is not established.',
                '## Analyst-proposed actions (not source requirements)',body.get('actions') or 'Pending analyst assessment.',
                '## Questions for review',body.get('reviewer_questions') or 'Check applicability, completeness and required internal evidence.']
            if body.get('finding_labels'):
                lines += ['## Analyst classification of generated findings', 'These labels are analyst judgments, not automated findings of supersession.']
                names = dict(change='Documented change',retained='Retained requirement',unresolved='Unresolved finding')
                for index, label in body['finding_labels'].items():
                    claim = body['result']['claims'][int(index)]
                    lines += [names[label]+': '+claim['text']+' ['+', '.join(claim['sources'])+']']
        lines+=['## Review history',json.dumps(item['history'],indent=2,ensure_ascii=False),'## Snapshot',json.dumps(body.get('snapshot'),indent=2),'## Sources']
        for s in body.get('result',{}).get('sources',[]):
            lines += [f"### {s['citation']} — {s.get('title',s['document_id'])}, page {s.get('page')}",
                s.get('source_url',''),s.get('text','')]
        lines+=['## Automated review limitations',json.dumps(dict(coverage=body.get('result',{}).get('coverage_check'),
            withheld=body.get('result',{}).get('flagged_claims',[]),warnings=body.get('result',{}).get('warnings',[])),indent=2,ensure_ascii=False)]
        return '\n\n'.join(lines)
