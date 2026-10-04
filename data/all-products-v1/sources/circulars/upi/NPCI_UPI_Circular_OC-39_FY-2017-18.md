# Circular 39 - Efficient implementations for merchant on-boarding on UPI

Circular/reference number: OC-39

<!-- Page 1 -->

NPCI /UPI/OC No. 39/2017-18  
 
 
 
                                           Date: 20th Nov, 2017 
To, 
All Member of UPI – Unified Payments Interface 
Subject: UPI - Efficient implementations for merchant on-boarding on UPI  
 
A) Objective  
 
Objective of this circular is to explain the existing and proposed process to handle merchant transactions 
in UPI where merchant Acquiring PSP and merchant bank is same. The proposed process shall help in 
handling of deemed approved transactions and confirmation to merchants for certainty in rendering of 
goods/services to the customers. 
 
B) Process for handling the merchant transactions which are declined/deemed approved 
 
Existing Process: 
NPCI sends a credit request message to merchant bank and the merchant bank either send a decline 
response or the transaction response from merchant bank to NPCI may timeout, if merchant bank switch 
is not able to process the request message to CBS (due to any reason) or CBS is not responding with status. 
In such case, merchant PSP is forwarding the same declined/ deemed approved response to the merchant. 
Thus, merchant unable to provide the goods/services due to the customer due to decline/deemed 
approved status.   
     Proposed Process: 
If merchant bank & merchant Acquiring PSP is same, merchant bank should send approved response (RC-
00) to NPCI (in the following scenarios) and NPCI shall forward the same approved response to the 
merchant PSP; 
i) 
Merchant bank switch is not able to process the request message to CBS (due to any reason)  
ii) 
CBS is not responding (with status) to merchant bank switch. 
Merchant banks should ensure to reconcile all such transactions and pass credit to the merchant’s account if 
online credit is unsuccessful.  Thus, the proposed process will help in reducing grievances/ customer 
complaints arising due to decline/deemed approved transactions and increase the customer’s user 
experience. 
C) Check transaction status enablement for merchants:  
 
Existing Process:  
Merchant PSPs are initiating check transaction messages to NPCI UPI switch if the transaction status is 
unknown (due to response time out) and updating the status at PSP end as approved, decline or deemed 
approved as the case may be.  However, the status received for such check transaction message is not 
being sent to the merchants. Merchants are therefore unable to get the online status of the transactions, 
which is very essential for merchants to handle the customer complaints. 
Proposed Process:

<!-- Page 2 -->

i) 
Whenever merchant PSPs gets time out response, it is advised that merchant PSPs initiate online 
check transaction message with NPCI UPI switch and update the status in online (status can be 
approved, declined or deemed approved). 
ii) 
Merchant PSPs should update the same status to the merchants in online through API call. 
iii) 
Merchants should update the status to the respective customers. 
iv) 
API call is applicable for both online / offline Acquiring scenario.  
 
Thus, the proposed process shall hep the merchants in providing the status of the transaction to their 
customers instantly in online mode.  
All member banks currently acquiring merchants for UPI payments are requested to make the 
suggested developments and process changes latest by 15th Dec’17. Kindly disseminate the information 
contained herein to the officials concerned. 
Thanking you and looking forward to your continued support. 
Yours faithfully, 
 
 
Dilip Asbe 
Chief Operating Officer
