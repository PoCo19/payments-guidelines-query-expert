# Circular 98 UDIR - Enhancing Complaint handling & resolution process for UPI transactions

Circular/reference number: NPCI/UPI/OC-98/2020-21
Date: 2nd July, 2020

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
NPCI/UPI/OC-98/2020-21 November 24, 2020
To,
All UPI Members - Banks, PSP's & Third Party Applications
Madam / Dear Sir,
Subject: UDIR- Enhancing Complaint handling & resolution process for UPl transactions
We refer to the RBI circular RBI/2020-21/21 DPSS.CO.PD No.116/02.12.004/2020-21 on Online
advised PSO & PSPs j.e. banks and non-banks & TPAPs to implement online dispute resolution
process for handling and resolving customer complaints. The Unified Dispute & Issue Resolution
(UDIR) approach was discussed in the UPi Steering Committee meeting held on 2nd July, 2020 and
was endorsed by SC for implementation by members.
2. Key enablements
Following are the key propositions, which ecosystem participants needs to enable for facilitating online
dispute resolution of customer complaints for UPl transactions:
A. Payer App
1. To enable raising of complaint/dispute from UPI App.
2. To display status of transaction and disputes, as and when updated at URCs.
3. To adhere to the guidelines
B. Payer PSP
1. To enable TPAP with standardized API's for enabling UDiR.
2. To ensure adherence to velocity checks for APl usage.
C. Remitter/Beneficiary Bank
1. To ensure necessary changes are done at switch and CBS end for supporting API's for online
status check and to take appropriate action on pending transactions viz. DRC (debit reversal
timeout) or Deemed (credit timeout) transactions, as the case may be.
UDIR process.
1001A, he Capital, B.Wing, 1oth Floor,
Bandra Kurla Complex, BanBgrEotumbai 400 051.
T: +9122 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
3. Member bank's CRM or any other system can also connect to UPl for raising and resoiving
complaints using the same APls.
3, Changes in existing dispute management process
The list of APl's and other important points are given in Annexure A
Members and TPAPs are requested to start the development and do the required changes at their
end for commencing certification (Bank - Remitter / Beneficiary, PSP - Payer / Payee and APp
testing) with NPCl at the earliest, to ensure go live by January 1 st, 2021.
Members can refer the documents listed below (Reference documents) for implementation. All
members should have it implemented it in their DR setup too for giving seamiess services to the end
customers.
You may please make a note of the above and disseminate the information contained herein to all
officials concerned.
Yours Sincerely,
Praveena Rai
Page 2 of 4

<!-- Page 3 -->

NPCL
e Lpi  hp
NATIONALPAYMENTS CORPORATION OF INDIA
Annexure A
UDIR - Enhancing Complaint handling & resolution process for UPI transactions
A. List of API's to be included to enable UDIR
1. ReqChkTxn APl (Existing API - will be enhanced)
2. ReqComplaint API (New APl) will have following categories:
i. Compiaint
Dispute
Refund
iv. StatusUpdate
CheckStatus
vi. Reversal
B. Some of the important points to manage UDIR program are as follows:-
1. Payer App to enable online transaction & dispute status check and raising of
complaints/disputes for resolution.
2. UPl will proactively auto trigger an API to bank (remitter/beneficiary) for checking and updating
the status of pending transactions viz. DRC (debit reversal timeout) or Deemed (credit tirmeout)
transactions, as the case may be.
As this functionality shall attempt to proactively update the status of pending transactions and
notify all the parties involved, members are advised to judiciously use request check
transaction APl (ReqChktxn). PSP/Banks to restrict it to not more than 3 attempts per
transaction per day, once it is implemented.
APls with appropriate action for updating the status of pending fransactions and onine
resolution of complaint.
4. For all requests (APls) received at NPCl, the status shall be checked in URCS first. The APl
request shall be sent to bank (beneficiary / remitter) for pending transactions and/or where
dispute or adjustment is not raised. On receipt of the response from the bank, the status and/or
dispute or adjustment, as the case may be, shall be updated in URCS and notified to all the
parties involved.
5. Auto-conversion of complaints into chargeback - Complaints received after the specified TAT,
shall be directly raised as chargeback, if not resolved online through Complaint APl.
Page 3 of 4

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
6. Acquirers are expected to integrate with aggregators and online merchants (as per NPCl
specification) for getting the status of the transaction at their end / response on dispute raised,
online on receipt of request complaint APl.
7. Rermitter / Beneficiary can also make use of the APl to raise first level adjustments / dispute
and to update the status of the transaction (TCC / RET / DRC).
8. Reconciliation, Settlement & Dispute Management process:
a. There shall be no changes in raw data files and settlement reports. Transaction status
(response code- RC) shall be updated in the raw data files for cases where TCC / RET /
DRC are updated within the settlement cycle.
b. Adjustment report shall have a separate indicator ('UDiR' in field ‘originating channel') to
identify disputes and adjustments (incl. TCC / RET / DRC / RRC) raised thru APls.
Members can refer the adjustment report for cases where the transaction status is updated
after settlement cutover.
c. Please note importantly, members live on UDIR should not pass manual entries
(credit/reversal) to customer account for exceptions / pending transactions identified
during reconciliation on the transaction date (T+0). Members can do so on T+1 day
(onwards), only after checking the latest settlement / adjustment reports and customer
account before passing manual entries, to avoid duplicate credit/reversal. Refer TsD for
further details.
d. The existing dispute management process including TAT, dispute & adjustment type,
customer penalties for delayed credit for failed transactions, etc. shall be followed for
complaints raised under UDIR approach.
Page 4 of 4
