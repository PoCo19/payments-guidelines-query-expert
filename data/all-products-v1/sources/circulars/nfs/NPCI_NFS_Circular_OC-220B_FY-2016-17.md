# Circular 220B - Annexure B_Details of Interoperable Cash Deposit transaction in Raw_STL

Circular/reference number: OC-220B

<!-- Page 1 -->

Annexure B 
 
Details of ICD transaction in Raw data files and STL Reports 
 
Details of ICD transactions in raw file & STL report 
Type of Transaction 
Transaction Type 
Issuer / Beneficiary details 
Raw 
file 
STL 
report 
1. Own Account Deposit 
Cash deposit in Own account (Card & Bene a/c. validation) 
IQ 
IQT 
Issuer Card No. 
Cash deposit in Own account (Credit to Bene account) 
FD 
FDT 
Issuer Card No. 
  
2. Third party account deposit 
a) Beneficiary details (identifier): Card number 
Cash deposit in third party account (Card validation) 
PV 
PVT 
Issuer Card No. 
Cash deposit in third party account (Bene a/c. validation) 
CQ 
CQT 
Bene card No. 
Cash deposit in third party (Credit to Bene a/c.) 
CD 
CDT 
Bene card No. 
b) Beneficiary details (identifier): Aadhaar number 
Cash deposit in third party account (Card validation) 
PV 
PVT 
Issuer Card No. 
Cash deposit in third party account (Bene a/c. validation) 
UQ 
UQT 
Bene IIN + Aadhaar No. 
Cash deposit in third party (Credit to Bene a/c.) 
UD 
UDT 
Bene IIN + Aadhaar No. 
c) Beneficiary details (identifier): Mobile number + MMID 
Cash deposit in third party account (Card validation) 
PV 
PVT 
Issuer Card No. 
Cash deposit in third party account (Bene a/c. validation) 
MQ 
MQT 
Bene MMID + Mobile No. 
Cash deposit in third party (Credit to Bene a/c.) 
MD 
MDT 
Bene MMID + Mobile No. 
d) Beneficiary details (identifier): Account number + IFSC code 
Cash deposit in third party account (Card validation) 
PV 
PVT 
Issuer Card No. 
Cash deposit in third party account (Bene a/c. validation) 
AQ 
AQT 
Bene IIN + last 13 digits of account no. 
Cash deposit in third party (Credit to Bene a/c.) 
AD 
ADT 
Bene IIN + last 13 digits of account no. 
 
Transaction Type 
Raw data Files 
STL report 
Issuer file 
Acquirer file 
Issuer file 
Acquirer file 
Issuer Card Validation  
(Acquirer - Issuer) 
Issuer - PV / IQ 
Acquirer - PV / IQ 
Issuer - PVT / IQT 
Acquirer - PVT / IQT 
Beneficiary Account 
Validation  
(Issuer - Beneficiary) 
Beneficiary -  
CQ/AQ/MQ/UQ 
Issuer -  
CQ/AQ/MQ/UQ 
Beneficiary -  
CQT/AQT/MQT/UQT 
Issuer -  
CQT/AQT/MQT/UQT 
Cash Deposit  
(Acquirer - Beneficiary) 
Beneficiary -  
FD/CD/AD/MD/UD 
Acquirer  -  
FD/CD/AD/MD/UD 
Beneficiary -  
FDT/CDT/ADT/MDT/UDT 
Acquirer  -  
FDT 
/CDT/ADT/MDT/UDT
