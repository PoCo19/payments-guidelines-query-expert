# AePS | OC 80A| FY 23 24 | Annexure A Operational details of Dual Auth transactions in AePS (Updated on 17th July’23)

Circular/reference number: OC-80A

<!-- Page 1 -->

 
 
 
Page 1 of 7 
 
Annexure A 
Operational details of Dual Auth transaction in AePS 
 
A. The Dual Authentication flow broadly includes: 
I. 
Signatory name fetch from Issuer/Remitter bank based on SHG account number 
II. 
Selection of (signatory) name at Acquirer bank’s BC terminal and biometric 
authentication for the selected signatory. This shall be done twice for dual 
authentication.  
III. 
Financial transaction i.e. cash withdrawal, cash deposit and fund transfer on the 
successful Aadhaar authentication of required signatories. For Cash deposit service, 
single signatory authentication will be required to perform transaction in SHG account. 
IV. 
ONUS Dual Auth (SHG) - Bank’s BC agents can serve SHG account holders using 
Aadhaar based biometric authentication at their own BC Agent outlet by performing 
Aadhaar based authentication of the signatories (dual) as ONUS transactions i.e. the 
BC has to be of the same bank in which SHG has the account. Accordingly, banks 
need to do the necessary development for Onus Dual auth (SHG) signatory fetch.  
V. 
Extant AePS dispute management process, including fraud liability shift process shall 
be applicable for Dual Auth transactions. 
 
B. Details of Dual Auth transaction in Raw data files and NSTL Reports 
 
Details of Dual Auth transactions in raw file & NSTL report 
Type of transaction 
Online 
transaction 
Purpose Code 
Raw 
File 
Identifier 
NTSL Report Identifier 
 
1. Dual Auth OFFUS Cash Withdrawal (CW) 
Dual Auth CW Signatory 
Fetch (ReqSigFetch) 
27 
35 
- 
Dual Auth CW 1st signatory 
Auth (ReqBioAuth) 
27 
36 
ACQUIRER/ISSUER 
DUALAUTH 
SHG 
WDL 
AUTH 
Dual 
Auth 
CW 
2nd 
signatory 
Auth 
+ 
Txn 
posting (ReqPay) 
27 
15 
ACQUIRER/ISSUER 
DUALAUTH SHG WDL  
2. Dual Auth (SHG) OFFUS Cash Deposit (CD) 
Dual Auth CD Signatory 
Fetch (ReqSigFetch) 
28 
35 
-

<!-- Page 2 -->

 
 
 
Page 2 of 7 
 
Dual Auth CD signatory 
Auth + BAV (ReqPay) 
28 
37 
ACQUIRER/ISSUER 
DUALAUTH SHG DEP BAV 
Dual Auth CD Confirmation 
(CDA) (ReqChkTxn) 
28 
23 
ACQUIRER/ISSUER 
DUALAUTH SHG DEP 
3. Dual Auth (SHG) OFFUS Fund transfer (FT) 
Dual Auth FT 1st signatory 
Auth (ReqBioAuth) 
29 
39 
ACQUIRER/ISSUER 
DUALAUTH SHG FT AUTH 
Dual Auth FT 2nd signatory 
Auth (ReqBioAuth) 
29 
- 
- 
Dual Auth FT - Txn posting 
(ReqPay) 
29 
40 
ACQUIRER/ISSUER 
DUALAUTH SHG FT 
 
I. 
SHG ID shall be 12 digit numeric identifier. 
II. 
SHG ID will be populated under “ATTXNID” attribute i.e. character 310 to 324 in 
Acquirer raw data file  
III. 
SHG ID will be populated under “ITTXNID” attribute i.e. character 443 to 457 in Issuer 
raw data file 
IV. 
For Fund Transfer, “UD” & “AC” will be the identifiers to be used for UID based FT 
(Bene) and Account + Bank based FT (Bene) respectively. 
a. Identifiers i.e. UD or AC will reflect in “ATRFU1” attribute i.e. character from 325 
to 342 in Acquirer raw data file. 
b. Identifiers i.e. UD or AC will reflect in “ITRFU1” attribute i.e. character from 458 
to 475 in Issuer raw data file 
 
C. Details of File naming convection for Dual Auth transaction 
 
Type 
of 
transaction 
Raw Data Files (New) 
Acquirer file  
Issuer file 
Dual Auth Cash 
withdrawal 
ACQDUALAUTHSHG<Bank Code> 
<yymmdd>.mbankcode 
ISSDUALAUTHSHG<Bank 
Code> <yymmdd>.mbankcode 
Dual Auth Cash 
Deposit 
ACQDUALAUTHSHG<Bank Code> 
<yymmdd>.mbankcode 
ISSDUALAUTHSHG<Bank 
Code> <yymmdd>.mbankcode 
Dual Auth (SHG) 
Fund Transfer 
ACQDUALAUTHSHG<Bank Code> 
<yymmdd>.mbankcode 
ISSDUALAUTHSHG<Bank 
Code> <yymmdd>.mbankcode 
 
I. 
Separate raw data files (new) shall be made available for Dual Auth transactions.  
II. 
For all other reports such as NTSL, Adjustment report, DVR and GST, Dual Auth 
transaction details shall be made available in the existing reports itself.  
III. 
Existing NPCI Authentication switching fee shall be applicable for first signatory 
authentication

<!-- Page 3 -->

 
 
 
Page 3 of 7 
 
IV. 
Existing NPCI AePS OFFUS switching fee shall be applicable for second signatory 
authentication + transaction processing. 
V. 
Existing AePS OFFUS Interchange fee shall be for Dual Auth transactions i.e. Cash 
withdrawal, Cash Deposit and Fund Transfer. 
 
 
D. PAN Attribute Details in Raw Data File 
 
i. 
Dual Auth Cash Withdrawal: 
 
 
Last 4 digits of “RefKey” from payer tag of OLN transaction will be fetched i.e. CIF 
of 1st signatory (36 – raw data file identifier) – Non Financial leg (ReqBioAuth) 
 
Last 4 digits of “RefKey” from payer tag OLN transaction will be fetched i.e. CIF of 
2nd signatory (15 – raw data file identifier) – Financial leg (ReqPay) 
 
ii. 
Dual Auth Cash Deposit: 
 
 
Last 4 digits of “RefKey” from payer tag of OLN transaction will be fetched i.e. CIF 
of 1st signatory (37 – raw data file identifier) – (ReqPay) 
 
Last 4 digits of “RefKey” from payer tag of OLN transaction will be fetched i.e. CIF 
of same signatory (23 – raw data file identifier) – (ReChqTxn) 
 
iii. 
Dual Auth Fund Transfer:  
 
 
Last 4 digits of “SHG ID” will be fetched from OLN transaction (39 – raw data file 
identifier) –Non- Financial leg (ReqBioAuth) 
 
Last 4 digits of “ACNUM” from payer tag of OLN transaction will be fetched i.e. 
SHG account number (40 – raw data file identifier) –Financial leg (ReqPay)

<!-- Page 4 -->

 
 
 
Page 4 of 7 
 
E. Bank portal view of Dual Auth Transaction subtypes 
 
1) Dual Auth Cash withdrawal  
 
a) First signatory authentication 
 
Non-financial tab – with Transaction subtype - 36- Dual Auth Withdrawal-Auth 
 
 
Transaction summary page:

<!-- Page 5 -->

 
 
 
Page 5 of 7 
 
b) Dual Auth Withdrawal (Transaction Posting)-15 
 
 
 
2) Dual Auth - Cash Deposit  
 
a) Verification -37 Dual Auth Cash Deposit-BAV

<!-- Page 6 -->

 
 
 
Page 6 of 7 
 
b) Dual Auth Cash Deposit Advice - 23-DualAuth Deposit-CDA 
 
 
3) Dual Auth – Fund Transfer  
 
a) Transaction subtype -40-Dual Auth (SHG) Fund Transfer

<!-- Page 7 -->

 
 
 
Page 7 of 7 
 
b) Transaction subtype - 39-DualAuth Fund Transfer AUTH 
 
 
 
----End of document----
