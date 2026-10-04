import json,unittest
from unittest.mock import patch
from answer_format import format_answer,requested_style
from app import Engine

def claim(i):return dict(draft_index=i,text=f'Checked statement {i}.',sources=['S1'],support_status='automated_supported')
def block(kind,*indices):return dict(type=kind,claim_indices=list(indices))

class AnswerFormatTests(unittest.TestCase):
 def test_auto_respects_paragraph_layout(self):
  blocks,origin=format_answer([claim(1),claim(2)],[block('paragraph',1,2)],2)
  self.assertEqual(origin,'model_layout');self.assertEqual(blocks[0]['type'],'paragraph');self.assertEqual(len(blocks[0]['claims']),2)
 def test_auto_mixed_and_steps(self):
  blocks,origin=format_answer([claim(1),claim(2),claim(3)],[block('paragraph',1),block('steps',2,3)],3)
  self.assertEqual([b['type'] for b in blocks],['paragraph','steps'])
 def test_rejected_claim_cannot_leak_into_layout(self):
  blocks,_=format_answer([claim(2)],[block('paragraph',1),block('bullets',2)],2)
  self.assertEqual(blocks,[dict(type='bullets',claims=[claim(2)])])
 def test_all_withheld_produces_no_blocks(self):
  self.assertEqual(format_answer([],[block('paragraph',1)],1)[0],[])
 def test_invalid_layout_falls_back_without_losing_claims(self):
  invalid=[None,'text',[],[block('paragraph',1,1)],[block('paragraph',1,3)],
           [block('paragraph',1)],[block('script',1,2)],[block('paragraph',True,2)],
           [dict(type='paragraph',claim_indices=[1,2],text='Unchecked conclusion')]]
  for layout in invalid:
   blocks,origin=format_answer([claim(1),claim(2)],layout,2)
   self.assertEqual(origin,'fallback');self.assertEqual([c for b in blocks for c in b['claims']],[claim(1),claim(2)])
 def test_explicit_style_overrides_model(self):
  for style,expected in [('paragraphs',['paragraph']),('bullets',['bullets']),('mixed',['paragraph','bullets'])]:
   blocks,_=format_answer([claim(1),claim(2)],[block('steps',1,2)],2,style)
   self.assertEqual([b['type'] for b in blocks],expected)
 def test_mixed_repaired_after_intro_withheld(self):
  blocks,_=format_answer([claim(2),claim(3)],[block('paragraph',1),block('bullets',2,3)],3,'mixed')
  self.assertEqual([b['type'] for b in blocks],['paragraph','bullets'])
 def test_single_claim_never_invents_mixed_intro(self):
  self.assertEqual(format_answer([claim(1)],None,1,'mixed')[0],[dict(type='paragraph',claims=[claim(1)])])
 def test_explicit_question_format_and_selector(self):
  for q,style in [('Explain in a paragraph','paragraphs'),('Answer without bullets','paragraphs'),('Use bullet points only','bullets'),('Use a mix of paragraphs and bullets','mixed')]:
   self.assertEqual(requested_style('auto',q),style)
  self.assertEqual(requested_style('bullets','Explain in a paragraph'),'bullets')
  with self.assertRaises(ValueError):requested_style('html','question')
 def test_backend_filters_before_materializing_layout(self):
  e=Engine.__new__(Engine);e.config={'generation_model':'test','claim_check_enabled':True}
  e.ollama=lambda *args:{'response':json.dumps({'abstain':False,'claims':[{'text':'Good','sources':['S1']},{'text':'Bad','sources':['S1']}],'layout':[block('paragraph',1,2)]})}
  with patch('app.assemble',return_value=([dict(citation='S1')],dict(notes=[],route='clause'))),patch('app.check_claims',side_effect=lambda e,c,s:([dict(c[0],support_status='automated_supported')],[c[1]],[])):
   result=e.answer(dict(query='Explain',mode='generate'))
  self.assertEqual(result['answer_blocks'][0]['claims'][0]['text'],'Good')
  self.assertNotIn('Bad',json.dumps(result['answer_blocks']))
  self.assertEqual(len(result['flagged_claims']),1)

if __name__=='__main__':unittest.main()
