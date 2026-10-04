# IMPS I OC 95 I FY 20-21 I Implementation Guidelines for IMPSv3.5

Circular/reference number: OC-95I
Date: 15th November 2020

<!-- Page 1 -->

 
1001A, The Capital, B Wing, 10th Floor, 
BandraKurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101 
contact@npci.org.inwww.npci.org.in 
CIN: U74990MH2008NPL189067 
 
 
 
 
 
                     
  
          
NPCI/IMPS/OC No. 95/2020-21 
 
 
 
 
 
September 18, 2020 
 
To, 
All Members of IMPS 
Madam/ Dear Sir, 
Sub: Implementation Guidelines for IMPSv3.5 
NPCI has introduced 2 new features in IMPS with the revised  Online Technical Specifications 
version 3.5. Both these features are non-financial transactions catering to the industry 
requirement and facilitating various business needs. 
 
A. 
The 2 new enhancements in IMPS include the following: 
1.) Check Status: 
This is a non-financial transaction type introduced to address the challenges with respect to 
Deemed approved Transactions in IMPS. This will enable the providers to fetch the latest 
status of the transaction. The implementation shall improve the customer experience and 
thereby minimize customer complaints. 
2.) Name Inquiry:  
The non-financial transaction enables Remitter Bank to validate the beneficiary name on the 
basis of IFSC Code + Account Number (for P2A) and MMID (for P2P). This feature of beneficiary 
verification shall enable many business use-cases.  
Banks are directed to use this service only when a subsequent financial transaction has to be 
initiated in IMPS. 
 
B. 
Additionally, Banks must populate the requisite MCCs for Corporate transactions (Refer 
IMPS OC 94).  
The technical specifications & process flow for the above mentioned three functionalities is 
attached in Annexure I & II.

<!-- Page 2 -->

 
1001A, The Capital, B Wing, 10th Floor, 
BandraKurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101 
contact@npci.org.inwww.npci.org.in 
CIN: U74990MH2008NPL189067 
 
 
 
All member banks are requested to implement all above mentioned three enhancements by 
15th November 2020. Banks are required to implement the above both as a Remitter and 
Beneficiary with due certification from NPCI before going live with these functionalities. 
 
Yours Sincerely, 
SD/- 
Praveena Rai 
Chief Operating officer

<!-- Page 3 -->

 
1001A, The Capital, B Wing, 10th Floor, 
BandraKurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101 
contact@npci.org.inwww.npci.org.in 
CIN: U74990MH2008NPL189067 
 
 
 
 
Annexure I 
 
 
Annexure II 
Process flow for the functionalities are as below: 
Check Status:   
• Check Status allows banks to fetch the latest status of a DEEMED APPROVED Transaction. 
• Remitter Bank initiates “Check Status” from its end. 
• Based on the transaction type, NPCI will look for status of transaction in its logs. If NPCI has 
the response from the beneficiary, NPCI will forward the response to Remitter stating 
transaction status. 
• If NPCI does not have a status of the transaction in its logs, NPCI will forward the Check 
status request to the Beneficiary.  
• Beneficiary will check the transaction details and sends a response. NPCI will forward the 
response to remitter bank. 
• Check Status will fetch status of transactions for the ongoing settlement cycle only. 
• Remitter bank is required to drop the “Check Status” transaction at its end, if the customer 
requests the status of the transaction occurred in any other cycle than the current cycle. 
 
Name Inquiry:  
 
• Remitter Bank initiates a Name Inquiry transaction. 
• NPCI receives the request and forwards the request to the intended Beneficiary bank. 
• Beneficiary Bank responds with Beneficiary Name. 
• Name Inquiry initiated with high velocity (for Corporates) should also carry 
MCC:4512/4513 in DE-18. 
• Retail Consumer should have a separate section across channels to perform Name Inquiry 
with the further capability/option of saving the same as beneficiary, if needed. 
• Initiator (Remitter bank) should have the customer consent to initiate name inquiry and 
verify his CBS name.
