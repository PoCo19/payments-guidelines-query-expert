# AePS | OC 45| FY 19 20 | AePS Raw data file and reports generated in BCS application

Circular/reference number: NPCI/AePS/2019-20/008

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/AePS/2019-20/008 September25,2019
To,
AllAePSMemberBanks
DearMadam/Sir,
Sub:AePS-RawData fileand reportsgenerated in BcSapplication
We refer to our AePs Interface Specification Document version 6.1 where banks have been
informed that‘Unique Reference Number (URN) and Transaction ld (TXN Id)'will be made
available in bothlssuerand AcquirerRawDatafiles.
At present the data in Raw Files ends at position 4o7 for Issuing Banks andat
position274forAcquiringBankswhichwill bechangedto552and419respectively
With this revision Member banks will start getting URN and TXN Id data in RAW data files
(which is currently blank) as follows:
Issuer RAW data (Position 408 - 457)
URN-408to442
TXNId=443to457
AcquirerRAWdata (Position275-324)
URN--275to309
TXNId-310to324
URN will be populated for all transaction types with value that will vary from 15 to maximum
35 characters and will be left justified followed by spaces to the right. URN will be used in
Dispute life cycle processing and every dispute shall have URN as the input field for
matching.
TXN Id will be populated only for 'Cash Deposit' transaction type,the value will vary from 12
to maximum 15 characters and will be left justified followedby spaces to the right.TxNld
will be filled with spaces for other than Cash Deposit transaction type.
ReferAnnexure A for revised Issuer &Acquirer Raw data file formats
There shall be no change in file naming convention of raw data files.
Please note that with this revision all banks will start getting additional extended data in both
Issuing & Acquiring Raw Data files which needs to be accounted for in their daily
reconciliationprocess.
Page 1 of 6
1001A,TheCapital,BWing,10thFloor,
Randra KiirlaComnloy Randra rF) Miimhai 4oOO51

<!-- Page 2 -->

The change in raw data will also have change in the following reports:
1..DRC File-TXNUID field will containURN number.
2.EMSFile-TXNIdcolumnwillnowconsistofURN.
3.Bulk Dispute File Upload Format- URN is mandatory in the revised bulk dispute
uploadformat-ReferAnnexureB
Effective October 10,2019 we will be implementing the above mentioned changesin
both Issuer and Acguirer raw data files and reports generated for banks in Bcs
system.
We have shared the sample Raw data files through mail incase of any assistance required
you may contact the undermentioned officials.
We request you to take note of the above and disseminate the information contained herein
to officials concerned.
For any further clarification, please send in your query to the following officials:
Name E-mail Mobile Number EscalationMatrix
Rajendra Maurya rajendra.maurya@npci.org.in Level 1
NayanBhandarkar nayan.bhandarkar@npci.org.in Level 2
Gururaj Rao gururai.rao@npci.ora.in Level3
Yours faithfully,
S.m.Na
SaiprasadNabar
Chief OnlineProducts-Operations
Encl:AnnexureA-RevisedIssuer&AcquirerRawDataFileFormat
B-RevisedBulkUploadFileFormat
Page2of 6

<!-- Page 3 -->

Annexure A
Revised IssuerRaw DataFileFormat:
Field From To Length Type Description
ITPTID AN PARTICIPANTID
ITTRTY AN TRANSACTIONTYPE
ITTRFA FROMACCOUNTTYPE
ITTRTA ANS TOACCOUNTTYPE
ITSER# 10 21 12 TRANSACTION SERIAL #
ITRSPC 22 23 AN RESPONSECODE
ITCRD# 42 19 PANNUMBER
ITMBR# 43 43 ANS MEMBERNUMBER
ITAPR# 44 49 ANS APPROVALNUMBER
ITSTAN 50 61 12 SYSTEM TRACE AUDIT #
ITTDAT 62 67 TRANSACTION DATE
ITTTIM 68 73 TRANSACTION TIME
ITMCAT 74 77 MERCHANTCATEGORYCODE
ITSDAT 78 83 SETTLEMENTDATE
ITCAID 98 15 ANS CARD ACCEPTORID
ITCATI 99 106 ANS CARDACCEPTOR TERMINALID
ITCATA 107 146 40 ANS CARDACCEPTOR TERMINALLOC
ITAQID 147 157 11 ANS AQUIRERID
ITNTID 158 160 ANS NETWORKID
ITAC1# 161 179 19 ANS ACCOUNT1NUMBER
ITAC1B 180 189 10 ANS ACCOUNT 1 BRANCH ID
ITAC2# 190 208 19 ANS ACCOUNT2NUMBER
ITAC2B 209 218 10 ANS ACCOUNT2BRANCHID
ITTRCC 219 TRANSACTION CURRENCY
ITTRNS 222 236 15 TRANSACTION AMOUNT
ITATRS 237 251 15 ACTUAL TRANSACTION AMT
ITTRFE 252 266 15 TRANSACTIONACTIVITY FEE
ITI1CC 267 269 ISSUER1SETTLEMENTCURRENCY
ITI1AS 270 284 15 ISSUER1SETTLEMENTAMOUNT
ITI1FS 285 299 15 ISSUER1SETTLEMENTFEE
ITI1PS 300 314 15 ISSUER1STLPROCESSINGFEE
ITC1CC 315 317 ANS CARDHOLDER1BILLCURRENCY
ITC1AS 318 332 15 CARDHOLDER 1BILLINGAMOUNT
CARDHOLDER 1BILLACTV FEE
ITC1AF 333 347 15
ITC1PF 348 362 15 CARDHOLDER1BILLPROCFEE
ITC1SF 363 377 15 CARDHOLDER1BILLSVCFEE
TRANS/CRDHLDR1CONVRATE
ITTC1R 378 392 15
ITSC1R 393 407 15 STLMNT/CRDHLDR1CONVRATE
Page 3 of 6

<!-- Page 4 -->

ITURN 408 442 35 ANS Unique ReferenceNumber
ITTXNID 443 457 15 ANS TransactionIdentifier(UsedSHG&
Deposit)
ITRFU1 458 475 18 ANS Reserved ForFuture Use
ITRFU2 476 493 18 ANS Reserved For Future Use
ITRFU3 494 494 ANS Reserved For FutureUse
ITRFU4 495 498 ANS Reserved For Future Use
ITRFU5 499 502 ANS Reserved For Future Use
ITRFU6 503 552 50 ANS Reserved ForFuture Use
** Note:- Any field without values shall either be populated with spaces for data type
ANS and zero'sfordatatype N
Revised AcquirerRawData File Format:
Field From To Length Type M/0 Description
ATPTID AN Participant ID
ATTRTY AN TransactionType
ATTRFA ANS FromAccountType
ATTRTA ANS To Account Type
ATSER# 10 21 12 Transaction Serial Number
ATRSPC 22 23 AN Response Code
ATCRD# 24 42 19 PAN Number
ATMBR# 43 43 ANS MemberNumber
ATAPR# 44 49 ANS ApprovalNumber
ATSTAN 50 61 12 System TraceAudit Number
ATTDAT 62 67 Transaction Date
ATTTIM 68 73 Transaction Time
ATMCAT 74 77 Merchant Category Code
ATCASD 78 83 CardAcceptorSettlementDate
ATCAID 84 98 15 ANS Card Acceptor ID
ATCATI 99 106 ANS CardAcceptorTerminal ID
ATCATA 107 146 40 ANS Card Acceptor Term.Location
ATAQID 147 157 11 ANS AcquireID
ATASDT 158 163 Acquirer Settlement Date
ATTRCC 164 166 Transaction Currency Code
ATTRNS 167 181 TransactionAmount
ATATRS 182 196 15 Actual TransactionAmount
ATTRFE 197 211 15 TransActivityFee
ATASCC 212
AcquirerSettlementCurrencyCode
ATASAS 215 229 15 AcquirerSettlementAmount
ATASFS 230 244 15 Acquirer Settlement Fee
ATASPS 245 259 15 AcquirerSettlementProcessFee
ATASCR 260 274 15 AcquirerSettlementConversionRate
ATURN 275 309 35 ANS Unigue Reference Number
Page 4 of 6

<!-- Page 5 -->

Transactionldentifier(UsedSHG&
ATTXNID 310 324 15 ANS Deposit)
ATRFU1 325 342 18 ANS Reserved For Future Use
ATRFU2 343 360 18 ANS ReservedForFutureUse
ATRFU3 361 361 ANS Reserved For Future Use
ATRFU4 362 365 ANS ReservedForFutureUse
ATRFU5 366 369 ANS Reserved For Future Use
ATRFU6 370 419 ANS ReservedForFuture Use
** Note:- Any field without values shall either be populated with spaces for data type
ANSandzero'sfordatatypeN
Page 5 of 6

<!-- Page 6 -->

Annexure B
RevisedBulkUploadFileFormat (URNismandatory):
Header Description Length
Bankadjref BankAdjustmentReferenceNumber Length - 100 (AN)
Flag DRC/B/C Length - 03 (A)
Shtdat Transaction Date YYYY-MM-DD (N)
Adjamt TransactionAmount (N)
Shser RRN Length -50 (N)
Shcrd 19 Digit (PAN Number) Length - 53 (AN)
Filename .csvfileName Length - 50 (AN)
Reason ReasonCode Length -05 (AN)
URN UniqueReferenceNumber Length - 35 (AN)
** URN will be mandatory for where the same is available in Raw Data files and other
Reports.
Page6of 6
