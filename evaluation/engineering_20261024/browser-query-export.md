# Does the 10 lakh cumulative Capital Market figure in UPI OC185B make a single IPO mandate limit 10 lakh?

Status: Needs review | Version: 3

Local reviewer attribution is not authentication. Imported snapshots do not certify current applicability.

## Question

Does the 10 lakh cumulative Capital Market figure in UPI OC185B make a single IPO mandate limit 10 lakh?

## Documented findings

The table in UPI OC 185B (The cited source) lists a 'Cumulative Limits (24 hrs)' of ₹10 Lakh for the Capital Market category but does not state that this figure sets the per-mandate limit for a single IPO. [S1]

The cited source (OC 127) establishes that the per transaction value limit for UPI based ASBA IPO is Rs 5 Lakh, while The cited source (OC 71) historically advised maintaining a per transaction limit of Rs 2 lakhs for UPI based ASBA transactions. [S2, S8]

Engineering test draft: independent payments review pending.

## Review history

[
  {
    "id": 1,
    "item_id": "d8a58f46905749f181159c87f9ecbb37",
    "version": 1,
    "at": "2026-10-23T19:29:25.576277+00:00",
    "action": "created",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 2,
    "item_id": "d8a58f46905749f181159c87f9ecbb37",
    "version": 1,
    "at": "2026-10-23T19:29:42.274199+00:00",
    "action": "generation_started",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 3,
    "item_id": "d8a58f46905749f181159c87f9ecbb37",
    "version": 2,
    "at": "2026-10-23T19:30:03.015781+00:00",
    "action": "generated",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 4,
    "item_id": "d8a58f46905749f181159c87f9ecbb37",
    "version": 3,
    "at": "2026-10-24T04:09:23.591481+00:00",
    "action": "edited",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 5,
    "item_id": "d8a58f46905749f181159c87f9ecbb37",
    "version": 3,
    "at": "2026-10-24T04:09:32.936834+00:00",
    "action": "submit",
    "reviewer": "",
    "note": ""
  }
]

## Snapshot

{
  "corpus": "d205ac78542f0e94d70f2beb68cd48b0ba242d1ef0024492c23bd32f67f889c8",
  "sources": {
    "2023-UPI-181": "8b377e94550d322f20b1c3b16fb310a15ae1aa6dcdcfcc2c5a5759e20ea4bf8d",
    "2023-UPI-185": "badd6513dfccee57eb7de84b4141ecbc0458e6f454adf717a68182c717078c50",
    "2024-OC-185A": "d0d81eb10066693cdc5d20f32e5e248cd9ea501f2b524e30640d251dcdb18da9",
    "2024-OC-200": "ba8f17a6602b004ffce35dcfb3f551325b620158cabdacd950160d99eebd6d0a",
    "2025-OC-185B": "58a16b264a0a8e296388b9bc4578f69001d6744ecc1a9fd99adf937d75b334ba",
    "npci-source-4e6fac099b791778ded35153": "79a8f1e072c7346e093cd48807d2cc9c252dbb1972d212fc8733f5b108ddcbbb",
    "npci-source-9c7b5f01193a8e2a82195b29": "d96a33fee000d21a44fd30e077539c4da38fa10b4f5039d7e49246c05ed1e8aa"
  },
  "models": {
    "generation_model": "qwen3.5:9b",
    "embedding_model": "qwen3-embedding:0.6b",
    "context_length": 16384,
    "max_output_tokens": 3072
  },
  "installed_models": {
    "status": "available",
    "digests": {
      "qwen3.5:9b": "6488c96fa5faab64bb65cbd30d4289e20e6130ef535a93ef9a49f42eda893ea7",
      "qwen3-embedding:0.6b": "ac6da0dfba84a81fdbfbaf330198c33cd77c4cdfc53e8bc50eb581914a15621d"
    }
  },
  "graph": "6f31ab81eccd69f0568728cb0c4ae7da244295851e7f72e52c69cd073c9d2c45"
}

## Sources

### S1 — Addendum to OC 185A -Implementation of higher per transaction limit for specific categories in UPI, page 2

https://www.npci.org.in/uploads/UPI_OC_No185_B_FY_2025_26_Addendum_to_OC_185_A_Implementation_of_higher_per_transaction_limit_for_specific_categories_in_UPI_ba517a0902.pdf

### Annexure I 1. Below are the categories where higher limits are extended | Sr No | Categories | Merchant Category/Identifier | Enhanced Limits | Cumulative Limits (24 hrs) * | |---|---|---|---|---| | 1 | Capital Market | 6211 | ₹5 Lakh | ₹10 Lakh | | 2 | Insurance | 5960; 6300; 6529 | ₹5 Lakh for each listed MCC | ₹10 Lakh | | 3 | Government e-Market Place (EMD Payments) | 9311 | ₹5 Lakh | ₹10 Lakh | | 4 | Travel | 4722 | ₹5 Lakh | ₹10 Lakh | | 5 | Credit Card Bill Payments | 5413 | ₹5 Lakh | ₹6 Lakh | | 6 | Collections | 7322 | ₹5 Lakh | ₹10 Lakh | | 7 | Business/Merchant (Including Pre-Approved Payments) | Payer MCC shall not be 0000 and Purpose Code — 20 or 15 | ₹5 Lakh | NA | | 8 | Jewellery | 5944 | ₹2 Lakh | ₹6 Lakh | | 9 | FX Retail use case with BBPS Platform | MCC-6012; Purpose Code — BF (New Purpose Code for regular UPI transaction); Purpose Code — 01 (For One Time Mandate) | ₹5 Lakh | ₹5 Lakh | | 10 | Digital Account Opening for Term Deposits | 7410 (New MCC) | ₹5 Lakh | ₹5

### S2 — UPI OC 127 - Implementation of Rs 5 Lakh limit per transaction for specific categories in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_127_Implementation_of_Rs_5_Lakh_limit_per_transaction_for_specific_categories_in_UPI_9c0353fa31.pdf

NPCI NATIONALPAYMENTSCORPORATIONOFINDIA NPCI/UPI/OCNo.127/2021-22 gthDecember,2021 ToAllMember-UnifiedPaymentsInterface(UPl) DearMadam/Sir, Subject:lImplementationof Rs5Lakh limitpertransactionforSpecificCategories inUPl With UPl emerging as a preferred payment method, there is need to extend the per transaction limit in UPl which ispresentlyuptoRs2Lakhpertransactionforspecificusecases. In view of the above,theper transactionvalue limit inUPl has been now enhanced to Rs 5 lakh for Retail Direct SchemeandUPIbasedASBAIPO.Thedetailsareasbelow Foruse-case qualifying underthefollowing business categories; Category Identifier Purpose Code01 InitiaiPublicOffering(IPO) MCC - 6211 GSec throughRBl Retail Direct PurposeCode25 Scheme(RDS)* MCC - 6211 *For RDS wehave introduced a new purpose as an identifier which is purpose code 25.Memberbank acting as an acquirer for RDS scheme shall send the transaction with the new purpose code All such transactions shall be considered under "Verified Merchant"and appropriate rules will be applicable. Merchants and other payment providers are requested to take note of the above enhancement and undertake requisite changeson the App&application systems.Members arerequestedtomake the necessary changes by 14th December, 2021. Yours sincerely, Praveena Rai ChiefOperatingOfficer 1001A,TheCapital,BWing,10thFlo0r, BandraKurlaComplex,Bandra(E),Mumbai4ooO51. T:+912240009100F:+912240009101 contact@npci.org.inwww.npci.org.in CIN:U74990MH2008NPL189067

### S3 — Addendum to OC 185 - Implementation of Rs 5 Lakh limit per transaction for specific categories in UPI, page 2

https://www.npci.org.in/uploads/UPI_OC_No_185_A_FY_24_25_Implementation_of_Rs_5_Lakh_limit_per_transaction_for_specific_categories_in_UPI_054c82bc8b.pdf

aR ART eT |p NATIONAL PAYMENTS CORPORATION OF INDIA Annexure to OC 185A Implementation of Rs 5 Lakh limit per transaction for specific categories in UPI Regarding circular no. NPCI/UPI/ 2024-25/OC-185A, which pertains to the implementation of a Rs 5 Lakh limit per transaction for verified merchants in specific categories in UPI - Category Circular reference & ee Tax Payments MCC - 9311 NPCI/UPI/2024-25/0C-185A Hospitals and MCC - 8011, 8021, 8031, 8041, NPCI/UPI/2023-24/0C-185 Educational 8042, 8049, 8050, 8062, 8071, (Existing — No Change) Services 8099, 0742, 8211, 8220, 8241, 8244, 8249, 8299 IPO & G Sec MCC 6211, NPCI/UPI/OC-127/2021 -22 through RBI Purpose Code — 01 (IPO), 25 (RDS) | (Existing - No Change) Retail Direct Scheme (RDS) Note:

### S4 — Addendum to OC 185A -Implementation of higher per transaction limit for specific categories in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_No185_B_FY_2025_26_Addendum_to_OC_185_A_Implementation_of_higher_per_transaction_limit_for_specific_categories_in_UPI_ba517a0902.pdf

3. Member banks may continue to be provided the discretion to set their internal limits based on their internal policy, within the overall ceilings prescribed by NPCI.

### S5 — Addendum to OC 185A -Implementation of higher per transaction limit for specific categories in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_No185_B_FY_2025_26_Addendum_to_OC_185_A_Implementation_of_higher_per_transaction_limit_for_specific_categories_in_UPI_ba517a0902.pdf

4. The per transaction limit for P2P shall continue as per the extant guidelines. Member, Apps and PSPs take note of the above enhancement, undertake requisite changes and ensure the compliance with the same by 15" September 2025. Yours Sincerely, SD/- Sourabh Tomar Head UPI Product 10014, The Capital, B Wing, 10" Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 O51- a T: +91 22 40009100 F: +91 22 40009101 Together ‘om contacti@npci.org.in www.npci.org.in WeBuild woe CIN: U74990MH2008NPL189067

### S6 — Addendum to OC 185 - Implementation of Rs 5 Lakh limit per transaction for specific categories in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_No_185_A_FY_24_25_Implementation_of_Rs_5_Lakh_limit_per_transaction_for_specific_categories_in_UPI_054c82bc8b.pdf

sae ersshr aprary Pere NATIONAL PAYMENTS CORPORATION OF INDIA NPCI/UPI/2024-25/0C/185A 24" August 2024 To All Members of UPI, Dear Madan/Sir, Subject: Addendum to OC 185 - Implementation of Rs 5 Lakh limit per transaction for specific categories in UPI With UPI emerging as a preferred payment method, there is a need to enhance the per transaction limit in UPI for specific categories. This proposed enhancement aligns with previous limit enhancements implemented through circulars such as NPCI/UPI/OC-127/2021- 2022 dated 9'" December 2021 and NPCI/UPI/OC-185/2023-2024 dated 19" December 2023. In view of the above, the per transaction value limit in UPI has now been enhanced to = 5 lakhs for entities under categories aligned to tax payments. This enhanced limit shall only be applicable to ‘Verified Merchants’, in the applicable category. To enable this enhancement:

### S7 — Addendum to OC 185A -Implementation of higher per transaction limit for specific categories in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_No185_B_FY_2025_26_Addendum_to_OC_185_A_Implementation_of_higher_per_transaction_limit_for_specific_categories_in_UPI_ba517a0902.pdf

1. The enhanced limits shall be applicable for merchants which are categorised as ‘Verified Merchant’.

### S8 — Circular 71 - Enhancement of per transaction limit to Rs 2.Lakhs for UPI based ASBA, page 1

https://www.npci.org.in/uploads/Circular_Enhancement_2_Lakhs_UPI_ASBA_7f656631f8.pdf

NPCI NATIONALPAYMENTSCORPORATIONOFINDIA NPCI/UP1/2019-20/OCNo.71 June21,2019 To, AllMembersofUPl Dear Sir/Madam, Subject:EnhancementofUPlpertransaction limittoRs.2lakhs forUPIbasedAsBA The second phase of the UPl option in IPO is going live with effect from July 1, 2019. It is now advised that all members and PsP banks live on UPl 2.0mandateblock functionality should maintain the per transaction limit of Rs. 2 lakhs for UPl based ASBA transactions with purpose Code01withMCC6211. Member banks and PsPs are advised to ensure necessary checks at their end and maintain transaction limits as directed above for both, mandate block (non-financial) and mandate The ScSB's registered with SEBl and PsP banks shall submit the necessary compliance to ipo.upi@npci.org.inonorbeforeJune30,2019. Yours faithfully, DilipAsbe ManagingDirector&CEO 1001A,The Capital,BWing,10Floor. BandraKurlaComplex,Bandra(E),Mumbai 400O51. T:+912240009100F:+912240009101www.npci.org.in CIN:U74990MH2008NPL189067

### S9 — Addendum to OC 185A -Implementation of higher per transaction limit for specific categories in UPI, page 2

https://www.npci.org.in/uploads/UPI_OC_No185_B_FY_2025_26_Addendum_to_OC_185_A_Implementation_of_higher_per_transaction_limit_for_specific_categories_in_UPI_ba517a0902.pdf

1. * Issuing banks are required to ensure that such cumulative limits are kept at their end. > Formatting note: the three Insurance MCC subrows and their merged cumulative-limit cell have been combined into one Markdown row without changing the values.

### S10 — Implementation of Rs 5 Lakh limit per transaction for specific categories in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_185_Implementation_of_Rs_5_Lakh_limit_per_transaction_for_specific_categories_in_UPI_65fd071f6c.pdf

HRT WERT Bras PRT NATIONAL PAYMENTS CORPORATION OF INDIA NPCI/UPI/OC-185/2023-24 19" December 2023 To, All Members of UPI Dear MadanVSir, Implementation of Rs 5 Lakh limit per transaction for specific categories in UPI With UPI emerging as a preferred payment method, there is a need to enhance the per transaction limit in UPI for specific categories, as per the RBI Statement on Developmental and Regulatory Policies, dated 8'" December 2023. In view of the above, the per transaction value limit in UP] has now been enhanced to = 5 lakhs for merchants under categories aligned to hospitals and educational services. This enhanced limit shall only be applicable to ‘Verified Merchants’. To enable this enhancement:

### S11 — Addendum to OC 185 - Implementation of Rs 5 Lakh limit per transaction for specific categories in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_No_185_A_FY_24_25_Implementation_of_Rs_5_Lakh_limit_per_transaction_for_specific_categories_in_UPI_054c82bc8b.pdf

2. Acquiring entities must ensure thai the classification of their merchants within ‘MCC- 9311’ strictly adheres to the tax payments only. They shall ensure that entities are added to the ‘Verified Merchant’ list after proper due diligence.

### S12 — Addendum to OC 185A -Implementation of higher per transaction limit for specific categories in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_No185_B_FY_2025_26_Addendum_to_OC_185_A_Implementation_of_higher_per_transaction_limit_for_specific_categories_in_UPI_ba517a0902.pdf

urcdte ease ara Perr NATIONAL PAYMENTS CORPORATION OF INDIA NPCI/UPI/2025-26/0C/185B 28" August 2025 To, All Members in UPI, Dear Madan/Sir, Subject: Addendum to OC 185 A — Implementation of higher per transaction limit for specific categories in UPI Vide reference to NPCI/UPI/2024-25/0C/185 A dated 24" August 2024, NPCI has increased the per transaction limits for entities under categories aligned to Tax Payments to ₹5 lakh. With UPI emerging as a preferred payment method, there are requirements from the market on extending higher per transaction limits for additional categories of transactions in UPI. In view of the above the per transaction limits for the mentioned categories in the Annexure I are enhanced accordingly along with additional guidelines:

### S13 — Enablement of UPI Mandate feature of Single Block Multiple Debits, page 2

https://www.npci.org.in/uploads/UPI_OC_No_200_FY_24_25_Enablement_of_UPI_Mandate_feature_of_Single_Block_Multiple_Debits_f2f9bc9230.pdf

c. The per transaction limit for such mandate creations shall be Rs 5 Lakh for the purpose code 76, while for purpose code 77 existing UPI limits shall be applicable.

### S14 — Addendum to OC 185A -Implementation of higher per transaction limit for specific categories in UPI, page 2

https://www.npci.org.in/uploads/UPI_OC_No185_B_FY_2025_26_Addendum_to_OC_185_A_Implementation_of_higher_per_transaction_limit_for_specific_categories_in_UPI_ba517a0902.pdf

UPI transaction); Purpose Code — 01 (For One Time Mandate) | ₹5 Lakh | ₹5 Lakh | | 10 | Digital Account Opening for Term Deposits | 7410 (New MCC) | ₹5 Lakh | ₹5 Lakh | | 11 | Digital Account Opening — Initial Funding | 7409 (New MCC) | ₹2 Lakh | ₹2 Lakh | **Notes**

### S15 — Compliance to Merchant Onboarding in UPI and Usage Limits, page 1

https://www.npci.org.in/uploads/NPCI_UPI_OC_181_Compliance_to_Merchant_Onboarding_in_UPI_and_Usage_Limits_90abfb97fa.pdf

b. ₹4.0 lakh cumulative credit limit The mentioned change is to be implemented by 10th December 2023.

### S16 — Enablement of UPI Mandate feature of Single Block Multiple Debits, page 2

https://www.npci.org.in/uploads/UPI_OC_No_200_FY_24_25_Enablement_of_UPI_Mandate_feature_of_Single_Block_Multiple_Debits_f2f9bc9230.pdf

d. It is re-iterated that issuer bank shall do all the necessary validation at the time of mandate creation. The execution of such mandates shall be considered success with the premise that mandate created successfully shall be executed successfully. With reference to NPCI/UPI/OC No. 88/2020-21 dated 14° May 2020 and further with NPCI/UPI/OC No.128/2021-22 dated 14 December 2021, NPCI has defined the scope of Deemed Debit and the same shall be extended to Single Block Multiple Debits mandates as well.

### S17 — Enablement of UPI Mandate feature of Single Block Multiple Debits, page 2

https://www.npci.org.in/uploads/UPI_OC_No_200_FY_24_25_Enablement_of_UPI_Mandate_feature_of_Single_Block_Multiple_Debits_f2f9bc9230.pdf

i. QR based ii, Intent iii. | SDK/Plug In The execution/debit of the mandate shall be as per the extant mode of mandates. Other mode of initiation shall be envisaged later.

### S18 — Compliance to Merchant Onboarding in UPI and Usage Limits, page 1

https://www.npci.org.in/uploads/NPCI_UPI_OC_181_Compliance_to_Merchant_Onboarding_in_UPI_and_Usage_Limits_90abfb97fa.pdf

2. As per the NPCI guidelines, MCC 7407 has been assigned for P2PM category of merchant. Acquirers shall populate the correct MCC in the ‘subCode’ field of the merchant tag in UPI, use to identify the nature of merchant business. Acquirers are required to make the necessary changes for the same by 15th February, 2024.

## Automated review limitations

{
  "coverage": {
    "status": "issues_flagged",
    "findings": [
      {
        "kind": "possible_conflict",
        "reason": "The answer cites S1 (OC 185B) as establishing a 'Cumulative Limits (24 hrs)' of ₹10 Lakh for Capital Market but explicitly states it does not set the per-mandate limit. However, S2 (OC 127) establishes a distinct 'per transaction value limit' of Rs 5 Lakh specifically for UPI based ASBA IPOs. The answer fails to reconcile whether the ₹10 Lakh cumulative figure in OC 185B supersedes, replaces, or coexists with the ₹5 Lakh per-transaction limit defined in OC 127 for the same category (IPO/MCC 6211). By treating them as separate without clarifying if the cumulative cap overrides the per-transaction cap for a single mandate, the answer leaves the specific limit for a single IPO mandate ambiguous.",
        "quotes": [
          {
            "citation": "S1",
            "quote": "### Annexure I 1. Below are the categories where higher limits are extended | Sr No | Categories | Merchant Category/Identifier | Enhanced Limits | Cumulative Limits (24 hrs) * | |---|---|---|---|---| | 1 | Capital Market | 6211 | ₹5 Lakh | ₹10 Lakh | | 2 | Insurance | 5960; 6300; 6529 | ₹5 Lakh for each listed MCC | ₹10 Lakh | | 3 | Government e-Market Place (EMD Payments) | 9311 | ₹5 Lakh | ₹10 Lakh | | 4 | Travel | 4722 | ₹5 Lakh | ₹10 Lakh | | 5 | Credit Card Bill Payments | 5413 | ₹5 Lakh | ₹6 Lakh | | 6 | Collections | 7322 | ₹5 Lakh | ₹10 Lakh | | 7 | Business/Merchant (Including Pre-Approved Payments) | Payer MCC shall not be 0000 and Purpose Code — 20 or 15 | ₹5 Lakh | NA | | 8 |"
          },
          {
            "citation": "S2",
            "quote": "NPCI NATIONALPAYMENTSCORPORATIONOFINDIA NPCI/UPI/OCNo.127/2021-22 gthDecember,2021 ToAllMember-UnifiedPaymentsInterface(UPl) DearMadam/Sir, Subject:lImplementationof Rs5Lakh limitpertransactionforSpecificCategories inUPl With UPl emerging as a preferred payment method, there is need to extend the per transaction limit in UPl which ispresentlyuptoRs2Lakhpertransactionforspecificusecases. In view of the above,theper transactionvalue limit inUPl has been now enhanced to Rs 5 lakh for Retail Direct SchemeandUPIbasedASBAIPO.Thedetailsareasbelow Foruse-case qualifying underthefollowing business categories; Category Identifier Purpose Code01 InitiaiPublicOffering(IPO) MCC - 6211 GSec throughRBl"
          }
        ]
      },
      {
        "kind": "scope_unclear",
        "reason": "The question asks about a 'single IPO mandate limit'. The evidence in S1 (OC 185B) defines a 'Cumulative Limits (24 hrs)' column alongside an 'Enhanced Limits' (per transaction) column. The answer asserts the ₹10 Lakh figure is cumulative and not per-mandate, but does not clarify if a single mandate can exceed the per-transaction limit (₹5 Lakh from S2) provided it stays within the 24-hour cumulative cap, or if the per-transaction limit strictly applies to every individual mandate regardless of the cumulative total. The distinction between a 'per transaction' measure and a 'cumulative' measure is present in the text but the answer does not explicitly define how they interact for a single mandate scenario.",
        "quotes": [
          {
            "citation": "S1",
            "quote": "### Annexure I 1. Below are the categories where higher limits are extended | Sr No | Categories | Merchant Category/Identifier | Enhanced Limits | Cumulative Limits (24 hrs) * | |---|---|---|---|---| | 1 | Capital Market | 6211 | ₹5 Lakh | ₹10 Lakh | | 2 | Insurance | 5960; 6300; 6529 | ₹5 Lakh for each listed MCC | ₹10 Lakh | | 3 | Government e-Market Place (EMD Payments) | 9311 | ₹5 Lakh | ₹10 Lakh | | 4 | Travel | 4722 | ₹5 Lakh | ₹10 Lakh | | 5 | Credit Card Bill Payments | 5413 | ₹5 Lakh | ₹6 Lakh | | 6 | Collections | 7322 | ₹5 Lakh | ₹10 Lakh | | 7 | Business/Merchant (Including Pre-Approved Payments) | Payer MCC shall not be 0000 and Purpose Code — 20 or 15 | ₹5 Lakh | NA | | 8 |"
          },
          {
            "citation": "S2",
            "quote": "NPCI NATIONALPAYMENTSCORPORATIONOFINDIA NPCI/UPI/OCNo.127/2021-22 gthDecember,2021 ToAllMember-UnifiedPaymentsInterface(UPl) DearMadam/Sir, Subject:lImplementationof Rs5Lakh limitpertransactionforSpecificCategories inUPl With UPl emerging as a preferred payment method, there is need to extend the per transaction limit in UPl which ispresentlyuptoRs2Lakhpertransactionforspecificusecases. In view of the above,theper transactionvalue limit inUPl has been now enhanced to Rs 5 lakh for Retail Direct SchemeandUPIbasedASBAIPO.Thedetailsareasbelow Foruse-case qualifying underthefollowing business categories; Category Identifier Purpose Code01 InitiaiPublicOffering(IPO) MCC - 6211 GSec throughRBl"
          }
        ]
      }
    ],
    "basis": "Automated same-model review of supplied evidence only; not exhaustive or independent verification."
  },
  "withheld": [
    {
      "text": "The cumulative limit in OC 185B is a separate measure from the per-mandate ceiling, and the document does not indicate that the single IPO mandate limit becomes 10 lakh.",
      "sources": [
        "S1",
        "S9"
      ],
      "draft_index": 3,
      "support_status": "uncertain",
      "review_reasons": [
        "The table amount is not tied to a matching category and limit type in the claim. Cite the correct row and retain its scope."
      ]
    }
  ],
  "warnings": [
    "Coverage is limited to the imported snapshot. Issue dates are not effective dates. OCR text may contain errors; verify figures and tables against the original.",
    "Graph-assisted retrieval: source-anchored proposed links; independent review is pending. Preserve each requirement's scope and effective date. A partial amendment does not replace the entire original circular. Current applicability beyond the indexed sources is unverified.",
    "Graph scope caution: Distinguish transaction limits from cumulative 24-hour limits and retain verified-merchant and bank-policy conditions.",
    "Graph scope caution: Prioritise the source specific to UPI ASBA IPO purpose01 and MCC6211 when explaining a mandate limit. A cumulative capital-market table value is a different measure and does not by itself change a per-mandate ceiling.",
    "Graph scope caution: The original OC71 extraction has an incomplete line; do not reconstruct missing execution conditions.",
    "Some evidence was omitted by the passage/character budget. Coverage is partial.",
    "Imported document metadata and extraction remain unverified; consult the original PDFs. Unknown issue dates are excluded when using an issue-date cutoff.",
    "Claims are automatically checked against cited excerpts. This is not independent expert verification. Uncertain or unsupported claims are withheld for review.",
    "1 of 3 draft claims were withheld. The remaining statements may not fully answer your question; inspect the sources and review details.",
    "Citation IDs are validated. Whether each citation supports its claim still requires review.",
    "The answer may omit a material qualification or contain an unresolved difference in scope. Inspect the evidence review below."
  ]
}