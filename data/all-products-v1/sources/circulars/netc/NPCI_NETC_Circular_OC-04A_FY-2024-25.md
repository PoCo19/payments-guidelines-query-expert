# NETC | OC 04A | FY 24-25 | Changes to the rule for declining transactions from tags in exception.

Circular/reference number: NPCI/2024-25/NETC/004A

<!-- Page 1 -->

NPCI/2024-25/NETC/004A       
 
 
 
 
 
 January 28, 2025 
To, 
All Members of NETC 
 
Subject: Addendum to Circular 004 – Changes to the rule for declining transactions 
from tags under exception 
Reference may be taken from our circular no 004 dated October 16, 2024, on changes to the 
rule for declining transactions from tags under exception. Based on the feedback from the 
stakeholders it has been decided to modify the rule as provide below: 
Transactions that are presented shall be validated based on reader read time and the time at 
which the tag is placed under hotlist / low balance / blacklist. Transactions presented on tags 
which are not active for more than 60 minutes prior to reader read time and up to 10 minutes 
after reader read time shall be declined with reason code 176.  For illustrations, please refer 
to Annexure I. All other guidelines stated in circular-004 shall remain in force and applicable. 
This shall be implemented effective February 17, 2025. 
Member banks are advised to make necessary changes in their systems and processes in 
alignment with these changes. To ensure smooth implementation, acquirer banks are advised 
to communicate these updates to plaza operators and system integrators. 
The information herein may please be disseminated to all the concerned.  
 
Regards, 
 
Sd/- 
Giridhar G M 
Chief – Customer Success

<!-- Page 2 -->

Annexure – 1 – Examples illustrating Transaction status as per old and new functionality. 
 
Sl. Exception Activity Exception Activity Time Reader read time 
Result as 
per new 
process 
1 
Add 
2025-01-01 13:00:00 
2025-01-01 14:10:01 
Txn. declined 
with reason 
code 176 
2 
Add  
Remove 
2025-01-01 13:00:00 
2025-01-01 13:30:00 
2025-01-01 14:10:01 
Txn. 
Accepted 
3 
Add  
Remove 
2025-01-01 13:00:00 
2025-01-01 16:10:00 
2025-01-01 16:07:01 
Txn. 
Accepted
