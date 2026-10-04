# NETC | OC 003 | F.Y. 25-26 | Implementation of bulk upload and download functionality for disputes and evidences in NRCS

Circular/reference number: NPCI/2025-26/NETC/003
Date: 19th August, 2025

<!-- Page 1 -->

NPCI/2025-26/NETC/003    
 
 
 
 
 
    19th August, 2025      
To, 
All NETC Members 
 
Subject: Implementation of bulk upload and download functionality for disputes 
and evidence in NETC NRCS back-office portal. 
In continuation of our efforts to enhance operational efficiency in dispute management, 
NPCI is introducing bulk dispute with evidence upload/download functionality in the NRCS 
back-office portal, effective 1 September 2025. This feature will enable member banks 
to process dispute with supporting evidence files in a single batch, as well as to download 
multiple incoming evidence files at once, significantly reducing manual efforts.  Depending 
on the requirement of evidence for a given dispute the stakeholders may provide the 
evidence else the bulk upload can be done without evidence. 
It is mandatory for the participants to submit all the evidence as applicable during 
chargeback/representment and pre-arbitration/pre-arbitration decline stages itself. No 
evidence shall be allowed to be submitted through the system during NRP / Arbitration 
stages. As approved in steering committee meeting dated 27th February, 2025 the option 
for web or bulk evidence upload will be disabled for the following stages: 
1. Arbitration raise 
2. Arbitration withdrawal 
3. Arbitration acceptance 
4. Arbitration continuation 
NPCI may seek evidence at NRP or arbitration stages in exceptional cases. Member are 
advised to review the summary of major changes in Annexure 1 and the detailed user 
manual in Annexure 2 and undertake necessary internal preparations for the scheduled 
rollout. 
For any queries or clarifications, members are advised to raise a ticket in the CRM 
system. 
Regards, 
 
Sd/- 
Giridhar G.M. 
Chief – Customer Success

<!-- Page 2 -->

Annexure - 1  
Summary of Major Changes 
Sl. No. 
Particulars 
1 
User interface (dispute upload): Selecting Dispute → Bulk File Upload 
option in NRCS opens a separate popup window for the batch upload, while 
the main NRCS screen remains active for other tasks. 
2 
New field: The bulk upload CSV file now includes a new field 
“EvidenceFileName” to specify the names of evidence documents for each 
transaction. Up to 4 evidence file names can be listed per dispute, separated 
by the ‘|’ character. (If no evidence is to be attached, the header must still be 
included but left blank as per the revised file format). 
3 
Evidence File Naming Convention: NRCS will rename evidence files in all 
acknowledgement and incoming reports as per below format:  
<UploadPartyOrgID>_<DateTime>_<OriginalEvidenceName> to ensure 
traceability. 
4 
ZIP File Composition: Uploads must be submitted as a single ZIP file 
containing:  
(i) the PGP-encrypted dispute CSV file, and  
(ii) all evidence files referenced in the CSV file  
If no evidence are referenced, the ZIP should contain only the PGP dispute 
file. if a PGP file is directly uploaded to NRCS, it shall be rejected for incorrect 
file format. 
5 
Bulk Download of Evidence: All incoming evidence files will be made 
available for bulk download. The NRCS portal will package these incoming 
evidence files (and the corresponding incoming encrypted dispute file) into a 
ZIP folder for download. 
6 
File Size Limits: The combined size of the upload ZIP (including the PGP 
dispute file and all evidence) must not exceed 1,000 MB. Each individual 
evidence file inside the ZIP must not exceed 2 MB. 
7 
Upload Constraints: Only one upload ZIP can be processed at a time per 
bank; simultaneous uploads are not supported and will result in an error. 
Ensure that each file is fully processed before initiating the next upload.

<!-- Page 3 -->

8 
Evidence File Reuse: If the same evidence applies to multiple disputes, the 
same file may be referenced by multiple CSV file records instead of duplicating 
the file in zip folder. For example, a single RC copy can be referenced for all 
disputes requiring it. (Regardless, the referenced evidence file must be 
present in the ZIP.) This reduces redundancy and keeps file sizes smaller.

<!-- Page 4 -->

Annexure 2: 
User Manual – NRCS Bulk Upload and Download Functionality (Version 1.0) 
User manual - 
flow_NRCS bulk uploa
