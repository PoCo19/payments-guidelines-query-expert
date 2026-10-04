"""An auditable SQLite snapshot of documents, chunks, features and references."""
import hashlib
import json
import re
import sqlite3
import uuid
from product_scope import feature_applies
from contextlib import closing
from pathlib import Path


class Registry:
    def __init__(self, docs, pages, parts, rules, reviews=None):
        self.docs, self.parts, self.rules = docs, parts, rules
        self.features = {d["id"]: [r["id"] for r in rules if feature_applies(r,d) and re.search(r["pattern"], d["subject"], re.I)] for d in docs}
        for part in parts:
            self.features[part["document_id"]] = sorted(set(self.features[part["document_id"]] + part.get("feature_ids",[])))
        self.edges = []
        for doc in docs:
            for ref in doc.get("related_circulars", []):
                targets = [d for d in docs if d["series"] == doc["series"] and str(d["circular_number"]).upper() == str(ref).upper()]
                # Ambiguous references remain unresolved; never pick a year arbitrarily.
                target = targets[0] if len(targets) == 1 else None
                matching = [p for p in pages if p["document_id"] == doc["id"] and re.search(r"(?<![A-Za-z0-9])"+re.escape(str(ref))+r"(?![A-Za-z0-9])", p["text"], re.I)]
                self.edges.append(dict(from_id=doc["id"], target_id=target["id"] if target else None,
                    reference=str(ref), relation="references", basis="imported_related_circulars",
                    evidence_pages=[p["source_page"] for p in matching],
                    evidence_status="number_occurrence_only" if matching else "metadata_only",
                    status="resolved" if target and target["availability"] == "converted" else "text_unavailable" if target else "ambiguous" if targets else "missing",
                    candidate_ids=[d["id"] for d in targets]))
        for r in reviews or []:
            if r.get("status")=="accepted" and r["kind"]=="relationship":
                self.edges=[e for e in self.edges if not (e["from_id"]==r["document_id"] and e["target_id"]==r["target_id"])]
                target=next(d for d in docs if d["id"]==r["target_id"])
                self.edges.append(dict(from_id=r["document_id"],target_id=r["target_id"],reference=str(target["circular_number"]),relation=r["relation"],basis=r["reviewer_kind"],evidence_pages=[r["page"]],evidence_status="source_anchor_reviewed",status="resolved" if target["availability"]=="converted" else "text_unavailable",candidate_ids=[r["target_id"]],review_id=r["id"],evidence_quote=r["anchor"]))
        self.fingerprint = hashlib.sha256(json.dumps(dict(docs=docs, parts=parts, rules=rules, edges=self.edges), sort_keys=True).encode()).hexdigest()

    def neighboring_documents(self, doc_id):
        out = []
        edges = self.edges
        if getattr(self,"path",None):
            with closing(sqlite3.connect(self.path)) as db:
                edges = [json.loads(row[0]) for row in db.execute(
                    "SELECT metadata_json FROM relationships WHERE from_id=? OR target_id=? ORDER BY edge_id",(doc_id,doc_id))]
        for edge in edges:
            if edge["status"] != "resolved":
                continue
            if edge["from_id"] == doc_id:
                out.append((edge["target_id"], "referenced_by_seed", edge))
            elif edge["target_id"] == doc_id:
                out.append((edge["from_id"], "references_seed", edge))
        return out

    def persist(self, directory):
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / ("registry-" + self.fingerprint[:24] + ".sqlite3")
        self.path = path
        if path.exists():
            with closing(sqlite3.connect(path)) as db:
                if db.execute("SELECT value FROM metadata WHERE key='fingerprint'").fetchone()[0] != self.fingerprint:
                    raise ValueError("Registry fingerprint mismatch")
            return path
        temp = path.with_suffix("." + uuid.uuid4().hex + ".tmp")
        # A build is transactional; only a completed file receives the snapshot name.
        with closing(sqlite3.connect(temp)) as db, db:
            db.executescript('''
              CREATE TABLE IF NOT EXISTS metadata(key TEXT PRIMARY KEY, value TEXT NOT NULL);
              CREATE TABLE IF NOT EXISTS documents(id TEXT PRIMARY KEY, series TEXT, circular_number TEXT, issue_date TEXT, metadata_json TEXT NOT NULL);
              CREATE TABLE IF NOT EXISTS chunks(id TEXT PRIMARY KEY, document_id TEXT REFERENCES documents(id), page INTEGER, section_id TEXT, metadata_json TEXT NOT NULL);
              CREATE TABLE IF NOT EXISTS features(document_id TEXT REFERENCES documents(id), feature_id TEXT, basis TEXT, evidence TEXT, PRIMARY KEY(document_id,feature_id));
              CREATE TABLE IF NOT EXISTS relationships(edge_id INTEGER PRIMARY KEY, from_id TEXT REFERENCES documents(id), target_id TEXT, relation TEXT, metadata_json TEXT NOT NULL);
            ''')
            db.execute("PRAGMA foreign_keys=ON")
            for table in ("relationships", "features", "chunks", "documents", "metadata"):
                db.execute("DELETE FROM " + table)
            db.execute("INSERT INTO metadata VALUES ('fingerprint',?)", (self.fingerprint,))
            db.executemany("INSERT INTO documents VALUES (?,?,?,?,?)", [(d["id"],d["series"],str(d["circular_number"]),d.get("issue_date"),json.dumps(d)) for d in self.docs])
            db.executemany("INSERT INTO chunks VALUES (?,?,?,?,?)", [(p["id"],p["document_id"],p["page"],p.get("section_id",""),json.dumps(p)) for p in self.parts])
            db.executemany("INSERT INTO features VALUES (?,?,?,?)", [(d["id"],feature,"title_clause_and_review_union",d["subject"]) for d in self.docs for feature in self.features[d["id"]]])
            db.executemany("INSERT INTO relationships VALUES (?,?,?,?,?)", [(i,e["from_id"],e["target_id"],e["relation"],json.dumps(e)) for i,e in enumerate(self.edges)])
        temp.replace(path)
        return path
