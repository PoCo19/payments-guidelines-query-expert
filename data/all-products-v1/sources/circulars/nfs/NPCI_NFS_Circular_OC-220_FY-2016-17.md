# Circular 220 - NFS ATM Network_Settlement & Reconcilation procedure for interoperable cash deposit (ICD) transaction

Circular/reference number: NPCI/NFS/OCNo.220/2016-17
Date: 18th August, 2016

<!-- Page 1 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.220/2016-17 18th August, 2016
To，
All MembersofNational FinancialSwitch(NFS)
Madam/DearSir,
Sub:NFS ATM Network -Settlement and reconciliation procedure for Interoperable Cash Deposit (ICD)
transactions.
We are pleased to inform operationalising one more value added service (VAs)i.e.Interoperable Cash Deposit
(iCD)in NFS.Using thismode,bank customers would be able to deposit cash for creditingbeneficiary account
either in the same bank or with any other bank (enabled for ICD)by using their Debit/ATM card at the Cash
DepositMachine(CDM)ofNFSmembersenabledforthisservice.
1.Objective
The objective of this circular is to familiarise NFS members with the settlement and reconciliation procedure for
ICDtransactions.
Theimportantfeatures of theIcDtransactionsareasfollows:
a.Inter-operable: This will help customers of the participating NFSmember bank to deposit cash at the
CDM of the bank for crediting beneficiary account either in the same bank or with any other bank
(enabledforICD)byusingtheirDebit/ATMcard.
Please note that the cardholder's bank (lssuing bank), bank whose CDM is used (Acquiring Bank) and the
bank of the beneficiary (Beneficiary bank), all members should be enabled for ICD transactions in NFS.
b.Card based transaction:For IcD transactions, the depositor will have to use his card and PiN at the
Acquiring bank'sCDM for depositing cash.It will be the cardholder's (lssuing)bank responsibility to
authorizethetransactionbasedonCardandPiN.
C.2 set oftransactions:There will be 2 leg of the transaction for ICD.First will be validation leg and the
second will be deposit leg. Transaction flow of both the legs of transactions is given below in this
documentforreference.
Own account and third party deposits:Cardholder can deposit cash in his own account i.e.account
linked to the card used for depositing cash OR for crediting third party account held with any
participating bank. The cardholder will have option to select ‘own account deposit' or ‘third party
accountdeposit'.
Page1of5
1001A,TheCapital,BWing,10thFloor,Bandra KurlaComplex,Bandra (E),Mumbai 400051.,T:+912240009100 F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

e.Multiple Identifier for 'Third Party Account Deposit': It is proposed to have following options for giving
beneficiarydetailsforcreditingthirdpartyaccount:
Beneficiary's16/19digitDebit/ATMCardNumber
Beneficiary'sMobilePhoneNumber&MMiD
Beneficiary'sAccountNumber&IFSC
iv)AadhaarNumber
(Aadhaar number shall be checked at NPCl end for determining the beneficiary bank based on
the Aadhaar mapper. Beneficiary bank shall be required to ascertain the mapped account
number against the Aadhaar number entered by the depositor for crediting the account)
f.Displaying Beneficiary Account Holder's Name: The beneficiary account holder's name, as sent by the
beneficiary in the validation leg, will be displayed to the depositor. After seeing the beneficiary name
displayed on the screen, depositor can continue with the transaction for depositing cash or can cancel
thetransaction,ifcardholdersodesires.
g. Transaction Limits: There will be transaction limit of up to Rs. 49,999/- per transaction for ICD
transactions in NFS. The check needs to be applied by Acquirer and Beneficiary bank at their end for
onlinetransactions.
2.TransactionflowofICD
Thetransactionof ICD shall consistof thefollowingtwolegs:
a. ValidationLeg:ForCard&BeneficiaryAccountValidation
b.Deposit Leg: For Credit to the Beneficiary's Account
Thetransaction flowofvalidationleg anddeposit leg is given inAnnexureA.
Page2of5

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
3.Settlementand reconciliation procedureforICDtransactions
There will be threeentities involvedin IcD transactionas mentioned below:
b)Acquirer :whoseCDMisused bycardholderfordepositing cash
c) Issuer :whosecardisusedforcashdeposit (cardholder'sbank)
α) Beneficiary:who holdsthebeneficiary's account
SettlemententriesforICDtransactionisdepictedinthetablegivenbelow:
No. Sr. Issuer Acquirer Beneficiary Transactionamount Interchange Switchingfees
+Servicetax +Servicetax
Debit Credit Debit Credit Debit Credit
Issuer* NPCI*
Acquirer Beneficiary Beneficiary (50%) Acquirer Issuer NPCI
(50%)
Acquirer
Issuer (50%) Issuer NPCI
(50%)
Issuer(50%)+
Acquirer Beneficiary Acquirer Issuer NPCI
Beneficiary (50%)
Issuer (50%) +
Acquirer Beneficiary Acquirer Issuer NPCI
Beneficiary(50%)
*Shall be applicable only if suchtransactions areroutedtoNFs.
Same Bank
DifferentBank
4.Rawfiles,STLandDailySettlementReports(DSR)
Separate NTSL/DSR reports and raw data files, STL, verification reports, etc. shall be made available for ICD
transactions under menu option‘Files>>>Download Raw DataMiS_IcD'.The reports shall be made available in
the same format as other NFs transactions under Issuer and Acquirer section which can be used by NFS
membersforsettlementandreconciliation.
The details of ICD transactions in raw data file &STLreportsaregiven in AnnexureB for reference.
SampleNTSL/DSR report isgiven inAnnexureCforreference.
NoteforidentifyingONUStransactions:
ON US transactions canbe identified on the basis of Issuer Card no. (BIN)/Beneficiary details (BIN/IN);
AcquirerIDandRRN.
Thesevalueswill be same in eachrecord with same transaction type e.g.Pv/ cQ/ cD/ etc.available in
Acquirerrawdatafileand Issuerrawdatafile.
Page3of 5
1001A,TheCapital,BWing,10thFloor,BandraKurla Complex,Bandra(E),Mumbai 400051.T:+912240009100F:+912240009101www.npci.org.in
CIN：U74990MH2008NPL189067

<!-- Page 4 -->

5.Deemedsuccessfultransactions (RC-71)
Transactions that are timed out at Beneficiary's end i.e.leg 6 in Fig.2 & Fig.4 above is not received by NPCl will
be treated as 'deemed successful'with response code (RC) as ‘71'.These transactions shall be considered in
settlement as'deemed successful'for the deposit leg having transaction type as CD/UD/MD/AD/FD in raw data
files. Beneficiary bank should ccnsider the transaction amount available in raw data file for reconciling deemed
successfultransactions.
Beneficiary bank should ensure that all the transacticns settled (with RC-oo & 71) by NFS are credited to the
beneficiary's account. In case beneficiary's account has not been credited online for a particular transaction, it
should be identified and manually credited to the beneficiary's account by the beneficiary bank as part of their
such cases the beneficiary bank should immediately raise credit adjustment for that transaction to return the
funds to the Issuer.This is critical to avoid customer inconvenience and disputes for IcD transactions.
6.Reportof transactionsnot settled forthedayand transactions settled subsequently
ICD transaction consists of two legs (1)validation leg and (2) deposit leg, and both the transaction legs have two
different RRN and STAN.Unique'Deposit ID'will be sent by NPCI in the validation leg to the Acquirer.Acquirer
shculd send the same Deposit ID' in the deposit leg of the transaction to NPCl. During settlement and for
transaction life cycle management (disputes / adjustments) both the legs of the transaction shall be matched
basedonthe'DepositID'.
In an exceptional scenario, if Acquirer sends incorrect 'Deposit ID' and if it does not match with the 'Deposit ID'
in validation leg, then that particular deposit transaction shall not considered for settlement by NpCl on that
day. Report of such non-settlement deposit transactions shall be made available to NFS members in DMS under
menuoption'CDReports>>>NotsettledCashDepositTransactionReport'.
NPCl shall update the correct 'Deposit ID'in deposit leg of transaction by referring the validation leg and/or
based on the clarification sought from the Acquirer.Once the correct'Deposit ID'is updated and the transaction
is matched with validation leg, it will be considered for settlement. Such transactions settled subsequently will
be separately shown in next day's NTSL/DSR report.A report containing such transactions settled subsequently
shall be made availableto NFSmembers in DMS under menu option'cD Reports>>>Settled Cash Deposit
TransactionReport'
7.Successful CashDepositreportforIssuingbank
Cardholder's (lssuing) bank is not involved in deposit leg of the transaction. To know the status of the deposit
transaction,a separate reportlssuerSuccessful CashDepositTransactionReport'shall be madeavailableto the
Issuing bank on daily basis along with raw data files, STL reports, etc. in DMS.This report shall contain details of
report will help the Issuing bank to know the details of approved cash deposit transactions for which
interchangefeesisleviedtothebank.
Page4of5

<!-- Page 5 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
The detailed process of dispute management life cycle (dispute / adjustment)will be provided in a separate
circular.
Please make note of the above mentioned process and disseminate the instructions contained herein to the
officialsconcerned.
Foranyqueriesorclarification,pleasecontact:
Name e-mail ID MobileNumber
SaritDas sarit.das@npci.org.in 8108108694
MehfoozKhan mehfooz.khan@npci.org.in 8108122867
AvinashKunnoth avinash.kunnoth@npci.org.in 8879772725
AbhayParekh abhay.parekh@npci.org.in 8879772794
Yours faithfully,
RamSundaresan
Head-Operations
Encl:1.AnnexureA-TransactionflowofICD
2.AnnexureB-Detailsof ICDtransaction inRawdatafilesandSTLReports
3.AnnexureC-SampleDSRforICDtransactions
4.AnnexureD-NFSOC.219dated18thAugust,2016-Interchangefees forICDinNFS
Page 5 of 5
1001A,TheCapital,BWing,10thFloor,BandraKurla Complex,Bandra (E),Mumbai 400051.T:+912240009100F:+912240009101www.npci.org.in
CIN：U74990MH2008NPL189067
