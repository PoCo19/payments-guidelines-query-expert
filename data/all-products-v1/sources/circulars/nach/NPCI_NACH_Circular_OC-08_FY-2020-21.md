# Circular no. 08 - Payment pre-validation services - Guidelines

Circular/reference number: NPCI/2020-21/NACH/Circular

<!-- Page 1 -->

 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
NPCI/2020-21/NACH/Circular No. 008 
 
 
 
 
     Jun 30, 2020 
 
To 
All member banks participating in NACH 
 
Payment pre-validation services – Guidelines 
Refer to Circular no. 023 dated March 19, 2020 on “Payment pre-validation services”, the 
stakeholder are hereby advised on the process to be followed for presenting the account 
validation records: 
1. On-boarding process: 
Non DBT - Real time:  
 
Initiating bank / Government departments to approach NPCI for creation for one time 
Non DBT entity identifier code (4 digit).  
 
Corporates can avail this service only through their sponsor bank. Sponsor bank 
should get in touch with NPCI to the entity identifier code. 
 
In-case initiating bank is raising the request on-behalf of government or corporate then 
separate code needs to be applied for each unique corporate or government 
department in the request sent. 
 
The format for raising request to NPCI for creation of code is provided in Annexure I. 
 
Non DBT - File based:  
 
Corporates or government department can participate through their sponsor bank only. 
 
For file based mode the sequence number in filename (6 digit unique number) should 
start with “8”.  
DBT - Real time:  
 
Government department on completion of certification process can get connected 
directly to NPCI or through their sponsor bank. 
 
A new entity identifier code (4 digit) to be taken from NPCI for the identification of the 
government department. The format for raising the request to NPCI for creation of code 
is provided in Annexure I. 
 
DBT - File based:  
 
Government department can participate through their sponsor bank only. 
 
For file based mode the sequence number in filename (6 digit unique number) should 
start with “9” whereas for OMC (LPG subsidy) validation the sequence number can 
start with any value between “0” to “7”. 
 
In addition, Government departments’ on-boarding directly to NPCI should submit 
sponsor bank authorization letter (Refer Annexure II for format) for collection of 
charges.

<!-- Page 2 -->

 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
2. Record processing: 
File based: 
 
LPG subsidy - No change in account validation process, format or naming convention. 
Input & response naming convention given below for reference. 
o Input 
 
Format: AV-<Initiating bank code>-<Receiving bank code> -<Initiating 
bank user ID>-<DDMMYYYY>-<6 digit Sequence number–should not 
start with “8”  or “9”>-INP.txt 
 
Example: AV-XXXX-OMCC-XXXXUSER1-02032020-000002-INP.txt 
o Response 
 
Format: AV-<Initiating bank code as received in input>-<Receiving 
bank code as received in input> -<Receiving bank user ID>-<Date as 
received in input>-<Sequence number as received in input>-RES.txt 
 
Example: 
AV-XXXX-OMCC-OMCCUSER1-02032020-000002-
RES.txt 
 
DBT (bank to bank) – No change in account validation process, format or naming 
convention. Input & response naming convention given below for reference. 
o Input 
 
Format: AV-<Initiating bank code>-<Receiving bank code> -<Initiating 
bank user ID>-<DDMMYYYY>-<6 digit Sequence number–should start 
with “9”>-INP.txt 
 
Example: AV-XXXX-YYYY-XXXXUSER1-02032020-900002-INP.txt 
o Response 
 
Format: AV-<Initiating bank code as received in input>-<Receiving 
bank code as received in input> -<Receiving bank user ID>-<Date as 
received in input>-<Sequence number as received in input>-RES.txt 
 
Example: AV-XXXX-YYYY-YYYYUSER1-02032020-900002-RES.txt 
 
 
Non DBT - Initiating bank based on request from the corporate or government 
department to initiate account validation file as per the existing format however naming 
convention will be different. Naming convention given below 
o Input 
 
Format: AV-<Initiating bank code>-<Receiving bank code> -<Initiating 
bank user ID>-<DDMMYYYY>-<6 digit Sequence number–should start 
with “8”>-INP.txt 
 
Example: AV-XXXX-YYYY-XXXXUSER1-02032020-800002-INP.txt 
o Response 
 
Format: AV-<Initiating bank code as received in input>-<Receiving 
bank code as received in input> -<Receiving bank user ID>-<Date as 
received in input>-<Sequence number as received in input>-RES.txt 
 
Example: AV-XXXX-YYYY-YYYYUSER1-02032020-800002-RES.txt

<!-- Page 3 -->

 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
 
Real time: 
 
Usage of entity identifier code in API request:  
i. 
Header of the JSON message  
ii. 
In xml under <Source type="CODE" value="XXXX" name="" /> 
Introduction of purpose field: 
The purpose of the request should be captured during the initiation of this service. The 
purpose codes allowed in provided in Annexure III. Any codes used which is not in the list 
will be rejected by NPCI system. 
This code will be used in <Request id="26062018" type="DETAILS_ENQ" refUrl=""/> in 
the xml request. 
Note: This is applicable for both “Validation of an account based on account number and 
IFSC” and “Request for an account holder name” API services. 
3. Introduction of additional reject reasons & account type 
 
i. 
New reason code in line with the transaction return codes have been introduced 
for reject response  
ii. 
New codes for new account types introduced 
The list of updated codes are provided in Annexure IV. 
Member banks are advised to take note and disseminate the information to all the concerned. 
For clarification, the same to be raised through CRM. 
 
With Warm Regards 
 
Giridhar. G. M 
(Chief – Offline product operations & technology)

<!-- Page 4 -->

 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
Annexure I 
 
(To be printed in sponsor bank letterhead) 
 
To,  
Chief – Offline product operations & technology, 
National Payments Corporation of India 
C/O ICICI Towers, 6th Floor,  
Tower I, North Wing, 
Plot No. 12, Financial District, Nanakram Guda,  
Hyderabad, Telangana 500032. 
 
 
Sub: Request for creation of Non-DBT code for prepayment validation service 
 
We _______________________ (bank name) participating in National Automated Clearing 
Cell (“NACH”) as a sponsor bank for _____________________________________ 
(Government 
department 
name 
/ 
Corporate 
name) 
with 
utility 
code 
_____________________, request NPCI to create Non-DBT code for participation in Non-DBT 
account validation service provided by NPCI. 
 
When using this service, we also ensure the following: 
1. Only valid API request received from the corporate or Government departments 
will be initiated to NPCI.  
2. Restrict the initiation of unwanted or false request.  
3. In-case of any incorrect request submission to NPCI, the same will be handled 
internally between the corporate and sponsor bank. 
 
 
 
 
 
 
(Signature of Authorized Signatory) 
 
(Name of the Authorized Signatories & designation with bank seal)

<!-- Page 5 -->

 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
Annexure II – Format of sponsor bank authorization letter 
 
(To be printed in sponsor bank letterhead) 
 
To,  
Chief – Offline product operations & technology, 
National Payments Corporation of India 
C/O ICICI Towers, 6th Floor,  
Tower I, North Wing, 
Plot No. 12, Financial District, Nanakram Guda,  
Hyderabad, Telangana 500032. 
 
 
Sub: Authorization for debiting charges from settlement account 
 
We _______________________(bank name) participating in National Automated Clearing 
Cell (“NACH”) as a sponsor bank for ____________________ (Government department 
name) hereby authorize NPCI to debit our settlement account maintained with RBI for 
records processed by the department with the code of _____ (4 digit code created by NPCI) 
through real time account validation service provided by NPCI. 
 
 
 
(Signature of Authorized Signatory) 
 
(Name of the Authorized Signatories & designation with bank seal)

<!-- Page 6 -->

 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
Annexure III 
 
Sl. No. Purpose 
Purpose code 
1 Customer on-boarding - loan 
CO01 
2 Customer on-boarding - Demat 
CO02 
3 Customer on-boarding - Brokerage/ SIP/ MF CO03 
4 Customer on-boarding - Subscriptions 
CO04 
5 Customer on-boarding - Others services 
CO05 
6 Vendor on-boarding 
VO01 
7 Mandate registration - Physical mandate 
MR01 
8 Mandate registration - eSign mandate 
MR02 
9 Mandate registration - API mandate 
MR03 
10 Payment pre-validation - Credit 
PP01 
11 Payment pre-validation - Debit 
PP02 
12 Payment pre-validation - Refund credit 
PP03 
13 DBT beneficiary on-boarding 
DB01 
14 DBT payment pre-validation 
DB02

<!-- Page 7 -->

 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
CIN: U74990MH2008NPL189067 
 
Annexure IV: 
Additional reject reasons  
Response Code 
Description 
Status 
S601 
Account is in open and active state 
Existing 
S602 
Account under litigation  
Existing 
S603 
A/c inactive 
Existing 
S604 
Dormant A/c 
Existing 
S605 
Account holder expired 
Existing 
S606 
A/c blocked or frozen 
Existing 
S607 
Customer insolvent / insane 
Existing 
S608 
Account Closed 
New code 
S609 
No such Account 
New code 
S610 
KYC Documents Pending 
New code 
S611 
Invalid IFSC code  
New code 
S612 
Network failure (CBS) 
New code 
S613 
A/c in Zero balance/No transactions have happened New code 
900 
PAN Number not linked to Account 
New code 
 
Account type for account status API 
Response Code 
Description 
Status 
T651 
Savings account 
Existing 
T652 
Current account 
Existing 
T653 
Cash credit account 
Existing 
T654  
Overdraft account 
Existing 
T699  
Others 
Existing 
T656 
FD 
New code 
T657 
RD 
New code 
T658 
Loan account 
New code 
T659 
PMJDY account 
New code 
T660 
NRE/NRO account 
New code 
T661 
HUF - Hindu Undivided family 
New code 
T662 
PF & PPF 
New code 
T663 
Basic Savings Bank Deposit (BSBD) New code
