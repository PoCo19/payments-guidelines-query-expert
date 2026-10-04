# Concept Note for Implementation of RuPay qSPARC based National Common Mobility Card

<!-- Page 1 -->

        
 
 
 
CONCEPT NOTE FOR 
IMPLEMENTATION OF RuPay qSPARC 
BASED NATIONAL COMMON 
MOBILITY CARD  
v 2.1 
National Payments Corporation of India (NPCI) 
Mumbai 
Abstract 
This document talks about the National Common Mobility Card (NCMC) Program and RuPay 
based on this NCMC Program. This also covers the Standard Operating Procedure for its 
implementation by Transit Operators (e.g. Bus, Metro), Para-Transit (Toll, Parking etc.), and 
Smart Cities. Proliferation strategy for Transit, Retail, Smart City, and Para-transit segments has 
also been discussed in this document.

<!-- Page 2 -->

 
 
 
Page 1 of 36 
 
Contents 
1 
Executive Summary ............................................................................................................................... 3 
2 
Purpose of the Document ..................................................................................................................... 5 
3 
Background ........................................................................................................................................... 6 
3.1 
Existing Payments Mechanisms .................................................................................................... 6 
3.2 
Challenges and Limitations ........................................................................................................... 6 
4 
National Common Mobility Card Program ........................................................................................... 7 
4.1 
Introduction .................................................................................................................................. 7 
4.2 
NCMC Proposition: EMV Open Loop Card with Stored Value ...................................................... 7 
4.3 
Brand Name for NCMC Cards ........................................................................................................ 9 
4.4 
Advantages of NCMC Open Loop Smart Card over Closed Loop Variant ..................................... 9 
5 
RuPay qSPARC based NCMC ............................................................................................................... 11 
5.1 
Key Features of RuPay qSPARC based NCMC ............................................................................. 12 
5.2 
Value Proposition of RuPay qSPARC based NCMC to Key Stakeholders .................................... 13 
6 
RuPay qSPARC based NCMC Implementation Model ......................................................................... 15 
6.1 
Sample NCMC Implementation Model (Bus Transport) ............................................................. 15 
6.2 
Key Consideration Points for Implementation Model ................................................................ 16 
6.3 
Required Activities for NCMC Implementation .......................................................................... 17 
6.4 
Roles & Responsibilities of Key Stakeholders ............................................................................. 18 
6.5 
Adoption of NCMC by Other Card Schemes ............................................................................... 20 
7 
Standard Operating Procedure for NCMC Implementation ............................................................... 21 
8 
Certifications & Compliances .............................................................................................................. 23 
8.1 
Issuer Bank Certification Requirements ..................................................................................... 23 
8.2 
Acquirer Bank Certification Requirements ................................................................................. 23 
8.3 
ETIM/Terminal Certification Requirements ................................................................................ 24 
8.4 
AFC Certification requirements (CDAC) ...................................................................................... 24 
9 
Commercial Pricing ............................................................................................................................. 25 
10 
NCMC Ecosystem Pilot at Delhi Metro Rail Corporation (DMRC) ................................................... 26 
10.1 
Roles & Responsibilities of Involved Stakeholders ..................................................................... 26 
10.2 
Key Highlights .............................................................................................................................. 26 
10.3 
Launch of One Nation One Card ................................................................................................. 27 
11 
RuPay qSPARC based NCMC Proliferation Strategy ........................................................................ 28 
11.1 
Transit Segments ......................................................................................................................... 28

<!-- Page 3 -->

 
 
 
Page 2 of 36 
 
11.1.1 
Role of Operators ................................................................................................................ 28 
11.1.2 
Role of Banks ....................................................................................................................... 30 
11.1.3 
Role of Card Scheme ........................................................................................................... 30 
11.1.4 
Role of Government ............................................................................................................ 31 
11.2 
Retail Segments........................................................................................................................... 32 
11.2.1 
Role of Merchant ................................................................................................................ 32 
11.2.2 
Role of Banks ....................................................................................................................... 32 
11.2.3 
Role of Card Scheme ........................................................................................................... 33 
11.2.4 
Role of Government ............................................................................................................ 33 
11.3 
Smart City Segments, Toll and Parking ....................................................................................... 33 
11.3.1 
Role of Smart City and Toll Operators ................................................................................ 33 
11.3.2 
Role of Banks ....................................................................................................................... 34 
11.3.3 
Role of Card Scheme ........................................................................................................... 34 
11.3.4 
Role of Government ............................................................................................................ 34 
12 
Further Information and Clarification ............................................................................................. 35 
13 
Annexures ....................................................................................................................................... 36

<!-- Page 4 -->

 
 
 
Page 3 of 36 
 
1 Executive Summary 
The digital penetration in retail segments is increasing gradually on card as well as mobile platforms 
with the holistic effort of financial institutions, customers, solution providers and government. 
However, the digital adoption is limited across low value payments in segments including retail, 
transit, toll, parking and smart cities. 
Key Requirements of the ecosystem are 
 
Need for offline transactions in low value payments - faster speed with near zero declines 
 
Need of payment solution which is independent of network connectivity 
 
Challenges in terms of existing banking infrastructure to support huge surge in digital 
transaction on account of low value payments digitization 
National Common Mobility Card (NCMC) program, as envisaged by MoHUA (Ministry of Housing & 
Urban Affairs), offers the above proposition and is proposed to be rolled out on RuPay Contactless 
Product (qSPARC). 
This card may be used for all payment applications (low value – offline/high value – online) including 
transit, retail, toll, parking and smart cities. The stored value of the card offers the offline transaction 
proposition across all low value segments. The additional feature of service area on the card may be 
used for any merchant specific application e.g. season tickets etc. Further, it is also feasible to provide 
targeted government incentives e.g. medicines, books etc. through NCMC. The card may be issued 
as Debit/ Prepaid/Credit Card.  
RuPay qSPARC based NCMC implementation is aimed at providing a vendor and bank agnostic digital 
payment platform wherein customers may use RuPay NCMC cards issued by any bank for digital 
payments across various segments. The implementation should ensure multi-bank cards are 
accepted wherein the customers should be able to use RuPay cards issued by any bank including local 
or small banks. 
Important factors in proliferation of RuPay qSPARC based NCMC requires default issuance by key 
banks in the country and deployment by operators with open loop compatible AFC and devices. Role 
of key stakeholders is as below:

<!-- Page 5 -->

 
 
 
Page 4 of 36 
 
 
Segments 
Merchant/Operator 
Banks 
NPCI/CDAC 
Government 
Transit 
and 
Smart 
Cities 
NCMC 
implementation for 
all greenfield 
projects. Phase-
wise upgradation 
for Brownfield 
projects 
Issuance of RuPay 
qSPARC based 
NCMCs as default 
Debit/Prepaid/Credit 
Cards to avoid any 
project specific 
issuance. 
Develop RuPay 
qSPARC based 
NCMC acceptance 
ecosystem across 
various merchants 
Specification 
support to involved 
stakeholders 
including 
operators, bank 
and vendors to 
develop the 
ecosystem  
Financial support for 
AFC/ETIMs and Transaction 
charges 
Mandates through respective 
Ministries for implementation 
of open loop RuPay qSPARC 
based NCMC and Interface 
Specification of NCMC 
compliant AFC System” 
 
Retail 
Acceptance of 
RuPay qSPARC 
based NCMCs 
Mandates for RuPay qSPARC 
based NCMC acceptance. 
Para-
Transit 
Acceptance of 
RuPay qSPARC 
based NCMCs for 
Toll & Parking 
 
 
NCMC was inaugurated by Honorable Prime Minister as One Nation One Card in Ahmedabad on March 
4th, 2019.

<!-- Page 6 -->

 
 
 
Page 5 of 36 
 
2 Purpose of the Document 
This document provides an overview of the National Common Mobility Card (NCMC) program, key 
features of NCMC specification, benefits to involved stakeholders and the use cases covering transit, 
toll, parking, smart cities and retail payments. This also covers various aspects related to NCMC 
implementation including sample implementation model, standard operating procedure (SOP) and 
roles & responsibilities of involved stakeholders. NCMC proliferation strategy has also been covered 
in this document to achieve higher adoption and penetration of the NCMC cards across all use cases.  
With the aim of digitizing the payments across each segments (low value as well as high value), a 
huge surge is expected in number of digital transactions which may have a challenge in view of 
existing banking infrastructure. This requires the offloading of low value transactions from real time 
processing by the bank. This will help to digitize the low value payments with near zero failures. 
RUPAY qSPARC based NCMC offers the additional feature of offline transactions for low value 
payments at a faster speed with near zero declines. This card may be used for all payment 
applications (low value as well as high value) including transit, retail, toll, parking and smart cities.

<!-- Page 7 -->

 
 
 
Page 6 of 36 
 
3  Background 
3.1 
Existing Payments Mechanisms 
The banking industry has evolved gradually during the last 3-4 decades with various payment 
solutions to digitize the retail payments. These solutions are mainly based on two platforms namely 
Card & Mobile. Card has been the preferred mode of payment in the physical space in view of the 
customer convenience, familiarity and consumer behaviour while the mobile platform has taken a 
significant leap during the last few years in the ecommerce channel.  
Apart from retail, there are various other segments involving low value payment e.g. transit (bus, 
metro, suburban railways), toll, parking etc. which are highly dominated by cash based tickets. The 
customer takes paper ticket by paying cash either at ticket counters or during journey. Various 
operators of these segments have implemented closed loop/semi-close loop cards based digital 
payment collection system. The lifecycle of such cards is being managed by respective operators. 
Few operators have also adopted the mobile based solution for digital fare collection.  
However, the digital adoption is very limited across these low value segments due to 
interoperability challenges of closed loop/semi-closed loop cards.  
3.2 
Challenges and Limitations 
The existing cash based payments practice for low value payments across various segments has 
multiple challenges e.g. cash handling, revenue leakages, pilferages etc. The adopted digital 
payments practice suffers from the key challenge in terms of interoperability and other challenges 
as mentioned below:- 
 
Closed loop/Semi-closed loop cards have usability limited to specific merchant/operators and 
hence customers need to carry multiple cards for multiple use cases. 
 
Popularity of these cards among citizens is limited due to restricted usage of the card and hence 
lower digital penetration. Moreover operators/merchants need to bear extra cost for life cycle 
management of the cards. 
 
In context of Indian scenario, where network connectivity is a challenge, any mobile based 
payment collection system will have limited digital penetration. 
 
Low value payments pose a huge challenge of volume, where transit alone generates close to 
10 crore transactions a day. Online authentication of such volumes can lead greater number of 
declines.In view of the above challenges and the need to drive the digital payments adoption 
across all segments with high as well as low value payments, there is a requirement of a 
common card payment system wherein a single card may be used for all payment applications 
including transit, toll, parking, smart cities and retail.

<!-- Page 8 -->

 
 
 
Page 7 of 36 
 
4 National Common Mobility Card Program 
4.1 
Introduction 
With vision of One Card for all Payment systems, Ministry of Housing & Urban Affairs (MoHUA) has 
come out with a National Common Mobility Card (NCMC) model to enable seamless payment for 
low value as well as high value payments across all use cases including travel by different metros 
and other transport systems across the country, retail shopping and purchases. A committee was 
formed with representatives of National Informatics Centre (NIC), Centre for Development of 
Advance Computing (C-DAC), Bureau of Indian Standards (BIS), National Payment Corporation of 
India (NPCI) and the Ministry of Finance. 
After extensive study of various models being followed across the world, the Committee 
recommended the EMV Open Loop Card with stored value based model and the same was 
approved. This card meets travel needs based on stored value of money and can be used for all low 
value payments including travel by any means of transport, smart cities, toll, parking etc. and also 
enables account based retail applications. Accordingly, this card does away with the need of 
carrying separate cards for banking and transit requirements. 
NPCI, CDAC and BEL has been working with MoHUA, Government of India for implementation of 
National Common Mobility Card Program (NCMC). This specification is dual interface (contact & 
contactless) EMV card based specification and is interoperable based on open standards. This is 
aimed at low value payments for various segments e.g. Transit, Smart cities, Toll, Parking and other 
low value merchant payments in addition to the normal day to day retail payments. These 
specifications are capable of supporting not only payment products but also transit applications like 
monthly passes, season tickets & government applications such as social security, driving license, 
Id/access card etc. This results in increased customer’s convenience as it allows customers to use 
the same card for variety of needs. 
4.2 
NCMC Proposition: EMV Open Loop Card with Stored Value 
The NCMC committee, as mentioned in above clause, identified the key requirements of this NCMC 
Card as Interoperability, Open Loop, EMV Chip, Offline transactions and minimum transaction time. 
Based on their requirements and study of international markets, the committee studied three 
models of proposition: 
 
Model 1 - Closed Loop based Solution 
 
Model 2 – EMV Open Loop Account based Solution  
 
Model 3 – EMV Open Loop Card with Stored Value

<!-- Page 9 -->

 
 
 
Page 8 of 36 
 
The comparative analysis of these three model are as mentioned below:- 
Particulars 
Model 1 – Closed Loop 
Model 2 – EMV Open Loop 
Account based 
Model 3 – EMV Open Loop 
with Stored Value 
Proposition 
 
Issuance of closed loop 
cards 
by 
respective 
Operators to digitize 
the payments 
 
Usage 
for 
services 
provided 
by 
the 
respective Operator 
 
Usage of bank issued EMV 
cards which are linked to 
account 
 
Fare calculation as well as 
debit from account to be 
done at the backend post 
processing 
of 
offline 
transactions by terminal 
 
Usage of bank issued 
EMV cards with stored 
value on the card 
 
Supports 
offline 
transaction 
without 
financial 
risk 
to 
Operator or Financial 
Institutions 
 
Provision 
of 
season 
tickets on the card 
Limitations 
 
Lacks the key feature 
of interoperability 
 
Restricted usability for 
services provided by 
the 
respective 
operator only 
 
Extra cost to operators 
in 
maintaining 
the 
payments mechanism 
and 
card 
lifecycle 
management 
 
Risk 
of 
insufficient 
balance on the card as the 
transactions are based on 
deferred authorization  
 
Challenge in storing the 
season tickets on the card 
 
Increased capex and opex 
due 
to 
manage 
the 
backend 
 
Challenge 
for 
Bank 
infrastructure to manage 
the large volume of low 
value transactions on real 
time basis 
- 
 
Considering the Indian Transit scenario, available infrastructure for bank & operators, market 
dynamics, feedback from financial institutions and the customer behavior; Model 3 – EMV Open 
Loop Card with Stored Value was finalized as the ideal model for NCMC Card.  
The Report of the committee for standards and specifications of National Common Mobility Card is 
available at link - http://mohua.gov.in/upload/uploadfiles/files/CommitteeReportofNCMC03.pdf.   
The NCMC specification may be adopted by all Payment Scheme Networks operating in the country 
as communicated by RBI.

<!-- Page 10 -->

 
 
 
Page 9 of 36 
 
4.3 
Brand Name for NCMC Cards 
The NCMC program has been envisaged with a vision of ‘One Card for all Payments’. In view of the 
same, the name of this card should portrait its usability across all segments for all types of payment 
applications including retail, transit, toll, parking and smart cities. This will help in wider awareness 
and acceptance of NCMC cards across the country.  
Please refer to RuPay branding guidelines for qSPARC based NCMC design compliance.   
4.4 
Advantages of NCMC Open Loop Smart Card over Closed Loop Variant  
NCMC open loop smart card offers various advantages over the closed loop smart card in terms of 
various parameters including customer experience, interoperability, infrastructure requirements, 
ease of implementation and vendor agnostic solutions. The details are as enumerated in below 
mentioned table: 
S. No. 
Concern 
Open Loop Smart Card 
Closed Loop Smart Card 
1 
Customer Friendly 
Customer may use the same card for Metro 
and Bus travel in all the City and States 
within the country.   
Customer need to buy different cards for 
different public transport Systems. 
2. 
Convenience 
Customers may use their bank issued NCMC 
card for fare payment rather than waiting in 
a queue for card/token/ticket issuance.  
Customer may require to stand in queue 
for card issuance, Top up etc. 
3. 
Loyalty Points 
 Consumer may benefit from loyalty/reward 
points from partner banks, as provided in 
case of Debit and Credit cards. 
No such provision. Any such loyalty and 
discount is a cost to the Public Transport 
Operators. 
4. 
Minimum 
Infrastructure 
Public Transport Operators can minimize 
their cost involved in    maintenance of 
infrastructure and manpower for card 
issuance, Top up, card replacement and 
refunds, as open loop cards can be issued by 
multiple partner banks.   
Each Public Transport Operators need to 
bear 
the 
significant 
expense 
for 
maintenance 
of 
infrastructure 
and 
manpower for card issuance, Top up, card 
replacement and refunds. 
5. 
Negotiating Power 
As open loop acceptance devices are based 
on open interoperable standards, there are 
multiple vendors available for payment 
acceptance devices, which provide an 
opportunity 
for 
cost 
and 
service 
negotiation. 
Closed loop cards may be of proprietary 
standards, leading to vendor lock in for 
subsequent purchase and renewals of 
acceptance devices. 
6. 
No vendor lock in 
Open standards based payment acceptance 
devices 
provides 
the 
freedom 
for   
subsequent purchase and renewals of 
devices. 
Proprietary standards may lead to vendor 
lock in for subsequent purchase and 
renewals of acceptance devices.

<!-- Page 11 -->

 
 
 
Page 10 of 36 
 
7. 
Ease 
of 
Implementation 
Well standardized payment acceptance 
devices   and availability of multiple vendors 
provides ease of implementation. Payments 
related scope of work to be taken care by 
partner bank and hence PTOs may focus on 
their key activities. 
PTOs need to evaluate multiple proprietary 
specifications leading to difficulty in 
implementation. 
8. 
Fast Deployment 
Due to similar implementation process, best 
practices and reference implementation 
guidelines, there will be standardized 
procurement practices, and RFPs. This 
considerably expedites the deployment of 
digital 
payments 
in 
Public 
Transport 
Operators. 
Each 
deployment 
will 
have 
specific 
requirements and considerable expertise is 
required 
by 
each 
Public 
Transport 
Operators for selection of appropriate 
solution. 
9. 
Retail acceptance 
NCMC open loop card offers acceptance at 
all the existing retail PoS devices. 
Closed loop cards can only be accepted 
within their operating environments.

<!-- Page 12 -->

 
 
 
Page 11 of 36 
 
5 RuPay qSPARC based NCMC 
RuPay qSPARC based NCMC offers the proposition of One Card for all Payment Systems wherein a 
single card may be used for all payment applications including transit, toll, parking, smart cities and 
retail. 
 
i. 
Multi-Modal Transit: RuPay qSPARC based NCMCs may be used across all transit modes 
including Metros, buses, ferries, suburban railways etc. A citizen would not be required to be 
dependent on cash or operator specific various closed loop cards. He can use one card for fare 
payment across any mode of public transport. 
ii. 
Toll: There are significant number of customers using cash lane at the toll plaza and making 
payment in cash. With the help of RuPay qSPARC based NCMC, a citizen may pay the toll 
charges at toll booths by simply tap & pay. This will help to achieve higher digital penetration 
in toll segment for customers using cash lane. 
iii. 
Parking: A citizen may use the RuPay qSPARC based NCMCs at parking zones for making 
payments of parking charges. This will help to reduce the transaction time and increase the 
digital payments penetration.  
iv. 
Smart Cities: Digital payments play a vital role in smart cities projects. A common card payment 
system is the key proposition of smart cities to enable usage of one card for all sorts of 
payments including transit, civic as well as non-civic payments in the cities. RuPay qSPARC 
based NCMCs offer the unique proposition for Common Card Payment System of smart cities.   
v. 
Retail: RuPay qSPARC based NCMCs may be used in contact as well as contactless mode for 
retail payments. The customer may use this card for low value payments as well as high value 
payments. As per RBI existing norms, 2nd factor authorization is not required for transaction 
below INR 2000. For such payments, the customer may make the payment by simply tap & pay. 
The offline transaction feature may also be leveraged to reduce the transaction time and

<!-- Page 13 -->

 
 
 
Page 12 of 36 
 
eliminate the dependency of network connectivity for extreme low value payments under INR 
200. 
MoHUA issued an advisory, vide Advisory No. 9, dated June 8th, 2017, advising all smart cities to 
follow the NCMC standards for implementation of common card payment system. This card is 
envisaged to be accepted in all kinds of public transport, para transit and non-transit services and 
other merchant payments like utility bills, taxes, shopping etc. The copy of advisory note is enclosed 
here as Annexure – A.   
Ministry of Electronics and Information Technology (MeitY) has issued following advisories 
recommending all Public Transport Operators to adopt open loop NCMC cards for digital fare 
collection,  
a) An advisory, vide No. 12(39)/2017-DPD, dated April 4, 2018enclosed here as Annexure –B.  
b) An advisory, vide No. 12(57)/2017-DPD, dated March 14th, 2019 enclosed here as Annexure 
–C 
c)  An advisory, vide No. 12(57)/2017-DPD, dated August 2nd, 2019 enclosed here as 
Annexure –D 
 
5.1  Key Features of RuPay qSPARC based NCMC 
Key Functionalities/Particulars 
NCMC Proposition 
Payment Model 
 
Card based payment model 
Transaction Type 
 
Supports online (contact & contactless) & off-line (contactless) 
transactions 
Stored Value 
 
Provision to store balance on card for offline payments 
Provision for multiple service areas 
 
Multiple service areas (optional to use with mutual concurrence) to 
support acquirer/operator specific programs e.g. Passes / Season 
Tickets / Smart City Specific application / Loyalty points etc. 
Card usage 
 
Same card to be used at ATMs, Merchant establishments & online 
(e-commerce) payments in addition to other areas of contactless 
payments viz., transit, toll, parking & other small value merchant 
payments 
Card issuance 
 
Can be issued by any member authorized by RBI; On the platform of  
o 
Debit Cards 
o 
Prepaid Cards 
o 
Credit Cards  
In future these cards may also be made available in various other form 
factors including wearables, stickers etc.

<!-- Page 14 -->

 
 
 
Page 13 of 36 
 
Topping up the stored value 
 
Provision of Topping up the stored value through any mode of 
payment viz. cash, account and online channels 
Offline Transaction Risk 
 
Since the offline transaction is permitted against stored value on 
card, there is minimal risk of any loss to the bank or merchant 
Security 
 
Underlying technology i.e. EMV is best available globally  
Cost of providing contactless card to 
the customer 
 
RBI has mandated that effective Feb 01, 2016, all cards issued by 
banks in India would be EMV. Therefore, cost of providing 
contactless card to the customer will be only marginal as against 
steep increase in territories where mag-stripe ecosystem exists 
Synergy with existing technology 
 
NCMC specifications can co-exist with the existing technology being 
used by acquirer/operator and migration to common standards may 
be achieved gradually to suit the convenience. 
 
5.2 Value Proposition of RuPay qSPARC based NCMC to Key Stakeholders 
Stakeholders 
Value Proposition 
Commuter/Consumer 
 
One card for all low & high value payments across various categories; No need to 
carry multiple cards for different usage 
 
Super quick with contactless transactions enabled on the card 
 
Digital trail for all transactions 
 
No need to stand in a queue 
 
Auto Top-up facility; need not to worry for recharge 
 
Secured with EMV Technology; Gold standard of card payments 
In 
vehicle 
Crew/ 
Counter Operators 
 
Low cash handling due to NCMC cards based fare collections 
 
Efficient fare collection process with the minimal transaction time  
 
Efficient crowd management  
 
Increased productivity

<!-- Page 15 -->

 
 
 
Page 14 of 36 
 
PTOs/Merchants 
 
Unified cards to support offline and online transaction modes; contactless ability 
 
Common standards for standardized operating cost 
 
Fast deployment of digital payments due to standardized implementation process 
 
Savings on card lifecycle management cost 
 
Reduced operating cost on account of lower cash handling, infrastructure & 
manpower cost 
 
Business intelligence with rich data insights aimed at business optimization and 
ROI based communication 
 
May run proprietary loyalty and VAS schemes with high convenience and customer 
satisfaction   
 
No vendor lock in due to open loop standard platform. 
Banks 
 
Customer loyalty & stickiness 
 
Additional revenue opportunities with large customer base 
 
Savings on cost of servicing customers and cash handling 
 
Increased usability of bank issued cards due to transit related use case 
 
Improved brand image to offer value added products/services 
 
Rich data insights with valuable customer data for data analytics and customized 
offers for customers 
Retail Ecosystem 
 
Usability of one card for all payments would encourage customer for digital 
payment in retail 
 
Cost on account of running loyalty cards may be reduced by leveraging the NCMC 
cards   
 
Tap & pay to enable efficient payment during peak hours for low value purchases 
 
Lifestyle experience to customers 
Government  
 
NCMC would help in digitizing the low value payments, a key segment highly 
dominated by cash payments in India  
 
Higher digital penetration to achieve the digital payments target  
 
Reduced leakages across the value chain of the system 
 
Reduced cash circulation in the economy 
 
May be leveraged to provide targeted government incentives e.g. medicines, 
books, travel passes etc. through NCMC

<!-- Page 16 -->

 
 
 
Page 15 of 36 
 
6 RuPay qSPARC based NCMC Implementation Model  
6.1 
Sample NCMC Implementation Model (Bus Transport) 
The NCMC implementation is aimed at providing a Vendor and Bank agnostic digital fare 
collection platform wherein the customers may use RuPay qSPARC based NCMCs 
(Debit/Prepaid/Credit Card) issued by any Bank for digital fare payments. This will help the 
customers to get associated with any bank as per their choice rather than being restricted to a 
single bank. The acceptance of RuPay qSPARC based NCMCs issued by multiple banks will further 
help to get the higher digital penetration for fare collection. 
A sample implementation model for State Road Transport Undertakings (SRTUs) – Bus Operators 
has been shown below for the reference purpose. The same concept will get extended across other 
segments including Metro, Toll, Parking and Smart Cities with modification as per their existing fare 
collection system.

<!-- Page 17 -->

 
 
 
Page 16 of 36 
 
6.2 
Key Consideration Points for Implementation Model 
With the Multiple Issuance Open Loop model, there will be following key benefits to the operators:-  
Tangible Benefits 
Intangible Benefits 
 
Significant reduction in OPEX associated with cash 
handling and leakages 
o 
Even with a large adoption of closed loop 
smart card benefits are passed on as 
discounts for operator issued cards and 
thus negate the above savings 
 
Reduction in OPEX related with card life cycle 
management 
 
CAPEX savings on the infrastructure since it 
invalidates the need of large scale card issuance and 
top infrastructure 
 
Higher adoption of digital payments 
 
Consumers benefits the most as they need not block 
their balances for each operator 
o 
A single prepaid account can work across 
all low value offline payments like bus, 
parking, retail 
o 
The cards can be easily topped up with 
their existing accounts through BHIM and 
used without any dedicated need of 
balance check counters 
 
Industry as a whole benefit due to availability of 
standard solutions and vendors 
 
  
The implementation model should ensure following key points to achieve the vision of 
interoperable, vendor/bank agnostic NCMC solution. 
 
Segregation of Ticketing engagement from Payment RFP 
 
Operators should approach AFC vendors for deployment of ticketing solution and application 
o Banks to be approached only for payment acquiring and settlement 
o Avoid CAPEX investment through an acquiring bank 
o The cost of the AFC/e ticketing  System including gate validators/ETIMs may either be 
picked up by the operator or the banks may provide a rental model to the operator 
 
As a short term option the acquiring bank may provide instant issuance of Rupay NCMC prepaid 
cards on a limited basis  only  
o Till such time every customer starts carrying an EMV open loop stored value card, 
acquiring bank may provide limited issuance 
 
Some of the operators may need support to their existing business operation challenges 
o Particularly in bus environment, it may be prudent to develop a regional AFC hub for 4-
5 operators combine

<!-- Page 18 -->

 
 
 
Page 17 of 36 
 
6.3 
Required Activities for NCMC Implementation 
S.No. 
Activity 
Description 
1 
AFC 
Deployment/Upgrade 
 
Upgrade of existing gate validators/ ETIMs with EMV devices certified as 
per NCMC specification 
o 
Level 1 (Hardware) to be certified as per EMVCo 
o 
Level 2 Kernel (Software) to be certified as per NCMC specs 
o 
Level 3 (Payment Application) to be certified as per NCMC specs  
 
Upgrade of AFC System including ETIMs/Gate as per Interface 
Specification of NCMC Ecosystem (Part IV – VII) 
 
Complete back-office deployment to support Automatic fare Collection 
System 
 
2 
Selection of Issuer Bank 
for instant Issuance of 
RuPay qSPARC based 
NCMCs 
at 
Service 
Delivery 
Points 
(if 
required) 
 
Responsible for issuance of NCMC Cards as per defined NCMC 
specification 
 
Multi-Banks Acceptance Model wherein customers may use NCMC cards 
issued by any certified bank 
 
The customers may get the NCMC cards from the bank of their own 
choice by visiting the respective branches or offices 
 
To facilitate the card issuance at Operator/Authority service points e.g. 
bus stops, depots etc., PTO need to select an Issuer Bank for instant 
issuance of NCMC cards 
3 
Selection of Acquirer 
Bank for acquiring of 
digital 
transactions 
done 
using 
RuPay 
qSPARC based NCMCs 
 
Responsible for acquiring of digital fare collection transactions done 
using NCMC cards issued by any certified Bank 
 
Acquirer Bank may be single or multiple as decided by Operator  
4 
Commercial Aspects 
 
Commercial Model to ensure the vendor/bank agnostic solution and 
Multi-Banks acceptance scenario wherein the customers should be able 
to use NCMC cards issued by any Bank including the local or small banks. 
 
As far as possible, the transaction charges should not be passed on to 
customer so that there is no resistance to digital adoption.

<!-- Page 19 -->

 
 
 
Page 18 of 36 
 
 
6.4 
Roles & Responsibilities of Key Stakeholders 
1. The roles & responsibilities of key stakeholders will be inclusive of but not limited to the 
following. It may vary as per the scope of work finalized by the Authority. 
Stakeholders 
Roles and Responsibilities 
Issuer Bank 
Issuer Bank issuing the RuPay qSPARC based NCMC enabled Debit/Prepaid/Credit 
Cards from their Branch networks 
 
Issuance and end to end lifecycle management of NCMC cards as a part of day to 
day normal banking activities for the Issuer Bank 
 
Shall provide various payment channels for the Card Top-up as per customer 
convenience  
 
Undertake transaction settlement and reconciliation with Acquirer Bank & Payment 
Schemes 
Instant Issuer Bank issuing the NCMC Cards from PTO Service Delivery Points (if 
required) 
 
Applicable only for cases wherein the Operators want to provide the NCMC cards 
instant issuance facility at Operator Service Delivery Points 
 
Procurement, personalization, instant issuance of Contactless cards based on NCMC 
specification as per RBI guidelines  
 
Shall provide various payment channels for the Card Top-up as per customer 
convenience  
 
Provide necessary EMV PCI-DSS compliant hardware for instant issuance related 
applications as per requirements 
 
Certifications & Compliances as per NCMC specification  
 
Provide helpdesk to customers for addressing any grievance or providing support in 
card usage  
 
Maintain entire life cycle management of NCMC cards issued by FI, card 
applications, payment scheme, card account management and card transactions 
 
Marketing, Loyalty, Fraud and Risk Management 
 
Admin console for Authority to access MIS reports etc. 
 
Provide an e-payment gateway and portal, Mobile Applications and SMS facilities 
for self-service and card top-up 
 
Undertake transaction settlement and reconciliation with Acquirer Bank & Payment 
Schemes 
 
Field training, hardware maintenance and consumables

<!-- Page 20 -->

 
 
 
Page 19 of 36 
 
Acquirer Bank 
 
Acquiring the digital fare collection transactions done using NCMC cards issued by 
any certified Bank 
 
Shall provide various payment channels for the Card Top-up on the web/mobile 
interface provided by the Authority/its vendor   
 
Provide EMV as well as PCI-DSS compliant hardware for acquiring related 
applications as per NCMC specifications 
 
Certifications & Compliances as per NCMC specification and Interface Specification 
of NCMC Ecosystem – Part VI 
 
Provide risk, fraud and dispute/chargeback capabilities  
 
Provide NCMC Card dedicated support to Issuer Bank with reference to transaction 
dispute, refunds, chargeback and merchant account management as per RBI 
requirements 
 
Provide Admin Console for Operators 
 
Manage email/SMS for citizens and merchants 
 
Undertake transaction settlement and reconciliation with Operators 
 
Operators/Merchants 
 
Provide manpower to all its Service Points 
 
Provide domain services and respective IT applications like ITMS, AFCS/ETIMs in 
collaboration with AFC vendor 
 
Ensure necessary infrastructure development and reliable network connectivity to 
connect with FI ecosystem  
 
Provide sufficient space at each depot and central control center for setting up the 
required infrastructure 
AFC/ITMS Provider 
 
Supply and deployment of Electronic Ticketing System (ETS) to roll-out the NCMC 
solution 
 
Provide ETIMs/validators on bus terminals, city bus, BRTS, etc. 
 
Provide technical maintenance and support of the ETIM application software and 
hardware system over the contract period 
 
Maintain the sufficient spare parts (of Handheld and other hardware parts) at depot 
(or any other location specified by the Authority) for maintenance of ETM and 
meeting the SLA 
 
Certifications & Compliances as per NCMC specification and Interface Specification 
of NCMC Ecosystem (Part IV – VII) 
 
Provision of all the consumable items like SIM, Monthly Charges of connectivity, 
paper roll (for paper tickets) 
 
Backend hardware and hosting infrastructure for hosting the ETM backend

<!-- Page 21 -->

 
 
 
Page 20 of 36 
 
 
Web-Portal for various MIS and settlement report 
NPCI/RuPay 
 
Certification of Issuer and Acquirer Banks in line with NCMC Specification 
 
Certification of cards & terminal vendors as per NCMC specification 
 
Assistance to operators in conceptualization, roll-out and implementation of NCMC 
solution 
 
Settlement of inter-bank transactions 
 
Pricing for inter-bank transactions 
Note: RuPay qSPARC standard and specifications are maintained and certified by NPCI, while AFC 
specifications under NCMC may be governed by BIS/STQCI/CDAC under the guidance of MoHUA. NCMC 
Card and Terminal Specifications are developed and owned by NPCI, hence any stakeholder who wants to 
use the specifications to participate in NCMC program will have to get duly certified by NPCI/RuPay. 
6.5 Adoption of NCMC by Other Card Schemes 
Card and Terminal specifications which are developed by RuPay/ NPCI under NCMC are based on 
RuPay’s qSPARC and thus sharing with other cards schemes requires commercial royalty 
considerations with NPCI/RuPay, subject to various terms and conditions.

<!-- Page 22 -->

 
 
 
Page 21 of 36 
 
7 Standard Operating Procedure for NCMC Implementation 
NCMC implementation processes have been enumerated here for the reference purpose. This may 
be followed by any operator in transit/para-transit and smart cities for implementation purpose. 
S. No. 
Steps 
Description 
Reference 
1. 
Familiarization 
with NCMC 
 
Understand the key aspects of NCMC 
implementation including:- 
o 
Product overview 
o 
Key features of the product  
o 
Pre-requisites 
for 
NCMC 
implementation 
 
Reference document – 
‘Concept Document for 
Implementation of One 
Nation One Card’ 
2. 
Gap Analysis 
 
Operators need to evaluate their existing fare 
collection/ payments system for the gap 
analysis purpose. This will help them:- 
o 
To understand the readiness of the 
existing system for implementation of 
NCMC based fare collection system 
o 
To identify upgrade areas and related 
activities  
 
Analysis of their existing 
AFCS/ITMS, 
backend, 
ETIM devices etc. 
3. 
NCMC 
Implementation 
model 
 
Finalize the NCMC implementation model 
based on business requirements covering 
following key points:- 
o 
Provision of instant issuance, if required 
o 
Multi-banks 
acceptance 
wherein 
customers may use the NCMC card issued 
by any certified Bank 
o 
Single/Multiple Acquirer Bank based on 
the requirement. To start with, Operator 
may go ahead with a single Acquirer Bank 
and may extend it further based on 
transaction volume or requirements  
 
Reference document – 
‘Concept Document for 
Implementation of One 
Nation One Card’ 
4. 
Define Roles & 
Responsibilities 
 
Define the roles and responsibilities of key 
stakeholders 
based 
on 
finalized 
NCMC 
implementation model:- 
o 
System Integrator/AFC System Provider 
o 
Acquirer Bank 
o 
Issuer Bank for instant issuance purpose, 
if any 
 
Reference document – 
‘Concept Document for 
Implementation of One 
Nation One Card’

<!-- Page 23 -->

 
 
 
Page 22 of 36 
 
In case operator has challenges in dealing with 
two separate partner banks as mentioned 
above, the acquirer bank may be given the 
additional responsibility of instant issuance at 
operator service points. However, the system 
should ensure the acceptance of cards issued 
by any bank through their branch networks 
5. 
Finalization 
of 
Business Model 
 
Finalize the business model for NCMC 
implementation (Capex & Opex) covering 
following key points:-   
o 
No vendor lock-in because of business 
model 
o 
Acceptance of NCMC Cards issued by any 
Bank 
There should not be any exclusive business 
arrangement with any partner bank to ensure the 
truly interoperable and vendor agnostic solution.  
 
Reference document – 
‘Concept Document for 
Implementation of One 
Nation One Card’ 
6. 
Engagement and 
Selection 
of 
Vendors for AFC 
System/ 
ITMS/ 
ETIMs 
devices 
etc. 
 
Engagement 
with 
existing 
System 
Integrator/AFC/Terminal vendor for NCMC 
based implementation 
 
Selection of System Integrator/AFC/Terminal 
vendor in case the existing vendor is not willing 
for NCMC implementation 
 
Sample 
RFPs 
for 
‘Selection of Electronic 
Ticketing System (ETS) 
provider’ 
 
The 
list 
of 
terminal 
kernels certified as per 
NCMC specification is 
available at website of 
NPCI. 
Link 
- 
https://www.npci.org.in
/tap-go-circulars 
7. 
Engagement and 
Selection 
of 
Financial 
Institutions 
for 
Instant 
Issuer 
Bank & Acquirer 
Bank  
 
 
Multi-banks acceptance as the key requirement 
wherein customers may use NCMC cards issued 
by any Bank through their branch/business 
correspondent networks 
 
Selection of Acquirer Bank for acquiring of 
digital transactions done using NCMC cards 
 
Selection of Instant Issuer Bank for instant 
issuance of NCMC cards at operator service 
points, if required 
 
To start with, instant Issuance activities may be 
assigned to the Partner Acquirer Bank, as 
decided by Operator/Authority 
 
Sample 
RFPs 
for 
‘Selection 
of 
Partner 
Bank working as Acquirer 
and Instant Issuer’ 
 
The list of Banks certified 
on NCMC platform is 
available at website of 
NPCI. 
Link 
-  
https://www.npci.org.in
/live-members-2

<!-- Page 24 -->

 
 
 
Page 23 of 36 
 
8 Certifications & Compliances 
The table below provides an overview of the certifications required for an Acquirer and Issuer Bank. 
These certifications will be done as per the latest specifications prevalent during the implementation. 
8.1 
Issuer Bank Certification Requirements 
S. No. 
Product/ System 
Role in payment eco-
system 
Certification Type 
Followed Guidelines 
1 
Card 
Issuance 
Physical Card 
EMVCo 
2 
RuPay qSPARC based 
NCMC Application 
RuPay 
3 
White 
Plastic 
Certification 
RuPay 
4 
Issuer Host 
Transaction processing by 
Issuer Bank 
Issuer 
Host 
Certification 
RuPay 
5 
Central 
Clearing 
House Certification 
(CCH) 
Clearing and settlement 
CCH Certification 
RuPay 
 
8.2 
Acquirer Bank Certification Requirements 
S.No 
Product/ System 
Role in payment eco-
system 
Certification Type 
Followed Guidelines 
1 
Acquirer  Host 
Transaction processing by 
acquirer 
Acquirer 
 
Host 
Certification 
AFC/Terminal Interface 
RuPay 
Interface 
Specification 
of 
NCMC 
Ecosystem 
– 
Part VI 
2 
Central 
Clearing 
House Certification 
(CCH) 
Clearing and settlement 
CCH Certification 
RuPay

<!-- Page 25 -->

 
 
 
Page 24 of 36 
 
8.3 
ETIM/Terminal Certification Requirements  
S. No. 
Product/ System 
Role 
in 
payment 
eco-
system 
Certification Type 
Followed Guidelines 
 
1 
 
Terminal 
Acceptance 
Hardware 
Level 
requirement (L1) 
EMVCo 
Terminal 
Kernel- 
(Contact L2) 
EMVCo 
Terminal 
Kernel-
(Contactless L2) 
RuPay 
Terminal 
Application 
(L3) 
RuPay 
 
8.4 
AFC Certification requirements (CDAC)  
S.No  Product/ System  
Role in payment eco-system  
Followed Guidelines  
1  
Terminal  
Transit Service Management  
Interface 
Specification 
of 
NCMC 
Ecosystem – Part IV  
2 
Terminal -- AFC 
Terminal 
- 
AFC 
Backend 
Communication 
Interface 
Specification 
of 
NCMC 
Ecosystem – Part V 
3 
Terminal/AFC - Banking 
Interface  
Terminal / AFC  - Acquirer 
Communication 
Interface 
Specification 
of 
NCMC 
Ecosystem – Part VI 
4 
Terminal - Gate 
Terminal 
– 
Gate 
Communication 
Interface 
Specification 
of 
NCMC 
Ecosystem – Part VII 
S.No  Product/ System  
Role in payment eco-system  
Followed Guidelines  
1  
Terminal  
Transit Service Management  
Interface 
Specification 
of 
NCMC 
Ecosystem – Part IV  
2 
Terminal -- AFC 
Terminal 
- 
AFC 
Backend 
Communication 
Interface 
Specification 
of 
NCMC 
Ecosystem – Part V 
3 
Terminal/AFC - Banking 
Interface  
Terminal / AFC  - Acquirer 
Communication 
Interface 
Specification 
of 
NCMC 
Ecosystem – Part VI 
4 
Terminal - Gate 
Terminal 
– 
Gate 
Communication 
Interface 
Specification 
of 
NCMC 
Ecosystem – Part VII

<!-- Page 26 -->

 
 
 
Page 25 of 36 
 
9 Commercial Pricing 
The commercial pricing structure for RuPay qSPARC based NCMC will remain similar to any bank 
issued payment card. There are two types of transactions namely ON-US transaction and OFF-US 
transaction as described below:- 
 
ON-US Transaction are transactions where Issuer and Acquirer Bank are same. Hence, these 
transactions are not routed via Payment Scheme switch. 
 
OFF-US Transaction are transactions where Issuer and Acquirer Bank are different. These 
transactions are routed via Payment Scheme switch.  
 
In case of OFF-US transaction, the commercial pricing structure will consist of following components:- 
 
Merchant Discount Rate (MDR)/Transaction Fee payable by Merchant to Acquirer Bank is a fee 
charged by the Acquirer Bank to the Merchant for accepting payments from customers through 
credit/debit/prepaid card.  
 
It is to be noted that in case of debit card, RBI has defined the guidelines with upper limit on MDR. 
In case of credit and prepaid card, it is as per the individual negotiation between the Acquirer 
Bank and merchant. Interchange Fee payable by Acquirer Bank to Issuer Bank is the fee paid by 
the Acquirer Bank to card Issuer Bank for each card transaction. This fee will be as per the 
prevalent circular floated by card scheme from time to time.  
Switching Fee payable by Issuer and Acquirer to Payment Scheme is the fee charged by card scheme 
to facilitate the inter-bank transactions. This fee will be as per the prevalent circular floated by card 
scheme from time to time. 
For domestic offline POS transactions (NCMC wallet based transactions), MDR is maximum up to 
0.90% and interchange is maximum up to 0.58%.

<!-- Page 27 -->

 
 
 
Page 26 of 36 
 
10 NCMC Ecosystem Pilot at Delhi Metro Rail Corporation (DMRC)   
In order to showcase the entire NCMC ecosystem for digital fare collection along with indigenized 
Gates, AFC and Validators, the pilot has been done at Delhi Metro across few stations. The pilot at 
DMRC was initiated by MoHUA on Jan 31st, 2019. This has been done in collaboration with CDAC, 
BEL, NPCI and SBI (as an Acquirer Bank). Under this pilot, NCMC based Gates, Validators and AFC has 
been deployed across few stations of DMRC and RuPay Contactless Debit Cards with NCMC has been 
issued to a closed user group for testing. The settlement between Acquirer and Issuer Banks is being 
done by NPCI.   
 
10.1 Roles & Responsibilities of Involved Stakeholders 
The pilot implementation ecosystem consists of following stakeholders:- 
Stakeholders 
Roles and Responsibilities 
DMRC 
 
DMRC is a public transport authority for implementing NCMC solution at identified 
metro stations in Delhi. 
CDAC 
 
CDAC has provided the indigenous AFC system based on NCMC standards. 
BEL 
 
BEL has provided the EMV compliant NCMC based validators and gates to support 
offline purchase transactions at metro station entry/exit gates.    
Acquiring Bank 
 
SBI is the acquiring bank and responsible for presenting all online as well as offline 
transactions to NPCI for settlement. 
Issuing Bank 
 
Issuing Banks are responsible for issuing cards through branches as per regular 
process.  
NPCI 
 
NPCI is responsible for settlement of all the inter-bank transactions received from 
acquirer. 
 
10.2 Key Highlights 
a) Banks certified on RuPay Debit NCMC have issued cards to closed group users from CDAC, BEL, 
DMRC, NPCI and Issuer Banks’ own employees.  
b) Following transactions are being done at DMRC Metro stations under this pilot using NCMC cards 
issued by any certified banks:- 
o Online Money Add transactions to top-up the Stored Value/Offline Wallet 
o Online Service Creation transactions 
o Offline purchase transactions using Stored Value at Metro station   
o Offline balance enquiry to know the balance in Stored Value

<!-- Page 28 -->

 
 
 
Page 27 of 36 
 
10.3 Launch of One Nation One Card 
Marking the beginning of a new era of payment segment, Hon’ble Prime Minister Narendra Modi 
launched ‘One Nation One Card’ as a part of NCMC Eco-system in Ahmedabad on 4th March, 2019.  
This card is based on RuPay NCMC specification and aimed at providing seamless digital payments 
across various use cases including metro, bus, suburban railways, toll, parking, smart city, retail and 
other use cases.

<!-- Page 29 -->

 
 
 
Page 28 of 36 
 
11 RuPay qSPARC based NCMC Proliferation Strategy 
The first NCMC project went live in Jun 2017. Post that, many operators from Transit and Smart Cities 
segments have been on-boarded for NCMC based fare collection system or common card payment 
system. However, the penetration of NCMC card has not picked up significantly due to various 
challenges associated with involved stakeholders. In this regards, a holistic approach is required 
across target segments to enable the faster and higher penetrations of NCMC cards across India. 
With the key proposition of One Card for all Payments; the higher penetration of NCMC cards will 
help to drive the digital adoption in payment space across the country.  
This section talks about the proliferation strategy in Transit, para-transit and retail segments to drive 
the adoption of RuPay qSPARC based NCMCs at a faster pace in an effective manner. This requires 
the cohesive support from all involved stakeholders including Operators/Merchants, Financial 
Institutions, Payment Scheme Network and Government. 
11.1 Transit Segments 
This segment covers various public transport systems including metro, buses and suburban 
railways. As described in Section 6 of this document, NCMC implementation across these public 
transport systems include following key aspects:- 
 
AFC system including backend and Terminals/validators/ETIM devices as per NCMC 
specification – Currently, Operators are managing the fare collection system either in-house 
or through AFC system provided by System Integrator. For operators managing the AFC 
system through System Integrator, the NCMC implementation requires up-gradation as per 
NCMC specification and Interface specification on NCMC Ecosystem (Part IV-VII). Whereas, 
for operators managing the AFC system in-house, the AFC system need to be developed 
accordingly and should support the transactions done using RuPay qSPARC based NCMCs.  
 
NCMC certified partner banks as an Acquirer Bank and Instant Issuer Bank (if required) 
The roles & responsibilities of involved stakeholders for NCMC proliferation across Transit segments 
are as covered in this section. 
11.1.1  Role of Operators 
The approach of operators will be driven by the project type – Greenfield or Brownfield projects, 
as described below. 
 
Greenfield Projects – These are new projects built from scratch and it does not have the 
constraints in terms of legacy infrastructure. These projects require fresh procurement of 
devices, software and fresh installation of set up. The upcoming BRTS/Urban mobility Projects 
are covered under such projects. For all such projects, the operator should directly go ahead 
with the implementation of digital fare collection in line with NCMC specification and 
Interface specification of NCMC Ecosystem (Part IV-VII). This would enable the NCMC

<!-- Page 30 -->

 
 
 
Page 29 of 36 
 
acceptance from day 1 and also avoid any financial implication to the operator on account of 
existing system up-gradation to NCMC based system at a later stage.    
o For Greenfield projects, the operator should procure the devices including 
terminal/validator/ETIM devices as per NCMC specification and Interface 
specification of NCMC Ecosystem (Part IV-VII). .  
o For acquiring and card issuing purpose, the operator should follow the multi-banks 
acceptance scenario (as described in Section 6) wherein the customers should be able 
to use RuPay qSPARC based NCMCs issued by any bank. 
 
Brownfield Projects – Such projects are operational & carry the legacy of closed loop 
ecosystem. The NCMC implementation in such projects require the replacement/up-
gradation of existing terminal/validator/ETIMs as per NCMC specification. This may involve 
certain investment on account of infrastructure up-gradation. Government support for such 
projects will help to expedite the NCMC proliferation in this segment. 
o For all such projects, the future extensions should be done in line with NCMC 
specification.  
o Operators should discuss with existing vendors for up-gradation of existing devices to 
enable NCMC acceptance. PTO may also consider the replacement of existing devices 
with NCMC compliant devices in phase wise manner with buyback of existing devices. 
o For acquiring and card issuing purpose, the operator should follow the multi-banks 
acceptance scenario (as described in Section 5) wherein the customers should be able 
to use RuPay qSPARC based NCMCs issued by any bank. 
 
Concept of Centralized/Zonal AFC – At present, the operators have deployed the AFC 
infrastructure at the individual level. The AFC infrastructure deployment may not be possible 
for small scale operator on account of the cost involved. The provision for Centralized/Zonal 
AFC will help to enable the acceptance of RuPay qSPARC based NCMCs across all public 
transport operators (small as well as large scale). 
The model architecture for Centralized/Zonal AFC in case of SRTUs has been shown below.

<!-- Page 31 -->

 
 
 
Page 30 of 36 
 
 
In case of Centralized AFC System, there will be a single AFC System across all SRTUs. This will 
act as a plug n play system for all SRTUs. In case of Zonal AFC System, the AFC System will be 
at the regional or zonal level. This will act as a plug n play system for all SRTUs under that 
region. This Zonal AFC System may be managed by a representative SRTU of the respective 
region. 
Centralized/Zonal AFC model offers the savings on account of AFC system deployment cost 
by individual operators. This will also offer the matured system with best practices across 
various operators. This will further help in faster implementation of digital fare collection. 
11.1.2 Role of Banks 
All Banks need to support the vision of NCMC implementation from issuance and acquiring related 
aspects based on multi-banks acceptance scenario as detailed out in Section 5 of this document.    
 
Banks certified on NCMC platform should issue NCMC Debit/Credit cards as default 
debit/credit cards to the customers. To start with, Bank should go ahead with RuPay 
debit/credit card issuance in cities where NCMC based transit projects are operational or 
under implementation. This needs to be further extended across all potential cities of India. 
This will help to eliminate the extra effort by PTO or partner bank on account of transit project 
specific card issuance. 
 
The transaction charges payable by PTO to the Acquirer Banks should be nominal and in line 
with Industry practice. Customer should not be burdened with extra cost for issuance of cards. 
11.1.3 Role of Card Scheme 
The role of card Scheme will involve following key activities:- 
 
Certification of payment related components like Card, terminal and banking infrastructure 
 
Settlement of inter-bank transactions done using RuPay qSPARC based NCMCs.

<!-- Page 32 -->

 
 
 
Page 31 of 36 
 
 
Provide hand-holding support to all operators for NCMC implementation. 
 
Interaction with involved stakeholders in the transit ecosystem and onboard them for NCMC 
specification. 
11.1.4 Role of Government 
The government has a key role in enabling the NCMC proliferation across the country by providing 
implementation mandates and financial support to all transit project operators.   
 
Mandates to Transit Operators – As Government already communicated to all transit 
operators for NCMC adoption, implementation should be the focus. The approach can be: 
below:- 
o For Greenfield projects, the operator should deploy all the required infrastructure as 
per NCMC specification and Interface specification of NCMC Ecosystem (Part IV-VII)  
and ensure the digital fare collection based on NCMC based open loop cards. The 
model should be based on multi-banks acceptance scenario wherein the customer 
may use RuPay qSPARC based NCMCs issued by any Bank. 
o For Brownfield projects, the operator should ensure the future extensions in line with 
NCMC specification. Also the up-gradation of existing system should be planned in a 
time-bound phase-wise manner.   
 
Financial Support to Transit Operators – In view of the financial conditions of operators 
across the country, the government should consider provision of the financial support to 
concerned operators to ensure the NCMC proliferation across the country. The financial 
support may be provided on following items:- 
 
Particulars 
Greenfield Projects 
Brownfield Projects 
AFC Deployment 
- 
 
Required 
for 
operators 
managing the fare collection 
in-house and not having AFC 
system 
 
Centralized/Zonal 
AFC 
system may be a potential 
solution for operators across 
the country 
Terminal/Validator/ Device 
Up-gradation 
- 
 
Cost 
involved 
in 
up-
gradation/replacement 
of 
existing devices with NCMC 
compliant devices 
Subsidy 
on 
MDR/ 
Transaction 
Charges 
 
Subsidy 
on 
transaction 
charges 
payable 
by 
Operator to Acquirer Bank 
 
Subsidy 
on 
transaction 
charges payable by Operator 
to 
Acquirer 
Bank 
for

<!-- Page 33 -->

 
 
 
Page 32 of 36 
 
payable by Operator to 
Acquirer Bank 
for transactions done using 
RuPay 
qSPARC 
based 
NCMCs for a defined period 
transactions 
done 
using 
RuPay qSPARC based NCMCs 
for a defined period 
 
 
RBI KYC norms for Transit Segments – Basis the customer profile using the transit segments, 
there are significant number of customer who do not fulfill the criteria of Full KYC/Minimum 
KYC norms as per RBI regulation. Hence, the NCMC adoption is not getting proliferated across 
these customer segments. In view of the same, there is a need to relax the KYC norms for such 
customer segments. This segment may have a reduced upper limit on total transaction value 
as compared to that of minimal/full KYC customers. These customers may further get 
upgraded to minimum/full KYC based on applicable RBI KYC norms. 
11.2 Retail Segments 
With the proposition of ‘National Common Mobility Card’, RuPay NCMC has a huge potential for 
retail segment. As per RBI existing KYC norms, these cards may be used in contactless mode without 
2nd factor authorization for transaction value up to INR 2000. The contactless offline feature further 
enable the customers to make the payment in offline environment within less than a second. This 
has the unique proposition for modern retail stores getting huge footfalls as well as small retail 
stores looking for minimal transaction time without dependency on network connectivity.  
The penetration of RuPay NCMCs in this segment will help to drive the NCMC proliferation in the 
entire ecosystem. Further, the card penetration in this segment will help in adoption of RuPay 
qSPARC based NCMCs in transit segments as well without any transit project specific issuance. 
This requires the support from all involved stakeholders as mentioned below:- 
11.2.1 Role of Merchant 
 
Merchants should enable the acceptance of RuPay NCMCs at their stores through their 
partner acquirer banks.  
 
The Service Area feature of RuPay NCMCs may be leveraged by merchants to drive the special 
loyalty programs, membership programs for customers. This would enable usage of RuPay 
NCMCs in retail at large scale. 
11.2.2 Role of Banks 
 
Banks should get their Issuing host and Acquiring host system certified as per NCMC 
specifications.  
 
Banks should issue Rupay Debit/Credit cards as default Contactless Debit/Credit cards. This 
would enable the customers to use their existing Rupay Debit/Credit cards for all low value 
payments in retail stores as well as other use cases. This will eliminate the need of specific 
issuance of NCMC cards for any identified use case.

<!-- Page 34 -->

 
 
 
Page 33 of 36 
 
 
Banks should promote the acceptance of RuPay NCMCs across their partner modern retail 
outlets. They should also promote the acceptance of RuPay NCMCs across their 
large/medium/small merchants. 
11.2.3 Role of Card Scheme 
 
Certification of payment related components like Card, terminal and banking infrastructure 
 
Settlement of inter-bank transactions done using RuPay NCMCs. 
 
Handholding support to involved stakeholders including Banks and merchants for creating the 
ecosystem for NCMC. 
11.2.4 Role of Government 
 
Financial support in the form of promotional offers to customers as well as merchants in 
order to drive the usage and activation of RuPay qSPARC based NCMCs. 
 
Further, RuPay NCMC may be leveraged for issuance of Smart Cards/Payments Cards against 
various government provided services e.g. Jan Dhan Yojna, Driving License, PDS/Ration Card 
etc. 
 
The Service Area feature of NCMC may also be leveraged to provide targeted Government 
Incentives e.g. medicines, books, travel passes etc. 
11.3 Smart City Segments, Toll and Parking 
As of now, there are more than 100 cities which have been selected for smart cities projects. Digital 
payment ecosystem is a key part of these smart cities projects. In this regard, smart cities are 
implementing common card payment system which would provide citizens single card for making 
all sort of payments across all use cases in the city including civic as well as non-civic payments. 
MoHUA has already issued an advisory to Smart Cities for adopting NCMC based common card 
payment system. However, it needs to be pushed further for the implementation purpose to drive 
the proliferation in this segment.  
Toll and Parking segments which are highly driven by cash and have huge potential for digital 
payments. These are mostly unorganized and at a very nascent stage from the aspects of digital 
payments. NCMC proliferation in these segments will be driven gradually by its acceptance across 
all other segments as highlighted above. This will further get the synergy from involvement of 
Municipal Corporation/Smart City bodies for NCMC based implementation for Smart Parking 
projects.   
 
11.3.1 Role of Smart City and Toll Operators 
 
Smart City and Toll operators should implement NCMC based common card payment 
system for multiple use cases (civic, retail, transit, para-transit etc.) in the cities. This will help 
to provide an interoperable and vendor agnostic digital payment solutions leading to higher 
digital adoption.

<!-- Page 35 -->

 
 
 
Page 34 of 36 
 
 
The operator should procure the devices including terminal/validator/ETIM devices as per 
NCMC specification and Interface specification of NCMC Ecosystem (Part IV-VII).  
 
For acquiring and card issuing purpose, the operator should follow the multi-banks 
acceptance scenario (as described in Section 5) wherein the customers should be able to use 
RuPay qSPARC based NCMCs issued by any bank. 
11.3.2 Role of Banks 
All Banks need to support the vision of NCMC implementation from issuance and acquiring related 
aspects based on multi-banks acceptance scenario as detailed out in Section 5 of this document. 
 
Banks certified on NCMC platform should issue Rupay Debit/Credit cards as default 
debit/credit cards to the customers. To start with, Bank should go ahead with Rupay 
debit/credit card issuance in smart cities which are operational or under implementation. This 
needs to be further extended across all potential cities of India. This will help to eliminate the 
extra effort by Smart City or partner bank on account of project specific card issuance. 
 
The transaction charges payable by Authority to Acquirer Banks should be nominal and in line 
with Industry practice. Customer should not be burdened with extra cost for issuance of cards. 
11.3.3 Role of Card Scheme 
 
Certification of payment related components like Card, terminal and banking infrastructure 
 
Settlement of inter-bank transactions done using RuPay qSPARC based NCMCs. 
 
Handholding support to involved stakeholders including Banks, Smart City operators and 
ecosystem vendors for NCMC proliferation. 
 
Banks should leverage their existing NETC association with the Toll Operators and handhold 
them to enable the acceptance of RuPay qSPARC based NCMCs at the toll plaza. 
11.3.4 Role of Government 
 
In order to promote the NCMC across Smart City segments at a faster pace, Government 
should issue mandates to all Smart Cities operators for implementation of Common Card 
Payment System based on NCMC specification and Interface specification of NCMC 
Ecosystem (Part IV-VII).   
 
At state level, a common payment standard based on NCMC should be adopted by all smart 
cities of that state. This would reduce the repetitive effort and implementation timeline to a 
great extent. In this regard, state urban development authority may play a vital role as most 
of the smart cities at state level are funded by these authorities.

<!-- Page 36 -->

 
 
 
Page 35 of 36 
 
12 Further Information and Clarification 
Please contact Mr. Nalin Bansal, Head-RuPay, NCMC & NFS, NPCI (Contact number – 9810603372, 
email – rupay@npci.org.in, nalin.bansal@npci.org.in) for further clarifications and NCMC 
implementation. 
 
You may also visit https://www.npci.org.in for more information.

<!-- Page 37 -->

 
 
 
Page 36 of 36 
 
 
13 Annexures 
 
Please find below all the annexures:

<!-- Page 38 -->

0LQLVWU\RI8UEDQ'HYHORSPHQW6PDUW&LWLHV0LVVLRQ
$GYLVRU\1R






WK -XQH
6XE 6WDQGDUGVDQG6SHFLILFDWLRQVRI1DWLRQDO&RPPRQ0RELOLW\&DUG
7KH1DWLRQDO8UEDQ7UDQVSRUW3ROLF\XQGHUWKH0LQLVWU\RI8UEDQ'HYHORSPHQWHQYLVDJHV
DVLQJOHIDUHPHGLDRYHUDOOV\VWHPVRISXEOLFWUDQVSRUWIRU,QWHURSHUDEOH)DUH0DQDJHPHQW
6\VWHP ,)06 7KLV VLQJOH IDUH PHGLD ZLOO EULQJ D VHDPOHVV WUDYHO FRQQHFWLYLW\ DFURVV
GLIIHUHQWPRGHVRIWUDQVSRUWDQGGLIIHUHQWRSHUDWLRQVDFURVVGLIIHUHQWFLWLHVLQ,QGLD7KHPDLQ
IHDWXUHVRIWKHSURSRVHGV\VWHPDUH
x
,QWHURSHUDEOH&RPPRQ0RELOLW\&DUGDFURVVPRGHVRIWUDQVSRUWDQGFLWLHV
x
&RQYHQLHQFHDQGVHDPOHVVH[SHULHQFHIRUFRPPXWHU
x
(FRQRPLFVRIVFDOHWREULQJGRZQFRVWVFRPSDUHGWRVRORHIIRUWVRI3XEOLF7UDQVSRUW
2UJDQL]DWLRQV

7KH,)06VXSSRUWVIRUIDUHSD\PHQWRQ%XVHV0HWUR0RQRUDLODQG)HUU\HWFIRU
YDULRXVSXEOLFWUDQVSRUWRUJDQL]DWLRQVDFURVVWKHFRXQWU\7KH,)06VKDOOEHGHVLJQHGWREH
DFFHSWHGLQ
x
$OONLQGVRI3XEOLF7UDQVSRUWOLNHUDLOZD\VOLJKWUDLOWD[LDXWRHWF
x
3DUDWUDQVLWDQGQRQWUDQVLWVHUYLFHV 3DUNLQJ7ROO7D[LV$XWRULFNVKDZVHWF
x
2WKHUPHUFKDQWSD\PHQWOLNHXWLOLW\ELOOVWD[HVHWF

7RIDFLOLWDWHUROORXWRI,)060LQLVWU\RI8UEDQ'HYHORSPHQWFRQVWLWXWHGDFRPPLWWHH
WRGHYHORSVWDQGDUGVDQGVSHFLILFDWLRQVIRU1DWLRQDO&RPPRQ0RELOLW\&DUG1&0&7KH
UHSRUWRIWKHFRPPLWWHHUHFRPPHQGLQJVWDQGDUGVDQGVSHFLILFDWLRQVRIWKH1&0&LVDYDLODEOH
RQWKHOLQNJLYHQEHORZ
KWWSPRXGJRYLQXSORDGXSORDGILOHVILOHV&RPPLWWHH5HSRUWRI1&0&SGI

$OO WKH 6PDUW &LWLHV DUH DGYLVHG WR IROORZ WKH VWDQGDUGV DQG VSHFLILFDWLRQV
UHFRPPHQGHGE\WKHFRPPLWWHHLQWKHDERYHUHSRUWIRULPSOHPHQWDWLRQRISURSRVDOVIRUUROO
RXWRI6PDUW0RELOLW\&DUGVLQWKHUHVSHFWLYHFLWLHV
$QQH[XUH$

<!-- Page 39 -->



<!-- Page 40 -->



<!-- Page 41 -->



<!-- Page 42 -->



<!-- Page 43 -->
