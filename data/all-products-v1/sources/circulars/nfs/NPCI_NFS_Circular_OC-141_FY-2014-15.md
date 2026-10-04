# NFS OC 141 NFS ATM Network - Bifurcation of RC 08 processor Down

Circular/reference number: NPCI/NFS/OCNo.141/2014-15
Date: 11th November, 2014

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.141/2014-15 11th November, 2014
To,
All MembersofNationalFinancialSwitch(NFS)
Madam/DearSir,
Sub:NFSATMNetwork-BifurcationofNFSResponseCode'o8'(ProcessorDown)
Obiective:
The objective of bifurcating NFS response code'O8'(Processor Down)in the NFS ATM Network is to
enable NFs monitoring team and NFS members to identify the reason of decline i.e.whether NFs
ATM transactions are declining due to'Node offline'or due to lssuer timeout'and take appropriate
action.
ExistingProcess:
A dedicated 24*7 Helpdesk team at NPCl monitors all the transactions on NFS Network and bank
node status for each of the member banks. Helpdesk team generates alerts to member banks for
instances of technical declines observed on NFs ATM network for respective banks.It also provides
support to members for identifying and addressing any issue, so as to control transaction declines.
Major reasons of technical declines due to issue at network or application level are given below:
RC08 / Iso91-Processordown (DuetoApplication/Network issues)
RC39/ISO96-UnabletoProcess(DuetoissuesatBank'sCBS/Hostend)
Presently,in online system,if ATM transaction is declined due to 'Node Offline' (issuer unavailable)
or due to ‘Response not received from the issuer for online authorisation request sent by NpCi
(issuertimeout),theresponsecode (RC)iscapturedasO8'inNFS (ISORC'91").
Proposed changes:
The NFsresponse code ‘O8'(Processor Down)will be bifurcated into following two response codes
atNFSend:
1.Where NPClis not able to send online authorisation request to Issuer due to Node offline i.e.
Issuer is unavailable due to network or anyother issue,NFs Response code93'will be
populatedintheRawdata,STLreportand inDisputeManagement System(DMS).
However,there shall beno changes in online transactions.Banks shall continue to receive
IsoResponsecode'g1'forallsuchcases.
Page1of2
C-9,8thFloor PHTqT/Phone:02226573150
RBlPremises /Fax:02226571001
Bandra-KurlaComplex 专-a/email:contact@npci.org.in
BandraEast aa/Website:www.npci.org.in
-400051 Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

i.e. for Issuer timeout scenario, there shall be no change in the response code. Bank shall
continue to receive IsO response code'91'in online message and NFs response code 'O8"
willbepopulatedinRawfiles,STLreportsandDMS.
These changes in response codes (bifurcation into'o8'and'93)will be made only in Rawdata, STL
report and in DMs. Bank is not required to carry out any changes at their end for online transactions.
Effective Date:The above changes will be implemented with effect from 2oth November 2014.
We request you to take a note of the above and disseminate the information to the officials
concerned in youroperationsandtechnologydepartment.
Forany further clarification, we request your team to get in touch with:
Name E-mail MobileNumber
ChetanBondre chetan.bondre@npci.org.in 9819996787
AvinashKunnoth avinash.kunnoth@npci.org.in 8879772725
AbhayParekh abhay.parekh@npci.org.in 8879772794
Yours faithfully,
RamSundaresan
Head-Operations
Page2of 2
