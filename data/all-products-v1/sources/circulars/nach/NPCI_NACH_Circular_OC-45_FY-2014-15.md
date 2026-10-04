# Circular No 45 - Update on NACH Debit - Mandate Mandagement System (MMS)

Circular/reference number: NPCI/NACH/2014-15/Circular45

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NACH/2014-15/Circular45 April25,2014
To,
AllMemberBanksofNACHSystem
Madam/DearSir,
NACHDebit-MandateManagement System (MMS)
NACHDebit-MandateManagementSystem(MMS)waslaunchedin2013,andsincethen,NPC
has taken many initiatives to facilitate banks towards offering this service to its customers.
Some of these initiatives include Centralised Mandate Validation Service (Circutar 16), Waiver of
MandateProcessing charges (Circular35)and RevisionofMandateform layout.
2. The Centralised Mandate Validation service was launched on October 7,2013.The
service ensures that only'good to debit'transactions are sent to the bank by NPCl, for debit
processing after validating parameters like the customer account number,bank IFsc/MiCR,
amount, start date/end date of the underlying active mandate.
3. To increase the acceptance of NACH mandates, NPCl decided to waive the Mandate
processing servicecharge to thebanksfrom January1,2014toDecember 31,2015.
4. Taking benefit of the above mentioned services, over 7o banks have started to offer
this service to their customers and more than 2,oo,o00 mandates have been registered on the
NACHplatformalready.
To provide you further insights into theproduct,we have created an elaborate FAQ on
MMS whichis attached along withthe circularforyourreadyreference.
C-9,8thFloor mqr/Phone:02226573150
RBIPremises q/Fax:02226571001
Bandra-Kurla Complex -/email:contact@npci.org.in
Bandra East aawse/Website:www.npci.org.in.
-400051 Mumbai 400051 CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
6. We urge all banks to start participating on the NACH debit platform by offering the
service to its customers. We look forward to your continued support to make NACH system a
success.Forany queries/furtherhelp,please email us at ach@npci.org.in
Warm Regards,
RajeethPillai
VP and Head NACH
C-9,8thFloor x39T/Phone:02226573150
RBIPremises a/Fax:02226571001
Bandra-Kurla Complex -/email:contact@npci.org.in
Bandra East /Website:www.npci.org.in
-400051 Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

FAQ-MMSandNACHDebit
Contents
I.OVERVIEWOFNACHDebit.
1. What is NACH?
2.What is NACH-DR?.
3.Whatarethebenefitsof NACH-DRto Banks?
Il.MandateForm..
4.Whicharethevarious fields tobecaptured onthe Mandateform?
5.WhicharetheMandatoryfieldstobecaptured onthe Mandateform?
ill.MandateManagementSystem(MMS)
6.What isMandateManagementSystem?
7.Whatarethedifferentmethods forcreationofa Mandate?.
8.Whyaretheretwo options for creating a mandate?
9.WhatarethefileformatstobeusedforMandateCreation/Amendment/Cancellation?
10o.Howmanymandates can abankupload atatime?
11.Who caninitiateaMandate?
12.What are the steps involved in initiating a mandatethrough Sponsor Bank via Corporates/Service
Provider?
13.What are the steps involved in the Process of customer initiating mandate request through
Destination Bank?
14.When isa UMRNgenerated/assignedtothemandate? 10
15.Can the Destination bankview and approve/reject all inward mandates using theGUi? 10
16.Does the bank need to encrypt the mandate files being uploaded to MMs?Does the bank need to
decrypt the INw mandate received for acceptance? .10
17.Can,banks send multiplemandates Create/Amendment/Cancel zipfilesto NPCIthroughout the
day?. 10
18.Similarly,canbankreceivemultiplemandatesCreate/Amendment/Cancel zipfilesfromNPCl
through the day.Or would the files bebundled at NpCl and what thebank would receive will bea
singleCreate/Amendment/Cancel zipfileforaday? 10
19.Who will beresponsibleformanaging thephysical mandates? 11
2o.What is the time availableto the instructed agent to accept themandate? 11
Page |1

<!-- Page 4 -->

21,What does RejectReason Codemean? 11
22.WhataretheSessionTimingsforMMS? 11
23.Whatall parametersarebeingvalidatedatNPCI'send? 12
IV.QueriesrelatedtoPAINo09 12
24.What isaUserNumber?Cana single corporate havetwoormoreuser numbers? 12
25.DoesNPClvalidatestheUserNumber?. .12
26.What isthelogicfollowedforgenerationofUserNumber? .13
27.Is the User Number unique to the Corporate or is it linked to the Sponsor Bank? .13
28.CanthesameUsernumberbeusedacrossall theproductsorbankshavetoseekdifferentUser
NumberforDifferentProducts? .13
29.Does NPCIvalidatetheUserNumber/User Nameat the time of Mandate Processing? 13
3o.Whatdo you meanby"UtilityCode"? 13
V.QueriesrelatedtoPain010: 13
31.What are the fields that can't beamended? .13
Vl.Queries related to Pain012: .14
32.lstheprocesssimilartotheNACHdebitfilewherebybankscangetanACK,partialACKoraNACK?
14
33.Dobankneedtosendonemandateresponsefile(PAiNO12-MandateAcceptance)foreachfile
theyreceivefromNPCl,orcantheysendone consolidatedPAiNO12 containing detailsofall
acceptance and rejectionsformandateinitiation,updating and cancellation requests?. 14
34.For the 3 separate files thatthe bank receive,can they sendback a single pain012file containing
records whichcould pertainto mandate creation,amendment or cancellation.. 14
35.If thebank receives 5mandates on dayO, can it stagger theapproval/rejection over the next3
days.i.e.approve one mandateon day 1, twomandates on day2and remainingmandateson day3.
.14
VII.QUERIESOFACHDEBIT(ATTRANSACTIONLEVEL)
36.Foreverysingle Inputfile (TransactionFile),doesthedestination bank receiveseparateinward
file? 14
37.WhataretheSessionTimings of NACH-Dr.? 15
Vill.Annexure 1-Description ofMandate fields. 16
IX.ANNEXURE2.Mandateimage 18
Page12

<!-- Page 5 -->

I.OVERVIEWOFNACHDebit
1.What isNACH?
TheNational Payments Corporation of India (NPCl)offerstobanks,financial institutions,Corporates and
Government/s a service termed as"National Automated Clearing House (NACH)"which includes both
Debit and Credit:It shall be referred to as NACH.NACH (Debit) & NACH (Credit)aims at facilitating
interbankhigh volume,lowvaluedebit/credittransactions,whicharerepetitive innature,electronically
usingtheNPCIservice.
2.WhatisNACH-DR?
NACH-DR is the product of NPCl to provide a better & efficient Mandate based debit servicesto the
banks.
Unique features of NACH Dr.
The following are thekeyfeatures of the NACH Debit:
Automated processing and exchange of mandate information electronically with well-defined
timelinesforacknowledgement/confirmation.
Each mandate needs tobeaccepted/authorized bythe debtor bank before the User can initiate
atransaction
Each mandate is uniquely identified by Unique Mandate Reference Number (UMRN)which
makes tracking of multiple mandate details easier for customers.
Defined and agreed SLA's to be implemented-provide Governance model and defined timelines
formandateprocessing.
Enabletheusageof standardized MandateForms.
Mandate repository containing Mandate details to be maintained for the purpose of validating
mandate UMRN available on the NACH transaction files, at the time of NACH transaction
processing.
MMSwouldallowprocessingofdebtorandcreditorinitiatedmandates.
MMs would allow processing of e-mandates as well as paper mandates, where e-mandates
would consist of only data file upload while paper mandates would consist of mandate image
and Data fileuploads.E-mandates canbe initiated onlybya debtorbank.
Bank can leverage on the existing CTS instrument scanning infrastructure for scanning and
maintainingrepositoryofthemandates images.
Page13

<!-- Page 6 -->

3.Whatarethebenefits ofNACH-DRto Banks?
BenefitsofNACH-DRareasfollows:
Standardization and digitization of mandates allowing complete audit trail of the Mandate
lifecycle.
Simplification of themandateacceptanceand recording process
Will resultinreducedoperational costforthebanksand itsclients
Will result in higher revenues for the banks and its clients as the scope of services expand pan
India-beyond the 90 Clearing centres
Unique identifier number allocated to each mandate (UMRN - Unique Mandate Reference
Number)
Secure web access for file upload/download, dissuading the concept of regional Ncc/Clearing
Housesubmissions
Mandates canbeprocessedbythememberforanybranchacrossthecountry
Allows corporateclientstodirectlyuploadfiles forapproval (DCA)
Functions on International Messaging Standard-Iso20022
MinimaltimetakentoactivatetheMandate-samedayprocessingpossible
Corporates get to have direct access to the NACH systems, making it easier for them to get
accesstostatus of transaction/mandate without delay.
Reduction of the uploading workto the sponsor banks,since the file upload will be done by the
corporatesthemselves
Page14

<!-- Page 7 -->

Il.MandateForm
4.Which are the fields to be captured on the Mandate form?
PleasereferAnnexure1
5.Whichare the Mandatoryfields tobe captured on theMandate form?
All fields are mandatory otherthan thefields mentioned below?
FieldNo.13whichisConsumerReferenceNumber,
FieldNo.14whichisScheme/PlanreferenceNumber
FieldNo.20,21&22(Telephone,Mobile&Mail-ID)
FieldNo.19whichis CustomerAdditional ldentification.
Il.MandateManagementSystem(MMS)
6.What is MandateManagementSystem?
Mandate Management System is a service of NACH Debit which facilitates the process of Mandate
Creation, Mandate Amendment, Mandate Cancellation and offers all Mis related to the Mandate.
MandateCreation Creation ofa new mandate infavorof the User Institution.
MandateAmendment-for amendment of any of the variables of an existing Mandate, whichis
Active.UMRN needs to be quoted for Amendment.
MandateCancellation-forcancellationof anActivemandate-UMRNis requiredtobe quoted
7.Whatarethedifferent methodsforcreationofaMandate?
There are two methods for creation of a mandate
a. UI based:The user can log into the NPCl provided MMS utility and initiate a mandate using a
userinterface,
b.File based:The MMS utility also gives the user the facility to upload more than once mandate
throughafileupload method.-Fileformataccepted will beXMLonly
8.Why are theretwooptions for creating a mandate?
The bank can use the Ul option for uploading singular mandates. The Ul allows the bank to create
Mandate and approve it at any point of time during theday (between SoD and EOD),without linkageto
theMRCand MARCcycles.
Page|5

<!-- Page 8 -->

The file based method for creation of a mandate is particularly for supporting the banks automated
process of initiating more than one mandate at a time.
9.What are thefile formats to be used for Mandate Creation/Amendment/Cancellation?
Mandate Creation- Pain009
MandateAmendment- Pain010
MandateCancellation Pain011
ResponseandAcknowledgementforeachoftherequestwill beprovided inPainO12format
Kindly refer section 2.3 of the Bank Specification Document (BSD)to gather more details on the file
formats.
1o.What is the size of the Mandate? Is it mandatory to restrict mandate to the specified size?
The mandate has to be in the size of a standard cheque ie.8"x32/3".
It ismandatoryto restrict the mandatetothe size mentioned above.
1i.What should bethe sizeand formatofthe scanned mandate?
Givenbelowisthe specificationofthescannedmandate.
Front Image
TheImageshouldbeinblack&white.
TheImage shouldbeinTIFFFormat
DPIfortheImage is200
FrontGrayscaleImage
TheImageshould beingrayscale
Theimage should be in JPEGFormat
DpIfor the Image should be 100
The size of a single image should not exceed 100 Kb.
The sample of the scanned copies is in Appendix.2.
1o.Howmanymandates cana bankuploadata time?
Thebank can upload anynumberof mandatesto theMMS system,provideda single imagefiledoesn't
exceed100Kbandasinglezipfilewithmultiple imageanddatafilesdoesn'texceed 10Mb.
Theutilityallows thebanktoupload multiple zipfiles.
Page16

<!-- Page 9 -->

1l.WhocaninitiateaMandate?
The Mandate Creation/Amendment/Cancellation request can beinitiated byboth,the Creditor Bankor
the Debtor Bank.
Inthecase wheretheMandate is initiatedbythe Creditor Bank,a scanned copyof thephysical mandate
along with the data filewill havetobe submitted for Acceptance of the Debtorbank.
In the case where the Mandate is initiated by the Debtor Bank, the scanned copy of the physical
mandatemaynot accompanythedata filewhensubmittedforacceptanceof the Creditor Bank.
12.What are the steps involved in initiating a mandate through Sponsor Bank via Corporates / Service
Provider?
annodmanidate
Midalos sento Dostinationbanicaia imaassentto
Spoosabaak NPCI,WIHOMRN
Corhortes Sponsor Bank NPCI Destinatlon Bank
Mandate
updatecorporates Destination tek
mardatedetalb B
updatas rocprds
AtSpomortanktinkoffics
UnnNeeneratios
npci'spurview
Step1
TheCorporates/Service Providers that holdsan account with Sponsor Bank send an application to the
sponsor Bank forgetting Utility Code, whichwould allowthem toparticipate in the NACHprocess.
Step 2
Acustomerwho has purchasedorsubscribedthe servicefrom corporate/serviceprovideranddesiresto
pay through a mandate arrangement would fill up NACH mandate form provided by the corporate and
sign it for authorizing debit to his bank account.Customer willhand over duly filled up mandate form to
corporate/service provider, who in turn would submit the same tothe sponsor bank.
Page 17

<!-- Page 10 -->

Step3
The sponsor bank will capture the Destination Bank IFSC/MiCR details & other mandatory mandate
transactiondetailsandsendittoNPCl.
Step4
The mandate image and the related mandate transaction data will be routed to the concerned
destinationbanksovertheMMSsystem withinthetimelinesstatedbyNPCl.
Step5
The Destination Bank will validate the transaction date and thedetails given on the image of mandate.It
will send themandateverificationand acceptanceconfirmation messageto sponsorbank via NpCl,and
updates records at its end.
Step6
The Sponsor bank sends mandate informationupdate with UMRN to corporate fortheir recordupdates
to ensure the NACH transaction file carry the UMRN reference against the transactions sent for
processing in future.Once a mandate is uploaded, Corporate can view the same,since access has been
enabledtothemdirectlybyNPCl.
Page18

<!-- Page 11 -->

13. What are the steps involved in the Process of customer initiating mandate request through
DestinationBank?
Verified
Verification& mandaje
forwarding the information with
Mandateinitiatipn by datato Sponsor UMRN tont to
austomur: with UMRN BankviaNPCI Verified mandatedata with UMRN corporites
intorhat
Customer Destination Bank NPCI Sponsor Bank Corporates
Databaseupdatea Databaseupdite
Custamer sendingconfirmation sendingconfirmation
UMRN response response
NPCI's purview
Step1
The end customer that holds an account with Destination Bank sends the mandate initiation request
throughInternet/IVR/Paper(Mandateform)totheDestinationbank.
Step 2
Destination bank receives the mandate request along with the mandate data and sends the mandate
information overtheMMS.(e-mandate)
Step3
The mandate transaction data will be routed to the concerned sponsor banks with UMRN generated by
NACHsystem
Step 4
Sponsorbankupdatesitsrecordandforwardittocorporate/serviceprovider.
Step5
Corporate/serviceproviderupdates itsrecord and sendsthe confirmationto Sponsorbank.
Page19

<!-- Page 12 -->

Step 6
SponsorbanksendstheconfirmationtoNPCl.
Step7
NPCl routestheconfirmationtowardtheDestinationbank.
Step8
Upon receivingthe confirmationfrom Sponsorbank/Corporatevia NPCI MMSthedestinationbanks
providesupdatetoits customeronthestatus ofthemandate
14. When is a UMRN generated/assigned to the mandate?
The UMRN isgenerated immediately after the initiating bank/party creates the mandate using a GUI or
the xml file upload.The ACK/NACK file generated immediately after mandate submission will reflectthe
UMRN.
15.Can the Destination bank view and approve/reject all inward mandates using the GUl?
Yes.The GUl allows the Destination bank to view and approve/reject all mandated, irrespective of the
fact that themandate has been created by the Sponsor bank using the GUl or an xml file upload.
16.Does the bank need to encrypt the mandate files being uploaded to MMs? Does the bank need to
decrypt the INW mandate received foracceptance?
Yes.Standardencrypt/decryptprocess followed byNACH.
17.Can, banks send multiple mandates Create / Amendment / Cancel zip files to NPCl throughout the
day?
Yes,Banks can send multiple separate mandates create/amend/cancelfiles to NPCl throughouta day.
18. Similarly, can bank receive multiple mandates Create/ Amendment / Cancel zip files from NPCl
through the day. Or would the files be bundled at NpCi and what the bank would receive will be a
single Create/ Amendment/ Cancel zip file fora day?
Bank will receive a separate file for create/amend/cancel/accept, throughout a day No bundling will be
doneatNPcl.
Page/10

<!-- Page 13 -->

19.Who will be responsible for managing the physical mandates?
It will be responsibilityonthesponsorbankto retainaphysical copyof themandateforthe
period asperRBl guidelines.Sponsorbank should also ensurethatthe imagecopyand
mandatetransactiondatetoberetainedasperRBlguidelines.
20. What is the time available to the instructed agent to accept the mandate?
The instructed agent will have to accept/reject the mandate within5 business days of the generation of
would beconsideredas deemed rejected.
21.What does RejectReason Codemean?
Reject Reason Codes are the codes defined by NPCl. The instructed agent whilerejecting a mandate will
assignoneofthesecodesasareasonforrejectingthemandate.
22.Whatarethe SessionTimingsforMMs?
Session TimingsforMandatesareasfollows:
StartofDay (SOD) 10:00AM all days
MandateRequest Cut-off (MRC) Weekdays:10:00AMto12:30PM
Saturday:10:00AMto11:30PM
MandateAcceptanceReportCut-off Weekdays:12:30PMto05:00PM
(MARC)
Saturday:11:30AMto03:00PM
EndOfDay (EOD) Weekdays:05:00PM
Saturday:03:00PM
Page/11

<!-- Page 14 -->

23.What is the Centralised Mandate Validation Serviceoffered byNPCl?
The Centralised Mandate Validation service was launched on October 7, 2013.The service ensures that
only'good to debit' transactions are sent to the bank by Npcl for debit processing after validating
parameters like the customer account number, bank IFsc/MicR, amount, start date/end date of the
underlying activemandate.
>Fields whichwill bevalidated at NPCI
UMRN-Active/Non-Active
CustomerAccountNumber
DestinationBankIFSC/MICR
Amount
MaximumAmount
StartDate
EndDate/Until cancelled
Status ofthe Mandate (Active/inactive)
If the input transactions fail abovevalidations,NPCl willreject thosetransactions at SponsorBank end
itself and these transactions will not be sent to destinationbank for processing.
IV.Queriesrelated toPANoog
24.What is a 'User Number'? Can a single corporate have two or more user numbers?
It is the ID issued to a corporatethat is linked to the Sponsorbank.The corporatewill have to get a new
Usernumber if it changes its bank or will have tomaintain multipleusernumber if it is transacting with
more than onebank.
25.DoesNPCIvalidatestheUserNumber?
Yes, User number is being validated during the transaction leg and NPCl will reject the transaction,
without sending it to destination bank, in case of incorrect User number. Scenarios in which User
numberwill beconsideredinvalidisasfollows:
> If the user number mentioned in the transaction file does not match with the one that was
mentioned in the mandate.
If the user number does not exist.
Iftheusernumberdoes notmatchwiththeUserName.
Page / 12

<!-- Page 15 -->

26.What is the logicfollowed forgenerationof UserNumber?
User number will be generated by NACH. Logic is Sponsor bank's short code followed by running
sequencenumber.
27.Is the User Number unique to the Corporate or is it linked to the Sponsor Bank?
User number is unique across the system,if a corporate has a tieup with two banks he will have 2 user
numbers.
28. Can the same User number be used across all the products or banks have to seek different User
Number for Different Products?
As the user number fields having different lengths depending on the file formats so user can't use NACH
CRorDRusernumbersforAPBandECS.
29.Does NPCl validate the User Number/ User Name at the time of Mandate Processing?
No,NPCl does not validate the User number/User name at the time of Mandate processing or
transactionprocessing.
30o.Whatdoyoumeanby"UtilityCode"?
Utility Code/ Corporate User ID referto the User Numberthat has been allocatedby NPCl, to
the Corporates.
V.Queries related to Pain 010:
31.Whatarethe fields thatcan'tbe amended?
Thefieldsthatcan'tbeamendedare:
a.)UMRN
b.)PaymentType
c.)DebtorBankName
d.)Debtor Bank ID
e.)NameofDebtorAccountHolder
Page/13

<!-- Page 16 -->

Vl.Queries related to Pain 012:
32.Is the process similar to the NACH debit file whereby banks can get an ACK,partial ACK ora NACK?
eachmandate, therewill notbeanypartial ACK, asdoneinACH.
33.Do bank need to send one mandate response file (PAlNO12-Mandate Acceptance)for each file
they receive from NPCl, or can they send one consolidated PAiNoi2 containing details of all
acceptance and rejections for mandate initiation, updating and cancellation requests?
For every acceptance, there is a paino12 message is sent. Consolidated file upload process is not
available,
34. For the 3 separate files that the bank receive, can they send back a single paino12 file containing
records which could pertain to mandate creation, amendment or cancellation.
The banks cannot use a single Acceptance xml file for all three types of mandates -Creation,
Amendment and Cancellation.Eachmandate willhave tobe accepted individually.
35. If the bank receives 5 mandates on day 0, can it stagger the approval/rejection over the next 5
days. i.e.approve one mandate on day 1, two mandates on day 2 and remaining mandates on day 5.
Oncethe inward fora mandate is generated the Instructed agent has 5business daystoapprovethe
mandate.The Instructed agent may decide to stagger theapproval/rejection over the period of these
fivedays.
VII.QUERIESOFACHDEBIT(ATTRANSACTIONLEVEL)
36. For every single Input file (Transaction File), does the destination bank receive separate inward
file?
No, the destination bank will not get different inwardsfor different input files.Instead it will get
a single consolidated inward file for all the input files initiated on the bank.Only in case where
the transaction count exceeds 20000 records, the file gets split into multiple file with 20000 or
lessrecords ineach.
Page/14

<!-- Page 17 -->

37.What are the Session Timings of NACH-Dr.?
Presentation and Return Timings
Weekdays
Presentation:10:00-12:30hrs Return:1500-1700hrs
Saturdays
Presentation:10:00-11:30hrs Return:14:00-15:00hrs
SettlementTimings
Weekdays
PresentationSettlement:13:00-14:00hrs ReturnSettlement:17:30-18:30hrs
Saturdays
PresentationSettlement:12:00-13:00hrs ReturnSettlement:15:30-16:30hrs
Page | 15

<!-- Page 18 -->

Vill.Annexure1-DescriptionofMandatefields.
1. UMRN-UMRN is a Unique Mandate Reference numberallocated to each new mandate created
in NACH Debit.It is auto generated by the NACH system during mandate creation.UMRN is
mandatory forevery transaction and even during mandate amendment and cancellation.
2. DATE-The date on which the mandate was initiated. It should be in the following format:
DD/MM/YYYY
3. SPONSORBANKCODE-SponSorBankIFSC/MICRcode.
4. UTiLITYCODE-It is theUserNumber allocated to the Utility/Biller/Bank entity/Aggregator.
5. NAMEOFUTILITY/BILLER/BANK/COMPANY-It isthenameof the serviceprovider.
6. ACTiON-Actionthatthecustomerwanttotake i.e.Create/Amend/Cancel.
A/c Type-It is the type ofiaccount held by the Payer against which themandate is being issued
(Fore.g.Savings, Current, CC,Others)
8.LEGALACCOUNTNO.-Payer'sbankaccount number.
9. Name of theDestination Bank with Branch:Name of the Payer's Bank and its Branch Name
10.IFSc/MICRCode-IFSC/MICRCodeofPayer'sbank.
1i.Maximumamountpertransaction that couldbeprocessed, inwords.
12.Amount in figures, similarto the amount mentioned in words..
13.CONSUMER REFERENCE NUMBER (Reference 1)- It is the reference number that has been
allotted to the Payerby the User institution (Utility/Biller/Bankentity).
14.SCHEME/ PLAN REFERENCE NUMBER (Reference 2)-Scheme/Plan reference number under
whichthe Payer is authorizing the Userinstitution to debit his/her account.
15.FREQUENCY-Itreferstothefrequencyoftransactions.
16,PERIOD-Validityofmandatewithdates inDD/MM/YYYYformat.
17.Names of customer/s and signaturesas wellas seal ofcompany (where required)
18.Undertakingbycustomer
19.CustomerAdditionalIdentification-PermanentID of customer.E.g.PAN/Aadhaar No.
20.Telephone numberwith STD Code,of Payer.
Page|16

<!-- Page 19 -->

21. 10 digit mobile numberof Payer.
22.Mail IDofPayer.
Page|17

<!-- Page 20 -->

IX.ANNEXURE2.Mandateimage
MandateValidtillNovember30,2014
UMRN
Sponsor Bank Code Utility Code
I/We hereby authorize Create mandate.on: Savings: Current:
(NameorUrmty/nler/Bank/Gonpeny) Canceit nandate on:
Update mandate.on Others:
LegalAccountNumberTT
MANOATEINSTRUCTIONFORM with (NameafDestinatior BankwithBranch) ZIFSC/MICR.Code wtodebitamountof/uptoamaximum.of
Rupees
for Paymenttowards Consumerreference Number?
Scheme/ fian.reference Number:
FREQUENCY PERIOD
Monthly Hatf Yearly Starting from
Bi-Monthly Yearly Upto
Quarterly as andwhen presented ar Until.cancelled Nanse/sand Signiture/s olAccoutit Holidees-1? faaporbankniciorda
Telegshtel(
RevisedMandateformvalidfromApril25,2014
UMRN Date
Tick（) Sponsor Bank Code Utility Code
CREATE /Weherebyauthorize todebit (tickv) SB/CA/CC/5B-NRE/SB-NRO/Other
MODIFY
CANCEL Banka/cnmber
withBank IFSC orMICR
an amount of Rupees
FREQUENCY MthlyQtlyH-YrlyYrlyAs&whenpresented DEBITTYPEFixedAmount MaximumAmount
Reference1 Phone No.
Reference2 Email ID
PERIOD
From
To
Or Until Cancelled
3.
This is to conifirm that thedecluration hasbeen airefuily read,understeod &made by me/us
Page/18
