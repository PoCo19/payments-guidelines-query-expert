# Circular No.74 - Host to Host Implementation

Circular/reference number: NPCI/2014-15/NACHCircularNo74

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2014-15/NACHCircularNo74 December23,2014
To
AllNACHMemberbanks
Host to Hostimplementation
Government of Indiahasre-launchedtheDirectBenefitTransfersforLPG(DBTL)w.e.f.November
15,2014 andthiswill be mandatoryacross India w.e.f January01,2015.The transfers will happen
on the basis of Aadhaar number as well as Account number.Member banks have been informed
of this development.NPCl, DFS and MOPNG have conducted various preparatory meetings for this.
Further Reserve Bank of India has mandated NPCl to migrate both credit and debit transactions
processed by RECS and NECS centers to NACH platform.A separate circular on the modalities for
migrationof ECS credit anddebit to NACHplatform will be issued by NPCl.
2. We are expecting many fold increase in the volume that will be routed through NACH system.
To accommodate the memberbanks we will be running multiple sessions for all the products. In
order to cope with the volume and handle such volume within the time frame stipulated for each
of the sessions it is necessary that all themember banks should have automated solution to process
both outward as well as inward transactions for all the products across NACH system. NPCI has
been advocating Host to Host functionality for this purpose.
3. Host to Host automation: Host to Host (H2H) is a mechanism which will allow seamless file
transfer between Bank and Clearing House in a secured way, which provide STP (Straight through
Processing) capabilities to participants. This will help the member banks to develop end to end
automation. The technical document released on H2H functionality requirements is attached for
your perusal. The member banks should develop H2H encompassing the following minimum
functionality
i. Auto split and merge based on the NPCl set limit
ii. Auto signing and Un-signing
iv. Seamless file transfer between Bank and Clearing house
4.Whiledeveloping the utilitymemberbanks also should take caretoensurethat thetransactions
with old account numbers are converted and posted so as to ensure that the parity of processing
is maintained with the current NEcs system for both the debit and credit transactions.
5.All the member banks are advised to take necessary steps for implementation of Host to Host
functionality for all the products of NACH and complete the same before January 31, 2015.
Thanking you
Yours faithfutly,
(Giridhar G.M.)
VPandHead-CTS&NACHOperations
Enclosure:H2HAutomated solutiondocument
-9,8 C-9, 8th Floor srr/Phone:02226573150
RBIPremises q/Fax:02226571001
Bandra-Kuria Complex -/email:contact@npci.org.in
Bandra East aa/Website:www.npci.org.in
-400051 Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
NATIONALAUTOMATED CLEARING HOUSE
Host - to -Host
AutomatedSolution

<!-- Page 3 -->

Host -to-Host Automated Solution NPCI NATIONALPAYMENTSCORPORATIONCFNDIA
Documents Details
Author NACH Technology
Published Date 28/08/2014
Version V1.0
Total Page number
Documentclassification Public
Document History
Date Version Change
Prepared By: Date
NACH Technology 28/08/2014
Reviewed By: Date
Approved By: Date
National Payments Corporation of India [Type of Document: Public] Page 2 of 9

<!-- Page 4 -->

Host-to-Host Automated Solution NPCi NATIONALPAYMENTSCORPORATIONOFINDIA
Table of Contents
1.0 Current NACH Process.
1.1 NACHFile Flow.
1.2 Bank End Activities
2.0 Host - to -Host Automated Solution....
2.1 Processforautomatictransferof files to NACH (INP/RTN)
2.2 Process for automatic transferof filesfrom NACH (INW/RES)
2.3 Other Functionalities which can be added to the Client Solution.
2.4 Advantages of Hostto Host Automated Solution
3.0 Automated file transfer model through SFTP
3.1 Security Features..
3.2 Folder Structure for SFTP.
3.3 Connection to be opened
3.4 Setting to be done at Bank End.
4.0 Bank Actionable..
5.0 Checklist for Banks..
NationalPayments Corporation of India [Type of Document: Public] Page 3 of 9

<!-- Page 5 -->

Host-to-HostAutomated Solution NPCI NATICNALPAYMENTSCCRPCRATIONOFINDIA
1.0 Current NACH Process
1.1 NACH File Flow
NACH file flow involves two parties namely Sponsor Bank and Destination Bank.Sponsor Bank
initiates a credit / debit transaction to a Destination Bank.
There are four legs to the file flowInput files (iNP) uploaded by Sponsor bank, Inward files
(INW) received by Destination bank,Return files (RTN) uploaded by Destination bank and
Responsefiles(RES)receivedbySponsorbank.
BANK INP BANG
INW
Sponsor Bank RES RTN Destination Bank
Transaction Settlement Funds made Intimation to
Initiation Presentation File Retum available the Beneficiary
Settlement Settlement
File File
Sottlement Agent Bonoficiary
Corparatos
Transaction Origination TransactionResponse
1.2 Bank End Activities
Followingarethemanual activitiesdone by thebank
Signing and Unsigning of files
Uploadingand Downloadingof files fromNACH
Authorising eachfile in NACH
Monitoring the ACK files
Voucher posting in CBS
Reconciliation
Split the INP files if it is of huge size
Merge the INW files if required
National Payments Corporation of India [Type of Document:Public] Page 4of 9

<!-- Page 6 -->

Host -to -Host Automated Solution NPCI NATIONALPAYMENTSCORPCRATIONOFINDIA
2.0 Host-to-Host Automated Solution
To overcome the above said manual activities and handle volume there is a need to implement a
client solution at bank end with the following proposed functionality
End to End automation
Auto split and merge based on the NPCl set limit
Auto signing and Unsigning
Seamless file transfer
2.1 Process for automatic transfer of files to NACH (INP/RTN)
File of any size will be uploaded to the client side solution. If the file size is greater than the
specified limit, then the solution will split the file automatically. While splitting, the split files
details and their corresponding data will be stored.
Then the solution will automatically sign the split files and push into NACH through H2H.
Authorization of files at NACH will not be required using this model.
ACK for split files will be automatically pulled by the client solution and user will be alerted in
case of any negative acknowledgement.
2.2Process for automatic transfer of files from NACH (INW/RES)
The solution will pull and unsign the Inward/Response Files. If required, then the bank can
combine the split response files using the solution.
2.3 Other Functionalities which can be added to the Client Solution
Technical Validations at the banks end, so that the rejects at NACH will be minimized
Converting Text files to XML and vice-versa, it will be useful if XML file format is
mandated.
Convert the file given by corporate to NACH acceptable format
Generate response to corporate in corporate file format if required
Generate CBS uploaded file for Voucher posting
Provide Reconciliationreport as perthe banks internal requirement
Generate MiS at the bank end itself
Handleall NACHfiles formats and functionality like bank extension, cancelation of file,
etc
IntegratewithMMS (MandateManagement System)ofNACH
This client solution will be customisable as per the banks requirement, load and environment.
2.4 Advantages of Host to Host Automated Solution
Seamless End to End Automation
Handling of Huge Volumes
National Payments Corporation of India [Type of Document: Public] Page5of9

<!-- Page 7 -->

Host -to-Host Automated Solution NPCi
NATIONALPAYMENTSCORPCRATION OF INDIA
Reduces human intervention
Increases operational convenience and transparencyfor Banks
Customizableas perbank'srequirement
Can be extended to other products like MMS and DMS, if required
3.0 Automated file transfer model through SFTP
This alternative way of automatically uploading and downloading files into NACH application
uses standard Secure File Transfer Protocol (SFTP) for secure end-to-end file transfer.
This results in lower manual intervention with higher process automation. Bank server will
connect to NPCI server and PUT signed files into the system and GET processed signed files from
theassigned folders using SFTP.
3.1 SecurityFeatures
This solution uses SFTP, a network protocol designed to provide secure file transfer and
manipulationfacilities over SSH.
SFTP server adapter will be configured at the NACH server end to facilitate SFTP with the banks
which will act as SFTP client.Authentication for SSH/SFTP connections is performed by the
exchange of session keys for the server (NACH system) and the client solution. This assures that
both parties know who they are exchanging data with.
Sequence of events for connecting & authentication for host to host communication will be as
follows:
1.Client will issue a request for connection to the server.
2. Server will respond with host signature. The client can match the host key provided
separately when establishing the connection to verify the server.
3.2 Folder Structure for SFTP
Files to beuploaded from bank (INP & RTN)will be in theroot directory("/)
Once a bank uploads a file in the root directory, NPCl server will immediately pick up
and process thefile
ACK & SFG Error messages can be downloaded from folder:"/lnbox"
INW & REs files will be available for the bank in a folder with the bank's short code.
Example:For XYz Bank, INW & RES files for that bank will be available in a folder called
"/XYZB"
National Payments Corporation of India [Type of Document:Public] Page6of9

<!-- Page 8 -->

Host -to -Host Automated Solution NPCI
NATIONALPAYMENTSCORPCRATIONCF INDIA
3.3 Connection to be opened
NACHUAT Host to Host Connection (Availableat NPCINET):
Natted IPAddress Port Server Name Comments
Server to Server connection will
192.168.179.243 9131 NACH UAT-SFG takeplacethroughthis IP and SFTp
port (9131)
NACH Production Host to Host Connection
NACH Production Host to Host Connection (Bank coming through NPClnet)
Natted IPAddress Server Name Port Comments
192.168.179.233 NACHPRSFG 9293 ForPR site
192.168.179.234 NACH HA-SFG 9293 For HA site
192.168.171.228 NACHDR-SFG 9293 ForDR site
NACH Production Host to Host Connection-(Bank coming though INTERNET)
Natted IPAddress Server Name Port Comments
103.14.161.35 NACH PR SFG 9293 For PR site
103.14.161.135 NACH HA-SFG 19293 For HA site
103.14.160.35 NACHDR-SFG 9293 For DR site
Banks can connect using DNS nameas nachh2h.npci.org.in.
3.4Setting to be done at Bank End
Setting to be done at Bank End
Step-1:
1.RUN-CMD
2.Netshinterfaceipv4show subinterfaces
3. Check MTU value
4.If Value1500goto step-2
Step-2:
To set the MTU size for the network interface, follow these steps:
1. Click Start, click Run,typeregedit, and then click OK.
2. Locate the following key in the registry:
National Payments Corporation of India [Type of Document: Public] Page 7 of 9

<!-- Page 9 -->

Host - to -Host Automated Solution NPCI NATIONALPAYMENTSCORPORATION GE INDIA
a.HKEY_LOCALMACHINEISYSTEMICurrentControlSetIServiceslTcpiplParameterslInte
rfacesl<IDfornetwork interface>
3. On the Edit menu, point to New, and then click DWORD Value.
4.Type MTU, and then press ENTER.
5. On the Edit menu, click Modify.
6.In the Value data box, type the value of the MTU size, and then click OK.
a. Value: 1300
Base: Decimal
or value:514
Base: Hexadecimal
7.Quit Registry Editor.
8. Restart the computer.
9. Restart the System
Again to do step-1 for checking MTU value
4.0 BankActionable
ImplementationofH2HAutomatedSolution
IntegrationofH2H solutionwithBank CBS
Share IP with NPCI team for opening the required connections
Opening the required connection and ports from Bank end
Class3 certificatefromIDRBTfordigital signing
Banks need to generate public-private Key pair at their end and share the Public key to
NPCI team
National Payments Corporation of India [Type of Document: Public] Page8of9

<!-- Page 10 -->

Host -to-Host Automated Solution NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
5.0ChecklistforBanks
Step Description
Status
Received an overview on Host to Host from NPCI team
Share theNPCinet IP/Static Public IP tobeused for H2H test run to
NPCIteam
Open thenecessaryconnection.
Decide an SFTP client to be used for H2H test run
Some mandatory Setting to be done at Bank end. Steps shared in
Section 3.5
First round of testing completed in NACH UAT
Generate SSH key pair and share Public key with NPCI for test run
Get Publickey of NACH system from NPCI team.
Second round of testing in UAT by logging through using ID,
Password and Private key
10 Once successful H2H test run is done, work on automation of signing
and PUT/GET to/from NACH SFTP server
11 Share the NPClnet IP to NPCI team which will be used for Production
run and also send a request for creation of H2H user
12 Open the necessary connection.
13 Setup the server and in-houseapplication to be used for SFTP
Communication
14 Generate SSH key pair and share Publickey with NPCI for
Production run
15 Complete a test run in production server by uploading a UiD Status
fileora Mapperfile
16 NACH Host to Host goes live
National Payments Corporation of India [Type of Document:Public]
Page9of 9
