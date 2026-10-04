# Circular 80 – Third party validation API using PAN in UPI

Circular/reference number: NPCI/UPI/OCNo.80/2019-2020
Date: 2nd March, 2020

<!-- Page 1 -->

NPCL
NATIONAL PAYMENTS CORPORATION OF INDIA
NPCI/UPI/OCNo.80/2019-2020 February 28, 2020
To,
All Member Banks- Unified Payments Interface (UPl)
Dear Sir/Madam,
Sub: Third party validation API using PAN in UPI
Background:
Securities and Exchange Board of India (SEBl) has introduced UPl as a payment option for public issues
vide their SEBI Circular no. SEBl/HO/CFD/DlL2/CIR/P/2018/138 dated November 1, 2018 and has also
mandated that customers have to use their own bank account while making an application.
validated with the depositories) has to be validated with PAN in the customer's bank account in order to
reject applications made using third party accounts.
We have implemented account validation (AV) as an option in UPl wherein the PAN as provided by the
customer to any Regulated Entity as part of KYC is captured in UPl through the acquiring bank and the
same is validated against the records as available in the Core Banking System (CBs) of banks and
provided in response.
II. Process flow (Using PAN as a Validator)
The objective is to provide an online mechanism of validating the PAN and Account linkages, inputting the
recipient PAN details as an additional input along with account number and IFsC or UPI id. In response,
the recipient PAN and the account details are matched against the customers' bank account and shall
accordingly pass a suitable flag in response (Success or Failure - the scenarios are Annexed)
Mermbers are requested to implement this before 2nd March, 2020
Yours faithfully
Dilip Asbe
MD & CEO
1001A, The Capital, B Wing, 10th Fioor,
Bandra Kuria Complex, Bandra (E), Mumbai 4O0 O51.
T: +9122 40009100 F: +9122 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCIN
NATIONALPAYMENTSCORPORATIONOFINDIA
(Annex to circular NPCl/UPI/OC No 80/2019-2020 dated February 28, 2020)
Third party validation API using PAN in UPI
Scenarios
Scenario 1 Scenario 2 Scenario 3
Input
PAN + (A/C +IFSC) or UPI id PAN + (A/C +IFSC) or UPI id PAN + (A/C +IFSC) or UPI id
Result PAN MATCH NO PANMATCH PAN DOES NOT EXIST
Response SUCCESS FAILURE FAILURE
Account no + IFsC
Account Nature - Single or
Joint.
Account Holder - Primary
Additional or Secondary
details No details passed No details passed
Account Type - Savings!
Current/NRE/NRO/Others
Mask Name
