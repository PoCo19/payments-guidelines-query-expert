# RuPay | OC018 | FY 24-25 | Modification in NPCI EFRM & BCS portal for RuPay chargeback

Circular/reference number: OC-018

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
NPC//2024-25/RuPay/018 December 06th 2024
To,
All Members participating in RuPay (Domestic) Scheme
Dear Sir /Madam,
Sub: Modification in NPCI EFRM & BCS portal for RuPay chargeback processing
NPC! has made the dispute resolution mechanism available for all the stakeholders to facilitate
improve the efficacy of charge back process and prevent unscrupulous elements exploiting
the systems it has been decided to implement the following decline rules and controls.
A. Rule in BCS:
a. Chargeback raising through File Upload:
Any cardholder raises chargebacks exceeding 5 in a period of 30 rolling days
then such cards shall be blocked for raising further chargeback through file
upload option in the RuPay BCs portal. The rejection message will be displayed
in the front end with rejection reason "More than the allowed number of
chargebacks raised in the last 30 days". The rejection report will also be
available as in the curent bulk upload failure scenario. From the 6th chargeback
onwards the issuing bank will have to raise the chargeback through front end
with a maker checker control in the RuPay BCs portal by submitting a
declaration / Proof of Purchase transactions.
This shall be effective December 17, 2024.
b. Chargeback raising through Front End:
If any issuer bank raises chargebacks using only the front-end option right from
the first chargeback, maker checker control applies right from the first
chargeback. From the 6th chargeback onwards issuing bank will have to submit
the declaration. The document uploaded should be legitimate with stamp and
sign of the issuing member bank officials.
The format of the declaration and the types of evidence that banks should submit is
attached in the Annexure A and Annexure B respectively. Bank officials should do
proper due diligence at their end while dealing with such cases. If the case is referred
may decide the verdict against the issuing member as part of compliance.
B. FRM Rule: In cases where any card holder raises chargebacks exceeding 5 in a period
of 2 months then such cards shall be included in the negative list in FRM, and the
following rules shall be applied:
1. Any further transactions (POS/ECOM) pertaining to the cards that are part of such
negative list shall be declined with Reasory code 59 - Suspected Fraud, decline.
Page1l6
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4Oo Os1.
T: +91 22 40009100 F: +91 22 40009101
contact(anpci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCL
NATIONAL PAYMENTSCORPORATIONOF INDIA
a. It may be noted that the chargeback already raised by the customer (before the
card getting included in the negative list) shall continue to be in open state,
acquiring banks should verify and take appropriate action.
b. Banks can search rejected authorisation transactions in real time using front
end NPCI EFRM portal through relevant risk score. Banks can also search
transactions rejected under the RuPay chargeback rule in daily perimeter
report in the SFTP folder made available by NPCl. The report gives a
comprehensive view of transaction level data for easy reference.
c. To cater to genuine customers, there will be an option to unblock the card
through NPCl. The process for unblocking is explained in the Annexure C
attached to the circular.
& update customer accordingly by sending email & SMS.
e. Issuing Bank to maintain a separate list of such cards details so that further
complaints received from same card can be reviewed for suspected behaviour
before raising chargeback.
This shall be effective December 10, 2024.
Advisory for the banks for controlling charge back volume:
Issuer:
It is expected that the Issuer carries out desired due diligence before raising the chargeback
on the Acquirer. Some recommended best practices are:
1. Posing "challenging questions" related to the disputed transactions.
2. Reaching out to the customer who are raising unduly high number of chargebacks and
understanding the issue.
3. If the customer appears to be trying to exploit the system, then further course of action
as may be required should be initiated.
Acquirer:
[t may please be noted that the merchant is the responsibility of the acquirer therefore all
efforts should be made that the merchants adhere to the scheme rules and customer
complaints are very minimal. Also, in case of customer complaints, specifically for not
providing goods and services the merchants should have a very strong mechanism for
redressal. Additionally, the acquirers shall do the following:
1. Periodic analysis should be carried out to identify the merchants who are receiving
excessive number of chargebacks, especially more so in offline cases.
2. Wherever required, the Acquiring bank should do deeper analysis and also reach out
to such merchants who are receiving huge number of chargebacks for necessary due
diligence.
3. It is necessary to weed out the merchants that are facilitating any misdeeds so that the
genuine customer interests are taken care.
Page2l6

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
It may please be noted that the measures listed above are only indicative, both issuer and
acquirer banks shall take all the possible measure to ensure that their customers / merchants
do not exploit the systems. Further it may be noted that the existing policies and procedures
will continue to be applicable for chargeback and disputes.
The information herein may please be disseminated to all the concerned for necessary action.
relationship manager.
With warrgregards
Giridhar G M
Chief of CustomerSuccess
Page3l6

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure A
Declaration Format
Use separate declarations for each case.
(OnBank'sLetterhead)
Date:
To,
The RuPay Operations Team,
National Payment Corporation of India,
Madam/Dear Sir,
Subject: Declaration from the customer for the Disputed transactions
We declare our cardholder,  has done the transaction
with the merchant on .Pleasefind belowthe transaction details.
We hereby acknowledge the declaration furnished herewith is true and correct. We request you to
kindly take note of this declaration for your records.
Merchant Name
RRN
Mask Card No
Transaction Amount ( Rs)
Transaction Date
Invoice No( In Any)
DescriptionofGoods&Services
AnymoreremarkorInputs bycustomer
(Authorized Signatory)
Name & Designation of the Signatory
Bank Seal
Page4l6

<!-- Page 5 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
Annexure B
Types of Evidence
Reason Code and Documentstobesubmittedby Documents to be submitted by
Description Issuer Acquirer
RC 1061- Credit not
processed for cancelled
or returned goods or Merchant letteradvisementto Document showing Credit was
services obtain credit processed
RC 1062- Goods and
services not as described
or cardholder received Document that justifies Goods and
defective goods or services were as per customer's
services Customer complaint letter description
RC 1063- Paid by
alternate means and card
was also billed for the Proof of payment done by other Proof of payment not received by
same transaction means other means
RC 1064- Go0ds or
services not provided /
Not received - Services Proof showing expected date of
were not provided or arrival
goods not received by Proof showing Goods or services
cardholder not received Proof of delivery
RC 1065- Account
Debited but Confirmation
Not Received at Merchant Proof of delivery
Location Customer complaint letter Proof of refund
Charge slip, Goods & services
receipt, Challan with the
Merchant name and transaction
date and time, transaction Delivery challan, Goods and
Card Present Transactions amount services delivery confirmation
Merchant emaiV Merchant App
notification and statement,
system generated challan by
Card Not Present merchant, Order details with the
Transactions shipment details. Proof of delivery
Page5l6

<!-- Page 6 -->

NPCI
NAYIONALPAYMENTSCORPORATIONCFINDIA
Annexure C
Process for Unblock of cards from FRM Block
Issuer bank to share the below information through a CRM ticket for unblock of card.
Sr No Fields
BIN Number
Masked PAN (First Six/Eight digits to be masked)
2. Bank user to raise the ticket in the CRM portal under the below category.
a. Department- Operations
b. Product- RuPay
C. Category-Unblock of Card
d. Sub-Category-Unblocking of card in EFRM
3. Up on receipt of the ticket NPCl will unblock the card within 48 hours.
Page6l6
