import hashlib
import json
import unittest
from unittest.mock import patch
from intake_quality import inspect_pages, reviewed_blockers
from structured_evidence import build_records, SYNTHESIS_GUIDANCE
from contextual_retrieval import lexical_text
import test_document_pipeline as intake
import test_research as research


class QualityTests(unittest.TestCase):
    def test_broken_table_is_blocking_but_money_is_review_only(self):
        pages=inspect_pages('doc',[(1,'| Category | Amount |\n|---|---|\n| Tax | INR 5 lakh | extra |')])
        self.assertEqual(reviewed_blockers(pages,[]),[1])
        codes={f['code']:f['severity'] for f in pages[0]['findings']}
        self.assertEqual(codes['monetary_values'],'review')
        self.assertEqual(codes['table_row_mismatch'],'blocking')

    def test_review_is_bound_to_exact_text_and_requires_identity(self):
        pages=inspect_pages('doc',[(1,'Some damaged \ufffd text')])
        review=dict(page=1,text_sha256=pages[0]['text_sha256'],reviewer='Test reviewer',reason='Compared with PDF')
        self.assertEqual(reviewed_blockers(pages,[review]),[])
        with self.assertRaises(ValueError):reviewed_blockers(pages,[dict(review,text_sha256='wrong')])
        with self.assertRaises(ValueError):reviewed_blockers(pages,[dict(review,reviewer='')])

    def test_valid_table_does_not_block(self):
        p=inspect_pages('doc',[(1,'| Category | Per transaction | Daily |\n|---|---|---|\n| A | INR 5 lakh | INR 10 lakh |')])
        self.assertEqual(reviewed_blockers(p,[]),[])


class IntakeIntegrationTests(unittest.TestCase):
    setUp = intake.IntakeTests.setUp
    cleanup_store = intake.IntakeTests.cleanup_store
    prepare = intake.IntakeTests.prepare
    def test_quality_quarantine_does_not_change_live_config(self):
        self.source.write_text(intake.TEXT+'\n| Category | Amount |\n|---|---|\n| Broken | INR 5 | extra |',encoding='utf-8')
        self.prepare(item=dict(self.item,allow_partial=True))
        d=intake.pipeline.read(intake.pipeline.release_path('test-one')/'index.json')[0]
        self.assertEqual(d['availability'],'needs_source_review')
        self.assertEqual(self.active.read_bytes(),self.before)
        self.assertEqual(d['intake_quality']['blocked_pages'],[1])

    def test_quality_report_tampering_invalidates_candidate(self):
        self.prepare();folder=intake.pipeline.release_path('test-one')
        (folder/'intake_quality.json').write_text('{}')
        with self.assertRaisesRegex(ValueError,'changed'):intake.pipeline.check_candidate(folder)

    def test_companion_pdf_is_saved_and_count_checked(self):
        from pypdf import PdfWriter
        writer=PdfWriter();writer.add_blank_page(width=100,height=100)
        pdf=self.root/'original.pdf'
        with pdf.open('wb') as f:writer.write(f)
        self.source.write_text('<!-- Page 1 -->\n'+intake.TEXT,encoding='utf-8')
        self.prepare(item=dict(self.item,original_pdf='original.pdf'))
        folder=intake.pipeline.release_path('test-one');doc=intake.pipeline.read(folder/'index.json')[0]
        self.assertEqual((folder/doc['local_pdf']).read_bytes(),pdf.read_bytes())
        self.assertTrue(doc['source_coverage']['page_count_verified'])
        self.assertNotEqual(doc['intake_quality']['basis'],'verified')
        intake.pipeline.verify_sources(folder)

    def test_companion_requires_page_alignment(self):
        from pypdf import PdfWriter
        writer=PdfWriter();writer.add_blank_page(width=100,height=100)
        with (self.root/'original.pdf').open('wb') as f:writer.write(f)
        with self.assertRaisesRegex(ValueError,'page markers'):self.prepare(item=dict(self.item,original_pdf='original.pdf'))

    def test_changed_companion_is_not_treated_as_unchanged(self):
        from pypdf import PdfWriter
        pdf=self.root/'original.pdf'
        writer=PdfWriter();writer.add_blank_page(width=100,height=100)
        with pdf.open('wb') as f:writer.write(f)
        self.source.write_text('<!-- Page 1 -->\n'+intake.TEXT,encoding='utf-8')
        item=dict(self.item,original_pdf='original.pdf');self.prepare(item=item)
        config=intake.pipeline.read(self.active);config['data_dir']=str(intake.pipeline.release_path('test-one'));intake.pipeline.write(self.active,config)
        writer=PdfWriter();writer.add_blank_page(width=200,height=100)
        with pdf.open('wb') as f:writer.write(f)
        with self.assertRaisesRegex(ValueError,'Existing id'):self.prepare(name='test-two',item=item)


class EvidenceTests(unittest.TestCase):
    def test_named_source_cannot_borrow_other_cited_amount(self):
        from scope_guard import attribution_scope_issue
        sources=[dict(circular_number='A1',document_id='a',text='The transaction limit is INR 5 lakh.'),dict(circular_number='B2',document_id='b',text='The cumulative limit is INR 10 lakh.')]
        self.assertIsNotNone(attribution_scope_issue('Circular A1 establishes INR 5 lakh per transaction and INR 10 lakh cumulative.',sources))
        self.assertIsNone(attribution_scope_issue('Circular A1 establishes INR 5 lakh per transaction. Circular B2 establishes INR 10 lakh cumulative.',sources))

    def source(self,text,**extra):
        return dict(citation='S1',document_id='doc',page=1,title='Limits',text=text,**extra)

    def test_rows_keep_ownership_and_column_meaning(self):
        text='| Category | Per transaction | Daily |\n|---|---|---|\n| Capital | INR 5 lakh | INR 10 lakh |'
        r=build_records('Capital transaction limit',[self.source(text)])
        row=r['records'][0]
        self.assertEqual(row['citation'],'S1')
        self.assertEqual(row['cells'][1],dict(header='Per transaction',value='INR 5 lakh'))
        self.assertEqual(row['cells'][2],dict(header='Daily',value='INR 10 lakh'))
        self.assertEqual(r['source_hashes']['S1'],hashlib.sha256(text.encode()).hexdigest())

    def test_excluded_sources_and_budget(self):
        self.assertFalse(build_records('q',[self.source('secret',generation_eligible=False)])['records'])
        self.assertFalse(build_records('q',[self.source('long '*2000)],budget=100)['records'])

    def test_original_prose_is_not_interpreted_or_changed(self):
        source=self.source('Participants may use the service unless excluded by section 4.')
        original=dict(source);r=build_records('Who may use it?',[source])
        self.assertEqual(source,original)
        self.assertEqual(r['records'][0]['quote'],source['text'])
        self.assertIn('actual question',SYNTHESIS_GUIDANCE)

    def test_contextual_text_does_not_change_evidence(self):
        p=dict(title='Limits',text='The ceiling is 5.',section_heading='Mandates',circular_number='REF-1')
        self.assertEqual(lexical_text(p),'Limits Limits The ceiling is 5.')
        self.assertIn('Mandates',lexical_text(p,True))
        self.assertEqual(p['text'],'The ceiling is 5.')


class SynthesisIntegrationTests(unittest.TestCase):
    def setUp(self):research.ResearchTests.setUp(self)

    def test_records_are_internal_and_output_remains_question_answer(self):
        self.e.config['structured_evidence_enabled']=True
        def generate(endpoint,payload):
            prompt=json.loads(payload['prompt'])
            self.assertEqual(prompt['question'],'What must UPI participants do about consent?')
            self.assertTrue(prompt['evidence_records']['records'])
            self.assertEqual(payload['format']['properties']['claims']['items']['properties']['sources']['items']['enum'],[s['citation'] for s in prompt['evidence']])
            self.assertIn('natural language',payload['system'])
            return {'response':json.dumps(dict(abstain=False,claims=[dict(text='They must capture consent before processing the request.',sources=['S1'])],primary_claim_indices=[1],layout=[dict(type='paragraph',claim_indices=[1])]))}
        with patch.object(self.e,'ollama',side_effect=generate):
            r=self.e.answer(dict(query='What must UPI participants do about consent?',document_ids=['network'],mode='generate',method='bm25'))
        self.assertTrue(r['answer_blocks'])
        self.assertNotIn('record_id',json.dumps(r['answer_blocks']))
        self.assertEqual(r['claims'][0]['text'],'They must capture consent before processing the request.')

    def test_contextual_index_keeps_corpus_fingerprint(self):
        from app import Engine
        other=Engine(data_dir=self.e.data_dir,config=dict(self.e.config,contextual_bm25_enabled=True))
        self.assertEqual(self.e.fingerprint,other.fingerprint)
        self.assertEqual(self.e.parts,other.parts)
