# UPI | OC No. 209 | FY 24-25 – Guidelines on UPI features for UPI 123Pay

Circular/reference number: NPCI/UPI/OC-209/2024
Date: 1st January 2025

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/UPI/OC-209/2024 October 25, 2024
To,
All UPI Members - Banks, PSPs and 123Pay Service Providers,
DearMadam/Sir
Subiect: Guidelines on UPI features for UPI 123Pay
UPl 123Pay enables smart phone and feature phone users to digitally undertake a host of
transactions based on four approaches, including voice payment based via IVR number, proximity
feature phone. NPCI developed Server-Side Common Library (SSCL) which is hosted at NPCl
end for enabling 123Pay transactions.
A reference is invited to press release issued by Reserve Bank of India (RBl), dated gth October
2024 with Subject Statement on Development and regulatory Policies' whereby RBl has decided
to increase per transaction limit from R5,000 to 10,000 for UPl 123Pay.
1. Members shall increase the per transaction limit to 10,000 from 5,000 with immediate effect.
2. Members shall implement Onboarding with Aadhar OTP in UPI 123Pay. Details as defined in
circular NPCI/UPl/OC-116/2021-22 and NPCl/UPI/OC-116A/2021-22 to be followed.
3. Members shall collectively identify and tag UPl 123Pay transactions as mentioned in
Annexure 1.
4. Members shall implement UPI Number functionality through integration with UPI numeric ID
Mapper. Details as defined in circular NPCl/UPl/OC-115/2021-22 to be followed.
services.
Compliance Action:
All live 123Pay members are advised to comply before 1st January 2025
Yours sincerely
SD/-
Kunal Kalawatia
Chief of Products
1001A,The Capital,B Wing,10th Floor,
BandraKurlaComplex,Bandra(E),Mumbai4o0O51.
T:+912240009100F:+912240009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure 1:
IdentifiersforUPl123Paytransactions.
a. Purpose Code
New purpose code 86 is issued for UPl 123Pay transactions. All 123Pay transactions should be
passed with purpose code 86 in the purpose="_" tag for financial and non-financial
transactions.
b.Initiation Mode
Initiation modes to be passed as per UPl Procedural guidelines. Earlier allotted Initiation mode =
‘31' for 123Pay transactions as mentioned in NPCI/UPl/OC-133A/2022-23 shall be considered
null and void.
C. Initiating channel
The following initiating channel to be passed for respective 123Pay transactions
Initiating
Sr.No. Particular Tag value
channel
OnCallbased IVR <Tagname="TYPE"value="IVR"/>
Feature phone
FP <Tag name="TYPE"value="FP"/>
application based
MissedCallBased MCP <Tagname="TYPE"value="MCP"/>
Soundfrequency based TONE <Tag name="TYPE"value="TONE"/>
1001A,The Capital, BWing,10thFloor,
BandraKurlaComplex,Bandra(E),Mumbai4oo051.
T:+912240009100F:+912240009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067
