# IMPS | OC 132 | FY 25-26 | Enablement of Bulk Payments in IMPS

Circular/reference number: NPCI/2025-26/IMPS/132
Date: 12th March 2026

<!-- Page 1 -->

NPCI ALWAYS
FORW RD
NATIONALPAYMENTS CORPORATIONOFINDIA
NPCI/2025-26/IMPS/132
To,
All Members -IMPS
Subject: Enablement of Bulk Payments in IMPS
With the objective of supporting instant one-to-many Type:
Circular
transactions through IMPs, Bulk Payments wili now be enabled
Product / Brand:
in IMPS. This functionality extends IMPs to the bulk disbursal
IMPS?
segment, enabling customers to initiate a single debit request
Category:
that results in multiple credits to beneficiaries in real-time. IMPSBulk Payment
IMPs members may offer this functionality to their customers, Member:
All Members
subject to adherence to the latest IMPs Bulk Payments
Technical Specifications released by NPCl (on 12th March 2026, Region:
Domestic
as updated from time to time) and compliance with the
System:
requirements listed below: IMPS Product
1. Purpose Code: Remitter Bank shall mandatorily populate Published:
12 March 2026
purpose code ‘89' for all IMPs Bulk Payment transactions.
Effective:
2. Functionality of Bulk Payments: Every Bulk Payment 05 May 2026
transaction request shall be assigned a unique set of
identifiers for the purpose of traceability, reconciliation, and Action:
Member Onboarding
auditability. Customer Channel Changes
Customer Communication
a. Each Bulk Payment transaction shall be identified by a
Parent Transaction ID and Parent Retrieval Reference
Number ("Parent RRN").
Parent Transaction means the overarching bulk payment
transaction received by NPCl from the member for
processing, containing all Child Transactions (as per the
threshold listed below).
Each Child Transaction shall be assigned a Child
Transaction ID and a Child Retrieval Reference Number
("Child RRN").
1001A, The Capital, B Wing. 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 400 O51.
T: +91 22 40009100 F: +9122 40009101
Wthir contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCL ALWAYS
FORWRD
NATIONALPAYMENTS CORPORATION OF INDIA
Child Transaction means each individual payment transaction within a Parent Bulk
Transaction, received by NpCl from the member for processing and is processed
independently while still linked to the Parent Transaction.
3. IMPS Transaction Limit: The existing IMPS per transaction limit, as prescribed by NPCl, will
continue to apply for every Beneficiary.
4. Settlement & Reconciliation:
a. Every Child Transaction under the Bulk Payment transaction shall be treated as an
individual IMps transaction for the purpose of processing, settlement, dispute
management and applicability of fees
b. The "Purpose Code" and "Parent RRN" will be added to the remitter raw data file and
adjustment report file that will be shared with the Remitter Bankl Prepaid Payment
instrument Issuer, and would require them to make necessary changes to the processing,
clearing and reconciliation processes as maybe required.
5. Fees & Charges: Existing switching fee and interchange fee shall be applicable to each Child
Transaction.
6. All Bulk Payment transactions shall continue to be governed by existing IMPs Procedural
Guidelines, Operating and Settlement Guidelines (including Dispute Resolution process),
circulars and Specification Documents released from time to time. For raising disputes, IRcs
will have an option for the IMPS Members to search for transactions using both Parent RRN
and Child RRN.
7. The role and responsibility of each Member are annexed to this Circular.
8. Members are advised to ensure that the contents of this Circular are promptly cascaded to
their respective Sub-members and other concerned entities for necessary compliance
Yours sincerely,
SD/-
Kunal Kalawatia
Chief of Products & Marketing
1001A, The Capital, B Wing, 10th Floor.
Bandra Kurla Complex, Bandra (E), Mumbai 4oo O51.
T: +91 22 40009100 F: +9122 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 3 -->

ALWAYS
FORWRD
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure
Roles & Responsibilities:
1. Remitter Banks/Prepaid Payment Instrument Issuers ("PPl Issuers") shall be responsible for
the following main activities:
a. ( Offering the functionality of Bulk Payment transactions to their respective customers
through their various payment channels.
b. Mandatorily populating purpose code ‘8g' for all IMPs Bulk Payment transactions
C. Sending a consolidated bulk IMPs fund transfer request to NPCl which should comprise
account details of multiple beneficiaries.
transaction.
e. Generating Child Transaction ID and Child RRN for every Child Transaction in Bulk
Payment transaction.
f. Verify and check per beneficiary limits in a Bulk Payment transaction.
g. Ensuring that for any failed Child Transaction/s, the amount is reversed back to customer's
account.
h. Updating reconciliation processes in accordance with the new format of reconciliation
report formats.
2. Beneficiary Banks / Prepaid Payment Instrument Issuers ("Ppl Issuers") shall be responsible
for the following main activities:
a. Credit the beneficiary's account in real-time and send confirmation to NPCl.
b. Return the transaction with the appropriate response code, as applicable.
C. Accept and return purpose code 8g' for all IMPs Bulk Payment Transactions
d. Continue to follow reconciliation and dispute resolution process as per existing IMPs
process.

<!-- Page 4 -->

ALWAYS
FORWARD
NATIONALPAYMENTSCORPORATIONOFANDIA
3.NPCI will ensure:
individual transaction and sending an individual credit request to respective Beneficiary
Banks.
b. Send a single consolidated response to the Remitter Bank/ PPl lssuer upon receipt of
status of Child Transactions from the beneficiary banks, providing the transaction status
of each Child Transaction, namely Success, Failure, or Deemed.
c. Add Purpose Code and Parent RRN columns in the remitter raw data file and the
adjustment report file shared with Remitter Bank/PP1 lssuer.
d. Apply switching fee and interchange fee for every Child Transaction as per the existing
IMPS pricing model.
