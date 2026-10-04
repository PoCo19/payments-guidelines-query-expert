# NETC | OC 004 | FY 26-27 | Changes introduced to streamline handling transactions from exception tagsChanges

Circular/reference number: NPCI/2026-27/NETC/004
Date: 01st July 2026

<!-- Page 1 -->

NPCI/2026-27/NETC/004 
 
 
 
 
 
             May 26, 2026 
To, 
All Members of NETC 
Subject: Changes introduced to streamline handling transactions from exception tags  
As part of ongoing efforts to enhance operational efficiency, strengthen real-time validation, 
and ensure seamless FASTag transaction processing, several improvements are being 
introduced to the NETC exception handling framework. 
1. Exception Validation changes 
Reference may be taken from NPCI Circular No. NPCI/2024-25/NETC/004A dated January 
28, 2025, which outlines the rules for declining transactions with Error Code 176 for FASTags 
under exception categories such as low balance, blacklist, and hotlist. 
As an enhancement to the above guidelines, effective 01st July 2026, the validation window 
for declining transactions on FASTags in exception status will be reduced from 60 minutes to 
10 minutes.  
Accordingly, as per this circular, transactions initiated on FASTags that is in low balance, 
blacklist, and hotlist status for more than 10 minutes prior to the reader read time and continue 
to remain so for up to 10 minutes after the reader read time will be declined with Error Code 
176, in line with the defined exception handling rules.  
Annexure I provides details on the priority of exception codes and applicable decline 
scenarios. 
2. Reduced Chargeback TAT for reason code 
Reference may be taken from NPCI Circular No. NPCI/2025-26/NETC/002 for guidelines 
related to chargebacks under Reason Codes 3004 (Vehicle in Blacklist) and 3005 (Vehicle in 
Low Balance). 
Considering the chargebacks raises with reason code 3004 (Vehicle in Blacklist) and 3005 
(Vehicle in Low Balance) are bank induced chargebacks which is not initiated from the end 
consumer, and to facilitate earlier reconciliation, the TAT for raising chargebacks under 3004 
and 3005 reason codes is reduced from 40 days to 25 days from the transaction settled time. 
Banks with immediate effect need to comply to the changes and raise any eligible chargeback 
on vehicle under exception within 25 days from the transaction settled time.  
System controls would be implemented in NRCS to reject chargeback raised after 25 days 
from the transaction settled time with the below mentioned reject reason, the effective

<!-- Page 2 -->

implementation date of which shall be communicated and implemented with a short notice 
once the central system is ready with the changes. 
 
NRCS Reject Reason Code 
Reason code description 
3207 
The TAT for the Dispute Cycle/Adjustment you trying to 
raise has expired
 
Annexure-II can be referred for the detailed chargebacks rules for transactions involving a 
tag under exception. 
 
3. Revision in INIT File Frequency 
 
To encourage the use of the API as the primary mode for checking FASTag exception status 
at plazas and acquiring banks, the frequency of the Consolidated (INIT) File shared by NPCI 
over SFTP is revised from daily to weekly, effective 01st July 2026. The file will be generated 
and shared via the existing transfer mode at 00:00 hours every Wednesday. 
Member banks are required to update their downstream systems, operational processes, and 
reconciliation workflows to align with the revised schedule. 
For new onboarding or in case of major technical failure, member banks may request an 
ad-hoc file generation which can be processed within 24 hours of request time. 
The information herein may please be disseminated to all the concerned officials for 
implementation. 
 
Regards, 
Sd/- 
Giridhar G M 
Chief – Customer Success

<!-- Page 3 -->

Annexure I 
1. Below table lists the priority while dealing with tags under exception. 
Code 
Category 
Description 
NH 
Priority 
SH Priority 
01 
Hot List 
Tags in negative balance or with violations 
3 
3 
02 
Exempted 
Tag 
exempted 
as 
per 
NHAI/MoRTH 
guidelines  
2 
2 
03 
Low Balance 
Tag with account balance below threshold 
4 
4 
04 
Invalid 
Carriage 
Tag of customer with physical disability 
2 
2 
05 
Blacklist 
Marked by RBI, NHAI, enforcement, or 
defense 
1 
1 
06 
Closed 
Closed, surrendered or replaced tag 
1 
1 
07 
(new) 
Pass 
Annual or Lifetime Toll Pass holder 
2 
Ignore 
08 
(new) 
E-notice 
Pending E-notice beyond defined time 
1 
1 
 
Below are scenarios where FASTag transactions should not be presented to NETC Switch. NETC 
Switch will decline the transactions with error code 176 if the tag was in the below mentioned 
exception codes for more than 10 minutes before reader read time and continued to remain in 
exception for more than 10 minutes after reader read time  
Tag Status at Reader Read time  
Plaza Type 
Blacklist (05) 
NH/SH/Non-toll use cases 
E-notice (08) 
NH/SH/Non-toll use cases 
Global Exempted (02)  
& Tag in Blacklist(05)/E-notice (08) 
NH/SH/Non-toll use cases 
Invalid Carriage (04)  
& Tag in: Blacklist(05)/E-notice (08) 
NH/SH/Non-toll use cases

<!-- Page 4 -->

Active Annual Pass(07)  
& Tag in Blacklist(05) /e-notice(08). 
NH 
Active Annual Pass  
& Tag in Hotlist(01) (or) Low Balance Exception(03) 
SH/non-toll use cases 
 
Annexure II  
1) Chargeback should not be raised 20 days after the transaction settled date for reason 
codes 3004(Vehicle was in blacklist) and 3005(Vehicle was in low balance).  
 
2) Scenarios when Issuing Bank should need to wait for 15 days cooling period and not raise 
chargeback because of tag getting removed from exception. 
 
3) Scenarios when Issuing Bank should not raise chargeback under reason code 3004 and 
3005. 
 
Tag 
status 
at 
Reader read time 
(RRT)
Tag Status at 
Presentation 
Transaction 
presented to NPCI 
Can Issuer raise 
Chargeback 
Active 
Active 
Within 
15 
minutes 
after RRT 
No 
Active 
Active 
Beyond 15 minutes 
after RRT 
No 
Active 
Exception 
Within 
15 
minutes 
after RRT 
No 
Exception for <10 
mins before RRT 
Active 
Within 
15 
minutes 
after RRT 
No 
Exception for <10 
mins before RRT 
Active 
Beyond 15 minutes 
after RRT 
No 
Exception for <10 
mins before RRT 
Exception 
Within 
15 
minutes 
after RRT 
No 
Exception for >10 
mins before RRT 
Active 
Within 
15 
minutes 
after RRT 
No 
Exception for >10 
mins before RRT 
Active 
Beyond 15 minutes 
after RRT 
No

<!-- Page 5 -->

4) Scenarios when Issuing Bank should need to wait for 15 days cooling period and not raise 
chargeback because of tag getting removed from exception. 
 
Tag 
status 
at 
Reader read time 
(RRT) 
Tag Status at 
Presentation 
Transaction 
presented 
to 
NPCI 
Tag 
got 
active within 
15 days of 
RRT
Can 
Issuer 
raise 
Chargeback 
Active 
Exception 
Beyond 
15 
minutes 
after 
RRT
Yes 
No 
Exception for >10 
mins before RRT 
Exception 
With 15 minutes 
of RRT 
Yes 
No 
Exception for <10 
mins before RRT 
Exception 
Beyond 
15 
minutes 
after 
RRT
Yes 
No 
Exception for >10 
mins before RRT 
Exception 
Beyond 
15 
minutes 
after 
RRT
Yes 
No 
 
5) Scenarios when Issuing Bank should not raise a chargeback because of delay from issuing 
bank in updating the tag status to exception. 
 
Tag 
status 
at 
Reader read time 
(RRT)
Tag Status at Presentation
Transaction 
presented 
to 
NPCI
Can 
Issuer 
raise 
Chargeback
Active 
Exception. 
No 
other 
transaction 
presented 
between 
RRT 
and 
presentation time.
Beyond 
15minutes 
after 
RRT.  
No 
 
6) Scenarios when Issuing Bank would need to wait for 15 days cooling period and can raise 
chargeback because of tag still in exception. 
 
Tag status at 
Reader 
read 
time (RRT) 
Tag 
Status 
at 
Presentation 
Transaction 
presented 
to NPCI 
Tag 
got 
active 
within 
15 
days of RRT
Can 
Issuer 
raise 
a 
Chargeback 
Active 
Tag 
went 
to 
Exception because of 
another 
transaction 
presented 
between 
RRT and presentation 
Beyond 
15minutes 
after RRT.  
No 
Yes 
Exception 
for 
>10 mins before 
RRT
Exception 
With 
in 
15minutes of 
RRT
No 
Yes 
Exception 
for 
<10 mins before 
RRT
Exception 
Beyond 
15 
minutes 
after RRT
No 
Yes 
Exception 
for 
>10 mins before 
RRT
Exception 
Beyond 
15 
minutes 
after RRT
No 
Yes
