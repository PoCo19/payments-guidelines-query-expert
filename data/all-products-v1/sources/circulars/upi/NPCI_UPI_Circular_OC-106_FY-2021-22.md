# UPI OC 106 - UDIR - Auto reversal facility for Deemed approved cases marked as RET by Beneficiary

Circular/reference number: NPCI/UPI/OC-106/2020-21

<!-- Page 1 -->

NPCI
NATIONALPAYMENTS CORPORATION OF INDIA
NPCI/UPI/OC-106/2020-21 March 23, 2021
To,
All Members participating in UPI Network
Madam / Dear Sir,
Sub:UDiR-Auto reversal facility forDeemed approved cases marked as RET by
Beneficiary
Ref: Operating Circular No. 98 dated 24th Nov, 2020 on UDiR & Technical Specification
Document (TSD)
We refer to UPI Operating Circular 98 on UDIR and are pleased to inform that UDIR (Unified
Dispute & Issue Resolution) is live in UPl.
As a part of the UDiR functionality, “Online reversal" will be triggered to all Remitter banks for
deemed approved cases as and when Beneficiary Bank (live in UDIR) marks “RET" in response
to Auto Update APl. Remitter can receive ReqPay Debit Reversal APl once the auto update is
triggered (presently it is triggered every hour for maximum of 3 attempts). The APl will have
“AUTOUPDATE' in Txn.note tag for these requests.
In order to handie these reversals, we hereby advised member banks to follow below procedure:
As a Remitter:
Remitter Banks needs to refer UPl Adjustment report before taking action on RET received cases
to ensure that double credits are not passed in customer accounts for Return adjustment.
Refer below table for details:
Report Adjustment Originating Reason
Bank As name Type Channel Code Changes Action
115- Refer for adjustment type
Remitter Adjustment RET UDIR 120 Yes RRC
No action to be taken in
reconciliation as money is
Remitter Adjustment RRC UDIR 501 Yes reversed online
Pass credit to customer
A/C, if not done in online
Remitter Adjustment RRC UDIR 502 No and flag RRC 5O1 in URCS
All Remitter banks, including those which are not live on UDiR, should follow the above process
(action) for RET cases. Bank should pass manual credit to customer accounts only after checking
whether the amount is reversed online or not to the customer account.
1001A, The Capital, B Wing, 10th Floor
Bandra Kurla Complex, Bandra (E), Mumbai 4ooo51
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
We would also like to update on below 2 points mentioned in UPl OC-98
1. Reconciliation, Settlement & Dispute Management Process - We would like to inform
you that updates received for Time Out and DRC pending transactions within the
files.
2. Auto Conversion of Complaints into Chargeback - This functionality is under
development at this moment. We will notify members once the functionality is made live
in.UDIR.
Please make note of the above and disseminate the instructions contained herein to the
officials concerned. For any queries or clarification, please contact:
Name e-mail ID Mobile Nurmber
Rama Raju rama.raiu@npci.org.in 81081 22895
Neha Kumari neha.kumari@npci.org.in 91678 52531
Yours faithfully,
Saiprasad Nabar
Chief - Online Product Operations & Technology
1001A, The Capital, B Wing, 10th Floor,
BandraKurla Complex,Bandra(E), Mumbai 4o0O51.
T: +9122 40009100 F: +9122 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067
