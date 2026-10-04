# Circular 17- UPI, a Compliance for successful Debit reversals b. Handling deemed approved transactions and reconciliation

Circular/reference number: OC-17
Date: 25th August, 2016

<!-- Page 1 -->

 
NPCI /UPI/OC No.17 /2016-17 
 
 
 
 
 
          March 9, 2017 
 
To, 
All Member Banks - Unified Payments Interface (UPI) 
  
Dear Sir/Madam, 
 
Subject: UPI –  
a. Compliance for successful Debit reversals  
b. Handling deemed approved transactions and reconciliation 
 
NPCI launched UPI on 25th August, 2016 and presently, 44 banks are live on UPI with 33 banks’ 
PSP Apps live on Play Store. With the ever increasing transaction volume and high 
publicity/visibility/awareness created for UPI coupled with large no. of customers using UPI, it 
becomes incumbent upon all participants to live up to customers’ expectations and make 
available high quality customer service.  
 
We have observed that non-processing of online debit reversal for declined transactions by the 
Remitter banks has led to increase in customer complaints.  Such complaints also leads to wide 
negative publicity of UPI as a Product. The issue of the customer not getting the amount 
reversed online for a declined transactions and resultant high complaints was also discussed 
and deliberated in the recent Steering Committee Meeting held on 13th February 2017.  
 
Further to our deliberations and analysis done jointly with member banks, we wish to inform 
that we have implemented 4 additional test cases to handle debit reversal failure/timeouts.  
We are also introducing a new response code for proper identification/understanding of 
declined transactions. The details are given in Annexure I.  Banks are requested to ensure strict 
Compliance thereof. 
 
Handling deemed approved transactions and reconciliation 
 
We refer operating circulars NPCI/UPI/OC No. 04/2016 – 17 & NPCI/UPI/OC No. 09/2016 – 17 & 
NPCI/UPI & IMPS/OC No. 79/2016-2017 wherein we have informed that all UPI member banks 
are expected to perform reconciliation on daily basis.  Our enquiries reveal that many banks 
are not having a process for daily reconciliation. If reconciliation is not done daily and any loss 
occurs due to technical issue and cannot be identified, it may lead to huge loss. 
 
We request to follow the process described in Annexure II to avoid customer’s complaints and 
any financial loss which may occur due to technical issues.  
 
All member banks should send us an undertaking informing that the Bank is performing daily 
reconciliation.  This undertaking should be signed by an official of the rank of General Manager 
or equivalent duly endorsed by the Audit Department of the Bank on or before 31st March 2017.

<!-- Page 2 -->

 
 
Should you need any further clarification, please contact the following officials:- 
 
Name 
E-mail ID 
Contact No 
Shivani Saxena 
Shivani.saxena@npci.org.in 
07506446567 
Soumyajit Roy 
soumyajit.roy@npci.org.in 
08879754970 
Rama Raju 
rama.raju@npci.org.in 
08108122895 
 
Yours faithfully, 
 
 
Dilip Asbe 
Chief Operating Officer

<!-- Page 3 -->

 
Annexure I 
 
1. Implementation of 4 additional reversal test cases: Presently the test cases includes 
only success and failure transactions.  We have created 4 additional test cases to include 
the scenarios of debit reversal failures/timeouts with store and forward facility at the 
bank’s end, in case their CBS is down/not responding for debit reversal advise. Our team 
will get in touch with all the banks and get the certification completed urgently.  
 
 
2. Addition of a New Response Code: We have introduced a new response code “ND” so 
that the reason for decline is properly identified: 
 
 
RC 
Abbreviation 
Description 
ND 
Debit reversal is declined as 
account has not been debited 
for original transaction. 
When a transaction is timed out in debit leg and 
reversal is generated on remitter bank, in such a case, 
the remitter bank should decline the reversal request 
with 'ND' if it has not debited the customer account.

<!-- Page 4 -->

 
 
 
Annexure II 
 
1. Reconciliation 
1.1 Three way reconciliation – (by bank as both remitter and beneficiary) 
 
We request to extract feed file from NPCI, your switch & CBS and perform three way 
reconciliation for all UPI transactions on daily basis. 
Note: Please match all approved & decline transactions (which includes Pay, Collect & 
Merchant transactions), reconcile all entries and exceptions should be properly handled.  
Bank has also to maintain proper records for reference and for responding to the 
complaints & queries of customers. 
 
1.2 Decline Transactions (bank as remitter) 
 
After reconciling the UPI transactions, please see if the customer account is not reversed 
in online for any unsuccessful transaction then the same has to be reversed manually or 
vice a versa.  
 
1.3 Approved Transactions (bank as remitter) 
 
For approved (merchant)/deemed approved transactions, raise chargeback only in case 
of customer complaints provided beneficiary bank has not raised TCC (102/103, as the 
case may be) or have not returned the funds. 
 
2. Reconciliation for Deemed Approved (DA) Transactions  
 
2.1 Reconciliation process for Deemed Approved transactions by Beneficiary Bank 
 
Download DA transactions daily from the RGCS application after every settlement 
cycle.  
 
Reconciliation has to be performed immediately after each settlement cycle. 
 
Raise Transaction Credit Confirmation (TCC) immediately if credited online or 
manually. 
 
Credit to customer account without any delay if not already credited. 
 
Raise Returns (RET) immediately if the bank is not able to credit the beneficiary 
customer account due to any reason whatsoever. 
 
2.2 Reconciliation process for Deemed Approved transactions by Remitter Bank  
 
Download DA transactions on daily basis from the RGCS application after every 
settlement cycle.  
 
Reconciliation has to be performed immediately after each settlement cycle. 
 
Download the dispute report daily containing Transaction Credit Confirmation 
(TCC) and Return (RET) to track time out transactions. 
 
After receiving the return (RET) from the beneficiary bank amount should be 
returned to the respective the remitting customers.

<!-- Page 5 -->

 
 
3. Handling Adjustment  
 
Members should download all adjustments raised by other banks from RGCS, check the 
status of those transactions and initiate suitable actions either by accepting or rejecting 
the adjustments within TAT.  
 
3.1 Credit Adjustments/Refunds for Merchant transactions 
 
All banks as remitter should download the credit adjustments/refunds raised by the 
acquiring bank for the merchant based transactions and reverse the customer’s account 
immediately after each cycle. 
 
 
3.2 Returns for Deemed approved Transactions 
 
Returns raised by other banks for deemed approved transactions has to be downloaded 
on daily basis and reversed to the customer’s account on same day so as to avoid any 
complaints. 
 
3.3 Download files from RGCS on daily basis 
 
Ensure to download all settlement files, adjustment reports, DSR, service tax reports 
etc. and maintain the records for reconciliation and future reference. 
 
4. Reconciliation of GL accounts for each settlement cycle 
 
4.1 Payable Account  
 
Reconcile all UPI transactions, initiate suitable actions and ensure that the payable GL 
a/c is reconciled daily.    
 
 
4.2 Receivable Account 
 
Reconcile all UPI transactions, initiate suitable actions and ensure the receivable GL A/c 
is reconciled daily. 
 
5. UPI App – Complaints 
 
5.1 Raise Complaints 
 
All UPI member banks are expected to download complaints raised by customers using 
your UPI app and upload the same in RGCS.  Download the response (to the complaints) 
file from RGCS on daily basis and upload the same in your UPI APP so that customers can 
view the status of their complaints on their mobile UPI app.

<!-- Page 6 -->

 
5.2 Respond to the complaints 
 
Download complaints raised by other UPI members on your bank as remitter or 
beneficiary. Verify the status of the complaints, initiate suitable actions (if required) 
and respond to the complaints with status using appropriate reason codes in RGCS on 
daily basis. 
 
        Note: Please refer Complaint Management Process V1.0 for details. 
 
6. Automated Recon Process & Dedicated Operations Team  
 
6.1 Automated Recon Process 
 
We recommend that the reconciliation process should be automated at the earliest so 
that large volume of transactions can be handled.   
 
6.2 Dedicated Team 
 
We would also like to highlight importance of having a dedicated team to handle UPI 
day to day operations such as reconciling the UPI transactions, handling customer 
complaints, etc. The point of contact (SPOC) should be communicated to NPCI support 
contacts mentioned by email.
