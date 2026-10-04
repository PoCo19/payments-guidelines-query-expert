# RuPay | OC026 | FY 23-24 | Deferred authorization solution for Credit-card

Circular/reference number: OC-026
Date: 2nd January 2024

<!-- Page 1 -->

NPCL
NATIONALPAYMENTS COEPORATIONOFINDIA
NPC1/2023-24/RuPay/026 2nd January 2024
To,
All Member Banks- RuPay
Subiect -RuPay Deferred Authorization solution for Credit card.
Dear Sir/Madam,
RuPay is the first-of-its-kind domestic Card payment network of India, with wide acceptance at ATMs,
Pos devices and e-commerce websites. Deferred Authorization payment enables credit card
purchases in offline scenarios like flights, cruises etc. In this transaction, the authorization process is
deferred until the POs terminal reconnects back, to offer purchase of various products and services
to enhance the consumer experience. All the validations of Card Present POs transactions shall be
applicable for Deferred Authorized transactions. The relaxation in requirement of Additional Factor of
Authentication (AFA) for Card transactions in Contactless mode shall be as per the RBI circular-
RBI/2020-21/71 DPSS.CO.PD No.752/02.14.003/2020-21dated 4th December, 2020.
Key features:
1. Issuer shall validate and respond to transactions, when the device reconnects back to the
network and thetransaction is sentto issuerforvalidation.
2. Acquirer shall equip the POs terminals for temporarily deferring authorization process during
the initial purchase by securely storing the card data, and sending the transactions for
validation post device coming in network.
3. Such merchants may offer products for purchase by use of POs terminals for card payments,
and ensure completion of the transaction post device coming in network.
Please refer Annexure A for the detailed transaction process flow of the inflight use case of deferred
authorization solution.
Your Sincerely,
SD/-
Kunal Kalawatia
Chief ofProducts
1001A, The Capital, B Wing, 10th Floar,
Bandra Kurla Complex, Bandra (E), Mumbai 4o0 O51.
T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN: U74990MH2008NPL189067
contact@npci.org.in

<!-- Page 2 -->

NATIONALPAYMENTSCORPORATIONOFINDLA
Annexure A
Please find below processing flow of inflight use case for deferred authorization solution
Step 1: On-board Sales- During the flight, airlines shall offer a selection of products and
services for purchase, such as food and beverages, entertainment, Wi-Fi access, and more.
Step 2: Card Payment Acceptance- To facilitate these purchases airlines equip their flight
attendants with portable POs terminal. These devices are capable of accepting credit card
payments securely.
Step 3: Card Processing- When a passenger decides to make a purchase, the staff will
present the POs terminal to the passenger, who can then insert or tap their credit or debit
card to initiate the transaction.
step 4: During the initial purchase process, the payment system will temporarily defer the
authorization step. This will be done at terminal end by storing the Track2 and PiN data of
the card which will further get stored in data base with Payment Card Industry Data Security
Standard (PCI DSS & PCI PTS) recommended encryption method.
Step 5: Post-Purchase Authorization- once the flight gets landed and terminal comes in
network connectivity the stored transaction will be sent to issuer for details validation and the
response(approved/decline) will be provided to terminal operator.
Step 6: Receipt & Completion of Payment- The passenger receives a receipt for the
transaction. Once the user successfully gets the transaction completion message from Issuer
then the transaction will get completed.
Step 7: Settlement- There is no change in settlement process as the transaction will be settled
solution.
We request member banks to enable Defered Authorization solution for RuPay customers by
considering the below benefits to both customers and merchants:
It provides a smoother and faster checkout experience, reducing the need to enter payment
details for every purchase.
1001A, B wing, 10th Floor, The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai - 400 051
CIN:U74990MIH2008NPL189067
Page 1 of 2

<!-- Page 3 -->

NC
NATIONAIPAYMENTSCORPORATIONOFINDIA
to carry cash for on-board purchases.
It also benefits by increasing on-board sales revenue and reducing the complexity of
handling cash during flights, cruise etc.
POS, certified for PIN Security Requirement (PCI- PTS) with the capability for PIN and track2
storage shall be certified with PCI DSS for managing the card transaction data.
We request members to make a note of the above and disseminate the information to the
concerned teams.
