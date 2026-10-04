# NETC | OC 005 | FY 25-26 | New chargeback reason codes in NRCS and guidelines for handling chargebacks

Circular/reference number: NPCI/2025-26/NETC/005
Date: 1st December 2025

<!-- Page 1 -->

 
01001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051 
CIN: U74990MH2008NPL189067 
NPCI/2025-26/NETC/005   
 
 
 
 
 
             October 28, 2025 
To, 
All Members of NETC 
Subject: Chargeback reason in NETC and guidelines for handling chargebacks. 
 
1. Basis feedback from the members in NETC Ecosystem, new reason codes for Debit 
Adjustment and chargebacks have been introduced in NRCS along with the updated 
evidence required for chargebacks.  
 
The details of the new chargeback reason codes can be found in Annexure – I and would 
be implemented in NRCS with effect from 1st December 2025. Consolidated list of 
evidence required from Issuing and Acquiring end for each chargeback reason code can 
be found in Annexure – II & Annexure – III.  
 
2. NPCI would be implementing controls to ensure compliance to the requirement of 
submitting evidence at the time of raising/representing a charge back. In case on non- 
compliance to this guideline, system shall reject such chargeback/representation. The 
following rejection reason code shall be used for this purpose.  
 
NRCS Reject Reason code 
Reason Code Description 
5225 
Rejected as no evidence uploaded for the 
chargeback reason. 
 
      NPCI shall be working on implementing the system controls and the date of 
implementation shall be communicated separately however the member banks shall start 
implementing this at the earliest not later than December 01, 2025.  It may please be noted 
that effective 1st December any chargeback raising / representation submitted without 
evidence as per the compliance sited above shall attract negative verdict in cases where the 
parties reach out for NRP / PRD. 
The information herein may please be disseminated to all the concerned officials for strict 
adherence from 1st December 2025. 
Regards, 
 
 
Sd/- 
Giridhar G M 
Chief – Customer Success

<!-- Page 2 -->

 
01001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051 
CIN: U74990MH2008NPL189067 
Annexure I: 
1) Introduction of new reason codes for raising Debit Adjustment: 
 
1. 1008 - DA raised on vehicle class mismatch 
2. 1009 - DA raised on vehicle number mismatch 
3. 1010 - DA for plaza following non-standard vehicle classification 
 
Reason Code & Description 
Preconditions to be satisfied 
1008 - DA raised on vehicle class 
mismatch 
 
i) To be raised if the vehicle class derived using GVW, axle, 
category is of a higher class compared to the mapper class 
of the tag.  
 
&  
 
ii) VRN of the vehicle passing through the plaza is same as 
the VRN associated with the tag. 
1009 - DA raised on vehicle number 
mismatch 
i) To be raised if the vehicle class derived using GVW, axle, 
category is of a higher class compared to the mapper class 
of the tag.  
 
&  
 
ii) VRN of the vehicle passing through the plaza is different 
from the VRN associated with the tag. 
1010 - DA for plaza following non-standard 
Vehicle Classification  
i) To be raised if plaza has a clause in concessionaire 
agreement which are not in line with the vehicle 
classification document and entitles to raise a Debit 
Adjustment for the transaction. 
 
2) Introduction of new reason codes for raising chargebacks: 
 
1. 3023 - Wrong DA raised on vehicle class mismatch  
2. 3024 - Wrong DA raised on vehicle number mismatch  
3. 3025 - Wrong DA raised on plaza following non-standard vehicle classification  
4. 3026 - Return Journey discount not provided  
5. 3027 - Toll Fare calculation error on closed loop plaza 
6. 3028 - Connecting Plaza benefit not provided 
7. 3029 - Pass benefit/Local discount not provided 
8. 3030 - Exemption not provided for EV vehicle at Exempted plazas 
 
Reason Code & Description 
Preconditions to be satisfied 
3023 – Wrong DA raised on vehicle class 
Mismatch  
To dispute debit adjustment raised with 1008 reason code (DA 
raised on vehicle class mismatch) 
 
3024 – Wrong DA raised on vehicle 
number mismatch  
To dispute debit adjustment raised with 1009 reason code (DA 
raised on vehicle number mismatch) 
 
3025 – Wrong DA raised on plaza following 
non-standard vehicle classification  
To dispute debit adjustment raised with 1010 reason code (DA 
for plaza following Non-standard Vehicle Classification) 
 
3026 – Return Journey discount not 
provided  
To raise dispute if the customer was not provided return 
journey discount within the Return journey window applicable 
at the plaza.  
 
3027 – Toll Fare Calculation error on 
Closed loop plaza 
To raise dispute related to overcharging on closed loop plaza 
with an entry and an exit.

<!-- Page 3 -->

 
01001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051 
CIN: U74990MH2008NPL189067 
3028 - Connecting Plaza benefit not 
provided 
To raise dispute related to overcharging on integrated plaza 
setup. 
 
3029 – Pass benefit/Local discount not 
provided  
To raise dispute if annual pass/monthly pass/ local resident 
discount is not provided. 
 
3030 - Exemption not provided for EV 
vehicle at Exempted plazas 
To raise dispute if the EV vehicles are charged despite being 
in the exemption list. 
 
 
 
3) Introduction of new reason codes for responding to chargebacks: 
 
1. 4011 - Valid DA, as vehicle passing is of higher class with same VRN 
2. 4012 - Valid DA, as vehicle passing is of higher class with different VRN 
3. 4013 - Valid DA, as plaza follows Non-standard Vehicle Classification 
4. 4014 - Return Journey discount provided 
5. 4015 - Return Journey discount not applicable at plaza 
6. 4016 - Return Journey Logic applicable for 24Hrs 
7. 4017 - Return Journey Logic applicable for 12Hrs 
8. 4018 - Return Journey Logic applicable for Same day 
9. 4019 - Toll Fare Calculation is correct for the Entry/Exit combination 
10. 4020 - Higher fare charged as per concessionaire agreement for missing Entry/Exit 
11. 4021 - Connecting Plaza benefit already provided to Customer 
12. 4022 - Pass benefit/Local discount benefits provided  
13. 4023 - Pass/Local discount is expired or not applicable 
14. 4024 - Invalid document or required evidence not submitted by the Issuer 
15. 4025 - Customer carrying Tag in Hand  
16. 4026 - Connecting Plaza benefit is not applicable at this plaza 
17. 4027 - Credit adjustment was raised for one of the duplicate transactions. 
18. 4028 - Not a duplicate transaction as per IHMCL duplicate transaction Policy. 
19. 4029 - Vehicle passing has a VRN different compared to the Fastag 
 
4) Removal of below reason codes: 
 
1. 3009 – Wrong Debit Adjustment 
2. 3014 – Other Specify (Chargeback Reason Codes – Debit) 
3. 3022 – Other Specify (Chargeback Reason Codes – Credit) 
4. 4010 – Other Specify (Re-Presentment Reason Codes) 
5. 1007 – Other Specify (Debit Adjustment Reason Codes) 
6. 2007 – Other Specify (Credit Adjustment Reason Codes)

<!-- Page 4 -->

 
01001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051 
CIN: U74990MH2008NPL189067 
Annexure II: Evidence Requirement from Issuers and Acquirers for Debit Adjustment 
and Chargebacks 
 
 
Reason Code 
Description 
Evidence from acquirers for raising Debit Adjustment  
1008 
DA raised on vehicle class mismatch 
 
i) [EVIDENCE] Vehicle passing image along with legible 
vehicle registration number. 
 
ii) [MMT] The vehicle class of the vehicle passing based on 
which Debit Adjustment is raised to be mentioned in MMT. 
 
1009 
DA raised on vehicle number mismatch 
 
i) [EVIDENCE] Vehicle passing image along with legible 
vehicle registration number. 
 
ii) [MMT] The vehicle class of the vehicle passing based on 
which Debit Adjustment is raised to be mentioned in MMT. 
 
1010 
DA for plaza following non-standard Vehicle 
Classification 
 
i) [EVIDENCE] Vehicle passing image along with legible 
vehicle registration number. 
 
ii) [MMT] The vehicle class of the vehicle passing based on 
which Debit Adjustment is raised to be mentioned in MMT. 
 
iii) [EVIDENCE & MMT] Clause in concessionaire agreement 
different from vehicle classification entitling plaza to raise 
Debit Adjustment. 
 
 
Note: Considering errors at the time of tag issuance leading to tags issued to incorrect vehicle numbers, 
It is mandated to submit clear images of the vehicle with visible vehicle number (front) with tag affixed and RC 
copy for raising chargeback with the below reason codes: 
a. 3001 - NETC Toll services not availed   
b. 3024 - Wrong DA raised on vehicle number mismatch 
Reason 
Code 
Description 
Evidence 
from 
Issuers  
Evidence 
from 
acquirers  
Guidelines 
for 
Issuers 
Guidelines 
for 
Acquirers 
3001 
NETC 
Toll 
services 
not 
availed/ 
Tag 
holder 
does 
not recognize 
the transaction 
[EVIDENCE] 
Clear 
images of the vehicle 
with 
visible vehicle 
number (front with tag 
affixed) and RC copy 
  
 
i) [EVIDENCE] Clear 
evidence 
of 
vehicle 
passing through plaza 
with 
legible 
vehicle 
registration 
number 
along 
with 
legible 
timestamp in “yyyy-mm-
dd hh:mm:ss” format. 
 
ii) [MMT] Timestamp in 
evidence 
should 
be 
within 5 minutes of 
Reader Read time 
 
1) Issuer is expected 
to check for abuse of 
chargeback 
by 
customer if there are 
repeated chargeback 
on 3001 from the 
same tag. 
 
2) Issuer should not 
be 
raising 
the  
chargeback if the VRN 
associated with the 
tag is not matching 
with the vehicle image 
collected 
from 
the 
customer. 
 
i) 
Timestamp 
in 
evidence should with-in 
5 minutes of Reader 
Read time. 
 
2) VRN of the vehicle 
passing should be clear 
while representing. 
 
3) Should accept the 
chargeback if the VRN 
is 
different 
from 
evidence submitted by 
Issuer. 
 
4) Evidence in image 
format is recommended 
for faster response.

<!-- Page 5 -->

 
01001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051 
CIN: U74990MH2008NPL189067 
3002 
Duplicate 
transaction 
done 
at Toll 
Plaza 
Below details are to 
be included in MMT. 
1. [MMT] RRN of 
original transaction. 
 
2. [MMT] Reader read 
Date 
& 
Time 
of 
original transaction. 
  
3. [MMT] Plaza ID of 
original transaction. 
[MMT] Details of why 
the transaction is not a 
duplicate transaction in 
MMT. 
 
[MMT] Details of credit 
adjustment raised if any 
in MMT. 
 
Chargeback 
should 
be 
raised 
only 
if: 
 
i) Difference in Reader 
Read time between 
the two transaction is 
within 
15 
minutes 
provided 
the 
two 
transactions 
originated from the 
same plaza with both 
transactions in same 
direction & No Credit 
adjustment was raised 
on one of the duplicate 
transactions 
 
ii) 
Difference 
in 
Reader Read time the 
two 
transaction 
is 
within 
10 
minutes 
provided 
the 
two 
transactions 
originated from the 
same plaza with both 
transactions 
in 
different direction. No 
Credit adjustment was 
raised on one of the 
duplicate 
transactions. 
Proactively raise Credit 
adjustment 
if 
the 
transaction is duplicate 
as 
per 
duplicate 
transaction policy.  
 
Should 
not 
be 
represented 
if: 
 
i) Difference in Reader 
Read time between the 
two transaction is within 
15 minutes provided the 
two 
transactions 
originated 
from 
the 
same plaza with both 
transactions in same 
direction. 
 
ii) Difference in Reader 
Read 
time 
the 
two 
transaction is within 10 
minutes provided the 
two 
transactions 
originated 
from 
the 
same plaza with both 
transactions in different 
direction. 
3003 
Vehicle was in 
exempted list 
[EVIDENCE] 
Evidence showing the 
vehicle in exemption 
list at the time of 
reader read time.  
 
 
[OPTIONAL 
EVIDENCE] Proof from 
internal system showing 
expiry of the exemption 
(or) remarks on why the 
tag was not in exempted 
list 
at 
the 
time 
of 
transaction. 
 
 
 
3004 
Vehicle was in 
blacklist 
Refer Annexure III for chargeback rules. Issuing bank to withdraw and not raise the chargeback to 
subsequent stages in dispute lifecycle if the tag has got active because of customer recharging the 
tag.  If any case gets referred to NRP, Tag status at RRT, Transaction presentation, chargeback raise, 
and Arbitration Raise would be considered for providing NRP verdict.   
3005 
Vehicle was in 
low balance 
3006 
Toll 
fare 
calculation 
error  
[MMT] Details on why 
the fare charged is 
higher in MMT. 
[EVIDENCE] Fare table 
showing the toll charges 
for the vehicle class. 
 
Chargeback category 
to be used for raising 
chargeback 
on 
overcharging 
for 
plazas 
other 
than 
closed 
loop 
and 
connecting plazas. 
 
Issuing 
Bank 
to 
validate fare against 
toll fare details at 
plaza before raising a 
chargeback. 
 
.

<!-- Page 6 -->

 
01001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051 
CIN: U74990MH2008NPL189067 
3011 
Paid by other 
means 
i) [EVIDENCE]Receipt 
given to customer by 
plaza should need to 
be 
shared 
while 
raising chargeback 
 
i) [EVIDENCE] Proof 
showing the FASTag 
debit is for a different 
transaction along with 
Vehicle passing image 
for 
the 
FASTAG 
transaction.  
 
ii) [EVIDENCE] Clear 
evidence 
of 
vehicle 
passing through plaza 
for both the cash and 
Fastag 
transaction 
showing legible vehicle 
registration 
number 
along 
with 
legible 
timestamp in “yyyy-mm-
dd hh:mm:ss” format. 
 
Chargeback 
should 
be 
raised 
on 
this 
category only if the 
customer 
had 
paid 
through 
alternate 
payment methods in 
addition to getting a 
debit in the FASTag 
wallet.  
 
3023 
Wrong 
DA 
raised 
on 
vehicle 
class 
mismatch  
i) 
[EVIDENCE] 
RC 
Copy or Vahan proof 
showing gross weight, 
number 
of 
axles, 
seating capacity. 
i) [EVIDENCE] Vehicle 
passing image along 
with 
visible 
vehicle 
registration number. 
 
ii) [MMT] The vehicle 
class of the passing 
vehicle based on which 
Debit 
Adjustment 
is 
raised should also be 
mentioned in MMT. 
Only RC proof or 
Vahan be considered 
valid. 
 
i) To represent if the 
vehicle class derived 
using 
GVW, 
axle, 
category is of a higher 
class compared to the 
mapper class of the tag.  
& 
ii) VRN of the vehicle 
passing 
through 
the 
plaza is same as the 
VRN associated with 
the tag. 
3024 
Wrong 
DA 
raised 
on 
vehicle 
number 
mismatch  
i) 
[EVIDENCE] 
RC 
Copy or Vahan proof 
showing gross weight, 
number 
of 
axles, 
seating capacity. 
 
ii) [EVIDENCE] Image 
evidence of vehicle 
with legible Vehicle 
number plate. 
 
i) [EVIDENCE] Vehicle 
passing image along 
with 
visible 
vehicle 
registration number. 
 
ii) [MMT] The vehicle 
class of the passing 
vehicle based on which 
Debit 
Adjustment 
is 
raised should also be 
mentioned in MMT. 
Only RC proof or 
Vahan 
to 
be 
considered valid. 
 
i) To represent if the 
vehicle class derived 
using 
GVW, 
axle, 
category is of a higher 
class compared to the 
mapper class of the tag  
&  
ii) VRN of the vehicle 
passing 
through 
the 
plaza is different from 
the 
VRN 
associated 
with the tag. 
3025 
Wrong 
DA 
raised on plaza 
following Non-
standard 
vehicle 
classification  
i) 
[EVIDENCE] 
RC 
Copy or Vahan proof 
showing gross weight, 
number 
of 
axles, 
seating capacity. 
 
i) [EVIDENCE] Vehicle 
passing image along 
with 
visible 
vehicle 
registration number. 
 
ii) [EVIDENCE] Snippet 
from plaza agreement 
showing 
the 
non-
standard 
vehicle 
classification clause 
 
iii) [MMT] The vehicle 
class of the passing 
Only RC proof or 
Vahan 
to 
be 
considered valid. 
To represent only if 
plaza 
having 
concessionaire 
agreement 
clause 
which are not in line with 
the vehicle classification 
document 
entitles 
to 
raise a DA for the 
transaction.

<!-- Page 7 -->

 
01001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051 
CIN: U74990MH2008NPL189067 
vehicle based on which 
Debit 
Adjustment 
is 
raised should also be 
mentioned in MMT. 
3026 
Return 
Journey 
discount 
not 
provided  
 
i) 
[MMT] 
RRN 
of 
original transaction 
 
ii) [MMT] Reader read 
Date 
& 
Time 
of 
original transaction to 
be included in MMT. 
 
iii) [MMT] Plaza IDs 
associated 
with 
original transaction. 
i) [EVIDENCE] Toll fare 
chart for the vehicle 
class showing Return 
fare. 
 
ii)  [MMT] 
Details 
of 
Credit 
adjustment 
raised 
if 
return 
journey discount is 
not provided 
 
 
i) Issuing Bank to 
verify 
whether 
the 
transaction falls within 
the eligible time limit 
for 
getting 
return 
journey discount.  
 
ii) Issuing Bank to 
validate 
whether 
Return 
journey 
discount is applicable 
at the plaza. 
 
 
i) Credit adjustment to 
be raised proactively if 
return journey discount 
is not provided. 
 
ii) 
Onward 
journey 
transaction should be 
presented before return 
journey transaction.  
1) 
 
3027  
Toll 
Fare 
Calculation 
error 
on 
Closed 
loop 
plaza 
i) 
[EVIDENCE] 
To 
provide screenshot of 
alternate 
payment 
mode token shared by 
customers 
showing 
plaza 
name, 
timestamp. 
 
ii) [MMT] Details of 
Entry/Exit Plaza name 
shared by customer. 
 
i) 
[EVIDENCE] 
If 
overcharged for farthest 
distance, plaza need to 
share the snippet of 
plaza agreement stating 
customer 
can 
be 
charged 
for 
farthest 
distance in the absence 
of the Entry Exit log. 
 
ii) 
[EVIDENCE] 
Toll 
Fare 
chart 
for 
the 
vehicle class for Entry-
Exit Plaza combination. 
 
iii) [EVIDENCE] vehicle 
passing image at entry 
and exit plaza based on 
which was available. 
  
iv) [MMT] Details of 
Credit 
adjustment 
raised 
on 
differential 
fare along with toll fare. 
 
i) Issuing Bank to 
validate fare against 
toll fare at the plaza 
before 
raising 
a 
chargeback. 
 
ii) Chargeback reason 
to be used only for toll 
fare calculation error 
related to closed loop 
plazas. 
i) Credit adjustment to 
be raised proactively in 
case of overcharging. 
 
3028  
Connecting 
Plaza 
benefit 
not provided 
 
i) 
[MMT] 
RRN 
of 
original transaction 
 
ii) [MMT] Reader read 
Date 
& 
Time 
of 
original transaction to 
be included in MMT. 
 
iii) [MMT] Plaza IDs 
associated 
with 
original transaction. 
i) [EVIDENCE] Toll fare 
chart for the vehicle 
class showing Return 
fare. 
 
ii) [MMT] Details of 
Credit 
adjustment 
raised if return journey 
discount is not provided 
 
 
i) Issuing Bank to 
raise chargeback post 
verifying whether the 
transaction falls within 
the eligible time limit 
for getting connecting 
journey discount.  
 
ii) Issuing Bank to 
validate 
whether 
connecting 
journey 
discount is applicable 
at the plaza. 
 
i) Credit adjustment to 
be raised proactively if 
connecting 
journey 
discount 
is 
not 
provided. 
 
ii) Transaction to be 
presented in the order 
of the reader read time.  
 
3029  
Pass 
benefit/Local 
discount 
not 
provided  
 
 
[EVIDENCE] 
Evidence showing the 
monthly 
pass/local 
discount active at the 
time of reader read 
time.  
 
i) [EVIDENCE or MMT] 
Evidence or remarks on 
why the chargeback 
raised on monthly pass 
is not valid.

<!-- Page 8 -->

 
01001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051 
CIN: U74990MH2008NPL189067 
 
(or) 
 
[EVIDENCE] 
Acknowledgment 
given to customers 
from plaza for monthly 
pass/local discount. 
ii) [EVIDENCE or MMT] 
Toll fare chart showing 
local 
discount 
fare. 
Evidence or remarks on 
why the chargeback 
raised on local pass 
discount is not valid. 
3030 
Exemption not 
provided 
for 
EV vehicle at 
Exempted 
plazas 
[EVIDENCE] 
Evidence showing the 
vehicle 
is 
in 
exemption list at the 
time of reader read 
time.  
 
[EVIDENCE or MMT] 
Proof 
from 
internal 
system showing why 
the 
vehicle 
is 
not 
exempted. 
 
 
 
 
Annexure III: Applicable for reason code 3004, 3005 - Chargeback rules for transactions 
presented on tags under Exception Hotlist (01), Low Balance (03), Blacklist (05)  
 
1) For chargeback reason code 3004 and 3005, issuing bank to not raise chargeback or not 
raise to the subsequent stages if the tag has got removed from exception. 
 
2) Scenarios when Issuing Bank should not raise chargeback under reason code 3004 and 
3005.  
 
Tag status at Reader 
read time (RRT) 
Tag 
Status 
at 
Presentation 
Transaction presented to 
NPCI 
Can 
Issuer 
raise 
Chargeback 
Active 
Active 
With in 15 minutes after 
RRT 
No 
Active 
Active 
Beyond 15 minutes after 
RRT 
No 
Active 
Exception 
With in 15 minutes after 
RRT 
No 
Exception for <20 mins 
before RRT 
Active 
With in 15 minutes after 
RRT 
No 
Exception for <20 mins 
before RRT 
Active 
Beyond 15 minutes after 
RRT 
No 
Exception for <20 mins 
before RRT 
Exception 
With in 15 minutes after 
RRT 
No 
Exception for >20 mins 
before RRT 
Active 
With in 15 minutes after 
RRT 
No 
Exception for >20 mins 
before RRT 
Active 
Beyond 15 minutes after 
RRT 
No 
 
3) Scenarios when Issuing Bank should need to wait for 15 days cooling period and not raise 
chargeback because of tag getting removed from exception. 
 
Tag status at Reader 
read time (RRT) 
Tag 
Status 
at 
Presentation 
Transaction 
presented to NPCI 
Tag got active 
within 15 days 
of RRT 
Can Issuer raise 
Chargeback 
Active 
Exception 
Beyond 15 minutes 
after RRT 
Yes 
No 
Exception for >20 mins 
before RRT 
Exception 
With in 15 minutes 
of RRT 
Yes 
No

<!-- Page 9 -->

 
01001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051 
CIN: U74990MH2008NPL189067 
Exception for <20 mins 
before RRT 
Exception 
Beyond 15 minutes 
after RRT 
Yes 
No 
Exception for >20 mins 
before RRT 
Exception 
Beyond 15 minutes 
after RRT 
Yes 
No 
 
4) Scenarios when Issuing Bank should not raise a chargeback because of delay from issuing 
bank in updating the tag status to exception. 
 
Tag status at Reader 
read time (RRT) 
Tag Status at Presentation 
Transaction 
presented to NPCI 
Can Issuer raise 
Chargeback 
Active 
Exception. No other transaction 
presented 
between 
RRT 
and 
presentation time. 
Beyond 15 minutes 
after RRT.  
No 
 
 
5) Scenarios when Issuing Bank would need to wait for 15 days cooling period and can raise 
chargeback because of tag still in exception. 
 
Tag 
status 
at 
Reader read time 
(RRT) 
Tag 
Status 
at 
Presentation 
Transaction 
presented 
to 
NPCI 
Tag got active 
within 15 days 
of RRT 
Can Issuer raise 
a Chargeback 
Active 
Tag went to Exception 
because of another 
transaction presented 
between 
RRT 
and 
presentation  
Beyond 
15 
minutes after RRT.  No 
Yes 
Exception for >20 
mins before RRT 
Exception 
With in 15 minutes 
of RRT 
No 
Yes 
Exception for <20 
mins before RRT 
Exception 
Beyond 
15 
minutes after RRT 
No 
Yes 
Exception for >20 
mins before RRT 
Exception 
Beyond 
15 
minutes after RRT 
No 
Yes
