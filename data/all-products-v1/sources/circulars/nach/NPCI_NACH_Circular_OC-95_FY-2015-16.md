# Circular No.95 - Additional Features in Aadhar Lookup for APB Credit

Circular/reference number: NPCI/2014-15/NACH/Circular95

<!-- Page 1 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2014-15/NACH/Circular95 March16,2015
To,
All NACHParticipating Banks
AdditionalfeaturesinAADHAARLookupforAPBCredit
Madam/DearSir,
We refertoour CircularNo.NPCl:2012-13:NACH:CircularNo 2 dated15th
March2013onthesubjectof“EnablingofAADHAARLookupfeatureforAPB-Credit
on NACH system.Adding to the existing features that banks will be able to view
themandate flag,OD flagand OD date.
2.The input fileformat will remain sameas prescribed in the Circular# 2however
to get the mandate flag, OD flag and OD date in addition to Aadhaar then the file
naming convention should be in thegiven format in Annexure 1.
3.Now that the member banks can verify the OD flag using following options,
1.NACHApplicationunderBankMiSoption
2.API
3.Aadhaarlookupfacility
4.Banks can continue using the old naming convention (UID-ST-ABCD-ABCDOO1-
DDMMYYYY-000001-INP.txt)toknowonlythestatusofAadhaarnumber.
Withwarmregards,
GiridharGM
VPandHead-CTS&NACHOperations
C-9,8thFloor qT/Phone:02226573150
RBlPremises q/Fax:02226571001
Bandra-KurlaComplex 专-/email:contact@npci.org.in
Bandra East aw/Website:www.npci.org.in
-400051 Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexurel
New filenaming convention
UID-MAP-ABCD-ABCD001-DDMMYYYY-000001-INP.tXt
Expected output fileformat
S.No Field Name FieldDescription
AadhaarNumber Aadhaarnumberofthebeneficiary
Mapping Status Status of Mapping
Mandate Flag Status of the flag
ODFlag Status of OD
ODDate Date onthe OD flag enabled
6 digit liN of the bank which holds the account for the
Mapped IIN
beneficiary
BankName Nameof theBank
LastUpdatedDate LastupdatedDateof theAadhaarnumber.
