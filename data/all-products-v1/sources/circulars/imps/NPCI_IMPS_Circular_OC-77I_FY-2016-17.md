# IMPS-I-OC-77-I-FY-16-17-I-Consideration-of-Late-Response-for-Settlement

Circular/reference number: OC-77I

<!-- Page 1 -->

N?C/ 
"fmft<r  ?f7Tc1R f;r7T', 
NATIONAL PAYMENTS COIi.PORAT/ON OF /NOIA 
NPCI/IMPS/OC No. 77/2016 -17 
December 26, 2016 
To, 
All Members of Immediate Payment Service {IMPS) 
Dear Sir/ Madam, 
Sub: IMPS - Consideration of Late Response for settlement 
Objective 
Objective of this documents is to explain the settlement process for late response by beneficiary banks 
for all IMPS time out/deemed approved transactions (except M2P) so as to reduce the deemed 
approved cases. 
A. Existing Process
Currently, NPCI IMPS switch is expecting to receive response from beneficiary banks within 30 
seconds for all request messages (P2P, P2A, P2U & P2M). Any response which is sent by 
beneficiary bank to NPCI within 30 seconds for OR (Original Request), VR (Verification Request) & 
AM (Advice Message) is considered for settlement. If the beneficiary banks sends any response 
beyond 30 seconds (whether approved or decline), such responses are not taken in to 
consideration. Hence, these transactions are treated as timed out cases and are settled as deemed 
approved transactions (RC-08 / ISO-91). The transactions in raw data file sent to banks and in RGCS 
is as follows. 
1. 
2. 
3. 
Approved response received within 30 seconds: Final status of the transaction will be 
updated as approved transactions - RC-00. 
Declined response received within 30 seconds: Final status of the transaction will be 
updated as declined transactions (Decline reason could be business decline or technical 
decline, as the case may be. E.g. RC-Ml, RC-CU, etc.). 
Verification Request (VR} or Advice Message (AM): When remitting bank/member does 
not receive the response within 30 seconds, it will send verification request up to three 
time (advice message is sent by NPCI if the beneficiary is enabled with advice message). 
Final position of the transaction will be updated as either approved, declined or deemed 
approved, as the case may be. 
4.
Response NOT recefved within 30 seconds for OR/VR/AM: Final status of these
transactions are updated as deemed approved. Beneficiary banks are expected to
reconcile deemed approved transactions within T +1 working day and confirm the status
in RGCS by marking TCC-102/103 or RETURNs.
1/3 
1001A, The Capital, S Wing, 10th Floor, Sandra Kurla Complex, Sandra (El, Mumbai 400 051. T: +912240009100 F: +912240009101 www.npci.org.in 
CIN : U74990MH2 008NPL189067

<!-- Page 2 -->

B. Proposed Process
No change is required to the existing process for point no. 1, 2 and 3 above. 
Only for point 4 (above), we propose to consider the late response (i.e. response received after 
30 seconds) in the settlement (for each settlement cycle). At the time of the processing 
settlement, IMPS switch will verify the timed out cases (i.e. those remaining after the response 
for VR/AM is updated) with the late response and accordingly the transaction status will be 
updated from deemed approved to Approved/Declined as the case may be. Raw data files for 
banks & RGCS will be generated after considering the late response and will contain the response 
code (either approved or declined). 
CONDITIONS FOR MARKING TRANSACTION's FINAL STATUS AS APPROVED/DECLINED/TIME 
OUT, as the case may be, are given below: 
1.
Flagging as Approved: If late response for OR is RC-00 then the final status of the
transaction will be updated as approved - RC-00.
2.
Flagging as Declined: If the late response for OR is declined, then the final status of
the transaction will be updated as declined, with applicable response code.
3.
Flagging as Timeout: If no late response is received for any timed out transaction,
then the final status of the transaction will be updated as timed out/deemed
approved.
NOTE; Late response for VR/AM is not considered now. We may consider handling late 
response for VR/AM in Phase 2. 
C. CHANGES REQUIRED AT BANKS SIDE
There is no major change is required .to be done at banks' side. Following minor changes are 
required to be made so as to bring time out/deemed approved cases to near zero: 
a. Existing Process
If the beneficiary bank's IMPS switch is not getting response from the CBS within 30 seconds, then 
the switch is sending timed out response (IMPS RC-08 /ISO RC-91) to NPCI. 
b. Proposed Process
Beneficiary banks should stop sending time out response to NPCI and are expected to send 
either approved or decline response without any time limit validation i.e. even after 30 
seconds. NPCI switch will validate and update such belated response as the final status of the 
transaction, as follows: 
i.
If the late response received is within the settlement cycle, it will be considered
and the final transaction status will be updated as Approved/Declined, as the case
may be.
ii.
If the late response is received after the settlement cycle, such late response will
be dropped and the transactioT will be considered as timed out. In such cases,
the existing TCC/RET process has to be followed.
2/3

<!-- Page 3 -->
