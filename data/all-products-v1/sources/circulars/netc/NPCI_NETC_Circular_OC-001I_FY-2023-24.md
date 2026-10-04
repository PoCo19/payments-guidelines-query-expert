# NETC I OC001 I FY 2023-2024 I Implementation of NETC FASTag Closure and Replacement

Circular/reference number: NPCI/2023-24/NETC/001
Date: 17th May, 2023

<!-- Page 1 -->

 
 
 
1001A, The Capital, B Wing, 10th Floor,   
Bandra Kurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101  
contact@npci.org.inwww.npci.org.in   
CIN: U74990MH2008NPL189067 
NPCI/2023-24/NETC/001 
 
 
 
 
 
 
         17th May, 2023 
To, 
All Issuer Members participating in NETC Product 
Dear Sir/Madam, 
Subject: Implementation of NETC FASTag Closure and Replacement Policy 
To contribute to the Government of India’s vision of creating NETC FASTag as unique identity for 
vehicles, we are requesting all issuing members and sub-members to comply with NETC FASTag 
Closure and Replacement Policy (Annexure 1). Currently as per NETC mapper data, there are 
vehicles having multiple Tags issued against the same vehicle. This policy works towards the goal 
of One Vehicle One Tag by mitigating any possible misuse of multiple Tags associated with 
vehicles. The policy will also standardize the tag closure and replacement processes across 
stakeholders and define the TAT’s and responsibilities of the issuers. 
The policy will have to be mandatorily followed by all issuing members effective 30th June 2023 for 
all clauses except Forceful Tag Closure. The Implementation timeline for forceful closure clause 
will be 1st December 2023. Issuers need to ensure that they complete Vahan and other relevant 
API Certification before 1st December 2023.  Kindly make a note of contents herein and 
disseminate the same to the relevant stakeholders. 
 
Yours faithfully, 
SD/- 
Kunal Kalawatia, 
Chief of Products 
 
Enclosed: 
Annexure 1: NETC FASTag Closure and Replacement Policy 
 
 
Annexure 2: FAQ’s for NETC FASTag Closure and Replacement Policy

<!-- Page 2 -->

 
 
 
Annexure 1: Tag Closure & Replacement Policy Document 
Background 
Currently as per NETC mapper data, there are vehicles having multiple Tags issued against the same 
vehicle. The purpose of this policy is to contribute to the government’s vision of creating NETC FASTag as 
identity for vehicles and to work towards the goal of One Vehicle One Tag by mitigating any possible 
misuse of multiple Tags associated with vehicles. This will also standardize the tag closure and 
replacement processes across stakeholders which currently differs as per Issuers internal processes and 
put forth well-defined SLA and responsibilities on the issuers. This will help to build compliance on FASTag 
issuance and also ensure data sanctity. This policy will be reviewed and updated periodically basis 
operational relevance and inputs from the ecosystem. 
A. Tag Closure 
Customer may apply for tag closure in following scenarios: 
a. Customer wants to/has sold the existing vehicle 
b. Customer wants to opt for a different issuer 
c. Special Case: 
i. Death of existing customer 
ii. Customer has brought a car with existing Tag in Negative Balance 
iii. Forceful tag suspension where Customer has opted for a new tag by a new issuer without 
requesting the previous issuer for tag closure. 
 
i. 
Policy for Consumers in case of Tag Closure (for aforesaid mentioned point a & b): 
In the above scenarios, the customer should follow the following process for Tag Closure: 
 
1. Access the issuer member and sub-member portal for NETC closure request of the NETC 
FASTag. Customer can also call the issuer member and sub-member customer care/ toll free 
number or write to Issuer member and sub-member email support for closure of the NETC 
FASTag.  
2. In case customer goes to the bank portal / Customer Care No, he has to select the Tag Closure 
option. 
3. Customer has to submit the relevant documents as per bank portal for closure along with 
NETC FASTag image. 
4. Customer has to submit the Bank account/ wallet details for refund of net applicable 
settlement amount in case of closure of the NETC FASTag (Bank can also refund the net 
settlement amount through DD). 
5. Customer has to confirm the removal and disposal of NETC FASTag from the vehicle (If in-case 
customer is unable to remove the tag due to un-accessibility of the vehicle like vehicle 
sold/stolen etc, customer wallet will be debited for transactions* occurring on the respective 
tag till T+5 days, T being the date of submission of valid closure request)

<!-- Page 3 -->

 
 
 
6. If the tag for which the closure request is being submitted has pending dues, then the 
customer will be first asked to clear the pending dues. 
7. Once the request is submitted the Customer tag shall be closed and final settlement amount 
shall be credited to Bank account of customer’s choice within 15 working days after the date 
of submission of valid closure request.  
8. In the mean-while customer may apply for a new NETC FASTag from the same/different issuer 
member and sub-member. 
 
ii. 
Special Case (for aforesaid mentioned point no. c): 
Death of the vehicle owner: 
1. The next of kin may apply for the tag closure with relevant proofs as per the requirement 
of issuer member and sub-member.  
2. The next of kin has to Confirm the removal and disposal of NETC FASTag from vehicle.  
3. Once the request is submitted the Customer tag shall be closed and final settlement 
amount shall be credited to Bank account of nominee’s choice within 15 working days 
after deduction of pending dues and the date of submission of valid closure request.  
4. In the mean-while customer may apply for a new NETC FASTag from the same/different 
issuer member and sub-member. 
 
Customer has brought a car with existing Tag in Negative Balance or where previous 
owner is not reachable 
1. Customer who has bought the vehicle has to submit a copy of ownership transfer/ RC 
Copy to existing Issuer member and sub-member of the old customer along with other 
documents as specified by respective issuer member and sub-member.  
2. Customer has to confirm the removal and disposal of NETC FASTag from vehicle. 
3. Issuer member and sub-member shall verify records and close the existing tag after 
clearing the pending dues/claims with previous owner within 15 working days after the 
date of submission of valid closure request.  
4. Customer may apply for a new NETC FASTag from the same/different issuer member and 
sub-member once the previous negative balance tag is closed. 
 
Forceful tag suspension where Customer has opted for a new tag by a new issuer without 
requesting the previous issuer for tag closure. 
1. NPCI will suspend the old tag as soon as any new tag is issued 
a. Customer visits new issuer member and sub-member issuance channels and gets 
a new tag 
b. Once the new tag is issued, NPCI will Mark all older tags in Low Balance (03) (In 
addition to existing tag exception code). NPCI shall also update the existing issuer 
member and sub-member via API and EOD SFTP file. (Development and 
certification required at NPCI and Issuer member and sub-member)

<!-- Page 4 -->

 
 
 
c. Issuer member and sub-member shall facilitate customer communication for 
consent at a frequency of 3 days. Issuer member and sub-member to facilitate 
any tag closure proactively being initiated by customer. 
d. If customer provides consent, then follow the tag closure process (as pt. i. Policy 
for Consumers in case of Tag Closure) and close the tag within 15 days of new tag 
being issued. 
e. If customer tag is not closed by issuer member and sub-member within 15 days, 
NPCI will mark the tag as 06 after 15 days of new tag issuance. NPCI will do so 
only in case of existing tag being in Active/Low Balance. NPCI will only act upon a 
hotlisted/Blacklisted Tag as soon as it is removed from the Hotlist/Blacklist. 
f. If customer raises a dispute on new tag issuance, then the same shall be notified 
to NPCI. These cases shall be taken up in Panel for Resolution of Disputes for 
conclusion and penalty be levied on defaulting Party. (Pt. C. for Penalty) 
Policy for Issuer member and sub-members/ Entities: 
Scenario 
Actions 
Responsibility – Issuer member and sub-
member 
Tag Closure  
 
Below Actions to be taken for “Tag 
Closure” 
1. Customer to confirm removal of 
the NETC FASTag from vehicle on 
issuer member and sub-member 
portal / physically along with 
Account details (for refund) and 
other relevant documents (as 
specified by the Bank). 
2. Issuer member and sub-member 
to show a disclaimer for debiting 
wallet 
for 
any 
pending 
transactions 
and 
debit 
adjustments occurring on the 
current NETC FASTag from wallet 
before final settlement of refund. 
3. Issuer member and sub-member 
to refund the applicable net 
amount to Customer’s choice of 
Bank Account/ or linked issuer 
member 
and 
sub-member 
Current/ Savings account, post 
receipt of relevant documents as 
received by bank 
 
1. Provide relevant forms and refund  
details to Customer for NETC FASTag 
refund in the Customer Portal. 
2. Confirm that the NETC FASTag is not 
Hotlisted/ Blacklisted and new NETC 
FASTag for the same can be issued, 
except in case of vehicles that are 
already blacklisted. 
3. For Hotlisted NETC FASTags –
Banks/Customers may handle the 
process of removing NETC FASTags 
from Hotlist after recovery of the 
balance due from the customer. 
4. Mark the Tag as Low balance (03) 
immediately after receipt of a valid 
closure request. 
5. Support any transactions till a period 
of T+3 days after receipt of tag 
closure 
request 
and 
debit 
adjustments for T+10 (5 days for DA 
and rest for chargeback and buffer) 
days. Transactions raised after the 
above mentioned SLA will be 
declined by NPCI switch.

<!-- Page 5 -->

 
 
 
Scenario 
Actions 
Responsibility – Issuer member and sub-
member 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
6. If the tag goes into Negative balance 
due to transactions and Debit 
adjustments received till above 
mentioned SLA, Issuer member and 
sub-member shall Mark the tag as 
Hotlist (01) till pending dues are 
recovered. 
7. If the tag is in Low Balance (03) after 
the period of above mentioned SLA 
or the customer has cleared all the 
pending dues, the issuer member 
and sub-member shall mark the 
respective Tag in Tag Closed (06) 
within T+15 days 
8. Refund the money to the Customer 
as per Customer’s choice, if the NETC 
FASTag is not Hotlisted/ Blacklisted 
within a period of T+15 days. 
It is the responsibility of issuer member and 
sub-member (same issuer member and sub-
member) to ensure two active tags cannot 
be issued for the same VRN number. 
1. Special 
Case: 
Death 
of 
existing owner 
1. Customer’s next of kin to remove 
the NETC FASTag from vehicle 
and confirm the same to Issuer 
member and sub-member along 
with Account details (for refund), 
death certificate, and other 
relevant documents (as specified 
by the Bank). 
2. Issuer member and sub-member 
to refund the applicable net 
amount to the Bank Account/ 
wallet of the customer’s nominee 
as per existing RBI guidelines. 
1. Issuer member and sub-member  
a. Provide relevant forms to Customer 
for release of payment. 
b. Confirm that the NETC FASTag is not 
Hotlisted/ Blacklisted and new NETC 
FASTag for the same can be issued, 
except in case of vehicles that are 
already blacklisted. 
c. For Hotlisted NETC FASTags –
Banks/Customers may handle the 
process of removing NETC FASTags 
from Hotlist after recovery of the 
balance due from the customer. 
d. Refund the money to the Customer 
as per Customer’s choice, if the NETC 
FASTag is not blacklisted.  
e. For blacklisted NETC FASTags – no 
refund and the same is intimated to

<!-- Page 6 -->

 
 
 
Scenario 
Actions 
Responsibility – Issuer member and sub-
member 
Customer, the new owner of the 
Vehicle may procure a NETC FASTag 
if there are no dues pending after 
getting No Objection Letter from 
blacklisting entity 
2. Special Case: Vehicle mapped 
past tag of earlier vehicle 
owner is Hotlisted or where 
previous 
owner 
is 
not 
reachable 
 
1. Customer to submit a copy of 
ownership transfer/ RC Copy to 
Issuer member and sub-member 
along with other documents.  
2. Issuer member and sub-member 
to verify records and issue new 
NETC FASTag to the Customer 
after 
clearing 
the 
pending 
dues/claims 
with 
previous 
owner. 
1. Issuer member and sub-member  
a. 
Confirm ownership transfer. 
b. 
Remove the tag from 01 exception 
code after recovering the pending 
dues and add the existing tag to 06 
exception code.  
c. 
Issue a new NETC FASTag to the 
Customer, as per existing processes. 
3. Forceful 
tag 
suspension 
where Customer has opted 
for a new tag by a new issuer 
without 
requesting 
the 
previous 
issuer 
for 
tag 
closure. 
NPCI will suspend the old tag as soon 
as any new tag is issued 
 
a. Customer 
visits 
new 
issuer 
member 
and 
sub-member 
issuance channels and gets a new 
tag 
b. Once the new tag is issued, NPCI 
will Mark all older tags in Low 
Balance (03) (In addition to 
existing tag exception code). NPCI 
shall also update the existing 
issuer member and sub-member 
via API and EOD SFTP file.  
 
a. Issuer member and sub-member shall 
facilitate customer communication for 
consent at a frequency of 3 days. Issuer 
member and sub-member to facilitate 
any tag closure proactively being 
initiated by customer. 
b. If customer provides consent, then 
follow the tag closure process (as pt. i. 
Policy for Consumers in case of Tag 
Closure) and close the tag within 15 days 
of new tag being issued. 
c. If customer tag is not closed by issuer 
member and sub-member within 15 
days, NPCI will mark the tag as 06 after 
15 days of new tag issuance. NPCI will do 
so only in case of existing tag being in 
Active/Low Balance. NPCI will only act 
upon a hotlisted/Blacklisted Tag as soon 
as 
it 
is 
removed 
from 
the 
Hotlist/Blacklist. The action taken by 
NPCI will be communicated to Banks via 
API and SFTP. 
d. If customer raises a dispute on new tag 
issuance, then the same shall be notified 
to NPCI. These cases shall be taken up in

<!-- Page 7 -->

 
 
 
Scenario 
Actions 
Responsibility – Issuer member and sub-
member 
Panel for Resolution of Disputes for 
conclusion and penalty be levied on 
defaulting Party. (Pt. C. for Penalty) 
 
B. Tag Replacement 
 
The customer may apply for tag replacement in the scenarios where: 
1. Current tag is damaged/not working 
Policy for Consumers 
1. Access the issuer member and sub-member portal for NETC FASTag replacement. Customer 
can also call the issuer member and sub-member customer care/ toll free number or write to 
Issuer member and sub-member email support for replacement of the NETC FASTag. 
2. In case customer goes to the bank portal / Customer Care No, he has to select the Tag 
Replacement option. 
3. Customer has to submit the relevant documents as per bank portal for replacement NETC 
FASTag image. 
4. In case of replacement, the residual amount will be transferred into new NETC FASTag (which 
will be assigned to the customer). 
5. Customer has to confirm the removal and disposal of NETC FASTag from the vehicle by 
providing consent on portal / form. 
6. If the tag for which the replacement request is being submitted has pending dues, then the 
customer will be first asked to clear the pending dues and the tag will be marked as (03).  
7. Customer wallet will be debited for transactions* occurring on the respective tag till T+10 
days.  
8. Customer will be issued a new tag which will be delivered via courier within 7 working days. 
 
Policy for Issuer member and sub-members/ Entities: 
Scenario 
Actions 
Responsibility – Issuer member and sub-
member 
Tag Replacement 
Issuer member and sub-member may 
ask for submitting relevant proof and 
issue fresh NETC FASTag after 
verification under same wallet so that 
customer can utilise the available 
account balance. 
1. Provide relevant forms and return 
details to Customer for NETC FASTag 
refund in the Customer Portal. 
2. Confirm that the NETC FASTag is not 
Hotlisted/ Blacklisted and new NETC 
FASTag for the same can be issued, 
except in case of vehicles that are 
already blacklisted.

<!-- Page 8 -->

 
 
 
Scenario 
Actions 
Responsibility – Issuer member and sub-
member 
3. For 
Hotlisted 
NETC 
FASTags 
–
Banks/Customers may handle the 
process of removing NETC FASTags 
from Hotlist after recovery of the 
balance due from the customer. 
4. Mark the Tag as Low balance (03) 
immediately after receipt of a valid 
replacement request. 
5. Support any transactions till a period of 
T+3 days after receipt of tag closure 
request and debit adjustments for T+10 
(5 days for DA and rest for chargeback 
and buffer) days. Transactions raised 
after the above mentioned SLA will be 
declined by NPCI switch. 
6. Issuer will issue a replacement tag to 
the customer and deliver the same via 
courier within 7 working days’ post 
receiving the replacement request.  
 
Please Note: It is the responsibility of issuer member and sub-member (same issuer member and sub-
member) to ensure two active tags shall not be issued for the same VRN. 
C. Penalty: 
After implementation of above, if it came to the notice of NPCI where issuer members and sub-
members or their Third Party Agent has done some malpractice w.r.t the issuance of NETC 
FASTag to a particular vehicle (on which a NETC FASTag has already been issued), following 
penalty will be levied onto the issuer member and sub-member.  
Instance 
Penalty 
1st  
INR 5 Lakh 
2nd  
INR 10 Lakh 
3rd  
INR 15 Lakh 
4th  
Bank will be disallowed for a period of 6 month to participate in NETC 
FASTag ecosystem 
 
The cases of disputes due to Tag replacement / incorrect tag issuance will be referred to NETC Steering 
Committee for further action.

<!-- Page 9 -->

 
 
 
Annexure 2: FAQ’s for NETC FASTag Closure and Replacement Policy 
Common FAQ’s 
1. What is the NETC FASTag Closure and Replacement Policy? 
Ans. It is a policy to standardise customer journey for NETC FASTag closure and replacement if 
in case customer wishes to close/replace their tag. 
2. In which scenarios is the policy applicable? 
Ans. The policy is applicable in following scenarios: 
 
Customer wants to/has sold their existing vehicle 
 
Customer wants to opt for a different issuer bank and hence is applying for closure of 
existing tag 
 
Special Case 
o Next of kin applying due to death of existing customer 
o Customer has bought a car with an existing tag 
o Forceful tag suspension where customer has opted for a new tag by a new issuer 
without requesting the previous issuer for tag closure 
 
Customer wants a replacement tag as the existing tag is damaged/not working 
FAQs for Banks 
3. Will the banks have to initiate tag closure? 
Ans. Bank will only proceed for tag closure/replacement if the customer initiates the same. The 
entire process needs to be completed within 15 days of customer submitting a valid 
closure/replacement request. 
4. What are the steps to be taken by bank to be compliant with the policy circular? 
Ans. Scenario wise steps to be taken by bank is mentioned in detail in the policy document. 
FAQs for the Consumers 
5. Do I need to close all my existing tags and mandatorily get a new tag issued for my vehicle 
after release of this circular? 
Ans. No. It is not required to close all existing tags and get a new tag. However, it is advised to 
close all your inactive tags and keep only one active tag linked with one vehicle in the system. 
6. Do I need to close all my older tags before applying for a new tag for my vehicle? 
Ans. Yes. It is recommended that you close all your older tags before getting a new tag issued as 
it will help in mapping one active tag with one vehicle. However, if in case you donot close all your 
older active tags, the system will automatically suspend your older active tags within 15 days after 
a new tag is issued on our vehicle. The same shall come into effect from 1st December 2023. 
Please note that while your older tags will be suspended, your tag linked wallet will still remain 
active. The wallet owner will have to initiate wallet closure process with the respective issuer bank 
if he/he wishes to close the same and get a refund of available balance.

<!-- Page 10 -->

 
 
 
7. How do I check the list and status of the tags linked to my vehicle? 
Ans. You can check the list of tags linked with your vehicle and their status on following link: 
https://www.npci.org.in/what-we-do/netc-fastag/check-your-netc-fastag-status 
8. What will happen to my balance funds if my tag is closed? 
Ans. Customer will be asked to submit the account details for refund of balance account when 
they initiate the process. In case of forceful tag suspension, the funds will be credited to the 
source account used while doing the recharge if the bank decides to close the tag linked PPI 
wallet as well. If not, you may contact the respective issuer bank. 
9. What is the procedure to be followed to initiate Tag Replacement/closure? 
Ans. The policy details the procedure to be followed by bank as well as customer. You may refer 
to respective issuer bank website to initiate the same. 
10. What is the Turn Around Time for Tag Closure/Replacement and for my funds to be 
refunded? 
Ans. The maximum TAT is of 15 days to complete tag closure/replacement and to process the 
funds back to customer. 
11. How and where can I request for my existing tag closure? 
Ans. You may visit your issuing bank’s website/ Mobile application to initiate NETC FASTag 
closure for your existing tag.
