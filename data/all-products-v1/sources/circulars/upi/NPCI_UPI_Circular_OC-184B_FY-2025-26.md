# UPI | OC No. 184 B | FY 2025-26 | Addendum to OC – 184 Modification in UPI chargeback rules and procedures

Circular/reference number: OC-184B

<!-- Page 1 -->

NPC
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCUPI/OCNo.184B/2025-2026 Jun 20, 2025
To,
All Members of Unified Payments Interface (UPl)
Subiect: Addendum to OC - 184 Modification in UPl chargeback rules and procedures
Reference may be taken from UPI operating circular vide NPCI/UPI/OC No. 184 &184A. In URCS if the
11th chargeback (IFSC +Account number) and 6th chargeback (Payer VPA +Payee VPA) gets declined
with reason code for CD1 and CD2 and after due diligence remitting bank finds the customer dispute is
genuine and want to raise chargeback then bank is raising request to NPCi for whitelisting the dispute
post which bank can raise chargeback through URCS.
In view of the above, to avoid NPCI intervention for whitelisting the disputes, NPCI has simplified the
process by allowing issuing/remitting bank to raise chargeback which are rejected due to negative
chargeback rule, the good faith dispute has been named as RGNB (Remitting bank raising good faith
negative chargeback).
Note: RGNB adjustment should be raised by the issuing/remitting bank only when URCS declines the
normal chargeback with CD1 & CD2 reason code. RGNB option is available only through front end.
This option should not be used to avoid any compensations and penalties, any deviation shall be treated
as non-compliance to the NPCI guidelines.
Refer Annexure - 1 for RGNB procedural guidelines and Annexure - 2 for user manual.
The above functionality will be implemented in URCS with effect from July 15, 2025.
Member banks are advised to take a note of the above and disseminate the information contained
herein to the officials concerned.
Warm Regards,
SD/-
Giridhar GM
Chief-CustomerSuccess

<!-- Page 2 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure- 1
RGNB - Remitting Bank Raising Good Faith Negative Chargebacks:
Remitter/issuing bank can raise good faith negative chargebacks in URCS which are decline
in URCS with reason code CD1 (declining the 11th Chargeback for iFSC and Account Number
based combination) and CD2 (declining the 6th Chargeback for Payer VPA and Payee VPA
combination). Once the adjustment is raised fund will be settled immediately by crediting the
lemitter bank who has raised the adjustment and debit the same to beneficiary bank who has
received good faith negative chargeback. Beneficiary bank who has received the good faith
negative chargeback has to accept or represent RGNB within 3 calendar days for P2P (U3)
and 15 calendar days for P2M (U2) otherwise the adjustment window will be closed on
deemed acceptance.
Key Points:
1. Member banks should do due diligence and proper validation of all adjustments
before raising in URCS as URCS will not vafidate adjustment entries raised by the
member banks in the system.
2. URCS will check the duplicate good faith chargeback through DRORGID, CRORGID,
TXNID, ADJAMOUNT, ADJFLAG AND TXN SUBTYPE fields. If duplicate
adjustments are identified, then URCS will decline the same.
3. Banks should use proper and correct three digits code while raising adjustments as
per the AUTH settlement only (If the AUTH transaction is settled e.g. Remitting bank
- ABC and Beneficiary bank XYZ then same bank codes have to be used for raising
debit/credit adjustments), three-digit code should not be altered.
4. P2P customer compensation will be processed same as per existing process. If the
good faith charge back is accepted or deemed accepted, then URCs will process the
compensation by default if it is beyond the TAT. URCS will check the number of days
between transaction date and adjustment date is beyond T+1 before 4PM then
compensation will be processed.
5. For P2M If acquiring bank/beneficiary bank wants to pay customer compensation
along with the dispute amount, then bank should choose compensation flag 'Y' for
yes otherwise choose 'N' for no.
6. Generic good faith chargeback RGNB transaction amount, customer compensation
amount (if applicable) will be settled in existing NTSL line item 'Net Adjusted
Amount' & *Customer Compensation' for Non-Compliance Debit/Credit.
7. All other validations will remain same refer 0C 206 & 206A for details.

<!-- Page 3 -->

NPCI
NATIONAIPAYMENTSCORPORATIONOFINDIA
DISPUTES REASON CODES, DISPUTE FLAGS & Description
Adjustment Report Yes
Penalty /Status Yes (Mandatory) Yes/No (As chosen by Bank) Yes (Mandatory) (Mandatory)
Movement Credit - REM Debit - BEN Credit - BEN Debit - REM
Who should Beneficiary/ Acquiring Bank Beneficiary IAcquiring Bank Beneficiary /Acquiring Bank URCS
Who can raise Remitting Bank/Issuing Bank URCS
Dispute Description Remitter Generic Good Faith Negative Chargeback Beneficiary Acceptance to the Generic Good Faith Negative Chargeback Beneficiary Representment to the Generic Good Faith Negative Chargeback Beneficiary Deemed Acceptance to the Generic Good Faith Negative Chargeback
TAT calendar days calendar days calendar days calendar days  calendar days calendar days. calendar days
Reason code Description It is valid P2P chargeback, not a negative chargeback It is valid P2M chargeback, not a negative chargeback Accepting P2P chargeback Accepting P2M chargeback Rejecting P2P chargeback, amount already credited in beneficiary account Rejecting P2M chargeback, goods/service already provided to the customer. Refund already processed Deemed acceptance of P2P Generic good faith chargeback Deemed acceptance of P2m Generic good faith chargeback
Reason Codes NB2 NA1 NA2 NR1 NR2 NR3 ND1 ND2
Dispute Flag RGNB RGNB BGNA BGNA BGNR BGNR BGNR BGND BGND
U2/U3
P2M P2M P2M
