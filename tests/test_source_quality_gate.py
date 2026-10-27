import hashlib
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock,patch
from source_quality_gate import gate_sources
from app import Engine


class SourceQualityGateTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.path=Path(self.temp.name)/'flags.json'
        text='Header. Corrupt value. An unrelated safe clause.'
        self.engine=SimpleNamespace(page_lookup={('doc',1):{'text':text}})
        self.path.write_text(json.dumps(dict(schema_version=1,flags=[dict(id='test',document_id='doc',page=1,page_sha256=hashlib.sha256(text.encode()).hexdigest(),unsafe_quote='Corrupt value.',reason='Known extraction error',review_status='AI_check_pending_review')])),encoding='utf8')
        self.bad=dict(citation='S1',document_id='doc',page=1,text='Corrupt value.')
        self.good=dict(citation='S2',document_id='doc',page=1,text='An unrelated safe clause.')

    def test_raw_text_retained_and_only_bad_fragment_excluded(self):
        marked,usable,notes=gate_sources(self.engine,[self.bad,self.good],self.path)
        self.assertEqual(marked[0]['text'],self.bad['text'])
        self.assertFalse(marked[0]['generation_eligible'])
        self.assertEqual(usable,[self.good]);self.assertTrue(notes)
        self.assertNotIn('generation_eligible',self.bad)

    def test_source_change_requires_flag_review(self):
        self.engine.page_lookup['doc',1]['text']='Corrected source text'
        marked,usable,_=gate_sources(self.engine,[self.good],self.path)
        self.assertFalse(usable);self.assertTrue(marked[0]['source_quality_issues'][0]['flag_stale'])

    def test_other_page_and_document_are_not_blocked(self):
        sources=[dict(self.bad,page=2),dict(self.bad,document_id='another')]
        self.assertEqual(gate_sources(self.engine,sources,self.path),(sources,sources,[]))

    def test_exact_repaired_page_is_usable_but_unknown_revision_is_not(self):
        repaired='Header. Correct value. An unrelated safe clause.'
        flags=json.loads(self.path.read_text())
        flags['flags'][0]['repaired_page_sha256']=hashlib.sha256(repaired.encode()).hexdigest()
        self.path.write_text(json.dumps(flags))
        self.engine.page_lookup['doc',1]['text']=repaired
        source=dict(self.bad,text='Correct value.')
        self.assertEqual(gate_sources(self.engine,[source],self.path),([source],[source],[]))
        self.engine.page_lookup['doc',1]['text']=repaired+' Unreviewed change.'
        self.assertFalse(gate_sources(self.engine,[source],self.path)[1])

    def test_companion_hints_cannot_reintroduce_blocked_citation(self):
        sources=[self.bad,dict(self.good,citation_companions=['S1'])]
        marked,usable,_=gate_sources(self.engine,sources,self.path)
        self.assertEqual(usable[0]['citation_companions'],[])
        self.assertEqual(marked[1]['citation_companions'],['S1'])

    def test_fully_blocked_context_abstains_without_model_call(self):
        e=Engine.__new__(Engine);e.config={'generation_model':'fixture'};e.ollama=Mock()
        with patch('app.assemble',return_value=([self.bad],dict(notes=[],route='clause'))),patch('source_quality_gate.gate_sources',return_value=([dict(self.bad,generation_eligible=False)],[],['Known source issue'])):
            r=e.answer(dict(query='What is the limit?',mode='generate'))
        e.ollama.assert_not_called();self.assertTrue(r['abstained'])
        self.assertEqual(r['sources'][0]['text'],'Corrupt value.')

    def test_blocked_text_not_sent_to_generator_or_accepted_as_citation(self):
        e=Engine.__new__(Engine);e.config={'generation_model':'fixture'}
        e.ollama=Mock(return_value={'response':json.dumps(dict(abstain=False,primary_claim_indices=[1],claims=[dict(text='False fact',sources=['S1'])],layout=[]))})
        with patch('app.assemble',return_value=([self.bad,self.good],dict(notes=[],route='clause'))),patch('source_quality_gate.gate_sources',return_value=([dict(self.bad,generation_eligible=False),self.good],[self.good],['Known source issue'])):
            with self.assertRaisesRegex(ValueError,'invalid citations'):e.answer(dict(query='What is the limit?',mode='generate'))
        prompt=json.loads(e.ollama.call_args.args[1]['prompt'])
        self.assertEqual([s['citation'] for s in prompt['evidence']],['S2'])
        self.assertNotIn('Corrupt value.',e.ollama.call_args.args[1]['prompt'])


if __name__=='__main__':unittest.main()
