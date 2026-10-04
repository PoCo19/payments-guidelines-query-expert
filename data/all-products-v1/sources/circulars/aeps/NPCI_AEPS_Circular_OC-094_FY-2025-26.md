# AePS | OC 094 | FY 25-26 | Implementation of Auto Acceptance of Chargeback option in ARCS back-office system.

Circular/reference number: NPCI/AEPS/OCN0.94/2025-2026

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/AEPS/OCN0.94/2025-2026 November 28, 2025
To,
All Members of Aadhaar Enabled Payment System (AePS)
Subject: Auto acceptance of chargebacks based on credit adjustments in the AePs system
Presently, credit adjustments raised by Acquiring banks and chargebacks initiated by Issuing banks
chargeback from T+0 day onwards (T = transaction date). Consequently, when a chargeback is
already raised and settled, any subsequent credit adjustment raised for the same transaction is
declined by ARCS, as per existing processing rules.
From a customer perspective, chargeback resolution typically takes up to five days, whereas a credit
adjustment could enable reversal to customer account on the same day of credit adjustment or T+1
day. To address the aforesaid issue, enhance efficiency and reduce dispute resolution turnaround
time (TAT), Auto-Acceptance of Chargebacks is being implemented.
Under this process, if a chargeback has been raised and settled, credit adjustment for the same
transaction will continue to be declined. However, ARCS will automatically accept the chargeback on
behalf of the Acquiring bank, ensuring faster resolution for the end customer.
Refer Annexure - 1A & 1B for the process and rules set for auto acceptance of chargeback in ARCS.
The above functionality will be implemented in ARCS with effect from Dec 23, 2025.
Member banks are advised to take a note of the above and disseminate the information contained
herein to the officials concerned.
Warm Regards,
SD/-
Giridhar GM
Chief- Customer Success
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4oo O51.
T: +9122 40009100 F: +91 22 40009101
contact@npci.org.inwww.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-1
A) Key Points: -
Auto acceptance of the chargebacks will be processed by the ARCs if chargeback is raised
and it is settled, post which if the Acquiring bank raises credit adjustment for the same
transaction, then the credit adjustment will be rejected as per the current process, however
ARCs will process auto acceptance of the chargeback on behalf of the Acquiring bank.
 Auto acceptance process is applicable only credit adjustments raised through bulk upload
option. In case, credit adjustment is raised through front end option, if chargeback is already
raised then ARCS will display the chargeback Accept/Reject option to Acquiring bank and
ARCS will not provide credit adjustment option.
Apart from above, there are no changes in any of the dispute rules/process such as TAT,
penalties, compensation, settlement, fees, GsT, reports/fifes, etc.
1) Below the Flag "UA" cites the chargeback has been accepted by the ARCS
BankAdjRefHo F009 Shttat Adjamt Shser URN Sherd File nane Reascn Apprcver Remarks Actinn
bank UA 2025-05- 15 200:00 306816538138 XXXyfw7OHLYCazOuKmheKKHToroinox 987 Sucoess
Below the Flag "A" cites the chargeback has been accepted by the Acquiring Bank
BarkAd ReiNo Fag Shtdal Adjamt Shser URN Stcrd File name Reasct statuts Approver Reaarks Action
benkcBiest 2025-11-12 150.00 531615917811 15bod0cb1386480685e3180304c34519 tost221025.csy
C) Refer belowthe table for rules and process set for auto acceptance of the Credit
adjustments.
Auto Acceptance of Chargeback is applicable for the following
type of transactions:
i) Cash Withdrawal (04)
TXN Type
ii) SHG cash withdrawal (15)
ili) Cash deposit BAV (32)
iv) BHIM Aadhar Pay (25)
Raised First in System Chargeback (settled)
Subsequent Adjustment
Credit Adjustment
Raised
1001A, The Capital, B Wing, 10th Floor.
Bandra Kurla Complex, Bandra (E), Mumbai 4O0 O51.
T: +9122 40009100F:+9122 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATION OFINDIA
ARCS declines credit adjustment as chargeback has already
Existing process
been processed
Irrespective of credit adjustment updated by ODR (UDIR) or by
Acquiring bank through bulk option in ARCS, if the chargeback is
already raised by the Issuing bank and settled then ARCS will
process auto acceptance of the chargeback, provided the
chargeback is not accepted/rejected by the Acguiring bank or it is
deemed accepted.
Note:
a) In case, chargeback raised and it is not settled, in such
Revised Process
scenario no auto acceptance shall be done by ARCS system.
The credit adjustment shall not be updated in ARCS as per
the existing processing rutes.
b) [ssuer/Acquirer Bank can know the source of chargeback
acceptance based on the following:
(i) If the Flag appears "A" it means chargeback has been
accepted by the Acquiring bank.
chargeback.
1001A, The Capital, B Wing,1Oth Floor
Bandra Kurla Complex, Bandra (E), Mumbai 4o0 051.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067
