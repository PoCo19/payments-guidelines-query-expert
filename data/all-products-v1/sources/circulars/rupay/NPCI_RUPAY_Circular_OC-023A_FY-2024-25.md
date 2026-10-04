# RuPay | OC023A | FY 23-24 | Addendum to OC 023 – Enablement of Pre-authorization for RuPay Cards

Circular/reference number: NPCI/RuPay/023A/2023-24
Date: 1st February 2024

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINIIA
NPCI/RuPay/023A/2023-24 gth February 2024
To,
All RuPay Members - Banks, Payment Gateways (PGs)
Subject: Addendum to OC o23 - Enablement of Pre-authorization for RuPay Cards
Dear Sir / Madam,
We refer to RuPay product circular vide reference no. NPCl/RuPay/023/2023-24 dated 20th December
2o23, on enablement of pre-authorization for RuPay cards, which provided the guidelines for allowed
days and maximum allowable limit for pre-authorized transactions.
The RuPay Steering Committee held on 1st February 2024 discussed the allowed days and maximum
allowable limit for pre-authorized transactions and endorsed the following revisions:
Sr. No. MCC Description Allowed Days Final Amount
3351 to 3441 Car Rentals 7 days The final bill amount should be less
4112 Passenger Railways 7 days than or equal to the pre-authorization
amount. If the final bill exceeds the
4121 Cab booking 7 days
pre-authorization amount, a fresh
7011 Hotel Bookings 7 days authorization must be initiated for the
8062 Hospitals 7 days remaining/ total bill amournt.
Please find the action required from the member banks and PGs:
1.  Issuing Bank: The issuer shall identify the pre-authorization transaction basis the value 55 in
DE-25 in the online transaction message and shall secure the funds in the cardholder's account.
It shall also ensure that the pre-authorization hold amount, duly specified by the merchant,
remains accessible to cover the pending transaction until the final settlement amount is
determined.
2. Acquiring Bank: The acquiring bank shall send the value 55 in DE-25 in the orline transaction
message to initiate a pre-authorization for POs transaction.
3. Payment Gateway (PG): For online e-commerce transaction, the PG shall send the pre-
authorization indicator in the BEPG_Authorize APl to initiate a pre-authorization.
Pease refer Annexure I for customer lifecycle in Pre-authorization. Members are reguested to refer to
RuPay Online Switching Interface Specification document and BEPG Acquirer Interface guide for more
information.
Member banks/ PGs are requested to make all the necessary changes and comply to the above actions
by 31st March 2024.
Yours sincerely,
SD/-
Kunal Kalawatia
Chief of Products
1001A, The Capital, B Wing, 1oth Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4O0 O51.
CIN:U74990MH2008NPL189067
contact@npci.org.in

<!-- Page 2 -->

NPC
NATIONALPAYMENTS CORPORATIONOFINIIA
Annexurel
Customer Lifecycle in Pre-Authorization .
Request for Pre-Authorization: When the payment is initiated, the merchant sends an
authorization request to secure the funds in the customer's account.
accordingly will approve/ decline the transaction.
Hold Period: During this period, the authorized amount is secured on the customer's account.
It's essential to ensure that the final settlement occurs within the specified timeframe, which is 7
days.
Settlement: There will be no change in the settlement process. However, the merchant/ acquirer
pre-authorization request would become void.
For example, please refer the below illustration:
Day. Scenario Description
Day 0 Merchant initiates the pre-auth (Date of transaction)
Day 0 Issuer checks the availability of funds and places temporary hold on the specified amount and
provides the confirmation.
Day 0 Merchant/ Acquirer can initiate a cancelation request for Pre-auth or proceed with presentment. If the
merchant initiates to cancel the pre-auth, the funds held will be released by the issuer
Day 1 Merchant/ Acquirer can initiate a cancelation request for Pre-auth or proceed with presentment.
Day 2 Merchant/ Acquirer can initiate a cancelation request for Pre-auth or proceed with presentment.
Day 3 Merchant/ Acquirer can initiate a cancelation request for Pre-auth or proceed with presentment.
Day 4 Merchant/ Acquirer can initiate a cancelation request for Pre-auth or proceed with presentment.
Day 5 Merchant/ Acquirer can initiate a cancelation request for Pre-auth or proceed with presentment.
Day 6 Merchant/ Acquirer can initiate a cancelation request for Pre-auth or proceed with presentment. A
maximum of 7 days are allowed to present the transaction (Day 0 to Day 6) by which Issuer should
receive the presentment.
Day 7 If presentment is not received by Day 6, funds held on the cardholder's account will be released by
the Issuer.
Handling allowable limit over and above the Pre-authorized amount:
In some cases, the final settlement amount may differ from the initial authorization due to additional
charges or adjustments. Merchant is required to handle these variances appropriately. Here's an
example:
Scenario;: A customer pre-authorizes a credit card for INR 2000 at a hotel. Upon check-out, the final bill
is INR 2100, including incidentals. In this case, the merchant needs to settle the transaction with the
additional amount of INR 100.
1001A, The Capital. B Wing, 10th Floor,
BandraKurlaComplex,Bandra(E),Mumbai 4oo o51.
T: +9122 40009100 F: +91 22 40009101 www.npci.0rg.in
CIN: U74990MH2008NPL189067
contact@npci.org.in

<!-- Page 3 -->

NPCL
NATIONALPAYMENTS CORPORATIONOFINDIA
Process: The merchant will send a presentment for INR 2ooo and shall take a fresh authorization of
additional INR 1o0. Alternatively, the merchant can initiate a cancellation of earlier Pre-authorization and
initiate a new authorization for the total bill amount, which will include the additional usage.
It's important to note that a settlement may have a different amount than the initial authorization, such as
when additional charges or adjustments are made. lssuers shall have chargeback rights in case of any
customer's complaint.
a. If the acquirer submits the presentment after 7 days, the issuer may choose to honor it or
reject it. If the issuer honors the request, the issuer will have the right to raise the
chargeback under late presentment (Reason code - 1081).
1001A, The Capital, B Wing, 10th Flo0r.
BandraKurlaComplex.Bandra(E).Mumbai 4oO O51.
T: +91 22 40009100 F: 91 22 40009101 www.npci.0rg.in
CIN:U74990MH2008NPL189067
contact@npci.org.in
