"""Explicitly rebuild the development pilot from local text; independent review remains pending."""
import argparse
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from graph_context import digest, normal


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--data-dir', type=Path, required=True)
    args = ap.parse_args()
    pages = {(p['document_id'], p['source_page']): p for p in
             (json.loads(line) for line in (args.data_dir/'all_circular_pages.jsonl').open(encoding='utf-8-sig') if line.strip())}
    docs = {d['id']: d for d in json.loads((args.data_dir/'index.json').read_text(encoding='utf-8-sig'))}
    base = 'npci-source-1a52e564b7b10a4cc8b13dde'
    # Each quote is a locator in unchanged extracted text, not a corrected reading.
    specs = [
        ('dd_original',base,1,'shall be considered as failure and shall not be treated as Deemed Debit.', 'original exclusions',0),
        ('dd_original_codes',base,1,'VO- Payment stopped by court order Remitter Bank VH- Mandate signature is tampered or corrupt', 'original exclusions codes',0),
        ('dd_amendment','2026-OC-128A',1,'response codes VH, K1, 59, and VO were excluded from the deemed debit scope.', 'amendment codes table',0),
        ('dd_capital_market','2026-OC-128A',1,'Acquirer / Payee may claim the transaction amount if it is as per the mandate created;', 'capital market exceptions BGGD MCC purpose',1),
        ('dd_other_otm','2026-OC-128A',1,'are to be considered as declined and no service should be rendered by the Acquirer/Payee.', 'other OTM exception no service',1),
        ('dd_settlement','2026-OC-128A',1,'shall continue to be treated as Deemed Debit and settlement shall be done by debiting respective Remitter bank', 'settlement purpose codes',1),
        ('dd_genuine','2026-OC-128A',2,'populated strictly for genuine scenarios only.', 'excluded declines genuine',4),
        ('dd_report','2026-OC-128A',2,'use the Deemed Debit report and raw files for reconciliation', 'report reconciliation',3),
        ('dd_reconciliation','2026-OC-128A',2,'perform three (3) way reconciliation', 'reconciliation',3),
        ('dd_expiry','2026-OC-128A',2,'auto unblocked upon expiry of the mandate period.', 'expiry unblock',3),
        ('dd_claim_window','2026-OC-128A',2,'within the mandate validity period.', 'BGGD claim validity',3),
        ('dd_execution','2026-OC-128A',2,'no duplicate executions are processed.', 'duplicate executions adjustments',3),
        ('dd_effective','2026-OC-128A',2,'The changes in deemed debit applicability in the URCS system will be effective from', 'effective date chargeback',0),
        ('bio_original','2025-OC-226',1,'This facility shall initially be available for transactions up to Rs. 5,000.', 'original transaction limit',0),
        ('bio_optional','2025-OC-226',1,'These additional methods are optional for the user', 'optional authentication reference RBI',3),
        ('bio_pin_setup','2025-OC-226',1,'UIDAI Face Authentication shall be introduced as an additional option, for UPI PIN Set/Re-Set', 'PIN setup UIDAI distinct authentication',3),
        ('bio_security','2025-OC-226',1,'restricting usage on rooted or jail-broken devices', 'security device validation',1),
        ('bio_consent','2025-OC-226',2,'shall ensure explicit customer consent is obtained', 'consent opt out',1),
        ('bio_eligibility','2025-OC-226',2,'validate authentication credentials before authorising', 'eligibility credentials',3),
        ('bio_binding','2025-OC-226',2,'fresh consent is obtained after each device binding', 'device binding consent',1),
        ('bio_communication','2025-OC-226',2,'at the time of biometric enablement, disablement, and transaction processing.', 'communication',4),
        ('bio_reset','2025-OC-226',2,'shall disable this method for the account for all UPI Applications', 'PIN reset disable consent',1),
        ('bio_rotation','2025-OC-226',2,'before one year of biometric enablement.', 'key rotation',2),
        ('bio_inactive','2025-OC-226',2,'activated only upon customer confirmation.', 'ninety day inactive confirmation',2),
        ('bio_amendment','2026-OC-226A',1,'enhanced from ₹5,000 to ₹10,000, effective 07th August 2026.', 'changed transaction limit effective date',0),
        ('bio_continuity','2026-OC-226A',1,'All existing validations, compliance requirements, specifications, and regulatory guidelines shall continue to remain fully applicable', 'continuing requirements',0),
    ]
    nodes = []
    for key, doc, page, quote, aspect, priority in specs:
        source = pages[doc,page]
        assert quote in normal(source['text']), key
        nodes.append(dict(id=key,document_id=doc,page=page,quote=quote,aspect=aspect,priority=priority,
                          page_sha256=digest(source['text']),source_url=docs[doc].get('source_pdf')))
    edges = [
        dict(from_id='2026-OC-128A',to_id=base,type='amends_aspect',aspect='deemed_debit_response_codes_and_operations',evidence_anchor='dd_amendment',effective_date='2026-07-15',effective_date_anchor='dd_effective',review_status='proposed_ai_assisted'),
        dict(from_id='2026-OC-226A',to_id='2025-OC-226',type='amends_aspect',aspect='on_device_biometric_transaction_limit',evidence_anchor='bio_amendment',effective_date='2026-08-07',effective_date_anchor='bio_amendment',review_status='proposed_ai_assisted'),
    ]
    graph = dict(schema_version=1,id='upi-128-226-v1',review_status='proposed_ai_assisted',
        purpose='Development pilot; navigation and coverage, not legal precedence or completeness certification.',
        limitations=['OCR tables require original-PDF review. OC128 page 2 contains an incomplete sentence.',
            'Only two amendment families. OC88, OC206A and the RBI reference in OC226 are outside this pilot.',
            'Effective dates are provisional source readings; issue-date filtering is not an effective-date rule engine.',
            'No independent source or question review has been completed.'],
        nodes=nodes,edges=edges,topics=[
            dict(id='upi_deemed_debit',terms=['deemed debit'],anchors=[n['id'] for n in nodes if n['id'].startswith('dd_')]),
            dict(id='upi_biometric',terms=['biometric','biometrics','on device authentication'],anchors=[n['id'] for n in nodes if n['id'].startswith('bio_')]),
        ])
    path = ROOT/'pilot/upi_128_226_graph_v1.json'
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(graph,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(path)


if __name__ == '__main__':
    main()
