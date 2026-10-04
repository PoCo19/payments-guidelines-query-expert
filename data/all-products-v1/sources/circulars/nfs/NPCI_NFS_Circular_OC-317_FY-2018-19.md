# Circular 317 - EMV Liability shift in DMS

Circular/reference number: NPCI/NFS/OCNo.317/2018-19
Date: 24th December, 2018

<!-- Page 1 -->

NPC
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.317/2018-19 24th December, 2018
To,
All Members ofNFSATMNetwork
Madam/ DearSir,
Sub: NFS ATM Network - EMV Liability Shift guidelines
RB1, vide its circular dated 26th May 2016, have advised, inter alia, that ATMs and micro-
ATMs instaled/operated by banksWhite Label ATM Operators (WLAOs) are enabled for
processing of EMV Chip and PIN cards.
We refer to OC 306 dated 10th September, 2018 on EMV migration of ATMs. EMV liability
shift for ATM transactions routed through NFS ATM network is not applicable oniy til 31st
December, 2018.
In the NFS Steering Committee meeting (SCM) held on 2gth November, 2018, EMV liability
shift process was discussed. The EMV liability shift process approved in the SCM is given in
AnnexureA.
We would like to inform that the EMV liability shift process for transactions routed through
NFs ATM network as mentioned in Annexure A shall be made effective from O1st January,
2019.
Please note importantly that -
1. The EMV liability shift process shall be applicable for domestic ATM cash withdrawat
and Card to Card fund transfer transactions routed through NFS ATM network
including Card & PIN micro-ATM transactions.
2. EMV liability shift shall also be applicable for international scheme cards (DFS, JCB,
UPl, etc.) accepted on NFS ATM network as per respective schemes' guidelines.
Updated addendum to NFS Operating and Settlement Guidelines (NFS-OSG) shall
be shared separately.
1001A, The Capital, B wing, 10th Floor, Bandra Kurla Complex, Bandra [E], Mumbai 400 051. T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

3.  EMV liability shift shall be applicable for transaction from 1st January, 2019 onwards.
4. Liability shift will not be applicable in the case of card lost / stolen fraud scenario, as
ATM transactions are card-present online - PIN authorized transactions.
5. : There will be no change in the NFS-RAW data files and settlement reports for EMV
transactions. However, changes are made in NFs-DMs to capture additional details
to facilitate identification of card and ATM terminal capability, and the method in
which the transaction has been processed in NFs ATM Network (as per RuPay
specifications).
Please make a note of the above change and disseminate the instructions contained herein
to officiais concerned.
For any queries or clarification, please contact:
Name e-mail ID Mobile Number
Mehfooz Khan mehfooz.khan@npci.org.in 8108122867
Avinash Kunnoth avinash.kunnoth@npci.org.in 8879772725
Yours sincerely,
Ram Sundaresan
sVP & Head -- Operations
Encl:
1. Annexure A - Procedural guidelines for EMV Liability shift
2. Annexure B - Issuer Declaration form
3. Annexure C - Acquirer Compliance form
4. Annexure D - Issuer Response form

<!-- Page 3 -->

Annexure A
Guidelines for handling disputes under EMV Liability Shift
1. EMV liability shift for counterfeit card fraudulent transactions
Acquirer shall be liable under EMV liability shift process, if an EMV chip and PIN based card
is cloned and this counterfeit card is used at ATMs and Micro-ATMs, which lack the
capability of processing transactions on the basis of EMV chip data.
Table indicating Issuer / Acquirer liability is given below:
Card Capability ATM Terminal Capability Liability
Magnetic Stripe only card Non-EMV Chip enabled ATM Issuer
Magnetic Stripe only card EMV Chip enabled ATM lssuer
EMV Chip Card EMV Chip enabled ATM Issuer
Counterfeit magnetic stripe card with track
Non-EMV Chip enabled ATM Acquirer
data copied from an EMV chip card
Counterfeit magnetic stripe card with track
EMV Chip enabled ATM Issuer
data copied from an EMV chip card
These guidelines shall be applicable for domestic ATM Cash withdrawal and Card to Card
fund transfer transactions routed through NFs ATM network including Card & PIN Micro.
ATM transactions.
2. Following fields shall be made available in DMs for transaction search for
raising disputes and adjustments:
a) Field Name -- Service Code
Card capability i.e. whether it is magnetic stripe only card or EMV chip card based on
service code condition. Service code value 2xx and 6xx in Data Element 35 (Track 2
data) in online message denotes that the card is EMV chip card.
b) Field Name - Card data input capability
ATM Terminal capability - Data Element 61 sub field 1 of PoS Data Code having the
card data input capability value shall denote whether the terminal is capable of accepting
EMV chip card (ICC) or not.

<!-- Page 4 -->

Relevant values as per RuPay specifications are given below for reference:
DE 61 subfield - 1
Value Card Data Input Capability (Description)
Unknown
Magnetic Stripe Read capability
ICC capability
Magnetic stripe and ICC capability
Magnetic stripe, contact ICC & Contactless capability
c) Field Name - PAN Entry mode
Transaction - First 2 digit of Pos Entry shall denote the PAN entry mode. It denotes the way
or manner in which the transaction has been processed.
Relevant values as per RuPay specifications are given below for reference:
DE 22 - first 2 digits
Digit 1 & 2 PAN Entry mode (Description)
00 PAN entry mode unknown
02 Magnetic Stripe Read
05 ICC
80 Fall back Transactions
90 Full and unaltered magnetic stripe read (enables CVD validation)
95 Chip card with unreliable CVD or iCVD
Note: The above mentioned 3 fields are added in the adjustment report.
3. Fall back transactions and Liability shift for Fall back transactions
a. Fall back transactions:
When a Chip Card is presented at a Chip terminal, the transaction should be
completed as a Chip Card transaction. If the transaction cannot be completed in this
manner, the transaction shall "fall back" to a magnetic stripe transaction and must be
submitted to the lssuer for authorization.
The Chip Card transaction may not be completed in the event that the Chip Card and
the Terminal fail to reach completion of the transaction due to technical problem.

<!-- Page 5 -->

Fall back transactions will be processed as per the below mentioned requirements:
The Acquirer and the ATM terminal is EMV chip complaint and the ATM is
enabled for accepting and processing EMV chip cards.
If the transaction cannot be completed as a Chip Card Transaction, a "fall
back' to magnetic stripe transaction is allowed.
Fall back transactions must be indicated in the financial request transaction
by sending DE 22 (POS Entry Mode) to ‘80X'.
b. Liability shift for Fall back transactions
Issuers Liability - Transactions accepted as Fall back transactions are the liability of
the Issuer if both of the following conditions apply
i. Card is an EMV Compliant Chip card.
i. Transaction is authorized by the Issuer and the appropriate values
identifying the transaction as a Fall back transaction are included within
the related Authorization Message by the Acquirer.
Note: Issuer may decide to approve or decline Fall back transactions as per their
internal policy and risk mitigation process.
Acquirers Liability - Transactions accepted as Fall back transactions are the liability
of the Acquirer if both of the following conditions apply
i. Card is an EMV Compliant Chip card.
i. Transaction is authorized by the Issuer and the appropriate values
identifying the transaction as a Fall back Transaction or any of the other
data elements required as per the RuPay EMV specification to identify it
the related Authorization Message by the Acquirer.
Acquirers should ensure that the process of Terminal wise (ATM / Micro-ATM)
monitoring of Fall back transactions for taking immediate corrective action is
implemented at the earliest.
shift
AsIssuer
a. A separate reason code 'Counterfeit EMV Card Fraud' is made available in NFS
DMs for raising chargeback.

<!-- Page 6 -->

No representment rights shall be available for chargeback under this reason code.
Acquirer can file compliance with NPC! if the guidelines contained herein is not
complied by the Issuer.
b.  EMV liability shift shall be applicable for transactions from 1st January 2019 onwards,
thus lssuer should not raise chargeback under this reason code for transaction dated
prior to 1st January 2019.
c. Issuer should block/hotlist the card before raising the chargeback and confirm while
raising chargeback.
d.  Issuer should report the counterfeit card fraud to risk management team of NPCl
(email id - fraudrisk@npci.org.in ) as per the specified process before raising the
chargeback.
e. Issuer to confirm that the transaction is not done by the card holder and the card was
with the cardholder at the time of the transaction, which is now disputed as fraudulent
transaction. Issuer shouid confirm that it is a fraudulent transaction suspected to be
done by using counterfeit / skimmed card in form of an Issuer Declaration as per the
format given in Annexure B.
Submission of Issuer Declaration form for chargebacks raised under this
reason code is mandatory. Copy of email sent to fraudrisk@npci.org.in may be
submitted along with lssuer Declaration form for reference.
g. Issuer may submit customer dispute letter / email along with Issuer Declaration, if
available.
h. Issuer should raise chargeback through chargeback menu option given in DMs front
end and not through Bulk upload option, as Issuer Declaration form is to be
submitted mandatorily for this reason code.
 Issuer shall not be able to raise chargeback under reason code - 'Counterfeit EMV
Card Fraud' if already a chargeback has been raised for the transaction under any
other reason code.
 Issuer shall be allowed to raise chargeback under new fraud reason code oniy if the
Service code value is 2xx or 6xx (i.e. card was EMV chip card) and PoS entry mode
is other than 05 and 95 (i.e. transaction was not processed as EMV transaction).
k. Customer compensation of Rs.100 per day of delay for ATM disputes will not be
applicable for these cases.
Please note:
lssuer should do proper due diligence and should be satisfied that the fraudulent
transaction was done using counterfeit card and the card was with the cardholder at
the time of the disputed transaction.

<!-- Page 7 -->

Chargebacks should not be raised routinely under this reason code except for
fraudulent transaction reported by the cardholder and which satisfies the guidelines
contained herein.
AsAcquirer
a. Acquirer shall not be able to raise representment for the chargebacks raised under
reason code - 'Counterfeit EMV Card Fraud.
chargeback is raised incorrectly i.e. not as per the guidelines contained herein.
back transactions, chargeback raised for transaction dated prior to 1st January 2019,
etc.
Acquirer should give proper explanation justifying the reason of raising
Compliance.
Transaction details contained in online message / DMs will be considered while
reviewing the case.
Acquirer may submit detailed transaction switch log which has additional details,
if required and/or any other document in support of their claim.
c. Acquirer should raise Compliance with NPCI by submitting the scanned copy of duly
filled Acquirer Compliance Form given in Annexure c by sending an email to
nfsops@npci.org.in & nfsdms@npci.org.in
Compliancehandling process
a. Compliance raised by Acquirer shall be shared with Issuer. Issuer can submit their
response in the Issuer Response form as per the format given in Annexure D within
7 days from the date of intimation.
b. NPCl may seek further information / clarification from members.
C. NPCl shall give decision based on the dispute raised, online transaction, documents
submitted by members, etc. Decision of NPCl shall be final and binding on members.
etc. shall be debited to Issuer and credited to Acquirer through RTGs settlement.
e. Processing fee of Rs.500/- plus GsT shall be applicable for raising compliance. It
shall be debited to the member against whom the decision is given.

<!-- Page 8 -->

iglaTieno.hocruemtnooonaynsolbeDoupa
otMaensonbneedsaxennA rinvigamo7soncigrooeibpsAboln

<!-- Page 9 -->

NPCI
Registered office - 1001A, B wing 10th Floor, The Capital, BKC, Bandra (East), Mumbai - 400 051.
Annexure B
ISSUER DECLARATION FORM
(For chargebacks raised - EMV liability shift guidelines)
Bank Details: Date:.
Bank Name
Branch Address
(where Cardholder holds
account)
Contact Details (officials whom NPCl or Acquirer can contact for clarification):
No. Name & Designation: Department  Telephone Mobile E-mail ID:
Transaction details:
Card number Type of Transaction ATM ID ATM Location RRN
(Cash WDL or C2C )
Transaction Transaction Transaction Response
Date Time Amount Disputed Amount code
Cardholder Dispute Details:
Sr. Particulars Declaration by Issuer
No.
Whether the complaint was raised at the
Branch / call center / through email /
through Internet or mobile app, etc.
( Please specify )
Date of receiving complaint
(dd-mmm-yyyy)
Chargeback Date
(dd-mmm-yyyy)
Page 1 of 2

<!-- Page 10 -->

NPC
AHIRT
Registered 0ffice - 1001A, B wing 10th Flo0r, The Capital, BKC, Bandra (East), Mumbai - 400 051.
Sr. Particulars Declaration by Issuer
No.
Date & time of Hot listing the card
(dd-mmm-yyyy)
Date of reporting done to NPCI's Risk
Management Team i.e. email sent to Email from (email id):
fraudrisk@npci.org.in
Date:
Copy of email attached (Y / N )
Copy attached:
What type of Account does the card
pertain to?
a)SB/ CA/ OD/ CC (e
(please specify)
b) Staff/ Customer b)
(please specify)
c)Account opening date c)
We hereby confirm that we have done proper due diligence of the complaint received and are
satisfied that the fraudulent transaction is suspected to be done by using counterfeit card. The
transaction was not done by the cardholder and the card was with the cardholder at the time of
transaction, which is now disputed as fraudulent transaction. We also confirm that the dispute is
guidelines.
We hereby declare that to the best of our knowledge and belief, the information furnished herein
and in the statements/ annexures enclosed herewith are true, correct and complete. We further
confirm that we shall readily submit any further information that may be called for by NPCl so as to
settle this case.
Date: Signature & Bank Seal:
Place: Name:
Designation & Department:
Page 2 of 2

<!-- Page 11 -->

NPCI
Registered Office - 1001A, B wing 1oth Floor, The Capital, BKC, Bandra (East), Mumbai - 400 051.
Annexure C
AcquirerCompliance Form
(for Chargeback received under EMV liability shift guidelines)
Bank Details: Date:
Bank Name
Contact Details (officials whom NPCI or Issuer can contact for clarification):
No. ↓ Name & Designation: Telephone Mobile E-mail ID:
Transaction details:
Transaction
Card No. Transaction
type ATM ID RRN
ID
(Cash WDL / C2C)
Beneficiary Details Transaction Transaction Chargeback Transaction
(onlyforCardto Card fundtransfer
transactions) Date Time date amount
ATM Details:
Whether ATM is
What is the Whether the
ENABLEDfor processing
ATM make ATM is Onsite / ATM Location
EMV Chip & PiN card
Offsite
transactions
Documents / cCTV / Images submitted: (Please mentioned YES or. NO in the relevant box for each item)
ATM Internal CCTV/ Any Other Document
EJ / JP Switch log
Camera footage External footage (Please specify)
Note: All documents submitted by the Acquirer should be stamped and signed by Bank official
Page 1 of 2

<!-- Page 12 -->

RUPayMFSASS#NFSCTSANPSNACH
Registered Office - 1001A, B wing 10th Floor, The Capital, BKC, Bandra (East), Mumbai - 400 051.
Acguirer's explanation for raising Compliance:
We hereby declare that to the best of our knowledge and belief, the information furnished herein
and in the statements/ annexures enclosed are true, correct and complete. We confirrm that the
copy of EJ/p and Switch report/logs are true copies of the records automatically generated and
stored in the system. We further confirm that we shall readily submit any further information that
may be called for by NPCl so as to settle this case.
Date: Signature & Bank Seal:
Place: Name:
Designation & Department:
Page 2 of 2

<!-- Page 13 -->

Registered Office - 1001A, B wing 1oth Floor, The Capital, BKC, Bandra (East), Mumbai - 400 051.
Annexure D
Issuer Response Form
(for Compliance raised by Acquirer under EMV liability shift guidelines)
Bank Details: Date:
Bank Name
Contact Details (officials whom NPCl or Issuer can contact for clarification):
No. Name & Designation: Department Telephone Mobile E-mail ID:
Transaction details:
Transaction
Card No. type ATM ID ATM Location RRN
(Cash WDL / C2C)
Beneficiary Details Transaction Transaction Chargeback Transaction
(onlyfor Card toCard fund transfer
transactions) Date Time Date Amount
Dispute Details:
Date and time of WhetherIssuerDeclaration Date & Time of Hot Date of reporting to
lodging complaint with Form was properly filled listing the card fraudrisk@npci.org.in
Bank and submitted while raising (please attach copy of
chargeback email)
List of additional documents submitted, if any
1)
2)
3)
Note: All documents submitted by the Acquirer should be stamped and signed by Bank official
Page 1 of 2

<!-- Page 14 -->

RUPayMP XSS NFSI CTSP NACH
Registered Office - 1001A, B wing 10th Floor, The Capital, BKC, Bandra (East), Mumbai - 400 051.
Issuer's Response on Compliance raised by Acguirer (submit complete details with proper
explanationl:
We hereby declare that to the best of our knowledge and belief, the information furnished herein
and in the statements/ annexures enclosed are true, correct and complete. We confirm that the
copy of Switch report/logs are true copies of the records automatically generated and stored in the
system. We further confirm that we shall readily submit any further inforrmation that rnay be called
for by NPCl so as to settle this case.
Date: Signature & Bank Seal:
Place: Name:
Designation & Department:
Page 2 of 2
