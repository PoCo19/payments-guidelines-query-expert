# OC149 A - Addendum to OC 149 - Reduction of business declines in UPI

Circular/reference number: OC-149A

<!-- Page 1 -->

 
NPCI/UPI/OC No. 149A/2022-23 
 
 
 
 
 
 
June 15, 2022 
 
To, 
 
All members of Unified Payments Interface (UPI)  
 
Madam / Dear Sir, 
 
Subject: Addendum to OC 149 - Reduction of business declines in UPI. 
 
This is with reference to our earlier Operating Circular (OC) 149 dated May 13, 2022, copy 
attached herewith, wherein we have communicated UPI members to work towards reducing the 
Technical Declines (TD) to below 1% and Business Declines (BD) to below 5%.  
 
Also, it was informed vide OC 149 that RBI has directed NPCI to advise banks to run customer 
literacy campaign, especially where BD is more than 10%. 
 
In view thereof, we request UPI member banks to provide a brief update to NPCI on all such 
literacy programs / campaign conducted from their side. 
 
Please make a note of the above and disseminate the information contained herein to the 
officials concerned. For any queries or clarification, please contact following officials: 
Name 
E-mail 
Contact Number 
Rumana Shaikh 
rumana.shaikh@npci.org.in 
9702266853 
Sonam Kandu 
sonam.kandu@npci.org.in 
8169658404 
Pankaj Samarth 
pankaj.samarth@npci.org.in 
8108122861 
 
Yours Sincerely, 
 
 
 
Saiprasad Nabar 
Chief – Online Product Operations and Technology

<!-- Page 2 -->

NPCI/UPI/OC No. 149/2022-23 
 
 
 
 
 
May 13, 2022 
 
To, 
 
All Member Banks  
 
Madam / Dear Sir, 
 
Subject:  Reduction of business declines in UPI 
 
UPI has become a popular mode of payment in the country. With increase in volumes, it is also 
essential that all ecosystem players should work towards minimizing the declines i.e. Technical 
declines and Business declines for seamless customer experience. RBI has advised NPCI to work 
towards reducing Technical Declines (TD) to below 1% and Business Declines (BD) to below 5%. 
Also RBI directed to advise all banks with BD more than 10% to take up targeted literacy 
campaigns amongst their customers. 
 
In order to work on business declines, banks are required to bifurcate such declines into customer 
induced declines and bank induced declines. Bank induced declines can be minimized, by 
analyzing and taking corrective action at respective Bank end. In view thereof, it is essential for 
member banks to analyse the business declines, take corrective actions and also run customer 
literacy campaigns, especially where business declines are more than 10%.  The sample list of 
business decline response codes for UPI along with suggested actions are provided in Annexure.  
 
Member Banks are hereby advised to make a note of the above and do the needful. 
 
 
Yours Sincerely, 
 
 
 
Saiprasad Nabar 
Chief – Online Product Operations and Technology

<!-- Page 3 -->

Annexure 
 
UPI Decline Codes 
 
UPI Decline 
Response 
Code 
Description of Decline 
Response Code 
Type of 
Declines 
To be checked 
by 
Suggested Actions 
Z7 
TRANSACTION FREQUENCY 
LIMIT EXCEEDED AS SET BY  
REMITTING MEMBER 
Bank 
Induced 
Remitter Bank,  
Payer PSP 
1.  Analyse the reason of decline. If it is on 
account of wrong mapping of response 
code, correct the mapping. 
2.       Bank to review the limits. If required, 
revise the limit. 
3.       Bank to send communication via SMS 
to customers regarding the Limit. 
4.       Payer PSP to give Pop up message for 
checking Transaction limit.  
Z8 
PER TRANSACTION LIMIT 
EXCEEDED AS SET BY 
REMITTING MEMBER 
Bank 
Induced 
Remitter Bank,  
Payer PSP 
1.       Analyse the reason of decline. If it is on 
account of wrong mapping of response 
code, correct the mapping. 
2.       Bank to review the limits. If required, 
revise the limit. 
3.       Bank to send communication via SMS 
to customers regarding the Limit. 
4.       Payer PSP to give Pop up message for 
checking Transaction limit.  
U03 
Bank NDC Limit Exceeded 
Bank 
Induced  
Remitter Bank 
Bank to  review and revise the NDC (Net 
Debit Cap) assigned. 
NU 
Unable to notify the 
Customer 
Bank 
Induced 
Payee PSP 
For AutoPay, Payee PSP to ensure that they 
initiate 
Pre-debit 
Notification 
API 
(ReqValCust) prior 24hrs of the subsequent 
execution and for the cases wherein 1st 
execution is not happening on the same day 
of mandate creation.
