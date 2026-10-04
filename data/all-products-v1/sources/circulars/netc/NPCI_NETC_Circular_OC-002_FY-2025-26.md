# NETC | OC 002 | F.Y. 25-26 | Chargeback rules for transaction presented on tags under Exception

Circular/reference number: NPCI/2025-26/NETC/002

<!-- Page 1 -->

NPCI/2025-26/NETC/002     
 
 
 
 
              August 05, 2025 
 
To, 
All Members of NETC 
Subject: Guidelines and liability rules for NETC transactions initiated against a tag which is 
under hotlist or blacklist or low balance status. 
1. Reference may be taken from Circular 009 dated Jan 28th, 2025, advising Issuers to 
comply with a 15-day cooling period from reader read time before raising chargebacks 
against transactions presented beyond 15 minutes from reader read time for following 
reason codes 3004 - vehicle was in blacklist, 3005 - vehicle was in low balance  
The 15 days cooling period from reader read time is now mandated for above mentioned 
chargeback reason codes regardless of when the transaction is presented to NPCI. 
To ensure compliance with this rule, system controls are being built in NRCS to accept 
chargebacks raised for above reason codes only after the 15-day cooling period. The 
chargeback raised before the prescribed 15-day cooling period shall be rejected with the 
following reject reason: 
NRCS Reject Reason Code 
Reason code description 
5224 
Chargeback for reason code 3004,3005 can be raised 
only post the cooling period of 15 days 
        
This shall be implemented with effect from October 01, 2025. 
2. Scenarios for which the issuer should be raising above mentioned chargebacks and 
scenarios for which the issuer should wait for 15 days before raising the charge back are 
detailed in Annexure I.  
It may please be noted that NPCI shall implement system controls for these rules, details 
of which shall be published separately at a later date. 
 
The information herein may please be disseminated to all the concerned officials. 
 
With warm regards 
 
SD/- 
Giridhar G M  
Chief – Customer Success

<!-- Page 2 -->

Annexure I: 
Exception quoted below refers to tags in Hotlist(01), Low Balance(03), Blacklist(05). 
 
1) Scenarios when Issuing Bank should not raise chargeback under reason code 3004 and 
3005.  
 
Tag status at Reader 
read time (RRT) 
Tag Status at 
Presentation 
Transaction 
presented to NPCI 
Can Issuer raise 
Chargeback 
Active 
Active 
With in 15 minutes after 
RRT 
No 
Active 
Active 
Beyond 15 minutes 
after RRT 
No 
Active 
Exception 
With in 15 minutes after 
RRT 
No 
Exception for <20 
mins before RRT 
Active 
With in 15 minutes after 
RRT 
No 
Exception for <20 
mins before RRT 
Active 
Beyond 15 minutes 
after RRT 
No 
Exception for <20 
mins before RRT 
Exception 
With in 15 minutes after 
RRT 
No 
Exception for >20 
mins before RRT 
Active 
With in 15 minutes after 
RRT 
No 
Exception for >20 
mins before RRT 
Active 
Beyond 15 minutes 
after RRT 
No 
 
2) Scenarios when Issuing Bank should need to wait for 15 days cooling period and not 
raise chargeback because of tag getting removed from exception. 
 
Tag status at 
Reader read time 
(RRT) 
Tag Status at 
Presentation 
Transaction 
presented to 
NPCI 
Tag got active 
within 15 
days of RRT 
Can Issuer 
raise 
Chargeback 
Active 
Exception 
Beyond 15 
minutes after RRT 
Yes 
No 
Exception for >20 
mins before RRT 
Exception 
With in 15 
minutes of RRT 
Yes 
No 
Exception for <20 
mins before RRT 
Exception 
Beyond 15 
minutes after RRT 
Yes 
No 
Exception for >20 
mins before RRT 
Exception 
Beyond 15 
minutes after RRT 
Yes 
No 
 
3) Scenarios when Issuing Bank should not raise a chargeback because of delay from 
issuing bank in updating the tag status to exception. 
 
Tag status at Reader 
read time (RRT) 
Tag Status at Presentation 
Transaction 
presented to NPCI 
Can Issuer 
raise 
Chargeback 
Active 
Exception. No other 
transaction presented between 
RRT and presentation time. 
Beyond 15 minutes 
after RRT.  
No

<!-- Page 3 -->

4) Scenarios when Issuing Bank would need to wait for 15 days cooling period and can 
raise chargeback because of tag still in exception. 
 
Tag status at 
Reader read time 
(RRT) 
Tag Status at 
Presentation 
Transaction 
presented to 
NPCI 
Tag got active 
within 15 
days of RRT 
Can Issuer 
raise a 
Chargeback 
Active 
Tag went to 
Exception because 
of another 
transaction 
presented between 
RRT and 
presentation  
Beyond 15 
minutes after 
RRT.  
No 
Yes 
Exception for >20 
mins before RRT 
Exception 
With in 15 
minutes of RRT 
No 
Yes 
Exception for <20 
mins before RRT 
Exception 
Beyond 15 
minutes after 
RRT 
No 
Yes 
Exception for >20 
mins before RRT 
Exception 
Beyond 15 
minutes after 
RRT 
No 
Yes
