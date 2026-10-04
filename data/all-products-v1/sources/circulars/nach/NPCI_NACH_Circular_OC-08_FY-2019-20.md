# Circular no.08 - Pradhan Mantri Shram Yogi Maan dhan (PMSYM)

Circular/reference number: NPCI/2019-20/NACH/CircularNo.008

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2019-20/NACH/CircularNo.008 May 31,2019
To
AllNACHMemberbanks
PradhanMantriShram YogiMaan-dhan(PMSYM)
Government of India has launched a contributory pension scheme for workers of unorganised
sector namely Pradhan Mantri Shram Yogi Maan-dhan (PMSYM) to provide old age
protection. For enrolment under the scheme, an eligible subscriber can approach the nearest
Common ServiceCentre(CsC)withthe documents viz.Aadhaarnumber, bank passbook,
etc.Upon completion of enrolment process an auto debitmandateform will begenerated and
will besigned/underhis/herthumb impression.
The contributions of the pensioner will be collected by sponsor bank through debit of the
subscribers bank account registered for this scheme through NACH system. As this scheme
is meant forworkers ofunorganized sectorand constitutes an important milestone in providing
them with social security, it has been decided to push only the mandate data without the
images in the existing file format, this is to avoid any undue rejection on account of signature
mismatch or due to usage of thumb impression in the mandate form by the worker.
Sponsorbank
MMS createlamend / cancel file format will be as per the existing format however there will
be change in naming convention, both the file format and the new file naming convention
isprovided inAnnexureIforreference.
Category code to be captured as “Woo1" (PMSYM - Mandate without images) in create
XML.
The sponsor or destination bank will not be allowed to create/amend/cancel mandate
through GUl and said operation can be done through xml only.
To ensure system readiness to consume, Unique Mandate reference (UMR) number
generated with identifier in fifth digit as "5".
As the image of the mandate will not be transmitted to the destination bank the sponsor
bank along with Life Insurance Corporation of India (LiC) and the Ministry of Labour &
Employment will work out a mechanism for retrieval of images in case of disputes,
mechanism for dispute registration and redressal etc. Document with detailed roles and
responsibilities of all the stakehoiders will be circulated to member banks in due course.
1001A,TheCapital,BWing,10hFloor
BandraKurlaComplex,Bandra(E),Mumbai400051.
T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Destination bank
Identification of the mandate for processing through following options:
a. Unique Mandate reference (UMR) number will be generated with identifier in 5th
digit as"5"
b. Category codewill be"Woo1"inthe inwardmandateXML
Sequence number ofthe mandate inward file namewill be prefixedwith“LVMW".
To validate the customer account provided in mandate XML with CBS (mandate images
will not be available) and upload the acceptance file into NPCI MMS.
There is no change in the XML file format however there is a change in the file naming
convention of inward file, both the file format and the naming convention is provided in
Annexurell forreference.
Destination bank should use the relevant reasons as provided in Annexure lll when
accepting / rejecting the mandate.
The Ministry of Labour & Employment has confirmed that the process has been approved by
all the competent authorities including DFS and IBA. Detailed mandate registration process is
provided in AnnexureIV.
As an exception for the process related to this scheme, NPCl will not be charging the mandate
processing fee of Rs. 1/-from the sponsor bank and Rs. 0.50 from the destination bank. Also
as the destination banks will be only validating the account numberthe incentive of Rs.5/-paid
forothercategory ofmandateswillnot be applicable for data mandates presented underthis
scheme.The destination banks will be paid the inter change of Rs.0.50 per debit transaction.
The destination banks shall automate the process of account validation and mandate
registration and ensure that response is provided within 2 working days of receiving the
mandatesthroughNACHsystem.
The member banks registering the mandates on the basis of data alone will be responsible
only for registering the mandates with the correct account number as is provided in the data
mandate and processing the transactions on the basis of registered mandates with due
validation. Other Disputes pertaining to mandate initiation, scheme administration etc will be
handled by the Ministryof Labour&Employment &Life Insurance Corporation of India.
Above changes are to be implemented with effect from June 07,2019.Member banks are
advised to make necessary system for processing thePM-sYMfiles. The volume of
mandates and transactions are expected to be on higher side all the banks are advised to do
capacity planning for processing large volume within the available time window.
1001A,TheCapital,BWing,10hFloor,
BandraKurlaComplex,Bandra(E),Mumbai4ooo51.
T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Anyqueries maypleaseberaisedthroughCRM tracker.
Withwarmregards,
Giridhar G.M
(Chief-Offlineproductoperations&runtechnology)
1001A,TheCapital,BWing,10thFloor,
BandraKurlaComplex,Bandra(E),Mumbai400O51.
CIN:U74990MH2008NPL189067

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-1
File nameconventions forMMS filename conventions as Sponsor bank:
Create(Changehighlightedinbold)
a. XMLfilenameconventions:
MMS-CREATE-Bank code-User id-ddmmyyyy-MWIxxxxxx-INP.xml
b. Zip name conventions:
MMS-CREATE- Bank code-User id-ddmmyyy-MWIxxxxxx-INP.zip
Amend
NoChange
Cancel
No Change
Mandate file format:
NoChange
1001A,TheCapital,BWing,10thFloor
BandraKurlaComplex,Bandra(E),Mumbai4oOO51.
T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 5 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-ll
File name conventionsfor MMs inward andAcceptfor destination bank:
Inward:(Changehighlightedinbold)
a.XMLfilenameconvention
MMS-CREATE-Bank code-User id-ddmmyyyy-MWIxxxxxx-INP.xml
b.Zipfilenameconvention
MMS-CREATE-bank code-ddmmyyyy-LVMWIxxxxxx-INW.zip
Amend
No Change
Cancel
No Change
Mandatefileformat:
No Change
1001A,TheCapital,BWing,10hFloor
BandraKurlaComplex,Bandra(E),Mumbai400051.
T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 6 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-IIl
SI.No. Code Name Type
ac01 ACKDefaultAcceptReason ACKAcceptReason
sack Automaticcancelrequestacceptance ACKAcceptReason
M036 NotaCBSactno.oroldactno.representwithCBSno AmendmentReason
A001 Oncustomerrequest AmendmentReason
C003 Accountclosed Cancel Reason
C004 Accountfrozen Cancel Reason
C005 Account inoperative Cancel Reason
C002 Cancellation oncorporaterequest Cancel Reason
C001 Cancellationoncustomerreguest Cancel Reason
10 M057 AccountHolderNameMismatchwithCBs NACKAcceptReason
11 M055 Account Inoperative NACKAcceptReason
12 M041 Accountblocked NACKAcceptReason
13 M037 Account closed NACKAcceptReason
14 M026 Accountfrozen NACKAcceptReason
15 M034 Amountof EMl morethan limit allowedfortheacct NACKAcceptReason
16 M035 Corporatenamemismatch NACKAcceptReason
17 M021 Duplicate mandate_first presented mandatealready NACKAcceptReason
18 M060 Invalidfrequency NACKAcceptReason
19 M056 Mandate Not Registered not maintaining reqbalanc NACKAcceptReason
20 M052 MandateNot Registered MinorAccount NACKAcceptReason
21 M051 MandateNotRegistered_NREAccount NACKAcceptReason
22 M030 MandateregistrationnotallowedforCCaccount NACKAcceptReason
M053 MandateregistrationnotallowedforPFaccount NACKAcceptReason
24 M054 MandateregistrationnotallowedforPPFaccount NACKAcceptReason
25 M038 Nosuchaccount NACKAcceptReason
26 M031 NotaCBSactno.oroldactno.representwithCBSno NACKAcceptReason
M011 Payment stopped byattachmentorder NACKAcceptReason
28 M012 Paymentstoppedbycourtorder NACKAcceptReason
M023 RefertothebranchKYCnotcompleted NACKAcceptReason
M032 Rejected aspercustomerconfirmation NACKAccept Reason
31 ncex TATexpired NACKAcceptReason
32 M013 Withdrawal stopped owing to death of account holde NACKAcceptReason
33 M015 Withdrawal stoppedowingto insolvency of account NACKAcceptReason
34 M014 Withdrawal stopped owing to lunacyofaccounthold NACKAcceptReason
1001A,TheCapital,BWing.10hFloor,
BandraKurlaComplex,Bandra(E),Mumbai4o0051.
T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 7 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
AnnexureIV
EnrolmentProcess:
1.Eligible subscriber will visit the nearest Common Service Centre and complete an on-
line registrationprocessbysharing his Aadhaar number, bank particulars and other
details of nominee and spouse.
2.Demographic authenticationbaseduponAadhaarnumber,OTPbasedmobilenumber
verification, manual verification ofbank particulars from supporting documents would
be done at CSC.
3. Upon completion of enrolment process and payment of initial contribution, an
enrolment cum auto debit mandateform is generated and signed by the subscriber.
4. CsC decentralised office would scan the signed enrolment cum auto debit mandate
form and upload the same to CsC system.
5. Subsequent to this a pension card would be generated and given to subscriber along
6.TheCSC centre would also return the original enrolment cum auto debit mandate form
to the subscriberto be retained byhim.
7.The data of subscribers enrolled and the amount collected from subscriber would be
transferredbyCSCtoLiConT+1forfurtherprocess.
Mandate registration process:
The pre-requisite of auto debit every month from an account is registration of mandate duly
verified by the destination banks.As the subscribers for this scheme is from unorganized
sector, (a few may be literate but may not be able to sign consistently and others may be
illiterate who can provide thumb impression only), the process of registration of mandate is
acting as a deterrent for smooth and seamless implementation of this Social Welfare scheme
Ministry of Labour & Employment, in consultation with IBA, few major banks, LIC and NPCl
designed a process wherein the mandates will be registered based on data without
transmission of physical mandate copy to the destination banks. The proposed process flow
isgivenbelow:
1.Customerwill approach Common Service Center (CsC)forpension scheme
registration.(The CsC is a strategic cornerstone of the National e-Governance Plan
(NeGP), approved by the Government in May 2006, as part of its commitment in the
National Common Minimum Programme to introduce e-governance on a massive
scale.It works under MeitY).
2. Csc will ensure customer related information are validated using customer bank
passbook before completing the registration process.Basic details to be validated are:
a. Customername
b. Customeraccountnumber
C. IFSC/MICRCode
d. Othercustomer information as available inthe passbookwhichis requiredfor
mandateregistration.
3.The onus of recording the correct details of the customer and validation of customer
will be on CsC. If there are any dispute at a later date by the customer on the debits
to his/her account, the onus of resolving the dispute to the satisfaction of the customer
is entirely on LIC.
1001A,TheCapital,BWing,10thFloor
BandraKurlaComplex,Bandra(E),Mumbai4ooO51.
T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 8 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
4. Post successful registration, CsC/LIC to prepare data mandate as per the format
provided by NPCI (to be shared).
5. The data mandate to be shared with sponsor bank.
6. Sponsor bank on receiving the data to upload into NPCl portal.
NPclwill generateinward torespectivecustomerbanksforprocessingthemandates.
8.  Customer banks will validate the account number only and accept if it is valid (name
validation will not be carried out by the bank).
9.If the account number is correct, the bank will register the mandate. If the account
number is incorrect, frozen, blocked or cannot be debited for any other reason, the
bank will reject the mandate with appropriate reason as per the reasons list provided
byNPCI.
10.NPClonreceivingtheaccept/rejectreasonfromcustomerbankwill generateresponse
back to the sponsor bank of LIC.
11.LiCshouldsharetheresponsedatawithCsC.
12. LIC will ensure that the transactions are generated only on the mandates that are
confirmed by banks as valid. In case LiC generates a transaction on a mandate that
has been rejected bythebank,such transactionswill berejected byNACH systemat
the time of upload itself.It is theresponsibility of LiC to ensurethat the response files
received from the customer's bank are updated in their database and originate
transactions on valid mandates only.
13. At the time of transaction presentation by sponsor bank, NPCl will validate transaction
data against the mandate data based on the Unique Mandate Reference Number
also validate the transaction data against the mandate data registered in their internal
systems before allowing debit to the customer account.
14. In the event of any dispute on the validity of the mandate or debit to an account, it will
be the responsibility of LiC and the Government to handle the dispute and settle with
thecustomeraccordingly.
15.NPCl will provide the disputemanagement system to the banks concerned for raising
disputesthroughthe system.NPCIwillfollowupwith sponsorbank,LiC for settlement
of disputes as per the defined TAT. If the dispute is not settled within the agreed TAT,
the sponsorbanks account willbedebitedto the extent ofdisputedtransactionamount
and credited to the dispute raising bank for crediting to the customer account (this is
as perthe disputemanagement processed detailed in NACH procedural guidelines).
1001A,TheCapital,BWing,10thFloor
BandraKurlaComplex,Bandra(E),Mumbai4o051.
T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067
