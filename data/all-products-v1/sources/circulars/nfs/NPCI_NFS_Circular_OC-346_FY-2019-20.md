# NFS OC 346 Encrypted files in DMS

Circular/reference number: NPCI/NFS/OCNo.346/2019-20
Date: 30th September, 2019

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.346/2019-20 30th September, 2019
To,
All MembersparticipatinginNFSATMNetwork
Madam/DearSir,
Sub:NFS ATM Network- Encrypted exchange of files in DMS between NPcl and
members
NPCl and members exchange files through back office system (i.e. DMS) for reconciliation,
settlement and dispute processing.NPCl will use PGP encryption standards to encrypt files
(containing Pll data) exchanged between NPCl and NFS members, so as to ensure that data is
protected.
PGPEncryptionOverview
PGP is an encryption program that provides cryptographic privacy and authentication for data
communication. PGP is used for encrypting and decrypting files which will be shared between
NPClandmembers.
Public and Privatekeys play a vital role in PGP to encrypt and decrypt the data.Public key is
used to encrypt the data and private keys are used to decrypt the data.NPCl will share the tool
for PGP encryption / decryption.
Thefollowing diagrams showtheencryptionand decryption process:
Sharingofsettlementfiles/adjustmentreports
EncryptFile
Encrypted
WwithNPCI DMS/SFPT
NPCIFiles File
PublicKey
Decryptfile
Encrypted
DMS/SFPT byNPCI
File NPCIFiles
PrivateKey
1001A,TheCapital,BWing,1othFloor,
BandraKurlaComplex,Bandra(E),Mumbai4ooO51.

<!-- Page 2 -->

UploadingofdisputefilesbyMembers
Member EncryptFile Encrypted
DMS/SFPT
Files withMember File
Public Key
Encrypted Decryptfile Member
DMS/SFPT
File by Member Files
Private Key
ChangesapplicabletoMembers
The PGP tool for file encryption / decryption will be placed in respective member's folder in DMS
system under thepath Info>>> ImportantdocumentswiththeURL-<Bank
code>_PGP_Encryption_Tool.zip.Members shall download and access the exe format file -
PGPEncryption.exe to encrypt / decrypt the settlement and disputes/adjustment files.
NPCl will be sharing files with Pll data encrypted under PGP algorithm. Members need to
download the files from DMS, decrypt using the PGP tool and then take it for further processing
internally. Similarly, members will encrypt the files containing Pll data with PGP tool and then
upload the file into DMs in case of uploading dispute/adjustment files.
This change is applicable for Interoperable Cash Deposit (ICD), DFS & JCB/CUPI settlement
reports also. Please refer to Annexure A for list of files generated in DMS which will be
encrypted.
Implementationdate:
TheprocessofPGPencryptionwillbeimplementedfrom16thOctober,2019.
Please make note of the above and disseminate the instructions contained herein to the officials
concerned.
Foranyqueries orclarification,pleasecontact:
Name e-mail ID MobileNumber
Sarit Das sarit.das@npci.org.in 8108108694
AvinashKunnoth avinash.kunnoth@npci.org.in 8879772725
Yours faithfully,
S-MNa 6
SaiprasadNabar
ChiefOnlineProductOperations
Encl:1.AnnexureA-ListofNFSsettlementfiles/reportstobePGPencrypted

<!-- Page 3 -->

AnnexureA
List of NFS settlementfiles/reportstobe PGPencrypted
NFS
FileDescription Filename
Raw Data NFSRawData<BANK CODE><DDMMYY>_1C zip.pgp
STL File NFSSt<BANK CODE><DDMMYY>1C zip.pgp
NTSL File NTSL<BANK CODE><DDMMYY≥ 1C xIs.pgp
LateReversal File VerifReversalTrans<BANKCODE><DDMMYY>zip.pgp
VerafNerif Veraf&Verif<BANKCODE><DDMMYY>_1C zip.pgp
Adjustment reports asperreportgenerated
FCQMBulkUpload as definedbyUser
DisputeBulkUpload asdefinedbyUser
SDMTBulkUpload asdefinedbyUser
ICD
File Description File name
Raw Data NFSRawData<BANKCODE><DDMMYY>CDzip.pgp
STL File NFSStI<BANKCODE><DDMMYY>CD_zip.pgp
NTSLFile NTSL<BANKCODE><DDMMYY>_CD_xIs.pgP
Adjustmentreports as per report generated
Dispute BulkUpload asdefinedbyUser
DFS
FileDescription Filename
Raw Data DFSRawData<BANKCODE><DDMMYY≥_zip.pgp
STL File DFSStI<BANKCODE><DDMMYY≥_zip.pgp
NTSLFile DFSS<BANKCODE><DDMMYY>_xIs.pgp
Adjustmentreports asperreportgenerated
JCB/UPI
File Description Filename
RawData JCBRawData<BANKCODE><DDMMYY>_zip.pgp
STLFile JCBStI<BANKCODE><DDMMYY≥_zip.pgp
NTSLFile UPIS<BANKCODE><DDMMYY>_xIs.pgp
Adjustmentreports asperreportgenerated
DisputeBulkUpload asdefinedbyUser
