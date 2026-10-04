# NFS OC – 416 GST Dispute Resolution in NFS BCS

Circular/reference number: NPCI/NFS/OCNo.416/2022-23
Date: 14th July
2021

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.416/2022-23 11thMay,2022
To,
All MembersofNationalFinancial Switch (NFS)
DearSir/Madam,
Sub:NFSATMNetwork-GSTDisputeResolutioninNFSBCS
In ourconstant endeavor to support members for recovery of (Input Tax Credit) ITC for non-sharing of
invoices,we are pleased to inform that we have developed a module in NFS BcS portal to raise disputes
for cases where the Payer (issuing Bank) has not received the invoices.
of invoices on Payee (Acquirer).This was alsodiscussed in GST Working Group Meeting held on 14th July
2021.The detailed process of the GST disputes is given below for reference.
1.ITCApplicability:
AsperGSTINrule,Payermemberscanclaim50%or100%of theGSTpaidasITCbasistheGSTIN
number obtained.A new menu option is created in NFS BCS portal for Payer members to update
the applicableITCfortheGSTINoftheirBankunderGSTdisputes>>ITCApplicability.This has to
be done mandatorily before the GsT disputes can be raised by the member through both the
optionsi.e.frontendandbulkupload.
Pleasenoteimportantly:
Calculationand settiementof fundswill happenonthebasisoftheITCoptionselectedby
the Payer member i.e.if a member selects 50% ITC then the disputeamount will be
considered at 50%of the GSTamount paid bythe Payersimilarly if the memberselects
100% ITC, then thedispute amount will be considered at 100%.
Memberwill beableto select the ITcApplicabilityonly oncefor a GSTiNand it shall be
applicabletoall thebankcodeshavingthe sameGSTINnumberin NFs BCS.Incaseof
changein GSTiN number,memberwill haveto submit the requestby fillingAnnexureA
gst.support@npci.org.in anddl gst@npci.org.inmail ids.Thenew GSTiNprovided will
reflect intheGSTreports forthemonth inwhichthe GSTiN is updatedandtheITCforthe
disputesshallalsobeapplicableforthemonththeGSTiNischangediritheNFSBCSportal.
2.GSTDispute
OnceITC Applicability is selected by the Payer, GST dispute can be raised for non-
receipt/incorrectGSTinvoices receivedforamonth.
Anew menu is created for raising GST disputes thru front end under the menu GST
Disputes>>GSTInvoiceSharing.
PayerwillalsohaveanoptiontoraiseGSTdisputesthroughbuikfileupload.Themenuis
availableunderGSTdisputes>GSTdispute-bulk.
1001A,TheCapital,BWing,10thFloo
BandraKurlaComplex,Bandra(E),Mumbai4ooO5
T:+912240009100F:+91224000910
contact@npci.org.in.www.npci.org.il
CIN:U74990MH2008NPL18906

<!-- Page 2 -->

Member will also have to ensure that the proper reason codes are selected while raising
the disputes.The list of reason codes isgivenbelowforreadyreference:
Codes Description
1001 Invoiceamount mismatch with GST reports
1002 Invoiceisunsigned
1003 Others
The detailed process to raise disputes through front end and bulk option is mentioned in Annexure B.
Please noteimportantly:
Members should ensure that the GST invoices shared in the NPCI GST portal (SFTP)is
checked thoroughly in all unique codes provided to the member before raising any
disputes in theNFS BCS portal.
Members can raise disputes for non-receipt of NFs invoices only and not any other
product.We will be providing a similarmodule to raise disputes for other NPCl products
in the respective back office applications.The detailed information for the same will be
communicated once the mcdules is developed for other NpCl products in the form of
circulars.
3.Disputelifecycle
The completedisputecycleandapplicableTATisgivenintablebelow:
Code GST Invoices Dispute Description Actiontakenby Expiry of TAT
TM+120days(wait
ID01 RaiseDisputebyPayer Payer period of 60 days
fromTM)
RI02 RejectionbyPayee Payee ID01+30days
A102 AcceptbyPayee Payee ID01 + 30 days
DA02 AutoAcceptancebyPayee Auto ID01+31stday
DI02 DeemedAcceptancebyPayee Auto DA02+16days
IC01 CompliancebyPayer Payer RI02+10days
IC02 CompliancebyPayee Payee DA02 +10 days
ICW01 ComplianceWithdrawal byPayer Payer IC01 + 10 days
ICWA2 ComplianceAcceptancebyPayee Payee IC01 + 10 days
ICWA1 ComplianceAcceptancebyPayer Payer IC02 + 10 days
ICP03 ComplianceCasePresentment Auto IC01/IC02+11thday
IVD03 Verdict infavourof PayerbyNPCI for NPCI ICP03+30days
InvoiceSharing
Verdict infavourof PayeebyNPCI for
IVD04 NPCI ICP03 +30days
Invoice Sharing

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Pleasenoteimportantly:
"TM"istransaction month.
Exampleto raiseID01:IfTMisJan'22,disputefor Jan'22 can be raised in Apr22and
May'22,
4.Mappingof rolefor GSTDisputes:
New User role module is created for GST disputes. Admin User will have the option of
assigning the role to the existing Users.
TheMemberAdmin canalso createnewMakerand Checkerforraising GSTDisputes in the
NFS BCSportal.
The system is expected tobeavailable for members from 25thMay,2022onwards.We will broadcast the
go live date in news/alerts in NFS BCS portal. Members are required to make necessary changes at their
end to read the NTSL files in case of a GST dispute.The details of the dispute resolution process are given
below in Annexure B for reference.
Please make a note of the above and disseminate the instructions contained herein to the officials
concerned.
Foranyqueriesorclarifications,pleasecontact:
Name e-mailID MobileNumber
SwapnaliWaydande swapnali.waydande@npci.org.in 8657997883
TejasviShirsat tejasvi.shirsat@npci.org.in 8879754909
Yours faithfully,
N.WS
SaiprasadNabar
Chief-OnlineProducts Operations
Encl:1.AnnexureA-GsTRegistrationDetails
2.Annexure B-Disputeresoluticn process

<!-- Page 4 -->

AnnexureA
GSTRegistrationdetails
(Onmember'sletterhead)
Nameofthemember:
GSTIdentificationNumber(GSTIN)/
PAN (Optional) TAN(Optional)
ProvisionalID
Address of principal placeof business inthe Stateas per GsT registration
AddressLine1
AddressLine2
AddressLine3
City
State
Pin code
ITcApplicabilityRate(Vtickanyonewhicheverisapplicable)
RateofITCApplicability 50% 100%
Product&Services(Vtickwhicheverisapplicable)
The abovegivenGSTINdetails is applicable forall Product and Services availed byus fromNPCl
OR
CTS CTS CTS IMPS Anynew
RuPayPOs
NFS Western Northern Southern /NUUP NACH AePS NETC product /
&E-Com
Grid Grid Grid /UPI service
** If GSTINis same for all the products,kindly tick (V)on“All Products and Services".If thereare separateGSTINfor
is ticked, it will be assumed that the given GsTiN is same for all the.products and services.
Date:
(AuthorizedSignatory)
Name&Designationofthesignatory:
BankName:
(RubberStamp)

<!-- Page 5 -->

AnnexureB
Disputeresolutionprocess
i. Disputeraisingthroughfrontend:
a.User to select"Payer"role for raising a dispute for non-receipt of GST invoices. The system
will check if the ITC applicability for the GSTIN has been updated.If it is not updated, maker
will be prompted to update the ITC applicability under"ITCapplicability"menu to continue.
Payercan proceedto raisea disputeonlyafterupdating theITCapplicability.
b. GsT Disputes will have maker and checker roles for raising disputes through front end.To
retrieve the transaction details the Maker will have select GST Invoice Sharing under GST
Disputes option.The following fields have to be selected while raising a dispute:
Fields DropdownOptions Field selection
Role Payer Mandatory
Payee
2monthscalendarwill bedisplayedpriortothe
Period current month Mandatory
ATM
ICD
Product Mandatory
DFS
JCB
Listofall memberswithwhomthetransactions
Bank have happened Optional
Listofalldisputes(DisputeLifecycleinpoint3of
OptionalforPayerrole
Dispute the circular) MandatoryforPayeerole
Pleasenoteimportantly:
The GST amount will be displayed on the screen as perthe ITC applicability selected bythe Payer
and it shall be considered for all calculations of GsT disputes. This field shall be editable for the
Payer for raising the first dispute only (IDO1). This is provisioned for cases where the invoice
amountisnotmatchingwiththeNPCIGSTreports.
Thedetailed process to raise disputes through front end isgiven in Fig 1.1 to 1.7.

<!-- Page 6 -->

Logof
NFS
NATIONALFINANCIALSWITCH
BharatClearing&Settlement Welcome:HDFCPLSMaker01/Friday,April292022
Hometransactions GSTdisputon Reports Download BukUpload Membor Management MISReports- FreguentChargeback Doauments
GSTDispute Search
Role Payer Period 01/01/2022 Product ATM
Bank --Seiect.. Dispute Select
(Chooseanydateonmonth-in.Periodfield)
Search Ctear
Fig.1.1
The User will have to click on the dropdown available on the top right corner to raise the next
levelofdisputeasshowninFig1.2andFig1.3.
Logc
NFSI
NATIONALFINANCIALSWITCH
BharatClearing&Settlement Welcome:HDFCPLSMakero:11Tuesday,April26,202
Home-TransactionsGSTdisputes ReportsDownload BuikUpload+ MembetManagementirMiSRepofts hFrequentChargeback Documents
Transaction Summary Backto GsTDisputeSearct Refresh Expon Select-
Payer Bank Name: Payee Bank Name:
Payer Bank Code: Payee Bank Code:
Payer GSTIN Number: Payee GSTIN Number:
PayerITC applicablity%: Month:
Amountpaid: GsTamount:
TraneanrinnllfeCvnle
Fig.1.2
Logo
NFS
NATIONALFINANCIALSWITCH
BharatClearing&Settlement Welcome:HDFCPLSMakero1a1Tuesday,April26,202:
Hone Transactions GSTdisputes ReportsDownload Bulk Upload- MemberManegement MISReporsy Frequent Chargeback Documerta
TransactionSummary BacktoGsTDisputeSearch Retresh Export
PayerBank Name: Payee Bank Name: C2290010-Sub of Raise DisputebyPayer Seiect-
Payer Bank Code: Payee Bank Code:
Payer GSTIN Number: Payee OSTIN Number:
PayeriTcapplicability%: Month:
Amountpaid: GsTamount:
Transaction Life Cycle
Fig.1.3
The dispute amount willbeeditable only fordispute raisedby payer.The amount will be editable
to the extant of iTC applicability.Amount entered more than the system calculated amount, the
systemshall notacceptthedispute.

<!-- Page 7 -->

Ralse Dispute by Payer
NATIONALFINANCIAA
TotalGSTamount 157.68 "Message ReasonCode -Seiect.. Tuesday.Aprl25.
Home 福Transacbans Amount,Dispute 157.68
Member Message Text
TransactionSumma eDiaputebyPayer
Payer Bank Name:
Payer Bank Code:
Payer GSTIN Number: PayeriTcapplicabllity  Cunce Clear.
Amountpald:
Transaction Life Cyele
Fig.1.4
The User will have to select one of the reasons given in the table below while raising a dispute
first time mandatorily. For all other lifecycles, the same will be in a non-editable format.The
reasoncodesforGsTdisputeraisewill beasbelow:
Codes Description
1001 InvoiceamountmismatchwithGSTreports
1002 Invoiceisunsigned
1003 Others
All fields are mandatory while raising dispute through front end. The dispute has to be approved
by the checker.
Checker Role: Once the maker raises the dispute through front end, checker will be able to
approve/reject the same through the menu option"GST DisputesGST Dispute Approval".Checker
can select multiple entries by selecting the check boxes and approve/reject or select an individual
entryand approve/reject.“Export"option is available to the checkerto download the details as per
thesearchcriteria.
The checker will have a filter option to select from the list to approve/reject/pending entries along
withdisputeraiseddateasshowninFig1.5
Logott
NFS
NATIONALFINANCIALSWITCH
BharatClearing&Settlement Welcome:HDFCPLSCheckero11Tuesday,Aprll26,2022
HomeriaTransactonsi- GSTdisputes iReports Downioadiy MemberManagement MisReportsaFreguentChargeback- Documents
ITcApplicabiltyApproval
From Raise GSTDisputeApproval
Date
Approval Submitteef
Status
Search EodoeDate Clear
Excel
Month Payer Bank Payee Bank AmountPaid CGSTAmount SGSTAmount IGSTAmount Total GST
012022 HDFC2400001-HDFCB ank iCIC2290010-Subofic4 INR876.00 INR0.00 INR0.00 INR157.68 INR157.68
012022 yue HDFC2400001-HDFCB 123 ICiC2290006-Subofsb INR867.00 INR0.00 INR0.00 INR156.06 INR156.06
Fig.1.5

<!-- Page 8 -->

On selectingan individual entry,thefollowing screen will be displayed.User will have to click on
thedesiredtransaction lifecycletoapprove/rejectthedispute.
Transachon Detal
NATIONAL FINANCI
Transaction Summary Expon uesday.April26,202
Payer Bank Name: Payee Bank Name:
Payer Bank Code: Payee Bank Code:
Payer GSTIN Number: Payee GSTIN Number:
FromRaise Payer ITC applicability%: Month:
Date Amount pald: GSTamount:
Approval
Status Transaction Life Cycle
>RalseDisputebyPayer(Pendingapproval).Ouitward
OExport
Month TotalGST
Fig.1.6
NATIONALFINAN
Transaction Summary Export ednesday.4pr27.2022
Payer Bank Name: Payee Bank Name:
Payer Bank Code: Payee Bank Code:
Payer GSTIN Number. Payee GSTIN Number:
FromRalse Payer ITC applicability%: Month:
Date Amountpaid: GsTamount:
Approval
Status Transaction Life Cycle
>Baiac.Diaputehy.PaystiPanding.anrraxal)-stncd
DExport
Reason Code Description ClaimAmount
Monts Document indicator TotalGST
MemberMessage Text Reference Number
912022 Raise Date and Time SettiementAmount INR157.68
012022 Currency Code.Sattiement CheckerUser Name INR158.00
Maker User Name
SeeFees
Approva
Fig.1.7
When the dispute is approved by the checker, a unique 18-digit reference number will be generated and
will be a part of the complete dispute cycle.A separate dispute report shall be provided for GsT disputes
and it shall havethisuniquenumberagainstthedisputes details.
ii. DisputeRaise-BulkUploadFiles
Members can use bulk upload menu forraising multiple disputes fornon-sharing of invoices by
clickingon"GSTdispute-bulk"menuunderGSTdisputes.
2. Bulk upload file is a 2 step process, i.e.uploading the file in the required format and staging the
file.
3. To check the status of all records staged, theuserhas toclick on the staged file.
4. Once thebulk file is processed, the approvedand rejected entries will be displayed on the screen.
5. Thefileformat for raisingthebulkdisputeforthe first dispute IDo1is given below:

<!-- Page 9 -->

PayeeBank Dispute GST Dispute Transaction Reason
code amount Type Product month Code
Thedetailstobeupdated ineach fieldisgiveninthebelowtable:
MenuOptions Description
PayeeBank code NFSBankCodeavailableintheBankwiseGSTreport
Dispute GSTamount GSTamounttotheextantofiTCapplicability
GSTDisputeTypereferthedisputecodementionedinpoint3
Dispute Type
ofthecircular
Product ATM,CD,DFS,JCB
Month inwhichtransactionwasprocessed intheformat
Transaction month
DDMMYYYY
Reason Code GSTreasoncodesmentionedinpoint2ofthecircular
Please note importantly:Reason code is a mandatory field for a fresh dispute raised.For dispute
lifecycle continuation, the reason code shall not be a part of the bulk dispute file.The entry will
be rejected in case any of these validations fail with the reject reason“Error -reason code
validation failed".
ii. Document Upload:
Documentupload ismandatoryinbelow stages ofthedisputes:
Rejection of a dispute
Complianceraisedbyboththemembers (within7dayspostraising compliance)
iv. Fees and Charges:
A compliance fee of INR 150O + GST will be charged to the member against whom the decision will be
given.
Thefund movement in case of verdict will be as mentioned inthe tablebelow:
Complianceraised by Decisioninfavourof Debit Credit
Payee-claim Payer-claim amount
Payer
Payer amount+1500+GST NPCI-1500+GST
Payee Payer-1500+GST NPCI-1500+GST
Payee-claim Payer-claimamount
Payer
Payee amount+1500+GST NPCI-1500+GST
Payee Payer-1500+GST NPCI-1500+GST

<!-- Page 10 -->

V. Changes inDaily/Monthlyreports
a. DSR Report
A new line itemGSTDisputeDetails shall be created in the DSR for GST disputes.This shall be a
dynamic entry and shall be captured whenever the fund movement happens.This shall be due
to acceptance/deemed acceptance and compliance decision of the GsT disputes.Members shall
makenoteof thisand makenecessarychanges attheirend.
Dispute DSRDescription
GSTDisputeAccept Penalty for non-compliance of Invoice sharing
from/to<Bankcode>
Deemed acceptance of penaltyfornon-
GSTdisputeDeemedacceptance compliance in Invoice sharing from/to<Bank
code>
Complianceacceptancepenaltyfornon-
GSTcomplianceaccept compliance of Invoice sharing from/to<Bank
code>
Compliance Penaltyafterverdict fornon-
GSTverdictfundmovement complianceofInvoicesharingfrom/to<Bank
code>
b.Cycle/Daily/MonthlyDisputeReport:
The reports forGST disputes aregiven belowwith the frequencyand location:
Report Frequency Path
Bank ReportsDownload>>File
Code_GST_DisputeReport_Product_DDMMYYYY_ Cycle wise Download>>GST_Reports
Cycle folder>>Month>>Date>>Cycle
ReportsDownload>>File
Bank Download>>GST_Reports
Code_GST DisputeReport Product DDMMYYYY Daily folder>>Month>>Date>>Cycle1
ReportsDownload>>File
Bank Download>>GST_Reports
CodeGSTDisputeReportProduct_MMYYYY Monthly folder>>Month>>YYYY-MM-00
TheFileformatforthedisputereportisgivenbelow:
Adj Pa
dat Adjt Adjt AdjDesc Reaso Cy Pa ye Invoice Adj NPCI NPCI TATExpi
ime ype ription ncode cle yer Month Amt Fee GST ryDate
