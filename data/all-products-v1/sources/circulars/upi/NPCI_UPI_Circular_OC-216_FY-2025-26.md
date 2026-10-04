# UPI | OC No. 216 | FY 2025-26 | UPI lite raw data file version 4.0

Circular/reference number: NPCI/UPI/OC216/2025-26

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
NPCI/UPI/OC216/2025-26 Jun 06, 2025
To,
All Members of Unified Payment Interface (UPl)
Subject: UPl Lite Raw Data File Version 4.0
live on UPI LITE have been advised to maintain LRN wise balances and carry out
reconciliation at LRN level. In order to facilitate such reconciliation banks shall be provided
with LRN wise balance for each transaction in raw file for reconciling the same with Lite Pool
I GL account on daily basis.
Transaction wise LRN balance raw file naming convention will be as follows (Read @@@ as
three digits short code of the bank). For example:
UPILRNRAWDATAACQ@@@050325_10C.cSV.pgp
UPILRNMERCHANTRAWDATAACQ@@@050325_10C.cSV.pgp
New UPi lite raw file version 4.0 will be provided for every settlement cycle.
It may be noted that currently various banks are using different versions of raw files (1.0 to
4.0). In order to bring uniformity and ease of maintenance it has been decided to withdraw
the lower versions of raw file with ultimate aim of moving all the banks to 4.0. The following
action is required from the banks using different versions:
1. Banks, currently, live on UPl lite version 3.0 should migrate to the new raw file version
4.. UPl lite balance in raw data file for each transaction will be provided in an
additional column which is added in Raw data provided for remitting banks.
2. Member banks that are still using lower versions (1.0 and 2.0) are advised to move to
higher versions, preferably version 4.0 so that they are future ready for going live with
UPI lite.
3.Withdrawal of older version:
a. For the banks that are live on UPl lite, the version 4.0 shall be mandatory and
hence version 3.0 shall be withdrawn.
b. For other banks using versions 1.0 or 2.0 version 4.0 shall be preferable
however 3.0 shall be mandatory. Versions 1.0 and 2.0 shall be withdrawn.
4. The above changes shall be effective October 01, 2025.
Member banks are advised to take note of the above and make necessary changes in all
applicable systems for performing daily reconciliation smoothly and efficiently.
The information herein may please be disseminated to the officiais concerned.
With warm regards,
SD/-
Giridhar G M
Chief - Customer Success
Enclosed: Annexure - 1

<!-- Page 2 -->

IOLN
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure - 1
UPI LITE RAW FILE VERION 4.O FORMAT & SPECIFICATION
Max
New Field Field Actual length
Prefix name Description Type Length (For Sample Date
Future
use)
TIsubtype Transaction Type AN 20 U3
TItxnid UPI Transaction ID AN 35 100 4e6eb8209582479aad3608ca9901193a
Terrm RRN AN 12 100 506415108438
TIrespCode Response Code AN 20 00
TIDate Transaction Date 030525
TI TItime Transaction Time 152505
TIsetAmount Settlement Amount 15,2 15.2 2000
Tiumn UMN AN 255 255 22ATbrGPiFwtMAcO30oFpePGwys@andb
TIMapperid Mapper Id AN 16 16
TCinitiationMode Initiation Mode AN 10
TCpurpose Purpose Code AN 10 82
PRid Payer Code AN ABC
PR PRMCC Payer MCC AN 20 0000
PRvpa Payer VPA AN 255 255 22ATbrGPiFwfMAcO30oFpePGwYS@andb
PEid Payee Code AN ABC
PE PEmcc Payee MCC AN 20 0000
PEvpa Payce VPA AN 255 255 46AFEKyk2wW1fbwUajSihaTCAzt@andb
REid Rem Code AN ANC
RElfsc REM IFSC CODE AN 20 ABDB0123456
RE REaccType Type Remitter Account AN 30 10
REaccountNo NUMBER REM ACCOUNT AN 30 30 111112222233333444445555566666
BEid Bene Code AN ABC
BEIsc BENI IFSC CODE AN 11 20 ABDB0123456
BE
BEaccType Bene Account Type 30 01
BEaccountNo BENEACCOUNT NUMBER AN 30 30 999998888877777666655555444444
LI LRN Payer Lite Reference AN 35 35 55555762111111122226666666666666666
FS FuelSurcharge Fuel Surcharge 15,2 15,2 100
GSTonFueiSurcharge surcharge GST on Fuel 15,2 15,2 18
LI liteRefNoPayee Number Payee Lite Reference AN 35 36 58780762111111122226666666666677777
LRN balance (15
liteBalanceAMT length and 15,2 15,2 120
decimals)
Beneficiary, LI= Lite, FS= Fuel Surcharge

<!-- Page 3 -->

NPCI
NATIONAL PAYMENTS CORPORATION OFINDIA
UPl lite raw file format
UP1 Lite Version 4 - U3 file format
HT,Acquirer,7C,10150486,4.0
@ib,1,11,81,icp,o080,3757b9c6443c454cb4457ce9677081d7
Qilp,c000,01988048147098031160760891805450.n@i,cBc.8cRBaBc,1,56410017767,cBC,BcRBcRI,1,641810007767,0100810481.4709003107608618
450,311
TX,3,UPc678ele86d5c79c509e99celd9c5,38339765,80,04061,30034,00008,,00,41,NPI,8000,8630914301@upi,NPI,0000,8639143
FT,13786,396665191
UPl Lite Version 4-U2file format.
HL.MerchantAca,7c,20250406,4.
TX,2,B25697e96f5e3484b27a27164e4de23,225275337034,00,04625130023500,111,44,ABC,0800,rajrohitjain71@LBY,XG,5943,spay-2403067
@obizaxis,XY,BARB0JUBILE,2,8898201111736,AXBUTIBe080553,0290211108728639268221110900270852238569445003,18850
@LBYM,554,paymr6g@py,AVHMA1,33118024,PM,BMUL,2,114208808110089042495,70
FT,2,2128B95107
