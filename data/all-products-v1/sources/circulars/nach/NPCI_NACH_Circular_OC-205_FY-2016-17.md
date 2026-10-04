# Circular No 205 - Implementation of standard scheme codes for DBTCircular No 205 - Implementation of standard scheme codes for DBT

Circular/reference number: NPCI/2016-17/NACH/Circular

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2016-17/NACH/Circular No.20g December 15,2016
To
AllNACHMemberBanks
Implementationof standard schemecodesforDBT
DBT mission office vide their OM No.D-11011/02/2016-DBT (Cab) (Pt.), dated September
23, 2016 and corrigendum dated December 09, 2016 issued standard scheme codes for
various central and state government schemes.The standardised scheme codes are of 5
digits. Both the OM's referred above are enclosed for the reference of the member banks.
The scheme codes will be used uniformly by all the stakeholders.
PFMs will be providing the scheme code to the member banks in payment files as an xml
tag as per the specifications provided in Annexure I. Technical details of the tag will be
issued by PFMS as well separately. Sponsor banks are advised to take a note of the same.
Along with this, 7 digit code issued by NPCl has to be incorporated by the sponsor banks at
the transaction level.
Providing the right scheme codes in the NACH files is of critical importance, as this forms
the basis for calculation of incentive and charges and the claims will be raised on the
departments based on the scheme codes. For submission of data in NACH, the banks
should follow the process given below
1. Provide 5 digit scheme code as given by PFMS at the header level suffixing spaces.
5 digit scheme code issued by DBT mission, it will be issued by NPCl to sponsor
banks) at the record level
NPCI will introduce a validation to check whether the 5 digit scheme codes provided in the
file at the header level is a sub-set of the 7 digit user code provided at the transaction
level. This is to ensure that the data pertaining to the same scheme is uploaded in a
single file. If there is any mismatch, the file will be rejected by the NACH system.
The above scheme code structure is applicable for DBT schemes only. For other schemes,
NPCl may allow the existing user codes to continue or allot new codes. A separate
communication will be sent on this to the respective sponsor banks who are processing the
data for these schemes.
NPCl will be providing the mapping of new 5 digit scheme code and the relevant 7 digit
user code allotted by NPCl.Note that within 15 days from the date of implementation of
scheme codes by PFMS, NPCl will disable the old user codes. Member banks should ensure
that from day one the right user codes are used for uploading the files, no time extension
will be allowed beyond 15 days.
1001A, The Capital, B Wing,10th Floor.Bandra Kurla Complex,Bandra [E).Mumbai 400 051.T:+91 22 40009100 F:+9122 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
As per the directive of the government, for DBT, the banks are alreeyAsed SSo&tEP oF INDIA
to the customers intimating the credit to the account. After the implementation of
standard scheme codes, the member banks should include the scheme name for which the
credit is received in the account both in the statement of account of the customer as well
as SMS alert sent to the customer.Note that only the scheme name should be provided not
the scheme codes. For this purpose banks may maintain tables listing the scheme codes
and their names and map the relevant scheme name at the time of sending SMs and
populating account statement. The standard text for sending the SMS is given in Annexure
Technical specifications is provided in Annexure Ill.
Member banks are advised to take note and ensure smooth implementation of scheme
codes.
For any-queries, please write to ach@npci.org.in
WitKwarm regards
(Giridhar G M)
VP&Head-NACH&CTSOperations
1001A,The Capital,BWing,10thFloor,Bandra Kurla Complex, Bandra (E),Mumbai 400051.T:+912240009100 F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
AnnexureI
XML tag
<PaymentsMessageld="000PPAPAYREQ081120161235"Source="CPSMS" Destination="ooo"
BankCode="000" BankName="STATE BANK OF INDIA" RecordsCount="1"
PaymentProduct="PPA"xmlns="http://cpsms.com/PaymentRequest">
<BatchDetails Corporateld="NHM" CPSMSBatchNo="C111600451386" C3535-"1030"
C1106-"32">
Where NHMwillbethe schemecode
Annexure Il
SMsalerts tocustomers
Department of financial services has advised all the member banks to implement the
scheme specific SMs credit alerts to all the beneficiaries. All the destination banks are
advised to take necessary steps to implement the SMS alerts on the following lines.
Post crediting the transaction amount SMs to be initiated
INR<Transaction amount> under DBT Scheme -<scheme name≥ is credited to your
account number ending with ***<last four digit> on 
1001A,The Capital,BWing,10th Floor,Bandra Kurla Complex,Bandra (E), Mumbai 400051.T:+912240009100 F:+91 22 40009101 www.npci.org.in
CIN：U74990MH2008NPL189067

<!-- Page 4 -->

NPCIN
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure III
Technical specificationdocument
No Field Description Length Field TypeMandatory/Optional Remarks
(Header) Credit Contra
Record
APBS transaction code33for
NUM Mandatory
APBStransaction code APBS credit.
User number issued by NPCl.
ALP / NUM Mandatory If 5 digits, the same should be
User Number 5or7 suffixed with spaces
Name of Government
ALP/NUM Mandatory
UserName 40 Department/Agency/User
Userdefinedreferencenumber
ALP / NUM Mandatory
User Reference 14 for entire transaction
APBSTapeInput NUM Optional
Number User defined input tape
Sponsor Bank IIN NUM Mandatory 6digit SponsorBanklIN
User's Bank Account Account number of user with
ALP /NUM Optional
Number 15 sponsor bank
Ledger Folio Number ALP / NUM Optional Ledgerfolioparticulars
User defined limit which would
User Defined limit for NUM Optional be taken to validate individual
individual items 13 items amount
10 Total Items NUM Mandatory Total items in the file
Total Amount
NUM Mandatory
11 (Balancing Amount) 13 Amount in paise
Settlement Date Dateonwhichsettlementistobe
NUM Mandatory
12 (DDMMYYYY) effected
Reserved (kept blank APBS itemsequence numberto
NUM Optional
13 by user) be allotted by NPCI
Reserved (kept blank Checksum total generated by
NUM Optional
14 by user) 10 NPCI
15 Filler ALP / NUM Optional Spaces
Total 165
1001A,The Capital,BWing,10th Floor,Bandra Kurla Complex,Bandra (E),Mumbai 400051.T:+912240009100 F:+9122 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 5 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Sr. Mandatoryl
No Field Description Length Field Type Optional Remarks
Credit Records
APBSTransaction
NUM Mandatory
Code Transactioncode77forAPBScredit.
6digitDestinationBankllN,Leftpadded
withzeroes.Thisfieldcouldbeleftblank
NUM Optional
Destination Bank by the sponsor bank as the APBS mapper
IIN has capability to populate this field.
Destination Account MICRtransaction code
NUM Optional
Type (10/11/12/29/30/31)
Ledger Folio
ALP / NUM Optional
Number Alphanumericledgerfolioparticulars
BeneficiaryAadhaar
NUM Mandatory
Number 15 Beneficiary's 12 digit Aadhaar Number
BeneficiaryAccount Beneficiary's account name (to be
ALP / NUM Optional
Holder's Name 40 updated by destination bank)
Sponsor Bank lIN NUM Mandatory 6digitSponsorBank IIN
ALP / NUM Mandatory
User Number Existing user number
10 User Name ALP / NUM Mandatory ExistingUserNumber
User defined reference number such as
ledgerfolionumber,share/debenture
ALP / NUM Mandatory certificate number or any other unique
User Credit identification number given by user to
11 Reference 13 individualbeneficiaries
12 Amount 13 NUM Mandatory AmountinPaise
Reserved (APBS APBSitem sequencenumbertobe
NUM Optional
13 Item Seq.No.) 10 allotted by NPCI
Reserved
NUM Optional
14 (Checksum) 10 Checksum total generated byNPCI
Reserved (Flag for NUM Optional Flag for items credited (1) andreturned
15 success /return) uncredited (O) allotted by NPCI
Spaces in case null, otherwise return
Reserved (Return NUM Optional code left padded with space (tobe
16 codes) updated by destination bank)
17 Filler NUM Optional To be kept blank
Total 165
1001A,The Capital, B Wing,10th Floor,Bandra Kurla Complex, Bandra (E),Mumbai400051.T:+912240009100 F:+9122 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067
