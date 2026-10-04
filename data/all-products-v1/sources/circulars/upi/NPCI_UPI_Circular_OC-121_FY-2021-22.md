# UPI Circular 121-Changes in UPI RAW data file

Circular/reference number: NPCI/UPI/2021-22/OC.121
Date: 25th October, 2021

<!-- Page 1 -->

NPCL
 p  pat
NATIONAL PAYMENTSCORPORATIONOFINDIA
NPCI/UPI/2021-22/OC.121 25th October, 2021
To,
All Member Banks, Unified Payments Interface (UPl)
Madam / DearSir
Subject: Changes in UPI raw data file.
In our constant endeavor to improve the overall settlement performance of NPCI various products,
NPCI has proposed changes in existing UPI settlement process in order to achieve the below
objectives,
1. Increase in existing UPl settlement cycles from 6 to 8.
2. Efficient settlement time window.
Considering exponential growth in UPI transactions volume, NPCI has explored various options
to further enhance the raw data generation process and was discussed the same in working group
meeting that was conducted on 18th August 2021 with UPl member banks.
Based on bank's discussion in working group meeting and feedback on raw data changes, NPCl
has decided to make following changes in UPl raw data.
1. Raw data file format as given in Annexure A for Domestic UPI transactions.
2. Raw data file format as given in Annexure B for International UPI transactions.
3. E BBPS transactions would be excluded from merchant Raw data file. Separate BBPS RAW
data files are already available to Banks.
4. Raw Data files will be in csv format.
5. If the sub-member entity is TPAPs subject to access to be provided by Bank and only PSP
files would be available to TPAPs.
6. Raw data file of PsP will have account number field as blank.
7. PSPs files would include transactions wherein entity is PSP only and is neither remiter
bank nor beneficiary bank. Transactions where PsP is same as remitter or beneficiary
bank are already available in ISS & ACQ RAW data files and hence will be excluded from
PSP files.
8. Discontinuing Timeout & DRC Reports as these records are already available in RAW
data files.
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 400 051.
T: +9122 40009100 F: +9122 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

The above changes are scheduled to go live with effect from 1st March, 2022 for banks that
these changes by 30th June, 2022.
Please make note of the above and disseminate the instructions contained herein to the officials
concerned.
For any queries or clarification, please contact:
Name Email Id
Sapna Gupta sapna.gupta@npci.org.in
Sarit Das sarit.das@npci.org.in
Pankaj Samarth pankaj.samarth@npci.org.in
Ramaraj R rama.raju@npci.org.in
Yours faithfully.
SaiprasadNabar
Chief-Online Product Operations
ENCL:

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure A - Raw data fields for Banks - Domestic UPI
Sr. No Fields
Transaction Type
RRN
UPI Transaction ID
Response Code
Transaction Date
Transaction Time
Settlement Date
Settlement Amount
BENIIFSCCODE
10 BENIACCOUNTNUMBER
11 REMIFSCCODE
12 REMACCOUNTNUMBER
13 IssCode
14 Acq Code
15 Payer Code
16 PayeeCode
17 PayerVPA
18 Payee VPA
19 UMN
20 Initiation Mode
21 Purpose Code
From Account Type
23 To Account Type
24 MCC
25 Mapper ID

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure B - Raw data fields for Banks - International UPl
Sr. No Fields
Transaction Type
RRN
UPI Transaction ID
Response Code
Transaction Date
Transaction Time
Settlement Date
Settlement Amount
BENIIFSCCODE
10 BENIACCOUNTNUMBER
11 REMIFSCCODE
12 REMACCOUNTNUMBER
Iss Code
Acq Code
15 Payer Code
16 Payee Code
17 PayerVPA
18 Payee VPA
19 UMN
Initiation Mode
21 Purpose Code
22 FromAccount Type
23 To Account Type
24 MCC
Currency Code
26 Institutions Code
27 MapperID
28 Country code*
29 Transaction Amount in International Currency*
30 Markup rebate*
*Note: The following field changes has been made in International raw data file format that have
shared in our previous communication.
Removedfromrawdatafile New fields added in raw data file.
Markup Amount Country code
MarkupAmountinINR Transaction Amount in International Currency
Markup rebate
