# Circular 78 - Reconciliation and handling declined / timed out transactions in UPI for One-time mandate block

Circular/reference number: NPCI/UPI/OCNo.78I2019-2020

<!-- Page 1 -->

NPCL
NATIONALPAYMENTS CORPORATION OFINDIA
NPCI/UPI/OCNo.78I2019-2020 January 27,2020
To,
All Member Banks- Unified Payments Interface (UPl)
Dear Sir/Madam,
Sub: Reconciliation and handling declined / timed out transactions in UPl for One Time Mandate
block transaction types.
1. Background
UPl One Time Mandate block functionality facilitates blocking of funds in the customer's bank account on
approving the mandate block request using his/her UPl PiN. Subsequent debit/unblock against the blocked
funds is initiated by the originator of mandate request.
SEBI has vide their circular no.SEBI/HO/CFD/DIL2/CIR/P/2018/138 dated 01-November-2018 allowed
the UPI One Time Mandate block for Application Supported by Blocked Amount (AsBA) process in Initial
Public Offering (IPO) from January 01, 2019.
The volume in UPl One Time Mandate block is increasing as customers are opting for this channel to
participate in the IPO process. With similar use cases envisaged in coming days, it is imperative that the
process for this functionality is further streamlined.
2. Objective
It is observed that customer complaints in UPl One Time Mandate transaction arise on account of
unsuccessful or 'failed' transactions.
"UPl mandate failed transactions are on account on timeout sessions or when the response is not
received at NPCl within Turn Around Time (TAT) or any other technical issues."
The objective of this Circuiar is to explain handling and the controis to be built in UPl One time mandate
block transactions. The following inconsistencies are observed currently;
a) For mandate failed transactions banks do not unblock the funds to the customer's account either
online (basis the failed response) or during reconciliation process.
b) Member banks are not downloading the mandate related (financial/non-financial) raw file from UPl-
RGCs portal and performing 3 way reconciliation to initiate suitable action wherever it is applicable
post reconciliation.
Member banks are to conform to the process for handling failed mandate block transactions as defined in
the Annex enclosed with this circular. This will ensure customer confidence and bring uniformity among
member banks in processing of the failed / timed out UPl mandate block transactions.
Yours faithfully,
Praveena Rai
1001A, The Capital, B Wing, 10th Floor.
Bandra Kurla Complex, Bandra (E), Mumbai 4Oo O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annex
Reconciliation and handling declined / timed out transactions in UPlfor One Time Mandateblock
transaction types.
1, Daily reconciliation
Member banks to refer UPl Circular NPCI/UP/OC No. 9/ 2016-17 dated December 1, 2016 and
ensure following compliances for One Time Mandate related transactions as well;
a) For the purpose of reconciliation, member banks to download all financial & non-financiai
mandate transaction files cycle-wise from RGCS.
b) Banks are expected to perform three way reconciliation of mandate transactions cycle-wise,
basis the feed file (Raw Data) fram NPCl, banks switch and CBS extract.
 The reconciliation process for mandate transactions should be automated completely.
2.24 x 7 availability of mandate functionality across all banks
All member banks in UPl are to allow One Time Mandate block functionality 24x7 including at the
time of banks daily/monthly scheduled Start of Day (SOD) and End of Day (EOD) activities.
3. Online Blocking of funds in customer's bank account for mandate creation
The issuer bank to post a success response only after the funds in the customer's bank account is
successfully blocked online. If the funds in the customer's bank account do not remain blocked after
recover the funds from the customer's account in case of subsequent debit request to such blocks.
4. Procedure to handle online failure/time out scenarios in UPl One Time Mandate block
transactions
i. Mandate transaction Type - Create' :
For mandate type - CREATE, where the transaction is declined / failed online/ timed out at the
issuer bank, the funds in the customer's bank account should not remain blocked.
UPl times out the mandate create transaction and the final status will be failed when the issuer
bank does not send ack for ReqMandate or does not send the RespMandate within Turn
Around Time (TAT). For all declines, UPI  will sendRespMandateand
ReqMandateConfirmation with failure response to payer/payee PsP. UPl will also send
RegMandateConfirmation with failure to issuer bank.
Issuer bank to further initiate 'check status APl' with NPCl to confirm the final status of the UPl
One time mandate block transaction in case the bank receives a negative ack.
Action: If the funds remain blocked in the customer's bank account, the same should be
unblocked oniine basis the RegMandateConfirmation sent by UPl switch to issuerbank. If the
online unblocking of funds fails at issuer bank's end in CBs due to any reason, then issuer bank
is expected to identify the failed transactions (based on reconciliation) and unblock the same
manually in CBs and ensure customer's funds are unblocked for such failed transactions.

<!-- Page 3 -->

NPCI
NATIONAL PAYMENTS CORPORATION OFINDIA
ii. Mandate transaction Type - "Update' :
For mandate type - UPDATE, where the update transaction is declined / failed online / timed
out at the issuer bank, the funds in the customer's bank account shoufd not rernain blocked with
the amount as in the failed update request.
UPl times out the mandate update transaction and the final status will be failed, if the issuer
bank does not send ack for RegMandate or does note send the RespMandate within TAT. For
alf declines, UPl will send RespMandate and ReqMandateConfirmation with failure response
to payer/payee PsP. UPl will also send ReqMandateConfirmation with failure to issuer bank.
[ssuer bank to further initiate 'check status APl' with NPCl to confirm the final status of the UP[
One time mandate modify transaction in case the bank receives a negative ack.
Action: In case mandate type update request is failed due to any reason, the funds in the
customer's account should remain blocked with the previous success mandate amount. The
customer's account should not remain blocked with the amount as in the failed update request.
If the online update fails at issuer bank's end in CBs, then the issuer bank is expected to identify
(based on reconciliation) the failed transactions and revise the same manually in CBs.
ili. Mandate transaction Type - ‘Revoke' :
For Mandate Type - Revoke, all transactions should be approved except for declines at Issuer
bank's end on account of time out sessions / technical declines. In case of failure, UPl will send
RespMandate and ReqMandateConfirmation with failure response to payee/payer PsP. UPl
will also send ReqMandateConfirmation with failure to issuer bank.
Further, PsPs and the issuerlacquiring bank to keep a check at their end to ensure that no
other mandate type transactions like Create , Update and Debit is allowed, once revoke is
initiated against the same mandate.
Issuer bank to further initiate 'check status APl' with NPCl to confirm the final status of the UPl
One time mandate block revoke transaction in case the bank receives a negative ack.
Action: If the online 'Revoke' fails at issuer bank's end in CBS and the funds in the customer's
account remains blocked then the issuer bank is expected to identify  such failed
transactions(based on reconciliation) and unblock the same in-offline. The payee PsP shall
re-initiate failed revoke transactions online to minimise dependency on the offline settlement
process.
iv. Mandate transaction Type - ‘Financial Mandate Execution-Debit' :
In case of financial mandate execution - Debit, all transactions should be approved except for
declines at Issuer bank's end on account of time out sessions / technical declines.
When NPCl sends debit request message to issuer bank and the bank does not respond back
to NPCl within TAT, then NPCI will send debit reversal request message to the issuer bank.
Debit Reversal request to issuer is initiated in the following scenarios:
Failed financial mandate execution (Debit) or
When an acquiring bank sends a successful credit reversal for which UPl raises a debit
reversal.

<!-- Page 4 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Basis the debit reversal as cited above, the issuer bank is expected to re-block the funds in the
customer's account, if unblocked, and ensure a success response to the Debit Reversal
Confirmation (DRC) raised by UPl. In case DRC fails, the issuer bank to act in the following
manner in reconciliation'
If the customer's account is re - blocked online successfully, however, bank failed to respond
properly then the fund remains blocked, hence no issue.
If the customer's account was not re- blocked online, bank to re-block the account offline.
If the customer's account was not debited in the first place itself, the fund rernains blocked.
Action: The funds in the customer's account should not be released when the online mandate
debit execution faits, as this may result in out of fund scenarios for the lssuer bank. Further, it
is advised that the payee / acquirer/ initiates the mandate financial execution-debit well before
the mandate ‘End Date' so that the issuer bank has sufficient time to reconcile and recover the
funds. from the customer's account.
In case the online mandate execution-debit fails, basis the regquest received from the
payee/acquiring bank, the issuer bank is expected to identify such failed transactions and
recover the funds offline and credit the acquiring bank.
The above process shall be applicable till the time the 'Deemed Debit' in case of mandate
execution is introduced, which was approved in the UPl SCM dated August 20, 2019.
In case of Deemed Debit, as the customer has already authorized debit to the account by
accepting the mandate request, the financial mandate execution transaction, if failed, shall be
treated as Deemed debit and to be settled offline. For deemed debit cases, bank will not be able
to verify the digital signature offline and bank shall debit the customer account without verifying
the signature and details. NPCl shall communicate the deemed debit process through OC, once
the necessary developments and testing is done.
5. Partial Debit: UPl One time mandate has the option of partial debit against the total funds blocked
in the customer's bank account. In case of partial debit, debit is done for the requested partial
amount, and the remaining fund should be unblocked to the customer's bank account
(Online/Offline or both).
6. Auto Unblock of Funds on Mandate Expiry
One Time Mandate block reguest comes with a start date and a corresponding end date that defines
the life span of the mandate. The acquiring bank/payee PsP to ensure that the execution/revoke of
the mandate is initiated and settled within the life span of the mandate. On the end date of the
mandate the issuer bank should release the funds blocked in the customer's account through an
automated process on real time.
7. Decline of Duplicate Transaction
Issuer bank/ Payer PsP to ensure that mulfiple mandate blocks are not allowed in the customer's
account for the same mandate. The following to be taken into consideration;
no existing mandate request that is already created basis a unique identifier for the mandate. In
case of UPl based AsBA process, the issuer bank/payer PsP to check on the reflD tag that contains
the IPO identifier and the application number and avoid multiple mandate blocks.

<!-- Page 5 -->

NPCI
NATIONALPAYMENTS CORPORATION OFINDIA
8. SMs alerts to the customer for all the mandate transaction type
Member banks to send post transaction alert / notification to customers for all mandate type
transactions of Create/Update/Revoke/Debit and any actions initiated after reconciliation is done.
This notification to shall, at the minimum, inform about the payee details, transaction reference
number, transaction amount, mandate type, date/time of debit, etc.
9. Maker&Checker
Banks to reconcile all mandate transactions with proper maker and checker process as defined in
this document.
****
