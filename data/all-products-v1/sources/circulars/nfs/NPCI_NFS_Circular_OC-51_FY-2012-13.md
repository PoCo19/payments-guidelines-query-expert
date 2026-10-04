# NFS OC 51 Addition of reason code in bulk upload file format

Circular/reference number: NPCI/NFS/OCNo.51/2011-12

<!-- Page 1 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.51/2011-12 Feb03,2012
To
AllMemberBanksofNationalFinancialSwitch(NFS)
DearSir/Madam,
Sub:Additionof reason codein bulkupload fileformat.
The present facility of uploading Dispute Data through files (which is referred to as Bulk upload file
option) has been amended additionally with the feature of capturing the reason codes along with the
Dispute Details.The Bulk upload file option with type of disputed and reason codes has been listed in
theAnnexure-l.
We request Banks to adopt the amended file structure at the earliest that will facilitate NFS Member
Banks in understanding the reason for which a dispute has been raised or rejected in NFS Dispute
Managementsystem.
The existing fileformat (of Bulkupload without reason codes)and newfileformat (Bulk upload with
reasoncodes)canbecarriedouttillMarch31,2012.
However we would like to bring to your notice that the existing file format (Bulk upload without reason
codes)will not be supported on the DMS system fromApril 01,2012.Hence we request youto amend
your internal Software,processes by implementing the changes at your end by the above date that will
assistusinsendingthereasoncodesforeachoftheDisputes.
Please notethat there isnoBulkdisputeoptionavailableforany Good Faithcases.
Foranyclarifications,please contactus as perthe escalationmatrix listed in Annexure-ll given below.
Yoursfaithfully,
M.Balakrishnan
ChiefOperating Officer
C-9,8thFloor sr3qr/Phone:02226573150
RBIPremises a/Fax:02226571001
Bandra-KurlaComplex -a/email:contact@npci.org.in
Bandra East aaz/Website:www.npci.org.in
-400051 Mumbai400051

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-l
Reasoncodeswithdisputesflag&description
ReasonCode ReasonCodeDescription DisputeFlag Dispute Description
CashRetractatATM ChargebackAccepted
PresenterError Chargeback Accepted
PowerDownbeforecashispresented ChargebackAccepted
CommunicationerroratATM ChargebackAccepted
Hardware Fault ChargebackAccepted
PartialDispense Chargeback Accepted
MessageRejectatATM ChargebackAccepted
Communication erroratAcquirer Switch ChargebackAccepted
Deemed Acceptance ChargebackAccepted
Accountdebited but cashnot dispensed Chargeback
Partialamountdispensed Chargeback
CustomerFailedtoCollectCash Chargeback
Chargebackbasedonreconciliation Chargeback
Single DisputeMultipleTransactions Chargeback
FoundCashOverageatATM CreditAdjustment
SettlementnotReceived Debit Adjustment
SettlementPartiallyReceived DebitAdjustment
IncompleteEvidence DB Debit Chargeback
NoEvidenceProvided DB Debit Chargeback
Invalid Evidence DB DebitChargeback
TransactionDeniedbycustomer DB DebitChargeback
AdditionalProofSubmitted DR DebitRe-Presentment
CustomerDenyingTransaction Pre-Arbitration
Invalid Evidence Pre-Arbitration
ValidEvidenceSubmitted PR Pre-Arbitration Rep
Others PR Pre-ArbitrationRep
Full AmountDispensed-ProofAttached Re-presentment
Partial Amount Dispensed-ProofAttached Re-presentment

<!-- Page 3 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
2)Bulkfileformatwithdescription
Bulk header FieldDescription Type Remarks
bankadjref Bank Adjustment Reference Character BanksreferenceNumberforDispute
flag Disputeflag Character ReferTable1ofAnnexure
shtdat Date Date Transactiondate
adjamt Amount Numeric DisputeAmount
shser RRN Numeric RetrievalReferenceNumber
shcrd CardNumber Numeric CardNumber
filename Filename Character Nameofthefile
reason Reasoncode Numeric ReferTable1ofAnnexure
3)Specimenformatfilewithreasoncode
bankadjref,flag,shtDat,adjamt,shser,shcrd,filename,reason
ACQ/ISS/RRN/DD/MMM/YY,B,YYYY-MM-DD,50,132913824424,999999******0224,fi1ename,1
ACQ/ISS/RRN/DD/MMM/YY,B,YYYY-MM-DD,50,132913824427,999999******0224,fi1ename,2
ACQ/ISS/RRN/DD/MMM/YY,B,YYYY-MM-DD,100,132913824430,99999******0224,fi1ename,3
Please note, exceptaddition of reasoncode, bulkfileformatwill remain same

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-ll
ContactDetails of NFSDMSTeam
NFSContactDetails
Levell
NFSDMS
Ph:022-40508662
Ph:022-40508500
nfsdms@npci.org.in
Level Il
Mr.AjitRaju Mr.NiranjanRepaka
Ph:022-40508655,022-40508500 Ph:022-40508663,022-40508500
M:+91-8108108695 M:+91-8108122881
ajit.raju@npci.org.in niranian.repaka@npci.org.in
Mr.Suhas Parab Mr.SaritDas
Ph:022-40508665,022-40508500 Ph:022-40508657,022-40508500
M:+91-8108122864 M:+91-8108108694
suhas.parab@npci.org.in sarit.das@npci.org.in
Level ll
Mr.R.Sankara Subramanian Mr.Krishna Prasad
Ph:044-28160730 Ph:022-40508659,022-40508500
M:+91+9840721856 M:+91-8108122871
sankara.subramanian@npci.org.in Krishna.prasad@npci.org.in
Level IV
Mr.ShaktiswarRao Ms.NayanBhandarkar
Ph:022-40508670,022-40508500 Ph:022-40508669,022-40508500
M:+91-8108122856 M:+91-8108122829
saktiswar.rao@npci.org.in nayan.bhandarkar@npci.org.in
Mr.AN Murali
Ph:044-28160731
M:+91-9246118642
murali.an@npci.org.in
LevelV
Mr.SureshVavilala
Ph:022-40508515,022-40508500
M:+91-8108122876
suresh.vavilala@npci.org.in
