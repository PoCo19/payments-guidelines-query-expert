# AePS | OC 84| FY 23 24 | UDIR Enhancing complaint handling and resolution process for AePS transactions

Circular/reference number: NPCI/2023-24/AEPS/084
Date: 21st July 2023

<!-- Page 1 -->

 
P a g e  1 | 4 
 
NPCI/2023-24/AEPS/084                                                                                                                21st July 2023  
To,  
All Members participating in AePS Network 
 
Madam/Dear Sir, 
Sub: Unified Dispute and Issue Resolution (UDIR) - Enhancing complaint handling and resolution 
process for AePS transactions. 
We refer to RBI Circular RBI/2020-21/21 DPSS.CO.PD No. 116/02.12.004/2020-21 dt. 6th Aug'20 on 
Online Dispute Resolution (ODR) System for Digital Payments, whereby it has advised PSO and PSPs 
i.e. banks and non-banks to implement online dispute resolution process for handling and resolving 
customer complaints. 
NPCI has introduce UDIR which can act as a layer for member banks to connect their systems and 
handle disputes / queries thru API calls. 
Key Enablement: Following are the key propositions, which participants need to enable for facilitating 
online dispute resolution of customer complaints for AePS transaction. 
1. Issuer/Remitter Bank 
a. To connect their CRM/Complaint management system or any other internal system 
(mobile/internet banking/etc.) to UDIR system at NPCI to be able to raise dispute. 
b. To make necessary changes in reconciliation and complaint handling process at Bank end. 
c. To process reversal in customer account on the basis of response (failed transaction) 
received wherever applicable. 
d. To communicate customer any change in the status of the transaction / complaint or 
dispute through CRM, mobile app, internet banking, SMS, Email etc. 
2. Acquirer/Beneficiary Bank 
a. To connect their switch application from which status of AEPS transaction can be 
ascertained and responded with on receipt of API request from UDIR.  
b. System connected to UDIR to have real time transaction data so that it can respond to the 
request received from UDIR, immediately after completion of transaction. 
c. To make necessary changes in reconciliation and dispute handling process at Bank end. 
d. To allow registration of complaint (Dispute) and checking status of transaction/complaint 
through BC/CSP/Agent point using UDIR API - Acquirer’s internal system (which is 
connected to BC) to connect with UDIR for customer transacting on any BC/CSP/Agent 
terminal of the (same) Acquirer. 
The list of APIs and other important points are given in Annexure A 
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

 
P a g e  2 | 4 
 
Annexure A  
AePS – UDIR OC NPCI/2023-24/AEPS/084 dated 21st July 2023  
1. List of APIs - UDIR 
Sr.No 
API  
Type (Category) 
Scenarios/Transactions 
Initiator 
Responder 
1 
ReqChkTxn 
ChkTxn 
To check the status of the 
transaction / dispute or 
adjustment raised at NPCI 
Issuer/ 
Acquirer 
(incase BC 
initiated)  
UDIR 
2 
ReqChkTxn 
ChkTxn 
To check the status of the 
transaction at the 
acquirer's end  
AePS SWITCH 
(NPCI) 
Acquirer 
Switch 
3 
ReqComplaint 
Complaint 
To raise a complaint for 
financial transaction 
Issuer/ 
Acquirer 
(incase BC 
initiated) 
UDIR 
4 
ReqChkTxn 
STATUS 
To check the response for 
timeout cases for 
complaints 
Issuer/ 
Acquirer 
(incase BC 
initiated) 
UDIR 
UDIR 
 
 
Acquirer 
Switch 
5       ReqChkTxn 
DisputeStatusChk 
To check the status of the 
fund transfer at the 
beneficiary end 
AePS Switch 
(NPCI) 
Beneficiary 
(Issuer) 
6       ReqChkTxn 
Advice 
Initiated by NPCI to Issuer 
for Cash deposit 
transactions 
AePS Switch 
(NPCI) 
Issuer 
Switch 
7 
ReqPay 
Reversal 
Initiated by Acquirer 
within settlement cycle  
sent to Issuer via AePS 
Switch 
Acquirer  
Switch (NPCI) 
 
 
AePS  
Switch (NPCI) 
AePS 
Switch 
(NPCI) 
 
Issuer 
Switch 
 
All API's mentioned above are asynchronous in nature. 
In case of any rejection/error for API call, members to check the API response and act accordingly.

<!-- Page 3 -->

 
P a g e  3 | 4 
 
2. Reconciliation and Dispute Management: 
a) Dispute/adjustment shall be raised directly in the ARCS (back office) system for transactions 
based on the complaint received through API of UDIR and response receive from 
Acquirer/Beneficiary. 
 
b) UDIR shall help resolve customer complaints in the following ways: 
i. 
Generating online reversal for the transaction based on response from 
Acquirer/Beneficiary Bank (if it’s within the reversal time period). 
ii. 
Raising credit adjustment for transactions failed at Acquirer Bank end and where 
reversal is not possible.  
iii. 
Raising chargeback (CB) for transactions. 
 
c) Issuer/Remitter Banks can also have their Mobile Banking and Internet Banking systems 
directly connected to UDIR for checking the status of the transaction / dispute as well as raise 
disputes (complaints). 
 
d) Whenever the Bank raises a ReqComplaint request to UDIR, it is assumed that the request is 
for NPCI to raise a dispute (chargeback) on their behalf, based on the status of the transaction. 
 
e) Customer complaints related to the below scenarios will be addressed by UDIR: 
Transaction Type 
Particulars 
Flag 
Code 
Cash Withdrawal  
Cash not received  
B 
NA 
Fund Transfer 
Remitter account debited but Beneficiary A/c not credited 
B 
NA 
Cash Deposit 
Cash not deposited in account 
B 
NA 
BHIM Aadhaar 
Pay 
 
Credit not processed for cancelled or returned goods and 
services 
B 
1061 
Goods and Services not as described / defective 
B 
1062 
Paid by alternate means 
B 
1063 
Goods or Services Not Provided / Not Received 
B 
1064 
Account Debited But Confirmation Not Received at Merchant 
Location 
B 
1065 
NOTE: If (Complaint) chargeback is initiated with any other reason code, the same will be 
rejected by UDIR  
f) When UDIR system requests the status of a transaction from Acquirer /Beneficiary –  
Acquirer: Cash withdrawal (CWD) | BHIM Aadhaar Pay(PUR) | Cash deposit (CDT) 
These values to be received / shared in “respCode” in RespChkTxn API subtype as 
DisputeStatusChk  
Code    Description 
00         Success  
UR 
Failure 
UP 
Unable to update

<!-- Page 4 -->

 
P a g e  4 | 4 
 
Beneficiary: Fund transfer FDT these values to be received / shared in RespChkTxn API, type - 
CREDIT and subtype - DisputeStatusChk  
Code   Description 
00       Success  
UP 
Beneficiary Unable to update 
Note – For not credited scenarios, the response code (RC) will be as per current online 
specifications (other than “00”)  
g) The APIs can connect and facilitate online transaction/dispute status check and raise 
complaints up to 90 days from the date of transaction. 
h) The existing dispute management process including TAT, dispute and adjustment type, 
customer compensation for delayed credit for failed transactions, etc. shall remain same and 
will be followed for complaints (dispute) raised under UDIR. 
i) 
Members shall also be able to connect their reconciliation or back office system to UDIR for 
raising first level disputes/ adjustments viz. Chargeback, Re-presentment, Credit Adjustments, 
etc. directly through APIs in future. 
4.  Raw files and Adjustment report 
a) No change in the existing raw data file. 
b) Reason Code (UR) shall be updated in ‘raw data files’ for transactions where reversal is 
processed before settlement cutover. 
c) New columns are introduced in existing adjustment report as below. 
 
 
d) In ARCS front end, dispute / adjustments raised under UDIR can be identified basis “UDIR” in 
maker and checker. 
 
5. Importantly, for detailed functionality, specification, validation and controls, member to refer 
the latest Technical Specification Document for implementation.   
 
 
Column 
Value 
Scenario 
Originating 
Channel 
UDIR 
For UDIR initiated disputes 
Web 
For disputes initiated through Web 
File 
For disputes initiated through file upload 
Adjustment 
Settlement 
date 
Settlement date 
of the dispute 
For disputes raised between 23:00 and 00:00, this date 
will reflect the settlement date (which will be the next 
day) 
In all other cases, this will be the same as the dispute 
raise date 
Reason code 
Reason code used 
while raising the 
dispute 
Reason code chosen by banks while raising disputes
