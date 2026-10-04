# NETC | OC 001 | FY 25-26 | Implementation of new Exception Code

Circular/reference number: NPCI/2025-26/NETC/001
Date: 27th June 2025

<!-- Page 1 -->

 
 
 
 
 
1001A, The Capital, B Wing, 10th Floor,   
Bandra Kurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101  
contact@npci.org.inwww.npci.org.in   
CIN: U74990MH2008NPL189067   
NPCI/2025-26/NETC/001 
                                                                              27th June 2025 
To, 
All Members participating in NETC Product 
Dear Sir/Madam, 
Subject: Implementation of New Exception Codes in NETC Ecosystem 
With reference to the Gazette Notification number CG–DL-E-18062025- 263948 dated 17th June 
2025 (attached as Annexure 1), the Ministry of Road Transport and Highways (MoRTH) has 
announced the launch of the Annual Pass scheme. This pass, when activated on a FASTag, 
facilitates toll-free passage for private cars/jeeps/vans at designated National Highway (NH) and 
National Expressway (NE) fee plazas for a period of one year or up to 200 trips (whichever occurs 
earlier), without any per-trip user fee charges. The scheme will be effective from 15th August 2025. 
In parallel, MoRTH/NHAI has also commenced the implementation of the Multi Lane Free Flow 
(MLFF) system at selected toll plazas across the National Highways network. 
MLFF aims to enable seamless toll collection using RFID and ANPR technology, replacing physical 
barriers. Under this model, all vehicles will be allowed to pass through the toll plaza, and an e-
Notice will be raised for toll payment for FASTag with insufficient balance post-facto. 
To enable smooth implementation of both the Annual Pass scheme and the MLFF system, NPCI 
is introducing two new exception codes in the NETC framework, as detailed below: 
Code 
Category 
Description 
07 
Pass  
Annual Pass Holders 
08 
E-notice  
Pending E-Notice beyond defined period 
 
These enhancements are aimed at standardizing exception handling and improving overall 
operational efficiency across the NETC ecosystem.

<!-- Page 2 -->

 
 
 
 
 
1001A, The Capital, B Wing, 10th Floor,   
Bandra Kurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101  
contact@npci.org.inwww.npci.org.in   
CIN: U74990MH2008NPL189067   
Key Implementation Guidelines: 
• 
The updated exception code priorities and handling logic are detailed in Annexure 2. 
• 
Issuer and Acquirer systems must be updated to support the new codes, including API 
integration and tag exception management. 
• 
Exception Code 07 – Annual Pass will be managed centrally by NPCI. The Annual Pass 
scheme shall not be applicable for the State Highways, Parking plazas and any other use 
case of FASTag. 
• 
Codes 08 will require Issuer Banks to maintain comprehensive audit trails and support 
removal based on resolution status. 
Timelines: 
• 
The implementation of the exception code 07 must be completed by 30th June 2025 and 
the exception code 08 by 31st July 2025 
• 
All member banks/entities are requested to confirm their readiness for Exception Code 07 
implementation by 29th June 2025. 
You are kindly requested to circulate this communication to all relevant teams within your 
organization and ensure adherence to the specified timelines. 
Yours faithfully, 
SD/- 
Kunal Kalawatia, 
Chief of Product 
Enclosed: Annexure 1 & 2

<!-- Page 3 -->



<!-- Page 4 -->



<!-- Page 5 -->

 
 
 
 
 
1001A, The Capital, B Wing, 10th Floor,   
Bandra Kurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101  
contact@npci.org.inwww.npci.org.in   
CIN: U74990MH2008NPL189067   
Annexure 2 
Exception Code Summary - Description and Priority: 
Code 
Category 
Description 
NH 
Priority 
SH/Parking/any 
other use case 
of FASTag 
Priority 
01 
Hot List 
Tags 
in 
negative 
balance 
or 
with 
violations 
3 
3 
02 
Exempted 
Tag exempted as per NHAI/MoRTH 
guidelines  
2 
2 
03 
Low Balance Tag 
with 
account 
balance 
below 
threshold 
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
07 (new) 
Pass 
Annual Pass holder 
2 
Ignore 
08 (new) 
E-notice 
Pending E-notice beyond defined time 
1 
1 
 
Exception Handling Mechanism and operating guidelines for Acquirer Banks/ Entities on 
New Exception codes will be as follows:  
1. NPCI will continue to share the exception status of tags with Acquirer Banks using the 
existing mechanism i.e. using Request Detail API, Query Exception API, Get Exception 
API and SFTP files (both consolidated as well as incremental)

<!-- Page 6 -->

 
 
 
 
 
1001A, The Capital, B Wing, 10th Floor,   
Bandra Kurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101  
contact@npci.org.inwww.npci.org.in   
CIN: U74990MH2008NPL189067   
2. Acquirer Banks must ensure that the tags with exception code 01 (Hotlist), 03 (Low 
Balance), 05 (Blacklist), 06 (Closed/ Replaced) and 08(E-notice) are not allowed to 
transact on any of the merchant sites or NETC FASTag acceptance points. 
3. Acquirer Banks must ensure that the tags with exception code 02 (Exempted) and 04 
(Invalid Carriage) are exempted from all toll user fee (NH and SH). 
4. Acquirer Banks must ensure that tags marked with Exception Code 07 (Pass) are 
exempted from all toll user fees on National Highways (NH) only, as ref. above. For State 
Highways (SH) and Parking Plazas and any other use case of FASTag, if a tag carries 
only Exception Code 07, it should be treated as Code 00 (Active), however, if Code 07 is 
present alongside any other exception code, then Code 07 must be ignored, and the 
other applicable exception code(s) shall be processed as per standard protocol. 
 
Operating Guidelines for new Exception Codes  
1. Exception Code 07 – Pass (Annual Pass Holders) 
• 
Addition: 
o 
Exception Code 07 is centrally managed by NPCI. 
o 
Tags meeting the eligibility criteria (i.e., valid Annual Pass holders) will be 
automatically updated with Exception Code 07 by NPCI. 
o 
Acquirers will receive this status via the standard NPCI interfaces (APIs/SFTP). 
• 
Removal: 
o 
NPCI shall centrally remove Exception Code 07, for following scenario: 
▪ 
Expiry of the Annual Pass validity period, or 
▪ 
Completion of the 200-trip limit (whichever is earlier), or 
▪ 
Revocation/withdrawal of the pass for any other authorized reason. 
o 
Upon removal by NPCI, corresponding updates will be disseminated to all 
stakeholders, and entities must ensure timely reflection of the revised tag status 
within their respective systems.

<!-- Page 7 -->

 
 
 
 
 
1001A, The Capital, B Wing, 10th Floor,   
Bandra Kurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101  
contact@npci.org.inwww.npci.org.in   
CIN: U74990MH2008NPL189067   
• 
Special Note: 
o 
In cases where Exception Code 07 is present alongside another exception code 
(e.g., Code 01 – Blacklist, or Code 03 – Low Balance), State Highways (SH), 
Parking plazas and any other use case of FASTag must ignore Code 07 and take 
action based on the other active exception code(s). 
o 
For SH, Parking plazas and any other use case of FASTag, if Code 07 is the only 
exception, it must be treated as Code 00 (Active), and the tag should be 
processed as a regular valid FASTag. 
o 
 When a ReqPay (Request for Payment) transaction is initiated for a tag marked 
with Exception Code 07, it must be processed strictly as a non-financial 
transaction, ensuring no user fee deduction takes place. 
 
2. Exception Code 08 – E-notice (Pending Enforcement Notices): 
• 
Addition: 
o 
Issuer Members may flag a tag under Code 08 if an enforcement notice (e.g., e-
notice) is pending beyond a defined period. 
o 
Acquirers will receive this status via the standard NPCI interfaces (APIs/SFTP). 
• 
Removal: 
o 
Once the pending notice is resolved, Issuer Members must promptly remove the 
tag from Code 08. 
o 
Issuer Members must maintain audit logs for addition and removal. 
o 
Removal updates should reflect in NPCI APIs and SFTP. 
• 
System Requirements: 
o 
Exception tags under Code 08 should not be allowed to transact across any NH, 
SH Toll plazas, Parking and any other use case of FASTag.
