# NETC I OC008 I FY 2021-2022 I Tag issuance process for Issuer Bank Entity and addition of New exception codes in NETC Ecosystem

Circular/reference number: NPCI/2021-22/NETC/008
Date: 24th March, 2022

<!-- Page 1 -->

 
 
 
 
 
1001A, The Capital, B Wing, 10th Floor,   
Bandra Kurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101  
contact@npci.org.inwww.npci.org.in   
CIN: U74990MH2008NPL189067   
NPCI/2021-22/NETC/008 
 
 
 
 
 
 
       24th March, 2022 
To, 
All Members participating in NETC Product 
Dear Sir/Madam, 
Subject: Tag issuance process for Issuer Bank/Entity and addition of New exception codes 
in NETC Ecosystem 
NETC ecosystem has grown exponentially in the recent times. Today, NETC is operational with 
48 Mn FASTags on 1000+ toll plazas, including 200+ toll plazas on State Highways and an 
additional of 53 Parking Plazas across the country. 
To manage the tag status at plazas and to ensure fast movement, it was adopted to have 3 
exception codes (Blacklist, Low Balance and Exempted). However, with the increased size of the 
NETC FASTag registered user base, NPCI has created additional exception codes to manage the 
tag status in a more structured way.  
The additional exception codes are: Hotlist, Closed/ Replaced and Invalid Carriage.  
NETC Stakeholders are requested to incorporate this update in the ecosystem as per the attached 
guidelines (Refer Annexure 1). The new guidelines will be implemented from 30th June 2022.  
Please note that additional certification is not required to be completed by Banks/ Entities. All the 
Member Banks/ Entities would be required to share confirmation of readiness by 29th June 2022. 
Kindly make a note of contents herein and disseminate the same to the relevant stakeholders. 
For any queries or clarification, please contact the following officials: 
Name 
E-Mail ID 
Mobile Number 
Vipeesh Kumar 
vipeesh.kumar@npci.org.in 
9892227037 
Avishkar Ghogare 
avishkar.ghogare@npci.org.in 
9370085186 
 
Yours faithfully, 
SD/- 
Kunal Kalawatia, 
Chief of Product 
Enclosed: Annexure 1

<!-- Page 2 -->

 
 
 
 
 
1001A, The Capital, B Wing, 10th Floor,   
Bandra Kurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101  
contact@npci.org.inwww.npci.org.in   
CIN: U74990MH2008NPL189067   
Annexure 1 
Proposed Process: 
Following is the list of new exception codes incorporated by NPCI: 
Exception 
Code 
Category 
Definition 
Priority 
01 
Hotlist 
Tags in negative balance or Tags with violations. 
1 
02 
Exempted 
Tag exempted from toll fare as per NHAI/MoRTH 
guidelines except for tags of vehicles belonging to 
customer with physical disability. 
2 
03 
Low Balance 
Tag with customer account balance below minimum 
threshold limit but not in negative balance. 
3 
04 
Invalid Carriage 
Tag of vehicle owned by customer with physical 
disability. 
2 
05 
Blacklist 
Tag Blacklisted by RBI, IHMCL/NHAI, Central/State 
law enforcement, police, defense etc. 
1 
06 
Closed/ 
Replaced 
Tag of customer who closes account, surrenders tag 
or switches to a new Issuer bank/ entity. 
1 
 
Operating guidelines for addition or removal of a tag in respective exception codes will be 
as follows: 
1. 
Hotlist (01): 
a. The current exception code description and definition of 01 code will be changed to Hotlist. 
b. All existing 01 tags will remain in the same exception code. 
c. Henceforth, a tag can be added in 01 only by respective Issuer bank [own registered tag 
only]. 
d. A tag can be added/ updated in 01 by respective Issuer bank only if a tag is in negative 
balance or vehicle mapped to the tag is in violation of NETC Procedural guidelines. 
e. A tag can be removed from 01 only by the respective Issuer bank. 
f. A new tag cannot be added in 01 while Tag registration. 
g. A new tag cannot be assigned to a vehicle if its mapped tag is present in 01 exception.

<!-- Page 3 -->

 
 
 
 
 
1001A, The Capital, B Wing, 10th Floor,   
Bandra Kurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101  
contact@npci.org.inwww.npci.org.in   
CIN: U74990MH2008NPL189067   
2. Exempted (02): 
a. All existing 02 tags will remain in the same exception code. 
b. Henceforth, a tag can only be added/updated in 02 by specific authorized Issuers as per 
notification from IHMCL. 
c. A tag cannot exist in 04 exception code if it is already in 02 exception code. 
3. Low Balance (03): 
a. A tag can be added/ updated in 03 by respective Issuer bank only [own registered tag only]. 
b. A tag can be removed from 03 only by the respective Issuer bank. 
4. Invalid Carriage (04): 
a. A tag can only be added/updated in 04 by specific authorized Issuers as per notification 
from IHMCL. 
b. A tag cannot exist in 02 exception code if it is in 04 exception code. 
c. The vehicles with 04 exception code will be exempted from toll fees on all toll plazas and 
will imitate the behaviour of 02 exempted tags in NETC ecosystem. 
d. Any ReqPay transaction in Merchant Type Toll for 04 Invalid carriages should be with 
transaction type NONFIN and amount Zero. The toll transactions should be declined 
otherwise. 
e. For other merchant types, transactions for 04 invalid carriages can be Debit, Credit, Non-
fin with zero or nonzero amount. 
5. Blacklist (05): 
a. A Tag can be added in 05 blacklist only by respective Issuer bank [own registered tag only] 
after direction from NPCI based on notification by RBI, GOI or any Law and Enforcement 
Agency in India. 
b. A tag with invalid IIN or an unregistered IHMCL/NHAI tag can be added in exception code 
05 Blacklist by any acquirer bank. 
c. A new tag cannot be added in 05 while tag registration. 
d. A new tag cannot be assigned to a vehicle if its mapped tag is present in 05 exception. 
6. Closed/ Replaced (06): 
a. A tag can be added in 06 only by respective Issuer bank [own registered tag only] after 
removing the tag from all the existing exception codes. 
b. Once a tag is added in 06 exception code, the tag cannot be removed from 06 or added in 
any other exception code. 
c. A new tag cannot be added in 06 while tag registration.

<!-- Page 4 -->

 
 
 
 
 
1001A, The Capital, B Wing, 10th Floor,   
Bandra Kurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101  
contact@npci.org.inwww.npci.org.in   
CIN: U74990MH2008NPL189067   
Exception Handling Mechanism and operating guidelines for Acquiring Banks/ Entities on 
New Exception codes will be as follows: 
1. 
NPCI will continue to share the exception status of tags with acquiring banks/entities using 
the existing mechanism i.e. using Request Detail API, Query Exception API, Get Exception 
API and SFTP files (both consolidated as well as incremental). 
2. 
Acquiring banks have to ensure that the tags with exception code 01 (Hotlist), 03 (Low 
Balance), 05 (Blacklist) and 06 (Closed/ Replaced) are not allowed to transact on any of the 
merchant sites or NETC FASTag acceptance points. 
3. 
Acquiring banks have to ensure that the tags with exception code 02 (Exempted) and 04 
(Invalid Carriage) are exempted from all toll fares as per the existing government guidelines. 
The Tag Issuance and registration Process for Issuing Banks/ Entities is as follows: 
1. 
Issuer Bank/ Entity should validate all the customer details and vehicle details (Vehicle 
Registration Number, Vehicle Identification Number, Engine Number, Gross Vehicle weight, 
Vehicle Type etc.) against the valid proofs before registering the details in Issuer database 
and NETC Database. 
2. 
Issuer Bank/ Entity should ensure that the tag details are registered in NETC database as 
soon as the same are registered in Issuer database. 
3. 
Issuer Bank/ Entity should ensure that one vehicle is being registered with only one tag by 
them on same day.
