# Circular No 206 - Trade Receivable Discounting System TReDS

Circular/reference number: NPCI/2016-17/NACH/CircularNo.206

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2016-17/NACH/CircularNo.206 December21,2016
To
AllNACHmemberbanks
TReDS-TradeReceivableDiscounting System
Trade Receivables Discounting System is a system used to secure finances for micro, small
and medium enterprises. MSMEs sellers, corporate buyers, financiers which include banks
and non-banks will be direct participants in this. TReDs thus serves as a platform to bring
the stakeholders and participants together for discounting, trading and settlement of the
invoices.It has been set up under the regulatory framework set up by RBl under Payment
and Settlement Systems Act 2007.
RBI has authorized NPCI for undertaking the settlement of TReDS.TReDS utility in NACH
caters to many to many transactions wherein the debit and credit legs of the
transactions are tightly coupled with each other .i.e. the initiation of credit
transactions will be dependent on the success of debit transactions linked to them
and the failed transactions will be reversed through the subsequent credit session.
The system will be implemented in a phased manner.
Phasel
Existing NACH system will be used for processing the TReDS transactions.
File format
Transactionfiles
Theformat will be same as current 3o6 file format however TRE"a product
identifier is introduced to differentiate between ACH files & TReDs files.This
new product identifier will be prefixed with the sequence number during the
generation of inward file, which helps destination bank in identifying the
inwards.
Mandates
Existing pain format will be used however new mandate category i.e.“Too2" is
introduced to differentiate between the mandate variants. As per RBl
guideline, the cap amount for this category is set as Rs. 1 Crore.
1001A,The Capital, B Wing,10th Floor.Bandra Kurla Complex,Bandra (E).Mumbai 400051.T:+9122 40009100 F:+912240009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
File processing flow H p h pa
NATIONALPAYMENTSCORPORATIONOFINDIA
Input files will be uploaded by the bank through Host-to-Host.
System generates an acknowledgement file for the file submitted into ACH
system.
System generates inward file to destination bank for the transactions settled
during the presentation session.
Destination Bank user needs to submit the return file for the inward
transactions.Once the file is uploaded, the authorizing or returning will be
through front end screen. The file will need to be approved by the
destination bank checker user.
System generates an acknowledgement file for the return file uploaded into
NACH
 System generates final output file (response file) to the Sponsor Bank for
the Input file submitted.
Sessions
TReDS sessionwill be in similar lineswiththeNACH sessions whereinthe input files
can be uploaded up to 7 days in advance with product type as “TRE" so that the
given below
St. No. TReDSSession Presentation Return
Debit 07:00AMto 08:00 AM 09:00 AM to 11:00AM
Credit1 01:00 PMto02:00PM 02:30PMto03:30PM
Implementation timeline
Member banks todisseminatetheinformationto allthe concerneddepartments to
implementPhase-lfromJanuary02,201?
1001A,The Capital, BWing,10th Floor,Bandra Kurla Complex,Bandra (E),Mumbai 400051.T:+9122 40009100 F:+9122 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
Phase Il
NATIONALPAYMENTSCORPORATIONOFINDIA
A TReDS utility will be plugged into NACH. TReDS utility facilitates uploading a
singlepresentation filewithmultiple debits and multiplecredits in advanceto the
settlement date in NACH application i.e. the only change in phase Il is the way
sponsor bank initiates the TReDS files, a new file format is introduced for sponsor
banks only. The new input file format is enclosed in Annexure I for reference.
Mandate processing & file processing at destination bank end remains the same as
in Phase I.
Sessiontiming
Sl. No. TReDSSession Presentation Return
Debit 07:00AMto08:00AM 09:00 AM to 11:00 AM
Credit1 12:00noonto12:30PM 01:30PMto02:30PM
Credit2 03:30PMto04:00PM 04:30PMto05:00PM
Implementation timeline
NPCl will issue separate communication on the Phase Il implementation timeline.
Roles & responsibilities of Sponsor Bank
Registration of TReDS mandates in NACH
In case of mandates rejection, resubmission of the TReDS mandate to NACH
Files to be uploaded in the prescribed format specified by NPCl
Sufficient funds to be maintained in the RTGS account
Reconciliation of TReDS settlement account maintained with Sponsor Bank
Sharing the final response file to TReDS entities
Roles & responsibilities of Destination Bank
To upload response for the mandates within the TAT
No one day extension will be granted by NPCl on the TReDS files, hence
banks must ensure proper systems are in place for processing & uploading
the return / response within the session timeline.
1001A,The Capital,BWing,10th Floor, Bandra Kurta Complex,Bandra (E),Mumbai 400051.T:+912240009100 F:+912240009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 4 -->

NPCI
Important:
NATIONALPAYMENTSCORPORATIONOFINDIA
In TReDsprocess flowall thedebit transactions thathavenotbeen responded to
by the destination banks will be treated as deemed returned and the system will
reverse the settlement done in presentation session.The settlement entries will
be as follows
Presentation session
Debit sponsor bank
Credit destination bank
Returns session/deemedreturnedcases
Debitdestinationbank
Credit sponsor bank
Memberbanks shouldtakenoteoftheaboveprocessputinplaceprocessfordaily
specifically in case of deemed returned transactions.
For any clarifications pleasewriteback toach@npci.org.in
With warm regards,
(Giridhar G M)
VP&Head-NACH&CTSOperations
1001A,TheCapital,BWing,10thFloor,Bandra Kurla Complex,Bandra (E),Mumbai 400051.T:+912240009100 F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 5 -->

Annexure!
Sponsor Bank file format
Sr. Len Field
Field Description Mandatory Remarks
No gth Type
(Header) Credit Contra Record
ACH transaction code NUM Mandatory TR
ALP
Control Optional Spaces
NUM
ALP
User Name 40 Mandatory Alpha Numeric description
NUM
ALP
Control 14 Optional Spaces
NUM
ACH File Number NUM Optional User defined input tape
ALP
Control 11 Optional Spaces
NUM
ALP Total Debit Amount in
Total Debit Amount 13 Optional
NUM Paise
ALP Aipha numeric LedgerFolio
Ledger Folio Number Optional
NUM particulars
User defined limit which
User Defined limitfor would be taken for
13 NUM Optional
individual items validating the credit/ debit
items, in paise
Amount Credit Amountin
10 Total Credit Amount 13 NUM Mandatory
paise
Settlement Date Date on which settlement
11 NUM Mandatory
(DDMMYYYY) is sought to be effected
Reserved (kept blank by ACH File sequence number
12 10 NUM Optional
user) to be allotted by NPCI
Reserved (kept blank by Checksum Total generated
13 10 NUM Optional
user) by NPCI
ALP
14 Filler Optional Spaces
NUM

<!-- Page 6 -->

User number allotted by
ALP
15 UserNumber 18 Mandatory NPCl at the time of
NUM
Registration
User defined reference
ALP numberforthe entire
16 User Reference 18 Mandatory
NUM transaction (Alpha
Numeric)
Sponsor Bank IFSC/ ALP SponsorBankIFSC/MICR/
17 11 Mandatory
MICR / IIN NUM IIN code
Acct.number of the User
to be debited/credited by
Sponsor Bank (Alpha
User's Bank Account ALP
18 35 Optional numeric)
Number NUM
(debited in the case of ACH
Credit & credited in the
case of ACH Debit)
Total credit and debit items
19 Total items NUM Mandatory
in file
Inthepresentation session
for input file, the
settlement cyclefield will
be blank. After processing
Settlement Cycle (Kept
20 NUM Optional when the file is sent to the
blank by User)
destination bank,
settlement cycle field will
have system generated
value in file header.
ALP
21 Filler 57 Optional Spaces
NUM
Total 306
Credit Records
Record Identifier NUM Mandatory 11 for CR, 12 for DR
Control ALP Optional Spaces

<!-- Page 7 -->

NUM
As provided by Bank -
Destination Account Needs to be as per
NUM Optional
Type NECS(10/11/12/13/29/30/
31) or blank.
ALP Alpha numeric Ledger Folio
Ledger Folio Number Optional
NUM particulars
ACHitemSequence
Reserved (Reversal ACH
10 NUM Optional Number generated by NPCI
item Seq No)
in RES
Flag for items credited /
debited (1), returned
Reserved (Reversal
NUM Optional uncredited / undebited (0),
Transaction Status)
recalled (5), rejected(2),
Partial Debit(6)
Reserved (Reversal Reversaltransaction
NUM Optional
Reason Code) reason code
AlP
Control Optional Should be spaces
NUM
BeneficiaryAccount ALP Mandatory for ACH-
40 Alpha numeric description
Holder's Name NUM CR and ACH-DR
Group reference should be
Transaction group ALP
10 16 Mandatory same for a set od credit
reference NUM
and debit transactions
ALP Alpha numericdescription;
11 UserName/Narration 20 Optional
NUM Will be used as Narration
12 Reversal Credit Amount 13 NUM Optional Amountinpaise
13 Amount 13 NUM Mandatory Amount in paise
Reserved(ACH item
14 10 NUM Optional To be Blank
Seq No.)
15 Reserved (Checksum) 10 NUM Optional To be Blank
Reserved (Flag for
16 NUM Optional To be Blank
success /return)
17 Reserved(Reason NUM Optional Tobe Blank

<!-- Page 8 -->

Code)
DestinationBankIFSC/ ALP Mandatory for ACH-
18 11 DestnBankIFSC/MICR/IN
MICR/IIN NUM CRand ACH-DR
Beneficiary's Bank ALP Mandatory for ACH- Beneficiary Bank Account
19 35
Account number NUM CRand ACH-DR Number
Sponsor Bank IFSC/ ALP
20 11 Mandatory SpnsrBankIFSC/MICR/IIN
MICR/IIN NUM
ALP User number allotted by
21 UserNumber 18 Mandatory
NUM NPCI
Type to identify
ALP financier(FIN)/seller(SEL)/b
22 EntityType Mandatory
NUM uyer(BUY)/TReDS
charges(TRE)
Userdefined Reference
Number such as Ledger
Folio number, or Share/
Debenture Cert. No. or Job
ALP
23 Transaction Reference 27 Mandatory Card No. or any other
NUM
unique identification
number given by the User
for the individual
beneficiaries
It is a 3 digit alpha numeric
which is mapped to
ALP product (eg: APBS
24 Product Type Mandatory
NUM Schemes),List of product
types will be provided by
NPCI.
Used in APBS file for
Beneficiary Aadhaar
25 15 NUM Optional Aadhaar number.To be
Number
spaces
ALP MandatoryforDebit
26 UMRN 20 Optional
NUM transactions
27 Control ALP Optional Tobe Blank

<!-- Page 9 -->

NUM
Total 306
