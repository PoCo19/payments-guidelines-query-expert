# RuPay | OC023 | FY 23-24 | Enablement of Pre-authorization for RuPay cards

Circular/reference number: NPCI/RuPay/023/2023-24
Date: 20th December 2023

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/RuPay/023/2023-24 20th December 2023
To,
All RuPay Members - Banks, Payment Gateways (PGs)
Subject: Enablement of Pre-authorization for RuPay cards
Dear Sir / Madam,
RuPay has enabled Pre-authorization functionality for specific Merchant Category Codes (MCCs) to
provide an improved and convenient payment option for RuPay cardholders.
Pre-authorization often referred to as 'pre-auth', is a key feature which serves as a means for businesses
to reserve a specific amount of a customer's funds temporarily, ensuring that the necessary funds are
secured before the services are availed and the transaction can be settled subsequently. Businesses
while offering customers a secure and efficient payment process.
Identifying Pre-authorization transactions: Indicator for Pre-authorization transaction will be present
in DE-25 with value 55. For detailed information, kindly refer to RuPay - Online Switching Interface
Specification.
Development required for the following entities:
i. Issuer: The issuer shall identify the Pre-authorization transaction basis DE-25 and secure the
funds in the cardholder's account.
i. Acquiring Bank: The acquiring bank shall send the value 55 in DE-25 to initiate a Pre-
authorization for POS transaction.
ili. Payment Gateway (PG): The PG shall send the pre-authorization indicator to initiate a Pre-
authorization for ECOM transaction.
RuPay Debit/ Credit cards.
Member banks/ PGs are requested to make all the necessary changes and comply to the above actions
by28thFebruary2024.
Yours sincerely;
SD/-
Kunal Kalawatia
Chief of Products
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4oo O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
Annexure I
Please refer the below table for the provisional MCC list for which the Pre-authorization transactions will
be allowed.
MCC Description Allowed Days and Maximum allowable limit
7011 Hotel Bookings 4 days and 15% of the authorized amount
8062 Hospitals 4 days and Rs 10,000 over and above authorized amount
3351 to 3441 Car Rentals 4 days and 15% of the authorized amount
4112 PassengerRailways 4 days and 15% of the authorized amount
4121 Cab booking 4 days and 15% of the authorized amount
Customer Lifecycle in Pre-Authorization -
Request for Pre-Authorization: When the payment is initiated, the merchant sends an
authorization request to secure the funds in the customer's account.
Authorization: The issuing bank verifies the customer's account for availability of funds and
accordingly will approve/ decline the transaction.
Hold Period: During this period, the authorized amount is secured on the customer's account.
It's essential to ensure that the final settlement occurs within the specified timeframe, which is 4
days.
Settlement: There will be no change in the settlement process. However, the merchant/ acquirer
is expected to raise the presentment within 4 days from the date of presentment post which, the
pre-authorization request would become void.
For example, please refer the below illustration:
Day Scenario Description
Day 0 Merchant initiates the pre-auth (Date of transaction)
Day 0 Issuer checks the availability of funds and places temporary hold on the specified amount and
provides the confirmation.
Day 0 Merchant/ Acquirer can initiate a cancelation request for Pre-auth or proceed with presentment. If the
merchant initiates to cancel the pre-auth, the funds held will be released by the issuer
Day 1 Merchant/ Acquirer can initiate a cancelation request for Pre-auth or proceed with presentment.
Day 2 Merchant/ Acquirer can initiate a cancelation request for Pre-auth or proceed with presentment.
Day 3 Merchant/ Acquirer can initiate a cancelation request for Pre-auth or proceed with presentment. A
maximum of 4 days are allowed to present the transaction (Day 0, Day 1, Day 2 and Day 3) by which
Issuer should receive the presentment.
Day 4 If presentment is not received by Day 3, funds held on the cardholder's account will be released by
the Issuer.
1001A, The Capital, B Wing. 10th Floor.
Bandra Kurla Complex, Bandra (E), Mumbai 4o0 O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
C1N: U74990MH2008NPL189067

<!-- Page 3 -->

NPCL
NATIONALPAYMENTS CORPORATIONOF INDIA
Handling allowable limit over and above the Pre-authorized amount:
In some cases, the final settlement amount may differ from the initial authorization due to additional
charges or adjustments. Issuer is required to handle these variances appropriately. Here's an example:
Scenario: A customer pre-authorizes a credit card for INR 2000 at a hotel. Upon check-out, the final bill
is INR 2100, including incidentals. In this case, the merchant needs to settle the transaction with the
additional amount of INR 100.
Process: The merchant will send a presentment for INR 2100, which will include the additional usage.
The issuing bank shall process this request, and the additional INR 100 will be charged to the
customer's account.
It's important to note that a settlement may have a different amount than the initial authorization, such as
when additional charges or adjustments are made. Issuers shall have chargeback rights in case of any
customer's complaint.
a. If the acquirer submits the presentment after 4 days, the issuer may choose to honor it or
reject it. If the issuer honors the reguest, the issuer will have the right to raise the
chargeback under late presentment (Reason code - 1081).
b. In the event where the customer raises the dispute for additional amount charged or the
additional amount is not there in the cardholder's account, the issuer will have the right to
raise the chargeback under incorrect transaction details (Reason code - 1083). This is to
facilitate a smoother resolution process and minimize potential disputes.
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Compiex, Bandra (E), Mumbai 400 O51.
T: +9122 40009100 F: +9122 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 4 -->

NPCL
NATIONALPAYMENTS CORPORATIONOFINDIA
Annexure II
<< ON BANK LETTER HEAD >>
To, <<Date>>
Chief of Products,
National Payments Corporation of India
3rd Floor, Raheja Titanium, Off. Western Express Highway,
Goregaon (East), Mumbai, 400063
Subject: Reguest for enabling Pre-Authorization transactions for <<Bank Name>> RuPay Cards
Dear Sir/Madam,
With reference to the circular no. NPCl/2023-24/RuPay/023 dated 20th December 2023, this is to inform
you that our Bank has completed development to process Pre-Authorization transactions for RuPay
Cards. We have made the necessary changes in our Production System and have kept reguired controls
at our end.
Request you to enable Pre-Authorization transactions for our Bank cards (Please refer the selection (V)
at the earliest.
Credit Card
Debit Card
In cases where a customer's account lacks sufficient funds for a transaction, except for the pre
authorization hold, the bank shall bear the responsibility to honor payment to the merchant.
'The bank shall ensure that the pre-authorization hold amount, duly specified by the merchant, remains
accessible to cover the pending transaction until the final settlement amount is determined.
Regards,
<<Name of the official>>
<<Designation>>
<<Organization>>
1001A, The Capital, B Wing, 10th Floor.
Bandra Kurla Complex,Bandra (E),Mumbai 4ooo51.
T:+912240009100F: +912240009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067
