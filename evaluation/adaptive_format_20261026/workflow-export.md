# Formatting replay: Compare the purposes of UPI Lite and UPI Tap & Pay in a two-column table. Keep each cell self-contained and the answer br

Status: Draft | Version: 2

Location: active

Local reviewer attribution is not authentication. Imported snapshots do not certify current applicability.

## Question

Formatting replay: Compare the purposes of UPI Lite and UPI Tap & Pay in a two-column table. Keep each cell self-contained and the answer brief.

## Documented findings

| Evidence 1 | Evidence 2 |
| --- | --- |
| UPI Lite is designed to process small transactions of Rs. 500 or less without a UPI PIN, provided the user has enabled the feature and the app includes passcode, biometrics, or pattern locks. [S1] | UPI Tap & Pay enables contactless NFC\-based payments by tapping an unlocked mobile device on a PoS terminal or QR tag, extending beyond QR scanning to include Point of Sale terminals. [S8] |

## Review history

[
  {
    "id": 1,
    "item_id": "e2b2c12e7e7041c4b34aa3902d2710ae",
    "version": 1,
    "at": "2026-10-26T16:20:09.525141+00:00",
    "action": "created",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 2,
    "item_id": "e2b2c12e7e7041c4b34aa3902d2710ae",
    "version": 1,
    "at": "2026-10-26T16:20:09.527144+00:00",
    "action": "generation_started",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 3,
    "item_id": "e2b2c12e7e7041c4b34aa3902d2710ae",
    "version": 2,
    "at": "2026-10-26T16:20:09.545810+00:00",
    "action": "generated",
    "reviewer": "",
    "note": ""
  }
]

## Snapshot

{
  "corpus": "d205ac78542f0e94d70f2beb68cd48b0ba242d1ef0024492c23bd32f67f889c8",
  "sources": {
    "2023-UPI-186": "cf213dd043b4b3bc1a96bd6f2ce799198abe14fa1dc484c0f3d807ed9eddb6d9",
    "2025-OC-169A": "9cff6449b86b0900a97a9ad031dac782fb4365ced7772b3604465d77e01c36d6",
    "2025-OC-225": "a4099192751180239f1fa33b48cb7b7433e54b8b9c4f0ba05e3d0180ba477d6a",
    "2026-OC-186A": "cb3512ac64d06e871f0bbf4e86c69ae9396d1025f346e4edf3dbeb99a7da77da"
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

### S1 — Introduction of UPI TAP & PAY mode of Payments, page 1

https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf

4. On Tap, the transaction amount of Rs.500 and less will be processed through UP! LITE account, if enabled by the user, if not, then the transaction shall be processed with UPI PIN. UPI APPs are recommended to have the App passcode, biometrics or pattern based lock in case of UPI LITE.

### S2 — Enhancement - UPI Tap & Pay on Point of Sale (PoS), page 2

https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf

UPI Application Provider 1. UP! Application Providers / PSP Banks shall ensure explicit User consent is obtained after each device binding operation before allowing further transactions using UPI! Tap & Pay.

### S3 — Addendum to Enhancement in UPI LITE Limits, page 2

https://www.npci.org.in/uploads/UPI_OC_No_169_A_FY_202425_Addendum_to_Enhancement_in_UPI_LITE_Limits_270c24bcbc.pdf

4. NPCI circular, ‘introduction of UP! TAP & PAY mode of Payments’ vide No. NPCI/UPI/OC No.186/2023-24, dated 19"" December 2023

### S4 — Introduction of UPI TAP & PAY mode of Payments, page 1

https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf

NZE) NATIONAL PAYMENTS CORPORATION OF INDIA NPCI/UPI/OC No.186/2023-24 19th December 2023 To, All Members, Unified Payments Interface (UPI) Dear Sir/Madam, Subject: Introduction of UP] TAP & PAY mode of payments In addition to the existing modes (Scan & Pay, Pay to Contact, UPI Number, etc.) of UPI Payments, “UPI Tap & Pay” is the new mode introduced for UP] transactions. Following is the construct for UPI Tap & Pay transactions:

### S5 — Enhancement - UPI Tap & Pay on Point of Sale (PoS), page 2

https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf

2. UPI Application Providers shall ensure that device lock is enabled as a prerequisite for activating UP! Tap & Pay. Further, the device shall be in an unlocked state at the time of initiating a UP! Tap & Pay transaction.

### S6 — Introduction of UPI TAP & PAY mode of Payments, page 2

https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf

11. UPI QR specifications shall be embedded inside the UP! Smart Tag (NFC Tag), or in the paper-based UP] Smart QR (NFC QR). The details of the same are part of UPI Tap & Pay product kit. 12, Transactions performed using UPI Tap & Pay mode of payment will follow the existing dispute management process. With reference to the above, UPI Member are requested to take note and Go-live on mentioned functionality by 31st January’ 2024. Yours Sincerely, SD/- Kunal Kalawatia Chief of Products

### S7 — Enhancement - UPI Tap & Pay on Point of Sale (PoS), page 2

https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf

3. UPI Application Providers shall ensure that UP! Tap & Pay is made available through a dedicated call-to- action. The functionality shall be presented as a standalone feature and shall not be embedded within any other service, feature, or menu category.

### S8 — Enhancement - UPI Tap & Pay on Point of Sale (PoS), page 1

https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf

serena a Oe Prt | FORWPRD NPCI/UPI/OC-186A/2026-27 10" September 2026 To, Members and UPI Application Providers — Unified Payments Interface (UPI) Subject: Enhancement - UPI Tap & Pay on Point of Sale (PoS) With reference to UPI Operating Circular NPCI/UPI/OC-186/2023-24 dated 19° December 2023, UPI Tap & Pay through Near Field Communication (NFC) on QR was introduced as an additional mode for initiating UPI transactions. In addition to QR, UPI Tap & Pay shall now be extended to Point of Sale (PoS) terminals enabling Users to make contactless (NFC-based) UPI! payments by unlocking their mobile device and tapping it on the PoS terminal.

### S9 — Introduction of UPI TAP & PAY mode of Payments, page 1

https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf

5. On Tap, the transaction amount more than Rs.500 will need UP! PIN and will be processed online.

### S10 — Introduction of UPI TAP & PAY mode of Payments, page 1

https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf

3. UPI Apps shall provide separate call to action button for Tap & Pay mode on the homepage.

### S11 — Addendum to Enhancement in UPI LITE Limits, page 2

https://www.npci.org.in/uploads/UPI_OC_No_169_A_FY_202425_Addendum_to_Enhancement_in_UPI_LITE_Limits_270c24bcbc.pdf

5. NPCI circular, ‘Introduction of Auto Top-up on UPI LITE’ vide No. NPCI/UPI/OC No.205/2024-25, dated 27" August 2024

### S12 — Addendum to Enhancement in UPI LITE Limits, page 2

https://www.npci.org.in/uploads/UPI_OC_No_169_A_FY_202425_Addendum_to_Enhancement_in_UPI_LITE_Limits_270c24bcbc.pdf

3. NPC circular, ‘Customer awareness and engagement for UPI LITE Enablement and Top-up’ vide No. NPCI/UPI/OC No.179/2023-24, dated 02"* November 2023

### S13 — Introduction of UPI TAP & PAY mode of Payments, page 1

https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf

1. UPI APPs shall ensure to provide the Tap & Pay mode of payment only through mobiles devices having NFC capability.

### S14 — Introduction of UPI TAP & PAY mode of Payments, page 2

https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf

10. Acquiring banks shall ensure to procure the NFC Tags from NPC! empanelied vendors as communicated via circular no. NPCI/2020-21/NETC/002 and NPCI/2022- 23/RuPay/013 and updated from time to time.

### S15 — Enabling Cash Withdrawal through MicroATM using UPI at Business Correspondent (BC) touch points, page 1

https://www.npci.org.in/uploads/UPI_OC_No_225_FY_2025_26_Enabling_Cash_Withdrawal_through_Micro_ATM_using_UPI_at_Business_Correspondent_touch_points_829f5cf0d0.pdf

3. Per transaction, per day limit and monthly limit for such transaction shall be 25,000, 710,000 and %50,000 , respectively. Each transaction shall have mandatory Two Factor Authentication (2FA) allowed in UPI. (UPI LITE accounts shall not be permitted). Account which in nature of credit shall not be allowed to for suich transactions. /

## Automated review limitations

{
  "coverage": {
    "status": "issues_flagged",
    "findings": [
      {
        "kind": "possible_conflict",
        "reason": "The answer states UPI Lite processes transactions 'without a UPI PIN' (S1), but evidence S9.1 explicitly states that transactions over Rs.500 'will need UP! PIN'. The answer's definition of UPI Lite as processing 'Rs. 500 or less' aligns with S1.1, which confirms the limit and PIN exemption for amounts <= Rs.500, but the answer does not clarify that amounts exceeding this limit require a PIN, potentially creating an incomplete picture if interpreted broadly.",
        "quotes": [
          {
            "citation": "S1",
            "quote": "4. On Tap, the transaction amount of Rs.500 and less will be processed through UP! LITE account, if enabled by the user, if not, then the transaction shall be processed with UPI PIN. UPI APPs are recommended to have the App passcode, biometrics or pattern based lock in case of UPI LITE."
          },
          {
            "citation": "S9",
            "quote": "5. On Tap, the transaction amount more than Rs.500 will need UP! PIN and will be processed online."
          }
        ]
      },
      {
        "kind": "scope_unclear",
        "reason": "The answer describes UPI Tap & Pay as enabling payments by 'tapping an unlocked mobile device on a PoS terminal or QR tag' (S8). However, evidence S5.1 and S7.1 specify that the device must be in an 'unlocked state at the time of initiating' a transaction and that device lock is a prerequisite for activation. The answer's phrasing 'tapping an unlocked mobile device' might imply the user unlocks it during the tap, whereas the evidence suggests the device must already be unlocked as a condition for the feature to function, which is a subtle but relevant distinction in scope.",
        "quotes": [
          {
            "citation": "S8",
            "quote": "serena a Oe Prt | FORWPRD NPCI/UPI/OC-186A/2026-27 10\" September 2026 To, Members and UPI Application Providers — Unified Payments Interface (UPI) Subject: Enhancement - UPI Tap & Pay on Point of Sale (PoS) With reference to UPI Operating Circular NPCI/UPI/OC-186/2023-24 dated 19° December 2023, UPI Tap & Pay through Near Field Communication (NFC) on QR was introduced as an additional mode for initiating UPI transactions. In addition to QR, UPI Tap & Pay shall now be extended to Point of Sale (PoS) terminals enabling Users to make contactless (NFC-based) UPI! payments by unlocking their mobile device and tapping it on the PoS terminal."
          },
          {
            "citation": "S5",
            "quote": "2. UPI Application Providers shall ensure that device lock is enabled as a prerequisite for activating UP! Tap & Pay. Further, the device shall be in an unlocked state at the time of initiating a UP! Tap & Pay transaction."
          }
        ]
      },
      {
        "kind": "possible_conflict",
        "reason": "The answer claims UPI Tap & Pay extends 'beyond QR scanning to include Point of Sale terminals' (S8). Evidence S4.1 introduces UPI Tap & Pay as a new mode for UPI transactions in addition to existing modes like Scan & Pay. While not a direct conflict, the answer's focus on NFC/PoS might obscure the fact that Tap & Pay was initially introduced alongside QR scanning capabilities (as per S8.1 mentioning 'NFC on QR'), and the answer does not explicitly mention the QR component's role in the initial introduction, which could be seen as an omission of scope.",
        "quotes": [
          {
            "citation": "S8",
            "quote": "serena a Oe Prt | FORWPRD NPCI/UPI/OC-186A/2026-27 10\" September 2026 To, Members and UPI Application Providers — Unified Payments Interface (UPI) Subject: Enhancement - UPI Tap & Pay on Point of Sale (PoS) With reference to UPI Operating Circular NPCI/UPI/OC-186/2023-24 dated 19° December 2023, UPI Tap & Pay through Near Field Communication (NFC) on QR was introduced as an additional mode for initiating UPI transactions. In addition to QR, UPI Tap & Pay shall now be extended to Point of Sale (PoS) terminals enabling Users to make contactless (NFC-based) UPI! payments by unlocking their mobile device and tapping it on the PoS terminal."
          },
          {
            "citation": "S4",
            "quote": "NZE) NATIONAL PAYMENTS CORPORATION OF INDIA NPCI/UPI/OC No.186/2023-24 19th December 2023 To, All Members, Unified Payments Interface (UPI) Dear Sir/Madam, Subject: Introduction of UP] TAP & PAY mode of payments In addition to the existing modes (Scan & Pay, Pay to Contact, UPI Number, etc.) of UPI Payments, “UPI Tap & Pay” is the new mode introduced for UP] transactions. Following is the construct for UPI Tap & Pay transactions:"
          }
        ]
      },
      {
        "kind": "scope_unclear",
        "reason": "The answer states UPI Lite requires the app to have 'passcode, biometrics, or pattern locks' (S1). Evidence S5.1 and S7.1 specify similar lock requirements for UPI Tap & Pay activation. However, the answer does not clarify whether these lock requirements are identical in nature or if there are any differences between the two modes regarding authentication mechanisms beyond the PIN exemption for UPI Lite.",
        "quotes": [
          {
            "citation": "S1",
            "quote": "4. On Tap, the transaction amount of Rs.500 and less will be processed through UP! LITE account, if enabled by the user, if not, then the transaction shall be processed with UPI PIN. UPI APPs are recommended to have the App passcode, biometrics or pattern based lock in case of UPI LITE."
          },
          {
            "citation": "S5",
            "quote": "2. UPI Application Providers shall ensure that device lock is enabled as a prerequisite for activating UP! Tap & Pay. Further, the device shall be in an unlocked state at the time of initiating a UP! Tap & Pay transaction."
          }
        ]
      }
    ],
    "basis": "Automated same-model review of supplied evidence only; not exhaustive or independent verification."
  },
  "withheld": [],
  "warnings": [
    "Coverage is limited to the imported snapshot. Issue dates are not effective dates. OCR text may contain errors; verify figures and tables against the original.",
    "Comparison uses ranked topic evidence. It is not a complete document-by-document comparison.",
    "Research entity was not specified. Source-specific applicability must remain explicit in the answer.",
    "Claims are automatically checked against cited excerpts. This is not independent expert verification. Uncertain or unsupported claims are withheld for review.",
    "Citation IDs are validated. Whether each citation supports its claim still requires review.",
    "The answer may omit a material qualification or contain an unresolved difference in scope. Inspect the evidence review below."
  ]
}