"""Maintained, source-anchored graph assistance. Links never decide legal precedence."""
from collections import deque
import hashlib
import json
from pathlib import Path
import re


def normal(text):
    return ' '.join(text.split())


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


class EvidenceGraph:
    """Small publisher-neutral graph overlay; immutable corpus and existing chunk IDs."""

    def __init__(self, path, engine):
        raw = Path(path).read_bytes()
        self.fingerprint = hashlib.sha256(raw).hexdigest()
        self.data = json.loads(raw)
        if self.data.get('schema_version') != 1:
            raise ValueError('Unsupported evidence graph schema')
        self.nodes = {n['id']: n for n in self.data['nodes']}
        if len(self.nodes) != len(self.data['nodes']):
            raise ValueError('Duplicate graph anchor')
        self.parts = {}
        for key, n in self.nodes.items():
            page = engine.page_lookup.get((n['document_id'], n['page']))
            doc = engine.by_id.get(n['document_id'])
            if not doc or doc['availability'] != 'converted' or not page:
                raise ValueError('Graph source unavailable: ' + key)
            if digest(page['text']) != n['page_sha256']:
                raise ValueError('Graph source changed; review anchors: ' + key)
            quote = normal(n['quote'])
            if not quote or quote not in normal(page['text']):
                raise ValueError('Invalid graph quote: ' + key)
            matches = [p for p in engine.parts_by_doc[n['document_id']]
                       if p['page'] == n['page'] and quote in normal(p['text'])]
            if not matches:
                raise ValueError('Graph quote no longer fits a source chunk: ' + key)
            self.parts[key] = min(matches, key=lambda p: len(p['text']))
        self.edges = self.data['edges']
        for e in self.edges:
            if e['type'] not in ('references', 'amends_aspect', 'clarifies', 'related_topic'):
                raise ValueError('Unsupported graph relation')
            if e.get('review_status') not in ('proposed_ai_assisted', 'human_reviewed'):
                raise ValueError('Graph relationship needs explicit review status')
            proof = self.nodes.get(e['evidence_anchor'])
            if not proof or proof['document_id'] != e['from_id'] or e['to_id'] not in engine.by_id:
                raise ValueError('Invalid relationship provenance')
            if e['type']=='related_topic' and (e.get('target_anchor') not in self.nodes or self.nodes[e['target_anchor']]['document_id']!=e['to_id']):
                raise ValueError('Topic relationship needs evidence at both endpoints')
        for topic in self.data['topics']:
            if not topic['terms'] or not topic['anchors'] or any(n not in self.nodes for n in topic['anchors']):
                raise ValueError('Invalid graph topic')

    def expand(self, query, seed_documents, requested, allowed):
        """Two hops, at most 12 chunks. Query relevance AND retrieved identity required."""
        seed_documents = set(seed_documents)
        requested = set(requested)
        q = normal(re.sub(r'[^\w]+', ' ', query.lower()))
        from product_scope import ALIASES
        named_products={name for name,pattern in ALIASES.items() if re.search(pattern,query,re.I)}
        relevant_topics=[t for t in self.data['topics'] if not named_products or not t.get('products') or named_products.intersection(t['products'])]
        matching_topics={t['id'] for t in relevant_topics if any(re.search(r'\b'+re.escape(term)+r'\b',q) for term in t['terms'])}
        picked = []; topics = []; reached = set(); used_edges = []; wanted = []; gaps=[]; cautions=[]
        for topic in relevant_topics:
            docs = {self.nodes[n]['document_id'] for n in topic['anchors']}
            matches = any(re.search(r'\b' + re.escape(t) + r'\b', q) for t in topic['terms'])
            starts = docs & (seed_documents | requested)
            if not starts or not (matches or docs & requested):
                continue
            # A shared document can cover many use cases. An explicit topic such as
            # IPO must not activate every other topic containing that document.
            if matching_topics and topic['id'] not in matching_topics:
                continue
            topics.append(topic['id'])
            gaps.extend(topic.get('source_gaps',[]));cautions.extend(topic.get('cautions',[]))
            queue = deque((d, 0) for d in sorted(starts) if allowed(d))
            visited = set()
            while queue:
                doc, depth = queue.popleft()
                if doc in visited:
                    continue
                visited.add(doc)
                if depth == 2:
                    continue
                for e in self.edges:
                    if doc not in (e['from_id'], e['to_id']):
                        continue
                    target = e['to_id'] if doc == e['from_id'] else e['from_id']
                    if target in docs:
                        if e not in used_edges:
                            used_edges.append(e)
                        if allowed(target):
                            queue.append((target, depth + 1))
            reached.update(visited)
            # Retain excluded anchors in the coverage checklist, never as evidence.
            wanted.extend(topic['anchors'])
        terms = set(q.split())
        wanted = list(dict.fromkeys(wanted))
        ordered = sorted(wanted, key=lambda n: (
            self.nodes[n].get('priority', 10),
            -len(terms & set(self.nodes[n]['aspect'].split())), n))
        seen = set()
        for key in ordered:
            n = self.nodes[key]; p = self.parts[key]
            if n['document_id'] not in reached or not allowed(n['document_id']):
                continue
            if p['id'] not in seen and len(picked) < 12:
                scopes=list(dict.fromkeys(self.nodes[k].get('scope','') for k in wanted if self.parts[k]['id']==p['id'] and self.nodes[k].get('scope')))
                picked.append(dict(p, graph_anchor=key,graph_scope=scopes)); seen.add(p['id'])
        return picked, dict(status='active' if topics else 'not_applicable',
            fingerprint=self.fingerprint, topics=topics, max_hops=2, max_graph_chunks=12,
            relationships=used_edges, expected_anchor_ids=wanted,
            source_gaps=list(dict.fromkeys(gaps)),cautions=list(dict.fromkeys(cautions)),
            review_status=self.data['review_status'],
            limitation='Proposed links guide source retrieval only. No automatic supersession or current-applicability decision.')

    def coverage(self, trace, selected):
        hits = []
        for key in trace['expected_anchor_ids']:
            n = self.nodes[key]
            found = any(p['document_id'] == n['document_id'] and p['page'] == n['page']
                        and normal(n['quote']) in normal(p['text']) for p in selected)
            hits.append(dict(anchor_id=key, document_id=n['document_id'], page=n['page'], included=found))
        trace['anchor_coverage'] = hits
        trace['complete_within_pilot'] = bool(hits) and all(h['included'] for h in hits)
        groups={}
        for key in trace['expected_anchor_ids']:
            group=self.nodes[key].get('support_group')
            if group:groups.setdefault(group,set()).add(self.parts[key]['id'])
        for p in selected:
            companions={s['citation'] for members in groups.values() if p['id'] in members for s in selected if s['id'] in members and s['id']!=p['id']}
            if companions:p['citation_companions']=sorted(companions)


def load_graph(engine):
    path = engine.config.get('evidence_graph_path')
    if not path:
        return None, None
    try:
        resolved = Path(path)
        if not resolved.is_absolute():
            resolved = Path(__file__).parent / resolved
        return EvidenceGraph(resolved, engine), None
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return None, 'Graph expansion unavailable: ' + str(exc) + '. Standard retrieval remains available.'


def graph_status(engine):
    graph=getattr(engine,'evidence_graph',None)
    configured=bool(engine.config.get('evidence_graph_path'))
    return dict(status='active' if graph else 'degraded' if configured else 'disabled',
        fingerprint=graph.fingerprint if graph else None,
        anchors=len(graph.nodes) if graph else 0, relationships=len(graph.edges) if graph else 0,
        topics=[t['id'] for t in graph.data['topics']] if graph else [],
        review_status=graph.data.get('review_status') if graph else None,
        warning=getattr(engine,'evidence_graph_error',None),
        corpus_expansion='not_selected_for_release',
        limitation='Graph coverage is bounded. All other eligible documents remain searchable. Links do not establish supersession.')
