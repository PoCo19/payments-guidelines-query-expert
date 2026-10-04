# Circular No 046 Validation of user code in transactions for NACH

Circular/reference number: NPCI/2017-18/NACH/Circularno.046

<!-- Page 1 -->

NPCD
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2017-18/NACH/Circularno.046 January 16, 2019
To
AllNACHMemberbanks
Validation of user codes in transactions for NACH
NPCI has been issuing separate user codes for processing DBT and non-DBT related
transactions.The banks were advised to use only relevant codes allotted for various
purposes.
We are bringing thefollowing validations
Account based transactions: User code and Product type
Aadhaarbasedtransactions:UsercodeandTransactions
If user code issued for DBT purpose is used with Non-DBT product or vice aversa the system
will reject such files / transactions.
The list of possible scenarios and their expected results,of usage of DBT & Non-DBTuser
code, are provided in Annexure1.This will be effect fromFebruary 01,2019.Member
banks are advised to disseminate the information to all theconcerned and ensure
compliance.
For clarifications, please raise queries through CRM tracker.
Withwamregards,
GiridharGM
(SVP -NACH & CTS Operations)
1001A,TheCapital,BWing.10thFloor,BandraKurlaComplex,Bandra (E),Mumbai400051.T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-l:
UserNumber New
Product User Existing
Scenario Product validation Proces Remark
type code Process
Header Record
Account DBT / DBT
7 or 18 digit 7 digit Pass Pass Success
Based PFM scheme
18 digit user
Account DBT / DBT code are not
7 or 18 digit 18 digit Pass Fail
Based PFM scheme allowed for
DBTproducts
Corporate is of
Account DBT / 7 or 18 type NON DBT
NON DBT 7 or 18 digit Pass Fail
Based PFM digit and product is
of DBT
10/ECS/
Account 7 or 18
SAL/PEN/ NON DBT 7 or 18 digit Pass Pass Success
Based
RPN/LPG
Corporate is of
10/ECS/
Account DBT 7 or 18 type DBT and
SAL/PEN/ 7 or 18 digit Pass Fail
Based scheme digit product is of
RPN/LPG
NON DBT
Aadhaar DBT
77 or 79 7 digit 7 digit Pass Pass Success
Based scheme
Corporate is of
Aadhaar type NON DBT
77 or 79 NON DBT 7 digit 7 digit Pass Fail
Based and product is
of DBT
Aadhaar
10 78 or 80 NON DBT 7 digit 7 digit Pass Pass Success
Based
Corporate is of
Aadhaar DBT type DBT and
11 78 or 80 7 digit 7 digit Pass Fail
Based Scheme product is of
NON DBT
1001A,TheCapital,BWing.10thFloor,BandraKurlaComplex,Bandra (E),Mumbai400051.T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067
