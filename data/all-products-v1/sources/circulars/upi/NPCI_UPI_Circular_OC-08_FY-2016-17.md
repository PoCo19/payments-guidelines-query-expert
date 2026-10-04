# Circular 08 - Addendum to Circular for implementing UPI 1.5 changes

Circular/reference number: NPCI/UPI/OCNo.8/2016-17
Date: 19th September 2016

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOF INDIA
NPCI/UPI/OCNo.8/2016-17
November15,2016
AllMemberBanks-UnifiedPaymentsInterface (UPi)
DearSir/Madam,
Sub:Addendum toCircular for implementing UPI1.5changes
We draw your attention to our earlier circular no. NPCl/UPl/0C No: 07 /2016-17 dated 1gth of October, 2016
held on the 1gth of September 2016, the members deliberated multiple matters, most of which were
communicated in the aforementioned circular.
2) At present, the customer generates his UPI PIN through the PSP App using the "last 6 digit of the Debit
Card & Expiry date" as the first factor & the "lssuer generated oTp" as the second factor. In this regard,
NPCI had received inputs from member banks to provide for usage of ATM PIN as the 2nd factor for
generating UPI PIN while on-boarding the customer. NPCI took cognizance of this aspect and
accordingly tabled an agenda of 'Generating UPI PIN using ATM PIN as the "What you know factor"
with the IMPs/UPI Steering Committee in its meeting held on 19th September 2016.
3) NPCl, now having received consensus from all members of the Steering committee wishes to advise
that banks shall provide for the usage of ATM PIN in addition to existing factors.
a. Changes at NPCI end to capture the ATM PIN within the NPCI library and changes in the
message specifications to accommodate the ATM PIN. NPCI shall be progressing to make
requisite changes in this regard.
b. Member banks shall be required to make changes in their UPI PSP App flows to enable capture
of ATM PIN (only on NPCI Library). Like-wise a communication to the members with regard to
the change in the process flow, both at the front-end (PsP App) and through other written
communicationis warranted.
c. Issuers will need to first identify the full card number and validate the pin by sending message
to EFT switch operated by the bank.
Member banks are advised to make requisite changes as per above and this change can be released along with
UPI1.5 releasei.e, by 31st Dec 2016. You may please bring this communication to the notice of all relevant staff
in your organization. Member banks are advised to keep the internal Risk Management department informed
in this regard.
We are also attaching herewith a proposed/recommended architecture flow "Annexure I" for your reference
and use.
Yours faithfully,
DilipAsbe
Chief Operating Officer
1001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051. T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
ANNEXUREI
1.Customer downloads UPI PSP App of his choice from the Google play store.
2. PSP App sends an encrypted SMS to the PSP server along with device details and mobile number for
hard-binding' the device. The hard bound device shall act as the first factor of authentication for all
subsequenttransactions.
3.The Customer creates his profile on the PsP App and subsequently selects the bank where he holds
theaccount.
4.The accounts linked to the mobile number are fetched from the Issuing Bank through the defined APls
& linked accounts are displayed on thePsPApp (in maskedformat).
5. The preferred account no. is selected by the customer and is added.
6. In order to create UPI-PiN for the first time / change or set his UPI PIN, the customer enters the last 6
digits of his/her debit card and the expiry of the card (the existing factors).
7. The customer shall be required to enter his ATM PIN and Issuer OTP in the NPCI Library.
8.The customer enters his preferred UPI PIN in the NPCI library.
9. The existing details & the ATM PIN (additional factor) along with the desired UPI PIN is forwarded to
the issuerthroughthe secured mechanism.
1o. Issuer supposed to validate the same andgive a response to UPI system.
