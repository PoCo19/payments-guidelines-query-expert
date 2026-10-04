# Circular 45 - UPI OC 45 – Solution to reduce Deemed Transactions

Circular/reference number: OC-45

<!-- Page 1 -->

1 
 
NPCI/ UPI/OC No.  45 /2017 – 18 
 
 
 
 
                       12th Feb, 2018 
 
To, 
 
 
 
 
 
 
 
 
 
 
 
 
 
All Members of Unified Payments Interface (UPI) 
 
 
Dear Sir / Madam, 
 
 
Subject: 1) Implementation of new response/error codes 
                2) Best practices to reduce - ‘Deemed approved’ transactions, ‘Unsuccessful debit              
                     Reversals’ and ‘overall declines’ 
 
Objective: Objective of this circular is to explain the process to reduce deemed approved & debit 
time out transactions (requiring DRC from Member banks) in UPI. This shall help to reduce 
operational work, avoid customer complaints and enhance positive user experience. 
 
To meet the above objective, we propose following changes: 
 
Other key requirements: 
 
1. Robust Infrastructure 
 
You are all aware that UPI volumes are growing significantly day by day. Thus, with the increase 
in volumes, if the infrastructure (switching capacity, network bandwidth & servers/DB capacity 
etc.) is not resized on time, then the volume of decline & deemed approved transactions will 
increase. 
 
Hence, to mitigate the above issue, it is proposed that all UPI members are required to check the 
system capacity (switching capacity, network bandwidth & servers/DB capacity, application 
capacity etc.) and resize the same immediately when the need arises. Please ensure that your 
systems i.e. Production (PR), High Availability (HA)/Backup system & Disaster Recovery (DR) 
systems are in sync and DR should be ready so as to invoke in case of any issue in 
Production/Primary or HA systems.   
Sr. No 
Proposal/Developments 
For detailed process 
refer- 
1 
Implementation of new response code RC-CS for CRR (Credit 
Reversal Request) 
Annexure A 
2 
New decline response codes for I/O (Input/Output) error 
Annexure B 
3 
New error codes for acknowledgement (ACK) not received for 
non-financial transactions 
Annexure C 
4 
Execution of VR/CT between beneficiary switch and 
CBS (VR- Verification Request / CT- Check Transactions) 
Annexure D

<!-- Page 2 -->

2 
 
 
2. Minimum hops between beneficiary switch & CBS 
 
It is advised that all members should have minimum hops between beneficiary switch and CBS so 
that the request & response messages reach to the source & destination within the TAT and helps 
in avoiding declined /deemed approved transactions. 
 
All members are requested to take a note of the above and required to put in place proper 
processes so as to reduce the declines & deemed approved transactions which will increases 
approval ratios.  
Kindly disseminate the information contained herein to the officials concerned. 
For any clarification, please contact the following officials:- 
Name 
Email Id 
Contact Number 
Rosa Bagul (Operations) 
rosa.bagul@npci.org.in  
07738180884 
Prabhat Sharma (Product) 
prabhat.sharma@npci.org.in  
07045958824 
UPI Help Desk 
upi.helpdesk@npci.org.in 
040-6729 9417 
 
 
Yours faithfully, 
 
Ram Sundaresan 
SVP & Head – Operations

<!-- Page 3 -->

3 
 
ANNEXURE – A 
 
1. Implementation of new Response Code (RC) – CS for CRR (Credit Reversal Request) 
 
1.1) 
Existing Process:  
 
Once the debit authorisation is success, NPCI sends credit request message to beneficiary bank. 
If NPCI does not get any response from Beneficiary bank, then NPCI will initiate up to 3 Check 
Transaction (CT) messages to seek the status of the original transaction (Approved/Declined). If 
NPCI does not get any response even after 3 CT messages, then NPCI will initiate CRR - Credit 
Reversal Request Message. 
 
In case NPCI receives the response from Beneficiary bank in any of 3 CT messages, depending 
on response, NPCI will stop generating further CT messages and will treat transactions as 
“Approved” or “Declined” based on the response received. 
 
On receiving CRR beneficiary banks are expected to check the status in CBS and initiate actions as 
follows: 
 
 
 
In the above flow, the transaction will be treated as declined transaction and debit reversal will 
be generated. In the above scenario the below response for credit reversal will be accepted: 
1) NC – No credit given 
2) OC – Original credit request not found 
3) 00 – Reversal Successful 
4) 96 – Reversal declined 
 
Note: 
 
For all the above cases (except for RC 96) a decline response will be updated in Raw File 
as per the response received from the remitting bank for debit reversal request message 
(E.g. RR, UR, RS, UP, R9, S9). 
 
Where the Response Code 96 is received for Credit Reversal Request (CRR) or no 
response is received on time, response code ‘RB’ will be updated in Raw File and 
transaction will be treated as “Deemed Approved”.

<!-- Page 4 -->

4 
 
 
 
1.2) 
Proposed Process:  
 
 
 
 
If NPCI receives the response from Beneficiary bank in any of 3 CT messages, depending on 
response, NPCI will stop generating further CT messages and will treat transactions as 
“Approved” or “Declined” based on the response received. 
 
In the above flow, the transaction will be treated as success when beneficiary bank will send an 
online response to NPCI as approved i.e. RC – CS (Credit Success) for CRR. 
 
Thus, instead of making an approved transaction into decline, NPCI proposes to make it approved 
by implementing new response code RC-CS. Bank has to provide the approval number in the 
response to CRR. Please note approval number is mandatory. 
  
All members of UPI are requested to build the aforesaid condition and implement the new RC-CS 
in your switch. This will help in reducing the timed-out and declined transactions and also help in 
increasing the approval ratio. NPCI will move the new Response Code - CS in production system 
by Feb 15, 2018.  Banks should get this change certified with NPCI before moving the patch in 
production system.   
 
For the banks who are not implementing the new Response code CS, the existing process will 
continue. 
 
NOTE: Response Code CS is only an online code. This is not updated in Raw File. Raw File shall 
be updated as approved i.e. RC-00 if beneficiary sends online response message with response 
code as RC-CS.

<!-- Page 5 -->

5 
 
ANNEXURE – B 
 
2. Decline response code for I/O (Input/Output) Error 
 
(Input/Output) error definition: 
UPI sends a Debit/Credit request message to banks (i.e. remitter/beneficiary as the case 
may be) and if there is any connection timeout issue while posting this request message, 
UPI switch has the ability to flag the status as message is not received by the destination 
bank due to any reason. 
 
Existing Process 
In the existing process, if there is connection timeout issue for debit request sent to 
remitter bank, UPI switch is sending the Check Transaction Request (up to 3 times) and 
Debit Reversal Request to the remitting bank. Same is the case for the Credit Request 
scenario, UPI switch is sending Check Transaction Request (up to 3 times) and Credit 
Reversal Request to the beneficiary bank. 
 
Proposed Process: 
In the proposed process, UPI switch will consider the connection timeout as decline 
transaction and will not initiate check transactions request messages and Debit/Credit 
reversal request messages as this will help banks in reducing operational work. 
  
Note: Error codes will be sent in online mode and response code will be updated in raw 
data. NPCI will move the new RC for I/O error in production system by Feb 15, 2018. 
 
Action at Bank end: While NPCI is updating new response codes to avoid offline issues, it 
is expected of member banks to ensure proper connectivity is established; switch should 
read and respond to all the connectivity messages so that most of the transactions will 
get approved instead of decline due to connectivity issue. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Sr. 
No. 
Error 
Code 
(Online 
Code) 
Response Code 
(Raw File) 
Description 
Leg 
(Debit/
Credit) 
Status as 
per 
existing 
scenario 
Status of 
Transaction 
(Proposed) 
1 
U85 
 01 
Connection 
Timeout 
in 
ReqPayDebit 
Debit 
Debit 
timeout 
Decline 
2 
U88 
RR/UR/R9/U9 
Connection 
Timeout 
in 
ReqPayCredit 
Credit 
Deemed 
Approved 
Decline

<!-- Page 6 -->

6 
 
ANNEXURE – C 
 
 
3. New Error Codes for Acknowledgement(ACK) not received for Non-Financial transactions 
 
At present UPI sends error code U13 for ACK not received or ACK is invalid. NPCI will add below 
error codes for Meta/non-financial transactions to bring more clarity on reason of decline.  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Sr. No 
Error Codes 
Scenarios & Description of the Error Codes 
1 
U97 
Message level ack not given by Bank for non-financial txn 
2 
U98 
Null ACK received by UPI for non-financial Transaction 
3 
U99 
Negative ACK received by UPI for non-financial Transaction 
4 
A15 
REQ ACK Not Received

<!-- Page 7 -->

7 
 
 
ANNEXURE – D 
 
4. Execution of VR/CT between Beneficiary switch & CBS (VR – Verification Request / CT – 
Check Transaction) 
 
4.1) 
Existing Process: 
When UPI switch sends a credit request message to beneficiary switch, it will forward 
the same to CBS and wait up to 29 seconds or time defined by the banks (as the 
response time to NPCI is 30 seconds). If there is no response received from CBS within 
that time then beneficiary switch will send response time out status to UPI switch. 
Same is the case for check transaction (CT) and credit reversal request (CRR) messages 
being sent by NPCI to beneficiary switch. 
 
TAT for credit leg messages are as follows, Original Request – 30 Seconds, CT-1, 2 & 3 
– 30 Seconds (each CT TAT is 10 seconds) and CRR TAT – 30 Seconds, total TAT is 90 
seconds. 
 
4.2) 
Proposed Process: 
The beneficiary bank should initiate VR/CT to CBS every 5 seconds to seek the status 
of the transaction (whether approved or declined) instead of waiting for 29 seconds. 
Similar process should be put in place for check transaction message and credit 
reversal request messages being sent by NPCI. 
 
This solution will help in reducing the deemed approved transactions significantly, 
which occurs due to intermittent network fluctuations or for any other reason.
