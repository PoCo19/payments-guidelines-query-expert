# Circular 38 - UPI - RRC Refund/Return Reversal Confirmation

Circular/reference number: OC-38
Date: 12th May 2017

<!-- Page 1 -->

NPCI/ UPI/OC No. 38/2017 – 18 
 
 
 
                                        01st Nov, 2017 
 
To, 
 
 
 
 
 
 
 
 
 
 
 
All Members of Unified Payments Interface (UPI) 
 
Dear Sir / Madam, 
 
Sub: UPI – RRC “Refund/Return Reversal Confirmation” 
 
Objective: Objective of this circular is to explain handling and controls to be built for credit 
adjustments/returns by the customer banks.  
 
We have observed that Remitting/issuing banks are not reversing their customer’s account 
even after receiving the credit adjustments / returns from beneficiary/acquiring banks. In 
such case, customers are getting out of fund for many day and further those transactions are 
resulting in customer complaints. This matter has been deliberated in the UPI Steering 
Committee Meeting (SCM) held on 12th May 2017. After detailed deliberation, SCM has 
approved implementing the below defined process i.e. “Refund/Return Reversal 
Confirmation – RRC” in RGCS for credit adjustments & returns by the customer banks. 
 
Process:  
 
Customer banks (Remitting/Issuing Banks should download all the credit adjustments 
(received for approved transactions) & returns (received for deemed approved transactions) 
which are raised by the beneficiary/acquiring banks in RGCS on T+1 working day and initiate 
credits to the respective customers in CBS. Please check and ensure there is a debit present 
in CBS before processing the reversal credit to the customer account. 
 
Once the reversals are successfully processed in CBS, only then the customer banks should 
confirm the status in RGCS with status as RRC adjustment flag and reason code 501 (please 
refer below RRC rules table for more details). 
 
The aforesaid process will help in getting the funds in to the customer’s account latest by T+2 
working day and thereby result in reduction of customer complaints. 
 
Penalty: The aforesaid issues were discussed and penalty of Rs.25 + GST for any aberration to 
the above process was approved by SCM in the meeting held on 12-05-2017. 
 
Applicability: The above penalty is applicable for UPI approved & deemed approved 
transactions (Pay, Collect & Merchant transactions).

<!-- Page 2 -->

 
RRC Rules: 
Description 
Remarks 
Adjustment Type 
RRC - Refund Reversal Confirmation 
RRC is allowed on  
Credit Adjustment & Returns ( i.e. RC-00 & RB TXNs) 
Applicable for  (Txn – Types) 
UC-UU-U3 & U2 
Who will raise RRC 
 Issuing Bank – For U2 
 Remitting bank - For UC-UU & U3 TXNs 
Who will receive RRC 
 Acquiring (Merchant Bank) -For U2 TXNs 
 Beneficiary Bank -For UC-UU & U3 TXNs 
 PSPs – For all TXNs 
 NPCI – For all TXNs 
TAT for raising RRC 
Adjustment raised date (A) : A+1 working day 
Fund Movement 
Non- Financial (This is only acknowledgement) 
Adjustment Flag for front end /bulk 
upload 
RRC 
Reason Codes 
501 
Penalty  (If RRC is not updated by the 
Remitting/issuing bank in RGCS on A+1 
working day) 
Rs.25 + GST 
Penalty Movement 
 Issuing Bank to Acquiring Bank (For Merchant 
TXNs – U2) 
 Remitting bank to Beneficiary bank (for Pay & 
Collect TXNs UC,UU & U3 ) 
Response code allowed on 
RC-00 & RB 
Applicable for TXN -Types 
UC-UU-U3 & U2 
Bulk Upload format 
Same as existing .CSV file format of TCC/ RET (please 
use appropriate adjustment flag & reason code for 
raising RRC) 
 
Effective Date: The penalty, as aforesaid, will be implemented with effect from 20th Nov., 
2017. 
All members are requested to take a note of the above and ensure to put in place proper 
process so as to ensure compliance to NPCI guidelines of handling credit adjustments & 
returns. Kindly disseminate the information contained herein to the officials concerned. 
For any further clarification please contact the following official:- 
Name 
Email Id 
Contact Number 
Rosa Bagul 
rosa.bagul@npci.org.in 
07738180884 
Achinto B 
achinto.bupadhyay@npci.org.in  
09477112085 
Neha Kumari 
neha.kumari@npci.org.in 
09167852531 
 
 
Yours faithfully,
