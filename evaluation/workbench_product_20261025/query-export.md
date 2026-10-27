# What is UPI Lite? Explain its purpose in simple terms.

Status: Needs review | Version: 3

Location: active

Local reviewer attribution is not authentication. Imported snapshots do not certify current applicability.

## Question

What is UPI Lite? Explain its purpose in simple terms.

## Documented findings

UPI Lite is an 'On-Device wallet' functionality designed for small value transactions that allows users to process payments in near offline or complete offline modes. [S5]

Its purpose is to reduce the load on core banking systems by enabling faster, highly reliable payments for transaction values below a specific limit without requiring real-time online verification for every debit. [S2, S7, S16]

Users can allocate funds from their bank account to the UPI Lite balance stored on their device, which resides in an escrow or designated account at the bank. [S5]

## Intended audience

Operations team — engineering walkthrough

## Review history

[
  {
    "id": 1,
    "item_id": "d28f0f9967094775bfb66034dabeeb62",
    "version": 1,
    "at": "2026-10-24T19:03:35.611679+00:00",
    "action": "created",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 2,
    "item_id": "d28f0f9967094775bfb66034dabeeb62",
    "version": 1,
    "at": "2026-10-24T19:03:40.336052+00:00",
    "action": "generation_started",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 3,
    "item_id": "d28f0f9967094775bfb66034dabeeb62",
    "version": 2,
    "at": "2026-10-24T19:03:44.455475+00:00",
    "action": "generated",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 4,
    "item_id": "d28f0f9967094775bfb66034dabeeb62",
    "version": 2,
    "at": "2026-10-24T19:04:51.510456+00:00",
    "action": "source_or_configuration_changed",
    "reviewer": "",
    "note": "Source corpus or model/graph configuration changed. Regenerate before approval."
  },
  {
    "id": 5,
    "item_id": "d28f0f9967094775bfb66034dabeeb62",
    "version": 2,
    "at": "2026-10-24T19:04:51.667925+00:00",
    "action": "generation_started",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 6,
    "item_id": "d28f0f9967094775bfb66034dabeeb62",
    "version": 3,
    "at": "2026-10-24T19:05:19.844740+00:00",
    "action": "generated",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 10,
    "item_id": "d28f0f9967094775bfb66034dabeeb62",
    "version": 3,
    "at": "2026-10-24T19:06:34.687405+00:00",
    "action": "submit",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 11,
    "item_id": "d28f0f9967094775bfb66034dabeeb62",
    "version": 3,
    "at": "2026-10-24T19:06:53.499363+00:00",
    "action": "archived",
    "reviewer": "",
    "note": "All versions and review history retained."
  },
  {
    "id": 12,
    "item_id": "d28f0f9967094775bfb66034dabeeb62",
    "version": 3,
    "at": "2026-10-24T19:06:53.592780+00:00",
    "action": "restored",
    "reviewer": "",
    "note": "All versions and review history retained."
  },
  {
    "id": 15,
    "item_id": "d28f0f9967094775bfb66034dabeeb62",
    "version": 3,
    "at": "2026-10-25T05:39:31.770542+00:00",
    "action": "trash",
    "reviewer": "",
    "note": "All versions and review history retained."
  },
  {
    "id": 16,
    "item_id": "d28f0f9967094775bfb66034dabeeb62",
    "version": 3,
    "at": "2026-10-25T05:39:31.866703+00:00",
    "action": "restored",
    "reviewer": "",
    "note": "All versions and review history retained."
  }
]

## Snapshot

{
  "corpus": "d205ac78542f0e94d70f2beb68cd48b0ba242d1ef0024492c23bd32f67f889c8",
  "sources": {
    "2023-UPI-169": "43e3891dc593a4b990b97becff930fc412bceef6be7332e3faf694fc0fc17c04",
    "2023-UPI-179": "08a4b8549e708c1872026d8f5ecb304dd24d5861831945fd7bbdd97eb91cfb54",
    "2025-OC-138B": "7fda76dddc1e09d2dc18c9473207ce23293ceeaad9a23bd293bb9b0b6f7cb658",
    "2025-OC-169A": "9cff6449b86b0900a97a9ad031dac782fb4365ced7772b3604465d77e01c36d6",
    "2025-OC-216": "5e562b47e003695d8ca89639533167f5e7da6cdf86aecd43f47195067dff971b",
    "npci-source-5a8de8043d311df7f2560420": "1ff3b1568996c6e62fb1e395275f936534267d229dbcea149475c8f9658e4033"
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

### S1 — Addendum to Introduction of UPI LITE, page 1

https://www.npci.org.in/uploads/UPI_OC_No_138_B_FY_2024_25_Addendum_to_Introduction_of_UPI_LITE_2c25ec3dfd.pdf

1. All members shall implement ‘Transfer Out’ functionality. It allows users to withdraw funds from their UPI LITE balance to the source bank account from which it was loaded, without disabling UPI LITE. Purpose Code 46 shail be used to identify ‘Transfer Out’ transactions.

### S2 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 2

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

UPI Lite offers the following advantages to the UPI ecosystem:

### S3 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 3

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

2. Carry out reconciliation and settlement of UPI Lite transactions including the balance verification with respect to UPI Lite.

### S4 — Customer awareness and engagement for UPI LITE Enablement and Top up, page 1

https://www.npci.org.in/uploads/UPI_OC_No_179_FY_23_24_Customer_awareness_and_engagement_for_UPI_LITE_Enablement_and_Top_up_ab742a2d5d.pdf

3) Post UPI LITE enablement, UPI LITE shall be the default instrument for transactions value below 500.

### S5 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 1

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

volumes. As an efficient strategy to process large-scale small value digital payments and based on the guidelines issued by RBI for enabling mobile devices to support offline payments vide its circular no. CO.DPSS.POLC.No. S1264/ 02-14-003/2021-2022 titled “Framework for facilitating small value digital payments in offline mode” dated 3rd January 2022, NPCI has designed the “UPI Lite – On-Device wallet” (“UPI Lite”) functionality for UPI user (User). In phase 1, UPI Lite will process transactions in near offline mode i.e. debit offline and credit online, and at a later point, UPI Lite will process transactions in complete offline mode i.e. debit and credit both offline. A User of UPI App will have the option to enable UPI Lite i.e. “On-Device wallet” on her/his UPI App. Once enabled, the User can allocate funds from her/his bank account to UPI Lite. Such funds shall reside with the User’s bank in an escrow / pool / designated account and such balance shall reside on-device on the common library (CL) of the User’s UPI App. At present, only debit from UPI Lite balance shall be permitted and all credits to UPI Lite (including refunds, etc.) will be processed online in the User’s bank account maintained in the bank’s core banking system. The upper limit of an UPI Lite payment transaction shall be ₹200/-.The total limit

### S6 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 2

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

9. The issuing bank shall also facilitate the handling of customer grievances after the transaction information with respect to UPI Lite transactions is made available to these banks.

### S7 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 2

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

3. Reduction of load on core banking system of the member bank. User experience on UPI Lite:

### S8 — UPI lite raw data file version 4.0, page 1

https://www.npci.org.in/uploads/UPI_OC_No_216_FY_2025_26_UPI_lite_raw_data_file_version_4_0_175ca4e4c9.pdf

2. Member banks that are still using lower versions (1.0 and 2.0) are advised to move to higher versions, preferably version 4.0 so that they are future ready for going live with UPI lite.

### S9 — Addendum to Introduction of UPI LITE, page 1

https://www.npci.org.in/uploads/UPI_OC_No_138_B_FY_2024_25_Addendum_to_Introduction_of_UPI_LITE_2c25ec3dfd.pdf

2. All the Issuer Banks five on UPI LITE shall maintain LRN (Lite Reference Number) level balances and ensure that reconciliation is carried out on daily basis with NPCI data so that LRN balances are reconciled in sync with NPC] data on an ongoing basis.

### S10 — Addendum to Introduction of UPI LITE, page 1

https://www.npci.org.in/uploads/UPI_OC_No_138_B_FY_2024_25_Addendum_to_Introduction_of_UPI_LITE_2c25ec3dfd.pdf

ard esta yar Peer NATIONAL PAYMENTS CORPORATION OF INDIA NPCIVUPI/OC No. 138 B/2024-25 215 February 2025 To, All UP] Members Dear Sir/Madam, Subject: Addendum to Introduction of UPI LITE With reference to the NPCI circular NPCI/UPI/OC No.138/2021-22, UPI LITE for small value transactions was introduced. To further enhance user convenience on UPI LITE, all Issuer Banks, PSP Banks, and UPI Apps live on UPI LITE are required to implement the following:

### S11 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 2

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

1. Superior user experience using faster near real-time small value payments

### S12 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 1

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

UPI Lite (including refunds, etc.) will be processed online in the User’s bank account maintained in the bank’s core banking system. The upper limit of an UPI Lite payment transaction shall be ₹200/-.The total limit of UPI Lite balance for an “On-device wallet” shall be ₹2,000/- at any point of time. Replenishment of funds in UPI Lite shall only be allowed in online mode with additional factor authentication (AFA) or using UPI AutoPay which has been registered by the User in online mode with AFA.

### S13 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 4

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

3. UPI Lite payments shall be covered under the provision of RBI’s limited customer liability circular (as amended from time to time) namely – DBR.No.Leg.BC.78/09.07.005/2107-18 dated July 06, 2017; DCBR.BPD.(PCB/RCB).Cir.No.06/12.05.001/2017-18 dated December 14, 2017 and para 17 of Master Direction on Prepaid Payment Instruments dated August 27, 2021.

### S14 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 3

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

1. Debit the User’s bank account on receipt of UPI Lite top-up request and manage the funds allocated by the User for UPI Lite.

### S15 — Addendum to Enhancement in UPI LITE Limits, page 1

https://www.npci.org.in/uploads/UPI_OC_No_169_A_FY_202425_Addendum_to_Enhancement_in_UPI_LITE_Limits_270c24bcbc.pdf

NPCI/UPI/OC No. 169 A/2024-25 — 27th February 2025 To, All UPI Members Dear Sir/Madam, **Subject: Addendum to Enhancement in UPI LITE Limits** With reference to the NPCI/UPI/OC No. 138/2021-22, dated 16th March 2022 and NPCI/UPI/OC No. 169/2023-24, dated 31st August 2023, UPI LITE was introduced and transaction limit was increased from ₹200 from ₹500 respectively. > Transcription note: the source itself uses “from ₹200 from ₹500”; that wording is retained.

### S16 — Enhancement in UPI LITE transaction limit to ₹500, page 1

https://www.npci.org.in/uploads/UPI_OC_169_Enhancement_in_UPI_LITE_transaction_limit_to_Rs_500_0188d612d9.pdf

NPCI/UPI/OC No. 169/2023-24 31st August 2023 To All Member-Unified Payments Interface (UPI) Dear Madam/Sir, **Subject: Enhancement in UPI LITE transaction limit to ₹500** UPI LITE has been designed to play a vital role in reducing infrastructure load on the Core Banking System of the banks. This feature has been making the small value transactions faster and highly reliable for transaction value below ₹200. As per the latest circular issued by RBI on 24th August, 2023 vide Circular No: RBI/2023-24/57 CO.DPSS.POLC.No.S526/02-14-003/2023-24 with subject ‘Enhancing transaction limits for Small Value Digital Payments in Offline Mode’, the upper limit of an offline payment transaction is now increased from ₹200 to ₹500. In view of the above, the per transaction value limit for UPI LITE (Purpose code 44 - Online and 45 - Offline) has now been enhanced to ₹500. The details are as below: | UPI LITE Limit | Previous Limit | New Limit | |---|---|---| | Per Transaction | ₹200 | ₹500 | | Max balance in UPI lite account | ₹2000 | ₹2000 (No change) | The existing UPI pricing shall be applicable for transaction amount ₹201-₹500 for both P2P and P2M transactions. With reference to the above, Member Banks (Payee PSP), Third Party App providers (TPAPs), Merchants and other payment providers are requested to take note of the above enhancement

### S17 — Customer awareness and engagement for UPI LITE Enablement and Top up, page 1

https://www.npci.org.in/uploads/UPI_OC_No_179_FY_23_24_Customer_awareness_and_engagement_for_UPI_LITE_Enablement_and_Top_up_ab742a2d5d.pdf

2) For new UPI customer onboarding, UPI apps shall define journey for enabling UPI LITE also during UPI onboarding with consent from the user.

### S18 — Customer awareness and engagement for UPI LITE Enablement and Top up, page 1

https://www.npci.org.in/uploads/UPI_OC_No_179_FY_23_24_Customer_awareness_and_engagement_for_UPI_LITE_Enablement_and_Top_up_ab742a2d5d.pdf

4) Top-up notifications/ pop-up with call to action shall be given to the customer, if UPI LITE balance goes below 200. Pop-up/ notifications shall be given in below ways:

## Automated review limitations

{
  "coverage": {
    "status": "issues_flagged",
    "findings": [
      {
        "kind": "possible_conflict",
        "reason": "The answer states that UPI Lite allows processing payments in 'near offline or complete offline modes' (S5). However, excerpt S16.2 explicitly states that for transaction amounts between ₹201 and ₹500 (the enhanced limit), the pricing applies to 'both P2P and P2M transactions' but does not specify if these specific higher-value transactions within the new limit can be processed in 'complete offline mode'. The answer implies complete offline capability is a general feature, while S16.2 introduces a tiered limit structure that might restrict complete offline usage to amounts ≤₹200 or require online verification for amounts >₹200, creating an incompatibility between the general claim of 'complete offline' and the specific rules for the enhanced ₹500 limit.",
        "quotes": [
          {
            "citation": "S5",
            "quote": "volumes. As an efficient strategy to process large-scale small value digital payments and based on the guidelines issued by RBI for enabling mobile devices to support offline payments vide its circular no. CO.DPSS.POLC.No. S1264/ 02-14-003/2021-2022 titled “Framework for facilitating small value digital payments in offline mode” dated 3rd January 2022, NPCI has designed the “UPI Lite – On-Device wallet” (“UPI Lite”) functionality for UPI user (User). In phase 1, UPI Lite will process transactions in near offline mode i.e. debit offline and credit online, and at a later point, UPI Lite will process transactions in complete offline mode i.e. debit and credit both offline. A User of UPI App"
          },
          {
            "citation": "S16",
            "quote": " increased from ₹200 to ₹500. In view of the above, the per transaction value limit for UPI LITE (Purpose code 44 - Online and 45 - Offline) has now been enhanced to ₹500. The details are as below: | UPI LITE Limit | Previous Limit | New Limit | |---|---|---| | Per Transaction | ₹200 | ₹500 | | Max balance in UPI lite account | ₹2000 | ₹2000 (No change) | The existing UPI pricing shall be applicable for transaction amount ₹201-₹500 for both P2P and P2M transactions. With reference to the above, Member Banks (Payee PSP), Third Party App providers (TPAPs), Merchants and other payment providers are requested to take note of the above enhancement"
          }
        ]
      },
      {
        "kind": "scope_unclear",
        "reason": "The answer claims UPI Lite is designed to 'reduce the load on core banking systems' (S7, S16). While S16 supports this for small value transactions generally, S4 and S15 specify that after enablement, UPI Lite becomes the 'default instrument for transactions value below 500'. It is unclear if the answer's general statement about reducing load applies to *all* small value transactions or only those processed via the offline mechanism, as the default status might imply a broader scope than just the offline capability.",
        "quotes": [
          {
            "citation": "S4",
            "quote": "3) Post UPI LITE enablement, UPI LITE shall be the default instrument for transactions value below 500."
          },
          {
            "citation": "S7",
            "quote": "3. Reduction of load on core banking system of the member bank. User experience on UPI Lite:"
          },
          {
            "citation": "S16",
            "quote": " increased from ₹200 to ₹500. In view of the above, the per transaction value limit for UPI LITE (Purpose code 44 - Online and 45 - Offline) has now been enhanced to ₹500. The details are as below: | UPI LITE Limit | Previous Limit | New Limit | |---|---|---| | Per Transaction | ₹200 | ₹500 | | Max balance in UPI lite account | ₹2000 | ₹2000 (No change) | The existing UPI pricing shall be applicable for transaction amount ₹201-₹500 for both P2P and P2M transactions. With reference to the above, Member Banks (Payee PSP), Third Party App providers (TPAPs), Merchants and other payment providers are requested to take note of the above enhancement"
          }
        ]
      },
      {
        "kind": "possible_conflict",
        "reason": "The answer states users can 'allocate funds from their bank account to the UPI Lite balance' (S5). Excerpt S12 clarifies that replenishment is allowed only in 'online mode with additional factor authentication (AFA) or using UPI AutoPay'. The answer's phrasing 'allocate funds... without requiring real-time online verification for every debit' (inferred from the second point about purpose) might be misinterpreted as allowing offline allocation, whereas S12 explicitly restricts replenishment to online mode with AFA.",
        "quotes": [
          {
            "citation": "S5",
            "quote": " will have the option to enable UPI Lite i.e. “On-Device wallet” on her/his UPI App. Once enabled, the User can allocate funds from her/his bank account to UPI Lite. Such funds shall reside with the User’s bank in an escrow / pool / designated account and such balance shall reside on-device on the common library (CL) of the User’s UPI App. At present, only debit from UPI Lite balance shall be permitted and all credits to UPI Lite (including refunds, etc.) will be processed online in the User’s bank account maintained in the bank’s core banking system. The upper limit of an UPI Lite payment transaction shall be ₹200/-.The total limit"
          },
          {
            "citation": "S12",
            "quote": "UPI Lite (including refunds, etc.) will be processed online in the User’s bank account maintained in the bank’s core banking system. The upper limit of an UPI Lite payment transaction shall be ₹200/-.The total limit of UPI Lite balance for an “On-device wallet” shall be ₹2,000/- at any point of time. Replenishment of funds in UPI Lite shall only be allowed in online mode with additional factor authentication (AFA) or using UPI AutoPay which has been registered by the User in online mode with AFA."
          }
        ]
      },
      {
        "kind": "possible_conflict",
        "reason": "The answer mentions UPI Lite is an 'On-Device wallet' (S5). Excerpt S9 requires banks to maintain 'LRN (Lite Reference Number) level balances' and reconcile with NPCI data daily. The answer does not mention this specific reconciliation requirement or the LRN balance concept, which might be a necessary operational detail for the 'wallet' functionality that is omitted.",
        "quotes": [
          {
            "citation": "S5",
            "quote": "volumes. As an efficient strategy to process large-scale small value digital payments and based on the guidelines issued by RBI for enabling mobile devices to support offline payments vide its circular no. CO.DPSS.POLC.No. S1264/ 02-14-003/2021-2022 titled “Framework for facilitating small value digital payments in offline mode” dated 3rd January 2022, NPCI has designed the “UPI Lite – On-Device wallet” (“UPI Lite”) functionality for UPI user (User). In phase 1, UPI Lite will process transactions in near offline mode i.e. debit offline and credit online, and at a later point, UPI Lite will process transactions in complete offline mode i.e. debit and credit both offline. A User of UPI App"
          },
          {
            "citation": "S9",
            "quote": "2. All the Issuer Banks five on UPI LITE shall maintain LRN (Lite Reference Number) level balances and ensure that reconciliation is carried out on daily basis with NPCI data so that LRN balances are reconciled in sync with NPC] data on an ongoing basis."
          }
        ]
      }
    ],
    "basis": "Automated same-model review of supplied evidence only; not exhaustive or independent verification."
  },
  "withheld": [],
  "warnings": [
    "Coverage is limited to the imported snapshot. Issue dates are not effective dates. OCR text may contain errors; verify figures and tables against the original.",
    "Some evidence was omitted by the passage/character budget. Coverage is partial.",
    "Imported document metadata and extraction remain unverified; consult the original PDFs. Unknown issue dates are excluded when using an issue-date cutoff.",
    "Requested aspects not located by passage heuristics: Definitions. The answer may be partial.",
    "Claims are automatically checked against cited excerpts. This is not independent expert verification. Uncertain or unsupported claims are withheld for review.",
    "Citation IDs are validated. Whether each citation supports its claim still requires review.",
    "The answer may omit a material qualification or contain an unresolved difference in scope. Inspect the evidence review below."
  ]
}