# 15-Jul-2015 - RuPay/13/2015-16 - Enhancememts in RuPay Global Clearing and Settlement System (RGCS)

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Circular: RuPay/13/2015-16 July 15, 2015
EnhancementsinRuPayGlobalClearingandSettlementSystem(RGCS)
We have made enhancement in RuPay Global Clearing and Settlement System (RGcS) so as to
facilitate member banks in handling their day to day operational activity more effectively.
The following enhancements havebeen implemented with effect from Jun 28, 2015.The detailed
functionality of these enhancements are given in Annexure A.
1.Acquiring banks are now allowed to process clearing and settlement of PoS and e-Commerce
transactions for specific declined response codes. Complete dispute life cycle shall be available
toissuingbanks for suchtransactions.
2. Relaxation in matching parameters on refund transactions.
3. DMSapproved/authorisedtransactionfilegenerationonadailybasis.
4. Late presentment indicator populated in settlement files for Presentments beyond defined TAT.
5. Additional raw data files consisting of header and footer is being generated.
6. Availability of new reports
ON-USReports and
MemberFund Collection (MFC)/MemberFund Disbursement (MFD).
7. Settlement date is incorporated in all settlement reports.
8. For SMS declined transactions, amount will be available in DsR and all other settlement reports.
Download of RuPay Circulars, Manuals and PGP Tool has been enabled.
10. Option to Input Secret Question and answer for existing and new RGcS production users.
We request you to take note of the above and disseminate the information contained herein to
officials concerned.
Foranyfurther clarification,please send in your query to the following officials:
Name E-mail Mobile Number
Pramila Shetty pramila.shetty@npci.org.in 8879772787
Nayan Bhandarkar nayan.bhandarkar@npci.org.in 8108122829
Yours faithfully,
RamSundaresan
Head-Operations
Encl:
Detailsofenhancements-AnnexureA
File naming convention and File message format-Annexure B
Format of additional RawData FilewithHeaderandFooter-AnnexureC
Page 1 of 6
The Capital, qT/Phone:02240009100
1001 Unit No.1001A, B Wing, q/Fax:02240009101
1070 10th Floor,PlotNo.C-70, 专-/email:contact@npci.org.in
 , f  GBlock,BandraKurlaComplex, aa/Website:www.npci.org.in
40005 Bandra(E),Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI  p  p
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure A
Sr. EnhancementDescription Existing Revised Functionality
No. Functionality
Acquiring banks are now Not Allowed A.Acquiring Banks can raise Presentment for DMs
allowed to process transactions andDebit Adjustment for SMS transactions for
clearing and settlement of the decline response codes listed here below:
POSande-Commerce
transactions for specific ITM/ RGCS Decline Description
declined response codes.
Response Codes
31/22 Suspected malfunction
Complete dispute life cycle
50/68 Acquirertime-out
will be available to
member banks (issuer and 08/91 Issuerorswitchisinoperative
Acquirer) for such 89/96 System malfunction
transactions. 40/CR UnabletoProcessReversal
07/20 Invalid response
28/21 No action taken
41/CS Unableto Process Storeand forward
B.Likewise, complete dispute life cycle will be available to
memberbanks (Issuer and Acguirer)for such transactions
Relaxation in matching 6parameters Matching parameters have been relaxed and only the below
parameters on refund to be mentioned 3 parameters to be considered for processing refund
transactions. matched transactions:
while
processing 1. Primary Account Number
refund 2.  Acquirer Reference Data (RRN)
transactions. 3. Acquirer Institution ID Code
DMS approved/authorised File not DMS response file - 87 for Acquiring Banks and DMS response file -
transaction file generation generated 88 for Issuing Banks is being generated.
on daily basis.
File naming convention and file message format is available in
Annexure B.
Population of Late Not Late Presentment Indicator (<nLtPrsntlnd>) will be populated as "y"
presentment indicatorin populated in acknowledgement/incoming files for Presentments beyond time
settlement files for frame of 7 days from the next day of authorisation date.
Presentments beyond "n" will be populated for transactions presented within the time
defined time frame TAT. frame.
Additional raw data files Existing raw Additional raw data files (HDR_Extended) with header and footer
consisting of header and data file details is being generated. File format for both the raw data files
trailer is being generated. does not (ExtendedandHDR_Extended)is identical.
contain
header and Header and footer message structure of the additional raw data file
footer is available in Annexure C.
Page 2 of 6

<!-- Page 3 -->

Two additional reports as mentioned below is being generated in
Availabilityof new reports Reports not
i) ON-US Reports and ii) available reports folder:
MemberFundCollection
1.ON-Us transaction report. This report consists of both 1) e-
(MFC)/MemberFund
commerce ON-US transactions (routed through NPCl)and
Disbursement (MFD).
2) Successful ON-Us transactions uploaded by member
banks in file type 80 (transactions not routed through
NPCI).
2.MFC/ MFD report.This report will contain details of fund
collection and fund disbursement transactions originated by
member banks.
Settlement date Not available Settlement date in "DD-MM-YYYY" format will be available in all
incorporated in all settlement reports.
settlement reports.
ForSMSdeclined Only For SMS declined transactions, along with the transaction count,
transactions, consolidated consolidated consolidated amount is available in DsR and all settlement reports.
amount is available in DSR transaction
and all other settlement count is
reports. available
Download of RuPay Not available RuPay Circulars, Manuals and PGP Tool will be shared in designated
Circulars, Manuals and folders on RGCS portal.
PGPToolhasbeen
enabled.
Not available Secret Question and Answer feature has been built in RGCS system
10 Option to Input Secret
QuestionandAnswerfor in"User Profile"screen.
existing and new RGCS
New and existing users can define/ change secret question and
production users.
answer for resetting their individual passwords.
Page 3 of 6

<!-- Page 4 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
AnnexureB
Filenaming conventionforDMStransaction
Sr. Element Format Description andPossiblevalues
No
File Type N2 It defines thefiletype.
87-DMSresponsefile to Acquirer.
88-DMS incomingfiletoIssuer.
Clearing Cycle N1 It represents the clearing cycle number in which the transactions
indicator were processed in the RGCS.
Possible values:
O-Default
N -Integer representing the clearing cycle number in which the
transaction was processed
Participant ID AN11 It represents the participant ID allotted to themember by NpCl.It
comprisesofthebelow mentioned components
4Digit Alphabet valueof IFSC/Swift bank identifier code
3 digit numeric Bank code (Middle three digits of MiCR Code issued
by RBI)
4digit numericrunning serialNumber
E.g.ForABC Bank
EFGH（IFSC/SwiftBankidentifier)
002 (Middlethree digits of ABCbank'sMICRCode)
0001(Running Serial Number-1)
PID=EFGH0020001
Julian Date YYDDD In case of member generated files (File type-O01) Julian date will be
YY-Year the date on which generates the outgoing file.
DDD-Julian In case of Network generated acknowledgement files (i.e.file type.-
date O2)the Julian date will be the fileprocessed/generated date.
(Note: NPCl generates acknowledgment file for each of the outgoing
files received from members).
In case of Network generated incoming files (i.e.File type -o1) the
.Julian date will be the file processed/generated date (Settlement
date).
In case of Network generated acknowledgement for ON HOLD
transactions (i.e. file type-04),Julian date will bethe file
processed/generated date as mentioned in the members outgoing
file.
File Sequence N2 It defines the file sequencenumberfora particular date.
The range can be from 0o to 99.
e.g.
00-1stfile
01-2ndfile
Page4of6

<!-- Page 5 -->

Table 1File namingconvention
MessageFormat:DMSTransaction
Acquirer Issuer
NPCI ACQ NPCI
SL
No Field Name XML Tag to [Outgoing] Incoming [AC] to [Outgoing] Incoming [ISS]
ACQ NPCI [ACK] NPCI [ACK]
MTI <nMTI>
Function Code <nFunCd>
Record Number <nRecNum>
DateandTime,Local Transaction <nDtTmLcTxn>
Primary Account Number <nPAN>
Retrieval ReferenceNumber <nRRN>
Acquirer InstitutionID code <nAcqinstCd>
ApprovalCode <nApprvlCd>
Card Acceptor Terminal ID <nCrdAcptTrmld>
10 Amount,Transaction <nAmtTxn>
11 Currency Code, Transaction <nCcyCdTxn>
12 Amounts,Additional <nAmtAdd>
13 Transaction Originator Institution ID code <nTxnOrglnstCd>
14 Transaction Destination Institution ID code <nTxnDeslnstCd>
15 Unique File Name <nUnFINm>
16 Date, Settlement <nDtSet>
17 SettlementDR/CRIndicator <nSetDCInd>
18 Amount, Settlement <nAmtSet>
19 Currency Code, Settlement <nCcyCdSet>
20 Conversion Rate,Settlement <nConvRtSet>
21 Amount, Billing <nAmtBil>
22 Conversion Rate, billing <nConvRtBil>
23 Currency Code, Billing <nCcyCdBil>
24 RGCS Received date <nRGCSRcvdDt>
25 FeeType Code1 <nFeeTpCd>
26 InterchangeCategory1 <nlntrchngCtg>
27 Fee amount 1 <nFeeAmt>
28 FeeDR/CR Indicator1 <nFeeDCInd>
29 Fee Currency 1 <nFeeCcy>
Page5of 6

<!-- Page 6 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
AnnexureC
Data Elements Description for Raw Data File
Following are the details description of Data Elements used in Raw Data file w.r.t Header & Trailer.
HDRElement:HeaderIdentifier
HeaderIdentifier
Type A3
Format Fixed
Description Identifies the header message type of Raw Data File.
Constraints Thefield is mandatoryforHeadermessageof RawData File.
Possiblevalues HDR
TRL Element:Trailer RecordIdentifier
TrailerRecord ldentifier
Type A3
Format Fixed
Description IdentifiesthetrailermessagetypeofRawDataFile
Constraints The field is mandatoryfor Trailermessageof Raw data File.
Page 6of 6
