import json
import unittest
from types import SimpleNamespace
from unittest.mock import Mock
from evidence_focus import phase_matches,phase_companions
from evaluation.coverage_candidate import check_answer_coverage
from evaluation.coverage_review_candidate import review_findings
from claim_repair import repair_claims


class NotificationRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.pre=dict(id='pre',document_id='direction',text='Pre-transaction notification is not required for MetroCard auto-replenishment.',section_heading='Pre-transaction notification',next_chunk_id='post')
        self.post=dict(id='post',document_id='direction',text='An issuer shall send a post-transaction notification.',section_heading='Post-transaction notification')

    def test_lower_ranked_phase_survives_topic_dominance(self):
        distractors=[dict(id=str(i),text='MetroCard issuer refund debit messages',section_heading='Refund') for i in range(20)]
        query='Can MetroCard auto-replenishment omit the message after a debit because advance notice is exempt?'
        protected=phase_matches(query,distractors+[self.pre])
        self.assertEqual(protected,[self.pre])
        engine=SimpleNamespace(parts_by_id={'pre':self.pre,'post':self.post})
        self.assertEqual(phase_companions(engine,query,protected),[self.post])

    def test_common_notification_terms_do_not_establish_topic(self):
        self.assertFalse(phase_matches('Must the issuer send notification after debit?',[self.pre]))
        self.assertFalse(phase_matches('Must a foreign wire send a message after debit?',[self.pre]))
        self.assertFalse(phase_matches('What are MetroCard refund rules?',[self.pre]))

    def test_focused_candidates_bounded_without_mutation(self):
        before=dict(self.pre)
        self.assertEqual(len(phase_matches('MetroCard notices after debit',[dict(self.pre,id=str(i)) for i in range(6)])),2)
        self.assertEqual(self.pre,before)

    def test_repair_keeps_requested_phase_beyond_first_six_sources(self):
        sources=[dict(citation='S1',document_id='direction',text=self.pre['text'],section_heading=self.pre['section_heading'])]
        sources += [dict(citation=f'S{i}',document_id='other',text='Unrelated context.') for i in range(2,9)]
        sources.append(dict(citation='S9',document_id='direction',text=self.post['text'],section_heading=self.post['section_heading']))
        claim=dict(text='Post-transaction notification is exempt.',sources=['S1'],draft_index=1,review_reasons=['The cited notification rule concerns a different event phase.'])
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(return_value={'response':json.dumps(dict(status='unresolved',text='',sources=[]))}))
        _,_,_,audit=repair_claims(engine,[],[claim],[],sources,'Is the MetroCard message after debit optional?')
        prompt=json.loads(engine.ollama.call_args.args[1]['prompt'])
        ids=[s['citation'] for s in prompt['evidence']]
        self.assertIn('S9',ids);self.assertIn('S1',ids);self.assertLessEqual(len(ids),6)
        self.assertEqual(audit[0]['evidence_citations'],ids)

    def test_combined_phase_and_scope_failure_can_still_attempt_repair(self):
        sources=[dict(citation='S1',document_id='direction',text=self.pre['text'],section_heading=self.pre['section_heading']),
                 dict(citation='S2',document_id='direction',text=self.post['text'],section_heading=self.post['section_heading'])]
        claim=dict(text='Post-transaction notification is exempt.',sources=['S1'],draft_index=1,
                   review_reasons=['The cited notification rule concerns a different event phase.',
                                   'The specific scope (MetroCard) is not supported.'])
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(return_value={'response':json.dumps(dict(status='unresolved',text='',sources=[]))}))
        _,remaining,_,audit=repair_claims(engine,[],[claim],[],sources,'Is the MetroCard message after debit optional?')
        self.assertEqual(engine.ollama.call_count,1)
        self.assertEqual(audit[0]['status'],'unresolved')
        self.assertEqual(remaining,[claim])


class CoverageContextTests(unittest.TestCase):
    def engine(self,rows):
        return SimpleNamespace(config={'generation_model':'test'},ollama=Mock(return_value={'response':json.dumps(dict(findings=rows))}))

    def test_warning_dismissal_needs_exact_answer_quote(self):
        claims=[dict(text='Only enrolled merchants qualify.',sources=['S1'])]
        findings=[dict(kind='possible_omission',reason='Missing condition',quotes=[])]
        for quote in ['', 'All merchants qualify.']:
            with self.subTest(quote=quote),self.assertRaises(ValueError):
                review_findings(self.engine([dict(index=0,decision='already_addressed',reason='Covered',answer_quote=quote)]),'Who qualifies?',claims,findings)
        kept,audit=review_findings(self.engine([dict(index=0,decision='already_addressed',reason='Explicit condition',answer_quote='Only enrolled merchants qualify.')]),'Who qualifies?',claims,findings)
        self.assertFalse(kept);self.assertEqual(audit[0]['proposal'],findings[0])

    def test_every_proposal_needs_a_unique_review(self):
        findings=[dict(kind='possible_omission',reason='First',quotes=[]),dict(kind='possible_omission',reason='Second',quotes=[])]
        with self.assertRaises(ValueError):
            review_findings(self.engine([dict(index=0,decision='retain',reason='Gap',answer_quote='')]*2),'Question',[],findings)

    def test_unavailable_second_reading_preserves_warnings(self):
        finding=dict(kind='possible_omission',reason='Condition missing',evidence_ids=['S1.1'])
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(side_effect=[{'response':json.dumps(dict(findings=[finding]))},TimeoutError('test')]))
        r=check_answer_coverage(engine,[dict(text='It applies.',sources=['S1'])],[dict(citation='S1',document_id='a',text='Only enrolled merchants qualify.'),dict(citation='S2',document_id='b',text='Other rules.')],dict(query='Who qualifies?',entity='',requested_aspects=['requirements']))
        self.assertEqual(r['status'],'issues_flagged');self.assertEqual(r['findings'][0]['review_status'],'unverified')
        self.assertEqual(r['warning_review_status'],'unavailable')

    def test_reviewer_receives_intact_qualification_and_exact_text(self):
        text='Only for verified merchants. '+('Illustrative context. '*45)+' These categories are excluded.'
        sources=[dict(citation='S1',document_id='one',text=text),dict(citation='S2',document_id='two',text='The addendum includes the previously excluded category.')]
        engine=SimpleNamespace(config={'generation_model':'test'},ollama=Mock(return_value={'response':json.dumps({'findings':[dict(kind='possible_omission',reason='A qualification is missing.',evidence_ids=['S1.1'])]})}))
        r=check_answer_coverage(engine,[dict(text='The limit applies.',sources=['S1'])],sources,dict(query='What applies?',entity='',requested_aspects=['requirements']))
        payload=engine.ollama.call_args_list[0].args[1]
        evidence=json.loads(payload['prompt'])['evidence']
        self.assertEqual(evidence[0]['excerpts'],[dict(id='S1.1',text=text)])
        self.assertEqual(r['findings'][0]['quotes'][0]['quote'],text)
        self.assertEqual(sources[0]['text'],text)

if __name__=='__main__':unittest.main()
