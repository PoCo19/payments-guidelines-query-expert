# NFS | OC419 | FY 24-25 | Upgradation of NFS back-office system from “BCS NFS” to “BCS 2.0 NFS”.

Circular/reference number: NPCI/NFS/OCNo.419/2024-25
Date: 18th March 2024

<!-- Page 1 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo.419/2024-25 May 11, 2024
All MembersofNational Financial Switch-NFSATMNetwork
Sub: Upgradation of NFS back-office system from "BCS NFs" to "BCS 2.0 NFs"
Reference may be taken from our Operating Circular NPCI/2023-24/NFS/073 dated 18th March 2024 on
upgradation of NFS operational activities from BCS NFS to the new system BCS 2.0 NFS, we wish to inform
you that the upgraded version of NFs back-office application Bcs 2.0 shall be moved to production with
effect from May 18, 2024.
Banks are advised to take note that BCS 2.o NFs has been developed similar to BCS NFS, the file formats
for all settlement reports and adjustments remain the same.
1.  List of important changes that shall be implemented in the new version provided in Annexure -- I.
2.  Go live instructions with cut over activity timings are provided in Annexure - Il.
Member banks are advised to take a note of the above and disseminate the instructions contained herein
to all the stakeholders concerned. Should you need any further assistance, please feel free to contact the
officials as per the contact details provided in Annexure - IIl.
YourFaithfully,
GiridharG M
Chief-CustomerSuccess&GovtRelations
1001A, The Capital, B Wing,10th Floor,
Bandra Kurla Complex,Bandra(E),Mumbai 4oo o51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure I
The following changes shall be implemented in the upgraded version:
1. Calculation of customer compensation amount in case of delayed credit / reversal with reference
to harmonization of TAT guideline:
a) If a dispute is accepted before NFs 3rd settlement cycle cut off, the penalty will be calculated
as (dispute acceptance date - transaction date - 5) *100.
b) For disputes accepted thereafter the penalty will be calculated as (dispute acceptance date 
customer compensation penalty is applicable)
2. Additional reports under ADHOC report download option:
a) FcQM inquiry report: With the help of this report the bank can verify the status of the
transactions reported in FCQM.
b) Response code-wise analysis Report: This report contains a response code wise transactions
summary.
3. List of reports that shall be discontinued in NFs 2.0 BcS are as follows:
(e Monthly Report
1. ATMWISE_FULL_REVERSAL_REPORT_XXX_DD-MM-YYYY_tO_DD-MM-YYYY.XLS
Bank wise monthfy dispute report1.xls
3. Response code wise analysis Acq rReport.xls
4. Response code wise analysis report.xls
5. TDR_REPORT.xIs
(q Daily Report
1. Response code wise analysis Acq report.xls
2. Response code wise analysislss report.xis
3. VerafVerifXXXDDMMYY_XC_zip.pgp
4. NTSL report format:
NTsL file is used for "Final Settlement Amount" calculation and the individual dispute line items
are provided in the "Adjustment Report", thus, this information is redundant in the NTSL report.
In view thereof, in the BCS 2.0 NFS system, there is a change made in the NTSL report wherein the
individual dispute line items shall not be provided. The consolidated value of disputes like "Total
representment amount", "Total adjustment amount" etc., as only these are required for
calculating the “final settlement amount", along with the respective total "No of Txns".
1001A, The Capital, B Wing, 10th Fioor,
Bandra Kurla Complex,Bandra (E), Mumbai 4oo O51.
T: +91 22 40009100 F: +9122 40009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure I!
System requirements, go live instructions, activity timings for cut over:
1. System Requirements:
Member to take note of the System Specification Requirement for Bcs 2.0 NFs. Please refer to the
below specifications foreasy reference.
Particulars Specifications
RAM Minimum 1 GB RAM
Supported Browser Microsoft Internet Explorer and Chrome version 112 & above
To make the best use of Bcs 2.0 NFS, we recommend a monitor of
Screen Resolution 1024x768 pixels or higher, and 32-bit colour or higher
JavaScript is used in BcS 2.0 NFs to enhance the user experience and
provide advanced functionality. BCS 2.0 NFS requires Java to be installed
JavaScript and turned on.
Cookies BCs 2.0 NFS application reguires cookies to be enabled in the browser.
Bcs 2.o NFs uses 'pop-up' windows to display some content. If you are
using a browser that offers pop-up control or is running an add-on
Pop-up Control for this site.
2. Go live instructions:
a) Identify resources who will be closely working with NPCl, to help upgrade the banks facility to
the new clearing & settlement system, provide post go live support by monitoring and
reporting any issue to NpCi for resolution.
(q Banks shall use the same URL (currently used to access the existing back-office system).
c) Once the new BCS 2.0 NFS URL is enabled at by all member banks, NPCI would decommission
the URL of the old system.
d) Admin checker user has been introduced in the new Bcs 2.o NFS in order to enhance security.
The password would be set to "Admin@12345" for all the existing Member Bank Admins,
Maker & Checker users. Upon first time login to the new BcS 2.0 NFS system, users must set
the Secret questions and change their passwords immediately.
f)  Admin users can map the respective profile & permissions to the maker & checker users to
perform theirdaily operations.
g) The old reports and raw files (for last 3 months) shall continue to be available in the new
system as the data and reports shall be migrated.
3.Activity timings for cut over:
a) 13th May 2024:
1. Member Bank administrators to ensure that no On boarding, BiN addition / modification
/ deletion, BIN / Bank migration is carried out until the BCs 2.0 NFS Upgradation.
b)17th May 2024, 22:00 Hrs.:
1001A, The Capital, B Wing.1oth Floor.
 Bandra Kurla Complex, Bandra (E), Mumbai 4oo o51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 4 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
1. Bcs NFs application will be decommissioned, and member banks will not have access to
the portal.
17th May 2024, 22:00 Hrs.:
1.  BcS 2.0 NFS application will be commissioned.
2. Migration activities would be carried out between 17th May 22:00 hours & 18th May 17:00
hours. During this period all transactions / auth would continue to be pushed to the BCs
2.o NFS system. During this time the URL will be down, i.e., banks won't be able to upload
disputes during these 17 hours period (17th May 22:00 hours & 18th May 17:00 hours).
3. All the settlement reports of 18th May 2024 Cycle 2 & there upon would be available in
the new portal.
Annexure Inr
Contact details:
Operations
Name Email ID Contact Details
NFS Operations nfsdms@npci.org.in NA
Pralhad Raut pralhad.raut@npci.org.in 8369600256
Sanjay Mane sanjay.mane@npci.org.in 9930283950
Yogesh Suradkar yogesh.suradkar@npci.org.in 9821354323
Srimon Anbarasan srimon.anbarasan@npci.org.in 9870353010
Priya Pandey priya.pandey@npci.org.in 8452011854
Sanjoy Mukherjee sanioy.mukheriee@npci.org.in 8130317788
CustomerSuccess--DirectMemberBanks
Glen Gonsalves glen.gonsalves@npci.org.in 8291847129
Tejasvi Shirsat tejasvi.shirsat@npci.org.in 8879754909
Meha Manjula meha.manjula@npci.org.in 9051743497
Vaibhav Joshi vaibhav.joshi@npci.org.in 8291847139
Jyoti Jadhav iyoti.jiadhav@npci.org.in 8108108619
Customer Connect Unit (For Any Clarification/Doubts)-Sub -Member Banks
Mayur More mayur.more @npci.org.in 9892049137
Ameya Save ameya.save@npci.org.in 9769202052
Deepak Panday deepak.panday@npci.org.in 8237361755
Sunil Kumar sunil.kumar@npci.org.in 8879760247
Swati Dsa swati.dsa@npci.org.in 8879760289
Phaneendra Kumar phaneendra.kumar@npci.org.in 8143222999
1001A, The Capital, B Wing, 10tih Floor,
Bandra Kurla Complex, Bandra(E),Mumbai 4oo o5),
T: +9122 40009100 F: +9122 40009101
contact@npci.org.in www.npci.arg.in
CIN: U74990MH2008NPL189067
