# Circular No.79 - Implementation of deemed approved process in UPI & Segregation of UPI and IMPS settlements

Circular/reference number: OC-79

<!-- Page 1 -->

   F-,-rr-1; 
NATIONAL PAYMENTS CORPORATION OF /NOIA 
NPCI/UPI & IMPS/ OC No 79/2016-2017 
Jan27,2017 
To, 
All Members of UPI (Unified Payments Interface) & IMPS (Immediate Payment Services) 
Madam/Dear Sir, 
Sub: A. Implementation of Deemed Approved process in UPI 
B. Segregation of UPI & IMPS Settlement 
Please refer our circular NPCI/UPI/ OC No.14/2016-17 dated 5
th January 2017 wherein we have 
informed about implementation of -
(A) Deemed Approved process in UPI (for timed out transaction response from beneficiary banks)
(B) Segregation of UPI & IMPS Settlement
Date of Implementation of (Al & (Bl above: 1
st Feb 2017. 
(A) Implementation of Deemed Approved process in UPI
Existing Process 
When NO response for the credit reversal 
request within the TAT or 96 as the response 
code received from the beneficiary bank, in 
such 
cases, 
NPCI 
was 
considering 
the 
transaction as declined and the settlement was 
I not processed. The response code in the raw
data for such cases was reflected as 'BT'. 
New Process w.e.f. 1-2-2017 
When NO response for the credit reversal 
request within the TAT or 96 as the response 
code received from the beneficiary bank, in such 
cases, N PCI will be considering the transaction as 
deemed approved and the settlement will be 
processed. The response code in the raw data 
will be reflected as 'RB'. 
Note:- If the beneficiary responds to the credit reversal request as successful, then we 
will not be considering those transactions as deemed approved. Such transactions will 
be treated as declined and settlement will not be processed. The final response in the 
raw data for such cases will be 'BT'. 
(For further details on the existing and new process please refer the Annexure A) 
1. 
HOW BENEFICIARY BANK SHOULD HANDLE THE UPI TIMED OUT/DEEMED APPROVED
TRANSACTIONS:
EXISTING IMPS PROCESS FOR HANDLING DEEMED APPROVED TRANSACTIONS, RULES,
DISPUTES TAT & PENALTIES, ETC. WILL BE SAME FOR UPI DEEMED APPROVED
1 
1001A, The Capital, S Wing, 10th Floor, Sandra Kurla Complex, Sandra IE), Mumbai 400 051. T: +912240009100 F: +912240009101 www.npci.org in

<!-- Page 2 -->

TRANSACTIONS (FOR DETAILS PLEASE REFER our IMPS Circular 28 - Processing of Timed 
Out Txn). 
NOTE:- The penalty provision for UPI deemed approved transactions will be applicable 
from 16
th February, 2016. 
(For further details on penalty clauses, please refer our IMPS OC No 65 - Penalty for delayed 
credits for timed out txns_effective_0l.01.2016) 
2. 
DISPUTES ALLOWED FOR REMITTING BANK: 
a. 
Chargeback, pre-arb1trat1on, arbitration.
b. 
Deferred chargeback, pre-arbitration on deferred chargeback and arbitration on 
deferred chargeback.
3.
ACTION EXPECTED FROM BENEFICIARY BANKS: (TCC - Transaction Credit Confirmation).
Beneficiary should reconcile all deemed approved transactions and confirm the status in
RGCS as follows:
a 
Upload TCC - 102 in RGCS 1f customer a/c is credited online but response to NPCI 
has not been sent by beneficiary bank. 
b 
Upload TCC - 103 in RGCS 1f the customer a/c is not credit in online and the same 1s 
credited manually. 
c.
Upload Returns: If the customer account cannot be credited due to any reason (e.g. 
closed a/c, invalid a/c etc.) then beneficiary bank should return the funds to the 
remitting bank through RGCS.
d.
Beneficiary bank should download all adjustments raised by other banks (as
rem1tter) for deemed approved transactions and respond to those adjustment either 
by accepting or rejecting them in RGCS (Representing chargebacks, pre-arbitration
accept/reject for the chargebacks & deferred chargeback raised by the remitting 
banks on beneficiary banks.)
4.
A 
licabilit 
of DEEMED APPROVED transactions: Deemed approved functionality is 
applicable for all UPI financial transactions i.e. (A) PAY (B) COLLECT (C) MERCHANT
S.
DEEMED APPROVED RESPONSE CODE IN RGCS: RESPONSE CODE - RB is assigned as the 
response code for deemed approved transactions in U Pl 
Note: All UPI member banks as remitter should ensure not to reverse their customer's
account for the res onse code - RB in theiutomated__QLmanual reconciliation 
rocess.
Remitting bank should check TCC/RET and update their customers suitably for the deemed
approved transactions. If beneficiary bank does not raise TCC/RET, then remitting bank may
raise chargeback. "CHARGEBACKS SHOULD BE RAISED BY THE REMITTING BANKS ONLY IF 
THERE IS CUSTOMER COMPLAINT".. REMITTING BANKS SHOULD NOT RAISE ANY 
CHARGEBACK ONLY BECAUSE TCC/RET IS UPDATED BY BENEFICIARY BANK. 
2

<!-- Page 3 -->

SD/-

<!-- Page 4 -->

I. ' 
Annexure A 
Existing Process: 
NPCI sends credit request message to the beneficiary bank and beneficiary bank should respond 
to NPCI either as approved or declined with appropriate response code. If beneficiary bank does 
not send any response to NPCI, then it is treated as declined transaction. Please see the flow of 
transaction as follows:-
•
Remitting bank gives successful response to NPCI after debiting their customer's account
online
•
NPCI sends credit request message to the beneficiary bank
•
Beneficiary bank does not respond to the request message then N PCI will send Check
Transaction {CT) request message three times. If beneficiary respond to NPCI for the CT 
request, then the transaction will be updated as either approved or declined as the case 
may be.
•
If the response from beneficiary bank is not received for all three CT messages, then
NPCI send credit reversal request message to beneficiary bank and debit reversal
request message to the remitting bank. Transaction will be treated as decline
irrespective of whether response to the reversal request message is received or not 
received from beneficiary bank. And, no adjustments are allowed for such transaction.
•
Decline transactions are reversed by the remitting banks online or post reconciliation, if 
the on line reversal does not happen for any reason whatsoever.
•
The 
online 
response 
message 
{i.e. 
<RespreqMsgld=""
result="SUCCESS I FAILURE I PARTIAL I DEEMED" 
errCode="">) 
contains 
"APPROVED,
FAILURE, PARTIAL & DEEMED approved" flags. Currently NPCI is sending only Approved,
Partial and Failure flags. If beneficiary bank does not respond to the credit reversal
request message, presently, it is treated as declined transaction. 
Hence, presently,
DEEMED APPROVED flag is not being sent in the online message.
4

<!-- Page 5 -->

l 
Proposed Process: 
?f'ITTR 
NATIONAL PAYMENTS CORPORATION OF IND/A 
•
Remitting bank gives successful response to NPCI after debiting their customer's account
online.
•
NPCI sends credit request message to the beneficiary bank.
•
Beneficiary bank does not respond to the request message, then NPCI will send Check 
Transaction (CT) request message three times. If beneficiary bank respond to NPCI for
the CT request message, then the transaction will be updated as either approved or 
declined, as the case may be. 
•
If the response for any of the CT request messages is not sent by beneficiary bank, then
NPCI consider this as credit time out and send credit reversal request to beneficiary 
bank.
i)
If NPCI receives response for the credit reversal request message from the
beneficiary bank then NPCI update the same as either approved or declined as 
the case may be.
1i) 
If NPCI DOES NOT receive response for the credit reversal request message from
the beneficiary bank then NPCI will treat this transaction as DEEMED APPROVED 
with "Response C-9de - RB". Thereafter, NPCI will not send any debit reversal 
request message to the remitting banks.
iii)
PLEASE NOTE IMPORTANTLY THAT for any response code other than RC-00
(APPROVED) & RC- RB (DEEMED APPROVED), for all other decline transactions
remitting bank can reverse the customer's account in the online process. If the
online reversal fails due to any reason, in such cases, the customer's account has
to be reversed as part of the reconciliation process. Please check before
reversing the customer a/c manually, whether the customer a/c is debited and
the funds are available in pool a/c).
iv)
The 
onl1ne 
response 
message 
i.e.
<Resp 
reqMsgld='"' 
result="SUCCESS LFAILURE I PARTIAL I DEEMED" 
errCode="">) 
contains 
"APPROV[D, FAILURE, PARTIAL & DEEMED approved" flags. NPCI will start 
sending the "DEEMED" approved status in the online message to the PSP if the 
beneficiary bank does not send the response to the credit reversal request 
message. PSP should accordingly send response status as deemed approved to 
the customer on the UPI mobile APP 
For single debit multiple credit (SDMC) cases, even 1f one out of the multiple 
transaction 1s DEEMED APPROVED, then NPCI will send the status to the PSP as 
PARTIAL. PSP should verify the response code for each transaction and display 
the status to the customer's mobile screen as DEEMED APPROVED for SDMC 
transactions. 
Eg:- A customer 1nit1ated a transaction to 4 people. Out of which 1 transaction is 
deemed approved, one is declined and two arc successful. Then settlement will 
be proci?ssed for only 3 transactions For two successful record the response 
code will be 00, for deemed approved transaction the response code 1s RB and 
for the declined transaction the response code will be updated accordingly 
(based on the decline reason by the beneficiary). 
v)
Separate report for deemed approved transaction will be made available in
RGCS for both rem1tter and _beneficiary banks
5 
1001A. The Capital, B Wing, 10th Floor, Bandra Kurla Complei, Bandra IEI, Mumbai 400 051 T +912240009100 F +91 22 40009101 WWW npc1 org m
