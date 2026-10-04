# Circular No.110 NACH Debit (ECS Debit) File FOrmat and Return Reason Codes

Circular/reference number: NPCI/2015-16/NACH/110

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2015-16/NACH/110
July15,2015
To,
AllNACHMemberBanks
NACHDebit (ECS Debit)FileFormatand Return ReasonCodes
With reference to the circular number 100 dated April 15,2015on processing NACHDebit (EcSDebit)
files through NACH.
2. Member banks are requested to take a note of the below
a) Inward files for destination banks can be given with or without footer. Currently by default
we are providing the files with footer, the banks desirous of having the inward file without foot can
write to us for necessary mapping.
b) To facilitate the banks to generate the returns we have provided return file generator, it is
available under the Utilities menu. It is advised that the banks with high volumes have their own
systems in place for generating the returns file.
c) For NACH debit product returns, files with 50 character length will only be accepted. Please
note that return files in any other format will be rejected by the system.
3. For ready reference we have provided the file formats for NACH Debit - Input (Annexure I), Returns
4. As the process is migrated as is where-is basis, there is no provision in the system for extensions.
Member banks are advised to make all the necessary arrangements to handle inward and submit returns
in time. To facilitate larger time window NPCl is making the inward files available one day prior to
the value date.Note that no requests for extensions will be entertained.
5.For any queries/further help required, please feel free to email at ach@npci.org.in
With Warm Regards,
(Gtridhar G.M.)
VP & Head -CTS &NACHOperations
The Capital, TAT /Phone:02240009100
1001 Unit No.1001A, B Wing, /Fax:02240009101
10-70 10th Floor,Plot No.C-70, 专-1email:contact@npci.org.in
G Block, Bandra Kurla Complex, a专/Website:www.npci.org.in
400051 Bandra (E),Mumbai 400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-I Input FileFormat
S.No Field Descriptions Length Field Type Mandatory Remarks
(Header) Credit Contra Record
Ecstransaction codefor NECS NUM Mandatory Code55forECSDebit
UserNumber NUM Mandatory UsernumberallottedbyNpciforNEcs
User Name 40 ALPNUM Mandatory AlphaNumericdescription-ContainsInstitutionName
User Reference ALDNUM Qptional Userdefinedreterencenumoerfcrtheentiretransaction (Alpha
Numeric.if notprovided,will beoopulated fromSFG.
ECsfilenumber NUM Optional Userdefined inputtape
SponsorBankMiCR NUM Mandatory SoonsorBankMicR
User's BankAccountNumber 15 ALPNUM Optional
(Aiphanumeric)
Ledger Folic Number ALPNUM Optional Alpha numeric LedgerFolloparticulars.
UserDefined limitforindividualitems 13 NUM Optional User defined limit which would be taken forvalidat ng the credit
/debititems,inpaise
10 Total Amountinpaise(BalancingAmount) 13 NUM Mandatory Amountinpaise
SeltlementDate(DDMMYYYY) NUM Mandatory Date onwhich settlement is soughttobeeffected
12 Reserved (keptblankbyuser) 10 NUM Optional ACH File sequence numberto be allotted by NPCi
13 Reserved (keptblankbyuser) 10 NUM Optional ChecksumTotai generatea byNPCi
14 Filler ALPNUM Optional Soaces
Total 156
Debit Records
EcsTransaction Code NUM Mandatory Coce 66 for Ecs Debit
Destination sort code NUM Mandatory DestnBankMiCR
DestinationAccountType NUM Optional As provided by Bank-Needs to be asper
NECS(10/11/12/29/30/31)orolank.
LedgerFolioNumber ALPNUM Optional AlohanumericLedgerFolioparticulars.
Beneficiary'sBankAccountnumber 15 ALPNUM Mandatory Alpha numericdescription
Beneficiany Account Holder's Name 40 ALPNUM Mandatory Aiphanumericdescription
SoonsorBankMicR NUM Mandatory SpnsrBankIFSC/MICR/IN
UserNumber NUM Mandatory UsernumberallottedbyNpCi
UserName/Narration 20 ALPNUM Optional Alphanumericdescription.Canbeblankorwill containNarration
10 TransactionReference 13 ALPNUM Mandatory UserdefinedReferenceNumbersuchasLedgerFolionumber,or
Share/Debenture Cert.No.or Job Card No.or any other unique
identification numbergiwenbythe Userforthe individuai
beneficiaries
Amount 13 NUM Mandatory Amountinpaise
12 Reserved(ACHitemSeoNo.) 10 NUM Optional To be Blank
13 Reserved (Checksum) 10 WON Optional TobeBlank
14 Reserved (Flag forsuccess/return) NUM Optional TobeBlank
15 Reserved (Reason Code) NUM Optionat To be Blank
Total 156
The Capital, TqT/Phone:02240009100
1001 Unit No.1001A,B Wing, /Fax:02240009101
1070 10th Floor, Plot No. C-70, -/email:contact@npci.org.in
,af , G Block, Bandra Kurla Complex, ar/Website:www.npci.org.in
Bandra(E),Mumbai 400051
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-Il FileFormat for Returns
Sr. No Field Description Length Field Mandatory/optional Remarks
lype
Settlement Date NUM Mandatory FormatisDDMMYYYY
ACHItemSeq No. 10 NUM Mandatory AcHitem SeguenceNumbertobeallottedbyNPCi
User Number NUM Mandatory UsernumberaliottedbyNpCiatthetime of Registration
Amount 13 NUM Mandatory Amount inpaise
Return Reason Code NUM Mandatory Bankto Update Reasonfornotcrediting theitem elseblank or zeroes
foraccepted records
City Code NUM Mandatory City CodeofDestination Bank MICRprovidedinINWARD file
Bank Code NUM Mandatory Bank Coceof Destination BankMiCRprovided in INWARD file
BranchCode NUM Mandatory Branch Code ofDestinationBankMICRprovided in INWARD file
Spaces ALPNUM Optional Spaces
Total 50
Annexure-III Return Reason Codes forNACHDebit
Si No NAcH Debit Return Reasons
Account Since Closed/Trasferred
No SuchAccount
Account Discriptiion does not Tally
Balance Insufficient
NotArrangedfor/ExceedsArrangement
Payment StoppedbyDrawer
Payment Stopped underCourtOrders
MandateNot Received
Miscellaneous (to be specified)
Annexure-IV File Naming Convention
Input-- ECS-DR-XXXX-XXXX123-15072015-000001-INP.txt
InwardwithFooter-ECS-DR-ABCD-15072015-000001-INW.txt
InwardwithoutFooter-RECS-DR-ABCD-15072015-000001-INW.txt
Return-ECS-DR-ABCD-ABCD123-15072015-000001-RTN.txt
Response-ECS-DR-XXXX-XXXX123-15072015-000001-RES.txt
Where XxxX would be the short code of the sponsor bank, XxxX123 would be the login id through
which the file would be uploaded.ABcD would be the short code of the destination bank and
ABCD1223 would be the login id through which the return file would be uploaded.
The Capital, r3mqT/Phone:02240009100
1001
Unit No.1001A,B Wing, a1Fax:02240009101
1070
10th Floor, Plot No.C-70, 专-/email:contact@npci.org.in
 ,f a, G Block,Bandra Kurla Complex,
aa专/Website:www.npci.org.in
Bandra (E), Mumbai 400051
CIN:U74990MH2008NPL189067
