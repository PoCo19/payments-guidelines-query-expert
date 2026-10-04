"""Synthetic teaching fixture; no assertions about real UPI LITE requirements."""

FACTS = [
 ('Pilot scope','This fictional UPI LITE pilot is limited to participants confirmed by the product owner.'),
 ('Customer enrollment','Customers in the fictional pilot explicitly opt in through a participating app.'),
 ('Customer support','The pilot support team records unresolved customer cases and escalates them to the designated partner contact.'),
 ('Marketing scope','Pilot communications must describe participating providers and must receive product and brand review before publication.'),
 ('Partner readiness','Partner readiness requires recorded integration test evidence and an assigned operational support owner.'),
 ('Risk assurance','Controls listed as documented require implementation and testing evidence before being treated as verified pilot coverage.')
]


def create_demo(store, actor='Demo owner'):
    w=store.create({'actor':actor,'role':'product','title':'UPI LITE · simulated pilot','brief':'Course demonstration of cross-functional feature launch coordination. All partner and control records are synthetic. This is not current NPCI product guidance.','simulated':True})
    def act(action,**values):
        nonlocal w
        w=store.mutate(w['id'],{'actor':actor,'role':'product','revision':w['revision'],'action':action,**values})
    act('source_add',title='Simulated feature brief — not an NPCI circular',kind='simulated',scope='shared',text='\n\n'.join(value for _,value in FACTS))
    source=w['sources'][0]['id']
    for label,value in FACTS: act('fact_save',label=label,value=value,source_id=source,quote=value)
    act('partner_save',name='Demo Bank A',capabilities='Synthetic candidate with a pilot integration team',stage='testing',evidence='Simulated test plan; completion not yet confirmed')
    act('partner_save',name='Demo App B',capabilities='Synthetic app candidate with an identified product contact',stage='interested')
    act('control_save',name='Pilot enrollment review',scope='Synthetic review of opt-in evidence',status='documented',owner='Demo Risk Owner',evidence='Simulated draft control description only')
    act('control_save',name='Pilot incident monitoring',scope='Proposed monitoring and escalation for pilot failures',status='proposed',owner='Demo Operations Owner')
    # Cross-team sequencing is explicit and editable, not guessed by the model.
    risk=next(t for t in w['tasks'] if t['team']=='risk')
    bd=next(t for t in w['tasks'] if t['team']=='bd')
    act('task_save',id=bd['id'],title=bd['title'],depends_on=[risk['id']],status='todo')
    return w


def create_feature_demo(store,actor='Example setup'):
    w=store.create({'actor':actor,'role':'product','title':'UPI LITE feature review','brief':'Review support guidance, partner impact and transaction-rule coverage for an existing feature. This example uses fictional internal evidence.','simulated':True,'workspace_type':'existing'})
    def act(action,**kw):
        nonlocal w
        w=store.mutate(w['id'],{'actor':actor,'role':'product','revision':w['revision'],'action':action,**kw})
    facts=[('Review scope','Assess customer support, communication, participant impact and transaction-rule coverage for the existing feature.'),
           ('Source review','Confirm the applicable requirements using selected circulars and the supplied internal feature documents.'),
           ('Support handling','Support guidance should identify the responsible participant and the route for unresolved transaction cases.'),
           ('Rule evidence','Current UPI-side transaction-rule configurations must be assessed from internal rule evidence; public circulars alone do not establish active configurations.')]
    act('source_add',title='Example feature review brief',scope='shared',kind='simulated',text='\n\n'.join(v for _,v in facts))
    source=w['sources'][-1]['id']
    for label,value in facts:act('fact_save',label=label,value=value,source_id=source,quote=value)
    rule_quote='Example transaction rule: Repeated attempts by the same payer within the configured window are sent for review when the configured threshold is exceeded. Status: documented; deployment and threshold evidence have not been supplied.'
    act('source_add',title='Example transaction rule register',scope='risk',kind='simulated',text=rule_quote)
    act('risk_rule_save',name='Repeated payer attempts',feature_scope='UPI payer transactions; applicability to this feature needs review',condition='Attempt count for the same payer within the configured window exceeds the configured threshold',response='review',status='documented',owner='Example transaction risk team',source_id=w['sources'][-1]['id'],quote=rule_quote,verification='Configuration and deployment evidence not supplied')
    act('partner_save',name='Example Bank A',capabilities='Existing participant; feature support and operational impact need confirmation',stage='candidate')
    risk=next(t for t in w['tasks'] if t['team']=='risk');bd=next(t for t in w['tasks'] if t['team']=='bd')
    act('task_save',id=bd['id'],title=bd['title'],depends_on=[risk['id']],status='todo')
    return w
