import io
import json
import unittest
from unittest.mock import Mock, patch
from evaluation.benchmark_models import freeze, get_local, run_one


class BenchmarkTests(unittest.TestCase):
    def test_rejects_remote(self):
        with self.assertRaises(ValueError):
            get_local('https://example.org', '/api/tags')

    def test_freeze_captures_first_generation_and_restores(self):
        engine = Mock()
        original = engine.ollama
        engine.answer.side_effect = lambda _: engine.ollama('/api/generate', {'prompt':'frozen'})
        self.assertEqual(freeze(engine, 'question'), {'prompt':'frozen'})
        self.assertIs(engine.ollama, original)
        original.assert_not_called()

    def run_stream(self, parsed, final=True):
        rows = [{'response':json.dumps(parsed)}]
        if final:
            rows.append({'done':True, 'eval_count':10, 'eval_duration':1000000000, 'done_reason':'stop'})
        stream = io.BytesIO(('\n'.join(json.dumps(r) for r in rows)+'\n').encode())
        opener = Mock(); opener.open.return_value = stream
        with patch('urllib.request.build_opener', return_value=opener):
            return run_one('http://localhost:11434', {'prompt':json.dumps({'evidence':[{'citation':'S1'}]})}, 5)

    def test_records_latency_and_checks_citation_ids(self):
        row = self.run_stream({'abstain':False, 'claims':[{'text':'Claim', 'sources':['S1']}]})
        self.assertTrue(row['structure_and_citation_ids_valid'])
        self.assertEqual(row['output_tokens_per_second'], 10)
        self.assertIsNotNone(row['time_to_first_output_seconds'])

    def test_invalid_citations_are_not_reported_valid(self):
        row = self.run_stream({'abstain':False, 'claims':[{'text':'Claim', 'sources':['S9']}]})
        self.assertFalse(row['structure_and_citation_ids_valid'])

    def test_interrupted_stream_is_failure(self):
        with self.assertRaisesRegex(ValueError, 'before completion'):
            self.run_stream({}, final=False)


if __name__ == '__main__':
    unittest.main()
