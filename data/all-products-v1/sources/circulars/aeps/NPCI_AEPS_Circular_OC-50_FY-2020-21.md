# AePS | OC 50| FY 20 21 | AePS Best practices

Circular/reference number: NPCI/AePS/2020-21/001
Date: 5th June, 2020

<!-- Page 1 -->

 
 
 
 
        Page 1 of 5 
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
 
CIN: U74990MH2008NPL189067 
NPCI/AePS/2020-21/001          
 
 
 
 
 
 
  5th June, 2020 
 
To, 
All AePS Member Banks 
 
Madam / Dear Sir, 
 
Sub: i) Best Practices to reduce Technical Declines, ii) Best Practices on handling Customer complaints and 
iii) Steps to proactively identify and resolve the technical issues. 
 
This circular intends to explain the best practices and measures required to be taken in AePS ecosystem to 
reduce technical decline count and measures on handling Customer complaints. We also refer to our earlier 
circular number NPCI/2018-19/AePS/014 dated 6th March, 2019, under the subject “Best Practices to reduce 
Technical declines and Best Practices to reduce Biometric mismatch”. 
 
It may be noted that Reserve Bank of India (RBI) and Department of Financial Services (DFS) also take a note 
of AePS performance of all the member banks and NPCI. The benchmark of AePS technical declines is kept 
at less than 1%, which also includes technical declines due to scheduled activities and downtimes. 
To meet the above objective, we suggest banks to adopt the following best practices: 
 
Sr. No.  Proposal/Development 
For detailed process, refer 
1 
Best practices to be followed to reduce technical declines 
Annexure – I 
2 
Best practices to be followed on handling Customer complaints 
Annexure – II 
3 
Steps to proactively identify and resolve the technical issues 
Annexure – III 
 
All members are requested to take a note of the above and ensure to put in place processes to increase 
approval ratio and enhance customer experience.  
 
Yours faithfully, 
 
SD/- 
 
Saiprasad Nabar 
Chief – Online Products Operations 
 
Encl: Annexure-I, II &III

<!-- Page 2 -->

 
 
 
 
        Page 2 of 5 
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
 
CIN: U74990MH2008NPL189067 
Annexure - I 
 
Best Practices to be followed to reduce technical declines 
 
As per NPCI AePS Operating and Settlement Guideline banks are advised to undertake scheduled downtime 
activities only during non-peak hours ie. 00:00 hrs and 06:00 hrs. It improves the approval rate as most of 
the customer initiated AePS transactions are performed during day time.  
 
Further based on our experience and also after discussing with Member banks, we have identified below 
measures to reduce time-out scenarios to a large extent. Please find below such best practices to be followed 
by banks to reduce technical declines. 
 
As an Issuer Bank: 
 
 Capacity and Capability to handle 3x of existing peak volumes end to end. Existing peak volume needs 
to be reviewed on regular basis. 
 Minimum Hops between FI Switch and CBS. The AePS & its supporting infrasturce should operate 
from same DC (data center). 
 Additional ports to be configured between Bank FI switch and CBS based on the growth of the volume.  
 Multiple BGL accounts to resolve a/c lock status. 
 Multiple issuer Ports in round robin manner with NPCI. 
 Mapping of Response Codes as per NPCI specifications issued from time to time. 
 Analysis of declines due to Aadhaar not linked and frozen accounts and corrective actions to minimize 
such declines. 
 
As an Acquirer Bank: 
 
 Dedicated ports for issuer and Acquirer Transactions. 
 Additional servers and multiple ports to handle high volume 
 Generation of Online reversals instead of Credit Adjustments. 
 Analyze the reason of high U3 – Biometric mismatch declines has been the major contributor for 
declines in AePS.  Corrective action to be taken as per AePS Operating circular number NPCI/2018-
19/AePS/014 dated 6th March, 2019. 
 Timeout parameter of 65 seconds starts after transaction is sent to NPCI. The timeout parameter will 
be reviewed by NPCI from time to time and inform to member. 
 Analysing the reason of high online reversals and fix the issue to minimise the same. 
 Analysing the reason of decline due to format error & fix the issue.  
 
 
We have observed that technical declines have reduced substantially after implementing above suggested 
changes.

<!-- Page 3 -->

 
 
 
 
        Page 3 of 5 
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
 
CIN: U74990MH2008NPL189067 
 
Annexure-II 
 
Best practices to be followed on handling Customer complaints 
 
In view of the current lockdown/restriction imposed in the country and significant increase in volume due to 
DBT, we observe that there is considerable delay at Member Bank end in providing Reversal/credit to 
Customer Account for failed transactions. As a result we have observed various customer complaints, Police 
case on BC agents, abuse of BCs, complaints at bank branches etc. 
We request Member Banks as Issuer and Acquirer to initiate the additional Best Practices/measures enlisted 
herein below to ease the hardships of Customers and minimize the customer complaints: 
As an Issuer Bank: 
 
• 
Reversals of Failed/timed-out transaction on T+1 basis with simultaneous updation of DRC status in 
BCS system. 
• 
Crediting the Credit adjustment received to customer’s bank account on same day. 
• 
Robust Reconciliation process/system capable of handling the increase in volume. 
• 
SMS to customers for credit to accounts on a) Manual / Auto Reversals for failed transaction b) Credit 
for Credit Adjustment received.  
• 
Notification to branches and SMS to customers, for delays in reconciliation due to any issues. 
• 
Banks/branches/call centers to accept complaints lodged by Customers through various channels and 
direct these complaints to respective Teams for quicker resolution. Also a holding response to be sent 
to customers which includes expected timelines of resolution of complaint. 
 
 
As an Acquirer Bank: 
 
• 
Preferably introduce Centralised Complaint Management System for BCs to raise complaints. 
• 
Sharing the DRC status of Failed/timed-out cases to their respective BCs. 
• 
Raising of Credit adjustments (if any) on T+1 for transactions failed at Corporate BC/BC/Merchants 
due to time out/network issues between Acquiring Bank and BC partners/Merchants (these 
transactions will be successful at NPCI end).

<!-- Page 4 -->

 
 
 
 
        Page 4 of 5 
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
 
CIN: U74990MH2008NPL189067 
Annexure-III 
 
Steps to proactively identify and resolve the technical issues 
 
NPCI has done multiple exercises of capturing the PCAP logs with multiple banks. Based on our experience, 
please find below steps to be recommended to Member banks for timeout related issues and identifying the 
invalid response code cases: 
A. Steps to find out the timeout issue: 
i. 
The network switch is the entry point for the Bank after which there is Bank’s Firewall and 
then the Bank application.  
ii. 
When Bank has to enable a packet capture it is advisable to capture at NPCI network switch 
which is the entry point.  
iii. 
NPCI network team will provide the port details, wherein Bank network team can connect 
the laptop to capture the logs. 
iv. 
Bank can use wire-shark tool to capture the logs. 
v. 
This will help to diagnose the issue and if there is a delay observed / no response to NPCI 
request. In such scenarios, Bank has to check further where the packet is getting drop / 
which hop is taking more time.  
vi. 
At the same time NPCI will also take a capture at NPCI network so that end to end traffic can 
be analyzed. 
 
B. Bank Level Resolution of Invalid Response Code mapping: 
i. 
NPCI will decline the transactions as invalid Response code, if response code present in 
response message is not part of ISO Response Codes as per AePS online specifications. 
For example: Bank is responding with CBS response code or UIDAI response code, which is 
not part of ISO Response codes 
ii. 
Bank to check the cases of invalid response code through Raw Data file available in BCS 
portal of NPCI. 
iii. 
Bank to check the actual response code given to NPCI and check if same Response code is 
present in AePS Specifications or not. 
iv. 
If Not, Bank to make the correction in Response code provided to NPCI. 
v. 
If response code is present, the issue needs to be taken up with NPCI Monitoring/NFSHELP 
Team 
 
 
 
 
C. Invalid format received from Acquirer

<!-- Page 5 -->

 
 
 
 
        Page 5 of 5 
 
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051 
 
CIN: U74990MH2008NPL189067 
I. 
Acquirer will send transaction to the NPCI after following the AePS specification. After which 
NPCI will send the Issuer for authorisation.  
II. 
In case there is issue observed in any of the DE# (data element) the Issuer will decline the 
transaction with ISO 30 (invalid format). 
III. 
Acquirer has to check the transactions wherein incorrect DE# is sent and take corrective 
action. 
IV. 
Since the transaction is declined, the acquirer loses on the interchange as well as the customer 
is also not serviced. 
V. 
Details of the declines with RC 30 as acquirer is available on daily basis in the raw data which 
is shared with the Bank. 
 
D. Declines with RC 40 and RC 41 ( repeat reversal) 
i. 
In an event of time out at NPCI end, NPCI will generate reversal and send it to Issuer. Issuer 
Bank has to acknowledge the reversal request and process the credit to the Customer. 
ii. 
If Issuer is not acknowledging the reversal request, NPCI will send repeat reversal to the Issuer. 
iii. 
After sending repeat reversal, if Issuer Bank is not responding to such request than the 
transaction will be declined with RC 40 (Reversal by NPCI not acknowledged by ISSUER) 
iv. 
Similarly any reversal sent from Acquirer, Issuer has to acknowledge and send response. If 
Issuer does not send respond, then NPCI will send repeat reversal to the Issuer. 
v. 
After sending repeat reversal, if Issuer Bank is not responding to such request than the 
transaction will be declined with RC 41 (Reversal by ACQUIRER not acknowledged by ISSUER) 
vi. 
Issuer has to check the reasons for not responding to the reversal request and check the cases 
of RC 40 and RC 41 from the raw data which is shared with Bank on daily basis
