# How does UPI OC128A change the treatment of response codes 59 and K1 compared with OC128?

Status: Needs revalidation | Version: 2

Local reviewer attribution is not authentication. Imported snapshots do not certify current applicability.

## Question

How does UPI OC128A change the treatment of response codes 59 and K1 compared with OC128?

## Documented findings

UPI OC 128A changes the treatment of response code K1 by including it in the Deemed Debit scope for remitter banks, whereas UPI OC 128 excluded it from that scope. [S1, S4, S2]

## Review history

[
  {
    "id": 1,
    "item_id": "b703471d3fdf457685b8cdab8ca9b031",
    "version": 1,
    "at": "2026-10-20T13:12:10.803746+00:00",
    "action": "created",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 2,
    "item_id": "b703471d3fdf457685b8cdab8ca9b031",
    "version": 1,
    "at": "2026-10-20T13:12:19.536091+00:00",
    "action": "generation_started",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 3,
    "item_id": "b703471d3fdf457685b8cdab8ca9b031",
    "version": 2,
    "at": "2026-10-20T13:12:54.247231+00:00",
    "action": "generated",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 4,
    "item_id": "b703471d3fdf457685b8cdab8ca9b031",
    "version": 2,
    "at": "2026-10-20T17:56:20.596446+00:00",
    "action": "submit",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 9,
    "item_id": "b703471d3fdf457685b8cdab8ca9b031",
    "version": 2,
    "at": "2026-10-22T17:05:25.506365+00:00",
    "action": "source_or_configuration_changed",
    "reviewer": "",
    "note": "Source corpus or model/graph configuration changed. Regenerate before approval."
  }
]

## Snapshot

{
  "corpus": "d205ac78542f0e94d70f2beb68cd48b0ba242d1ef0024492c23bd32f67f889c8",
  "sources": {
    "2026-OC-128A": "b385e841930d616e6409c426fc9996707f62001c77489e59ed0fe73449d6565f",
    "npci-source-1a52e564b7b10a4cc8b13dde": "50918f76d11c1d4f8f2676f2bf712465b346feb59de361822e9727f694c8d90b",
    "npci-source-b46ab77f9c89add99339c841": "03ab0e46f5518413c2086c8d36bda8e4fe2227645cf2df362a35cc210cdf2ab0",
    "npci-source-c105a071f13b68399a188b87": "164858555f885732830ae712fdca2e6b668e62e2e7e3f5ee98ac691bb8d47b74"
  },
  "models": {
    "generation_model": "qwen3.5:9b",
    "embedding_model": "qwen3-embedding:0.6b",
    "context_length": 16384,
    "max_output_tokens": 3072
  },
  "graph": "6f31ab81eccd69f0568728cb0c4ae7da244295851e7f72e52c69cd073c9d2c45"
}

## Sources

### S1 — Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution, page 1

https://www.npci.org.in/uploads/UPI_OC_128_A_Addendum_to_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_3b1e59eab2.pdf

NATIONAL PAYMENTS: piste S00 | FORWPRD NPCI/UPI/OC-128A/2026-27 3° July 2026 To, All Members — Unified Payments Interface (UPI) a Dear Sir/Madam, Sub: Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution With reference to UP! OC no. NPCI/UPI/OC No. 128/2021-22 dated 14°" December 2021, response codes VH, K1, 59, and VO were excluded from the deemed debit scope. Basis the ecosystem feedback, the scope of Deemed Debit (DD) scenario are updated as mentioned below: Changes in the Deemed Debit Scenario: Decline Response Code and Description Decline B bee! P P ¥ Applicabilit 59 — Suspected fraud, decline/transaction declined | . | 1 | based on risk score by remitter | Remitter Bank Yes 2 K1 — Suspected fraud, decline/transaction declined Remitter Bank Yes based on risk score by remitter 3 | VO — Payment stopped by court order Remitter Bank No 4 |VH-— Mandate signature is tampered or corrupt Remitter Bank No 5 | VU/QD-— Mandate expired ae ae eed No 6 | VSs- Duplicate mandate request | ali Bank & Payer No | Note: No changes for any other response codes

### S2 — UPI OC 128 - Extension of additional response codes under Deemed Debit for mandate execution, page 1

https://www.npci.org.in/uploads/UPI_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_6b390acecf.pdf

Remitter Bank risk scoreby remitter K1- Suspected fraud, decline/transaction declined based on RemitterBank risk score by remitter VO- Payment stopped by court order Remitter Bank VH- Mandate signature is tampered or corrupt Remitter Bank Any un-responded/declined transactions with invalid response code apart from the above for mandate execution by remitter bank with Purpose Code 1, response shall be treated as Deemed Debit and settlement shall be done by debiting respective remitter bank and credit the same to acquirer bank. The identifier for such settlement shall be with response code RC- 1001A, The Capital, B Wing, 10th Flo0r, BandraKurlaComplex,Bandra(E),Mumbai4ooO51. T: +91 22 40009100 F: +91 22 40009101 contact@npci.org.in www.npci.org.in CIN:U74990MH2008NPL189067

### S3 — Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution, page 2

https://www.npci.org.in/uploads/UPI_OC_128_A_Addendum_to_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_3b1e59eab2.pdf

e) Issuer may raise chargebacks with appropriate reason codes for mandates executed post their validity period (Chargeback reason code 1081 — Transaction not settled within the specified timeframes) and duplicate executions (Chargeback reason code 1084 - Duplicate/Multiple Transaction), wherever applicable. Members to take note of the above and update the process accordingly. The changes in deemed debit applicability in the URCS system will be effective from 15" July 2026. Your Sincerely, 7 SD/- Giridhar GM Chief Customer Success 1001A, The Capital, B Wing, 10" Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051. Togethen (3 ee aera ener Rie CIN: U74990MH2008NPL189067

### S4 — UPI OC 128 - Extension of additional response codes under Deemed Debit for mandate execution, page 1

https://www.npci.org.in/uploads/UPI_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_6b390acecf.pdf

NPCI e Lpe hi at NATIONALPAYMENTSCORPORATIONOFINDIA NPCI/UPI/OCNo.128/2021-22 14th December, 2021 To All Members-Unified Payment Interface DearMadam/Sir, Subiect: Extension of additional response codes under Deemed Debit for mandate execution Mandate transactions functions with the premise that any mandate that is created successfully must also be executed successfully. To reduce the remitter end declines in case of the mandates execution including use case of [POs, we have developed the functionality of Deemed Debit (DD) for financial mandate execution which was introduced through UPI OC 88 dated 14th May, 2020 - Migration of "UP] - RGCS" system to “UPI Real Time Clearing & Settlement" (URCS) system w.e.f. 25th May 2020 wherein a few response codes under mandate execution was considered as Deemed Debit. Basis the ecosystem feedback, we have now extended the scope of Deemed Debit at the remitter side further wherein any declines at the remitter end shall be considered as Deemed Debit. Only in case if the remitter bank declines the transaction with the below mentioned response codes the transaction shall be considered as failure and shall not be treated as Deemed Debit. Sr. No Decline ResponseCode and Description Decline by 59-- Suspected fraud,decline/transaction declinedbased on

### S5 — Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution, page 1

https://www.npci.org.in/uploads/UPI_OC_128_A_Addendum_to_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_3b1e59eab2.pdf

3. Any un-responded/declined transactions with response codes apart from those mentioned above for mandate execution transactions with Purpose Code ‘01’ or ‘25’ or ‘76’, shall continue to be treated as Deemed Debit and settlement shall be done by debiting respective Remitter bank and crediting the Acquirer bank. JOOTA, The Capital, B Wing, 10° Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051- sae T: +91 22 40009100 F: +91 22 40009101 oer ‘on contact@npci.org.in www.npci.org.in eBuild Neem CIN: U74990MH2008NPL189067

### S6 — Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution, page 1

https://www.npci.org.in/uploads/UPI_OC_128_A_Addendum_to_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_3b1e59eab2.pdf

41. For 1PO, RDS and SBMD secondary markets use case (Purpose code ‘01’, ‘25’, ‘76 and where MCC is 6211): In case of declines with response codes ‘VO’, ‘VH’, ‘VU’, ‘QD’ or ‘VS’ i.e. from Sr. No. 3 to 6 mentioned above, Acquirer / Payee may claim the transaction amount if it is as per the mandate created; through BGGD option made available in URCS. [NPCVUPI/OC No. 206A/2024-25 dated 12'" March 2025]

### S7 — Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution, page 1

https://www.npci.org.in/uploads/UPI_OC_128_A_Addendum_to_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_3b1e59eab2.pdf

2. For other OTM use cases (i.e. purpose code ‘01’ and MCC other than 6211) Declines with response codes ‘VO’, ‘VH’, ‘VU’, ‘QD’ or ‘VS’ i.e. from Sr. No. 3 to 6 mentioned above, are to be considered as declined and no service should be rendered by the Acquirer/Payee.

### S8 — Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution, page 2

https://www.npci.org.in/uploads/UPI_OC_128_A_Addendum_to_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_3b1e59eab2.pdf

c) Acquirer banks can raise BGGD, wherever applicable, within the mandate validity period.

### S9 — Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution, page 2

https://www.npci.org.in/uploads/UPI_OC_128_A_Addendum_to_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_3b1e59eab2.pdf

d) Acquirer/Payee are advised to process executions within the mandate validity period and no duplicate executions are processed. In case of such instances, Acquirers should reconcile and process credit adjustments upfront.

### S10 — Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution, page 2

https://www.npci.org.in/uploads/UPI_OC_128_A_Addendum_to_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_3b1e59eab2.pdf

b) Remitter banks to ensure that funds blocked in the customer's account are auto unblocked upon expiry of the mandate period.

### S11 — Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution, page 2

https://www.npci.org.in/uploads/UPI_OC_128_A_Addendum_to_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_3b1e59eab2.pdf

a) Remitter and Acquirer banks are advised to perform three (3) way reconciliation for non- financial requests (create, update, revoke) and financial requests (execution) both with Mandate raw file and transaction raw file (including ‘Deemed Debit’ file) respectively.

### S12 — Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution, page 2

https://www.npci.org.in/uploads/UPI_OC_128_A_Addendum_to_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_3b1e59eab2.pdf

5. The identifier for such settlement shall be with response code ‘DD’ (Deemed Debit) in URCS for identifying the deemed debit transactions separately and initiate suitable actions. Also, additional report for transaction treated as Deemed Debit is made available to the member banks in URCS. All member banks are advised to use the Deemed Debit report and raw files for reconciliation purpose and necessary actions.

### S13 — Circular 45 - UPI OC 45 – Solution to reduce Deemed Transactions, page 1

https://www.npci.org.in/uploads/UPI_OC_45_Solutions_to_reduce_deemed_approved_transaction_d745e97fed.pdf

1 NPCI/ UPI/OC No. 45 /2017 – 18 12th Feb, 2018 To, All Members of Unified Payments Interface (UPI) Dear Sir / Madam, Subject: 1) Implementation of new response/error codes

### S14 — OC149 A - Addendum to OC 149 - Reduction of business declines in UPI, page 3

https://www.npci.org.in/uploads/OC_149_A_Addendum_to_OC_149_Reduction_of_business_declines_in_UPI_fdec42948f.pdf

Annexure UPI Decline Codes UPI Decline Response Code Description of Decline Response Code Type of Declines To be checked by Suggested Actions Z7 TRANSACTION FREQUENCY LIMIT EXCEEDED AS SET BY REMITTING MEMBER Bank Induced Remitter Bank,

### S15 — UPI OC 128 - Extension of additional response codes under Deemed Debit for mandate execution, page 2

https://www.npci.org.in/uploads/UPI_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_6b390acecf.pdf

Annex I. With the increase of scope of Deemed Debit, the acquirer bank has to ensure that there should transactions and reverse the same to respective remitter bank through credit adjustments on same day or T+1 where T is the execution day of the transaction. Remitter banks are aiso advised use the Deemed Debit report for reconciliation purpose and necessary actions. With reference to the above request the member banks to take note of the above enhancement and undertake the requisite changes. Yours sincerely, Saiprasad Nabar Chief Online Products Operations & Technology 1001A, The Capital, B Wing, 10th Floor, BandraKurlaComplex,Bandra(E),Mumbai4ooQ51. T: +91 22 40009100 F: +91 22 40009101 contact@npci.org.inwww.npci.org.in CIN:U74990MH2008NPL189067

### S16 — OC149 A - Addendum to OC 149 - Reduction of business declines in UPI, page 3

https://www.npci.org.in/uploads/OC_149_A_Addendum_to_OC_149_Reduction_of_business_declines_in_UPI_fdec42948f.pdf

Payer PSP 1. Analyse the reason of decline. If it is on account of wrong mapping of response code, correct the mapping.

### S17 — Circular 45 - UPI OC 45 – Solution to reduce Deemed Transactions, page 1

https://www.npci.org.in/uploads/UPI_OC_45_Solutions_to_reduce_deemed_approved_transaction_d745e97fed.pdf

2) Best practices to reduce - ‘Deemed approved’ transactions, ‘Unsuccessful debit Reversals’ and ‘overall declines’ Objective: Objective of this circular is to explain the process to reduce deemed approved & debit time out transactions (requiring DRC from Member banks) in UPI. This shall help to reduce operational work, avoid customer complaints and enhance positive user experience. To meet the above objective, we propose following changes: Other key requirements:

### S18 — UPI OC 128 - Extension of additional response codes under Deemed Debit for mandate execution, page 2

https://www.npci.org.in/uploads/UPI_OC_128_Extension_of_additional_response_codes_under_Deemed_Debit_for_mandate_execution_6b390acecf.pdf

NPCI NATIONAL PAYMENTS CORPORATION OFINDIA DD (Deemed Debit) in URCS for identifying the deemed debit transactions separately and initiate suitable actions in CBs. Also, additional report for transaction treated as Deemed Debit is also provided to the member banks in URCs. The format of such report is mentioned in

## Automated review limitations

{
  "coverage": {
    "status": "issues_flagged",
    "findings": [
      {
        "kind": "possible_conflict",
        "reason": "The answer claims OC128A includes response code 59 in the Deemed Debit scope, but evidence S1.1 explicitly lists '59' with a 'Decline by Remitter Bank' status of 'Yes', while the answer's text implies a change from exclusion to inclusion for K1 only, creating ambiguity about 59's status relative to OC128.",
        "quotes": [
          {
            "citation": "S1",
            "quote": "NATIONAL PAYMENTS: piste S00 | FORWPRD NPCI/UPI/OC-128A/2026-27 3° July 2026 To, All Members — Unified Payments Interface (UPI) a Dear Sir/Madam, Sub: Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution With reference to UP! OC no. NPCI/UPI/OC No. 128/2021-22 dated 14°\" December 2021, response codes VH, K1, 59, and VO were excluded from the deemed debit scope. Basis the ecosystem feedback, the scope of Deemed Debit (DD) scenario are updated as mentioned below: Changes in the Deemed Debit Scenario: Decline Response Code and Description Decline B bee! P P ¥ Applicabilit 59 — Suspected fraud, decline/transaction declined | . | 1 | based on risk"
          },
          {
            "citation": "S4",
            "quote": " (URCS) system w.e.f. 25th May 2020 wherein a few response codes under mandate execution was considered as Deemed Debit. Basis the ecosystem feedback, we have now extended the scope of Deemed Debit at the remitter side further wherein any declines at the remitter end shall be considered as Deemed Debit. Only in case if the remitter bank declines the transaction with the below mentioned response codes the transaction shall be considered as failure and shall not be treated as Deemed Debit. Sr. No Decline ResponseCode and Description Decline by 59-- Suspected fraud,decline/transaction declinedbased on"
          }
        ]
      },
      {
        "kind": "possible_conflict",
        "reason": "The answer states OC128 excluded K1 from the Deemed Debit scope, yet evidence S2.1 and S4.2 show that in OC128, K1 was already listed under 'Decline by Remitter Bank' with a 'Yes' status, contradicting the claim that it was excluded.",
        "quotes": [
          {
            "citation": "S2",
            "quote": "Remitter Bank risk scoreby remitter K1- Suspected fraud, decline/transaction declined based on RemitterBank risk score by remitter VO- Payment stopped by court order Remitter Bank VH- Mandate signature is tampered or corrupt Remitter Bank Any un-responded/declined transactions with invalid response code apart from the above for mandate execution by remitter bank with Purpose Code 1, response shall be treated as Deemed Debit and settlement shall be done by debiting respective remitter bank and credit the same to acquirer bank. The identifier for such settlement shall be with response code RC- 1001A, The Capital, B Wing, 10th Flo0r, BandraKurlaComplex,Bandra(E),Mumbai4ooO51. T: +91 22"
          },
          {
            "citation": "S4",
            "quote": " (URCS) system w.e.f. 25th May 2020 wherein a few response codes under mandate execution was considered as Deemed Debit. Basis the ecosystem feedback, we have now extended the scope of Deemed Debit at the remitter side further wherein any declines at the remitter end shall be considered as Deemed Debit. Only in case if the remitter bank declines the transaction with the below mentioned response codes the transaction shall be considered as failure and shall not be treated as Deemed Debit. Sr. No Decline ResponseCode and Description Decline by 59-- Suspected fraud,decline/transaction declinedbased on"
          }
        ]
      },
      {
        "kind": "scope_unclear",
        "reason": "The answer contrasts OC128A and OC128 regarding K1 but does not clarify whether 59's treatment changed or remained the same, leaving the scope of the change ambiguous.",
        "quotes": [
          {
            "citation": "S1",
            "quote": "NATIONAL PAYMENTS: piste S00 | FORWPRD NPCI/UPI/OC-128A/2026-27 3° July 2026 To, All Members — Unified Payments Interface (UPI) a Dear Sir/Madam, Sub: Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution With reference to UP! OC no. NPCI/UPI/OC No. 128/2021-22 dated 14°\" December 2021, response codes VH, K1, 59, and VO were excluded from the deemed debit scope. Basis the ecosystem feedback, the scope of Deemed Debit (DD) scenario are updated as mentioned below: Changes in the Deemed Debit Scenario: Decline Response Code and Description Decline B bee! P P ¥ Applicabilit 59 — Suspected fraud, decline/transaction declined | . | 1 | based on risk"
          },
          {
            "citation": "S4",
            "quote": " (URCS) system w.e.f. 25th May 2020 wherein a few response codes under mandate execution was considered as Deemed Debit. Basis the ecosystem feedback, we have now extended the scope of Deemed Debit at the remitter side further wherein any declines at the remitter end shall be considered as Deemed Debit. Only in case if the remitter bank declines the transaction with the below mentioned response codes the transaction shall be considered as failure and shall not be treated as Deemed Debit. Sr. No Decline ResponseCode and Description Decline by 59-- Suspected fraud,decline/transaction declinedbased on"
          }
        ]
      },
      {
        "kind": "possible_conflict",
        "reason": "The answer implies a clear distinction between OC128 and OC128A for K1, but evidence S2.1 and S4.2 suggest K1 was already included in OC128, making the stated change inaccurate.",
        "quotes": [
          {
            "citation": "S2",
            "quote": "Remitter Bank risk scoreby remitter K1- Suspected fraud, decline/transaction declined based on RemitterBank risk score by remitter VO- Payment stopped by court order Remitter Bank VH- Mandate signature is tampered or corrupt Remitter Bank Any un-responded/declined transactions with invalid response code apart from the above for mandate execution by remitter bank with Purpose Code 1, response shall be treated as Deemed Debit and settlement shall be done by debiting respective remitter bank and credit the same to acquirer bank. The identifier for such settlement shall be with response code RC- 1001A, The Capital, B Wing, 10th Flo0r, BandraKurlaComplex,Bandra(E),Mumbai4ooO51. T: +91 22"
          },
          {
            "citation": "S4",
            "quote": " (URCS) system w.e.f. 25th May 2020 wherein a few response codes under mandate execution was considered as Deemed Debit. Basis the ecosystem feedback, we have now extended the scope of Deemed Debit at the remitter side further wherein any declines at the remitter end shall be considered as Deemed Debit. Only in case if the remitter bank declines the transaction with the below mentioned response codes the transaction shall be considered as failure and shall not be treated as Deemed Debit. Sr. No Decline ResponseCode and Description Decline by 59-- Suspected fraud,decline/transaction declinedbased on"
          }
        ]
      }
    ],
    "basis": "Automated same-model review of supplied evidence only; not exhaustive or independent verification."
  },
  "withheld": [
    {
      "text": "UPI OC 128A changes the treatment of response code 59 by including it in the Deemed Debit scope for remitter banks, whereas UPI OC 128 excluded it from that scope.",
      "sources": [
        "S1",
        "S4",
        "S2"
      ],
      "draft_index": 1,
      "original_sources": [
        "S1",
        "S4"
      ],
      "citation_context_added": [
        "S2"
      ],
      "support_status": "unsupported",
      "review_reasons": [
        "The local model found that the cited evidence does not fully support the claim."
      ]
    }
  ],
  "warnings": [
    "Coverage is limited to the imported snapshot. Issue dates are not effective dates. OCR text may contain errors; verify figures and tables against the original.",
    "Graph pilot: source-anchored proposed links; independent review is pending. Preserve each requirement's scope and effective date. A partial amendment does not replace the entire original circular. Current applicability beyond the indexed sources is unverified.",
    "Some evidence was omitted by the passage/character budget. Coverage is partial.",
    "Imported document metadata and extraction remain unverified; consult the original PDFs. Unknown issue dates are excluded when using an issue-date cutoff.",
    "Research entity was not specified. Source-specific applicability must remain explicit in the answer.",
    "Some graph-pilot anchors were excluded by filters or context limits; linked-rule coverage is partial.",
    "Claims are automatically checked against cited excerpts. This is not independent expert verification. Uncertain or unsupported claims are withheld for review.",
    "1 of 2 draft claims were withheld. The remaining statements may not fully answer your question; inspect the sources and review details.",
    "Citation IDs are validated. Whether each citation supports its claim still requires review.",
    "The answer may omit a material qualification or contain an unresolved difference in scope. Inspect the evidence review below."
  ]
}