# IMPS I OC 56 I FY 14-15 I Generation of Advice message by NPCI in place of Verification Request

Circular/reference number: OC-56I

<!-- Page 1 -->

•nc1 ·1x,nll xllll ·:/lciH 
• ,.
..,. 
NATIONAL PAYMENTS CORPORATION OF INDIA 
NPCI/IMPS/OC No. 56/2014-15 
March 30, 2015 
To, 
All Members, 
Immediate Payment Service {IMPS) 
Dear Sir/Madam, 
Sub: Generation of Advice Message by NPCI in place of Verification Request
The Steering Committee of IMPS (in the Meeting held on 17-12-2014) approved that NPCI 
operationalize generation of advice message to beneficiary bank instead of Verification Request (VR) 
where the original transaction is timed out. 
Existing Process: 
Remitting bank/PPI (hereinafter referred as "Remitter") sends credit request message to NPCI and 
waits up to 30 seconds for receiving the response. If the Remitter does not receive the response 
within 30 seconds, it will generate VR to find out the status of the Original Request (OR). VR is sent 
by Remitter maximum three times in either of the following two situations. 
i)
Remitter does not receive any response within 30 seconds after sending OR (0200
message).
ii)
Remitter has received timed out response from NPCI (in 0210 message) i.e. IMPS RC-08 /
ISO RC-91 which means status of the transaction at the beneficiary bank's end is
unknown.
If beneficiary bank responds to the VR, then the original transaction will be updated either as 
approved (RC-00) or declined (RC-MO), as the case may be. In case no response is received from 
beneficiary bank even after sending three VRs, then the transaction will be treated as timed out and 
the transaction is settled as Deemed Approved. 
Issues with the current process: 
It is observed that at times, the Remitter is sending incorrect VR, as follows: 
i)
VR preceding OR - In this case beneficiary bank sends decline response (RC-MO) because
they do not find OR. Based on the RC-MO, the Remitter reverses and credits their
customer account online since the transaction is declined by beneficiary bank.
Subsequently, when the OR is received by beneficiary bank, the transaction amount is
credited to the a/c and successful response RC-00 is sent by beneficiary bank. NPCI will
settle funds between Remitter and beneficiary bank since the transaction is successful
and approved. This situation may result in financial loss since the transaction is reversed
to remitting customer's a/c online based on the declined response by beneficiary bank
for VR which did not have preceding OR.
ii)
Remitter sends VR and no OR is sent.
iii)
NPCI sends successful response (RC-00) to Remitter even then Remitter still sends VR
due to system issue. 
iv)
. 
VRs are sent at irregular intervals. 
-9, 8.
C-9, 8th Floor
/Phone: 022 2657 3150
3TR<fi Rl>-illlfHl,
RBI Premises
 / Fax:022 2657 1001
<rRTT- q;'faj<R1,
Bandra-Kurla Complex
- I email: contact@nPf}'Wg.in 
<rRTT ,
Sandra East
 / Website: www.npci.org.in 
 - 400 os 1
Mumbai 400051
CIN : U7 4990MH2008NPL 189067

<!-- Page 2 -->

Proposed Process: 
To address the above issues, NPCI has come up with following solution: 
a)
VR functionality will be discontinued. (Please refer Annexure -2 for details).
b)
For transactions where no response is received from beneficiary bank, NPCI will send advice
message (0220 message) every 30 seconds up to maximum of three times till the response is
received either as approved or declined.
c)
On receiving advice message from NPCI, beneficiary bank should respond (0230 message) to
NPCI with the status of the original transaction.
d}
If Remitter sends VR, NPCI will drop the VR and send timeout response to the Remitter i.e.
RC -08 / ISO - 91.
e)
Beneficiary bank should send in their 0230 response message, status of the original
transaction using any of the below mentioned four response codes.
0230 RESPONSE SENT BY BENEFICIARY BANK FOR A 0220 MESSAGE 
AND TREATMENT THEREOF FOR ORIGINAL TRANSACTION 
Original 
Transacti 
ISO 
on 
IMPS-
Update 
Transaction 
Settlement 
8583-
Description 
RC 
Status in 
Status 
Status 
RC 
IMPS 
(IMPS 
II 
/ITM RCs) 
00 
Transaction Approved 
00 
00 
Approved 
YES 
MO 
Transaction declined 
MO 
MO 
Declined 
NO 
•
No Original transaction: Advice
message (0220) received without
the Original Message (0200).
•
When advice message is received
from NPCI, beneficiary bank
TXN Status is 
Unknown 
NO 
ascertains the status of the original
08 
08 
Deemed 
YES 
transaction. If the status thereof is
Approved 
unknown, then the beneficiary
bank should send NO response -
"status of the transaction is
unknown".
If beneficiary bank sends any response other than above RCs, 
TXN Status is 
Unknown 
such response codes will be ignored and the transaction will be 
08 
Deemed 
YES 
treated as Deemed Approved. 
Approved 
If NPCI does not get response from the beneficiary bank even after sending three advice messages, 
the transaction is treated as timed-out and the transaction is settled as Deemed Approved. Advice 
message shall contain the same RRN which is sent in the original message. 
2/6

<!-- Page 3 -->

v 
llnc1 
-➔lxall1 xll1 'l_-!Jli:11--1 
I 'I....
NATIONAL PAYMENTS CORPORATION OF INDIA
Actions as Remitter: 
•
Under the new process, Remitter should stop generating VR for timed out transaction.
•
Remitter should verify the settlement file to find out the status of such transaction and take
appropriate action as mentioned below:
I) 
If the response for the transaction is RC 00, it means transaction is successful on line and
hence, no action required.
II)
If the response for the transaction is RC MO, means the transaction is declined
transaction and Remitter should reverse and credit the customer's a/c.
Ill) If the response for the transaction is RC 08, it means status of the transaction is 
unknown and hence Deemed Approved. In such case, the existing reconciliation process 
has to be followed. 
Actions as beneficiary bank: 
•
Beneficiary bank should respond to advice request message (0220) with advice response
message (in 0230).
•
If the original transaction is successful, then the beneficiary bank should send response code
RC 0O.
•
If the original transaction is unsuccessful, then the beneficiary bank should send response
code RC MO.
•
If the beneficiary bank has not received the original transaction but received an advice
message, then the beneficiary bank should send RC NO.
•
If the beneficiary bank switch is uncertain about the status of the transaction, then the
beneficiary bank should even send RC NO.
•
BENEFICIARY BANK SHOULD NOT SEND ANY RESPONSE CODE OTHER THAN RC-00, RC-MO,
& RC-NO.
•
0220 ADVISE MESSAGE IS NOT INDEPENDENT TRANSACTION AND HENCE HAS TO BE
RELATED TO ORIGINAL TRANASACTION. CARE MUST BE TAKEN TO ENSURE THAT MULTIPLE
CREDITS ARE NOT AFFORDED TO BENEFICIARY CUSTOMER BASED ON 0220 ADVISE
MESSAGE.
Actions from NPCI: 
•
NPCI will send timed out response RC 08 (ISO 91) to Remitter if beneficiary bank does not
send any response for an OR within 30 seconds. Thereafter, NPCI will send advice request
message (0220) to beneficiary bank for which the beneficiary bank has to send response
(0230 message).
•
If NPCI receives successful response i.e. RC-00, from the beneficiary bank for advice
message, then the transaction status will be updated as successful with RC-00 and the
transaction will be settled.
•
If NPCI receives response from the beneficiary bank as RC MO for advice message, then NPCI
will update the transaction as RC MO. Since the transaction is declined, NPCI will not settle
this transaction. No adjustment will be allowed in DMS for transaction with RC MO.
•
If NPCI receives response as RC NO then it will be considered as timed out transaction and
the transaction will be settled as Deemed Approved.
3/6

<!-- Page 4 -->



<!-- Page 5 -->

'l--!lxct'lll xlll ·:t1a11  
NATIONAL PAYMENTS CORPORATION OF INDIA 
Enc. 
Annexure -1: 
0 
0 
0 
(Customer initiates 
IMPS TXN using any 
of the below 
originating 
channels} 
0220 Request 
REMITTING 
BANK/PPI 
SWITCH 
G0 
0220 Request 
0200 Request 
G
Mobile 
0
BENY 
CBS 
ATM 
(0220 Advice Message) 
AM-1 
Internet 
M 
p 
BENEFICIARY 
BANK SWITCH 
REM CBS 
USSD 
WAP 
SMS 
IVR 
NUUP 
s 
(0220 Advice Messag 
AM-3 
(0230 Advice Response Message 
RC-00/M0/NO 
CUSTOMER A/C IS 
CREDITED/ 
[OR] 
MIGHT HAVE NOT 
CREDITED 
Transaction Flow: 
1)
Remitter bank's customer initiates transaction through any channel.
2)
The transaction information is received by the Remitter bank. Remitter bank validates the
transaction and debits the customer's account.
3)
Remitter sends the transaction to NPCI.
4)
NPCI forwards the message to the beneficiary bank.
S)
Beneficiary bank does not send any response to NPCI within 30 seconds.
6)
NPCI will send timed out response to Remitter (RC-08 /150-91). 
On receiving timed out
response, remitter should treat the transaction as deemed successful and should not raise any
Verification Requests. Status of the timed out transactions should be searched from OMS.
7)
For Remitter & NPCI, status of the original transaction at the beneficiary bank's end is unknown.
8)
NPCI will send 0220 advice message to beneficiary bank up to maximum of 3 times till the
beneficiary bank responds to the 0220 advice message.
9)
Beneficiary bank has to respond with 0230 message either with success (RC-00) or with decline
status (RC-MO). Beneficiary bank has to send RC-NO in case advice request message does not
find any original transactions and if the status of the original transaction is unknown.
10) If beneficiary sends any response other than RC-00, MO, & NO, such transactions will be
updated as timed out transactions RC-08 /150-91 and process the settlement as Deemed
Accepted.
11) NPCI will update the final status of the transaction accordingly. In case no response is received
for any of the three advice message sent by NPCI, then the transaction will be treated as
deemed approved and the existing process on RC-08 will be applicable.
5/6

<!-- Page 6 -->

Annexure - 2: 
NPCI WILL OPERATIONALISE THE ADVICE MESSAGE ON IMPS SWITCH W.E.F JUNE 01, 2015 -
BELOW SCENARIOS WILL BE APPLICABLE IF IMPS MEMBERS ARE NOT READY EITHER AS REMITTER OR BENEFICIARY 
Scenarios 
Remitter 
Beneficiary 
NPCI 
Remarks 
Settlement 
Institution 
Bank 
Status 
Remitter Institution will send VR to find the 
status of original transaction same as 
existing process. 
NPCI will forward the VR to Beneficiary bank 
VR status will 
Remitter 
Beneficiary 
and wait for response up to 30 seconds and 
updated 1f IMf 
Institution is not 
Bank is not 
update the original transaction status 
Existing VR 
Scenario - 1 
ready with 
ready with 
whatever the response sent by beneficiary 
process will 
RC is 00 or MC 
otherwise IMF 
advice message 
advice message 
bank, in case of no response received from 
remain 
RC-08 will be 
implementation 
implementation 
beneficiary then the transaction will be 
updated 
treated as timed out/deemed approved. 
On receiving VR, beneficiary bank should 
verify the status of original transaction and 
update in response message accordingly 
Remitter 
Beneficiary 
NPCI will send timed out response to 
NPCI will not 
initiate either 
Institution is 
Bank is not 
remitter institution and thereafter remitter 
VR nor Advice 
OR status will 
Scenario - 2 
ready with 
ready with 
should not generate VR, remitter should 
remain as final 
advice message 
advice message 
check the status of the transaction in 
Message to 
I status
implementation 
implementation 
settlement reports 
beneficiary 
bank 
Original 
transaction wil 
Remitter institution will send VR to find the 
NPCI will initiate 
be updated wi• 
status of original transaction same as 
Advice Message 
the advice 
Remitter 
Beneficiary 
existing process, NPCI will send time out 
and send it to 
response 
Institution is not 
Bank is ready 
response to remitter for all VRs. 
beneficiary 
message that i· 
Scenario - 3 
ready with 
with advice 
NPCI will forward the 0220 advice message 
bank and 
sent by 
advice message 
message 
to Beneficiary bank and wait for response 
update the 
beneficiary 
implementation 
implementation 
up to 30 seconds and update the original 
original 
bank, in case o 
transaction status with the response sent in 
transaction 
no response fo 
0230 message by beneficiary bank 
status 
advice messag1 
accordingly 
transaction wil 
be updated wit 
IMPS RC-08 
Original 
transaction will 
NPCI will initiate 
be updated wit 
Remitter institution will not send VR on 
Advice Message 
the advice 
Remitter 
Beneficiary 
receiving time out response from NPCI. 
and send it to 
response 
Institution is 
Bank is ready 
NPCI will send advice message to 
beneficiary 
message that is 
Scenario - 4 
ready with 
with advice 
beneficiary bank. 
bank and 
sent by 
advice message 
message 
Beneficiary bank will have to verify the 
update the 
beneficiary 
implementation 
implementation 
original transaction status and respond 
original 
bank, in case of 
accordingly in 0230 message 
transaction 
no response fo1 
status 
advice message 
accordingly 
transaction will 
be updated wit 
IMPS RC-08 
6/6
