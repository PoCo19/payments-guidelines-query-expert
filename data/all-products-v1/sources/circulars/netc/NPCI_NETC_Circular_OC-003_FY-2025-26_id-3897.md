# NETC | OC 003 | FY 26-27 | Implementation of system controls in NRCS for chargebacks raised under reason codes 3004 & 3005

Circular/reference number: NPCI/2026-27/NETC/003
Date: 5th August 2025

<!-- Page 1 -->

 
NPCI/2026-27/NETC/003 
 
 
 
 
 
                        April 08, 2026 
To, 
All NETC Members 
 
Subject: Implementation of system controls in NRCS for chargebacks raised under reason 
codes 3004 & 3005. 
 
Reference may be taken from Circular NPCI/2025-26/NETC/002 dated 5th August 2025 regarding 
the rules to be followed by the member banks while raising chargeback under reason codes 
3004(vehicle was in blacklist) & 3005(vehicle was in low balance). It has been observed that 
adherence to these guidelines remains inconsistent among members. Accordingly, to address 
this issue and prevent invalid chargebacks, NPCI is implementing controls in NRCS back office 
to validate and reject invalid chargebacks. Chargebacks falling under any of the scenarios listed 
in Annexure–1 will be declined with reason code 5228 – ‘Active Tag, Issuer chargeback is not 
valid.’ All rejected chargebacks will be reflected in the acknowledgement file. 
Go-live date: The functionality will be implemented with effect from 15th May 2026. 
All member banks are advised to update their respective recon modules to ensure compliance 
with these guidelines. Kindly disseminate the information contained herein to the officials 
concerned. 
Warm Regards, 
 
 
SD/- 
Giridhar GM 
Chief – Customer Success

<!-- Page 2 -->

 
Annexure – 1  
The following are the conditions under which chargebacks raised under reason code 3004 and 
3005 shall be treated as invalid and rejected by NRCS. 
Tag Status at 
Reader Read Time 
(RRT)  
Tag Status at 
Presentation  
Transaction 
Presented to 
NPCI 
Chargeback 
Eligibility 
System 
Outcome 
Active 
Active 
Within 15 minutes 
after RRT 
Not permitted 
Automatically 
rejected 
Active 
Active 
Beyond 15 minutes 
after RRT 
Active 
Exception 
Within 15 minutes 
after RRT 
Exception for <20 
mins before RRT 
Active 
Within 15 minutes 
after RRT 
Exception for <20 
mins before RRT 
Active 
Beyond 15 minutes 
after RRT 
Exception for >20 
mins before RRT 
Active 
Within 15 minutes 
after RRT 
Exception for >20 
mins before RRT 
Active 
Beyond 15 minutes 
after RRT
