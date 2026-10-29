# What is UPI Lite? Answer briefly.

Status: Draft | Version: 1

Location: active

Local reviewer attribution is not authentication. Imported snapshots do not certify current applicability.

## Question

What is UPI Lite? Answer briefly.

## Documented findings

UPI Lite is an on\-device wallet functionality designed for small value digital payments that allows users to allocate funds from their bank account to a balance residing on the device within the UPI App. [S6] It enables transactions without requiring a UPI PIN, though app authentication \(biometric or pattern\) is recommended unless disabled by the user. [S5, S7] The system supports near offline debit and online credit initially, with plans for complete offline processing later. [S6] Funds allocated to UPI Lite reside in an escrow or designated account at the user's bank. [S6] The product offers advantages including superior user experience via faster near real\-time payments and reduced infrastructure requirements for banks. [S3, S14, S18] Users can enable UPI Lite on their UPI App to process small value transactions. [S6]

## Original research settings

{
  "query": "What is UPI Lite? Answer briefly.",
  "entity": "",
  "answer_style": "auto",
  "fiscal_year": "",
  "document_ids": [],
  "method": "hybrid",
  "series": "",
  "cutoff": "",
  "mode": "generate",
  "scope": "related",
  "feature": "",
  "route": "auto",
  "rerank": true
}

## Review history

[
  {
    "id": 4,
    "item_id": "3d04273ced4547f1a244d82f0627e59d",
    "version": 1,
    "at": "2026-10-28T15:49:23.841464+00:00",
    "action": "research_answer_saved",
    "reviewer": "",
    "note": "Question, retrieval settings, cited answer and source snapshot copied from completed local research job."
  }
]

## Snapshot

{
  "corpus": "d205ac78542f0e94d70f2beb68cd48b0ba242d1ef0024492c23bd32f67f889c8",
  "sources": {
    "2023-UPI-179": "08a4b8549e708c1872026d8f5ecb304dd24d5861831945fd7bbdd97eb91cfb54",
    "2024-OC-205": "dba64c37734c03dc0eb6b0ff457acdcb944e0a325505959edbb4d7fee944069b",
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

### S1 — Introduction of Auto Top-up on UPI LITE, page 1

https://www.npci.org.in/uploads/UPI_OC_No_205_FY_24_25_Introduction_of_Auto_Top_up_on_UPI_LITE_487fb97b95.pdf

1. Issuer banks live on UPI LITE shall support the functionality of Auto Top-up on UPI LITE wherein the banks should allow creation of UP! LITE mandate and allow debits whenever the request comes from the PSP/App.

### S2 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 3

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

2. Carry out reconciliation and settlement of UPI Lite transactions including the balance verification with respect to UPI Lite.

### S3 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 2

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

UPI Lite offers the following advantages to the UPI ecosystem:

### S4 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 3

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

1. Debit the User’s bank account on receipt of UPI Lite top-up request and manage the funds allocated by the User for UPI Lite.

### S5 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 2

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

2. The UPI Lite transactions shall be offered without AFA i.e. UPI PIN. However, it is recommended that the UPI App is accessed by the User with app passcode/device authentication (biometric, pattern, etc.) before performing the UPI Lite transaction, unless the User has disabled the app authentication.

### S6 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 1

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

volumes. As an efficient strategy to process large-scale small value digital payments and based on the guidelines issued by RBI for enabling mobile devices to support offline payments vide its circular no. CO.DPSS.POLC.No. S1264/ 02-14-003/2021-2022 titled “Framework for facilitating small value digital payments in offline mode” dated 3rd January 2022, NPCI has designed the “UPI Lite – On-Device wallet” (“UPI Lite”) functionality for UPI user (User). In phase 1, UPI Lite will process transactions in near offline mode i.e. debit offline and credit online, and at a later point, UPI Lite will process transactions in complete offline mode i.e. debit and credit both offline. A User of UPI App will have the option to enable UPI Lite i.e. “On-Device wallet” on her/his UPI App. Once enabled, the User can allocate funds from her/his bank account to UPI Lite. Such funds shall reside with the User’s bank in an escrow / pool / designated account and such balance shall reside on-device on the common library (CL) of the User’s UPI App. At present, only debit from UPI Lite balance shall be permitted and all credits to UPI Lite (including refunds, etc.) will be processed online in the User’s bank account maintained in the bank’s core banking system. The upper limit of an UPI Lite payment transaction shall be ₹200/-.The total limit

### S7 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 3

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

1. UPI Lite transactions will be processed without any UPI PIN. However, the app authentication shall be used before using the UPI lite, unless this feature has been disabled by the User

### S8 — Addendum to Introduction of UPI LITE, page 1

https://www.npci.org.in/uploads/UPI_OC_No_138_B_FY_2024_25_Addendum_to_Introduction_of_UPI_LITE_2c25ec3dfd.pdf

ard esta yar Peer NATIONAL PAYMENTS CORPORATION OF INDIA NPCIVUPI/OC No. 138 B/2024-25 215 February 2025 To, All UP] Members Dear Sir/Madam, Subject: Addendum to Introduction of UPI LITE With reference to the NPCI circular NPCI/UPI/OC No.138/2021-22, UPI LITE for small value transactions was introduced. To further enhance user convenience on UPI LITE, all Issuer Banks, PSP Banks, and UPI Apps live on UPI LITE are required to implement the following:

### S9 — UPI lite raw data file version 4.0, page 1

https://www.npci.org.in/uploads/UPI_OC_No_216_FY_2025_26_UPI_lite_raw_data_file_version_4_0_175ca4e4c9.pdf

2. Member banks that are still using lower versions (1.0 and 2.0) are advised to move to higher versions, preferably version 4.0 so that they are future ready for going live with UPI lite.

### S10 — Addendum to Enhancement in UPI LITE Limits, page 1

https://www.npci.org.in/uploads/UPI_OC_No_169_A_FY_202425_Addendum_to_Enhancement_in_UPI_LITE_Limits_270c24bcbc.pdf

1. As per the latest notification issued by RBI on 4th December 2024 vide circular no. RBI/2021-22/146 CO.DPSS.POLC.No.S1264/02-14-003/2021-2022 with subject ‘Framework for Facilitating Small Value Digital Payments in Offline Mode’, for UPI LITE, the enhanced limits shall be ₹1,000 per transaction with ₹5,000 being the total limit. Replenishment of used limit shall be allowed only in online mode with AFA. Customer will further have the option to set Auto Top-up for limit replenishment as per NPCI circular, ‘Introduction of Auto Top-up on UPI LITE’, vide No. NPCI/UPI/OC No. 205/2024-25, dated 27th August 2024. The details of the LITE limits are as below: | Description | UPI LITE — Existing | UPI LITE — New | UPI LITE X (Offline) — No Change | |---|---|---|---| | Per Transaction Limit | ₹500 | ₹1000 | ₹500 | | Total Limit at any point in time | ₹2000 | ₹5000 | ₹2000 | The new limits shall apply to and govern all existing NPCI circulars pertaining to UPI LITE limit (Annexure A). All the members are required to make the necessary changes pertaining to limit increase immediately.

### S11 — Introduction of Auto Top-up on UPI LITE, page 1

https://www.npci.org.in/uploads/UPI_OC_No_205_FY_24_25_Introduction_of_Auto_Top_up_on_UPI_LITE_487fb97b95.pdf

2. UPI Apps shall support the necessary functionality and interface on their App for the customer to use Auto Top-up on UPI LITE.

### S12 — Introduction of Auto Top-up on UPI LITE, page 1

https://www.npci.org.in/uploads/UPI_OC_No_205_FY_24_25_Introduction_of_Auto_Top_up_on_UPI_LITE_487fb97b95.pdf

LITE can be deleted anytime with instant refund of UPI LITE balance to user's main bank account, the requirement of pre-debit notification (PDN), which is a usual mechanism for merchant mandate payments, has been dispensed wiih. Members (Banks & PSP/App) are required to ensure below guidelines are followed

### S13 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 4

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

3. UPI Lite payments shall be covered under the provision of RBI’s limited customer liability circular (as amended from time to time) namely – DBR.No.Leg.BC.78/09.07.005/2107-18 dated July 06, 2017; DCBR.BPD.(PCB/RCB).Cir.No.06/12.05.001/2017-18 dated December 14, 2017 and para 17 of Master Direction on Prepaid Payment Instruments dated August 27, 2021.

### S14 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 2

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

1. Superior user experience using faster near real-time small value payments

### S15 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 1

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

UPI Lite (including refunds, etc.) will be processed online in the User’s bank account maintained in the bank’s core banking system. The upper limit of an UPI Lite payment transaction shall be ₹200/-.The total limit of UPI Lite balance for an “On-device wallet” shall be ₹2,000/- at any point of time. Replenishment of funds in UPI Lite shall only be allowed in online mode with additional factor authentication (AFA) or using UPI AutoPay which has been registered by the User in online mode with AFA.

### S16 — UPI OC 138 - Introduction of “On-Device wallet” – UPI Lite for Small Value Transactions, page 3

https://www.npci.org.in/uploads/UPI_OC_138_Introduction_of_On_Device_wallet_UPI_Lite_for_Small_Value_Transactions_a0930bbc3d.pdf

C. Responsibility of the Issuing Bank, in addition to specifics in the circular

### S17 — Addendum to Enhancement in UPI LITE Limits, page 1

https://www.npci.org.in/uploads/UPI_OC_No_169_A_FY_202425_Addendum_to_Enhancement_in_UPI_LITE_Limits_270c24bcbc.pdf

NPCI/UPI/OC No. 169 A/2024-25 — 27th February 2025 To, All UPI Members Dear Sir/Madam, **Subject: Addendum to Enhancement in UPI LITE Limits** With reference to the NPCI/UPI/OC No. 138/2021-22, dated 16th March 2022 and NPCI/UPI/OC No. 169/2023-24, dated 31st August 2023, UPI LITE was introduced and transaction limit was increased from ₹200 from ₹500 respectively. > Transcription note: the source itself uses “from ₹200 from ₹500”; that wording is retained.

### S18 — Customer awareness and engagement for UPI LITE Enablement and Top up, page 1

https://www.npci.org.in/uploads/UPI_OC_No_179_FY_23_24_Customer_awareness_and_engagement_for_UPI_LITE_Enablement_and_Top_up_ab742a2d5d.pdf

ardryr weer yrart Freep NATIONAL PAYMENTS CORPORATION OF INDIA NPCI/UPUOC No.179/2023-24 2"4 November 2023 To, All Members, Unified Paymenis Interface (UPI) Dear Madan/Sir, Subject: Customer awareness and engagement for UPI LITE Enablement and Top-up This is in reference to NPCI circular NPC] /UPI/OC No.138/2021-22, dated 16 March 2022 with subject ‘Introduction of “On-Device wallet’ — UPI LITE for Small Value Transactions’ and NPCI/UPI/OC No.169/2023-24, dated 31% August 2023 with subject ‘Enhancement in UPI LITE transaction limit to 500’, whereby guidelines to operationalize UP! LITE small value transactions have been introduced. The objective of introducing UPI LITE was to reduce the need for infrastructure scale up at bank end to cater the growing volumes of UPI small value transactions. UP] LITE is fast and seamless, as UPI PIN is not required to complete the transaction. In addition, UPI] LITE reduces the demand of availability of the issuer infrastructure for completing the transaction and hence provides better success rates. To grow UPI LITE and further enhance the customer experience, UPI Apps shall carry out the below actions:

## Automated review limitations

{
  "coverage": {
    "status": "issues_flagged",
    "findings": [
      {
        "kind": "possible_conflict",
        "reason": "The answer states that funds reside in an 'escrow or designated account' (S6), but S10.2 explicitly defines the new limits for UPI LITE X (Offline) as having a total limit of ₹2000, while the standard UPI LITE has a total limit of ₹5000. The answer does not distinguish between these two modes or explain how the 'escrow' applies to both, creating ambiguity about the applicable limits for different transaction types.",
        "quotes": [
          {
            "citation": "S6",
            "quote": " will have the option to enable UPI Lite i.e. “On-Device wallet” on her/his UPI App. Once enabled, the User can allocate funds from her/his bank account to UPI Lite. Such funds shall reside with the User’s bank in an escrow / pool / designated account and such balance shall reside on-device on the common library (CL) of the User’s UPI App. At present, only debit from UPI Lite balance shall be permitted and all credits to UPI Lite (including refunds, etc.) will be processed online in the User’s bank account maintained in the bank’s core banking system. The upper limit of an UPI Lite payment transaction shall be ₹200/-.The total limit"
          },
          {
            "citation": "S10",
            "quote": " UPI LITE — New | UPI LITE X (Offline) — No Change | |---|---|---|---| | Per Transaction Limit | ₹500 | ₹1000 | ₹500 | | Total Limit at any point in time | ₹2000 | ₹5000 | ₹2000 | The new limits shall apply to and govern all existing NPCI circulars pertaining to UPI LITE limit (Annexure A). All the members are required to make the necessary changes pertaining to limit increase immediately."
          }
        ]
      },
      {
        "kind": "possible_conflict",
        "reason": "The answer claims UPI Lite supports 'near offline debit and online credit initially', but S10.2 introduces a new category 'UPI LITE X (Offline)' where both debit and credit are offline, with no change to limits. The answer fails to mention this specific offline-credit mode or the distinction between standard UPI Lite and UPI LITE X, blurring the scope of what is currently supported versus future plans.",
        "quotes": [
          {
            "citation": "S6",
            "quote": " will have the option to enable UPI Lite i.e. “On-Device wallet” on her/his UPI App. Once enabled, the User can allocate funds from her/his bank account to UPI Lite. Such funds shall reside with the User’s bank in an escrow / pool / designated account and such balance shall reside on-device on the common library (CL) of the User’s UPI App. At present, only debit from UPI Lite balance shall be permitted and all credits to UPI Lite (including refunds, etc.) will be processed online in the User’s bank account maintained in the bank’s core banking system. The upper limit of an UPI Lite payment transaction shall be ₹200/-.The total limit"
          },
          {
            "citation": "S10",
            "quote": " UPI LITE — New | UPI LITE X (Offline) — No Change | |---|---|---|---| | Per Transaction Limit | ₹500 | ₹1000 | ₹500 | | Total Limit at any point in time | ₹2000 | ₹5000 | ₹2000 | The new limits shall apply to and govern all existing NPCI circulars pertaining to UPI LITE limit (Annexure A). All the members are required to make the necessary changes pertaining to limit increase immediately."
          }
        ]
      },
      {
        "kind": "possible_conflict",
        "reason": "The answer states that 'UPI PIN' is not required, which aligns with S5.1 and S7.1. However, S10.2 mentions that replenishment of used limit shall be allowed only in online mode with AFA (Additional Factor Authentication). The answer does not clarify if AFA replaces UPI PIN for top-ups or if UPI PIN is still required for initial setup, creating an unclear requirement for authentication methods.",
        "quotes": [
          {
            "citation": "S5",
            "quote": "2. The UPI Lite transactions shall be offered without AFA i.e. UPI PIN. However, it is recommended that the UPI App is accessed by the User with app passcode/device authentication (biometric, pattern, etc.) before performing the UPI Lite transaction, unless the User has disabled the app authentication."
          },
          {
            "citation": "S10",
            "quote": " UPI LITE — New | UPI LITE X (Offline) — No Change | |---|---|---|---| | Per Transaction Limit | ₹500 | ₹1000 | ₹500 | | Total Limit at any point in time | ₹2000 | ₹5000 | ₹2000 | The new limits shall apply to and govern all existing NPCI circulars pertaining to UPI LITE limit (Annexure A). All the members are required to make the necessary changes pertaining to limit increase immediately."
          }
        ]
      },
      {
        "kind": "scope_unclear",
        "reason": "The answer mentions 'plans for complete offline processing later' (S6), but S10.2 already describes a mode where both debit and credit are offline ('UPI LITE X (Offline)'). The answer does not clarify whether this is considered the 'complete offline processing' mentioned or if it is a separate feature, leading to confusion about the current state of development.",
        "quotes": [
          {
            "citation": "S6",
            "quote": " will have the option to enable UPI Lite i.e. “On-Device wallet” on her/his UPI App. Once enabled, the User can allocate funds from her/his bank account to UPI Lite. Such funds shall reside with the User’s bank in an escrow / pool / designated account and such balance shall reside on-device on the common library (CL) of the User’s UPI App. At present, only debit from UPI Lite balance shall be permitted and all credits to UPI Lite (including refunds, etc.) will be processed online in the User’s bank account maintained in the bank’s core banking system. The upper limit of an UPI Lite payment transaction shall be ₹200/-.The total limit"
          },
          {
            "citation": "S10",
            "quote": " UPI LITE — New | UPI LITE X (Offline) — No Change | |---|---|---|---| | Per Transaction Limit | ₹500 | ₹1000 | ₹500 | | Total Limit at any point in time | ₹2000 | ₹5000 | ₹2000 | The new limits shall apply to and govern all existing NPCI circulars pertaining to UPI LITE limit (Annexure A). All the members are required to make the necessary changes pertaining to limit increase immediately."
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