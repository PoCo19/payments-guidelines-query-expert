import copy
import json
import math
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from app import Engine, ROOT, read_json
from ingestion import clause_chunks
from registry import Registry
from vector_store import ChromaStore


class IngestionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine=Engine(config={"chunker_version":"clauses-v1","embedding_model":"","generation_model":""})

    def test_every_source_word_retained_and_spans_exact(self):
        e=self.engine
        for page in e.pages:
            words=page["text"].split()
            covered=set()
            parts=[p for p in e.parts_by_doc[page["document_id"]] if p["page"]==page["source_page"]]
            for p in parts:
                self.assertEqual(p["text"]," ".join(words[p["start_word"]:p["end_word"]]))
                self.assertLessEqual(len(p["text"].split()),220)
                covered.update(range(p["start_word"],p["end_word"]))
            self.assertEqual(covered,set(range(len(words))),page["document_id"])

    def test_stable_ids_and_no_cross_document_links(self):
        again=Engine(config=self.engine.config)
        self.assertEqual(self.engine.fingerprint,again.fingerprint)
        for p in again.parts:
            for key in ("previous_chunk_id","next_chunk_id"):
                if p[key]:
                    self.assertEqual(again.parts_by_id[p[key]]["document_id"],p["document_id"])

    def test_headings_clauses_and_cross_page_continuation(self):
        pages=[dict(document_id="d",source_page=1,text="Key Guidelines\n1. Consent is required.\n2. Continuation starts here"),
               dict(document_id="d",source_page=2,text="and ends on this page.\nRemitter Bank\n1. Check enablement.")]
        parts=clause_chunks(pages)
        self.assertIn("Key Guidelines 1.",parts[0]["text"])
        self.assertEqual(parts[0]["clause_label"],"1.")
        self.assertEqual(parts[1]["next_chunk_id"],parts[2]["id"])
        self.assertEqual(parts[1]["section_id"],parts[2]["section_id"])
        self.assertNotEqual(parts[2]["section_id"],parts[3]["section_id"])
        self.assertEqual(parts[3]["section_heading"],"Remitter Bank")

    def test_long_clause_overlap(self):
        p=clause_chunks([dict(document_id="d",source_page=1,text="1. "+" ".join(str(i) for i in range(600)))])
        self.assertEqual(p[0]["text"].split()[-35:],p[1]["text"].split()[:35])
        self.assertTrue(all(x["clause_label"]=="1." for x in p))

    def test_features_allow_multiple_labels(self):
        self.assertTrue(any({"autopay","netc_ncmc"}.issubset(set(v)) for v in self.engine.registry.features.values()))


class ContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e=Engine(config={"chunker_version":"clauses-v1","generation_model":"test"})

    def ask(self,query="OC 186A UPI Tap Pay consent",**kwargs):
        return self.e.answer(dict(query=query,method="bm25",scope="related",mode="evidence",**kwargs))

    def test_strict_circular_stays_strict(self):
        r=self.e.answer(dict(query="OC 186A consent",scope="strict"))
        self.assertTrue(all(p["document_id"]=="2026-OC-186A" for p in r["sources"]))
        self.assertTrue(all(p["retrieval_reason"]=="direct_match" for p in r["sources"]))

    def test_related_reference_is_included_with_attribution(self):
        r=self.ask()
        parent=[p for p in r["sources"] if p["document_id"]=="2023-UPI-186"]
        self.assertTrue(parent)
        self.assertEqual(parent[0]["retrieval_reason"],"recorded_reference")
        self.assertEqual(parent[0]["relation"]["relation"],"references")
        self.assertEqual(parent[0]["via_document_id"],"2026-OC-186A")
        self.assertEqual(len({p["id"] for p in r["sources"]}),len(r["sources"]))
        self.assertEqual([p["citation"] for p in r["sources"]],[f'S{i+1}' for i in range(len(r["sources"]))])

    def test_expansion_respects_date_product_and_feature(self):
        r=self.ask("OC 186 Tap Pay",cutoff="2024-01-01",series="UPI",feature="tap_pay")
        self.assertTrue(r["sources"])
        for p in r["sources"]:
            self.assertLessEqual(p["issue_date"],"2024-01-01")
            self.assertEqual(p["series"],"UPI")
            self.assertIn("tap_pay",p["feature_ids"])
        self.assertNotIn("2026-OC-186A",{p["document_id"] for p in r["sources"]})

    def test_missing_seed_never_expands_to_neighbors(self):
        for q in ["OC 999 Tap Pay","OC 76B","OC 237","OC 186AA consent","OC 1860 consent"]:
            self.assertEqual(self.ask(q)["sources"],[])

    def test_missing_reference_reported_without_invented_text(self):
        r=self.ask("OC 76C")
        self.assertTrue(any("76B" in n for n in r["retrieval_trace"]["notes"]))
        self.assertFalse(any(p["circular_number"]=="76B" for p in r["sources"]))

    def test_budget_and_invalid_controls(self):
        with patch.dict(self.e.config,{"context_char_budget":2000}):
            r=self.ask()
            self.assertLessEqual(r["retrieval_trace"]["evidence_characters"],2000)
            self.assertLessEqual(len(r["sources"]),10)
        with self.assertRaises(ValueError): self.ask(feature="made_up")
        with self.assertRaises(ValueError): self.e.answer(dict(query="OC 186A",scope="bad"))

    def test_generated_prompt_carries_provenance(self):
        with patch.object(self.e,"ollama",return_value={"response":'{"abstain":true,"claims":[]}'}) as provider:
            self.e.answer(dict(query="OC 186A Tap Pay",mode="generate",scope="related"))
            prompt=json.loads(provider.call_args.args[1]["prompt"])
            self.assertTrue(all("document_id" in p and "page" in p and "retrieval_reason" in p for p in prompt["evidence"]))


class RegistryTests(unittest.TestCase):
    def test_ambiguous_reference_is_not_resolved(self):
        docs=[dict(id="a",series="UPI",circular_number="1A",subject="A",availability="converted",related_circulars=["1"]),
              dict(id="b",series="UPI",circular_number="1",subject="B",availability="converted"),
              dict(id="c",series="UPI",circular_number="1",subject="C",availability="converted")]
        r=Registry(docs,[],[],[])
        self.assertEqual(r.edges[0]["status"],"ambiguous")
        self.assertEqual(r.neighboring_documents("a"),[])

    def test_sqlite_roundtrip_and_references(self):
        e=Engine(config={"chunker_version":"clauses-v1"})
        with tempfile.TemporaryDirectory() as directory:
            r=Registry(e.docs,e.pages,e.parts,e.registry.rules)
            expected=r.neighboring_documents("2026-OC-186A")
            path=r.persist(directory)
            self.assertEqual(expected,r.neighboring_documents("2026-OC-186A"))
            db=sqlite3.connect(path)
            try:
                self.assertEqual(db.execute('SELECT count(*) FROM chunks').fetchone()[0],len(e.parts))
                self.assertEqual(db.execute('PRAGMA integrity_check').fetchone()[0],"ok")
                self.assertEqual(db.execute('PRAGMA foreign_key_check').fetchall(),[])
            finally:db.close()
            self.assertEqual(r.persist(directory),path)


class ChromaTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.parts=[dict(id="a",document_id="doc1",page=1,series="UPI",circular_number="1",text="Consent"),
                    dict(id="b",document_id="doc2",page=2,series="RuPay",circular_number="2",text="Limit")]
        self.s=ChromaStore(self.temp.name,"fp","model",self.parts)

    def test_real_chroma_cosine_filter_and_reopen(self):
        self.s.build([[1.,0.],[0.,1.]],"digest")
        self.assertAlmostEqual(self.s.query([1.,0.],{"doc1"})[0][1],1.,places=5)
        self.assertEqual([x[0] for x in self.s.query([1.,0.],{"doc2"})],["b"])
        reopened=ChromaStore(self.temp.name,"fp","model",self.parts)
        self.assertEqual(reopened.status,"Ready")
        self.assertEqual(reopened.query([0.,1.],{"doc2"})[0][0],"b")
        self.assertEqual(reopened.query([1.,0.],set()),[])

    def test_fingerprint_and_model_isolation(self):
        self.s.build([[1.,0.],[0.,1.]],"digest")
        self.assertIsNone(ChromaStore(self.temp.name,"changed","model",self.parts).collection)
        self.assertIsNone(ChromaStore(self.temp.name,"fp","changed",self.parts).collection)

    def test_bad_vectors_and_dimension_rejected(self):
        for vectors in ([[1,0]],[[1,0],[1]],[[0,0],[1,0]],[[math.nan,0],[1,0]]):
            with self.assertRaises(ValueError):self.s.build(vectors,"digest")
        self.s.build([[1.,0.],[0.,1.]],"digest")
        with self.assertRaises(ValueError):self.s.query([1,0,0],{"doc1"})

    def test_failed_build_preserves_published_snapshot(self):
        self.s.build([[1.,0.],[0.,1.]],"digest")
        before=self.s.manifest.read_bytes()
        with patch.object(self.s.client,"create_collection",side_effect=RuntimeError("simulated disk failure")):
            with self.assertRaises(RuntimeError):self.s.build([[0.,1.],[1.,0.]],"digest")
        self.assertEqual(before,self.s.manifest.read_bytes())
        self.assertEqual(ChromaStore(self.temp.name,"fp","model",self.parts).query([1,0],{"doc1"})[0][0],"a")

    def test_missing_record_rejects_incomplete_index(self):
        self.s.build([[1.,0.],[0.,1.]],"digest")
        self.s.collection.delete(ids=["a"])
        self.assertIsNone(ChromaStore(self.temp.name,"fp","model",self.parts).collection)

    def test_failed_upsert_preserves_published_snapshot(self):
        self.s.build([[1.,0.],[0.,1.]],"digest")
        before=self.s.manifest.read_bytes()
        create=self.s.client.create_collection
        def fail_collection(*args,**kwargs):
            collection=create(*args,**kwargs)
            collection.upsert=lambda **kwargs: (_ for _ in ()).throw(RuntimeError("simulated partial build failure"))
            return collection
        with patch.object(self.s.client,"create_collection",side_effect=fail_collection):
            with self.assertRaises(RuntimeError):self.s.build([[0.,1.],[1.,0.]],"digest")
        self.assertEqual(before,self.s.manifest.read_bytes())
        self.assertEqual(ChromaStore(self.temp.name,"fp","model",self.parts).query([1,0],{"doc1"})[0][0],"a")

    def test_corrupt_manifest_reports_rebuild(self):
        self.s.manifest.write_text("broken",encoding="utf-8")
        reopened=ChromaStore(self.temp.name,"fp","model",self.parts)
        self.assertIsNone(reopened.collection)
        self.assertIn("rebuild",reopened.status)


if __name__ == '__main__':unittest.main()
