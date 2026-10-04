import json
import unittest
from unittest.mock import patch
from app import Engine, chunks

class ResearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = Engine(config={"embedding_model":"","generation_model":"","ollama_url":"http://127.0.0.1:11434"})

    def test_corpus_and_provenance(self):
        e = self.engine
        self.assertEqual(len(e.docs),129)
        self.assertEqual(len(e.pages),251)
        self.assertEqual(e.stats()["converted"],107)
        self.assertEqual(len({p["id"] for p in e.parts}),len(e.parts))
        for p in e.parts:
            self.assertIn(p["document_id"],e.by_id)
            source = e.page_lookup[p["document_id"],p["page"]]
            self.assertIn(p["text"]," ".join(source["text"].split()))
            self.assertTrue(p["source_url"].startswith("https://"))

    def test_exact_number_and_series(self):
        found = self.engine.search("What does OC 186A say about Tap Pay?")
        self.assertTrue(found)
        self.assertTrue(all(p["document_id"]=="2026-OC-186A" for p in found))
        rupay = self.engine.search("credit card transaction limit",series="RuPay")
        self.assertTrue(rupay)
        self.assertTrue(all(p["series"]=="RuPay" for p in rupay))

    def test_missing_document_does_not_return_neighboring_rules(self):
        for query in ["OC 237", "OC 999", "OC 76B"]:
            self.assertEqual(self.engine.search(query),[])

    def test_date_filter_excludes_later_revision_and_later_issue(self):
        self.assertEqual(self.engine.search("OC 165",cutoff="2024-12-31"),[])
        self.assertTrue(self.engine.search("OC 165",cutoff="2026-03-01"))
        self.assertEqual(self.engine.search("OC 201A",cutoff="2024-12-31"),[])
        with self.assertRaises(ValueError):
            self.engine.search("Tap Pay",cutoff="bad-date")

    def test_reference_relationships_and_missing_parent(self):
        chain = self.engine.relationships("2026-OC-208C")
        ids = {d["id"] for d in chain["documents"]}
        self.assertIn("2024-OC-208",ids)
        self.assertIn("2025-OC-208A",ids)
        self.assertIn("2026-OC-208C",ids)
        chain = self.engine.relationships("2025-OC-76C")
        self.assertTrue(any(x["reference"]=="76B" and not x["available"] for x in chain["links"]))

    def test_disabled_models_fail_explicitly(self):
        with self.assertRaisesRegex(ValueError,"not built"):
            self.engine.search("Tap Pay",method="vector")
        with self.assertRaisesRegex(ValueError,"No generation"):
            self.engine.answer({"query":"OC 186A","mode":"generate"})

    def test_evidence_mode_does_not_call_model(self):
        with patch.object(self.engine,"ollama",side_effect=AssertionError("Must not call a model")):
            result = self.engine.answer({"query":"OC 186A"})
            self.assertEqual(result["claims"],[])
            self.assertFalse(result["abstained"])

    def test_unanswerable_no_keyword_overlap(self):
        result = self.engine.answer({"query":"quantum photosynthesis chlorophyll"})
        self.assertTrue(result["abstained"])
        self.assertEqual(result["sources"],[])

    def test_generation_rejects_fabricated_citation(self):
        with patch.dict(self.engine.config,{"generation_model":"test-model"}):
            with patch.object(self.engine,"ollama",return_value={"response":json.dumps({"abstain":False,"claims":[{"text":"Unsupported","sources":["S999"]}]})}):
                with self.assertRaisesRegex(ValueError,"invalid citations"):
                    self.engine.answer({"query":"OC 186A","mode":"generate"})

    def test_generation_accepts_citation_structure_and_abstention(self):
        with patch.dict(self.engine.config,{"generation_model":"test-model"}):
            with patch.object(self.engine,"ollama",return_value={"response":json.dumps({"abstain":False,"claims":[{"text":"A test claim","sources":["S1"]}]})}):
                result = self.engine.answer({"query":"OC 186A","mode":"generate"})
                self.assertEqual(result["claims"][0]["sources"],["S1"])
            with patch.object(self.engine,"ollama",return_value={"response":json.dumps({"abstain":True,"claims":[]})}):
                self.assertTrue(self.engine.answer({"query":"OC 186A","mode":"generate"})["abstained"])
            with patch.object(self.engine,"ollama",side_effect=AssertionError("No evidence must not call model")):
                self.assertTrue(self.engine.answer({"query":"OC 999","mode":"generate"})["abstained"])

    def test_vector_and_hybrid_respect_filter(self):
        vectors = [[1,0] for _ in self.engine.parts]
        with patch.object(self.engine,"vectors",vectors):
            with patch.object(self.engine,"ollama",return_value={"embeddings":[[1,0]]}):
                for mode in ["vector","hybrid"]:
                    results = self.engine.search("OC 186A",method=mode)
                    self.assertTrue(results)
                    self.assertTrue(all(p["document_id"]=="2026-OC-186A" for p in results))

    def test_chunking_large_block_keeps_order_and_boundaries(self):
        text = " ".join("word"+str(i) for i in range(700))
        output = list(chunks(text))
        self.assertTrue(len(output)>1)
        self.assertTrue(all(len(x.split())<=220 for x in output))
        self.assertTrue(all(x in text for x in output))
        self.assertTrue(output[-1].endswith("word699"))

    def test_qwen_query_instruction_and_empty_filter(self):
        with patch.dict(self.engine.config,{"query_instruction":"Find relevant circular passages"}):
            with patch.object(self.engine,"vectors",[[1,0] for _ in self.engine.parts]):
                with patch.object(self.engine,"ollama",return_value={"embeddings":[[1,0]]}) as provider:
                    self.engine.search("OC 186A",method="hybrid")
                    self.assertEqual(provider.call_args.args[1]["input"],"Instruct: Find relevant circular passages\nQuery: OC 186A")
                    provider.reset_mock()
                    self.assertEqual(self.engine.search("OC 999",method="hybrid"),[])
                    provider.assert_not_called()

    def test_generation_limits_and_truncation(self):
        with patch.dict(self.engine.config,{"generation_model":"test","context_length":8192,"max_output_tokens":1500}):
            with patch.object(self.engine,"ollama",return_value={"done_reason":"length","response":"{}"}) as provider:
                with self.assertRaisesRegex(ValueError,"output limit"):
                    self.engine.answer({"query":"OC 186A","mode":"generate"})
                payload=provider.call_args.args[1]
                self.assertFalse(payload["think"])
                self.assertEqual(payload["options"]["num_ctx"],8192)
                self.assertEqual(payload["options"]["num_predict"],1500)

if __name__ == "__main__":
    unittest.main()
