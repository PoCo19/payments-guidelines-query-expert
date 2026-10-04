"""Transactional launch state, version-bound reviews and dependency invalidation."""
from __future__ import annotations
import copy
import hashlib
import json
import re
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path
from contextlib import contextmanager

TEAMS = {'cs': 'Customer Success', 'marketing': 'Marketing', 'bd': 'Business Development', 'risk': 'Risk'}
WORKSPACE_TYPES = {'existing':'Existing feature review','change':'Feature change','new_launch':'New feature launch'}
ROLES = {'product', *TEAMS}


class Conflict(ValueError):
    pass


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def uid(prefix):
    return prefix + '_' + uuid.uuid4().hex[:12]


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def clean(value, limit=10000, required=True):
    if not isinstance(value, str) or len(value) > limit or (required and not value.strip()):
        raise ValueError(f'Expected text of 1–{limit} characters' if required else f'Expected text up to {limit} characters')
    return value.strip()


def actor(payload):
    name = clean(payload.get('actor'), 100)
    role = payload.get('role')
    if role not in ROLES:
        raise ValueError('Choose a review role')
    return name, role


def permitted(role, team=None):
    if role != 'product' and role != team:
        raise ValueError('This action belongs to the product owner or the relevant team')


def normal(text):
    return ' '.join(text.split()).casefold()


def find(items, key):
    for item in items:
        if item['id'] == key:
            return item
    raise ValueError('Record not found')


def fact_signature(fact):
    return digest({k: fact[k] for k in ('id', 'label', 'value', 'source_id', 'quote')})


def source_refs(workspace, references, scope='shared'):
    if not isinstance(references, list) or len(references) > 8:
        raise ValueError('Invalid source references')
    for ref in references:
        if not isinstance(ref, dict):
            raise ValueError('Invalid reference')
        source = find(workspace['sources'], ref.get('source_id'))
        quote = clean(ref.get('quote'), 2000)
        if source['scope'] not in ('shared', scope):
            raise ValueError('Reference is outside this team context')
        if normal(quote) not in normal(source['text']):
            raise ValueError('The quotation does not match the selected source. Copy its exact wording or choose the correct supporting source.')


def fact_valid(workspace, raw, existing_id=None):
    fact = {'id': existing_id or uid('fact'), 'label': clean(raw.get('label'), 120),
            'value': clean(raw.get('value'), 1600), 'source_id': clean(raw.get('source_id'), 100),
            'quote': clean(raw.get('quote'), 2000)}
    source_refs(workspace, [fact])
    return fact


def team_input(workspace, team):
    """Only feature facts and sources explicitly shared with this team enter its prompt."""
    return {'title': workspace['title'], 'brief': workspace['brief'], 'workspace_type':workspace.get('workspace_type','new_launch'), 'facts': workspace['facts'],
            'sources': [s for s in workspace['sources'] if s['scope'] in ('shared', team)],
            'partners': workspace['partners'] if team == 'bd' else [],
            'controls': workspace['controls'] if team == 'risk' else [],
            'risk_rules':workspace.get('risk_rules',[]) if team=='risk' else []}


def next_step(w):
    if not any(s['scope']=='shared' for s in w['sources']): return {'view':'sources','label':'Add source evidence','description':'Find a UPI circular or upload a document to get started.'}
    if not w['facts']: return {'view':'brief','label':'Prepare the feature brief','description':'Turn your selected sources into a short, cited brief.'}
    if not approved_facts(w): return {'view':'brief','label':'Review the feature brief','description':'Check the facts and resolve questions before preparing team work.'}
    for team,label in TEAMS.items():
        a=w['artifacts'].get(team)
        if not a or a['status']=='stale': return {'view':'teams','team':team,'label':'Prepare '+label+' work','description':'Create a draft from the current approved brief.'}
    for team,label in TEAMS.items():
        if w['artifacts'][team]['status']!='approved': return {'view':'teams','team':team,'label':'Review '+label+' work','description':'Check the draft, resolve questions and record the review.'}
    for task in w['tasks']:
        if task['critical'] and task['status']!='done':
            pending=[find(w['tasks'],i) for i in task['depends_on'] if find(w['tasks'],i)['status']!='done']
            task=pending[0] if pending else task
            return {'view':'actions','task_id':task['id'],'label':'Complete '+task['title'].lower(),'description':'Record an owner and evidence, then mark the action complete.'}
    complete=bool(w.get('decision') and w['decision']['status']=='recorded')
    return {'view':'actions','label':'View completed review' if complete else 'Record the final review','description':'All required reviews and actions are complete. Open the decision or export the review pack.' if complete else 'Review the team sign-offs and record the product owner’s decision.'}


def approved_facts(workspace):
    return bool(workspace['facts']) and workspace.get('fact_approval', {}).get('hash') == digest(workspace['facts'])


def issues(workspace):
    results = []
    for team, artifact in workspace['artifacts'].items():
        for item in artifact['items']:
            # Deliberately narrow, inspectable guardrails. Broader meaning is a human review task.
            text = normal(item['body'])
            for pattern, message in [(r'\b(?:all|every) (?:banks?|apps?|customers?)\b', 'Universal availability claim needs a narrower, supported scope'),
                                     (r'\b(?:risk.free|100% secure|zero risk|guaranteed approval)\b', 'Absolute safety or approval claim is not permitted')]:
                if re.search(pattern, text):
                    results.append({'team': team, 'item_id': item['id'], 'message': message, 'kind': 'claim_guard'})
        if artifact.get('open_questions') or any(i['kind']=='open_question' for i in artifact['items']):
            results.append({'team': team, 'kind': 'open_questions', 'message': 'Resolve or explicitly disposition open questions before approval'})
    return results


def readiness(workspace):
    blockers = []
    if not approved_facts(workspace):
        blockers.append('Product owner must approve the current feature facts')
    for team, label in TEAMS.items():
        if workspace['artifacts'].get(team, {}).get('status') != 'approved':
            blockers.append(f'{label} deliverable is not approved for its current inputs')
    blockers.extend(f'{TEAMS[i["team"]]}: {i["message"]}' for i in issues(workspace))
    for task in workspace['tasks']:
        if task['critical'] and task['status'] != 'done':
            blockers.append(f'{task["title"]} — {task["status"]}')
    return {'ready': not blockers, 'blockers': blockers, 'completed_tasks': sum(t['status'] == 'done' for t in workspace['tasks']),
            'total_tasks': len(workspace['tasks'])}


def invalidate(workspace, teams, reason):
    direct = set(teams)
    affected = set(direct)
    changed = True
    while changed:
        changed = False
        for task in workspace['tasks']:
            if any(find(workspace['tasks'], dep)['team'] in affected for dep in task['depends_on']) and task['team'] not in affected:
                affected.add(task['team']); changed = True
    # Task sequencing is not a content dependency: downstream tasks reopen, but
    # a deliverable is stale only when its own supplied inputs changed.
    for team in direct:
        artifact = workspace['artifacts'].get(team)
        if artifact:
            artifact['status'] = 'stale'
            artifact['stale_reason'] = reason
    for task in workspace['tasks']:
        if task['team'] in affected and task['status'] == 'done':
            task['status'] = 'todo'
            task['reopened_reason'] = reason
    if workspace.get('decision'):
        workspace['decision']['status'] = 'requires_review'
        workspace['decision']['reason'] = reason
    return sorted(affected)


def validate_pack(workspace, team, raw):
    if not isinstance(raw, dict) or not isinstance(raw.get('items'), list) or not 1 <= len(raw['items']) <= 12:
        raise ValueError('A deliverable needs 1–12 items')
    fact_ids = {f['id'] for f in workspace['facts']}
    items = []
    for entry in raw['items']:
        if not isinstance(entry, dict) or entry.get('kind') not in ('source_summary', 'proposal', 'open_question'):
            raise ValueError('Every item must distinguish source summary, proposal or open question')
        refs = entry.get('fact_ids')
        if not isinstance(refs, list) or len(refs) > 30 or any(not isinstance(x, str) or x not in fact_ids for x in refs):
            raise ValueError('Unknown fact reference')
        if entry['kind'] == 'source_summary' and not refs:
            raise ValueError('Source summaries need supporting feature facts')
        extra = entry.get('source_refs', [])
        source_refs(workspace, extra, team)
        items.append({'id': uid('item'), 'title': clean(entry.get('title'), 160), 'body': clean(entry.get('body'), 3500),
                      'kind': entry['kind'], 'fact_ids': list(dict.fromkeys(refs)), 'source_refs': extra})
    questions = raw.get('open_questions', [])
    if not isinstance(questions, list) or len(questions) > 15:
        raise ValueError('Invalid open questions')
    assessments=[]
    if team=='risk':
        rules={r['id']:r for r in workspace.get('risk_rules',[])}
        for a in raw.get('rule_assessments',[]):
            if a.get('rule_id') not in rules or a.get('rule_id') in {x['rule_id'] for x in assessments}: raise ValueError('Each rule assessment must reference a different saved transaction rule')
            if a.get('applicability') not in ('relevant','possibly_relevant','not_relevant'): raise ValueError('Choose rule applicability')
            if a.get('recommendation') not in ('retain','review','tune','retire','needs_evidence'): raise ValueError('Choose a rule recommendation')
            assessments.append({'rule_id':a['rule_id'],'applicability':a['applicability'],'recommendation':a['recommendation'],'rationale':clean(a.get('rationale'),2000),'proposed_change':clean(a.get('proposed_change',''),2000,False)})
        if rules and set(rules)!={a['rule_id'] for a in assessments}: raise ValueError('Assess every saved transaction rule before saving this risk draft')
    return {'items': items, 'open_questions': [clean(q, 1000) for q in questions], 'rule_assessments':assessments}


class Store:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS launches(id TEXT PRIMARY KEY, revision INTEGER NOT NULL, body TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, launch_id TEXT, revision INTEGER, created TEXT, actor TEXT, action TEXT, detail TEXT);
                CREATE TABLE IF NOT EXISTS jobs(id TEXT PRIMARY KEY, launch_id TEXT NOT NULL, kind TEXT NOT NULL, team TEXT,
                    state TEXT NOT NULL, created TEXT NOT NULL, updated TEXT NOT NULL, input_hash TEXT NOT NULL,
                    request TEXT NOT NULL, result TEXT, error TEXT);
                CREATE INDEX IF NOT EXISTS events_launch ON events(launch_id,id);
                CREATE INDEX IF NOT EXISTS jobs_launch ON jobs(launch_id,created);
                CREATE INDEX IF NOT EXISTS jobs_state ON jobs(state);
            ''')
            db.execute('PRAGMA journal_mode=WAL')

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=15)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def _read(self, db, launch_id):
        row = db.execute('SELECT body FROM launches WHERE id=?', (launch_id,)).fetchone()
        if not row:
            raise ValueError('Launch not found')
        w=json.loads(row['body'])
        w.setdefault('workspace_type','new_launch');w.setdefault('risk_rules',[])
        return w

    def _write(self, db, w, name, action, detail=None):
        w['revision'] += 1
        w['updated'] = now()
        db.execute('UPDATE launches SET revision=?,body=? WHERE id=?', (w['revision'], json.dumps(w), w['id']))
        db.execute('INSERT INTO events(launch_id,revision,created,actor,action,detail) VALUES(?,?,?,?,?,?)',
                   (w['id'], w['revision'], now(), name, action, json.dumps(detail or {})))

    def list(self):
        with self.connect() as db:
            launches = [json.loads(r['body']) for r in db.execute('SELECT body FROM launches ORDER BY rowid DESC')]
        return [{'id': w['id'], 'title': w['title'], 'revision': w['revision'], 'updated': w['updated'],
                 'simulated': w['simulated'], 'ready': readiness(w)['ready'],'workspace_type':w.get('workspace_type','new_launch'),
                 'sources':len(w['sources']),'facts_approved':approved_facts(w),'approved_teams':sum(a['status']=='approved' for a in w['artifacts'].values()),'decision_recorded':bool(w.get('decision') and w['decision']['status']=='recorded')} for w in launches]

    def get(self, launch_id):
        with self.connect() as db:
            db.execute('BEGIN')
            w = self._read(db, launch_id)
            w['events'] = [dict(r, detail=json.loads(r['detail'])) for r in db.execute('SELECT * FROM events WHERE launch_id=? ORDER BY id DESC LIMIT 100', (launch_id,))]
            w['jobs'] = [self.job_view(r) for r in db.execute('SELECT * FROM jobs WHERE launch_id=? ORDER BY created DESC,rowid DESC LIMIT 30', (launch_id,))]
        w['readiness'] = readiness(w)
        w['issues'] = issues(w)
        w['facts_approved'] = approved_facts(w)
        w['next_step']=next_step(w)
        return w

    @staticmethod
    def job_view(row):
        return dict({k: row[k] for k in ('id', 'kind', 'team', 'state', 'created', 'updated', 'error')},mode=json.loads(row['request']).get('mode','ollama'))

    def create(self, payload):
        name, role = actor(payload); permitted(role)
        workspace_type=payload.get('workspace_type','new_launch')
        if workspace_type not in WORKSPACE_TYPES: raise ValueError('Choose an existing feature, feature change or new launch')
        w = {'id': uid('launch'), 'title': clean(payload.get('title'), 160), 'brief': clean(payload.get('brief'), 6000),
             'workspace_type':workspace_type,'risk_rules':[],
             'simulated': payload.get('simulated') is True, 'revision': 0, 'updated': now(), 'sources': [], 'facts': [],
             'fact_approval': {}, 'artifacts': {}, 'archive': [], 'partners': [], 'controls': [], 'decision': None,
             'questions': [], 'tasks': []}
        for team, title in [('cs', 'Support briefing completed'), ('marketing', 'Creative assets reviewed'), ('bd', 'Pilot partner readiness confirmed'), ('risk', 'Risk assessment and control evidence reviewed')]:
            if workspace_type!='new_launch':
                title={'cs':'Support guidance reviewed','marketing':'Communication impact reviewed','bd':'Participant impact reviewed','risk':'Transaction rule assessment reviewed'}[team]
            w['tasks'].append({'id': uid('task'), 'team': team, 'title': title, 'owner': '', 'status': 'todo',
                               'critical': True, 'depends_on': [], 'evidence': '', 'due': '', 'reopened_reason': ''})
        with self.connect() as db:
            db.execute('INSERT INTO launches VALUES(?,?,?)', (w['id'], 0, json.dumps(w)))
            self._write(db, w, name, 'create')
        return self.get(w['id'])

    def delete(self,launch_id,payload):
        name,role=actor(payload);permitted(role)
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE');w=self._read(db,launch_id)
            if payload.get('revision')!=w['revision']: raise Conflict('This workspace changed. Refresh before deleting it.')
            if payload.get('confirmation')!=w['title']: raise ValueError('Enter the workspace name exactly to confirm deletion')
            for table in ('jobs','events'): db.execute(f'DELETE FROM {table} WHERE launch_id=?',(launch_id,))
            db.execute('DELETE FROM launches WHERE id=?',(launch_id,))
        return {'deleted':launch_id}

    def mutate(self, launch_id, payload):
        name, role = actor(payload)
        action = payload.get('action')
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            w = self._read(db, launch_id)
            if type(payload.get('revision')) is not int or payload['revision'] != w['revision']:
                raise Conflict('This launch changed. Refresh before saving; your edits were not applied.')
            detail = {}
            if action == 'brief_save':
                permitted(role)
                w['title']=clean(payload.get('title'),160); w['brief']=clean(payload.get('brief'),6000)
                if 'workspace_type' in payload:
                    if payload['workspace_type'] not in WORKSPACE_TYPES: raise ValueError('Choose a valid workspace type')
                    w['workspace_type']=payload['workspace_type']
                w['fact_approval']={}
                detail['affected_teams']=invalidate(w,TEAMS,'Feature brief changed')
            elif action == 'source_add':
                scope = payload.get('scope', 'shared')
                if scope not in ('shared', *TEAMS):
                    raise ValueError('Invalid source scope')
                permitted(role, scope if scope != 'shared' else None)
                source = {'id': uid('source'), 'title': clean(payload.get('title'), 200), 'text': clean(payload.get('text'), 24000),
                          'scope': scope, 'kind': payload.get('kind', 'internal'), 'created': now()}
                if source['kind'] not in ('public', 'internal', 'simulated'):
                    raise ValueError('Invalid source type')
                source['hash'] = digest(source['text']); w['sources'].append(source)
                if payload.get('provenance'):
                    source['provenance'] = {k:clean(str(payload['provenance'].get(k,'')),2000,False) for k in ('document_id','chunk_id','page','source_url','issue_date')}
                detail['affected_teams'] = invalidate(w, TEAMS if scope == 'shared' else [scope], 'New evidence added; assess applicability')
                if scope == 'shared': w['fact_approval'] = {}
            elif action=='source_remove':
                source=find(w['sources'],payload.get('id'));permitted(role,source['scope'] if source['scope']!='shared' else None)
                removed=[f['id'] for f in w['facts'] if f['source_id']==source['id']]
                w['facts']=[f for f in w['facts'] if f['id'] not in removed];w['sources'].remove(source)
                affected=set(TEAMS if source['scope']=='shared' else [source['scope']])
                for rule in w['risk_rules']:
                    if rule.get('source_id')==source['id']:rule.update(source_id='',quote='',status='proposed');affected.add('risk')
                if removed or source['scope']=='shared':w['fact_approval']={}
                detail={'removed_facts':removed,'affected_teams':invalidate(w,affected,'Source evidence removed')}
            elif action in ('risk_rule_save','risk_rule_remove'):
                permitted(role,'risk');key=payload.get('id');old=find(w['risk_rules'],key) if key else None
                if action=='risk_rule_remove':
                    if not old:raise ValueError('Select a transaction rule to remove')
                    w['risk_rules'].remove(old)
                else:
                    if len(w['risk_rules'])>=20 and not old:raise ValueError('Keep a workspace focused on at most 20 relevant transaction rules')
                    status=payload.get('status','proposed');response=payload.get('response','monitor')
                    if status not in ('proposed','documented','active','retired'):raise ValueError('Choose a valid rule status')
                    if response not in ('monitor','decline','step_up','review','rate_limit'):raise ValueError('Choose a valid rule action')
                    item={'id':key or uid('rule'),'name':clean(payload.get('name'),160),'feature_scope':clean(payload.get('feature_scope'),1000),
                          'condition':clean(payload.get('condition'),2000),'response':response,'status':status,'owner':clean(payload.get('owner'),160),
                          'source_id':clean(payload.get('source_id',''),100,False),'quote':clean(payload.get('quote',''),2000,False),
                          'verification':clean(payload.get('verification',''),2000,False)}
                    if status!='proposed' or item['source_id'] or item['quote']:
                        source_refs(w,[item],'risk');source=find(w['sources'],item['source_id'])
                        if status=='active' and source['kind']=='public':raise ValueError('An active transaction rule needs internal rule evidence; a public circular does not establish a live configuration')
                    if status=='active' and not item['verification']:raise ValueError('Add configuration or deployment evidence for the reported active status')
                    if old:w['risk_rules'][w['risk_rules'].index(old)]=item
                    else:w['risk_rules'].append(item)
                detail={'rule_id':key or item['id'],'affected_teams':invalidate(w,['risk'],'Transaction rule changed')}
            elif action in ('fact_save', 'fact_remove'):
                permitted(role)
                key = payload.get('id')
                old = find(w['facts'], key) if key else None
                if action == 'fact_remove':
                    if not old: raise ValueError('Select a fact')
                    w['facts'].remove(old)
                else:
                    new = fact_valid(w, payload, key)
                    if old == new: return self.get(launch_id)
                    if old: w['facts'][w['facts'].index(old)] = new
                    else: w['facts'].append(new)
                    key = new['id']
                w['fact_approval'] = {}
                # Added facts may add obligations for any team; edited facts have explicit dependencies.
                teams = list(TEAMS) if not old else [t for t,a in w['artifacts'].items() if key in a['fact_hashes']]
                detail = {'fact_id': key, 'before': old, 'after': None if action == 'fact_remove' else new,
                          'affected_teams': invalidate(w, teams, 'Feature fact changed: ' + (old or new)['label'])}
            elif action == 'facts_approve':
                permitted(role)
                if not w['facts']: raise ValueError('Add and review at least one cited feature fact')
                for f in w['facts']: fact_valid(w, f, f['id'])
                if w['questions']: raise ValueError('Disposition extracted open questions before approving facts')
                w['fact_approval'] = {'hash': digest(w['facts']), 'actor': name, 'time': now(), 'note': clean(payload.get('note'), 2000)}
            elif action == 'questions_resolve':
                permitted(role); detail = {'questions': w['questions'], 'disposition': clean(payload.get('note'), 4000)}; w['questions'] = []
            elif action in ('partner_save', 'control_save'):
                team = 'bd' if action == 'partner_save' else 'risk'; permitted(role, team)
                collection = w['partners'] if team == 'bd' else w['controls']
                key = payload.get('id'); old = find(collection, key) if key else None
                if team == 'bd':
                    stage = payload.get('stage')
                    if stage not in ('candidate', 'interested', 'testing', 'ready', 'live'): raise ValueError('Invalid partner stage')
                    item = {'id': key or uid('partner'), 'name': clean(payload.get('name'), 160), 'capabilities': clean(payload.get('capabilities'), 2000),
                            'stage': stage, 'evidence': clean(payload.get('evidence', ''), 2000, False)}
                    if stage in ('ready','live') and not item['evidence']: raise ValueError('Ready/live status requires recorded evidence')
                else:
                    status = payload.get('status')
                    if status not in ('proposed', 'documented', 'implemented', 'tested'): raise ValueError('Invalid control status')
                    item = {'id': key or uid('control'), 'name': clean(payload.get('name'), 160), 'scope': clean(payload.get('scope'), 2000),
                            'status': status, 'owner': clean(payload.get('owner'), 160), 'evidence': clean(payload.get('evidence', ''), 2000, False)}
                    if status in ('implemented','tested') and not item['evidence']: raise ValueError('Implementation/testing status requires evidence')
                if old: collection[collection.index(old)] = item
                else: collection.append(item)
                detail = {'id': item['id'], 'affected_teams': invalidate(w, [team], 'Partner or control evidence changed')}
            elif action == 'artifact_save':
                team = payload.get('team'); permitted(role, team)
                if team not in TEAMS: raise ValueError('Invalid team')
                artifact = w['artifacts'].get(team)
                if not artifact: raise ValueError('Generate a deliverable first')
                if artifact['status'] == 'stale': raise ValueError('Regenerate this stale deliverable before editing its revision')
                packed = validate_pack(w, team, payload)
                detail['note']=clean(payload.get('note'),2000)
                w['archive'].append(copy.deepcopy(artifact))
                artifact.update(packed, status='draft', version=artifact['version']+1, edited_by=name, edited_at=now())
                artifact['review']=None
                # Human edits and later revisions also depend on all facts offered for review.
                artifact['fact_hashes'] = {f['id']: fact_signature(f) for f in w['facts']}
                invalidate(w, [team], 'Deliverable edited; completion evidence must be rechecked')
                artifact['status'] = 'draft'; artifact['stale_reason'] = ''
            elif action == 'artifact_review':
                team = payload.get('team'); permitted(role, team)
                a = w['artifacts'].get(team)
                if not a or a['status'] == 'stale': raise ValueError('Generate a current deliverable first')
                note = clean(payload.get('note'), 2000)
                decision = payload.get('decision')
                if decision not in ('approved', 'changes_requested'): raise ValueError('Invalid review decision')
                if decision == 'approved':
                    if not approved_facts(w): raise ValueError('Approve current feature facts first')
                    if any(i['team'] == team for i in issues(w)): raise ValueError('Resolve flagged claims and open questions before approval')
                else: invalidate(w, [team], 'Team reviewer requested changes')
                a.update(status=decision, review={'actor': name, 'note': note, 'time': now(), 'version': a['version']})
            elif action == 'task_save':
                key = payload.get('id'); task = find(w['tasks'], key) if key else None
                team = task['team'] if task else payload.get('team'); permitted(role, team)
                if team not in TEAMS: raise ValueError('Invalid task team')
                status = payload.get('status', 'todo')
                if status not in ('todo', 'in_progress', 'blocked', 'done'): raise ValueError('Invalid task status')
                deps = payload.get('depends_on', task['depends_on'] if task else [])
                if not isinstance(deps, list) or any(not isinstance(d,str) for d in deps): raise ValueError('Invalid dependencies')
                deps = list(dict.fromkeys(deps))
                for dep in deps:
                    find(w['tasks'], dep)
                    if dep == key: raise ValueError('A task cannot depend on itself')
                item = {'id': key or uid('task'), 'team': team, 'title': clean(payload.get('title', task['title'] if task else ''), 200),
                        'owner': clean(payload.get('owner', ''), 160, False), 'status': status,
                        'critical': task['critical'] if task else payload.get('critical', True) is True,
                        'depends_on': deps, 'evidence': clean(payload.get('evidence', ''), 3000, False),
                        'due': clean(payload.get('due', ''), 10, False), 'reopened_reason': ''}
                if item['due']:
                    datetime.strptime(item['due'], '%Y-%m-%d')
                if status == 'done':
                    if not item['owner'] or not item['evidence']: raise ValueError('Completion needs an owner and evidence')
                    if not approved_facts(w) or w['artifacts'].get(team, {}).get('status') != 'approved': raise ValueError('Current feature and team deliverable approvals are required')
                    if any(find(w['tasks'], dep)['status'] != 'done' for dep in deps): raise ValueError('Complete prerequisite tasks first')
                if task: w['tasks'][w['tasks'].index(task)] = item
                else: w['tasks'].append(item)
                self._acyclic(w['tasks'])
                # Reopening a prerequisite reopens downstream completions transitively.
                reopened = {item['id']} if status != 'done' else set()
                while True:
                    more = {t['id'] for t in w['tasks'] if any(d in reopened for d in t['depends_on'])} - reopened
                    if not more: break
                    reopened |= more
                for t in w['tasks']:
                    if t['id'] in reopened and t['status'] == 'done': t.update(status='todo', reopened_reason='Prerequisite reopened')
                if w.get('decision'): w['decision']['status'] = 'requires_review'
            elif action == 'launch_decide':
                permitted(role)
                if not readiness(w)['ready']: raise ValueError('Resolve all readiness blockers before recording a launch decision')
                w['decision'] = {'status': 'recorded', 'actor': name, 'time': now(), 'note': clean(payload.get('note'), 3000), 'revision': w['revision']+1}
            else:
                raise ValueError('Unknown action')
            self._write(db, w, name, action, detail)
        return self.get(launch_id)

    @staticmethod
    def _acyclic(tasks):
        graph = {t['id']: t['depends_on'] for t in tasks}; visiting = set(); done = set()
        def walk(node):
            if node in visiting: raise ValueError('Task dependencies contain a cycle')
            if node in done: return
            visiting.add(node)
            for dep in graph[node]: walk(dep)
            visiting.remove(node); done.add(node)
        for node in graph: walk(node)

    def enqueue(self, launch_id, payload):
        name, role = actor(payload); kind = payload.get('kind'); team = payload.get('team')
        if kind not in ('extract', 'generate'): raise ValueError('Unknown job type')
        permitted(role, team if kind == 'generate' else None)
        if kind == 'generate' and team not in TEAMS: raise ValueError('Invalid team')
        mode = payload.get('mode', 'ollama')
        if mode not in ('ollama', 'template'): raise ValueError('Invalid generation mode')
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE'); w = self._read(db, launch_id)
            if payload.get('revision') != w['revision']: raise Conflict('Launch changed; refresh before generating')
            if kind == 'generate' and not approved_facts(w): raise ValueError('Approve current feature facts before generation')
            if kind == 'extract' and not any(s['scope']=='shared' for s in w['sources']): raise ValueError('Add shared source text first')
            if kind == 'extract' and mode == 'template': raise ValueError('Fact extraction requires the local model; facts can also be entered manually')
            if db.execute("SELECT 1 FROM jobs WHERE launch_id=? AND kind=? AND coalesce(team,'')=? AND state IN ('queued','running')", (launch_id, kind, team or '')).fetchone():
                raise Conflict('This workflow is already queued or running')
            if db.execute("SELECT count(*) FROM jobs WHERE state IN ('queued','running')").fetchone()[0]>=32:
                raise Conflict('The local queue is full. Let existing workflows finish before adding more.')
            snapshot = team_input(w, team) if kind == 'generate' else {'title':w['title'], 'brief':w['brief'], 'workspace_type':w['workspace_type'], 'sources':[s for s in w['sources'] if s['scope']=='shared'], 'facts':w['facts']}
            key = uid('job'); request = {'actor':name, 'mode':mode, 'snapshot':snapshot, 'artifact_hash':digest(w['artifacts'].get(team,{}))}
            db.execute('INSERT INTO jobs(id,launch_id,kind,team,state,created,updated,input_hash,request) VALUES(?,?,?,?,?,?,?,?,?)',
                       (key, launch_id, kind, team, 'queued', now(), now(), digest(snapshot), json.dumps(request)))
        return key

    def recover_jobs(self):
        with self.connect() as db:
            db.execute("UPDATE jobs SET state='interrupted',error='Server restarted during generation. Retry explicitly; previous reviews remain intact.',updated=? WHERE state='running'", (now(),))

    def enqueue_all(self,launch_id,payload):
        name,role=actor(payload);permitted(role)
        mode=payload.get('mode','ollama')
        if mode not in ('ollama','template'):raise ValueError('Choose AI drafting or example templates')
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE');w=self._read(db,launch_id)
            if payload.get('revision')!=w['revision']:raise Conflict('The workspace changed. Refresh before preparing team work.')
            if not approved_facts(w):raise ValueError('Review and approve the feature brief first')
            if db.execute("SELECT 1 FROM jobs WHERE launch_id=? AND state IN ('queued','running')",(launch_id,)).fetchone():raise Conflict('Team work is already being prepared. Check Activity for progress.')
            if db.execute("SELECT count(*) FROM jobs WHERE state IN ('queued','running')").fetchone()[0]>28:raise Conflict('The queue is full. Wait for the current drafts to finish.')
            ids=[]
            for team in TEAMS:
                snapshot=team_input(w,team);key=uid('job');ids.append(key)
                request={'actor':name,'mode':mode,'snapshot':snapshot,'artifact_hash':digest(w['artifacts'].get(team,{}))}
                db.execute('INSERT INTO jobs(id,launch_id,kind,team,state,created,updated,input_hash,request) VALUES(?,?,?,?,?,?,?,?,?)',
                           (key,launch_id,'generate',team,'queued',now(),now(),digest(snapshot),json.dumps(request)))
        return ids

    def take_job(self):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            row = db.execute("SELECT * FROM jobs WHERE state='queued' ORDER BY rowid LIMIT 1").fetchone()
            if not row: return None
            db.execute("UPDATE jobs SET state='running',updated=? WHERE id=?", (now(), row['id']))
            return dict(row, request=json.loads(row['request']))

    def finish_job(self, job, result=None, error=None):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE');team = job['team']; req = job['request']
            current=db.execute('SELECT state FROM jobs WHERE id=?',(job['id'],)).fetchone()
            if not current or current['state']!='running': return
            w = self._read(db, job['launch_id'])
            if error:
                db.execute("UPDATE jobs SET state='failed',error=?,updated=? WHERE id=?", (str(error)[:1000], now(), job['id'])); return
            snapshot = team_input(w, team) if job['kind']=='generate' else {'title':w['title'], 'brief':w['brief'], 'workspace_type':w['workspace_type'], 'sources':[s for s in w['sources'] if s['scope']=='shared'], 'facts':w['facts']}
            existing = w['artifacts'].get(team, {})
            if digest(snapshot) != job['input_hash'] or (job['kind']=='generate' and (digest(existing)!=req['artifact_hash'] or not approved_facts(w))):
                db.execute("UPDATE jobs SET state='superseded',error='Inputs or deliverable changed while generating; output was not applied.',updated=? WHERE id=?", (now(),job['id'])); return
            if job['kind'] == 'extract':
                if not isinstance(result,dict) or not isinstance(result.get('facts'),list) or not 1<=len(result['facts'])<=20: raise ValueError('Invalid extracted facts')
                pending = [fact_valid(w,f) for f in result['facts']]
                # Extraction is additive and de-duplicates quotations; existing reviewed facts are never replaced.
                signatures = {(f['source_id'],normal(f['quote']),normal(f['label'])) for f in w['facts']}
                for f in pending:
                    sig = (f['source_id'],normal(f['quote']),normal(f['label']))
                    if sig not in signatures: w['facts'].append(f); signatures.add(sig)
                questions = result.get('open_questions', [])
                if not isinstance(questions,list) or len(questions)>15: raise ValueError('Invalid questions')
                w['questions'] = [clean(q,1000) for q in questions]
                w['fact_approval'] = {}; invalidate(w, TEAMS, 'New extracted facts need product review')
            else:
                pack = validate_pack(w,team,result)
                if existing: w['archive'].append(copy.deepcopy(existing))
                invalidate(w,[team],'A new deliverable revision needs review')
                # Include all supplied facts, not only model-selected references, to cover omitted dependencies.
                pack.update(team=team,version=existing.get('version',0)+1,status='draft',created=now(),generator=req['mode'],
                            fact_hashes={f['id']:fact_signature(f) for f in w['facts']},input_hash=job['input_hash'],review=None)
                w['artifacts'][team] = pack
            self._write(db,w,req['actor'],job['kind']+'_completed',{'team':team,'job_id':job['id'],'mode':req['mode']})
            db.execute("UPDATE jobs SET state='completed',result=?,updated=? WHERE id=?",(json.dumps(result),now(),job['id']))

    def export(self, launch_id):
        w=self.get(launch_id)
        lines=[f'# {w["title"]}', '', '**SIMULATED CAPSTONE**' if w['simulated'] else '**Internal draft — review required**',
               f'Revision {w["revision"]}. Exported {now()}.', '', '## Feature facts']
        for f in w['facts']:
            s=find(w['sources'],f['source_id']); lines.extend([f'### {f["label"]} ({f["id"]})',f['value'],f'Source: {s["title"]} ({s["id"]})',f'> {f["quote"]}',''])
        for team,label in TEAMS.items():
            a=w['artifacts'].get(team); lines.extend(['## '+label])
            if not a: lines.append('Not generated'); continue
            lines.append(f'Status: {a["status"]}; revision {a["version"]}; generator {a["generator"]}')
            for item in a['items']:
                lines.extend(['### '+item['title'],item['body'],f'Type: {item["kind"]}. Facts: {", ".join(item["fact_ids"])}',''])
                for ref in item['source_refs']: lines.extend([f'Source: {find(w["sources"],ref["source_id"])["title"]}', '> '+ref['quote']])
            for q in a['open_questions']: lines.append('Open question: '+q)
            for assessment in a.get('rule_assessments',[]):
                rule=next((r for r in w.get('risk_rules',[]) if r['id']==assessment['rule_id']),{'name':'Removed rule '+assessment['rule_id']})
                lines.extend(['### Transaction rule: '+rule['name'],f'Applicability: {assessment["applicability"]}; recommendation: {assessment["recommendation"]}',assessment['rationale'],assessment['proposed_change']])
        lines.extend(['## Readiness']+[f'- {b}' for b in w['readiness']['blockers']])
        if not w['readiness']['blockers']: lines.append('All configured gates satisfied. A human launch decision is recorded separately.')
        lines.extend(['## Tasks']+[f'- {t["title"]}: {t["status"]}; owner: {t["owner"] or "unassigned"}; evidence: {t["evidence"]}' for t in w['tasks']])
        lines.extend(['## Partner register',json.dumps(w['partners'],ensure_ascii=False,indent=2),'## Control register',json.dumps(w['controls'],ensure_ascii=False,indent=2)])
        lines.extend(['## Transaction rule register',json.dumps(w.get('risk_rules',[]),ensure_ascii=False,indent=2)])
        lines.extend(['## Source snapshots']+[f'- {s["title"]}; {s["id"]}; scope: {s["scope"]}; kind: {s["kind"]}; SHA-256: {s["hash"]}; provenance: {json.dumps(s.get("provenance",{}),ensure_ascii=False)}' for s in w['sources']])
        lines.extend(['## Decision', json.dumps(w['decision'],ensure_ascii=False), '', 'Role selection is a local demonstration, not authenticated enterprise access. No external communications or production rules are executed.'])
        return '\n\n'.join(lines)
