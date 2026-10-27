# What changed in the UPI biometric addendum, and what should a payments analyst review?

Status: Needs review | Version: 3

Local reviewer attribution is not authentication. Imported snapshots do not certify current applicability.

## Question

What changed in the UPI biometric addendum, and what should a payments analyst review?

## Documented findings

The transaction limit for On-Device Biometric Authentication in UPI was enhanced from ₹5,000 to ₹10,000 effective 07th August 2026. [S1]

All existing validations, compliance requirements, specifications, and regulatory guidelines established in the earlier circular continue to remain fully applicable. [S1]

A payments analyst should review that Issuer Banks, PSP Banks, and UPI Applications must ensure adequate customer communication regarding the updated limit. [S1]

## Supplied operating context (not independently verified)

Not supplied; institution-specific impact is not established.

## Analyst-proposed actions (not source requirements)

Review checklist suggestions, not inferred institutional impacts:
- Product and operations: assess whether the documented change affects your processes.
- Compliance or policy owner: verify applicability, dates and retained obligations.
- Customer support: review whether approved guidance needs updating.
- Transaction risk owner: assess whether internal rules need review; no live rule configuration is inferred.

## Questions for review

Engineering review note: confirm source scope, retained safeguards and institution applicability with a payments reviewer. No independent approval has been recorded.

## Review history

[
  {
    "id": 6,
    "item_id": "ee18c2b95351495ea111a24f8d043f7e",
    "version": 1,
    "at": "2026-10-24T04:10:31.933461+00:00",
    "action": "created",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 7,
    "item_id": "ee18c2b95351495ea111a24f8d043f7e",
    "version": 1,
    "at": "2026-10-24T04:10:41.060711+00:00",
    "action": "generation_started",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 8,
    "item_id": "ee18c2b95351495ea111a24f8d043f7e",
    "version": 2,
    "at": "2026-10-24T04:11:09.607251+00:00",
    "action": "generated",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 9,
    "item_id": "ee18c2b95351495ea111a24f8d043f7e",
    "version": 3,
    "at": "2026-10-24T04:11:53.425229+00:00",
    "action": "edited",
    "reviewer": "",
    "note": ""
  },
  {
    "id": 10,
    "item_id": "ee18c2b95351495ea111a24f8d043f7e",
    "version": 3,
    "at": "2026-10-24T04:12:02.548666+00:00",
    "action": "submit",
    "reviewer": "",
    "note": ""
  }
]

## Snapshot

{
  "corpus": "d205ac78542f0e94d70f2beb68cd48b0ba242d1ef0024492c23bd32f67f889c8",
  "sources": {
    "2025-OC-226": "d871c32b5589542a3b190cc3fdfbb324c63d387389a0c5c62e863e09cf7f411e",
    "2026-OC-226A": "5cecb8f1f0b2cbdfeb0a992ad53dbf50a5ed6e728ce3037f8679ebb68412f8d8"
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

### S1 — Enhancement of Transaction Limit for On-Device Biometric Authentication in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_226_A_Enhancement_of_Transaction_Limit_for_On_Device_Biometric_Authentication_in_UPI_735a88b16a.pdf

NPCI/UPI/OC-226A/2026-27 — 03rd July 2026 To, All UPI Member Issuer Banks, PSP Banks and UPI Applications Dear Sir/Madam, **Subject: Enhancement of Transaction Limit for On-Device Biometric Authentication in UPI** Reference is drawn to NPCI circular NPCI/UPI/OC-226/2025-26 dated 07th October 2025, wherein On-Device Biometric Authentication (Fingerprint, Face, etc) was introduced as an additional option for authentication in lieu of UPI PIN. In view of increasing adoption in the ecosystem, it has been decided to revise the per-transaction limit for On-Device Biometric Authentication (fingerprint, face, etc.) in UPI is hereby enhanced from ₹5,000 to ₹10,000, effective 07th August 2026. Issuer Banks, PSP Banks and UPI Applications to ensure adequate customer communication regarding the updated limit. All existing validations, compliance requirements, specifications, and regulatory guidelines shall continue to remain fully applicable, and participants are required to ensure adherence. Yours faithfully, SD/- Sourabh Tomar Deputy Chief UPI Product

### S2 — Introduction of Additional Authentication methods in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

NATIONAL PAYMENTS: SEG eed pan | FORWPRD NPCI/UPI/OC-226/2025-26 7” October 2025 To, All UPI Member Issuer Banks, PSP Banks and UPI Applications Dear Sir/Madam, Subject: Introduction of Additional Authentication methods in UPI In the current UPI functionalities, one of the factors of authentication is implemented through the UPI PIN for transaction authentication (except UPI Lite and mandate execution) which is set using Aadhaar OTP or Debit Card credentials and Issuer OTP. We also refer to RBI circular RBI/2025-26/79 CO. DPSS. POLC. No. S 668 / 02-14-015 / 2025-2026 on Authentication mechanisms for digital payment transactions. To enhance customer experience, it has been decided to introduce additional authentication methods. These additional methods are optional for the user, and he/she may continue to use the existing methods. The following measures shall be introduced in UPI:

### S3 — Introduction of Additional Authentication methods in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

Key Guidelines: VIDA! Face Authentication for UPI PIN Set/Re-Set_and On-Device Biometric Authentication for UPI Transactions:

### S4 — Introduction of Additional Authentication methods in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

1. UPI PIN Set/Reset

### S5 — Introduction of Additional Authentication methods in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

1. UPI Applications / PSP Banks shall perform all required device compatibility validations & security validations including but not limited to restricting usage on rooted or jail-broken devices, unsupported OS versions, device compatibility and validating biometric enrolment/state, before the authentication through methods mentioned above. 1O01A, The Capital, B Wing, 10" Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051- eee T: +91 22 40009100 F: +91 22 40009101 oeernes ‘oo contact@npci.org.in www.npci.org.in eBuild ite= CIN: U74990MH2008NPL189067

### S6 — Introduction of Additional Authentication methods in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

i. UIDAI Face Authentication shall be introduced as an additional option, for UPI PIN Set/Re-Set in lieu of Card credentials or Aadhaar OTP.

### S7 — Introduction of Additional Authentication methods in UPI, page 2

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

NATIONAL Re | FORWPRD

### S8 — Introduction of Additional Authentication methods in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

2. Transaction Authentication

### S9 — Introduction of Additional Authentication methods in UPI, page 2

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

2. UPI Applications / PSP Banks and Issuer Banks shall ensure explicit customer consent is obtained, with customers having the!ability to opt out at any time.

### S10 — Introduction of Additional Authentication methods in UPI, page 1

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

i. On-Device biometric authentication (fingerprint, face, etc) shall be introduced as an additional option in lieu of UPI PIN. ii. This facility shall initially be available for transactions up to Rs. 5,000. The limit shall be reviewed in due course based on performance and evaluation. Issuer Banks, PSP Banks and UPI Applications may implement the above functionalities/features in adherence to NPC] Documenis.

### S11 — Introduction of Additional Authentication methods in UPI, page 2

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

3. Issuer Banks shall check,customer eligibility and validate authentication credentials before authorising biometric enablement, or PIN Set/Reset. UIDAI Face Authentication for UP] PIN Set/Re-Set:

### S12 — Introduction of Additional Authentication methods in UPI, page 2

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

4. UPI Applications / PSP Banks and Issuer Banks shall ensure strict adherence to UIDAI and other applicable’ guidelines. On-Device Biometric Authentication for UPI Transactions:

### S13 — Introduction of Additional Authentication methods in UPI, page 2

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

5. WPI Applications / PSP Bank shall ensure a fresh consent is obtained after each device binding operation before allowing further transactions.

### S14 — Introduction of Additional Authentication methods in UPI, page 2

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

6. Issuer Banks shall ensure appropriate customer communication at the time of biometric enablement, disablement, and transaction processing.

### S15 — Introduction of Additional Authentication methods in UPI, page 2

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

7. Issuer Banks shall disable this method for the account for all UPI Applications in case of changes or resets the UP! PIN. Transactions on such accounis shall be declined with specific error codes until a fresh consent is captured.

### S16 — Introduction of Additional Authentication methods in UPI, page 2

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

8. UPI Applications / PSP Banks shall ensure key rotation operation is undertaken before one year of biometric enablement.

### S17 — Introduction of Additional Authentication methods in UPI, page 2

https://www.npci.org.in/uploads/UPI_OC_No_226_FY_2025_26_Introduction_of_Additional_Authentication_methods_in_UPI_42c3693399.pdf

9. UPI Applications / PSP Banks shall mark the customer as inactive for this method if no transactions is performed within ninety day through this method and activated only upon customer confirmation. Your Sincerely, SD/- Sourabh Tomar Head UPI Product Togethen /== . ‘2D eBuild ==

## Automated review limitations

{
  "coverage": {
    "status": "issues_flagged",
    "findings": [
      {
        "kind": "possible_conflict",
        "reason": "The answer states that 'All existing validations... continue to remain fully applicable' (Answer Draft 2, Source S1). However, the earlier circular (S2.1 through S17.1) establishes specific operational requirements such as device compatibility checks (S5.1), obtaining fresh consent after device binding (S13.1), disabling the method upon PIN reset (S15.1), and key rotation within one year (S16.1). The answer's claim that these 'continue to remain fully applicable' is factually correct based on S1.2, but the potential for conflict arises if the analyst assumes the *limit change* supersedes all other operational constraints; the evidence shows they are distinct measures (per-transaction limit vs. cumulative operational rules). The answer distinguishes them by listing communication as a separate review item, which resolves the ambiguity.",
        "quotes": [
          {
            "citation": "S1",
            "quote": " Banks, PSP Banks and UPI Applications to ensure adequate customer communication regarding the updated limit. All existing validations, compliance requirements, specifications, and regulatory guidelines shall continue to remain fully applicable, and participants are required to ensure adherence. Yours faithfully, SD/- Sourabh Tomar Deputy Chief UPI Product"
          },
          {
            "citation": "S5",
            "quote": "1. UPI Applications / PSP Banks shall perform all required device compatibility validations & security validations including but not limited to restricting usage on rooted or jail-broken devices, unsupported OS versions, device compatibility and validating biometric enrolment/state, before the authentication through methods mentioned above. 1O01A, The Capital, B Wing, 10\" Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051- eee T: +91 22 40009100 F: +91 22 40009101 oeernes ‘oo contact@npci.org.in www.npci.org.in eBuild ite= CIN: U74990MH2008NPL189067"
          },
          {
            "citation": "S13",
            "quote": "5. WPI Applications / PSP Bank shall ensure a fresh consent is obtained after each device binding operation before allowing further transactions."
          }
        ]
      },
      {
        "kind": "scope_unclear",
        "reason": "The answer advises analysts to ensure 'adequate customer communication' (Answer Draft 3). The evidence in S14.1 specifies communication at 'enablement, disablement, and transaction processing', while S15.1 mentions communication during 'PIN changes or resets'. The answer does not explicitly clarify if the new limit enhancement requires a *new* communication protocol distinct from the existing ones listed in S14.1, potentially blurring whether the 'updated limit' triggers a specific subset of the broader communication requirements already mandated.",
        "quotes": [
          {
            "citation": "S1",
            "quote": " Banks, PSP Banks and UPI Applications to ensure adequate customer communication regarding the updated limit. All existing validations, compliance requirements, specifications, and regulatory guidelines shall continue to remain fully applicable, and participants are required to ensure adherence. Yours faithfully, SD/- Sourabh Tomar Deputy Chief UPI Product"
          },
          {
            "citation": "S14",
            "quote": "6. Issuer Banks shall ensure appropriate customer communication at the time of biometric enablement, disablement, and transaction processing."
          }
        ]
      },
      {
        "kind": "possible_conflict",
        "reason": "The answer cites Source S1 (dated 03rd July 2026) as the 'proposed changed source' and states the limit enhancement is effective 07th August 2026. Source S2 (dated 07th October 2025) sets the initial limit at Rs. 5,000. The answer implies S1 supersedes the limit in S2 but explicitly warns 'do not assume it supersedes the others'. This creates a scope conflict: if S1 only changes the limit and S2 remains 'fully applicable' (as per Answer Draft 2), then the *entirety* of S2 applies alongside S1. The answer fails to distinguish whether S1 is an amendment or a standalone circular, leading to uncertainty on whether S2's specific clauses (like S16.1 key rotation) are modified by S1 or remain exactly as written in S2.",
        "quotes": [
          {
            "citation": "S1",
            "quote": "NPCI/UPI/OC-226A/2026-27 — 03rd July 2026 To, All UPI Member Issuer Banks, PSP Banks and UPI Applications Dear Sir/Madam, **Subject: Enhancement of Transaction Limit for On-Device Biometric Authentication in UPI** Reference is drawn to NPCI circular NPCI/UPI/OC-226/2025-26 dated 07th October 2025, wherein On-Device Biometric Authentication (Fingerprint, Face, etc) was introduced as an additional option for authentication in lieu of UPI PIN. In view of increasing adoption in the ecosystem, it has been decided to revise the per-transaction limit for On-Device Biometric Authentication (fingerprint, face, etc.) in UPI is hereby enhanced from ₹5,000 to ₹10,000, effective 07th August 2026. Issuer"
          },
          {
            "citation": "S2",
            "quote": "NATIONAL PAYMENTS: SEG eed pan | FORWPRD NPCI/UPI/OC-226/2025-26 7” October 2025 To, All UPI Member Issuer Banks, PSP Banks and UPI Applications Dear Sir/Madam, Subject: Introduction of Additional Authentication methods in UPI In the current UPI functionalities, one of the factors of authentication is implemented through the UPI PIN for transaction authentication (except UPI Lite and mandate execution) which is set using Aadhaar OTP or Debit Card credentials and Issuer OTP. We also refer to RBI circular RBI/2025-26/79 CO. DPSS. POLC. No. S 668 / 02-14-015 / 2025-2026 on Authentication mechanisms for digital payment transactions. To enhance customer experience, it has been decided to"
          }
        ]
      },
      {
        "kind": "scope_unclear",
        "reason": "The answer mentions 'On-Device Biometric Authentication' generally. The evidence in S10.1 and S6.1 distinguishes between 'On-Device biometric authentication (fingerprint, face, etc)' and 'UIDAI Face Authentication'. The answer does not clarify if the limit enhancement applies to *all* biometric types mentioned in S10.1 or only specific ones, creating ambiguity on whether the Rs. 10,000 limit covers UIDAI Face Auth specifically introduced in S6.1.",
        "quotes": [
          {
            "citation": "S1",
            "quote": "NPCI/UPI/OC-226A/2026-27 — 03rd July 2026 To, All UPI Member Issuer Banks, PSP Banks and UPI Applications Dear Sir/Madam, **Subject: Enhancement of Transaction Limit for On-Device Biometric Authentication in UPI** Reference is drawn to NPCI circular NPCI/UPI/OC-226/2025-26 dated 07th October 2025, wherein On-Device Biometric Authentication (Fingerprint, Face, etc) was introduced as an additional option for authentication in lieu of UPI PIN. In view of increasing adoption in the ecosystem, it has been decided to revise the per-transaction limit for On-Device Biometric Authentication (fingerprint, face, etc.) in UPI is hereby enhanced from ₹5,000 to ₹10,000, effective 07th August 2026. Issuer"
          },
          {
            "citation": "S6",
            "quote": "i. UIDAI Face Authentication shall be introduced as an additional option, for UPI PIN Set/Re-Set in lieu of Card credentials or Aadhaar OTP."
          },
          {
            "citation": "S10",
            "quote": "i. On-Device biometric authentication (fingerprint, face, etc) shall be introduced as an additional option in lieu of UPI PIN. ii. This facility shall initially be available for transactions up to Rs. 5,000. The limit shall be reviewed in due course based on performance and evaluation. Issuer Banks, PSP Banks and UPI Applications may implement the above functionalities/features in adherence to NPC] Documenis."
          }
        ]
      }
    ],
    "basis": "Automated same-model review of supplied evidence only; not exhaustive or independent verification."
  },
  "withheld": [],
  "warnings": [
    "Coverage is limited to the imported snapshot. Issue dates are not effective dates. OCR text may contain errors; verify figures and tables against the original.",
    "Research entity was not specified. Source-specific applicability must remain explicit in the answer.",
    "Claims are automatically checked against cited excerpts. This is not independent expert verification. Uncertain or unsupported claims are withheld for review.",
    "Citation IDs are validated. Whether each citation supports its claim still requires review.",
    "The answer may omit a material qualification or contain an unresolved difference in scope. Inspect the evidence review below."
  ]
}