# UPI |OC-128A | FY26-27  Addendum to OC-128 Extension of additional response codes under Deemed Debit for mandate execution

Circular/reference number: NPCI/UPI/OC-128A/2026-27
Date: 3rd July 2026

<!-- Page 1 -->

NPC ALWAYS
FORWARD
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/UPI/OC-128A/2026-27 3rd July 2026
To,
All Members - Unified Payments Interface (UPl)
Dear Sir/Madam,
Sub: Addendum to OC-128 Extension of additional response codes under Deemed Debit for
mandate execution
With reference to UPI OC no. NPCI/UPl/OC No. 128/2021-22 dated 14th December 2021, response
codes VH, K1, 59, and VO were excluded from the deemed debit scope. Basis the ecosystem
feedback, the scope of Deemed Debit (DD) scenario are updated as mentioned below:
Changes in the Deemed Debit Scenario:
Sr. DD
Decline Response Code and Description Decline By
No. Applicability
59 -- Suspected fraud, decline/transaction declined
Remitter Bank Yes
based on risk score by remitter
K1 - Suspected fraud, decline/transaction declined
Remitter Bank Yes
based on risk score by remitter
VO - Payment stopped by court order Remitter Bank No
VH - Mandate signature is tampered or corrupt Remitter Bank No
Remitter Bank & Payer
VU / QD - Mandate expired No
PSP
Remitter Bank & Payer
VS - Duplicate mandate request No
PSP
Note: No changes for any other response codes
1. For IPO, RDS and SBMD secondary markets use case (Purpose code ‘01', ‘25', '76 and where
MCC is 6211):
In case of declines with response codes VO', “VH', VU', 'QD' or VS' i.e. from Sr. No. 3 to 6 mentioned
above, Acquirer / Payee may claim the transaction amount if it is as per the mandate created; through
BGGD option made available in URCS. [NPCl/UPI/OC No. 206A/2024-25 dated 12th March 2025]
2. For other OTM use cases (i.e. purpose code '01' and MCC other than 6211)
Declines with response codes VO', VH', "VU', 'QD' or 'VS' i.e. from Sr. No. 3 to 6 mentioned above,
are to be considered as declined and no service should be rendered by the Acquirer/Payee.
3. Any un-responded/declined transactions with response codes apart from those mentioned above
for mandate execution transactions with Purpose Code ‘01' or ‘25' or 76', shall continue to be
treated as Deemed Debit and settlement shall be done by debiting respective Remitter bank and
crediting the Acquirer bank.
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex,Bandra (E), Mumbai 4o0 O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCL ALWAYS
FORWARD
NATIONAL PAYMENTSCORPORATIONOFINDIA
4. Payer PsPs / Remitter Banks to ensure that declines under the above mentioned response codes
which are excluded for 'Deemed Debit' are populated strictly for genuine scenarios only.
5. The identifier for such settlement shall be with response code 'DD' (Deemed Debit) in URCS for
identifying the deemed debit transactions separately and initiate suitable actions. Also, additional
report for transaction treated as Deemed Debit is made available to the member banks in URCs.
All member banks are advised to use the Deemed Debit report and raw files for reconciliation
purpose and necessary actions.
6. Furthermore, members to note the following:
a) Remitter and Acquirer banks are advised to perform three (3) way reconciliation for non-
financial requests (create, update, revoke) and financial requests (execution) both with
Mandate raw file and transaction raw file (including 'Deemed Debit' file) respectively.
b) Remitter banks to ensure that funds blocked in the customer's account are auto unblocked
upon expiry of the mandate period.
c) Acquirer banks can raise BGGD, wherever applicable, within the mandate validity period.
d) Acquirer/Payee are advised fo process executions within the mandate validity period and no
duplicate executions are processed. In case of such instances, Acquirers should reconcile and
process credit adjustments upfront.
e) Issuer may raise chargebacks with appropriate reason codes for mandates executed post their
validity period (Chargeback reason code 1081 -- Transaction not settled within the specified
timeframes) and duplicate executions (Chargeback reason code 1084 - Duplicate/Multiple
Transaction), wherever applicable.
Members to take note of the above and update the process accordingly.
The changes in deemed debit applicability in the URCS system will be effective from 15th July 2026.
Your Sincerely,
SD/
Giridhar GM
Chief Customer Success
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 400 O51.
T: +91 22 40009100 F: +91 22 40009101
Werhia contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067
