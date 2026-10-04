# Circular 56 - Disabling cash retraction facility in ATMs - Advice of Acceptance of EJ Containing cash Dispensation Messages / Error Codes as valid proof during dispute resolution

Circular/reference number: NPCI/NFS/OCNo.56/2011-12

<!-- Page 1 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.56/2011-12 March26,2012
To
All MemberBanksofNationalFinancialSwitch(NFS)
DearSir/Madam,
Disabling Cash Retraction Facility in ATMs-Advice on Acceptance of EJ containing Cash
Dispensation Messages/Error Codes as Valid Proof duringDispute Resolution
Please refer to our Operating Circular no.47 dated January 19, 2012 (enclosed), on the subject of
disabling cash retraction facility in ATMsto contain cashretraction fraud.
For disputes raised through Online Dispute Management System, EJ copy is accepted as proof of
dispensing cash to the cardholder.However, while some ATM makes provide a clear message in EJ
regarding cash dispensation, some other ATM makes convey the proof of cash dispensation through
an error message. It is likely that EJ copy containing error message may be rejected by Member
Banks on the ground that this is viewed as invalid under the NFS guidelines. This may prolong the
process of dispute settlement.
In order to clear this ambiguity and present a clear direction on EJs containing error messages, it has
been decided to accept certain ATM error codes captured in the EJ of respective ATM makes as a
proof of cash dispensation. The table of such error codes is given in the appendix along with EJ
samples for the convenience of Member Banks. This table has been compiled based on our
discussionwithkeyATM vendors.
Member Banks are advised to use this table as a reckoner in disputes involving non receipt of cash
and to accept EJs containing such error codes as valid proof of cash dispensation.NpCl intends to
submit a copy of this circular along with EJ error code table to RBl with a request to circulate these
documentsto Banking Ombudsmanforreadyreferenceofthe latter.
In this context, we would like to again request Member Banks to report to NPCl, the following details
onaquarterlybasis foronward reportingtotheregulator:
1.Cases ofcomplaintsreceived fromthecustomerwhencash was leftback.
2.Number of ATMs wherethecashretractionfeaturehasbeendisabled.
Yoursfaithfully,
M.Balakrishnan
Chief Operating Officer
Encl.:As above
C-9, 8th Floor mqr/Phone:02226573150
RBIPremises q/Fax:02226571001
Bandra-KurlaComplex -/ email:contact@npci.org.in
Bandra East aqwrsc/Website:www.npci.org.in
-400051 Mumbai400051

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
APPENDIX
ATMVENDORWISEANALYSISOfATMBEHAVIOUR&DISPENSEERRORCODES
(Cash Retraction Disabled Scenarios)
Scenario1:CustomerDoesa Normal Transaction
Description: Customer does a successful cash withdrawal transaction and collects the dispensed cash
ATM Status Message Action EJ Format (Suggested) Remarks
Vendor (Dispense Error
Code)
DIEBOLD None Notapplicable TRANSACTIONLUNO123
DIEBOLDSYSTEMSPVT.LTD
25/12/1116:05
ATM ID :DSPL1234
SEQ NO. :1443
CARDNUMBER:99999999XXXX1234
ACCOUNTNO:0000000123456789
CASHWITHDRAWAL
TRANS AMOUNT:RS. 5000.00
RESP CODE:000
STATUSLUNO123
WINCOR NotApplicable None 16:39:27->TRANSACTIONSTART
16:39:27TRACK2DATA:12345678********
16:39:29PINENTERED
16:39:38TRANSACTIONREQUESTAB
16:39:38TRANSACTIONREPLYNEXT121FUNCTION2039
16:39:41CASHREQUEST:00010000
16:39:41 CASH 2:2,1;
16:39:45CASHPRESENTED
BANKLTD.
INDIA
DATE TIMETERM
02/11/1113:35ATMID
CARDNUMBER
12345XXXXXXXXX1234
RECORDNO. 4748
WITHDRAWAL RS.300.00
FROM A/C.000000123456789
AVAIL BAL RS.585.00
16:39:47CASHTAKEN
16:40:10<-TRANSACTIONEND
NCR No Error ABCBANK No error message
Message DATETIMETERM.ID printed.
04/26/0710:45MUMON032
LOCATION: XYZ...
CARDNO:429393XXXXXX4090
RECORDNO.8364
BALANCEINQUIRY
ACCOUNTNO.09580050007893
AVAILBAL98.56INR

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Scenario2:CustomerForgetsCashinDispenserClamp
Description: Customer does a normal cash withdrawal transaction but does not collect the cash. Since retract
mechanism is disabled, the cash continues to remains in the clamp and after the customer leaves the ATM premises,
the cash remains inthe clamp and is not retracted by the ATM presenter.Hence, Bank has technicallydispensed the
cashandthetransactionissuccessful.
ATM StatusMessage Action EJFormat (Suggested) Remarks
Vendor (Dispense Error
Code)
DIEBOLD DR01:23:00:30 PresentedMoney TRANSACTIONLUNO123 Errorprintedifcashisnot
Forgotten DIEBOLDSYSTEMSPVT.LTD collected
25/12/1115:29
ATMID ：DSPL1234
SEQNO. ：1444
CARDNUMBER:99999999XXXX1234
ACCOUNTNO：1001000200551319
CASHWITHDRAWAL
TRANSAMOUNT :RS. 5000.00
RESPCODE:OOO
STATUSLUNO123
002DR01:23:00:3025/12/1115:29:30
SERIAL#1444
PresentedMoneyForgotten
DR01:3F:00:40 ForgottenMoney 002DR01:3F:00:4025/12/1115:30:30 Thiserrorisprintedonce
Removed SERIAL#1444 theforgottencashis
ForgottenMoneyRemoved removed.
WINCOR Noerror ATM does not 17:28:21->TRANSACTIONSTART
retractthenotes 17:28:21TRACK2DATA:12345678********
&goesbackin 17:28:26PINENTERED
service 17:28:32TRANSACTIONREQUESTAB
17:28:32TRANSACTIONREPLYNEXT121FUNCTION2039
17:28:36CASHREQUEST:00010000
17:28:36 CASH 2:2,1;
17:28:39CASHPRESENTED
*063*17:28:50CASHPRESENTTIMEREXPIRED
17:28:55<-TRANSACTIONEND

<!-- Page 4 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
NCR No Error Cashshownto ABCBANK NoErrorMessageintheEJ.
Message customerand it DATETIMETERM.ID
will wait atthe 04/26/0710:45MUMON032 Whenevernextcustomer
exit untilpicked LOCATION:XYZ... tries for cash withdrawal
bythecustomer CARDNO:429393XXXXXX4090 transaction his transaction
orsomeoneelse RECORDNO.8364 fails and machine will go
BALANCEINQUIRY into suspendmode*for5
ACCOUNTNO.09580050007893 minutes.ATMalso sends
AVAILBAL98.56INR message to switch about
thisscenario.After 5
minutes, dispenserre-
initializesand cashatthe
exitispulled backtothe
purgebintomakethe
machine available for the
nextcustomer.
*Note:Certain switch may
handlethis differentlyand
mayneed to changethe
flowbasedonwhatBank
wantstodoaftersuchcash
notcollected cases.

<!-- Page 5 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.47/2011-12 January 18,2012
To
All MemberBanksofNational Financial Switch (NFS)
DearSir/Madam,
Disabling CashRetractionFacilityinATMstoContainCashRetractionFraud
During the past one year, several instances of fraud had been reported by member banks of NFS.
The most common type of fraud pertains to cash retraction.
The modus operandi is one of forcibly holding on to a few pieces of notes in ATM machines that has
cash retraction system while allowing one or two pieces of notes to be retracted and then claiming
non receipt of cash. Since retracted transactions are credited back to the customer's account, the
balance in fraudster's account remains unaffected even after collecting bulk of the delivered cash.
Presently, ATMs do not have the capability to count the pieces of retracted notes.For Acquiring
Banks, this created an ambiguity during periodic cash reconciliation on whether the shortage was
genuine or due to fraudulent partial retraction or fraud on the part of staff loading cash on ATMs.
This matter was discussed in detail at a special meeting of the NFs Steering Committee held on April
7, 2011. One of the possible solutions suggested at the meeting was to disable the cash retraction
facility inATMs.To understand the impact of this approach, NPCl requested select Member Banks to
conduct a Pilot at centres that reported high incidence of cash retraction fraud and submit their
findingstoNPCl.
The Pilot proved extremely effective in eliminating the misuse of cash retraction mechanism in ATMs
for committing fraudulent transactions. During the Pilot period, not a single instance of cash
retraction fraud was reported, a very positive indication that this could be the best approach for
preventing cash retraction frauds. A Report based on the outcome of the Pilot was submitted to the
Regulator for seeking their approval to this approach. RBl has accepted this proposal and vide.their
letter no.DPsS.c0.PDNo.1230/02.17.001/2011-12dated January9,2012 (enclosedherewith),has
granted approval for disabling cash retraction facility in ATMs.
In light of the above circular, all our Member Banks are advised to take note and ensure quick
implementationof thefollowingguidelines and confirmfull compliancebyMarch31, 2012:
C-9, 8th Floor gr/ Phone:02226573150
RBIPremises q/Fax:02226571001
Bandra-KurlaComplex -/email:contact@npci.org.in
BandraEast aqws/Website:www.npci.org.in
q-400051 Mumbai400051

<!-- Page 6 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
Educate the customer on the consequences of cash retraction and the reasons for disabling
the facility as customer awareness is very crucial to bring about discipline in collecting the
cashejected.
b) Display information regarding disabling cash retraction at each and every ATM location and
ensure wide propagation. The message may be flashed on the ATM machine before
conducting the transaction.
Draw a time plan by identifying the fraud prone areas to start with and complete the activity
withinthetimeframe.
Ensure that new ATMs being installed do not provide cashretraction features.
Report to NpCl on a quarterly basis, cases of complaints received from the customer when
cashwasleftback.
Disabling the cash retraction feature is a practicalapproach and the implementation of this feature
will certainly benefit the Banking Industry as a whole. Apart from making the NFS Network more
of their customers. This will have an immediate and positive impact on the dispute volumes and
facilitate in bringing the dispute percentage in line with International Benchmarks. Pro-active
support and cooperation of NFS Member Banks is hence requested in promptly implementing the
above guidelines. We are in readiness to extend necessary support in case of need.
Queries, ifanymaybeaddressedtoNPClasdetailedbelow:
1.Shri.Amit Shetty,SeniorManager,NFSBusiness,amit.shetty@npci.org.in,+918108108674
2. Shri. Satish Hegde, Manager, NFS Business, satish.hegde@npci.org.in, +91 810810 8618
Yoursfaithfully,
M.Balakrishnan
ChiefOperatingOfficer
Encl:Asabove

<!-- Page 7 -->

RESERVEBANKOFINDIA
www.rbi.org.in
DPSS.CO.PD.No.1230/02.17.001/2011-12 Januarv9,2012
Managing Director &Chief ExecutiveOfficer
National Payments CorporationofIndia
C-9,8thFloor,RBlPremises
BandraKurlaComplex
Bandra East
Mumbai-400051
DearSir,
Disabling Cash Retraction Facility in ATMs to contain Cash Retraction fraud
incidents
thecaptioned subject.
2.We advise that yourproposal for disabling cash retraction facility in ATMs to contain
cash retraction fraud incidents has been approved.
3.In this regard,youare requestedtoadvisethebanksasfollows --
a) To educate.the customer on the consequences of cash retraction and the
reasons for disabling this facility as customerawareness is very crucial to bring
about discipline in collecting the cash ejected. Information regarding disabling
cash retractionmaybe displayed at eachand everyATMlocation and should be
widely propagated.The message may be flashed on the ATMmachine before
conducting the transaction.
b) To draw a time plan by identifying the fraud prone areas to start with and
completion of the activity within the timeframe. Ensure that new ATMs being
installed do not provide cash retraction features.
leftbackonaquarterlybasis.
4.You are advised to submit a report on success of disabling cash retraction feature
withinthree months.
Yoursfaithfully
(Radha(Somakumar)
AssistantGeneralManager
14400001
4：（9122)22665336haT：(91-22)22659566-q：helpdpss@rbi.org.in
Department of Payment & Settlement Systems, Central Office, 14h Floor, Central Office Building,S.B.S.Marg, Mumbai-400 001.India
Tel:(91-22)22665336Fax:91-22)22659566E-mail:helpdpss@rbi.org.in
