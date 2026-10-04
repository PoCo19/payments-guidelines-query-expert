# IMPS I OC 117 I FY 23-24 I Circular 117 UDIR Enhancing complaint handling and resolution process for IMPS transactions

Circular/reference number: NPCI/2023-23/IMPS/117

<!-- Page 1 -->

 
 
NPCI/2023-23/IMPS/117                                                                                                                4th Aug 2023  
To,  
All Members participating in IMPS Network 
 
Madam/Dear Sir, 
Sub: Unified Dispute and Issue Resolution (UDIR) - Enhancing complaint handling and resolution 
process for IMPS transactions. 
We refer to RBI Circular RBI/2020-21/21 DPSS.CO.PD No. 116/02.12.004/2020-21 dt. 6th Aug'20 on 
Online Dispute Resolution (ODR) System for Digital Payments, whereby it has advised PSO and PSPs 
i.e. banks and non-banks to implement online dispute resolution process for handling and resolving 
customer complaints. 
NPCI has introduced UDIR which can act as a layer for member banks to connect their systems and 
handle disputes / queries thru API calls. 
Key Enablement: Following are the key propositions, which participants need to enable for facilitating 
online dispute resolution of customer complaints for IMPS deemed transactions. 
1. Remitter Bank 
a. To connect their CRM/Complaint management system or any other internal system 
(mobile/internet banking/etc.) to UDIR system at NPCI to be able to raise dispute. 
b. To make necessary changes in reconciliation and complaint handling process at Bank end. 
c. To process reversal in customer account on the basis of return response received from 
Beneficiary. 
d. To communicate to customer any change in the status of the transaction / complaint or 
dispute through CRM, mobile app, internet banking, SMS, Email etc. 
2. Beneficiary Bank 
a. To make necessary changes at Bank’ IMPS switch and CBS for ascertaining the status of 
transaction when ReqChkTxn API is received as Autoupdate or for complaint raised. 
b. To make necessary changes for processing credit or return for deemed transaction once 
the ReqChkTxn API is received. 
c. To make necessary changes in reconciliation and dispute handling process at Bank end. 
The list of APIs and other important points along with changes in handling of LR/CR/VR are given in 
Annexure A. 
Members can refer latest version of Technical Specification Document (TSD) for implementation. All 
members should have it implemented in their DR setup too, for giving seamless services to the end 
customers. 
You may please make a note of the above and disseminate the information contained herein to all the 
officials concerned. 
 
Yours sincerely, 
SD/- 
Kunal Kalawatia 
Chief Products

<!-- Page 2 -->

 
                                                                                                                                                               Annexure A 
IMPS – UDIR OC NPCI/2023-24/IMPS/117 dated 4th Aug 2023  
1. List of APIs - UDIR 
Sr. 
No 
API  
Type 
(Category) 
Scenarios/Transactions 
Initiator 
Responder 
1 
ReqChkTxn 
ChkTxn 
To check the status of the 
transaction / dispute or 
adjustment raised at NPCI 
Remitter 
UDIR 
2 
RespChkTxn 
ChkTxn 
NPCI response to remitter 
ReqChkTxn with latest transaction 
& dispute details 
UDIR 
Remitter 
3 
ReqChkTxn 
ChkTxn 
To check the status of the 
transaction at Beneficiary 
IMPS 
Switch 
Beneficiary 
Switch 
4 
RespChkTxn 
ChkTxn 
Beneficiary response to NPCI with 
the status of the transaction. 
Beneficiary 
Switch 
IMPS Switch 
5 
ReqComplaint 
Complaint 
To raise a complaint for financial 
transaction 
Remitter 
UDIR 
6 
RespComplaint 
Complaint 
Status of the complaint raised 
from NPCI. 
UDIR  
Remitter 
7 
ReqPay 
Credit 
Initiated by NPCI to remitter for 
crediting remitter account online 
IMPS 
Switch 
Remitter 
Switch 
8 
RespPay 
Credit 
Initiated by remitter to updates 
the status of the online credit 
Remitter 
Switch 
IMPS Switch 
9 
ReqChkTxn 
Status Check 
To check the response for timeout 
cases for complaints. If there is any 
complaint raised in prior and user 
selects the check status, this API  
Remitter 
UDIR  
All API's mentioned above are asynchronous in nature. 
In case of any rejection / error for API call, members to check the API response and act accordingly. 
2. Autoupdate in IMPS  
The auto update API will be triggered from IRCS to IMPS switch for deemed transactions, where 
beneficiary is live on UDIR. Beneficiary bank to update the status of the transaction (TCC / RET), 
including processing Credit or Return, in case it was not processed earlier in original online transaction. 
In case of return from Beneficiary bank, Remitter bank to process credit to customer account. Bank as 
a Remitter and Beneficiary need to have check for duplicate processing and ensure that the request is 
not processed more than once. 
The Auto update API indicative times shall be as following: 
Timing  
Transaction Time 
Range  
11:00 AM 
10:00 to 11:00 
12:00 PM 
11:00 to 12:00 
01:00 PM  
12:00 to 01:00

<!-- Page 3 -->

 
Note: Auto update will be triggered at interval of every 60 mins. Cases were no response is received 
in next 2 retry these transactions will be marked as timeout and will be made available in (New) UDIR 
adjustment reports. 
3. Reconciliation and Dispute Management: 
a) Dispute/adjustment shall be raised directly in the IRCS (back office) system for transactions 
based on the complaint received through UDIR API and response received from Beneficiary. 
 
b) UDIR will help resolve customer complaints in the following ways: 
i. 
Generating online reversal for the transactions marked returned by Beneficiary switch 
end (if it is within the reversal time period). 
ii. 
Raising chargeback (CB) for transactions. (wherever applicable)  
iii. 
Updating TCC/RET on the basis of response received by beneficiary in API response 
for Auto update and Complaint raised. 
 
c) Issuer/Remitter Banks can also have their Mobile Banking and Internet Banking systems 
directly connected to UDIR for checking the status of the transaction / dispute as well as 
raise disputes (complaints). 
 
d) Whenever the Remitter Bank raises a ReqComplaint request to UDIR, it is assumed that the 
request is for NPCI to raise a dispute (chargeback) on behalf of the Remitter Bank, based on 
the status of the transaction. 
 
e) Customer complaints related to the below scenarios will be addressed by UDIR: 
Dispute Category 
Dispute 
Flag 
Reason 
Code 
Reason Code Description 
Chargeback 
B 
108 
Remitter account debited but beneficiary 
account not credited 
Deferred 
Chargeback 
FB 
121 
TCC has been raised but customer still 
complaining that Beneficiary a/c is not 
credited. 
NOTE: If Complaint (chargeback) is initiated with any other reason code, the same will be 
rejected by UDIR 
f) When the UDIR system requests the status of a transaction from Beneficiary bank, the 
Beneficiary may give respond with following response code RC: 
RC 
Description 
00 
Success along with TCC and proper code 
UR 
Failure - along with RET and proper code 
UP 
Beneficiary Unable to update 
 
g) The APIs can connect and facilitate online transaction / dispute status check and raise 
complaints up to 60 days from the date of transaction.

<!-- Page 4 -->

 
h) Members shall also be able to connect their reconciliation or back office system to UDIR for 
raising first level disputes / adjustments viz. Chargeback, Re-presentment, Credit 
Adjustments, etc. directly through APIs in future. 
i) 
Please note importantly that –    
- 
Members live on UDIR should not pass manual entries (credit / reversal) to customer 
account for exceptions / pending transactions identified during reconciliation on the 
transaction date (T+0). Members can do so on T+1 day (onwards), only after checking 
the latest settlement / adjustment reports and customer account before passing manual 
entries, to avoid duplicate credit/reversal.  
- 
Members live on UDIR should not process credit online for complaint received on T+1 
day or later as Beneficiary unless bank has a system/process to validate the manually 
processed credits into the beneficiary account.  
j) 
The existing dispute management process including TAT, dispute & adjustment type, 
customer penalties for delayed credit for failed transactions, etc. shall be followed for 
complaints raised under UDIR approach. 
4.  Raw files and Adjustment report 
a) There shall be no changes in raw data files and settlement reports. 
b) In existing adjustment report new columns are added as per below table. This is for your 
information only. 
 
Column 
Value 
Scenario 
Originating 
Channel 
UDIR 
For UDIR initiated disputes/ Customer complaints via 
NPCI Website 
Auto-Update 
For auto-updated transactions 
Web 
For disputes initiated through Web 
Online-VR 
For disputes raised against online VR 
Online-CS 
For disputes raised against online CS 
File 
For disputes initiated through file upload 
Adjustment 
Settlement date 
Settlement date of 
the dispute 
For disputes raised between 23:00 and 00:00, this 
date will reflect the settlement date (which will be 
the next day) 
In all other cases, this will be the same as the dispute 
raise date 
Reason code 
Reason code used 
while raising the 
dispute 
Reason code chosen by banks while raising disputes 
OR 
00/M0 for disputes/adjustments raised based on 
online VR/CS

<!-- Page 5 -->

 
c) In IRCS front end, dispute / adjustments raised under UDIR can be identified basis. 
Value 
Scenario 
UDIR 
For UDIR initiated disputes 
Auto-Update 
For auto-updated transactions 
Online-VR 
For disputes/adjustments raised against VR 
Online-CS 
For disputes/adjustments raised against CS 
 
 
d) New report as UDIR Adjustment Report is made available to members as remitter and 
beneficiary for each cycle. It shall contain details of time outs and unable to update responses 
for UDIR APIs. Adjustment types are introduced for identification in new UDIR Adjustment 
report, however this shall not have any impact on settlement. 
Description 
Dispute 
Flag 
Beneficiary timeout 
BTO 
Beneficiary unable to update 
BUU 
Beneficiary invalid response 
BIR 
Remitter timeout 
RRC 
Remitter decline 
RDR 
Remitter invalid response 
RIR 
 
e) Changes in handling LR /VR/CS processing post Bank’s go live on UDIR: 
I. 
LR processing – will be dropped in online for Beneficiary banks live on UDIR and LR – 
Response code (RC) shall not be updated. 
II. 
In case of VR/CS processing, if original transaction is still in deemed status (08) and no 
disputes are raised through Auto Update, Complaints or thru IRCS. 
VR/CS 
Action 
Successful (00) 
TCC is raised in BCS and transaction is removed from timeout report 
/penalty calculation/Auto-update list. 
Declined (M0) 
RET is raised and transaction is removed from time out 
report/penalty calculation/auto-update list. 
Any other 
response code 
No change in status of the transaction as well as in IRCS 
 
In above scenarios, transaction status in raw data file will be deemed and settlement of 
funds will be in NTSL transaction section as per the adjustment raised.  
5. Importantly, for detailed functionality, specification, validation and controls, member to     
refer the latest Technical Specification Document for implementation.
