# UPI OC 157 - UPI Raw data Version 3.0

Circular/reference number: OC-157
Date: 31st October, 2022

<!-- Page 1 -->

NPC
NATIONALPAYMENTSCORPORATIONOFINDIA
NPC/UPI/2022-23/OC.157 31st October, 2022
To,
All Member Banks of Unified Payments Interface (UPl)
Madam / Dear Sir,
Subject: UPI Raw File Version 3.0.
We refer to the below mentioned operating Circulars wherein we have informed member banks
to migrate raw file version to V.2.0 in OC-121.
i) OC NPCl/UPl/OC No.121/2020-21 dated 25th October, 2021 (Sub. Changes in UPI
raw data file)
changes in UPl raw data files - 121)
ii) OC NPCl/UP/0C No.138/2021-22 dated 16th March, 2022 (Sub. Introduction of 'On
Device Wallet' - UPi Lite for small value transactions)
Subsequently, banks who have gone live on UPI Lite has approached NPCl to accommodate the
LRN (Lite Reference Number) in remitter and payer PsP raw files same as UPI Lite Balance file.
In view fhereof, it was proposed during the UPl working group meeting dated 6th October, 2022 to
introduce 4 additional fields at the end of each transaction record in new trimmed raw data files
(refer OC-121). Post deliberation in meeting, it was decided to use one of field for Lite reference
number (LRN) for UPI Lite transactions in remitter and payer PSP raw file and remaining 3 fields
shail be reserved for future purpose (refer Annexure - A for details), accordingly NPCl has made
live in production system on 8th September 2022.
Member Banks may please note importantly that
Additional 4 fields are incorporated in new trimmed raw data as a part of Version 3.0.
Specification of Version 3.0 (refer Annexure - A for details, highlighted in bold and italic for
quick reference).
LRN will be sent in Remitter and Payer PSP raw data files only.
Beneficiary and Payee PsP raw files will have blank values in respective 4 fields.
Banks who have gone live on version 2.0 are expected to migrate to raw file Version 3.0
before enabling UPl Lite functionality
Bank who are currently on Version 1.0 are expected to migrate to the new raw file version
3.0 directly for faster generation of raw files and enablement of UPl lite Functionality.
Please make a note of the above and disseminate the information contained herein to the officials
concerned.
Yours sincerely,
S.m.Na
Saiprasad Nabar
Chief Platform Officer
ENCL: Annexure - A
1001A, The Capital, B Wing. 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 400 O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

Annexure -- A
Domestic RAW Data format
Prefix NewFieldNarme Field Description Type ActualLength MaxLength Remark
(For Future Use)
TIsub Type Transaction Type AN 20
Titxnld UPITransaction ID AN 35 100
Tirm RRN AN 12 100
TlrespCode Response Code AN 20
TIDate Transaction Date
TI Titime Transaction Time
TlsetAmount Settlement Amount 15,2 15,2
Tlumn UMN 255 255
TIMapperld Mapper Id AN 16 16
TCinitiationMode Initiation Mode AN 10
Purpose Code 10
PRId Payer Code AN
PR PRmcc Payer MCC AN 20
PRvpa Payer VPA AN 255 255
PEId Payee Code AN
PE PEMCC Payee MCC AN 20
PEvpa Payee VPA AN 255 255
REld Rem Code AN
REifsc REMIFSCCODE AN 11 20
RE
REaccType Remitter Account Type AN 30
REaccountNo REMACCOUNTNUMBER AN 30 30
BEId Bene Code AN
BEifsc BENIIFSC CODE AN 11 20
BE BEaccType Bene Account Type AN 30
BEaccountNo BENEACCOUNTNUMBER AN 30 30
LRN Lite Reference Number AN 35 36
ResField1 ResFieldt
ResField2 ResField2
ResField3 ResField3
