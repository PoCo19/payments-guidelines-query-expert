"""Curate extended graph pilot from unchanged local text; no automatic source review."""
import argparse
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from graph_context import digest,normal


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--data-dir',type=Path,required=True);a=ap.parse_args()
    pages={(p['document_id'],p['source_page']):p for p in (json.loads(l) for l in (a.data_dir/'all_circular_pages.jsonl').open(encoding='utf-8-sig') if l.strip())}
    docs={d['id']:d for d in json.loads((a.data_dir/'index.json').read_text(encoding='utf-8-sig'))}
    graph=json.loads((ROOT/'pilot/upi_128_226_graph_v1.json').read_text(encoding='utf8'))
    graph['id']='upi-extended-v2'
    for t in graph['topics']:t['products']=['UPI']
    for n in graph['nodes']:
        if n['id'] in ('dd_original','dd_original_codes'):n['support_group']='oc128_original_exclusion_table'
    d76='npci-source-1ab364443958f0c6fcad0acf';d141='npci-source-853953bec76d31753dfa5904';d141b='npci-source-ab9a46ef29ebae2022dbb869'
    d71='npci-source-9c7b5f01193a8e2a82195b29';d127='npci-source-4e6fac099b791778ded35153'
    specs=[
      ('mode_original',d76,2,'disable all Wallet loads (MCC 6540) through Collect requests.','original mode restrictions',2,'Historical wallet modes; not a universal transaction ceiling'),
      ('mode_a','2024-OC-76A',1,'transactions (Initiation mode ‘04’ and ‘05’) shall be','intent restrictions domestic QR',0,'P2P intent versus non-verified offline P2M and QR share'),
      ('mode_a_date','2024-OC-76A',1,'ensure compliance effective 1% April 2024.','compliance date OCR',1,'OCR date needs original PDF check'),
      ('mode_c_ref','2025-OC-76C',1,'NPCI/UPI/2024-25/OC76B dated 23 August 2024','reference unavailable intermediate',0,'Source refers to OC76B, whose text is unavailable'),
      ('mode_c_domestic','2025-OC-76C',2,'2000/- for all P2M (non-verified offline merchants)','domestic QR share',0,'Domestic QR share and non-verified offline P2M'),
      ('mode_c_global','2025-OC-76C',2,'QR share & Pay shall not be allowed for all (Modification for International) UPI Global P2M transactions','international QR restriction',0,'International UPI Global P2M QR share; distinguish domestic limit'),
      ('mode_c_date','2025-OC-76C',2,'ensure compliance effective 30" April 2025.','compliance date',1,'OC76C implementation deadline'),
      ('safe_snapshot',d141,1,'(Updated as on 23rd February 2026*)','snapshot revised text',0,'Revised 2026 snapshot; not the original 2022 wording'),
      ('safe_rent',d141,1,'141D/2024-25(Addendum) dated 2nd April 2025.','rent other permitted modes',0,'Revised OC141 references OC141D'),
      ('safe_mandate',d141,2,'This circular is not applicable for Mandate Transactions (One time and Recurring Mandates)','mandate exclusion',0,'OC141 excludes one-time and recurring mandate transactions'),
      ('safe_gaming',d141,1,'In-App intent only (transaction initiation mode 04 & 05)','gaming Android mode scope',2,'Gaming and Android-specific passage; not every merchant category'),
      ('safe_b',d141b,1,"not be allowed from 10th November 2022 for android users.",'digital precious metals collect',1,'MCC5412 digital goods; Android collect restriction; not physical jewellery MCC5944'),
      ('safe_d_ref','2025-OC-141D',1,'NPCI/UPIOC-141C/2022-23','missing intermediate references',1,'OC141A and OC141C are referenced but not found in the indexed collection'),
      ('safe_d_rent','2025-OC-141D',1,'transactions will be allowed on initiation mode 03(Bharat QR).','rent Bharat QR addition',0,'Rent MCC6513 adds Bharat QR to existing modes'),
      ('safe_d_mandate','2025-OC-141D',1,'This circular is not applicable for Mandate transactions (One time and Recurring Mandates)','rent mandate exclusion',0,'OC141D explicitly excludes mandates'),
      ('limits_hospital','2023-UPI-185',1,'lakhs for merchants under categories aligned to hospitals and educational services.','hospital education limit',1,'Specific verified hospital and education merchants, not all payments'),
      ('limits_tax','2024-OC-185A',1,'lakhs for entities under categories aligned to tax payments.','tax per transaction',0,'Tax-payment category and verified merchants'),
      ('limits_tax_mcc','2024-OC-185A',1,'9311’ strictly adheres to the tax payments only.','tax MCC due diligence',1,'MCC9311 tax payments; distinguish GeM EMD purpose despite same MCC'),
      ('limits_annex','2024-OC-185A',2,'Purpose Code — 01 (IPO), 25 (RDS) | (Existing - No Change)','IPO RDS retained limit',0,'Annexure labels IPO/RDS under OC127 as existing, no change'),
      ('limits_ref','2025-OC-185B',1,'Vide reference to NPCI/UPI/2024-25/0C/185 A','reference later category extension',3,'Page 1 has ambiguous OCR currency rendering; do not treat it as a verified tax value'),
      ('limits_verified','2025-OC-185B',1,'applicable for merchants which are categorised as ‘Verified Merchant’.','verified merchant restriction',0,'Enhanced limits require verified merchant classification'),
      ('limits_bank','2025-OC-185B',1,'within the overall ceilings prescribed by NPCI.','bank internal lower limit',0,'Member banks retain discretion within network ceilings'),
      ('limits_p2p','2025-OC-185B',1,'The per transaction limit for P2P shall continue as per the extant guidelines.','P2P unchanged deadline',0,'Merchant-category changes do not increase the P2P limit'),
      ('limits_capital','2025-OC-185B',2,'| 1 | Capital Market | 6211 | ₹5 Lakh | ₹10 Lakh |','capital market transaction versus daily',0,'Table distinguishes enhanced per-transaction limit from cumulative 24-hour limit'),
      ('limits_cc','2025-OC-185B',2,'| 5 | Credit Card Bill Payments | 5413 | ₹5 Lakh | ₹6 Lakh |','credit card bill daily transaction',0,'Credit-card bill payments: separate per-transaction and daily columns'),
      ('limits_gem','2025-OC-185B',2,'| 3 | Government e-Market Place (EMD Payments) | 9311 | ₹5 Lakh | ₹10 Lakh |','GeM EMD category',1,'GeM EMD is a specified use case, not every MCC9311 payment'),
      ('limits_cumulative','2025-OC-185B',2,'Issuing banks are required to ensure that such cumulative limits are kept at their end.','issuer cumulative enforcement',1,'Issuer responsibility for 24-hour cumulative ceilings'),
      ('ipo_original',d71,1,'maintain the per transaction limit of Rs. 2 lakhs for UPl based ASBA transactions','historical IPO mandate ceiling',1,'Historical OC71 UPI-ASBA scope; purpose01 and MCC6211'),
      ('ipo_enhanced',d127,1,'now enhanced to Rs 5 lakh for Retail Direct SchemeandUPIbasedASBAIPO.','IPO mandate transaction enhancement',0,'Specific UPI ASBA IPO and RDS per-transaction ceiling, separate purpose identifiers'),
    ]
    for key,doc,page,quote,aspect,priority,scope in specs:
        p=pages[doc,page];assert quote in normal(p['text']),key
        graph['nodes'].append(dict(id=key,document_id=doc,page=page,quote=quote,aspect=aspect,priority=priority,scope=scope,page_sha256=digest(p['text']),source_url=docs[doc].get('source_pdf')))
    def edge(a,b,proof,kind='references',**kw):
        return dict(from_id=a,to_id=b,type=kind,evidence_anchor=proof,review_status='proposed_ai_assisted',**kw)
    graph['edges'] += [
      edge('2024-OC-76A',d76,'mode_a'),edge('2025-OC-76C','2024-OC-76A','mode_c_ref'),edge('2025-OC-76C',d76,'mode_c_ref'),
      edge(d141,'2025-OC-141D','safe_rent'),edge(d141b,d141,'safe_b'),edge('2025-OC-141D',d141b,'safe_d_ref'),
      edge('2024-OC-185A','2023-UPI-185','limits_tax'),edge('2025-OC-185B','2024-OC-185A','limits_ref'),edge('2024-OC-185A',d127,'limits_annex'),
      edge(d127,d71,'ipo_enhanced','related_topic',target_anchor='ipo_original',aspect='UPI_ASBA_IPO_history_not_explicit_number_reference'),
      edge('2025-OC-185B',d127,'limits_capital','related_topic',target_anchor='ipo_enhanced',aspect='MCC6211_related_scopes_not_automatic_mandate_override'),
    ]
    def topic(id,terms,anchors,gaps=(),cautions=()):return dict(id=id,terms=terms,anchors=anchors,products=['UPI'],source_gaps=list(gaps),cautions=list(cautions))
    graph['topics'] += [
      topic('upi_modes_76',['qr share','share and pay','global p2m','intent based','wallet load'],[s[0] for s in specs if s[0].startswith('mode_')],
            ['OC76B is recorded but its text is unavailable. The complete intermediate change history cannot be confirmed.']),
      topic('upi_safeguards_141',['safeguarding','rent','rental','digital gold','precious metals','online gaming'],[s[0] for s in specs if s[0].startswith('safe_')],
            ['OC141A and OC141C are referenced but not found in the indexed collection.','OC141E is listed without public text. Its requirements cannot be inferred.'],
            ['The available OC141 text is updated as of February 2026; it cannot establish the exact wording of the original 2022 version.','A restriction for regular payments must not be silently applied to mandates expressly excluded by the source.']),
      topic('upi_category_limits_185',['hospital','hospitals','education','educational','tax','insurance','credit card bill','gem','capital market','merchant limits','higher limits'],[s[0] for s in specs if s[0].startswith('limits_')],
            cautions=['Distinguish transaction limits from cumulative 24-hour limits and retain verified-merchant and bank-policy conditions.','The OCR rendering of the earlier tax amount in OC185B page 1 is ambiguous; verify the original PDF instead of asserting that rendering as a new limit.']),
      topic('upi_ipo_limit',['ipo','asba','initial public offering'],['ipo_original','ipo_enhanced','limits_annex','limits_capital','limits_bank','limits_verified'],
            cautions=['Prioritise the source specific to UPI ASBA IPO purpose01 and MCC6211 when explaining a mandate limit. A cumulative capital-market table value is a different measure and does not by itself change a per-mandate ceiling.','The original OC71 extraction has an incomplete line; do not reconstruct missing execution conditions.']),
    ]
    graph['limitations'].append('Extended development pilot: scope and topic links are AI-curated, not independent legal review. Missing family members remain explicit.')
    path=ROOT/'pilot/upi_extended_graph_v2.json';path.write_text(json.dumps(graph,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(path)


if __name__=='__main__':main()
