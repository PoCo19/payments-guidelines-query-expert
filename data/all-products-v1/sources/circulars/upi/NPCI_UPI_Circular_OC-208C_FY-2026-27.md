# UPI | OC No. 208C | FY 2026-27 | (Addendum to OC 208, 208A & 208B) - Implementation of NRP & PRD process & arbitration guidelines

Circular/reference number: NPCI/UPI/OCNo.208C/2026-27
Date: 30th June 2025

<!-- Page 1 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/UPI/OCNo.208C/2026-27 Apr 23, 2026
To,
All Members of Unified Payment Interface (UPl)
Subject: Addendum to OC 208, 208A & 208B-Implementation of NRP & PRD process
& arbitration guidelines
Reference may be drawn from NPCI/UPI/OC No. 208/2024-25 dated 03rd Oct 2024,
NPCI/UPI/OC No. 208A/2025-26 dated 30th Jun 2025, and NPCI/UPI/OC No. 208B/2025-26
dated 01st Aug 2025, wherein it was communicated that, until the automation process is fully
completed for NRP & PRD process, the existing manual procedure will continue to be followed
(refer Annexure-D, Point No. ili of NPCI/UPI/OC No. 208A/2025-26 dated 30th June 2025 for
details).
1. In view of the above, NPCl is introducing a new functionality in URCS that enables the
bulk upload and download of evidence for all the users. A comprehensive process for using
the bulk evidence upload & download features along with the rules to be followed has been
detailed in Annexure-1.
2. In addition to the above, upload evidence option through URCS front end is enabled for
the below dispute stages on both approved and deemed approved transaction.
a. Chargeback Raise
b. Deferred Chargeback Raise
Pre-Arbitration Raise
d. Deferred Pre-Arbitration Raise
e. Wrong Credit Chargeback Raise
Go-Live: The above-mentioned changes will be implemented in URCS with effect from 26th
May 2026.
3. To facilitate swift resolution of the dispute, NRP verdict will be rendered exclusively based
on the evidence provided during the chargeback and pre-arbitration stages. This process
will be applicable from 26th June 2026.
It may be noted that the evidence upload shall be allowed only up to Pre - Arbitration
stage. Banks should ensure that all the available I necessary evidences are submitted
well before Pre - Arbitration stage. System controls shall be implemented in URCS to
disable upload of evidence at all arbitration stages effective from 26th June 2026.
1001A, The c, ving, 10th Fl00r,
BandraKurlaComplex,Bandra (E),Mumbai400O51.
T:+912240009100F:+912240009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-2 can be referred for details of the dispute flags for which evidence upload
through bulk mode and front end is available.
4. Rules for Pre-Arbitration Raise & Upload Evidence:
a. Remitter Bank Responsibility - The remitting bank should raise a Pre-Arbitration only
after the expiry of the TAT of A+2 days, where A is the dispute raised date, provided
that the beneficiary bank has not upioaded any evidence or has uploaded invalid,
illegible, incorrect evidence. This provision is intended to ensure that the beneficiary
bank is afforded adequate opportunity to upload complete and valid evidence through
bulk within the prescribed TAT.
b. Beneficiary Bank Responsibility - The beneficiary bank should mandatorily upload all
supporting valid evidence within a TAT of A+1 day for the re-presentment of a
chargeback or re-presentment of a pre-arbitration to avoid further dispute lifecycle.
Refer Annexure-1, Point 5 which provides illustration table for A+1 & A+2 day TAT.
Note: The existing dispute rules in URCS remain unchanged; the above changes are
provisioned exclusively for bulk evidence upload and download functionality.
5. Repository of Evidence: Ensure that all evidence is downloaded on daily basis and stored
systematically with an appropriate backup mechanism to maintain a proper repository for
future reference.
6. Retention period for accessing the bulk evidence: Users can download evidence in bulk
from URCS up to 30 days.
Yours sincerely
SD/-
Giridhar GM
Chief--CustomerSuccess
Enclosed:
Annexure - 1: Key Points
Annexure - 2: Dispute Stages Eligible for Evidence Upload
Annexure - 3: User Manual
1001A, The CaPR, B/Wving, 10th Fl00r,
Bandra Kurla Complex,Bandra (E),Mumbai 4o0051.
T:+912240009100F:+912240009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure --1: Key Points
Bulk evidence upload feature
1.Dispute batchID wise Bulk Evidence Upload in URcsBack-Office
1. After the bulk dispute file (.csv) is successfully processed in URCS, the "Upload
Evidence" option is available for users alongside the respective dispute batch ID
in URCS.
2. User should place all relevant evidence documents in a single folder, compress
and upload exclusively in .ZiP format. Other archive formats such as .7z, .TAR,
.RAR, etc., are not permitted by URCS.
3. The maximum allowable zip folder size for bulk evidence upload is 50 MB.
4. For batch IDs with large number of disputes, users are advised to split the evidence
and upload in multiple frequencies (e.g., Batch ID of 5000 disputes, split the
evidence into parts based on file size and ensure the zip folder size is not more
than 50 MB).
2. Evidence Filename Specification
1. URCS generates a unique Adjustment Reference "Adjref" for all adjustments that
are raised and successfully settled irrespective of raising partial chargebacks/ re-
presentments etc. by users. This reference is updated in the existing column Adjref
of the adjustment report. E.g.: HDF_CSB_Arbitration Raise_1253689856
2. Users must use URCS-generated Adjref (not Bankadjref) when naming evidence
files, as URCS uses this value to map the evidence to the respective dispute.
3. Each evidence file must not exceed 1 MB. Larger files will be rejected while the
remaining valid files will continue to process.
4. Permitted file formats are .pdf, .doc, .docx, -png, jpg, .xls, .xlsx only.
Note: Text content in .doc, .docx, .xls, .xlsx is not accepted as valid evidence
These formats must contain images/proper proof/justification for rejecting the
dispute.
5. Only one evidence document can be uploaded per dispute in bulk mode. If the user
has multiple or large size evidence documents for the same dispute, they must
combine them into a single document and convert it into PDF or any other allowed
file format as mentioned above. If the same is not possible, the bank may choose
to do both dispute raising and evidence upload from front end option.
1001A, The C,/ving, 10th Flo0r,
Bandra Kurla Complex,Bandra (E),Mumbai 400 051.
T:+912240009100F:+912240009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 4 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
3.Maker-CheckerWorkflow
Bulk evidence upload is a mandatory maker & checker process. Refer Annexure-3 for
user manual.
1. After adjustments are raised and settled, users must extract the 'Adjref values from
the report and rename evidence files accordingly.
2.  The maker should upload dispute batch ID-wise bulk evidence into the URCS.
3. URCS then moves the reguest to the Checker tray, who must log in URCS, access
“"Bulk Evidence Approval" menu option and approve the evidence submissions.
4. Rejection Reason Codes
1. Once maker & checker process steps are completed, URCS displays completion
status of each evidence irrespective of URCS accepted or rejected them.
2. Rejected evidence will appear as ‘Rejected' along with the corresponding reason
code and description. The user must resolve the issue and reupload the evidence
by following the same process.
Rejection Reason Code Rejection Reason Code Description
BE1 Mismatch with adjustment record
BE2 Incorrect naming convention
BE3 Invalid file format
BE4 File already accepted
BE5 File size exceeds limit
BE6 Evidence not allowed for this adjustment type
Evidence that is successfully processed will appear as 'Accepted' and the reason
code fields will remain blank since no issues were encountered.
5. TATforBulk Evidence Upload
1. Bulk evidencemust be uploadedwithin A+1 day,whereAis thedispute raised date.
2. URCS will not allow any evidence which are attempted to upload after the TAT.
3. The sample table below illustrates the cut-off timelines:
1001A, The c品,wing, 10th Floor.
Bandra Kurla Complex, Bandra (E), Mumbai 400 051.
T: +91 22 40009100 F: +9122 40009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 5 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Particulars Day
Dispute Raised date (A) Monday, 15:00 hrs (example time)
TATs
Upload Cutoff date (A+1) Tuesday, 24:00 hrs
TAT Expiry From Wednesday, 00:01 hrs
timelines.
Bulk evidence downloadfeature
1. Frequency of Staging the Evidence in Folder
1. For the disputes raised in URCS through bulk/front-end option on day A+O and its
evidence uploaded by the users on day A+0 or latest by A+1 (A indicates dispute
raise date), URCS will compile and stage all evidence on A+2 day.
Example: If disputes are raised on Monday and the corresponding evidence is
uploaded on Monday or Tuesday, the evidence folder will be made available for
banks to download on Wednesday morning
2. 
containing all evidence of disputes raised and received by banks as a
Remitter/lssuer and BeneficiarylAcquirer. Users can download the folder from the
Evidence File'. By default, URCS will generate evidence folder every day. If the
shall get generated.
3.The evidence folder shall be encrypted in PGP format.
2. Naming Convention for Evidence Folder
The folder structure will follow the format below (XYZ is sample bank code). Users can
download evidence in bulk from URCS up to 30 days.
Master Folder Folder Sub Folder
XYZ DDMMYYYY XYZ.REM_DDMMYYYY_DC1.zip
_DC1.zip XYZ_BEN_DDMMYYYY_DC1.zip
Evidence_XYZ
DDMMYYYY.zip XYZ_REM_DDMMYYYY_DC2.zip
XYZ DDMMYYYY
_DC2.zip XYZ_BEN_DDMMYYYY_DC2.zip
1001A, The Capag, B/6Ving, 10th Floor,
BandraKurlaComplex,Bandra(E),Mumbai400051.
T: +91 22 40009100 F: +9122 40009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 6 -->

NPCIN
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure-2:Dispute Stages Eligible for Evidence Upload
Dispute Adj Flag FrontEnd Upload Bulk Upload
Chargeback Raise Yes Yes
Deferred Chargeback Raise FB Yes Yes
Re-presentment Raise Yes Yes
Deferred Re-presentment Raise FR Yes Yes
Pre-Arbitration Raise Yes Yes
Deferred Pre-Arbitration Raise FP Yes Yes
Pre-Arbitration Declined PR Yes Yes
Deferred Pre-Arbitration Declined FPR Yes Yes
Arbitration Raise AR No*** No***
DeferredArbitration Raise FAR No*** No***
Arbitration Continuation ACC No*** No***
Fraud Chargeback Raise FC Yes Yes
Fraud Chargeback Representment FCR Yes Yes
Wrong Credit Chargeback Raise WC Yes Yes
Wrong credit Representment WR Yes Yes
*** Evidence in the arbitration stages will be considered up to 1 month from the go-live
date 26th May 2026 as mentioned above in page 1 point no. 3.
1001A, The C昂,@@Ving, 10th Floor,
Bandra Kurla Complex,Bandra (E),Mumbai 400 051.
T:+912240009100F:+912240009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067
