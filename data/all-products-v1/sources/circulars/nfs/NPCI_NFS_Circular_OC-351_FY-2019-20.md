# Circular 351 - NFS ATM Network - Encrypted exchange of files in DMS between NPCI and members

Circular/reference number: NPCI/NFS/OCNo.351/2019-20

<!-- Page 1 -->

NPC
NATIONALPAYMENTSCORPORATIONOFINDXA
NPCI/NFS/OCNo.351/2019-20 16thOctober,2019
To,
AllMembersparticipatinginNFSATMNetwork
Madam/DearSir,
Sub:NFSATMNetwork-EncryptedexchangeoffilesinDMSbetweenNPCIandmembers
WerefertoNFSOCNo.346dated30thSeptember,2019onencryptionoffilesexchangedin
DMSbetweenNPCIandmembers.
Pleasebeinformedthat wehaveplacedPGpEncryptiontool inDMSforyourreference.The
tool can be usedfor encryption or decryption of fileshaving sensitive information.Go-live date
is16thOctober,2019as advisedthroughOCNo.346.
Steps to be followedfor accessing PGP tool for encryption/decryption of NFS settlement and
disputes/adjustmentfilesareprovidedinAnnexureA.
Please make note of the above and disseminate the instructions contained herein to the
officialsconcerned.
Foranyqueriesorclarification,pleasecontact:
Name e-mail ID MobileNumber
ImranPatni imran.patni@npci.org.in 9821599440
SaritDas sarit.das@npci.org.in 8108108694
AvinashKunnoth avinash.kunnoth@npci.org.in 8879772725
Yoursfaithfully,
GiridharGM
Chief-Offlineproductoperations&technology
Encl:1.AnnexureA-StepsforaccessingPGPEncryptionTool
1001A, The Capital, B Wing,10th Floor,
BandraKurlaComplex,Bandra(E),Mumbai4ooO51.
T:+912240009100F:+912240009101www.npci.0rg.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
AnnexureA
StepsforaccessingPGPEncryptionTool
DownloadingofPGPTool
a.Go to the path Info >>> Important Documents in DMS and download the file ‘PGP
EncryptionTool.zip'.
b. Unzip the tool using password npci@123 and install the tool in your system.
DownloadingofPrivateandPublicKeys
a.GotothemenuoptionPGPToolkit>>>PGPKeyand download belowgivenPrivate&
Public key files by right clicking on the link and select the 'Save as' option to save the
files inyoursystem.
i.XxX-PKey_PrivateKey.txt (XXXisyour3characterbankcode)
ii.XXX-PKey_Publickey.txt (xxXisyour3characterbankcode)
b. Members shouldplace the Private and Public Keyfiles in the unzipped folder of PGP
EncryptionToolandmakethefollowingchanges:
i. Edit (open with notepad)the file name:PGPEncryption.exe.config and replace the
line<add key="PKeylD"value=""/>with<add key="PKeylD" value="xxx"/>
whereXxxisyour3characterbankcode&savethesame.
i.Edit (openwithnotepad)filename:PGPEncryption.vshost.exe.config and replace
the line<addkey="PKeylD"value=""/>with<addkey="PKeylD"value="xxx"/>
whereXxXisyour3characterbankcode&savethesame.
Pleasenote that the above changes areone timeactivityfor running thePGP Encryption tool.
After completion of above given stepsfor accessing PGP Encryption Tool,members should
followthestepsgiven inNFSOC.346forencryption/decryptionof thefiles.
1001A,TheCapital,BWing.1o"Floor,
BandraKurlaComplex,Bandra(E),Mumbai4oO51.
T:+912240009100F:+912240009101www.npci.0rg.in
CIN:U74990MH2008NPL189067
