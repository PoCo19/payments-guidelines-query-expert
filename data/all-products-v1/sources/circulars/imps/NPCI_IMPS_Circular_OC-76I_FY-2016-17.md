# IMPS-I-OC-76-I-FY-16-17-I-Process-to-handle-Original-Request-(OR)-and-Verification

Circular/reference number: OC-76I

<!-- Page 1 -->

NPCI/IMPS/OC No. 76/2016 -17 
To, 
All Members of Immediate Payment Service (IMPS) 
Dear Sir/ Madam, 
Ni='Cl 
,w-<ffzl ll T'1
'(rrq 
NATIONAL PAYMENTS COf/PC' 4T10N OF IND/A 
Sep 28, 2016 
Sub: IMPS - Process to handle Original Request (OR} & Verification Request (VR} messages 
Objective: The objective of this circular is to explain the process to handle the Original Request 
(OR) & Verification Request (VR) messages for IMPS transactions by both remitting & 
beneficiary banks. 
REMITTING BANKS 
Original Request Message: Remitting banks should not reverse their customer's account if 
the on line response received for OR is RC - 00 Approved & 08 {ISO-91) - Timed out (treated 
as Deemed Approved for IMPS settlement purpose). For any Response Code other than - 00 
& 08 (1SO-91), the remitting bank should reverse the transaction amount on line. 
Verification Request Message: When remitting banks send verification request message and 
the response received is RC-MO ONLY then the customer account should be reversed on line. 
IF THE REMITTING BANK RECEIVES ANY RESPONSE OTHER THAN RC-MO FOR VR, REMITTING 
BANK SHOULD NOT REVERSE THE CUSTOMER ACCOUNT ONLINE. 
REMITTING BANK 
SHOULD HOLD THE FUNDS IN THE POOL ACCOUNT AND INITIATE SUITABLE ACTION POST 
RECONCILIATION. 
NOTE: Other than RC-MO, NPC/ will settle funds for transactions for any response codes 
received for VR since it is treated as deemed approved. 
BENEFICIARY BANK 
Original Request Message: Beneficiary members are expected to send valid response codes. 
If beneficiary bank receives VR without OR, the beneficiary bank should send time out 
response i.e. ISO RC-91 AND NOT RC - MO (please refer OC NPCI/IMPS/OC No 74/2014-15 for 
details). 
Verification Request Message: For verification request message, beneficiary banks are 
expected to send only following three response codes, as the case may be:-
) 
400 051 ¥ +91224000910C F +912240009101 A.npc1 org n 
1001A, The Capital, B Wing, 1Cth Floor Bandra Kurla Corrplex, Band•a (f ' M1.:nba 
CIN: U74990Ml-l2 008NPL189067

<!-- Page 2 -->

RC-IMPS 
RC- ISO 8583 
Description 
00 
00 
Approved 
08 
91 
No response received from beneficiary bank/Response Timeout 
/ Deemed Approved 
MO 
MO 
Original transaction is unsuccessful, instructing remitting bank to 
reverse their customer a/c on line 
All IMPS members are requested to take up the matter with the technology team/service providers 
and ensure that above process is in place. 
For Verification Request, any response code other than RC-00 & MO, NPCI will treat as deemed 
approved. Hence it is strongly recommended to follow the above said process to avoid any out of fund 
situation. Please refer to the following table for details:-
TRANSACTION TYPE 
IMPS RESPONSE CODES 
OR Response 
08 
08 
08 
08 
VR Response (VR - 1,2,3) 
00 
08 
MO 
Other than 00, 08, 
MO 
Status update in Raw file after 
00 
08 
MO 
08 
VR response 
Approve/Decline 
Approved 
Deemed 
Declined 
Deemed Approved 
Approved 
Settlement of funds:-
(Remitter Bank Debit -
YES. 
YES 
NO 
YES 
Beneficiary Bank Credit) 
Should you need any further clarification/information, please contact following officials: 
Name 
Email Id 
Contact Number 
Shivani Saxena 
shivani.saxenaC@ngci.org.in 
07506446567 
Neelam Mishra 
neelam.mishraC@ngci.org.in 
08879772839 
Yours faithfully, 
Ram Sundaresan 
•
Head - Operations
SD/-
