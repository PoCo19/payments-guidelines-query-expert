# UPI | OC No. 200 | FY 24-25 – Enablement of UPI Mandate feature of Single Block Multiple Debits

Circular/reference number: NPCI/UPI/OC.No200/2024-25
Date: 14th May 2020

<!-- Page 1 -->

NPCL
NATIONALHAYMENTS CORPORATIONOFINHA
NPCI/UPI/OC.No200/2024-25 31st July,2024
To,
All Members of Unified Payments Interface (UPl)
Dear Madam/Sir,
Sub: Enablement of UPl Mandate feature of Single Block Multiple Debits
With reference to circular NPCi/UPl/OC No.56/2018-19 dated 14thAugust 2018, Mandate
services were introduced in Unified Payments Interface (UPl) wherein the customer can pre-
authorise a transaction by blocking funds in the account for a debit to be initiated later.
Currently UPI supports One Time Mandate and Autopay as mandate services.
Feature of Single Block Multiple Debits
To further extend the mandate services, we are introducing Single Block Multiple Debits
mandate services wherein UPl mandate can be created with the block functionality where the
customer can pre-authorise a transaction by blocking the funds in the account for multiple
debits which shall be initiated later till the blocked funds gets exhausted or the mandate service
has been revoked. Members are required to ensure below guidelines are followed:
1. The issuer banks shall support the functionality of Single Block Muitiple Debit services
wherein the bank shall have the mechanism to create blocking of funds in the
customer's account and shall allow multiple debits against the block. The fund shall be
blocked in the account till the time mandate is expired, revoked or the mandate amount
is exhausted.
2. The UPl Apps shall support the necessary functionality and interface on their app for
the customer to process the transactions.
3. Members shall ensure that the mandate created successfully shall also be executed
successfully. All the necessary validation should be at the time of mandate creation
only.
4. The issuer bank shall ensure the necessary communication to the customer for all the
mandate related operations.
1001A, The Capital,  Wing. 70th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4o0 O51.
T: +91 22 40009100 F: +91 22 40009101 www.npci.0rg.in
CIN:U74990MH2008NPL189067
contact@noci.ora.in

<!-- Page 2 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
5. Acquiring Bank shall ensure that they are extending the services of Single Block and
Multiple Debits to the relevant merchants and are also making the necessary
developments at their end to support the services.
6. Banks shall ensure that proper reconciliation of transaction shall be performed as per
the extant NPCI guidelines.
This functionality can be used for services wherein the assurance on funds is required before
the delivery of goods/ services and ensures proper settiement of funds when a debit is initiated
a. Based on the use case, specific purpose codes shall be passed by the acquirer to
identify the transactions and process it accordingly. For Single Block Muitiple Debits,
the below are the Purpose codes defined:
Sr. No Purpose Code Use Case
76 Securities brokers and dealers (Secondary Market)
Online goods and service delivery
78 To be reserved for future use
79 To be reserved for future use
Note: Acquirers need to pass the correct purpose codes as specified based on use case.
b. Such mandate creations shall be payer-initiated mandates wherein the customer can
create mandate from the below mentioned methods:
i. QR based
Intent
SDK/Plug In
The execution/debit of the mandate shall be as per the extant mode of mandates.
Othermode of initiation shall be envisaged later.
The per transaction limit for such mandate creations shall be Rs 5 Lakh for the
purpose code 76, while for purpose code 77 existing UPl fimits shall be applicable.
It is re-iterated that issuer bank shall do all the necessary validation at the time of
mandate creation, The execution of such mandates shall be considered success with
the premise that mandate created successfully shall be executed successfully. With
reference to NPCI/UP//OC No. 88/2020-21 dated 14th May 2020 and further with
NPCI/UPI/OC No.128/2021-22 dated 14th December 2021, NPCI has defined the
scope of Deemed Debit and the same shail be extended to Single Block Multiple
Debits mandates as well.

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
e. Customer shall also be provided with an option of revoking the mandate based on
the merchant use case. Member shall ensure that revokes are successfully
processed in UPl.
t. Payer App/PsP shall clearly inform the type of mandate getting created to the
customer on the App interface. Payer App/PsP shall also make the provision for the
UPl feature of Invoice in the box functionality which will be envisaged for such
mandate use cases.
g. The Single Block Multiple Debit mandates shall be only applicable for P2M category
of transactions.
h.
Mandate block transaction type is defined. The member banks are instructed to refer
the circular UPl/0C/No.78/2019-2020 dated 27thJanuary 2020 and other necessary
guidelines for handling the reconciliation of Mandate with Single Block and Multiple
Debit transactions.
Further, additional guidelines to be followed are mentioned in the product document on
Mandate with Single Block and Muitiple Debits. (Annexure - A)
Member are requested to hereby note the changes and enable the feature by 3oth
November 2024.
Yours Sincerely,
SD/-
Kunal Kalawatia
ChiefofProducts
Ref: Annex A - Product Document on Mandate with Single Block and Multiple Debit
