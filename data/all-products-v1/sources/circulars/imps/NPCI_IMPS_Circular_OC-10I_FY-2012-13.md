# IMPS I OC 10 I FY 12-13 I Default MMID

Circular/reference number: NPCI/IMPS/OCNo.10/2012-13

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/IMPS/OCNo.10/2012-13 December4,2012
To,
All MemberandUpcomingBanksof InterbankMobilePaymentService (IMPS)
DearSir/ Madam,
Default MMID
As per the feedback received from industry,the IMps funds transfer process needs to be
simplified.One of the items identified for simplification is MMiD generation and usage.
Currently,in order to receive funds (using P2P or P2M PUSH process), or to send funds (using
P2MPULLprocess),customerneedstoprovidetheMMID.
Asper the feedback received, customer should beableto send orreceive fundsusing default
MMID. Default MMID is pre-defined number that is associated with customer's primary
account in the Bank.Customer may have multiple accounts, in which case, the primary account
shall have default MMiD,and the otheraccounts can haveMMIDas defined bythe Bank.
The changes as envisaged at the Bank end for the same are detailed in the enclosed Annexure l.
We request the Banks to implement this change, as detailed in Annexure I. This shall help to
simplifytheprocess of send/receivemoneythrough IMPS and helpin theadoption and usage
of IMPS.
Once the Bank is ready with the change,they may inform NPCl for testing and certification.
Thanking You,
Yours Faithfully,
SD/-
Ram Rastogi
Head-MobilePayments
C-9, 8th Floor r/Phone:02226573150
RBI Premises qFax:02226571001
Bandra-Kurla Complex e/emaitcontact@npci.org.in
Bandra East aawrsc/Website:www.npci.org.in
400051 Mumbai400051

<!-- Page 2 -->

Annexure
NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
1.Default MMID generation
Default MMiD that can be associated with the primary account of the customer shall be as
follows:
NBIN +'000'
Bank shall generate the default MMiD and link that with the primary account of customer at
the back-end and inform customer regarding the same.The Remitter customer should be able
to make payment to beneficiary using the default MMID or the real MMID of the Beneficiary.
If the customer uses the'Generate MMID'process or'Retrieve MMID'process, he shall get the
default MMID for the primary account and other defined MMID for other accounts.
In case customer de-registers and registers another mobile number with his bank account, the
default MMiD generated shall still be in the format defined above for the primary account.
Changes at Remitterand Beneficiary Bank
Changes required as explained above
2. Send money using default MMID of beneficiary
With default MMID implemented, even if the remitter doesn't know MMID of beneficiary
explicitly, he can initiate fund transfer request with default MMiD, in order to deposit funds to
beneficiary'sprimary account.
Changes at Remitter Bank
None
Changes at Beneficiary Bank
ProcesstransactionbasedondefaultMMIDaswell
3.Send money using IMPSmerchant payments PULLoption
Currently, in IMPS merchant payments PULL option, customer needs to enter mobile number,
MMIDandOTPatmerchantapplication.
Changes at Beneficiary Bank
None
Changes at Remitter Bank
ProcesstransactionbasedondefaultMMiDaswell
