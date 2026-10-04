# NPCI 2016-17/CTS/029 - Advisory note - Enable secure communication between CH and CHG - All

Circular/reference number: NPCI/2016-17/CTS/029

<!-- Page 1 -->

NP
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2016-17/CTS/029 April.26, 2016
To
AllCTSMemberBanks
EnablesecurecommunicationbetweenCHandCHG
We refer to the 18th Steering committee meeting held on January 19, 2016, where the
solution for using secure FTP (SFTP) communication between CH and CHG was proposed.
The advisory note on the same is provided in annexure I.
Yoursfaithfully
GiridharGM
(VP & Head Operations-CTS and NACH)
1001A,Bwing,10thFloor,TheCapital, Bandra-KurlaComplex, Bandra (East),Mumbai-400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NATICNALPAYMENTSCORPORATIONOFINDIA
Annexure-1
AdvisoryNote
EnableSecureCommunicationbetweenCHandCHG
Introduction:
In existing ECPIX System,weare usingFTP (FileTransferProtocol)forFiletransferbetween
CH and CHG.FTP is an unsecured protocol and was not designed to be a secure protocol,
and has many security weaknesses. In order to enable secure Communication we recommend
touse SFTP (securefile TransferProtocol)between CHandCHG.
SFTP:(SSHFile TransferProtocol,or SecureFile TransferProtocol)
SFTP, which stands for SSH File Transfer Protocol, or Secure File Transfer Protocol,is a
Advantageof SFTPoverFTP:
The major differencebetween FTP and SFTP is Uploaded files may be associated with their
basic attributes, such as timestamps. This is an advantage over the common FTP protocol,
which does not have provision for uploads to include the original date/timestamp attribute
without help.
EnableSecureCommunication betweenCHandCHG
Files can be transferred securely between CH and CHG using SFTP. The system is enhanced
to incorporate secure FTP in addition to the existing FTP for file transfer.The system allows
you to choose whether to use FTP or secure FTP (SFTP) to transfer files from CH to CHG or
from CHG to CH.
SystemRequirement:
1. In order to implement secure file transfer using SFTP, ensure that Ws_FTP 7.6.3 or
higher version must be already installed on the SsH enabled server.
Windows Server 2008 at the CHand CHG.
ParameterSetting:
After achieving above system requirement, CH operator needs to set the required
parameters at CH to enable SFTP communication between CH and CHG
CommercialsforWSFTPWITHSSHlicense
Option 1:Banks having existing license from NCR can do only Upgrade -APTRA Clear IPSwitch
WSFTPServer-UpgradetoSSH
Upgrade license Unit Price with one year support: Rs.46, 000/- (Rupees Forty Six
Thousand Only)
1001A, Bwing,10thFloor, TheCapital, Bandra-Kurla Complex, Bandra (East),Mumbai-400051
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
Option 2:Banks requiring New licenses -APTRA Clear IPSwitch wS FTP Server SSH
NEw license Unit Price with one year support: Rs.66, 000/-(Rupees Sixty Six Thousand
Only)
Implementation effort is ONE DAY per Grid provided CHI is remotely accessed by NCR.
ImplementationchargeswouldbeRs.20,000/-perGrid.
Contactperson
Member banks willing to upgrade from FTP to SFTP can contact the below SPOC from NCR.
S.No Name Contact Number E-mailid
BrijeshMishra 9819181250 Brijesh.Mishra@ncr.com
1001A, B wing,10th Floor,The Capital, Bandra-Kurla Complex, Bandra (East), Mumbai-400 051
CIN:U74990MH2008NPL189067
