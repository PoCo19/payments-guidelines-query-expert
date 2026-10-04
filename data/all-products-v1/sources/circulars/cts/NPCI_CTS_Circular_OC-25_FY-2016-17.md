# NPCI/2015-16/CTS/Circular No.25 - Annexure - Circular No. 25-Annexure - Specification document Version 2.4 - All

Circular/reference number: OC-25
Date: 9th  March 2016

<!-- Page 1 -->

CTS Clearing House Interface – Specification 
 
 
1 
 
 
 
 
 
 
 
 
 
 
                                                     
 
 
 
 
CTS CLEARING HOUSE INTERFACE 
 
 
 
 
 
 
 
 
SPECIFICATIONS 
 
 
 
 
 
 
 
 
 
9th  March 2016 
 
 
100-0010782 Revision 2.4 
 
 
 
 
 
 
 
 
NCR & RBI/NPCI PROPRIETARY – The information contained herein is the property of NCR Corporation and 
Reserve Bank of India / National Payment Corporation of India and all unauthorized use and reproduction is 
prohibited.

<!-- Page 2 -->

 
CTS Clearing House Interface – Specification 
 
 
2 
 
 
 
MAIN CHANGE SHEET 
 
 
Rev 
Date 
Description of Change 
Rev 1.1 
January 16, 2006 
- Initial 
Rev 1.2 
March 8, 2006 
NCR & RBI/NPCI internal review & changes 
Rev 1.3 
April 12, 2006 
NCR & RBI/NPCI internal review & changes 
Rev 1.4 
April 18, 2006 
NCR & RBI/NPCI internal review & changes 
Rev 1.5 
April 26, 2006 
NCR & RBI/NPCI internal review & changes 
Rev 1.6 
June 27-Jul 1, 2006 NCR & RBI/NPCI internal review & changes 
Rev 1.7 
July 20 – Aug 01, 
2006 
NCR & RBI/NPCI internal review & changes 
Rev 1.8 
17 Aug – 28 Aug 
2006 
NCR & RBI/NPCI internal review & changes 
Rev 1.9 
08 Sep – 19 Sep 
2006 
Changes in response to RBI/NPCI Document Review 
& discussions through 02 Sep 2006. 
Rev 1.10 
22 Sep 2006 
Changes shown via document markups. 
 
Change Sheets prior to Rev 1.9 reduced. 
 
Sect 2 Step 1 Physical Endorsement clarified 
 
Sect 7 details of security in separate document 
 
Appendix A corrections in CHI Interface 
Rev 1.11 
17 Nov 2006 
Changes are shown via document markups, relative 
to Rev 1.10 previously released. 
 
fixed corrupted Cover Page 
 
sect 9.3.1 deleted extraneous paragraph re: 4GB 
Memory 
 
sect 12, deleted reference to future Government 
Account Master in the CHMaster tables. 
 
Appx 1 deleted reference to host (recon) file 
 
Appx 2.1 clarify Extension File (EF) as well as 
DREF 
 
Appx 2.4, Appx 2.5, Appx 3.4.1, Appx 4.8, Appx 
4.8.1 describe DREF 
 
Appx 2.5, Appx 4.11.2, Appx 4.11.3.3, Appx 6 add 
necessary detail for AtParBankMaster element 
 
Appx 2.5, Appx 4.12, Appx 5.9 add detail and 
example for Unwound Item File 
 
Appx 4.11.2 redraw picture, A1 adjust indent of 
“Branch” 
 
Appx 4.11.3.7 completed description of 
DesignatedBranchForTransCode

<!-- Page 3 -->

 
CTS Clearing House Interface – Specification 
 
 
3 
Rev 1.12 
15 Feb 2007 
 
Changes are shown via document markups, 
relative to Rev 1.11 previously released. 
 
Sect 3.8 (IQA Defect Tests) -- use Thresholds from 23 
Nov 2006 Image Quality Assessment Report; Remove 
"ENABLE" column 
 
Sect 11.1 – license clarification 
 
Appx 1.2  
o 
C4 -- clarify Mandatory/Optional as applies to 
elements and attributes. Note that Fields having 
NULL or no default value are to be omitted from 
input files.  Default/pre-defined values for attributes 
are case-sensitive 
o 
C8 -- clarify element tags and attribute names are 
case-sensitive. 
 
Appx 2.1 -- diagram add DREF file 
 
Appx 2.5 -- specifically list DREF Drawee Extension 
File (it was already given in the description) 
 
Appx 3.3 -- add suggestion for better exception 
processing by inclearing system, clarify purging. 
 
Appx 4.1.2 -- diagram to swap ImageDS with 
ImageViewData to agree with order in A1; corrected 
legend. 
 
Appx 4.1.3.1 -- xmlns is lower case, VersionNumber 
xxyyyy is lower case, added DREF file 
 
Appx 4.1.3.3 -- IQAIgnoreInd is optional, default value 
is 0 
 
Appx 4.1.3.4 – MICRFingerPrint NOTE: clarified, added 
“Drawee” as possible value 
 
Appx 4.1.3.6 -- provided attribute descriptions, remove 
ViewSideIndicator values that are not supported. 
 
Appx 4.1.3.7 -- clarified Filename, and digital signature 
attributes, StartOfProtectedData and 
ProtectedDataLength are Mandatory, lengths must be 
greater than 0 
 
Appx 4.1.3.8 -- clarified ImageReferenceKeyLength, 
length must be greater than 0 
 
Appx 4.1.3.9 -- described ImageViewAnalysis and IQA 
interpretations. 
 
Appx 4.3.2 -- diagram to swap ImageDS with 
ImageViewData to agree with order in C1; corrected 
legend. 
o 
C1 list multiple MICRDS and ImageDS, 
ImageViewAnalysis elements 
 
Appx 4.3.3 -- diagram to swap ImageDS with 
ImageViewData to agree with order in B1; corrected 
legend. 
o 
C1 list multiple MICRDS and ImageDS, 
ImageViewAnalysis elements 
o 
C2 -- added Mandatory elements 
 
Appx 4.3.4.1 -- xmlns is lower case, VersionNumber

<!-- Page 4 -->

 
CTS Clearing House Interface – Specification 
 
 
4 
xxyyyy is lower case 
 
Appx 4.4.2 – corrected diagram 
 
Appx 4.5.2 -- diagram - corrected legend. 
o 
C1,C2 -- added structure and Mandatory elements 
Appx 4.5.3.4 – MICRDS for RRF sets source = “Drawee” 
Appx 4.6.2 -- diagram - corrected legend. 
 
Appx 4.6.3 -- diagram - corrected legend. 
o 
C2 -- added Mandatory elements 
 
Appx 4.7.2 -- diagram added 
o 
C1,C2 -- properly named the file, and added 
Mandatory elements 
 
Appx 4.8.1 C1, C3 -- list EF and DREF files 
 
Appx 4.8.2 -- diagram - corrected legend. 
 
Appx 4.9.1 C1 -- clarify File ID is unique 
 
Appx 4.9.3.1 -- clarify CreationDate and CreationTime, 
VersionNumber xxyyyy is lower case 
 
Appx 4.3.10.3.3.1–augment error resolution for 
FileStatusCode 2 
 
Appx 4.9.2 -- diagram to agree with C2; corrected 
legend. 
o 
C2 -- update diagram and clarify Mandatory 
elements 
 
Appx 4.9.3.1 -- xmlns is lower case, VersionNumber 
xxyyyy is lower case 
 
Appx 4.9.3.2 -- update that 2 attributes are Mandatory 
 
Appx 4.10.2 -- diagram - corrected legend. 
o 
C2 added Mandatory elements 
 
Appx 4.10.3.1 -- xmlns is lower case, VersionNumber 
xxyyyy is lower case 
 
Appx 4.11.3.1 -- xmlns is lower case 
 
Appx 4.11.3.7 -- TRANSCODE size is 3 
 
Appx 4.11.3.18 -- CODE size is 3 
 
Appx 5.1 -- corrected errors in CXF example 
 
Appx 5.2 -- corrected errors in PXF example 
 
Appx 5.3 -- corrected errors in RRF example, MICRDS 
is “Drawee” 
 
Appx 5.4 – corrected errors in RF example, MICRDS is 
“Drawee” 
 
Appx 5.5 -- corrected errors in ERF example 
 
Appx 5.6 -- corrected errors in EF example 
 
Appx 5.7 -- corrected errors in RES example 
 
Appx 9.1 -- C11, C22 removed extraneous NCR 
transport specifics 
 
Appx 9.2 -- table deleted as RBI/NPCI does not support 
JPEG images in TIFF files. 
 
Appx 9.3 -- C2 removed extraneous NCR transport

<!-- Page 5 -->

 
CTS Clearing House Interface – Specification 
 
 
5 
specifics 
 
Appx 9.4 -- C2 deleted 
 
Appx 9.5 -- C1 deleted 
 
Appx 9.6 new to define Required JFIF markers and 
tags for grayscale JFIF images 
Rev 1.12 
14 March 2007 
Further changes are shown via document markups, 
relative to Rev 1.11 previously released. 
 
Sect 11.1 – remove sentence regarding separate 
license 
 
Appx 2.5 PXF – added that number of items is a 
configurable parameter 
 
Appx 4.1.3.9 – corrected attribute spelling 
LegalAmountUsability 
 
Appx 4.5.3.3.1 – corrected to agree with RBI/NPCI 
Procedural Guidelines; 39 clarified; 40 added, 82,83,84 
deleted. 
 
Appx 4.7 – corrected working in introduction paragraph 
 
Appx 4.7.3.3.1 – changed descriptions 01,02,03 
 
Corrected sample files to reflect India values – Appxs: 
5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.8 
Rev 1.13 
04 July 2007 
 
Made a change in Section 2 – Step 2 Corrected the 
definition of calculation of maximum return period. 
Added following words – “Capture shall use 
SessionDate, CLOSE_RECEIVING_TIME of the 
Session and SessionExtensionHrs for the session to 
calculate the maximum return period.” 
Rev1.13 
19 July 2007 
 
Updated Section 2 – Step 3 – Removed the FID 
reference. FDD shall contain both data and images. 
 
Section 7 Security – Updated the diagram that shows 
the data flow through ECPIX and the digital signatures 
that are applied to items and files as the data flows. 
 
Added AtParBankMaster reference in Section 12. 
 
Updated Appx 3.7.1 Presentation Validations – 
Wrongly Presented Item Check para. 
 
Updated Appx 3.7.2 Returns and Extension Validations 
 
Rev 1.15 
14 July 2010 
 
Addition of a new reject reason code in section 4.9.3.3 
 
Modified the description for "Item Presentment Date vs 
item session date validation" in section 3.7.1 
 
Added 2 new validations in section 7.1 
 
Added support for 2048 bit key length in section 7 
 
Modified list of reports in section 8 
 
Updated TOC 
 
Updated memory configuration in sections 9.1.1, 9.2.1, 
9.3.1 & 9.4.1 
 
Updated software configuration in sections 9.1.2, 9.2.2,

<!-- Page 6 -->

 
CTS Clearing House Interface – Specification 
 
 
6 
9.3.2 & 9.4.2 
 
 
 
Updated section 3.8 for IQA thresholds parameters as 
per the site. 
Rev 1.16 
24 August 2010 
 
Modified the document to replace RBI with RBI/NPCI 
 
Modified section 1 for replacing word "pilot" with 
"project" 
 
Modified section 3.7.1 for Drawee city validation. 
 
Added a Note in section 3.7.2 
 
Modified section 8 for adding two reports, IQA Fail & 
IQA Pass 
 
Modified section 8 for rephrasing the statement for 
manual generation of reports 
 
Modified section 10 for updating the network capacity 
planning for 85kb 
 
Modified section 11.1 replacing "CHI" with "Bank" 
 
Modified section 8 for synchronizing the report names 
with that of the site. Also added 2 reports that were 
present on site but not in the document. 
Rev 1.17 
7th September 2010 
 
Added section 9.6 to mention about the CHI High 
Availability. 
 
Added a Note in section 9 for the Grid support for 32 bit 
CHI. 
 
Modified section 1 to rephrase the statement as 
suggested by NPCI. 
 
Modified section 11.1 to add the reference for 
Hardware configuration of the A-CHI server. 
Rev 1.18 
1st August 2011 
 
Deleted the comment in section 7 that says that 2048 
bit certificates shall be supported by means of a CR. 
 
Modified size of field “SecurityKeySize” in sections 
Appx 4.1.3.4 and Appx 4.1.3.7 to support 2048 bit 
certificates. 
Rev 1.19 
11th  August 2011 
 
Modified size of field “DigitalSignatureMethod” in 
sections Appx 4.1.3.4 and Appx 4.1.3.7 to support 
SHA256 signature algorithm. 
 
Added version (0002- for 2048 securitykey support) 
and (0003 – SHA256 algorithm support) in section 
4.1.3.1 & 4.5.3.1 for CXF and RRF files. 
 
Added the file header along with file version used in 
section 4.5.3.1, 4.6.4.1, 4.7.3.1, 4.8.3.1. 
 
27th  Feb 2012 
 
For CXF and RRF files added version (0002- for 2048 
securitykey support) and (0003 – SHA256 algorithm 
support) for xmlns attribute. 
Rev 1.20 
22nd March 2012 
 
Modified field value for DigitalSignatureLength in 
section Appx 4.1.3.7 ImageDS for SHA1 and SHA2 
Rev 1.21 
27th June 2012 
 
Modified the section 4.2.2 and 4.4.2 in appendix for 
CIBF and PIBF file structure.

<!-- Page 7 -->

 
CTS Clearing House Interface – Specification 
 
 
7 
Rev 1.22 
22nd Aug 2012 
 
Modified the section 9.1.1,9.2.1,9.3.1,9.4.1 and 9.5.1 to 
Add Windows 2008 OS and to modify Windows Disk 
requirement for Windows 2008.  
 
Modified the section 9.1.2,9.2.2,9.3.2,9.4.2 and 9.5.2 to 
add new Thirdpaty software requirement for Windows 
2008. 
 
Modified the section 9.6.1 to to Add Windows 2008 OS 
in CHI Cluster requirement. 
Rev 1.23 
9th Sep 2012 
 
Modified the the Roxio Entries in 9.1.2,9.2.2,9.3.2,9.4.2 
and 9.5.2 section. Modified the Software list in order 
show the Paid Third Parties in first followed by the free 
Third Parties. 
 
Modified the section 9.1.1,9.2.1,9.3.1,9.4.1 and 9.5.1 to 
separate Windows 2003 and Widows 2008 OS and 
And added note for Windows clustering requirement. 
Rev 1.24 
30th Nov 2012 
 
Updated section 9.1.1, 9.2.1, 9.3.1, 9.4.1 and 9.5.1 for 
change in processor model 
 
Updated section 9.1.2, 9.2.2, 9.3.2 and 9.4.2 for 
change in WebSphere edition from Standard to 
Express 
Rev 2.0 
7th Dec 2012 
 
Updated section 9.1.1, 9.2.1, 9.3.1, 9.4.1 and 9.5.1 for 
change in processor core details and model details. 
 
Updated section 9.1.1, 9.2.1, 9.3.1, 9.4.1 and 9.5.1 for 
change in disk drive details, drive configuration and 
formatting changed to tabular format. 
 
Updated section 9.1.1, 9.2.1, 9.3.1, 9.4.1 and 9.5.1 for 
modification of Database backup drive size. 
 
Updated section 9.1.2, 9.2.2, 9.3.2, 9.4.2 and 9.5.2 for 
removal of Windows 2003 Thirdparty requirement and 
addition of Oracle 11.2 32 bit client.  
 
Third-Party software components grouped separately 
based on license procurement. Formatting changed to 
tabular format. 
 
Updated section 9.1.2, 9.2.2, 9.3.2, 9.4.2 and 9.5.2 for 
removal of Windows 2003 Third-Party software 
requirement. 
 
Updated Security Module section of 9.1.1, 9.2.1, 9.3.1, 
9.4.1, 9.5.1 9.1.2, 9.2.2, 9.3.2, 9.4.2 and 9.5.2 for 
removal of Rainbow HSM card support. 
 
Updated section 9.1.2, 9.2.2, 9.3.2, 9.4.2 and 9.5.2 for 
addition of Third-Party software additional vesrion 
details and categorization of Third-Party as per there 
licensing term. 
 
Updated section 9.1.2, 9.2.2, 9.3.2, 9.4.2 and 9.5.2 for 
addition of Windows 2008 vesrion details and removal 
of Windows 2003. 
 
Moved section 9.6 (High Availability for CHI) under 
section 11 (High Availability and Disaster Recovery). 
 
Modified section 7 to remove the support for SHA1 
signature algorithm and 1024 security key length 
support and to add support for SHA256 signature

<!-- Page 8 -->

 
CTS Clearing House Interface – Specification 
 
 
8 
algorithm and 2048 security key length support. 
Rev 2.1 
05th OCT 2013 
 
Addition of a new section for interface specification of 
FILE for CHI Branch interface module’s bulk search 
o 
Appx 4.4 FILE for CHI Branch interface module’s 
bulk search 
o 
Appx 4.4.1 File Name Convention 
o 
Appx 4.4.2 Elements 
o 
Appx 5.10 Example of FILE for CHI Branch 
interface module’s bulk search 
 
Updated some format changes in below section. 
o 
Appx 4.1.3 Elements and Attributes 
 
Addition of section 9.6 for Extra Large CHI (Between 
400,000 and 550,000 items/day Inward + Outward) 
 
Addition of section 9.7 for Extra-Extra Large CHI (XXL 
CHI) (Between 450,000 and 800,000 items/day) 
 
Modified the 3.8 section for “Below Minimum Image 
Size” and “Exceeds Maximum Image Size” values for 
100DPI and 200DPI image resolution related changes. 
Rev 2.1 
26th DEC 2013 
 
Modified the change sheet section name so that it can 
be distinctly differentated the following section in the 
document. 
o 
Main Change Sheet. 
o 
Appendix Change Sheet. 
Rev 2.1 
24th Jan 2014 
 
Modified the note in 3.8 section to remove the SRS 
word, because SRS (System requirement specification) 
is not meant for CHI. 
Rev 2.1 
28th Jan 2014 
 
Modified the "11.2 Disaster Recovery – Alternate CHI" 
section to add Oracle Data guard as optional solution 
for database synchronization between Primary CHI and 
Alternate CHI. 
 
Added note in Third-Party Software section of 9.1.2, 
9.2.2, 9.3.2, 9.4.2, 9.5.2, 9.6.2, 9.7.2 to use Oracle 
Enterprise Edition for CHI's database if Bank's user 
wants to use Oracle Data Guard feature to replicate 
database between Primary and Alternate CHI. 
 
Rev 2.2 
18th Sep 2014 
 
Modified Appx 4.1.3.1 FileHeader section. 
 
Modified Appx 4.1.3.7 Image DS section. 
 
Modified Appx 5.1, 5.3 & 5.5 ECPIX file examples 
section. 
 
Modified Appx 3.7.1 Presented ValidationsRemoved 
FootNote from Appendix 4.1.3.3 
 
 
Rev 2.2 
10th Feb 2015 
 
Modified Appx 4.1.3.3 Item section.Footnote added for 
AccountNo 
 
Modifed Appx 4.3.10.3.3.1 Reject reason section. 
Rev 2.2 
16th Mar 2015 
 
Updated section 
9.1.2,9.2.2,9.3.2,9.4.2,9.5.2,9.6.2,9.7.2,for installation 
of SP1 on top of Windows server 2008 R2.  
 
Modified the section 8 for adding three reports Outward 
Clearing branch wise, MICR Reject Repair Report and 
Bank wise Reports

<!-- Page 9 -->

 
CTS Clearing House Interface – Specification 
 
 
9 
 
Updated section 4.3.10.3.3.1 to add new item reject 
reason codes for Return Reason comment validation 
and validation of BOFD routing number for P2F 
instrument 
 
 
IPSwitch WS_FTP version added in Footnote for SFTP 
in following section 9.2.1, 9.2.2, 9.3.2, 9.4.2, 9.5.2, 
9.6.2, 9.7.2. 
 
Rev 2.3 
20th Nov 2015 
 
Modified Appx 4.1.3.1 and Appx 5.1 section, new 
schema version is added CXF for adding validations for 
MICRRepairFlags attributes.  
 
Foot note is added for MICRRepairFlags validations. 
 
Rev 2.3 
11th Jan 2016 
 
Modified Appx 4.1.3.1 update validations for 
MICRRepairFlags attributes.  
 
Foot note is updated for MICRRepairFlags validations. 
 
Rev 2.4 
10th Feb 2016 
 
Modified Appx 4.1.3.1 update validations for 
Government validations. Description for Reject reason 
15 and 27 are updated 
Rev 2.4 
03RD Mar 2016 
 
Modified footnote in Appx 4.1.3.3, Added Foot note for 
Mandatory condition of AccountNo field 
Rev 2.4 
09th Mar 2016 
 
Modified Appx 4.1.3.3 Description changed for 
MICRRepairFlags - ‘xxxx5x’ to “if account is old.”  
 
Note : This document has the following change sheet section.  
 
Main Change Sheet. 
This section tracks all the changes in the document excluding the changes in the Appendix 
section. 
 
Appendix Change Sheet. 
This section tracks all the changes in the Appendix section.

<!-- Page 10 -->

 
CTS Clearing House Interface – Specification 
 
 
10 
TABLE OF CONTENTS 
CTS CLEARING HOUSE INTERFACE .................................................................................................................................. 1 
SPECIFICATIONS .................................................................................................................................................................. 1 
MAIN CHANGE SHEET ......................................................................................................................................................... 2 
TABLE OF CONTENTS ....................................................................................................................................................... 10 
1 
INTRODUCTION .......................................................................................................................................................... 13 
2 
CTS ARCHITECTURE ................................................................................................................................................. 14 
3 
CHI FEATURE FUNCTIONALITY ............................................................................................................................... 19 
3.1 
DAILY PROCESSING TIMELINES ............................................................................................................................... 19 
3.2 
CHI FOR OUTWARD PRESENTMENT ........................................................................................................................ 19 
3.3 
CHI FOR INWARD PRESENTMENT ............................................................................................................................ 20 
3.4 
CHI FOR OUTWARD RETURNS ................................................................................................................................ 20 
3.5 
CHI FOR INWARD RETURNS .................................................................................................................................... 20 
3.6 
CHI USER ROLES .................................................................................................................................................. 21 
3.7 
VALIDATION ........................................................................................................................................................... 22 
3.7.1 
Presentation Validations: ................................................................................................................................. 22 
3.7.2 
Return and Extension Validations: .................................................................................................................. 23 
3.8 
IQA DEFECT TESTS ............................................................................................................................................... 23 
3.9 
POSTING FILE CREATION ........................................................................................................................................ 25 
3.10 
STATUS MONITOR .................................................................................................................................................. 25 
3.10.1 
Monitor Status of Data and Images ............................................................................................................ 25 
3.10.2 
Monitor Status of Sessions at CH ............................................................................................................... 25 
3.11 
MEDIA BASED TRANSMISSION OF EXCHANGE FILES ................................................................................................. 26 
4 
INTERFACE WITH CAPTURE/DRAWEE BANK SYSTEMS ..................................................................................... 27 
5 
INTERFACE WITH BANK BRANCH ........................................................................................................................... 28 
5.1 
ONLINE MARKING OF RETURNS ................................................................................................................................ 28 
5.2 
ONLINE RETRIEVAL OF BRANCH POSTING DATA ......................................................................................................... 28 
5.3 
ONLINE UPLOAD OF RETURN REQUEST DATA ........................................................................................................... 28 
6 
ENQUIRIES .................................................................................................................................................................. 29 
7 
SECURITY ................................................................................................................................................................... 30 
8 
REPORTS .................................................................................................................................................................... 31 
9 
EQUIPMENT SIZING ................................................................................................................................................... 33 
9.1 
MINI CHI (UPTO 10,000 ITEMS/DAY) ........................................................................................................................ 33 
9.1.1 
Hardware ......................................................................................................................................................... 33 
9.1.2 
Software .......................................................................................................................................................... 34 
9.2 
SMALL CHI (UPTO 30,000 ITEMS/DAY) .................................................................................................................... 34 
9.2.1 
Hardware ......................................................................................................................................................... 34 
9.2.2 
Software .......................................................................................................................................................... 35 
9.3 
MEDIUM CHI (BETWEEN 30,000 AND 100,000 ITEMS/DAY) ...................................................................................... 36 
9.3.1 
Hardware ......................................................................................................................................................... 36 
9.3.2 
Software .......................................................................................................................................................... 37 
9.4 
LARGE CHI (BETWEEN 100,000 AND 250,000 ITEMS/DAY) ...................................................................................... 38 
9.4.1 
Hardware ......................................................................................................................................................... 38 
9.4.2 
Software .......................................................................................................................................................... 39 
9.5 
VERY LARGE CHI (BETWEEN 250,000 AND 400,000 ITEMS/DAY) ............................................................................. 41 
9.5.1 
Hardware ......................................................................................................................................................... 41 
9.5.2 
Software .......................................................................................................................................................... 42 
9.6 
EXTRA LARGE CHI (BETWEEN 400,000 AND 550,000 ITEMS/DAY INWARD + OUTWARD) ........................................... 43 
9.6.1 
Hardware ......................................................................................................................................................... 43 
9.6.2 
Software .......................................................................................................................................................... 45 
9.7 
EXTRA-EXTRA LARGE CHI (XXL CHI) (BETWEEN 550,000 AND 800,000 ITEMS/DAY) ............................................... 46 
9.7.1 
Hardware ......................................................................................................................................................... 46 
9.7.2 
Software .......................................................................................................................................................... 48

<!-- Page 11 -->

 
CTS Clearing House Interface – Specification 
 
 
11 
10 
NETWORK CAPACITY PLANNING ............................................................................................................................ 50 
11 
HIGH AVAILABILITY AND DISASTER RECOVERY ................................................................................................. 50 
11.1 
HIGH AVAILABILITY – ACTIVE-PASSIVE CLUSTER ..................................................................................................... 50 
11.2 
DISASTER RECOVERY – ALTERNATE CHI ................................................................................................................ 51 
11.3 
ALTERNATE DURING NETWORK FAILURE .................................................................................................................. 51 
12 
CLEARING HOUSE TABLES AVAILABLE FOR CAPTURE SYSTEM ..................................................................... 51 
13 
APPENDIX A – CHI INTERFACE SPECIFICATION ................................................................................................... 53 
APPENDIX CHANGE SHEET .............................................................................................................................................. 53 
APPX 1 
INTRODUCTION ................................................................................................................................................. 66 
APPX 1.1 
NOMENCLATURE AND NOTES ON READING THIS DOCUMENT ............................................................................ 66 
APPX 1.2 
CONVENTIONS ............................................................................................................................................... 67 
APPX 1.3 
REFERENCES ................................................................................................................................................ 68 
APPX 2 
PROCESS FLOW IN THE CHECK TRUNCATION SYSTEM (CTS) USING ECPIX ......................................... 69 
APPX 2.1 
PROCESS FLOW DIAGRAM ............................................................................................................................. 69 
APPX 2.2 
PRESENTMENT FLOW .................................................................................................................................... 70 
APPX 2.3 
RETURN FLOW .............................................................................................................................................. 70 
APPX 2.4 
EXTENSION OR PAPER REQUEST FLOW ........................................................................................................... 71 
APPX 2.5 
INTERFACE FILES .......................................................................................................................................... 72 
APPX 3 
FILE TRANSMISSION SPECIFICATIONS ......................................................................................................... 75 
APPX 3.1 
PRESENTMENT AND RETURN FILES DEPOSIT TIME ........................................................................................... 75 
APPX 3.2 
CONNECTIVITY FOR FILES TRANSFER ............................................................................................................. 75 
APPX 3.3 
FILE TRANSFER ............................................................................................................................................. 75 
APPX 3.4 
FILE FOLDER ................................................................................................................................................. 75 
Appx 3.4.1 
Participating Bank and Remote Branch Folders .................................................................................... 76 
Appx 3.4.2 
Clearing House Master Data Folder ....................................................................................................... 77 
Appx 3.4.3 
CHI and CH Data Folder ......................................................................................................................... 78 
APPX 3.5 
DUPLICATE FILES .......................................................................................................................................... 78 
APPX 4 
INTERFACE FILES ............................................................................................................................................. 78 
APPX 4.1 
CAPTURE EXCHANGE FILE (CXF) ........................................................................................................... 78 
Appx 4.1.1 
File Name Convention ............................................................................................................................ 78 
Appx 4.1.2 
File Structure .......................................................................................................................................... 79 
Appx 4.1.3 
Elements and Attributes .......................................................................................................................... 80 
APPX 4.2 
CAPTURE IMAGE BINARY FILE (CIBF) .................................................................................................... 99 
Appx 4.2.1 
File Name Convention ............................................................................................................................ 99 
Appx 4.2.2 
File Structure .......................................................................................................................................... 99 
APPX 4.3 
POSTING EXCHANGE FILE (PXF) .......................................................................................................... 101 
Appx 4.3.1 
File Name Convention .......................................................................................................................... 101 
Appx 4.3.2 
Master/Bank Posting eXchange File Structure ..................................................................................... 102 
Appx 4.3.3 
Branch/Trancode/AO Posting File Structure ........................................................................................ 104 
Appx 4.3.4 
Elements and Attributes ........................................................................................................................ 105 
Appx 4.3.5 
POSTING IMAGE BINARY FILE (PIBF) .............................................................................................. 110 
Appx 4.3.6 
RETURN REQUEST FILE (RRF) ......................................................................................................... 112 
Appx 4.3.7 
RETURN FILE (RF) .............................................................................................................................. 117 
Appx 4.3.8 
EXTENSION REQUEST FILE (ERF) ................................................................................................... 121 
Appx 4.3.9 
EXTENSION FILE (EF) ........................................................................................................................ 124 
Appx 4.3.10 
RESPONSE FILE (.RES) ................................................................................................................. 126 
Appx 4.3.11 
OUTWARD ACKNOWLEDGEMENT FILE (.OACK) ........................................................................ 134 
Appx 4.3.12 
CH MASTER DATA FILE ................................................................................................................. 137 
Appx 4.3.13 
UNWOUND ITEM(S) FILE ............................................................................................................... 152 
APPX 4.4 
CHI BRANCH INTERFACE MODULE'S BULK SEARCH INPUT FILE ..................................................... 155 
Appx 4.4.1 
File Name Convention .......................................................................................................................... 155 
Appx 4.4.2 
Elements ............................................................................................................................................... 155 
APPX 5 
APPENDIX  AA -  ECPIX FILE EXAMPLES .................................................................................................... 156 
APPX 5.1 
CAPTURE EXCHANGE FILE EXAMPLE ............................................................................................................ 156

<!-- Page 12 -->

 
CTS Clearing House Interface – Specification 
 
 
12 
APPX 5.2 
POSTING EXCHANGE FILE EXAMPLE ............................................................................................................. 158 
APPX 5.3 
RETURN REQUEST FILE EXAMPLE ................................................................................................................ 161 
APPX 5.4 
RETURN FILE EXAMPLE ............................................................................................................................... 162 
APPX 5.5 
EXTENSION REQUEST FILE EXAMPLE ........................................................................................................... 162 
APPX 5.6 
EXTENSION FILE EXAMPLE ........................................................................................................................... 163 
APPX 5.7 
RESPONSE FILE EXAMPLE ........................................................................................................................... 164 
APPX 5.8 
OUTWARD ACKNOWLEDGEMENT FILE EXAMPLE ............................................................................................ 165 
APPX 5.9 
UNWOUND ITEM FILE EXAMPLE .................................................................................................................... 165 
APPX 5.10 
EXAMPLE OF FILE FOR CHI BRANCH INTERFACE MODULE’S BULK SEARCH ..................................................... 165 
APPX 6 
APPENDIX  BB – CH MASTER DATA FILE EXAMPLE ................................................................................. 166 
APPX 7 
APPENDIX CC – CLEARINGTYPE .................................................................................................................. 167 
APPX 8 
APPENDIX DD – RETURN REASON CODES ................................................................................................. 169 
APPX 9 
APPENDIX EE – IMAGE DETAIL SPECIFICATIONS ..................................................................................... 170 
APPX 9.1 
REQUIRED TIFF TAGS FOR BLACK/WHITE G4 IMAGES .................................................................................. 171 
APPX 9.2 
REQUIRED TIFF TAGS FOR GRAYSCALE JPEG IMAGES ................................................................................ 172 
APPX 9.3 
EXTRA TIFF TAGS ....................................................................................................................................... 172 
APPX 9.4 
PRIVATE TIFF TAGS .................................................................................................................................... 172 
APPX 9.5 
SUPPORT FOR OTHER TIFF PARAMETERS .................................................................................................... 172 
APPX 9.6 
REQUIRED JFIF MARKERS AND TAGS FOR GRAYSCALE JFIF IMAGES ............................................................. 173 
APPX 9.7 
NOTE - CALCULATION OF EXTENSIONS AND RETURNS ................................................................................... 174 
APPX 10 
LIST OF PAPER TO FOLLOW (P2F) ITEMS .............................................................................................. 175 
APPX 10.1 
FILE NAME CONVENTION ............................................................................................................................. 175 
APPX 10.2 
FILE STRUCTURE ......................................................................................................................................... 175 
APPX 10.3 
RECORD FORMATS ...................................................................................................................................... 176 
Appx 10.3.1 
File Summary Record ....................................................................................................................... 176 
Appx 10.3.2 
Item Record ...................................................................................................................................... 176

<!-- Page 13 -->

 
CTS Clearing House Interface – Specification 
 
 
13 
1 Introduction 
 
The CTS Clearing House Interface (CHI) provides an easy-to-use and standardised connectivity between 
the capture/drawee bank systems of a Bank to the RBI/NPCI Clearing House (CH). It provides a gateway 
for conduit of data and images. It provides the required validation to ensure that the data entering the CH 
is free of operational errors. 
 
RBI/NPCI will provide or facilitate to provide each Bank participating in the clearing process with a license 
to install the CHI software on a server. Each Bank should be associated with a CHI for communication to 
the CH. It is the responsibility of each Commercial Bank (or its designate) intending to participate in the 
Cheque Truncation System, to procure the required hardware, hardware security modules (HSM), 
connectivity equipment and base platform software (Operating System, Database, Application Server etc). 
It is also the responsibility of the bank to arrange for installation, connectivity as agreed between NPCI & 
Banks and certification services from the vendors most suited to perform these services. 
 
This document is intended to provide an overview of the CHI application, present the hardware platform 
sizing and software required at the CHI that will allow a bank to connect itself to the CH for the CTS 
system. Appendix-A in this document provides the interfacing specification between External systems 
(Capture Systems & Drawee bank systems) and the CHI. 
 
The Interface Specification in Appendix-A is subject to modification as and when errors/concerns and 
enhancements are identified by RBI/NPCI, Banks or NCR.

<!-- Page 14 -->

 
CTS Clearing House Interface – Specification 
 
 
14 
2 CTS Architecture 
 
The following is the high level overview of the CTS System. 
 
 
 
 
The following paragraphs describe the high-level data content & data flow through the overall solution.  The 
numbers denote the steps in this process and are summarized below. 
 
Step1 
Forward Presentments 
 
 
Note: 
The Capture system feature|function is out-of-scope for this document. 
 
 
Note: 
The following ASSUMPTIONS apply to the Capture File set. 
 
the capture files are not encrypted.  They are sent in-the-clear to the CHI. 
 
 
Note: 
The following ASSUMPTIONS apply to the captured item data. 
 
the captured item data (MICR lines, images) may-or-may-not be digitally signed. 
 
There will be 3 image views of each item (grayscale front, binary front, binary 
back) 
 
 
Note: 
Physical Item ‘endorsement’ is to consist of the following: 
- 
Presentment Date of the item (ddmmyyyy) 8 N 
- 
Clearing Type 2 N 
- 
ISN (Item Seq No) consisting of: 
o Sorter ID 6 N 
o Run Number 2 N 
o Sequence Number 6 N  
- 
Truncating / Presenting BankBranch Routing Number 9 N  (per operation 
guidelines)

<!-- Page 15 -->

 
CTS Clearing House Interface – Specification 
 
 
15 
- 
IFSC (Indian Financial System Code) 11 AN (where ‘IFSC = all ‘0’ if IFSC does 
not exist.’) 
 
 
 
Capture File set shall conform to Capture Interface Specification in Appendix - A.  The 
basic details of the Capture File set are: 
 
an XML file, containing financial data for exchange, possibly capture-generated 
digital signature information of MICR, and pointer into the IBF file 
 
an IBF file, containing the images, possibly capture-generated digital signature 
information of images 
 
 
 
The ECPIX Gateway (CHI) has file folders for use by the capture modules and drawee 
modules of the bank, to send/receive data. 
It is the responsibility of the banks capture and drawee modules to get and put files 
using one of the methods as outlined in “Appendix 3.2 Connectivity For File transfer”. 
 
 
 
Capture File set may be either of ‘unsorted’ (mixed-bag) batch of items & data; or 
‘sorted’ batch of items & data. 
 
 
 
Capture file shall require Bank-Of-First-Deposit ADDEND A records.   
The Electronic Endorsements ADDEND C records are not required. 
Note:  RBI/NPCI requires that the cheques are physically endorsed, so endorsement 
data is visible in the image.  No electronic endorsements are needed. 
 
 
 
 
Step2 
Process File Set 
 
 
 
CHI Server shall ingest/process a Capture File set.  
 
 
Note: 
RBI/NPCI requires the system to ensure that any data received for processing, is 
unchanged throughout the life of that data.  To this end, Digital Signatures are used as 
follows: 
 
 
A digital signature of the Financial data (aka MICR Fingerprint) is calculated by the 
CHI 
 
 
A digital signature of each image view is calculated by the CHI. 
 
 
Note: 
CHI generated digital signatures will be used in ensuring data is unchanged as per 
RBI/NPCI’s business requirement. 
 
 
 
‘Digital signature placeholder positions’ shall be provided within the CTS system for 
storage of any pre-existing (capture generated) digital signature data.   
 
There may exist 1 ‘placeholder’ for each image view, and 1 ‘placeholder’ for the MICR 
Fingerprint. 
 
The Bank can choose to use/fill these placeholders with digital signatures. 
 
The ECPIX system passes along all digital signatures (CHI generated as well as capture 
generated ‘placeholders’) throughout the processing.  The CTS Central Archive system 
stores all digital signatures. 
 
 
 
RBI/NPCI has provided a 25 character (alphanumeric) ‘User Field’ for purposes 
important to the commercial bank. This ‘user field’ is ‘pass-through’ for all of CTS 
processing. This ‘user field’ is stored in the CTS Central Archive index for research. 
 
 
 
CHI Server shall perform item data validation on each item within the Capture File set, 
specified in detail in the ECPIX (CHI) Requirements section (below).

<!-- Page 16 -->

 
CTS Clearing House Interface – Specification 
 
 
16 
 
 
 
CHI Server shall perform IQA on each item within the Capture File set, details of the IQA 
tests are in later sections in this document. 
 
 
 
For purposes of handling the same capture file that was submitted multiple times, the 
CHI Server shall perform Duplicate Detection on each item within the Capture File set.   
 
This duplicate detection is performed based on a UDK (Unique Document Key 
consisting of: Presentment Date, PresentingBank Routing Number, Cycle Number and 
Item Sequence Number).  All items that are detected as UDK duplicates are returned to 
the capture system as ‘rejected items’. 
 
 
The items are assigned to an appropriate clearing session that is open and inherit a 
‘session date’ that is the business date of the session.  If there is no appropriate session 
that is open, then those items wait at the CHI until such a session opens. 
Capture shall use SessionDate, CLOSE_RECEIVING_TIME of the Session and 
SessionExtensionHrs for the session to calculate the maximum return period. 
A validation of the items Presentment Date vs the items session date is performed and 
items that exceed a system-limit are rejected. 
 
 
Step3 
Outward Exchange Files (Outclearings) 
 
 
 
CHI Server shall create an Exchange File set. 
 
The Exchange File set shall be encrypted, and digitally signed. 
 
 
Exchange File set shall contain the following: 
 
an ebXML container (aka an ‘FDD’) – holds the ‘financial settlement data 
and Images’ 
 
 
Step4 
Process File Set 
 
 
 
CH Server shall ingest/process an Exchange File set. 
 
 
 
CH Server shall perform decryption and digital signature validation of the Exchange File 
set as standards by RBI/NPCI. 
 
 
 
CH Server shall perform verification and digital signature validation of each item in the 
Exchange File set as standards by RBI/NPCI. 
 
 
 
For purposes of handling the same exchange file being submitted multiple times, the CH 
Server shall perform Duplicate Detection on each item within the Exchange File set.  
This duplicate detection is performed based on the UDK.  All items that are detected as 
UDK duplicates are ignored. 
 
 
 
Step5 
Inward Exchange Files (Inclearings) 
 
 
 
CH Server shall create an Exchange File set of Financial data for transmission to the 
CHI.  This is done after settlement is approved. 
 
 
Note:  
The Exchange files for Image data are created throughout the clearing process and 
transmission takes place in the background throughout the clearing process. 
 
 
 
The Exchange File set shall be encrypted, and digitally signed. 
 
 
Note: 
Exchange File set details are the same as step 3 previous.

<!-- Page 17 -->

 
CTS Clearing House Interface – Specification 
 
 
17 
 
Step6 
Process File Set 
 
 
 
CHI Server shall ingest/process an Exchange File set. 
 
 
 
CHI Server shall perform decryption and digital signature validation of the Exchange File 
set as standards by RBI/NPCI. 
 
 
 
CHI Server shall ensure valid digital signatures exist for each item in the Exchange File 
set as standards by RBI/NPCI 
 
 
 
For preventing the same exchange file from being submitted multiple times, the CHI 
Server shall perform Duplicate Detection on each item within the Exchange File set.  
This duplicate detection is performed based on the UDK. All items that are detected as 
UDK duplicates are ignored. 
 
Step7 
Drawee Bank (Inward) 
 
 
 
CHI Server shall create a Host/Posting File set that can be used by automated Drawee 
Bank Modules for inward processing at the receiving CHI. 
 
 
 
Host/Posting File set shall conform to details in Appendix - A. 
 
Step8 
Outward Return Request File 
 
 
 
A CHI will accept returns for the presented data (within the specified return cycle) from 
either: 
 
the CHI Branch module (interactive web session); or 
 
from any external system via the Return Request File interface provided. 
 
 
 
Return File set shall conform to details in Appendix – A. 
 
Step9 
Outward Exchange Files (Outward Returns) 
 
 
 
CHI Server shall create an Exchange File set. 
 
 
 
The Exchange File set shall be encrypted, and digitally signed. 
 
 
 
Exchange File set shall contain the following: 
 
an ebXML container (aka an ‘FDD’) – holds the ‘financial settlement data’ 
 
Step10 
Inward Exchange Files (Inward Returns) 
 
 
 
CH Server shall create an Exchange File set of Financial data for transmission to the 
CHI.  This is done after settlement is approved. 
 
 
 
The Exchange File set shall be encrypted, and digitally signed. 
 
 
 
Exchange File set shall contain the following: 
 
an ebXML container (aka an ‘FDD’) – holds the ‘financial settlement data’ 
 
Step11 
Inward Return 
 
 
 
A CHI will create the inward returns for external systems via the Inward Return File 
interface provided.

<!-- Page 18 -->

 
CTS Clearing House Interface – Specification 
 
 
18 
 
Inward Return File set shall conform to details in Appendix – A.

<!-- Page 19 -->

 
CTS Clearing House Interface – Specification 
 
 
19 
3 CHI Feature Functionality 
This section provides details of the CHI application functionality. Detailed operator manuals are available. 
The key characteristics on which the CHI has been designed are as follows:  
 
 
Easy to use Interface 
 
Published Interface (Appendix – A ) to external systems 
 
Encryption of data, signing of exchange files containing outward cheques or returns for clearing 
to be sent to CH ensuring confidentiality either on network or using media (CDROM/DVD) 
 
Validation of presentment data before transmission to the CH 
 
Access to CH for research, report and broadcasts. 
 
Listed below is the main functionality that a CHI performs.  
 
a. Accept cheque data and images in manageable lots from the Capture systems 
b. Validate, Analyze, Sort, Merge and send batched sets of data and images to the CH 
c. Confirm delivery and acceptance of sent batches 
d. Provide scrutiny of session and current ongoing activities at the CH 
e. Retrieve inward cheque data and images from the CH 
f. Provide a file Interface to the host bank’s in-clearing system to deliver received data 
g. Accept ‘returns’ to communicate exceptions decisions to the Presenting Bank through the CH. 
 
A drawee bank module can use the RRF file to send a list of unpaid items to the CHI (see 
section 3.4 below) 
 
Branches can login to the CHI webserver, and mark returns using the “Online Marking of 
Returns” module (see section 5.1 below) 
 
CHI Supervisor can login to the CH, navigate down through their inward files and perform 
“Pre-Settlement Returns”. 
 
CH Supervisor can research items, and then mark returns. (this is only used in exceptional 
circumstances, at the discretion of RBI/NPCI). 
h. Accept ‘extensions’ to communicate a need to extend making final decisions to the Presenting Bank 
through the CH. 
 
A drawee bank module can use the ERF file to request extensions for items drawn upon it.  
The CH extensions can be for reasons of holiday, further researching needed, physical 
paper requests etc. 
i. 
Provide external touch points to Presenting and Drawee Bank Systems. 
 
3.1 Daily Processing Timelines 
 
The CHI will support the processing timelines recommended by RBI/NPCI. The session timings are 
flexible and can be changed by RBI/NPCI to suit clearing requirements. 
A session has a Clearing Cycle Length that does not include an Extension period.  An Extension 
Request will extend the return cycle period based on the clearing rules and the holiday calendar. 
 
3.2 CHI for Outward Presentment 
The Outward presentment deals with accepting forward presentment data and images from the banks 
image capture system and exchanging them at the CH. 
 
CHI performs the following steps during the outward presentment workflow. 
 
i. 
Receive cheque MICR data in xml file and corresponding cheque image data in a binary file 
from image based capture unit that meets the standards stipulated by RBI/NPCI.  
ii. Register the files received in step i and transfer them to their specified directories

<!-- Page 20 -->

 
CTS Clearing House Interface – Specification 
 
 
20 
iii. Load, validate, authenticate and analyze (IQA Defect tests – See section on IQA later in this 
document) the received data and images 
iv. Digitally sign the Financial and each item view of the Image data 
v. Sort the MICR data and their related images as per drawee bank and payment type and 
create batches 
vi. Validate the MICR data against the session window to which they will be added at the CH 
vii. Build financial exchange files for the MICR data and image exchange files for the cheque 
image data 
viii. Transmit the above built exchange files via network or media  
ix. Process the acknowledgement from the CH and take appropriate action for informing the 
operator on the status of the transmission and loading status of the file  
3.3 CHI for Inward Presentment 
The Inward presentment deals with accepting inward presentment data and images from the CH and 
providing data in the form of files for use within the bank’s in-clearing (drawee bank) system. 
 
CHI performs the following activities during the inward presentment workflow. 
 
i. 
Receive inward financial data exchange files and image exchange files from the CH. 
ii. Authenticate and load the exchange file data into the system 
iii. Send an error exchange file to the CH if the inward financial data exchange file or image 
exchange file failed decryption or authentication 
iv. Send an acknowledgement exchange file to the CH if the inward financial data exchange file 
or image exchange file gets successfully loaded 
v. Validate the digital signatures on the MICR and Image Data 
vi. Generate files for interfacing with the bank’s inclearing or exception processing system 
3.4 CHI for Outward Returns 
The Outward returns deals with accepting outward return data from the bank’s inclearing or exception 
handling system. The return data is provided in a file known as Return Request file. 
 
CHI performs the following activities during the outward returns workflow. 
 
i. 
Receive return request files from the bank’s in-clearing system 
ii. Load the file and validate return data against the session window they will be added to at the 
CH 
iii. Build return Exchange file for the validated return data (This type of exchange file is devoid 
of any images and contains only the financial data and return reason codes for the returned 
cheque) 
iv. Transmit the above built exchange file via network or media depending upon system 
settings 
v. Process the acknowledgement from the CH and take appropriate action for informing the 
operator on the status of the transmission and loading status of the file  
3.5 CHI for Inward Returns 
The Inward returns deals with accepting inward return data from the CH and sharing this data in the form 
of return files with the bank’s inward return processing system. 
 
CHI performs the following activities during the inward returns workflow. 
 
i. 
Receive inward return financial data exchange files from the CH. 
ii. Authenticate and load the exchange file data into the system 
iii. Send an error exchange file back to the CH if the inward return financial data exchange file 
failed decryption or authentication

<!-- Page 21 -->

 
CTS Clearing House Interface – Specification 
 
 
21 
iv. Send a acknowledgement exchange file back to the CH if the inward return financial data 
exchange file gets successfully loaded 
v. Generate Return files comprised of received inward return financial for interfacing with the 
bank’s inward return processing system. 
3.6 CHI User Roles 
The proposed CHI has user interfaces dedicated to the operations of the system.  
 
Images flow through the system unattended. All operations in the CHI workflow operate in both Automatic 
modes thus making the CHI an unattended system. 
 
The administration of the CHI processes is shared between the following four types of users: 
 
a. System Administrator 
 
System Administrator is the Windows operating system administrator who installs the CHI 
application and creates users and groups. 
 
This user does not have any access to CHI application but is the super-administrator handling 
system and Operating system level exceptions and functionalities. 
 
System Administrator account is also used to manage the user privileges of other users created at 
an Operating system level. 
 
b. Supervisor 
 
Supervisor is the super-user of the CHI Application. Role based security is used to grant 
privileges to the Supervisor by the System Administrator. 
 
Supervisor is the only user enabled to monitor and view the clearing session going on at the CH. 
Creation of accounts for the Branch users will be performed by the Supervisor. 
 
Besides, some system level exceptions require the Supervisor privilege to handle and recover 
from exceptions. 
 
c. Operator 
 
Operator is the user that handles routine activities within the CHI Application. Role based security 
is used to grant privileges to the Operator by the System Administrator. 
 
Some of the functions handled by the operator include monitoring the application, maintaining the 
system, handling exceptions, recovering errors and informing the supervisor when in need of a 
critical decision. 
 
d. Application Administrator 
 
Application Administrator takes care of the application level maintenance and support activities of 
backup, cleanup, key generation and audit report generation. 
 
Application Administrator is also the Database administrator to manage and maintain the 
database. 
 
e. Branch Users 
 
Branch users are managed and maintained within the CHI Application by the Supervisor. Branch 
users connect to the Branch interface webserver provided by the CHI to perform branch level

<!-- Page 22 -->

 
CTS Clearing House Interface – Specification 
 
 
22 
activities such as Online returns, Online retrieval of branch posting data, Online upload of Return 
Request data.  
3.7 Validation 
 
The data is validated for its completion and correctness to conform to the details defined by the Interface 
Specification in Appendix – A. 
 
3.7.1 Presentation Validations: 
A high-level summary of the validations that are performed during presentation are: 
 
InterCity validation: 
1) Drawee bank code obtained from drawee bank sort code exists in ‘bank master’ table 
2) Drawee city code obtained from drawee bank sort code is eligible for intercity clearing in ‘city 
master’ table 
3) Bank of First Deposit and Drawee bank cannot be in the same city 
4) Bank of First Deposit city is eligible for intercity clearing in ‘city master’ table 
 
 
“PresentingBankRoutNo” field validation: 
This validation ensures that the PresentingBankRoutNo is a valid bank under the CHI, has not 
been BLOCKED or SUSPENDED and is in the CLEARING state. 
 
 
Clearing_Type and DocType validation: 
This validation ensures that the values within the ClearingType and DocType fields correspond 
to the values  mentioned in the CHI Interface. 
 
 
Item Presentment Date vs item session date validation: 
This validation ensures that the difference in days between Presentment/Capture date and 
Session date does not exceed the RBI/NPCI set limit. This validation also ensures that the 
presentment date of the items is not greater than the Clearing Date. 
 
 
IQA and number of image views validation: 
1) This validation ensures that the image views sent by capture are of the correct specification 
and their IQA defect test results fall within the purview of thresholds set by RBI/NPCI. 
2) This validation ensures that for items presented with the IQAIgnoreInd set to ‘1’, then the 
DocType must also be set to ‘C’ indicating ‘Image-to-follow-with-paper-to-follow’. 
 
 
ON_US check: 
This validation ensures that ON_US cheques are processed as per the RBI/NPCI defines 
ON_US settings for Banks and CHI. 
 
 
Payor Routing Code validation: 
This validation ensures that the Payor Routing code is valid, so that the cheque can be routed to 
the correct financial institution and its CHI.  
 
 
Wrongly Presented Item check: 
This validation ensures that the Bank code of Payor Routing code is a valid bank participating in 
clearing. If the bank does not participate directly in clearing, it should designate a participating 
bank to receive its cheques using translation rule. 
 
 
Transaction Code validation: 
This validation ensures that the Transaction Code is a valid code for the particular clearing type 
in the CHTables.

<!-- Page 23 -->

 
CTS Clearing House Interface – Specification 
 
 
23 
 
Duplicate item validation: 
This validation ensures that the Unique Document Key (UDK) of the item is not a duplicate of an 
item already in the system. 
 
 
Paper to follow validation: 
A new validation shall be introduced to ensure that BOFD city code equals drawee city code for 
P2F cheques. This ensures that paper to follow transactions are allowed only within the city and 
not across cities. 
 
 
Drawee city validation: 
This validation obtains the value of the CBS flag for the drawee bank. This validation will not be 
performed if the CBS flag is enabled for drawee bank. If the CBS flag is not enabled, this 
validation ensures that drawee city code obtained from the drawee bank sort code is eligible for 
clearing in the ‘city master’ table for that ClearingType.   
 
3.7.2 Return and Extension Validations: 
A high-level summary of the validations that are performed during returns and extensions are: 
 
Original item exists validation: 
This validation ensures that the referenced item is in the system 
 
 
Extension Period validation: 
1) that the Extension Period is within the maximum extension period allowed 
2) that the Extension was requested within the configured number of hours from inward 
presentment  
3) that the Extension Reason code is valid  
4) that the Item is not extended before 
5) that the item is not returned before 
Note : Its the banks onus to develop capabilities in their capture systems of marking extension 
city or bank wise 
 
 
Return validation: 
1) that the Return Period is within the maximum return period allowed 
2) that the item has not already been subject to Unwinding (bank put in SUSPENDED mode) or 
Bank Exclusion at the CH 
3) that the Return Reason code is valid 
4) that the item is not returned before 
 
 
 
3.8 IQA Defect Tests 
 
The following IQA Defect Tests will be carried out on the images at the CHI. 
 
Capture solutions must ensure that the IQA thresholds in their solutions are PARAMETERISED and can be 
changed to the values communicated by RBI/NPCI.  RBI/NPCI will be monitoring and adapting these 
thresholds for the Indian Cheque environment.  Any thresholds given in the table below are the current values.  
Banks will have to contact RBI/NPCI in order to receive the most-up-to-date values for the Indian Cheque 
environment.   
 
DEFECT TESTS 
  
  
  
  
Gray Front 
Binary Front 
Binary Rear 
Partial Image 
0 
0 
0 
Excessive Image Skew 
20 
20 
20

<!-- Page 24 -->

 
CTS Clearing House Interface – Specification 
 
 
24 
Piggyback Image 
n/a 
n/a 
n/a 
Streaks and|or Bands 
3 
3 
9 
Bent Corner 
20 
20 
20 
Below Minimum Image Size 
44236 
6553 
2457 
Exceeds Maximum Image Size 
68812 
15974 
3687 
Additional tests for RBI/NPCI 
  
  
  
Binary Too Light 
n/a 
3 
1 
Binary Too Dark 
n/a 
39 
39 
Image Height Mismatch 
10 
10 
10 
Image Length Mismatch 
10 
10 
10 
Below Minimum Image length 
150 
150 
150 
Exceeds Maximum Image length 
215 
215 
215 
Below Minimum Height 
60 
60 
60 
Exceeeds Maximum Height 
105 
105 
105 
Torn Corner 
20 
20 
20 
  
  
  
  
 
 
Note : “Below Minimum Image Size” and “Exceeds Maximum Image Size” values have been calculated as -
20% and +20% of the imagesize mentioned in previous releases of CHI IFS. 
 
The following table provides an explanation of the test, the thresholds and computed metrics. 
 
 
Test 
Threshold 
Units 
Range 
ANSI X9.37 
Partial Image 
Maximum allowable percentage of area of 
the image detected to be missing 
Percent 0-100 
ANSI X9.37 
Excessive Image 
Skew 
Maximum absolute value of the allowable 
angle of skew. Images with detected 
skew above this angle are flagged as 
suspects. 
Tenths 
of 
degree 
0-900 
ANSI X9.37 
Piggyback Image 
None 
 
 
ANSI X9.37 
Streaks and or 
bands 
Maximum allowable height of horizontal 
streaks and or bands detected in the 
image. 
Mm 
0-image 
height 
NCR Bent 
Corners 
Maximum allowable intrusion distance.   
This distance is measured on a 45 degree 
angle from the corner of the image. 
Mm 
0-100 
ANSI X9.37 
Below minimum 
image size 
Minimum allowable binary image size.   
Minimum allowable grayscale image size 
bytes 
0-
LONG_MAX 
ANSI X9.37 
Exceeds 
maximum image 
size 
Maximum allowable binary image size. 
Maximum allowable grayscale image 
size. 
bytes 
0-
LONG_MAX 
NCR Binary too 
light 
Minimum allowable percentage black 
pixels in the image 
Percent 0-100 
NCR Binary too 
dark 
Maximum allowable percentage black 
pixels in the image 
Percent 0-100 
NCR Image 
Height Mismatch 
Maximum allowable difference in image 
heights of all image views of a document. 
Mm 
0-
LONG_MAX 
NCR Image 
Length Mismatch 
Maximum allowable difference in image 
lengths of all image views of a document. 
Mm 
0-
LONG_MAX

<!-- Page 25 -->

 
CTS Clearing House Interface – Specification 
 
 
25 
Test 
Threshold 
Units 
Range 
NCR Below 
Minimum Image 
Length 
Minimum allowable image/document 
length.  This value should be set to the 
length of the shortest document expected 
to be scanned, within an allowable 
tolerance.  Images narrower than this 
length will be flagged as a suspect for this 
test condition. 
Mm 
0-
LONG_MAX 
NCR Exceeds 
Maximum Image 
Length 
Maximum allowable image/document 
length.  This value should be set to the 
length of the longest document expected 
to be scanned, within an allowable 
tolerance.  Images that are longer/wider 
than this length will be flagged as a 
suspect for this test condition. 
Mm 
0-
LONG_MAX 
NCR Below 
Minimum Image 
Height 
Minimum allowable image/document 
height.  This value should be set to the 
height of the shortest document expected 
to be scanned, within an allowable 
tolerance.  Images that are shorter than 
this length will be flagged as a suspect for 
this test condition. 
Mm 
0-
LONG_MAX 
NCR Exceeds 
Maximum Image 
Height 
Maximum allowable image/document 
height.  This value should be set to the 
height of the tallest document expected to 
be scanned, within an allowable 
tolerance.  Images that are taller than this 
height will be flagged as a suspect for this 
test condition. 
Mm 
0-
LONG_MAX 
NCR Torn Corner 
Maximum allowable intrusion distance. 
Mm 
0-100 
 
3.9 Posting File Creation 
 
Once the financial MICR data and corresponding images arrive at the CHI from the CH after the closing 
of a session, the system automatically generates the inclearings file for use in the drawee bank modules 
at the bank. 
3.10 Status Monitor 
3.10.1 
Monitor Status of Data and Images 
 
The CHI allows the supervisor to monitor the status of data and image Exchange files sent to the CH. 
 
The CH sends a positive, negative or error acknowledgement to the sending CHI depending upon 
whether the data within the Exchange file gets loaded and validated successfully against the session 
window. 
 
The CHI receives and loads the acknowledgement file and allows the supervisor to re-build and re-send 
the exchange file or take any other appropriate action depending upon the error identified in the 
acknowledgement file and displayed on the Operator Session Monitor window. 
3.10.2 
Monitor Status of Sessions at CH 
The CHI allows the system supervisor to monitor the status of the current on-going sessions at the CH. 
The supervisor can monitor the following details about each session.

<!-- Page 26 -->

 
CTS Clearing House Interface – Specification 
 
 
26 
 
i. 
View the financial data and images sent from the CHI (outward) and received at the CH 
ii. View the financial data and images received by the CH (inward) that will be transmitted to 
the CHI. 
iii. View Net / Gross Settlement figures for institutions associated with this CHI. 
iv. View and Download various reports generated at the CH. 
 
3.11 Media Based Transmission of Exchange Files 
 
In the event of a network failure, the application allows for data and image files to be exchanged with the CH 
using different types of Electronic medium (Magnetic and Optical). The same PKI infrastructure that is used 
during network transmission is used to create the files for transfer using physical media options.

<!-- Page 27 -->

 
CTS Clearing House Interface – Specification 
 
 
27 
4 Interface with Capture/Drawee Bank Systems 
 
The CHI is capable of supporting image based capture systems that meets the standards stipulated by 
RBI/NPCI. To make it simple to use, a file based communication medium is used to accept capture cheque 
MICR and image data. 
 
The protocol used for communication and transmission of files is FTP. Each capture uses a predefined account 
(set-up during installation) to send files to the CHI FTP directory from which the loading process takes place in 
the CHI application. The capture system informs the successful transmission of files by placing a ‘.done’ file in 
the target directory. The transmitted data and image files will be picked up by the CHI for processing only after 
it detects the presence of the corresponding ‘.done’ file. 
 
The details of the file interface is available in Appendix-A.

<!-- Page 28 -->

 
CTS Clearing House Interface – Specification 
 
 
28 
5 Interface with Bank Branch 
The CHI enables the various branches defined in its database to access it using a web server and process 
inward data and images.  
 
The following functionality is provided using this interface. 
5.1 Online marking of returns 
The CHI user can mark the cheque returns online using a browser interface to the CHI. An appropriate return 
reason code can be chosen and the user can authorize to return the cheque. 
 
The system internally generates a Return Request file, adds it to a session window with a payment type 
indicating a return to be accounted in the next settlement. 
5.2 Online retrieval of branch posting data 
This feature is useful for branches that have access to computers but have a problem maintaining live online 
connectivity with the CHI web server.  
 
Such branches can opt to download all their inward posting data from the CHI server at a designated time after 
session closure and then import this data into any branch returns processing software.  
5.3 Online upload of Return Request data 
This section of the CHI Branch interface module allows the branch user to submit the Return Request file 
containing the exception items from the branch returns processing software.  
 
The CHI accepts the file and adds it to a session window with a payment type indicating a return to be 
accounted in the next settlement.

<!-- Page 29 -->

 
CTS Clearing House Interface – Specification 
 
 
29 
6 Enquiries 
The research functionality in the CHI supports research screens for locating and viewing data. The duration for 
this data maintained will be for a typical return cycle. The CHI is not intended to become a long-term storage 
and research platform. These screens are all web based. 
 
Users can inquire the following cheques that have passed through the CHI system: 
i. Forward Presentment cheques 
ii. Inward Presentment cheques 
iii. Forward Return cheques 
iv. Inward Return cheques 
 
The research section allows the user to inquire items via the following methods: 
 
a. Research items based on item index 
Item index includes the combination of unique attributes used to identify each item distinctly 
 
 
b. Research items based on MICR data 
MICR data includes fields like Serial Number, Payor Sort Code, Account Number and Amount  
 
c. Research items based on Miscellaneous data 
Miscellaneous data includes other related fields like Return Reason code, Clearing Status, 
MICR repair flag etc.

<!-- Page 30 -->

 
CTS Clearing House Interface – Specification 
 
 
30 
7 Security 
 
The CHI has been designed with the cryptography functions of encryption and digital signatures, using public 
and private keys.  
 
All data interchanged between participants are both digitally signed and encrypted. The PKI infrastructure is 
used for this purpose. The CHI will be integrated with HSM (Hardware Security Module) to provide a higher 
level of security. In HSM, the PKI public and private keys will be stored inside the hardware module thus 
making it inaccessible, tamper proof and highly secure. 
 
The following diagram shows the data flow through ECPIX and the digital signatures that are applied to items 
and files as the data flows. 
 
FDD 
- is (MICR) Financial data & 
MICRFingerPrintDS 
<item> 
  <MICRDS source=”capture”> 
  <MICRDS source=”ECP.PBCC”> 
</item> 
- is Image binary data & image 
digital signatures 
<item> 
  <imageview> 
     <IMAGEDS source=”capture”> 
     <IMAGEDS source=”ECP.PBCC”> 
  </imageview> 
… … … 
</item> 
 
FDD files are: 
- 
encrypted with CH public 
key (the recipient) 
- 
digitally signed with CHI 
private key (the sender) 
FDD 
- is (MICR) Financial data & 
MICRFingerPrintDS 
<item> 
  <MICRDS source=”capture”> 
  <MICRDS source=”ECP.PBCC”> 
</item> 
- is Image binary data & image 
digital signatures 
<item> 
  <imageview> 
     <IMAGEDS source=”capture”> 
     <IMAGEDS source=”ECP.PBCC”> 
  </imageview> 
… … … 
</item> 
 
FDD files are: 
- 
encrypted with CHI 
public key (the recipient) 
- 
digitally signed with CH 
private key (the sender) 
CAPTURE 
(cheques) 
Presenting 
CHI 
CH 
Receiving 
CHI 
CXF 
<item> 
  <MICRDS source=”capture”> 
  <imageview> 
     <IMAGEDS source=”capture”> 
  </imageview> 
… … … 
</item> 
CIBF 
Image binary data 
And 
Image digital signatures 
DRAWEE 
 
PXF 
<item> 
  <MICRDS source=”capture”> 
  <MICRDS source=”ECP.PBCC”> 
  <imageview> 
     <IMAGEDS source=”capture”> 
     <IMAGEDS source=”ECP.PBCC”> 
  </imageview> 
… … … 
</item> 
PIBF 
Image binary data 
And 
Image digital signatures 
 
 
PKI technical details are in accordance with appropriate India Acts & IDRBT practice.  In summary: 
Hash algorithm SHA-256 
Padding algorithm pkcs#1 
RSA asymmetric encryption with 2048 bit key length 
Triple DES (3DES, TDES) symmetric encryption with 168 bit key length 
Certificates in X.509v3 format system certificate 
 
Security is managed by the creation of user role identifiers that will enable the assignment of certain functions 
to users of the system. For users of the CHI webserver, an additional application level security is included to 
only allow users to view the data they are allowed to view.  
 
All Web services are delivered using the SSL communication protocol. 
 
The details of smart card access for CHI shall be described in a separate Security document.

<!-- Page 31 -->

 
CTS Clearing House Interface – Specification 
 
 
31 
8 Reports 
 
The CHI allows connection with the CH to view and download clearing and settlement reports. The reports are 
available in the popular PDF format. Some of the reports available for the CHI generated at the CH are: 
 
a. Outward Items detailed Report – A comprehensive detailed report that lists each item 
presented by the CHI on a per session basis 
 
b. Inward Clearing Items - Branchwise Report – A comprehensive detailed report that lists each 
item received by branches in a bank on a per session basis 
 
c.  Outward Items Summary Report – A concise report summarizing items presented by the CHI 
on a per session basis 
 
d. Inward Items Summary Report – A concise report summarizing items received by the CHI on a 
per session basis 
 
e. Gross/Net Settlement  Report – Report detailing out the settlement position of the bank along 
with details per payment type on a per session basis 
 
f. 
Branch Settlement Report – Report that summarizes the outward and inward items for every 
branch in a bank on a per session basis 
 
g. Pre-Settlement Return Items Report - A comprehensive detailed report that lists each item 
presented by the CHI that has been returned at the CH before final settlement on a per 
session basis 
 
h. Clearing House Balance Register Report – A concise report summarizing the settlement 
position for a bank on a per session basis 
 
i. 
Duplicate Instruments Report – A comprehensive detailed report that lists the duplicate items 
sent and received by the CH on a per session basis 
 
j. 
Clearing Items Extension List – A detail report that list items which have been extended by the 
CH for a given business date. 
 
k. Inward Returns Clearing Items –Branchwise report - A comprehensive detailed report that lists 
each return item received by branches in a bank on a per session basis 
 
l. 
Outward clearing branch wise - contains BOFD branch wise details of presented items.  
 
m. Outward clearing branch wise XLS format - contains BOFD branch wise details of presented 
items. Format for this report is XLS 
n.  
 
 
The CHI also has an option of manually generating audit and exception reports. The following reports are 
generated locally at the CHI: 
 
a. Application Audit Report – Contains the audit of processes occurring within the CHI like 
loading of files, building of files, validation of data, IQA and creation of inward data 
 
b. Exception Audit Report – Contains the list of exceptions encountered during processing of 
data and images

<!-- Page 32 -->

 
CTS Clearing House Interface – Specification 
 
 
32 
c. User Activity Audit Report – Contains the audit of user actions and operations performed in the 
system by each user 
 
The CHI also has an option of scheduling daily reports. The following reports are generated locally at the 
CHI: 
 
a. Report on Items Failing Data Validation – Contains the list of items that were rejected at CHI 
 
b. Report of items detected as ‘Government Cheques’ – Contains the list of government cheques 
 
c. IQA Pass report – A detailed report of every IQA test results for all items that have passed the 
IQA validations. 
 
d. IQA Fail report - A detailed report of every IQA test results for all items that have failed the 
IQA validations. 
 
e. Paper to follow report – A script will be available to generate a csv file containing details of 
paper to follow cheques 
 
f. 
MICR Reject Repair Report - contains item details which got rejected due to MICR validation 
failures. Format for this report is PDF 
 
g. MICR Reject Repair Report XLS format - contains item details which got rejected due to 
MICR validation failures. Format for this report is XLS 
 
h. SAN Validation Report – contains item details which got rejected due to short account 
validation failures Format for this report is PDF and RPT

<!-- Page 33 -->

 
CTS Clearing House Interface – Specification 
 
 
33 
9 Equipment Sizing 
 
Minimum recommended equipment configurations have been provided for five categories. For purposes 
of selecting the category it is essential that the volumes at the CHI should take into account the outward 
and inward items. Thus, upto 10,000 items per day would mean 5000 inward items and 5000 outward 
items. For purposes of total size computation, it is assumed that the average image size per item 
consisting of 3 views is 75 Kbytes (using a Q-Factor between 25-30). Sizing has also taken into account 
that 40% of the total volume at the CHI should be processed in a peak-hour. 
Note: Grid Clearing House shall support any existing 32 bit CHI’s. It is recommended to upgrade the 
existing CHI’s to 64 bit platform. 
 
9.1 Mini CHI (upto 10,000 items/day) 
9.1.1 Hardware 
 
The following provides the guidelines for the sizing of a CHI server that is expected to handle a volume 
of loading 10,000 items/day (4,000 items in a peak hour). 
 
Processor 
 
 
Dual Intel Xeon Processors E5-2637 (2C, 5M Cache, 3.00 GHz, 8.00 GT/s Intel QPI). 
 
Memory 
 
16GB (DDR3, 1600MHz) 
 
Disk Drive Specification  
 
Disk 
RAID 
Drive 
Size 
(GB) 
Internal / External* 
Contents 
1 
RAID 1 
C 
80 
Internal Only 
OS 
2 
RAID 1 
D 
28 
Internal or External 
CHI Binaries, Database tables, data 
F 
10 
Oracle Logs, Index 
3 
RAID 1 
E 
20 
Internal or External 
Oracle Binaries & System tables 
G 
20 
Oracle Logs, data (copy 2) 
K 
30 
Database Backup 
 
*  
Internal:  15K RPM, Internal Drive, RAID on separate disk spindles. 
    
External: 15K RPM, SAN Drive, RAID on separate disk spindles  
 
 
    with SCSI RAID Enabled Backplane (or external SCSI/SAN Fibre Connect) 
 
Please note that the daily database backup should be transferred from disk to tape or backup CHI. 
 
Security Module 
 
LUNA PCIe 7000 HSM from Safenet Inc.

<!-- Page 34 -->

 
CTS Clearing House Interface – Specification 
 
 
34 
9.1.2 Software 
 
Operating System 
 
Microsoft Windows 2008 R2 (64 bit) Standard edition with appropriate CALs to handle the users within 
the Bank. 
 
Note: 1) W2008 R2 (64 bit) Enterprise edition is required if High Availability with Windows Active 
Passive Clustering needs to be configured. 
 
2) Install Windows Server 2008 R2 with Service Pack 1. 
 
Third-Party Software 
 
The CHI requires the following Third-Party software components for its operation. It is the responsibility of 
the commercial banks to procure licenses for these software components. Appropriate software media 
and installation instructions will be provided by RBI/NPCI as part of the CTS project. 
 
No. 
Software 
Version Additional Details 
1 
Oracle Standard Edition - 64bit 
11.2 
5 Named User Licenses 
2 
IBM WebSphere Application Server - Express Edition 
8.0 
280 PVUs 
3 
IPSwitch WSFTP Server1 
7.6 
  
4 
Netal SL4NT Logger 
3.2 
  
5 
CD Creator Software 
 
Roxio or similar 
 
 
Note: Oracle 11.2 Enterprise Edition - 64bit is required if Alternate CHI with Oracle Data Guard needs to 
be configured. 
 
The following Third-Party Software components are included with NCR CHI Software. Commecial Banks 
are NOT required to procure separate licenses for these components.  
 
No. 
Software 
Version Additional Details 
1 
IPSwitch WS FTP Professional 
2006 
 
2 
Crystal Reports 
11.0 
 
3 
Java Runtime Environment (JRE) 
1.5 
 
4 
MSXML 
4.0 
  
5 
PERL 
5.6 
 
6 
MDAC 
2.8 
 
7 
Adobe Reader 
10.0 
 
8 
Oracle Client - 32 bit 
11.2 
 
 
9.2 Small CHI (upto 30,000 items/day) 
9.2.1 Hardware 
 
The following provides the guidelines for the sizing of a CHI server that is expected to handle a volume of 
loading 30,000 items/day (12,000 items in a peak hour). 
 
Processor 
                                               
1 For SFTP File Transfer.It requires IPSwitch WSFTP Server with SSH version 7.6.3 and above.

<!-- Page 35 -->

 
CTS Clearing House Interface – Specification 
 
 
35 
 
Dual Intel Xeon Processors E5-2637 (2C, 5M Cache, 3.00 GHz, 8.00 GT/s Intel QPI). 
 
Memory 
 
16GB (DDR3, 1600MHz) 
 
Disk Drive Specification 
 
Disk 
RAID 
Drive 
Size 
(GB) 
Internal / External* 
Contents 
1 
RAID 1 
C 
80 
Internal Only 
OS 
2 
RAID 1 
D 
56 
Internal or External 
CHI Binaries, Database tables, data 
3 
RAID 1 
E 
22 
Internal or External 
Oracle Binaries & System tables 
G 
22 
Oracle Logs, data (copy 2) 
4 
RAID 1 
F 
15 
Internal or External 
Oracle Logs, Index 
K 
30 
Database Backup 
 
* Internal:  15K RPM, Internal Drive, RAID on separate disk spindles. 
    
  External: 15K RPM, SAN Drive, RAID on separate disk spindles  
 
 
      with SCSI RAID Enabled Backplane (or external SCSI/SAN Fibre Connect) 
 
 Please note that the daily database backup should be transferred from disk to tape or backup CHI. 
 
 
Security Module 
 
LUNA PCIe 7000 HSM from Safenet Inc. 
 
9.2.2 Software 
 
Operating System 
 
Microsoft Windows 2008 R2 (64 bit) Standard edition with appropriate CALs to handle the users within 
the Bank. 
 
Note: 1) W2008 R2 (64 bit) Enterprise edition is required if High Availability with Windows Active 
Passive Clustering needs to be configured. 
2) Install Windows Server 2008 R2 with Service Pack 1. 
 
 
Third-Party Software 
 
The CHI requires the following Third-Party software components for its operation. It is the responsibility of 
the commercial banks to procure licenses for these software components. Appropriate software media 
and installation instructions will be provided by RBI/NPCI as part of the CTS project. 
 
No. 
Software 
Version Additional Details 
1 
Oracle Standard Edition - 64bit 
11.2 
5 Named User Licenses 
2 
IBM WebSphere Application Server - Express Edition 
8.0 
280 PVUs 
3 
IPSwitch WSFTP Server2 
7.6 
 
                                               
2 For SFTP File Transfer.It requires IPSwitch WSFTP Server with SSH version 7.6.3 and above.

<!-- Page 36 -->

 
CTS Clearing House Interface – Specification 
 
 
36 
4 
Netal SL4NT Logger 
3.2 
 
5 
CD Creator Software 
 
Roxio or similar 
 
Note: Oracle 11.2 Enterprise Edition - 64bit is required if Alternate CHI with Oracle Data Guard needs to 
be configured. The following Third-Party Software components are included with NCR CHI Software. 
Commecial Banks are NOT required to procure separate licenses for these components.  
 
No. 
Software 
Version Additional Details 
1 
IPSwitch WS FTP Professional 
2006 
 
2 
Crystal Reports 
11.0 
 
3 
Java Runtime Environment (JRE) 
1.5 
 
4 
MSXML 
4.0 
  
5 
PERL 
5.6 
 
6 
MDAC 
2.8 
 
7 
Adobe Reader 
10.0 
 
8 
Oracle Client - 32 bit 
11.2 
 
 
 
9.3 Medium CHI (Between 30,000 and 100,000 items/day) 
9.3.1 Hardware 
 
The following provides the guidelines for the sizing of a CHI server that is expected to handle a volume 
of loading 100,000 items/day (40,000 items in a peak hour). 
 
Processor 
 
Dual Intel Xeon Processors E5-2637 (2C, 5M Cache, 3.00 GHz, 8.00 GT/s Intel QPI). 
 
Memory 
 
24GB (DDR3, 1600MHz) 
 
Disk Drive Specification 
 
Disk 
RAID 
Drive 
Size 
(GB) 
Internal / External* 
Contents 
1 
RAID 1 
C 
80 
Internal Only 
OS 
2 
RAID 1 
D 
180 
Internal or External 
CHI Binaries, Database tables, data 
3 
RAID 1 
E 
40 
Internal or External 
Oracle Binaries & System tables 
F 
20 
Oracle Logs, Index 
4 
RAID 1 
G 
20 
Internal or External 
Oracle Logs, data (copy 2) 
K 
60 
Database Backup 
 
 
 
* Internal:  15K RPM, Internal Drive, RAID on separate disk spindles. 
   External: 15K RPM, SAN Drive, RAID on separate disk spindles  
 
 
        with SCSI RAID Enabled Backplane (or external SCSI/SAN Fibre Connect)

<!-- Page 37 -->

 
CTS Clearing House Interface – Specification 
 
 
37 
Please note that the daily database backup should be transferred from disk to tape or backup CHI. 
 
Security Module 
 
LUNA PCIe 7000 HSM from Safenet Inc. 
 
9.3.2 Software 
 
Operating System 
 
Microsoft Windows 2008 R2 (64 bit) Standard edition with appropriate CALs to handle the users within 
the Bank. 
 
Note: 1) W2008 R2 (64 bit) Enterprise edition is required if High Availability with Windows Active 
Passive Clustering needs to be configured. 
2) Install Windows Server 2008 R2 with Service Pack 1. 
 
Third-Party Software 
 
The CHI requires the following Third-Party Software for its operation. It is the responsibility of the 
commercial banks to procure licences for these components. Appropriate software media and installation 
instructions will be provided by RBI/NPCI as part of the CTS project. 
 
No. 
Software 
Version Additional Details 
1 
Oracle Standard Edition - 64bit 
11.2 
5 Named User Licenses 
2 
IBM WebSphere Application Server - Express Edition 
8.0 
280 PVUs 
3 
IPSwitch WSFTP Server3 
7.6 
  
4 
Netal SL4NT Logger 
3.2 
  
5 
CD Creator Software 
 
Roxio or similar 
 
 
Note: Oracle 11.2 Enterprise Edition - 64bit is required if Alternate CHI with Oracle Data Guard needs to 
be configured. 
 
Following Third-Party Software components are included with NCR CHI Software. Commecial Banks are 
NOT required to procure separate licenses for these components.  
 
No. 
Software 
Version Additional Details 
1 
IPSwitch WS FTP Professional 
2006 
 
2 
Crystal Reports 
11.0 
 
3 
Java Runtime Environment (JRE) 
1.5 
 
4 
MSXML 
4.0 
  
5 
PERL 
5.6 
 
6 
MDAC 
2.8 
 
7 
Adobe Reader 
10.0 
 
8 
Oracle Client - 32 bit 
11.2 
 
 
 
                                               
3 For SFTP File Transfer.It requires IPSwitch WSFTP Server with SSH version 7.6.3 and above.

<!-- Page 38 -->

 
CTS Clearing House Interface – Specification 
 
 
38 
9.4 Large CHI (Between 100,000 and 250,000 items/day) 
9.4.1 Hardware 
 
The following provides the guidelines for the sizing of a CHI server that is expected to handle a volume 
of loading 250,000 items/day (100,000 items in a peak hour). 
 
Application Server 
 
Processor 
Dual Intel Xeon Processors E5-2637 (2C, 5M Cache, 3.00 GHz, 8.00 GT/s Intel QPI). 
 
Memory 
32GB (DDR3, 1600MHz) 
 
Disk Drive Specification 
 
Disk 
RAID 
Drive 
Size 
(GB) 
Internal / External* 
Contents 
1 
RAID 1 
C 
80 
Internal Only 
OS 
D 
20 
Internal Only 
CHI Binaries 
2 
RAID 1 
J 
225 
Internal or External 
CH Data Files 
3 
RAID 1 
K 
225 
Internal or External 
CH Data Files 
 
* Internal:  15K RPM, Internal Drive, RAID on separate disk spindles. 
External: 15K RPM, SAN Drive, RAID on separate disk spindles with RAID Enabled Backplane and 
external SAN Fibre Connect 
 
Security Module 
 
LUNA PCIe 7000 HSM from Safenet Inc. 
 
Database Server  
 
Processor 
 
Dual Intel Xeon Processors E5-2637 (2C, 5M Cache, 3.00 GHz, 8.00 GT/s Intel QPI). 
 
Memory 
 
32GB (DDR3, 1600MHz) 
 
Disk Drive Specification 
 
Disk 
RAID 
Drive 
Size 
(GB) 
Internal / External* 
Contents 
1 
RAID 1 
C 
80 
Internal Only 
OS 
D 
20 
Internal Only 
Oracle Binaries 
2 
RAID 1 
E 
25 
Internal or External 
Oracle System Tables, Control Files 
F 
30 
Oracle Redo Log Archive 
3 
RAID 1 
G 
20 
Internal or External 
Oracle Redo Logs 1, Data, Control 
Files

<!-- Page 39 -->

 
CTS Clearing House Interface – Specification 
 
 
39 
Disk 
RAID 
Drive 
Size 
(GB) 
Internal / External* 
Contents 
4 
RAID 1 
H 
20 
Internal or External 
Oracle Redo Logs 2, Index, Control 
Files 
5 
RAID 1 
I 
15 
Internal or External 
Undo Tablespace 
6 
RAID 1 
K 
150 
Internal or External 
Database Backup 
 
 
* Internal:  15K RPM, Internal Drive, RAID on separate disk spindles. 
External: 15K RPM, SAN Drive, RAID on separate disk spindles with RAID Enabled Backplane and 
external SAN Fibre Connect 
 
Please note that the daily database backup should be transferred from disk to tape or backup CHI. 
9.4.2 Software 
 
Application Server  
 
Operating System 
 
Microsoft Windows 2008 R2 (64 bit) Standard edition with appropriate CALs to handle the users within 
the Bank. 
 
Note: 1) W2008 R2 (64 bit) Enterprise edition is required if High Availability with Windows Active 
Passive Clustering needs to be configured. 
2) Install Windows Server 2008 R2 with Service Pack 1. 
 
Third-Party Software 
 
The CHI requires the following Third-Party software components for its operation. It is the responsibility of 
the commercial banks to procure licenses for these software components. Appropriate software Media 
and installation instructions will be provided by RBI/NPCI as part of the CTS project. 
 
 
No. 
Software 
Version Additional Details 
1 
IBM WebSphere Application Server - Express Edition 
8.0 
280 PVUs 
2 
IPSwitch WSFTP Server4 
7.6 
  
3 
Netal SL4NT Logger 
3.2 
  
4 
CD Creator Software 
 
Roxio or similar 
 
 
The following Third-Party Software components are included with NCR CHI Software. Commecial Banks 
are NOT required to procure separate licenses for these components.  
 
No. 
Software 
Version Additional Details 
1 
IPSwitch WS FTP Professional 
2006 
 
2 
Crystal Reports 
11.0 
 
3 
Java Runtime Environment (JRE) 
1.5 
 
4 
MSXML 
4.0 
  
5 
PERL 
5.6 
 
                                               
4 For SFTP File Transfer.It requires IPSwitch WSFTP Server with SSH version 7.6.3 and above.

<!-- Page 40 -->

 
CTS Clearing House Interface – Specification 
 
 
40 
6 
MDAC 
2.8 
 
7 
Adobe Reader 
10.0 
 
8 
Oracle Client - 32 bit 
11.2 
 
 
 
Database Server  
 
Operating System 
 
Microsoft Windows 2008 R2 (64 bit) Standard edition with appropriate CALs to handle the users within 
the Bank. 
 
Note: 1) W2008 R2 (64 bit) Enterprise edition is required if High Availability with Windows Active 
Passive Clustering needs to be configured. 
2) Install Windows Server 2008 R2 with Service Pack 1. 
 
Third-Party Software 
 
The CHI requires the commercial versions of the following Third-Party Software for its operation. It is the 
responsibility of the commercial banks to procure a license of software for installation. Appropriate 
Software Media and Installation instructions will be provided by RBI/NPCI as part of the CTS project. 
 
No. 
Software 
Version Additional Details 
1 
Oracle Standard Edition - 64bit 
11.2 
5 Named User Licenses 
2 
Netal SL4NT Logger 
3.2 
 
 
 
Note: Oracle 11.2 Enterprise Edition - 64bit is required if Alternate CHI with Oracle Data Guard needs to 
be configured. 
 
The following Third-Party Software components are included with NCR CHI Software. Commecial Banks 
are NOT required to procure separate licenses for these components.  
 
No. 
Software 
Version Additional Details 
1 
PERL 
5.6

<!-- Page 41 -->

 
CTS Clearing House Interface – Specification 
 
 
41 
9.5 Very Large CHI (Between 250,000 and 400,000 items/day) 
9.5.1 Hardware 
 
The following provides the guidelines for the sizing of a CHI server that is expected to handle a volume of 
loading 400,000 items/day (160,000 items in a peak hour). 
 
Application Server  
 
Processor 
Dual Intel Xeon Processor E5-2643 (4C,10M Cache, 3.30 GHz, 8.00 GT/s Intel QPI) 
 
Memory 
32GB (DDR3, 1600MHz) 
 
Disk Drive Specification 
 
Disk 
RAID 
Drive 
Size 
(GB) 
Internal / External* 
Contents 
1 
RAID 1 
C 
80 
Internal Only 
OS 
D 
20 
Internal Only 
CHI Binaries 
2 
RAID 10 
J 
360 
Internal or External 
CH Data Files 
3 
RAID 10 
K 
360 
Internal or External 
CH Data Files 
4 
RAID 1 
E 
30 
Internal or External 
Temp Directory 
 
 
 
* Internal:  15K RPM, Internal Drive, RAID on separate disk spindles. 
External: 15K RPM, SAN Drive, RAID on separate disk spindles with RAID Enabled Backplane and          
external SAN Fibre Connect 
 
Security Module 
 
LUNA PCIe 7000 HSM from Safenet Inc. – 2 Cards 
 
Database Server  
 
Processor 
 
Dual Intel Xeon Processor E5-2643 (4C,10M Cache, 3.30 GHz, 8.00 GT/s Intel QPI) 
 
Memory 
 
32GB (DDR3, 1600MHz)

<!-- Page 42 -->

 
CTS Clearing House Interface – Specification 
 
 
42 
Disk Drive Specification 
 
Disk 
RAID 
Drive 
Size 
(GB) 
Internal / External* 
Contents 
1 
RAID 1 
C 
80 
Internal Only 
OS 
D 
26 
Internal Only 
Oracle Binaries 
2 
RAID 1 
E 
40 
Internal or External 
Oracle System Tables, Control Files 
F 
48 
Oracle Redo Log Archive 
3 
RAID 1 
G 
40 
Internal or External 
Oracle Redo Logs 1, Data, Control 
Files 
4 
RAID 1 
H 
40 
Internal or External 
Oracle Redo Logs 2, Index, Control 
Files 
5 
RAID 1 
I 
24 
Internal or External 
Undo Tablespace 
6 
RAID 1 
K 
250 
Internal or External 
Database Backup 
 
 
 
* Internal:  15K RPM, Internal Drive, RAID on separate disk spindles.  
External: 15K RPM, SAN Drive, RAID on separate disk spindles with RAID Enabled Backplane and 
external SAN Fibre Connect 
 
Please note that the daily database backup should be transferred from disk to tape or backup CHI. 
9.5.2 Software 
 
Application Server  
 
Operating System 
 
Microsoft Windows 2008 R2 (64 bit) Standard edition with appropriate CALs to handle the users within 
the Bank. 
 
Note: 1) W2008 R2 (64 bit) Enterprise edition is required if High Availability with Windows Active 
Passive Clustering needs to be configured. 
2) Install Windows Server 2008 R2 with Service Pack 1. 
 
Third-Party Software 
 
The CHI requires the following Third-Party software components for its operation. It is the responsibility of 
the commercial banks to procure licenses for these software components. Appropriate software Media 
and installation instructions will be provided by RBI/NPCI as part of the CTS project. 
 
No. 
Software 
Version Additional Details 
1 
IBM WebSphere Application Server - Standard Edition 
8.0 
560 PVUs 
2 
IPSwitch WSFTP Server5 
7.6 
  
3 
Netal SL4NT Logger 
3.2 
  
4 
CD Creator Software 
 
Roxio or similar 
 
 
                                               
5 For SFTP File Transfer.It requires IPSwitch WSFTP Server with SSH version 7.6.3 and above.

<!-- Page 43 -->

 
CTS Clearing House Interface – Specification 
 
 
43 
Following Third-Party Software components are included with NCR CHI Software. Commecial Banks are 
NOT required to procure separate licenses for these components.  
 
No. 
Software 
Version Additional Details 
1 
IPSwitch WS FTP Professional 
2006 
 
2 
Crystal Reports 
11.0 
 
3 
Java Runtime Environment (JRE) 
1.5 
 
4 
MSXML 
4.0 
  
5 
PERL 
5.6 
 
6 
MDAC 
2.8 
 
7 
Adobe Reader 
10.0 
 
8 
Oracle Client - 32 bit 
11.2 
 
 
 
Database Server  
 
Operating System 
 
Microsoft Windows 2008 R2 (64 bit) Standard edition with appropriate CALs to handle the users within 
the Bank. 
 
Note: 1) W2008 R2 (64 bit) Enterprise edition is required if High Availability with Windows Active 
Passive Clustering needs to be configured. 
2) Install Windows Server 2008 R2 with Service Pack 1. 
 
Third-Party Software 
 
The CHI requires the following Third-Party Software for its operation. It is the responsibility of the 
commercial banks to procure licences for these components. Appropriate software media and installation 
instructions will be provided by RBI/NPCI as part of the CTS project. 
 
No. 
Software 
Version Additional Details 
1 
Oracle Standard Edition - 64bit 
11.2 
5 Named User Licenses 
2 
Netal SL4NT Logger 
3.2 
  
 
Note: Oracle 11.2 Enterprise Edition - 64bit is required if Alternate CHI with Oracle Data Guard needs to 
be configured. 
 
The following Third-Party Software components are included with NCR CHI Software. Commecial Banks 
are NOT required to procure separate licenses for these components.  
 
No. 
Software 
Version Additional Details 
1 
PERL 
5.6 
 
 
9.6 Extra Large CHI (Between 400,000 and 550,000 items/day Inward + Outward) 
9.6.1 Hardware 
 
The following provides the guidelines for the sizing of a CHI server that is expected to handle a volume 
of loading 550,000 items/day (Inward+Outward) with 30% of total daily volume in peak hour. 
 
Application Server

<!-- Page 44 -->

 
CTS Clearing House Interface – Specification 
 
 
44 
 
One Application Server is required for handling load of Extra Large CHI. Following is the required 
hardware configuration for the Application Server.  
 
Processor 
 
Dual Intel Xeon Processor E5-2690 (8C, 20M Cache, 2.90 GHz, 8.00 GT/s Intel QPI) 
 
Memory 
 
32GB (DDR3, 1600MHz) 
 
Disk Drive Specification 
 
Disk 
RAID 
Drive 
Size 
(GB) 
Internal / External* 
Contents 
1 
RAID 1 
C 
80 
Internal Only 
OS 
D 
180 
Internal Only 
CHI Binaries 
2 
RAID 10 
J 
     900 
External 
CH Data Files 
3 
RAID 10 
K 
900 
External 
CH Data Files 
4 
RAID 1 
E 
50 
Internal Only 
Temp Directory 
 
 
* Internal:  15K RPM, Internal Drive, RAID on separate disk spindles. 
External Shared: Shared storage array 15K RPM, SAN Drive, RAID on separate disk spindles with RAID Enabled 
Backplane and external SAN Fibre Connect 
 
Security Module 
 
LUNA PCIe 7000 HSM from Safenet Inc. – 2 Cards  
 
Database Server  
 
One Database Servers are required to handle load of Extra Large CHI. Following is the required hardware 
configuration for the database server.  
 
Processor 
 
Dual Intel Xeon Processor E5-2690 (8C, 20M Cache, 2.90 GHz, 8.00 GT/s Intel QPI) 
 
Memory 
 
32GB (DDR3, 1600MHz) 
 
Disk Drive Specification 
 
Disk 
RAID 
Drive 
Size 
(GB) 
Internal / External* 
Contents 
1 
RAID 1 
C 
80 
Internal Only 
OS 
D 
60 
Internal Only 
Oracle Binaries 
2 
RAID 1 
E 
100 
Internal or External 
Oracle System Tables, Control 
Files 
F 
300 
Oracle Redo Log Archive 
3 
RAID 1 
G 
100 
Internal or External 
Oracle Redo Logs 1, Data, 
Control Files

<!-- Page 45 -->

 
CTS Clearing House Interface – Specification 
 
 
45 
4 
RAID 1 
H 
100 
Internal or External 
Oracle Redo Logs 2, Index, 
Control Files 
5 
RAID 1 
I 
60 
Internal or External 
Undo Tablespace 
6 
RAID 10 
K 
1200 
Internal or External 
Database Backup 
 
* Internal:  15K RPM, Internal Drive, RAID on separate disk spindles. 
External Shared: Shared storage array 15K RPM, SAN Drive, RAID on separate disk spindles with RAID Enabled Backplane 
and external SAN Fibre Connect 
 
9.6.2 Software 
 
Application Server  
 
Operating System 
 
Microsoft Windows 2008 R2 (64 bit) Standard edition with appropriate CALs to handle the users within 
the Bank. 
 
Note : Install Windows Server 2008 R2 with Service Pack 1. 
 
Third-Party Software 
 
The CHI requires the following Third-Party software components for its operation. It is the responsibility 
of the commercial banks to procure licenses for these software components. Appropriate installation 
instructions will be provided by NPCI as part of the CTS project. 
 
 
 
No. 
Software 
Version 
Additional Details 
1 
IBM WebSphere Application Server - Standard 
Edition 
8.0 
1120 PVUs 
2 
IPSwitch WSFTP Server6 
7.6 
  
3 
Netal SL4NT Logger 
3.2 
  
4 
CD Creator Software 
 
Roxio or similar 
 
Following Third-Party Software components are included with NCR CHI Software. Commercial Banks 
are NOT required to procure separate licenses for these components.  
 
No. Software 
Version 
Additional Details 
1 
IPSwitch WS FTP Professional 
2006 
 
2 
Crystal Reports 
11.0 
 
3 
Java Runtime Environment (JRE) 
1.5 
 
4 
MSXML 
4.0 
  
5 
PERL 
5.6 
 
6 
MDAC 
2.8 
 
7 
Adobe Reader 
10.0 
 
8 
Oracle Client - 32 bit 
11.2 
 
 
 
Database Server  
 
Operating System 
                                               
6 For SFTP File Transfer.It requires IPSwitch WSFTP Server with SSH version 7.6.3 and above.

<!-- Page 46 -->

 
CTS Clearing House Interface – Specification 
 
 
46 
 
Microsoft Windows 2008 R2 (64 bit) Standard edition with appropriate CALs to handle the users within 
the Bank. 
 
Note : Install Windows Server 2008 R2 with Service Pack 1. 
 
Third-Party Software 
The CHI requires the following Third-Party Software for its operation. It is the responsibility of the 
commercial banks to procure licenses for these components. Appropriate installation instructions will be 
provided by NPCI as part of the CTS project. 
 
 
No. Software 
Version Additional Details 
1 
Oracle Standard Edition - 64bit 
11.2 
5 Named User Licenses  
2 
Netal SL4NT Logger 
3.2 
  
Note: Oracle 11.2 Enterprise Edition - 64bit is required if Alternate CHI with Oracle Data Guard needs to 
be configured. 
The following Third-Party Software components are included with NCR CHI Software. Commercial Banks 
are NOT required to procure separate licenses for these components.  
 
No. Software 
Version Additional Details 
1 
PERL 
5.6 
 
 
9.7  Extra-Extra Large CHI (XXL CHI) (Between 550,000 and 800,000 items/day) 
9.7.1 Hardware 
 
The following provides the guidelines for the sizing of a CHI server that is expected to handle a volume 
of loading 800,000 items/day (Inward+Outward) with 30% of total daily volume in peak hour. 
 
Application Server  
 
One Application Server is required for handling load of Extra-Extra Large CHI. Following is the required 
hardware configuration for the Application Server.  
 
Processor 
 
Dual Intel Xeon Processor E5-2690 (8C, 20M Cache, 2.90 GHz, 8.00 GT/s Intel QPI) 
 
Memory 
 
64GB (DDR3, 1600MHz) 
 
Disk Drive Specification 
 
Disk 
RAID 
Drive 
Size 
(GB) 
Internal / External* 
Contents 
1 
RAID 1 
C 
80 
Internal Only 
OS 
D 
180 
Internal Only 
CHI Binaries 
2 
RAID 1 
E 
50 
Internal Only 
Temp Directory 
3 
RAID 10 
J 
450 
External Shared 
CHI Data Files

<!-- Page 47 -->

 
CTS Clearing House Interface – Specification 
 
 
47 
Disk 
RAID 
Drive 
Size 
(GB) 
Internal / External* 
Contents 
4 
RAID 10 
K 
450 
External Shared 
CHI Data Files 
5 
RAID 10 
L 
450 
External Shared 
CHI Data Files 
6 
RAID 10 
M 
450 
External Shared 
CHI Data Files 
 
 
* Internal:  15K RPM, Internal Drive, RAID on separate disk spindles. 
External Shared: Shared storage array 15K RPM, SAN Drive, RAID on separate disk spindles with RAID Enabled 
Backplane and external SAN Fibre Connect 
 
 
Security Module 
 
LUNA PCIe 7000 HSM from Safenet Inc. – 3 Cards  
 
Database Server  
 
One Database Servers are required to handle load of Extra-Extra Large CHI. Following is the required 
hardware configuration for the database server.  
 
Processor 
 
Dual Intel Xeon Processor E5-2690 (8C, 20M Cache, 2.90 GHz, 8.00 GT/s Intel QPI) 
 
Memory 
 
64GB (DDR3, 1600MHz) 
 
Disk Drive Specification 
 
Disk 
RAID 
Drive 
Size  
(GB) 
Internal / External* 
Contents 
1 
RAID1 
C 
80 
Internal Only 
OS 
2 
RAID1 
D 
120 
Internal Only 
Oracle Binary and Diag 
3 
RAID1 
M 
32 
External Shared 
Data , Control Files 
4 
RAID1 
N 
32 
External Shared 
Data 
5 
RAID1 
O 
25 
 External Shared 
Undo Tablespace 
6 
RAID1 
P 
64 
External Shared 
Data 
7 
RAID1 
Q 
24 
External Shared  
Index Data 
8 
RAID1 
R 
16 
External Shared  
Control Files, Oracle Redo 
Logs, Oracle System Tables 
9 
RAID1 
S 
6 
External Shared  
Control Files, Oracle Redo 
Logs 
10 
RAID5 
U 
357 
External Shared  
Oracle Redo Log Archive 
11 
RAID1 
W 
27 
External Shared  
Temp Data  
12 
RAID5 
Y 
1600 
External Shared  
Backup files 
 
* Internal:  15K RPM, Internal Drive, RAID on separate disk spindles. 
External Shared: Shared storage array 15K RPM, SAN Drive, RAID on separate disk spindles with RAID Enabled Backplane 
and external SAN Fibre Connect

<!-- Page 48 -->

 
CTS Clearing House Interface – Specification 
 
 
48 
 
9.7.2 Software 
 
Application Server  
 
Operating System 
 
Microsoft Windows 2008 R2 (64 bit) Enterprise edition with appropriate CALs to handle the users within 
the Bank. 
 
Note : Install Windows Server 2008 R2 with Service Pack 1. 
 
Third-Party Software 
 
The CHI requires the following Third-Party software components for its operation. It is the responsibility 
of the commercial banks to procure licenses for these software components. Appropriate installation 
instructions will be provided by NPCI as part of the CTS project. 
 
 
 
N
o. 
Software 
Version 
Additional Details 
1 
IBM WebSphere Application Server - Standard Edition 
8.0 
1120 PVUs 
2 
IPSwitch WSFTP Server7 
7.6 
  
3 
Netal SL4NT Logger 
3.2 
  
4 
CD Creator Software 
 
Roxio or similar 
 
Following Third-Party Software components are included with NCR CHI Software. Commercial Banks 
are NOT required to procure separate licenses for these components.  
 
No. Software 
Version 
Additional Details 
1 
IPSwitch WS FTP Professional 
2006 
 
2 
Crystal Reports 
11.0 
 
3 
Java Runtime Environment (JRE) 
1.5 
 
4 
MSXML 
4.0 
  
5 
PERL 
5.6 
 
6 
MDAC 
2.8 
 
7 
Adobe Reader 
10.0 
 
8 
Oracle Client - 32 bit 
11.2 
 
 
 
 
Database Server  
 
Operating System 
 
Microsoft Windows 2008 R2 (64 bit) Enterprise edition with appropriate CALs to handle the users within 
the Bank. 
 
Note : Install Windows Server 2008 R2 with Service Pack 1. 
 
Third-Party Software 
 
                                               
7 For SFTP File Transfer.It requires IPSwitch WSFTP Server with SSH version 7.6.3 and above.

<!-- Page 49 -->

 
CTS Clearing House Interface – Specification 
 
 
49 
The CHI requires the following Third-Party Software for its operation. It is the responsibility of the 
commercial banks to procure licenses for these components. Appropriate installation instructions will be 
provided by NPCI as part of the CTS project. 
 
 
No. Software 
Version 
Additional Details 
1 
Oracle Enterprise Edition - 64bit 
11.2 
5 Named User Licenses  
2 
Netal SL4NT Logger 
3.2 
  
The following Third-Party Software components are included with NCR CHI Software. Commercial Banks 
are NOT required to procure separate licenses for these components.  
 
No. Software 
Version 
Additional Details 
1 
PERL 
5.6

<!-- Page 50 -->

 
CTS Clearing House Interface – Specification 
 
 
50 
10 Network Capacity Planning 
 
The networking capacity required at the CHI to communicate to the CH has been approximated as per the 
formula below. The banks are requested to choose a suitable router and communication equipment to 
handle the workload as computed below. 
 
The highlevel steps in computing your network capacity are: 
a) determine your peak day item volume by summing: 
i. outward volume for the biggest peak day 
ii. inward volume for the biggest peak day 
b) multiply by 0.0001537 
 
Example:  outward volume on biggest peak day is 13,500 items, inward volume on biggest peak day is 
11,800 ; sum is 25,300 items.  Now multiply by 0.0001537 results in 3.888 Mbps of required network 
capacity (minimum). 
 
The assumptions in place for the network capacity are: 
 
that the maximum image size is being transferred – namely 85KB 
 
that the busiest hour of the day moved 40% of the total item volume 
 
that a network can only be used up to 60% of it’s theoretical maximum 
 
that 10-bits represents the data plus network overhead 
 
there are 1024 KB in a MB and 3600 seconds per hour 
 
The actual formula is: 
 
Network capacity (Mbps) = 
)
6.0
*
3600
*
1024
(
)
10
*
40
.0
*
85
*
(
bits
KB
itemvolume
 
 
 
11 High Availability and Disaster Recovery 
 
11.1 High Availability – Active-Passive Cluster  
The HA Capability for the CHI can be implemented using Microsoft Windows 2008 Failover Cluster.  
In Microsoft Windows 2008 Failover cluster, the first installed server acts as a primary server. If the 
primary server fails, switch over to passive server will happen automatically. 
 
Notes: 
i. 
Hardware configuration for each server is as detailed in section 9 for the corresponding CHI 
variant 
ii. All application drives should be on external shared storage. 
iii. Microsoft Windows 2008 R2 64 bit Enterprise Edition is required on all servers. 
iv. All servers should be on the same CHI software version. 
v. Third-Party Software license requirements are applicable for each server as detailed in 
section 9 for the corresponding CHI variant.

<!-- Page 51 -->

 
CTS Clearing House Interface – Specification 
 
 
51 
11.2 Disaster Recovery – Alternate CHI  
 
The Alternate CHI can be setup as an independent replica of the primary CHI. Database replication 
between primary CHI and alternate CHI can be achived by following ways. 
 
1. Using Oracle Data Guard solution 
For operational readiness, the bank’s CHI Administrator must ensure that the primary CHI’s 
end-of-day database archive log is applied at the Alternate CHI on a daily basis.   
 
2. Using Oracle RMAN Backup recovery solution 
For operational readiness, the bank’s CHI Administrator must restore the primary CHI’s end-of-
day database backup at the Alternate CHI on a daily basis.   
 
In case of a disaster at the primary CHI, operations can start at the Alternate CHI from StartOfDay. 
 
Notes:  
i. 
Hardware configuration for the Alternate CHI is the same as the primary CHI as detailed in 
section 9 for the corresponding CHI variant. 
ii. Primary and Alternate CHIs must be on the same CHI software version. 
iii. Oracle 11.2 Enterprise Edition - 64bit is required for both primary and alternate CHI's 
database if Oracle Data Guard feature is used as a database replication solution for 
Alternate CHI processing. Appropriate Oracle license need to be procured as per the CHI 
flavor. 
iv. Third-Party Software license requirements are applicable for each server as detailed in 
section 9 for the corresponding CHI variant. 
 
11.3 Alternate during Network Failure 
See section 3.11. 
 
12 Clearing House Tables available for capture system 
 
The following Clearing House Master data shall be available for use by the capture systems.   
 
 
 
Clearing House and Clearing Center, including Bank/Branch and blockages 
 
Item Return Reason 
 
Calendar 
 
Bundle Collection 
 
Session Definition and Collection Type 
 
Clearing Type and DocType definitions 
 
Item Extension Reason 
 
Translation Rules 
 
Transaction Code 
 
City Master 
 
AtParBankMaster 
 
 
The Clearing House Table data will be contained in a single XML file, available in a file folder on the CHI 
server as described in section Appendix 3.4.  Capture and Drawee modules will have to detect that a new 
Clearing House Table Data file exists, and then undertake to get the file and use it for their purposes. 
 
The details of the CH Master XML file can be found in the Interface Specification in Appendix A.

<!-- Page 52 -->

 
CTS Clearing House Interface – Specification 
 
 
52

<!-- Page 53 -->

 
CTS Clearing House Interface – Specification 
 
 
53 
13 Appendix A – CHI Interface Specification 
APPENDIX CHANGE SHEET 
 
Rev 
Date 
Section 
Description of Change 
By 
A 
Apr 12, 
2006 
 
Rev A Initial, Available for RBI/NPCI and banks 
G. Franklin 
B1 
18 Apr 
2006 
many 
NCR & RBI/NPCI internal review and changes 
G.Franklin 
B2 
25 Apr 
2006 
many 
NCR & RBI/NPCI internal review and changes 
G.Franklin 
B3 
27 – 29 
June200
6 
many 
NCR & RBI/NPCI internal review and changes 
G.Franklin 
For 
CHI 
V1.7 
20 July  - 
01 Aug 
2006 
many 
NCR & RBI/NPCI internal review and changes 
G.Franklin 
For 
CHI 
V1.8 
17 Aug – 
28 Aug 
2006 
many 
NCR & RBI/NPCI internal review and changes 
Sunil Babu 
For 
CHI 
V1.9 
Thru Sep 
19 2006 
Many 
Very many changes in almost all sections due to 
RBI/NPCI Feedback on DRS. 
GF 
V1 
.10 
22 sep 
2006 
Many 
 
Appx 4.1.2 re-order ImageDS 
 
Appx 4.1.3.3 TruncatingRTNo 
 
Appx 4.3.1 typo/grammer 
 
Appx 4.3.2 re-order ImageDS 
 
Appx 4.3.3 re-order ImageDS 
 
Appx 4.3.4.1 added SettlementDate 
and SettlementTime to FileHeader 
 
Appx 4.8.1 filename typo 
 
Appx 4.10.3.1 added SettlementDate 
and SettlementTime to FileHeader 
 
Appx 4.11.x CHMaster Table cleanup 
 
Appx of sample files – corrected to 
agree 
 
Appx 9.2 is for information only

<!-- Page 54 -->

 
CTS Clearing House Interface – Specification 
 
 
54 
V1 
.11 
17 Nov 
2006 
 
 
Appx 1 deleted reference to host 
(recon) file 
 
Appx 2.1 clarify Extension File (EF) as 
well as DREF 
 
Appx 2.4, Appx 2.5, Appx 3.4.1, Appx 
4.8, Appx 4.8.1 describe DREF 
 
Appx 2.5, Appx 4.11.2, Appx 4.11.3.3, 
Appx 6 add necessary detail for 
AtParBankMaster element 
 
Appx 2.5, Appx 4.12, Appx 5.9 add 
detail and example for Unwound Item 
File 
 
Appx 4.11.2 redraw picture, A1 adjust 
indent of “Branch” 
 
Appx 4.11.3.7 completed description of 
DesignatedBranchForTransCode 
 
Appx 4.12 added section for Unwound 
Item File

<!-- Page 55 -->

 
CTS Clearing House Interface – Specification 
 
 
55 
V1 
.12 
15 Feb 
2007 
 
 
Appx 1.2 C4 -- clarify Mandatory/Optional as 
applies to elements and attributes. Note that 
Fields having NULL or no default value are to 
be omitted from input files.  Default/pre-defined 
values for attributes are case-sensitive 
              C8 -- clarify element tags and attribute 
names are case-sensitive. 
 
Appx 2.1 -- diagram add DREF file 
 
Appx 2.5 -- specifically list DREF Drawee 
Extension File (it was already given in the 
description) 
 
Appx 3.3 -- add suggestion for better exception 
processing by inclearing system, clarify 
purging. 
 
Appx 4.1.2 -- diagram to swap ImageDS with 
ImageViewData to agree with order in A1; 
corrected legend. 
 
Appx 4.1.3.1 -- xmlns is lower case, 
VersionNumber xxyyyy is lower case, added 
DREF file 
 
Appx 4.1.3.3 -- IQAIgnoreInd is optional, 
default value is 0 
 
Appx 4.1.3.4 – MICRFingerPrint NOTE 
clarified, added “Drawee” as a possible value. 
 
Appx 4.1.3.6 -- provided attribute descriptions, 
removed ViewSideIndicator values that are not 
supported. 
 
Appx 4.1.3.7 -- clarified Filename, and digital 
signature attributes, StartOfProtectedData and 
ProtectedDataLength are Mandatory,  lengths 
must be greater than 0 
 
Appx 4.1.3.8 -- clarified 
ImageReferenceKeyLength, lengths must be 
greater than 0 
 
Appx 4.1.3.9 -- described ImageViewAnalysis 
and IQA interpretations. 
 
Appx 4.3.2 -- diagram to swap ImageDS with 
ImageViewData to agree with order in C1; 
corrected legend. 
 
C1 list multiple MICRDS and ImageDS, 
ImageViewAnalysis elements 
 
Appx 4.3.3 -- diagram to swap ImageDS with 
ImageViewData to agree with order in B1; 
corrected legend. 
 
C1 list multiple MICRDS and ImageDS, 
ImageViewAnalysis elements 
 
C2 -- added Mandatory elements 
 
Appx 4.3.4.1 -- xmlns is lower case, 
VersionNumber xxyyyy is lower case 
 
Appx 4.4.2 – corrected diagram 
 
Appx 4.5.3.4 – MICRDS for RRF sets source = 
“Drawee” 
 
Appx 4.5.2 -- diagram - corrected legend. 
 
C1,C2 -- added structure and Mandatory 
elements 
 
Appx 4.6.2 -- diagram - corrected legend. 
 
Appx 4.6.3 -- diagram - corrected legend. 
 
C2 -- added Mandatory elements 

Appx 4 7 2
diagram added
GF

<!-- Page 56 -->

 
CTS Clearing House Interface – Specification 
 
 
56 
V1 
.12 
15 Feb 
2007 
-contd 
 
 
Appx 4.8.1 C1, C3 -- list EF and DREF files 
 
Appx 4.8.2 -- diagram - corrected legend. 
 
Appx 4.9.1 C1 -- clarify File ID is unique 
 
Appx 4.9.2 -- diagram to agree with C2; 
corrected legend. 
 
C2 -- update diagram and clarify 
Mandatory elements 
 
Appx 4.9.3.1 -- xmlns is lower case, 
VersionNumber xxyyyy is lower case, 
 
Appx 4.9.3.1 -- clarify CreationDate and 
CreationTime,  
 
Appx 4.9.3.2 -- update that 2 attributes are 
Mandatory 
 
Appx 4.3.10.3.3.1– augment Error Resolution 
for FileStatusCode 2 
 
Appx 4.10.2 -- diagram - corrected legend. 
 
C2 added Mandatory elements 
 
 
Appx 4.10.3.1 -- xmlns is lower case 
 
 
Appx 4.11.3.1 -- xmlns is lower case 
 
 
Appx 4.11.3.7 -- TRANSCODE size is 3 
 
Appx 4.11.3.18 -- CODE size is 3 
 
 
Appx 5.1 -- corrected errors in CXF example 
 
Appx 5.2 -- corrected errors in PXF example 
 
Appx 5.3 -- corrected errors in RRF example, 
MICRDS for RRF sets source = “Drawee” 
 
Appx 5.4 – corrected errors in RF example, 
MICRDS for RF sets source = “Drawee” 
 
Appx 5.5 -- corrected errors in ERF example 
 
Appx 5.6 -- corrected errors in EF example 
 
Appx 5.7 -- corrected errors in RES example 
 
Appx 9.1 -- C11, C22 removed extraneous 
NCR transport specifics 
 
Appx 9.2 -- table deleted as RBI/NPCI does 
not support JPEG images in TIFF files. 
 
Appx 9.3 -- C2 removed extraneous NCR 
transport specifics 
 
Appx 9.4 -- C2 deleted 
 
Appx 9.5 -- C1 deleted 
 
Appx 9.6 new to define Required JFIF markers 
and tags for grayscale JFIF images

<!-- Page 57 -->

 
CTS Clearing House Interface – Specification 
 
 
57 
V1 
.12 
14 March 
2007 
 
 
Appx 2.5 PXF – added that number of items is 
a configurable parameter 
 
Appx 4.1.3.9 – corrected attribute spelling 
LegalAmountUsability 
 
Appx 4.5.3.3.1 – corrected to agree with 
RBI/NPCI Procedural Guidelines; 39 clarified; 
40 added, 82,83,84 deleted. 
 
Appx 4.7 – corrected working in introduction 
paragraph 
 
Appx 4.7.3.3.1 – changed descriptions 
01,02,03 
 
Corrected sample files to reflect India values – 
Appxs: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.8

<!-- Page 58 -->

 
CTS Clearing House Interface – Specification 
 
 
58 
V1.1
3 
4 July 
2007 
 
 
Appx 4.3.10.3.3.1Reject Reason – Modified 
Existing Reject Reason Code “11” and Added 
2 New Reject Reason Code – “24 and 25”. 
 
Appx 4.1.3.3 and Appx 4.3.4.7 In Attributes of 
Item – “MICRRepairFlags” which was N is now 
NS 
 
In Appx 4.10.3.2 OACK FileSummary. 
TotalItemAmount attribute is removed as Item 
Tag does not not have amount attribute  
 
Account No (Drawee Account Number) is 
Optional. This correction is made in following 
sections – Appx 4.5.3.3, Appx 4.7.3.3, Appx 
4.8.3.3, Appx 4.9.3.3, Appx 4.12.3.2 
 
“DepositorAcct” is made Optional in Section – 
Appx 4.1.3.5,  
 
In Appx 4.3.10.3.3.1Reject Reason Section, 
added a new Reject Code - 26 for AT PAR 
Validation 
 
In Appx 4.7.3.3.1 Extension Reason Section - 
Added Extension Reason Code 07 for 
Blockage. 
 
Appx 4.3.4.7 Item Section – “ItemStatus” 
Attribute is now made Mandatory and Default 
is changed from “00” to “0” 
 
Appx 4.3.4.7.1 ItemStatus Section the 
ItemStatus Code which earlier was – “00”, “08”, 
“09” is now changed to “0”, “8”, “9” 
 
Appx 4.3.4.7.1 ItemStatus Section - 
Description of ItemsStatus Code after change 
9 (prior to change was 09) for Duplicate MICR 
Fields Check has been updated. 
 
Appx 4.10.3.3 Item now has ItemStatus 
Attribute to pass the Duplicate MICR Fields 
Detect Flag to Presenting Bank via OACK File 
 
Added Appx 4.10.3.3.1 Item Staus table for 
OACK File 
 
Changed the description of EOS in Appx 2.5. 
“These are 0KB files created to signal the bank 
modules that all the PXF and PIBF Files have 
been created for a session”. 
 
Update Appx 5.3 Return Request File 
Example, Update Appx 5.4 Return File 
Example with IFSC Code as 11 digits. 
 
"SettlementTime" attribute deleted from Appx 
4.3.4.1 Section, Appx 4.10.3.1, Appx 5.2 
Posting Exchange File Example, Appx 5.8 
Outward Acknowledgement File Example. 
 
Updated “SettlementDate” Description - "Value 
Date – Date on which the Items shall be 
posted in books of account for release of 
funds"  in Appx 4.3.4.1 Section, Appx 4.10.3.1 
Section. 
 
Updated Note below Appx 4.3.4.1 - "Drawee 
Module shall use SessionDate  and 
CLOSE_RECEIVING_TIME of the Session, to 
determine extension and return lengths for 
items in the session" 
RP

<!-- Page 59 -->

 
CTS Clearing House Interface – Specification 
 
 
59 
V1.1
3 
4 July 
2007 
 
 
Added "SessionExtensionHrs" attribute in Appx 
4.3.4.1 and Appx 4.10.3.1. 
 
Added following statement in Appx 4.10 – 
“Capture shall use SessionDate  and 
CLOSE_RECEIVING_TIME of the Session to 
calculate the maximum return period.” 
 
Corrected Sample CHM in Appx 6 – Appendix 
BB – “Blockage FROM_DATE="09072006" 
TO_DATE="10072006". 
 
Corrected Sample CHM in Appx 6 – Appendix 
BB – “CALENDAR_ID="23062006"”. 
 
Corrected Sample CHM in Appx 6 – Appendix 
BB – In TranslationRule – 
“FROM_DATE="20062006" 
TO_DATE="20082006"” 
RP

<!-- Page 60 -->

 
CTS Clearing House Interface – Specification 
 
 
60 
V1.1
3 
19 July 
2007 
 
 
Updated Government Cheque footnote in Appx 
4.1.3.3. Account Number shall no longer have 
AccountNumber + Transaction Code. 
 
In Appx 5.8, Updated complete Outward 
Acknowledgement File Example 
 
Appx 3.4.1 Participating Bank and Remote 
Branch Folders. Remote Branch Folders shall 
be under respective Bank Folders. 
 
Appx 4.3.10.3.3.1Reject Reason – Added a 
new Reject Reason Code for Government 
Cheque Validation 
 
Appx 2.5, 3.3 and 3.4.1 EOP File reference 
has been removed as it is no longer required in 
the system. 
 
Appx 4.8.1 Extension File (EF) Naming 
Convetion added AO File Option. 
 
Appx 4.11.3.13 – Session Definition Table, 
deleted field 
“CLOSE_RECEIVING_RETURNS_TIME”, 
Altered Description for field 
“CLOSE_RECEIVING_TIME” 
 
Appx 4.11.3.16 TranslationRule Element – 
FROM_DATE and TO_DATE date format 
deleted and size changed to 8 
 
Appx 4.11.3.17 Blockage Element – 
FROM_DATE and TO_DATE date format 
deleted and size changed to 8 
 
In Appx 4.12.1, Session No & Session Date 
added in UIF file name.  
 
In Appx 4.12.3.1, Session No & Session Date 
added in File Summary Record. 
 
In Appx 4.12.3.2, current default values 
replaced with 2 default values for "Record 
type" field. "PI" => to Indicate Presentment 
Item."RI" => to Indicate Return Item 
 
Updated Appx 5.9 Unwound Item File Example 
to reflect Session No, Session Date, Record 
Type changes. 
 
Appx 4.10.3.3, Update the Value (Default) 
Coloumn description for ItemStatus Field. 
 
Appx 4.11.3.13- removed 
"CLOSE_RECEIVING_RETURNS_OFFSET_
DAYS" & "DO_SAME_SESSION_RETURNS". 
 
Appx 4.11.3.17 Blockage Element – TO_DATE 
Usage is now set as NOT NULL. 
 
 
RP

<!-- Page 61 -->

 
CTS Clearing House Interface – Specification 
 
 
61 
 
 
 
 
Appx 4.11.3.6 Bank Element – Description for 
CLEARING_STATUS_CODE updated with 
SUSPENDED possible value used during Un-
Winding. 
 
Updated Process Flow diagram in Appx 2.1 
 
Added Appx 9.7 Note – Calculation of 
Extensions and Returns 
 
Added Note in Appx 4.11.3.20 
AtParBankMaster Element. 
 
Added Return Reason Code for Blockage in 
Appx 4.5.3.3.1 
 
V1.1
4 
26th Feb 
2008 
 
 
Implementation of CRF for MICR Repair Flag. 
Update sections; 4.1.3.3, 4.3.4.7 
 
Change impacting the resolution of GEMS ID 
33625678. Change the description of reject 
reason code 18 in Appx 4.3.10.3.3.1 
 
V1.1
5 
14th July 
2010 
 
 
Modified folder structure in Appx 3.4.1 
 
Modified Appx 4.3  to mention location of 
branch folder in city folder 
 
Added new SPEED_CLEARING attribute in 
Appx 4.11.3.6 
 
Added new SPEED_CLEARING attribute in 
Appx 6 Appendix  BB – CH Master Data File 
Example 
 
Added a new section Appx 10 List of Paper to 
Follow (P2F) Items 
 
V1.1
6 
23rd 
August 
2010 
 
 
Modified appx 3.4.1 for adding the city folder in 
the table 
 
Modified appx 10 to add the ascending order 
for P2F file. 
 
Modified appx 4.11.3.6 to change the name of 
the new field to “CBS enabled” 
 
V1.1
7 
6th 
Septemb
er 2010 
 
 
Modified appx 4.11.3.6 to modify the comment 
column for the field “CBS enabled” 
 
Modified appx 4.5.3.3.1 to change the name of 
the return reason section for codes 70-79 
 
V2.0 
7th 
Decemb
er 2012 
 
 
Modified appx 4.1.3.1, 4.1.3.4, 4.1.3.7 section 
to remove the support for SHA1 signature 
algorithm and 1024 security key length 
support. 
 
Modified appx 5.1, 5.2, 5.3 and 5.4 to update 
the file example for support for SHA256 
signature algorithm and 2048 security key 
length support.

<!-- Page 62 -->

 
CTS Clearing House Interface – Specification 
 
 
62 
V2.1 
5th 
October 
2013 
 
 
Addition of a new section for interface 
specification of FILE for CHI Branch interface 
module’s bulk search 
o Appx 4.4 FILE for CHI Branch interface 
module’s bulk search 
o Appx 4.4.1 File Name Convention 
o Appx 4.4.2 Elements 
o Appx 5.10 Example of FILE for CHI Branch 
interface module’s bulk search 
 
Updated some format changes in below 
section. 
o Appx 4.1.3 Elements and Attributes 
Added Min and Max size of attribute for following 
sesction  
o CXF 
 
Appx 4.1.3 Elements and Attributes 
 
Appx 4.1.3.2 FileSummary 
 
Appx 4.1.3.3 Item 
 
Appx 4.1.3.4 MICRDS 
 
Appx 4.1.3.5 AddendA 
 
Appx 4.1.3.7 ImageDS 
 
Appx 4.1.3.8 ImageViewData 
 
Appx 4.1.3.9 ImageViewAnalysis 
o PXF 
 
Appx 4.3.4.1 FileHeader 
 
Appx 4.3.4.1.1 FileSummary 
 
Appx 4.3.4.1.6 Item 
o RRF 
 
Appx 4.3.6.3.3 Item 
o ERF 
 
 
 
 
Appx 4.3.8.3.3 Item 
o EF 
 
 
 
 
Appx 4.3.9.3.3 Item 
o RES 
 
Appx 4.3.10.3.1 FileHeader 
 
Appx 4.3.10.3.2 FileSummary 
 
Appx 4.3.10.3.3 Item 
o OACK 
 
Appx 4.3.11.3.1 FileHeader 
 
Appx 4.3.11.3.2 FileSummary 
 
Appx 4.3.13.3.2 Item Record

<!-- Page 63 -->

 
CTS Clearing House Interface – Specification 
 
 
63 
V2.1 
9th 
Decemb
er 2013 
 
o UIF 
 
Appx 4.3.11.3.3 
Item Appx  
 
4.3.13.3.2 
Item Record 
Updated the Appx 4.1.3.9 ImageViewAnalysis 
section to add “-1” as a new flag for some of the 
IQA related test. 
 
 
V2.1 
9th 
Decemb
er 2013 
 
 
Addition of new Clering Type code for “LOCAL 
“ Clearing Type under section Appx 7 
Appendix CC – ClearingType 
 
V2.1 
26th 
January 
2014 
 
 
Added new Clearing Type “11” for NON CTS 
Cheqes under section “Appx 7 Appendix CC – 
ClearingType” and removed Clearing Type 12 
and 13 which are not being used in current 
scenario. 
 
V2.1 
28th 
January 
2014 
 
 
Modified the "Appx 4.1.3.3 Item" section to 
change the "UserField" attribute as mandatory 
field in "Item" element in CXF. This change 
was initiated as per NPCI's request.

<!-- Page 64 -->

 
CTS Clearing House Interface – Specification 
 
 
64 
V2.2 
18th 
Septemb
er 2014 
 
 
Modified Appendix 4.1.3.1 FileHeader.  
 
Changed VersionNumber attribute value from 
0003 to 0004.This change shall enable the 
system to validate the attribute level contraints. 
New CXF, RRF Schemas will be available in 
0004 Version.Version 0004 will cater to 
Interface specification changes from version 
2.0 to 2.2. 
 
Xmlns attribute value changed for CXF, RRF & 
ERF. 
For CXF & RRFupdated value from 
0003 to 0004. 
For ERF Updated value from 0001 to 
0002. 
 
Modified Appx 4.1.3.7 Image DS Section. 
 
Attribute SecurityKeySize & 
DigitalSignatureMethod value changed to 
v0004. 
 
Modified Appx 5.1, 5.3 & 5.5 ECPIX file 
examples section.  
 
Removed footnote from Appendix 4.1.3.3 
With reference to RBI Circular : “RBI/2014-15/237 
DGBA.GAD.No.H - 1204/42.01.035/2014 -15 : 
Dispensation of the requirement of forwarding of 
government cheques in physical form to 
Government “ deleted the footnote for capture 
treating 7 digit account as special case for 
government cheques 
 
 
Modified Appx 3.7.1 Presented Validations 
"With reference to RBI Circular : RBI/2014-15/237 
DGBA.GAD.No.H - 1204/42.01.035/2014 -15 : 
Dispensation of the requirement of forwarding of 
government cheques in physical form to 
Government “ 
Removed the “Government Cheque validation:”

<!-- Page 65 -->

 
CTS Clearing House Interface – Specification 
 
 
65 
V2.2 
10th 
February 
2015 
 
 
Modified Appx 4.1.3.3 Item Section. 
 
AccountNo attribute modified for 
Short Account Number Validation. 
 
Footnote added for AccountNo 
attribute. 
 
Comment added for userField 
Attribute. Userfiled string validation 
is as per RBI guidelines.  
 
Modified Appx 4.3.10.3.3.1 Reject Reason 
 
Reject Reason 7/15 is used for 
Short Account Number validation 
failure. 
 
V2.2 
16th 
March 
2015 
 
 
Modified Appx 4.3.10.3.3.1 Reject Reason 
 
Reject Reason 7/35 is used for 
reject reason comment validation 
 
Reject Reason 7/34 is used for 
validation of BOFD routing number 
for  P2F instrument 
 
V2.3 
20th 
Novemb
er 2015 
 
 
Modified Appx 4..1.3.1 and Appx 5.1 section  
 
Changed VersionNumber attribute value of 
CXF schema from 0004 to 0005. This 
change shall enable new validations on 
MICRRepairFlags attribute of item element. 
 
FootNote added for MICRRepaireFlags 
attributes validations. 
 
V2.3 
11th 
January 
2016 
 
 
Modified Appx 4.1.3.1 update validations for 
MICRRepairFlags attributes.  
 
Foot note is updated for MICRRepairFlags 
validations. 
 
V2.4 
10th 
February 
2016 
 
 
Modified Appx 4.1.3.1 updated validations for 
Government validations. Description for Reject 
reason 15 and 27 are updated 
 
V2.4 
03rd 
March 
2016 
 
 
Modified footnote in Appx 4.1.3.3, Added Foot 
note for Mandatory condition of AccountNo field 
 
V2.4 
09th 
March 
2016 
 
 
Modified Appx 4.1.3.3 Description changed for 
MICRRepairFlags - ‘xxxx5x’ to “if account is 
old.” 
 
 
 
Note: This document has the following change sheet section.  
 
Main Change Sheet 
This section tracks all the changes in the document excluding the changes in the Appendix 
section. 
 
Appendix Change Sheet. 
This section tracks all the changes in the Appendix section.

<!-- Page 66 -->

 
CTS Clearing House Interface – Specification 
 
 
66 
Appx 1 
Introduction 
This document describes the interface between the ECPIX’s Clearing House Interface (CHI) and the 
capture system. The capture system includes POD, Inclearings and Return-processing. The interface 
is based on the ANSI X9.37 DSTU 2003 definition but is not taken in its entirety and the format is 
changed from the record structure to XML. The images are provided in separate binary image files. 
The X9.37 DSTU 2003 should be used only as reference. This document will supersede X9.37 DSTU 
2003.   
This document describes the files used by depository (capture) institutions to send check data 
and images to the RBI/NPCI or when RBI/NPCI presents or returns check data and images to a 
depository institution. This document is updated from time to time and NCR and RBI/NPCI 
reserve the right to update or amend this document without prior notice. Updates to this 
document will be posted on the RBI/NPCI’s Web site. Every depository institution is required to 
work with this file structure and field definitions.   
CHI supports the receipt and the delivery of check data and images using this interface in the following 
ways: 
Items sent to CHI:   1. Forward Presentment of checks with data and images 
                                  2. Outward Returns with data only. 
                                  3. Extension Requests from the drawee bank with data only 
                                 
 
 
Items sent by CHI:  1. Inward Presentment of checks with data and images  
                                  2. Inward Returns with data only 
                                  3. Response file (ack/reject) for every incoming file from CHI  with data only 
                                  4. Extension file to depository bank with data only                                 
                                  5. Outward Acknowledgement file with data only 
 
 
 
 
Appx 1.1 
Nomenclature and Notes on Reading this Document 
A1 Within this interface specification, the following nomenclature shall be used: 
The word “shall” is used to indicate a binding function that must be performed by the system 
implementing the interface. The word “will” is used to describe additional details of the binding 
function. 
In the leftmost column of this document, each function has a unique identifier in the form: Rxx. The ‘R’ 
refers to the revision level of the document in which the function was first introduced or last changed. 
The ‘xx’ is a sequence number, starting at 1 within each section. As an example, the first function in 
each section of the document’s initial release will be “A1”, the second function will be “A2”, etc. 
When an existing function is changed between revisions, only the revision level changes; the 
sequence number remains the same. When a new function is added, it is assigned the new

<!-- Page 67 -->

 
CTS Clearing House Interface – Specification 
 
 
67 
revision level and the next new sequence number in the section. If a function is deleted within 
a section, its sequence number can no longer be used in that section. The change log will 
reflect all functions changed, added or deleted. 
 
A2 In this document term “ECPIX” refers to the CHI component of ECPIX. 
A3 In this document “capture file” will be used synonymous with “capture exchange file”. 
A4 In this document “posting file” will be used synonymous with “posting exchange file”. 
 
Appx 1.2  Conventions 
A1 
All XML elements in this document shall be documented in “BOLD and Italic”. This is for readability 
only and is not a restriction for implementation. 
 
A2 
All attribute values shall be in quotes ””.  
 
A3 
All XML element and their attributes are fixed and shall be used as defined in this document. All 
XML examples in this document are examples only and values are not real. The actual attribute 
values used in real applications will be different than values shown in the examples. The examples 
are given to help understand the concepts. 
 
C4 
The convention that shall be followed to describe the “Usage” column in all tables in this document 
is as follows:  
M – for Mandatory  
O -  for Optional  
N – Not applicable 
 
Mandatory Element means that the element is required.  If the element is missing, it will result in 
an error. 
Optional Element means that the element may or may not be present. 
 
Mandatory Attribute means that the attribute is required and its value should adhere to the data 
type and size specified.  If the attribute is missing, it will result in an error. 
Optional Attribute means that the attribute may or may not be present.  If present, its value 
should adhere to the data type and size specified. 
 
Fields having NULL or no default value should be omitted from input files. 
Default/pre-defined values for attributes are case-sensitive. 
 
A5 
The convention that shall be followed to describe the “Type” column in all tables in this document 
is as follows:  
N- Numeric. Shall be the numbers zero (0) through nine (9). No left padding with zeros required or 
supported. 
A- Alphabetic. The alphabetic characters shall consist of the upper case letters A through Z, the 
lower case letters a through z, and the blank (space) character. No distinction shall be made 
between the upper case and the lower case.  
AN – Alpha Numeric. An alphanumeric character shall be any of the alphabetic or numeric 
characters. 
ANS – String or Variable Characters 
NS – Numeric string. Will maintain the leading zeros. 
DATE – Numeric field in a localized format – RBI/NPCI requires “DDMMYYYY” 
TIME – Numeric field in the format “HHMMSS”. HH is hours in range 0-23. 
 
A6 
XML documents used in this interface shall conform to well formed XML in compliance with the 
W3C specification.

<!-- Page 68 -->

 
CTS Clearing House Interface – Specification 
 
 
68 
 
B7 
Every XML document used in this interface shall begin with an XML prolog: 
 <?xml version=”1.0” encoding=”UTF-8”?> 
 
C8 
All element tags and attribute names are case-sensitive. 
 
Appx 1.3 References 
1 
XML 1.0 (Third Edition) – World Wide Web Consortium.  Extensible Markup Language (XML) 1.0, 
Third Edition.  
Available at: http://www.w3.org/TR/2004/REC-xml-20040204/ 
Abstract: The Extensible Markup Language (XML) is a subset of SGML that is completely described in this 
document. Its goal is to enable generic SGML to be served, received, and processed on the Web in the way 
that is now possible with HTML. XML has been designed for ease of implementation and for interoperability 
with both SGML and HTML. 
2 
DSTU X9.37-2003 http://webstore.ansi.org/ansidocstore/dept.asp?dept_id=80 
 
3 
ISO 4217 Codes for the Representation of Currency and Funds 
Available at: http://www.iso.org/iso/en/prods-services/popstds/currencycodes.html 
 
4 
 Namespaces in XML 1.0 – World Wide Web Consortium. 
Available at: http://www.w3.org/TR/REC-xml-names/ 
Abstract: XML namespaces provide a simple method for qualifying element and attribute names used in 
Extensible Markup Language documents by associating them with namespaces identified by URI references.

<!-- Page 69 -->

 
CTS Clearing House Interface – Specification 
 
 
69 
Appx 2 
 Process flow in the Check Truncation System (CTS) using 
ECPIX  
Appx 2.1 Process Flow Diagram 
Capture
Exception
(Return )
Processing
Inclearing
CHI
CH
CHI
Return
Processing
Database
Bank 1
Bank 2
Clearing House
CXF
CIBF
CXF.f.RES
wPXF
PIBF
ECPIX
wRF
ERF
RRF
Outward Presentment
Outward Returns
Inward Presentment
Inward Returns
                                      Extension/paper Requests
                  Response Files
RRF.f.RES
ERF.f.RES
wEF
Host
wDREF
 
 
Files sent to CHI:    1. CXF*.XML and CIBF*.IMG – Outward Presentment of checks with images  
                                   2. RRF*.XML – Outward Returns of checks 
 
 
 
3. ERF*.XML – Extension/paper Request File from drawee bank 
 
Files sent by CHI:   1. wPXF*.XML and wPIBF*.IMG – Inward Presentment of checks with images  
                                   2. wRF*.XML – Inward Returns of checks 
                                   3. *.XML.f.RES – Response file for every incoming file (ack/reject) 
4. wEF*.XML – Extension/Paper request File 
wDREF*.XML – Extension request File for DRAWEE Module to indicate its items 
that were extended by the CH on behalf of the CHI (e.g. Holiday)

<!-- Page 70 -->

 
CTS Clearing House Interface – Specification 
 
 
70 
5. *.xml.<session_information>.OACK – Outward Acknowledgement File for CXF 
& RRF  
 
Where, “w” indicates either Master, Bank, Branch or All other files and “f” indicates the file id of the 
Response file. 
Appx 2.2 Presentment Flow 
The capture system sends captured items to the CHI as outward presentment. These items are sent in a 
set of two files;  
1) Capture eXchange File (CXF) which contains check data in XML format and a 
2) Capture Image Binary File (CIBF) containing check images. 
CHI receives the files and validates the files for file integrity, data integrity and Image Quality.  
 
If a file is invalid, then the whole file is rejected (.RES) and sent back to the capture system, 
with the FileStatus set to indicate the problem (By invalid file, we mean a file whose syntax is 
incorrect or whose format does not match with what we have mentioned in this specification. 
For reasons due to which a file can be termed as invalid, refer section 4.3.10.3.3.1in which the 
REJECT REASON attribute is N.A.).  
 
If any items in the file are invalid then those items are included in the Response file (.RES) with 
reject reason, and with the FileStatus set to indicate some items failed (For reasons due to 
which an item can be termed as invalid, refer section 4.3.10.3.3.1in which the REJECT 
REASON attribute is not N.A.).  
 
If the file is successfully accepted by CHI, then no items are included in the Response file 
(.RES), and the FileStatus is set to indicate success so that a positive acknowledgement is 
sent to the capture system.  
Once the items are accepted by the CHI, it processes the data, digitally signs the MICR data and image 
views and generates exchange file for the Clearing House (CH). Each exchange file is digitally signed 
and encrypted before it is transmitted to the CH. A clearing session must be open and available with CH, 
in order to send exchange files to the CH.  
CH decrypts the files, loads its contents into database, validates the data, clears and sorts the items by 
receiving bank, settles the data and generates inward exchange files for the CHI.  
CHI receives the inward exchange files, decrypts them, loads into database and generates inward 
presentment files for the drawee bank. The inward presentment data is sent in a set of two files;  
1) Posting eXchange File (wPXF) which contains check data in XML format and  
2) Posting Image Binary File (PIBF) containing check images.  
The single posting file set (PXF and PIBF) contain the data and images for the entire session. 
When the CHI receives end of session information from the CH, it creates an Outward Acknowledgement 
file for Presenting Bank module which contains Outward Presentment items that were accepted and 
settled successfully at the CH. 
Appx 2.3 Return Flow 
A drawee bank receives the inward presentment as inclearings and processes them for pay/no pay 
decisioning (exception processing). A Return Request File (RRF) is generated in XML format and sent to 
CHI.  The Return Request File has all the outgoing returns with return reason in it. This file does not 
include images of returns.   
CHI receives the file, validates the file for the file integrity and data integrity.

<!-- Page 71 -->

 
CTS Clearing House Interface – Specification 
 
 
71 
 
If a file is invalid, then the whole file is rejected (.RES) and sent back to the drawee system, 
with the FileStatus set to indicate the problem (By invalid file, we mean a file whose syntax is 
incorrect or whose format does not match with what we have mentioned in this specification. 
For reasons due to which a file can be termed as invalid, refer section 4.3.10.3.3.1in which the 
REJECT REASON attribute is N.A.). 
 
If any items in the file are invalid then those items are included in the Response file (.RES) with 
reject reason, and with the FileStatus set to indicate some items failed (For reasons due to 
which an item can be termed as invalid, refer section 4.3.10.3.3.1in which the REJECT 
REASON attribute is not N.A.). 
 
If the file is successfully accepted by CHI, then no items are included in the Response file 
(.RES), and the FileStatus is set to indicate success so that a positive acknowledgement is 
sent to the return processing system.  
The CHI then processes the data and generates exchange file for the CH. Each exchange file is digitally 
signed and encrypted before it is transmitted to CH.  
CH decrypts the files, loads its contents into database, validates the data, clears and sorts the items by 
receiving bank, settles the data and generates inward exchange files for the CHI.  
CHI receives the inward exchange file, decrypts them, loads into database and generates inward 
Returns File (RF) for the presenting bank. 
When the CHI receives end of session information from the CH, it creates an Outward Acknowledgement 
file for Drawee Bank module which contains Outward Return items that were accepted and settled 
successfully at the CH. 
  
Appx 2.4 Extension or paper request Flow 
A drawee bank can request an extension on the return period for an item or request paper for an item 
using Extension request file. These extension requests, if valid as per the clearing rules set by RBI/NPCI, 
will be routed back to the presenting bank with extension period and extension reason.  
 
If a file is invalid, then the whole file is rejected (.RES) and sent back to the drawee system, 
with the FileStatus set to indicate the problem (By invalid file, we mean a file whose syntax is 
incorrect or whose format does not match with what we have mentioned in this specification. 
For reasons due to which a file can be termed as invalid, refer section 4.3.10.3.3.1in which the 
REJECT REASON attribute is N.A.).. 
 
If any items in the file are invalid then those items are included in the Response file (.RES) with 
reject reason, and with the FileStatus set to indicate some items failed (For reasons due to 
which an item can be termed as invalid, refer section 4.3.10.3.3.1in which the REJECT 
REASON attribute is not N.A.).  
 
If the file is successfully accepted by CHI then no items are included in the Response file 
(.RES) , and the FileStatus is set to indicate success so that a positive acknowledgement is 
sent to the return processing system. 
 
For items that have been extended at the CH on behalf of the CHI, then the Drawee CHI will send a 
DREF file to the Drawee module to communicate the extension period and extension reason for the 
items.

<!-- Page 72 -->

 
CTS Clearing House Interface – Specification 
 
 
72 
Appx 2.5 Interface Files 
 
Capture Exchange 
File 
Capture eXchange File (CXF) is generated by the Capture and sent to the CHI for 
outward presentment 
. 
One CXF file contains a group of items (recommended 250 items) of the same 
presentment date.  
CXF file contains the MICR financial data of items along with the image data 
attributes to locate, interpret and process images within its corresponding CIBF file.  
 
Capture Image 
Binary File 
The Capture Image Binary File (CIBF) contains the image binary data for every 
item view described in corresponding CXF file.  
Every CXF file must have one associated CIBF file.  
 
Response Files 
Response file (.RES) is created for every file received by the CHI. The file name 
will be the original filename with a file id and “.RES” extension added at the end. 
If any items from the incoming file are rejected either for a syntax error or any other 
valid reasons, then the items are returned in the Response file with a reject reason 
and a FileStatus set to indicate the problem.  
CHI will generate a Response file with no items included and the FileStatus set to 
indicate success, thus making this file a positive acknowledgement.  
Response files do not include any images. They are created in the same directory 
in which the CHI receives its corresponding CXF / RRF / ERF file. 
Posting Exchange 
File 
The Posting eXchange file (PXF) is generated by the CHI for the Receiving bank’s 
in-clearing system, using the data received from the Clearing House. These are 
inward presentments. The CHI generates mainly three types of posting files: Master 
Posting Files for all items received at the CHI, Bank Posting file for every bank 
within the CHI and Branch Posting file for every branch configured within a bank.  
In case of Branch posting file, a separate file is created for every unique transaction 
code.  
PXF contains the MICR financial data of items along with the image data attributes 
to locate, interpret and process images within its associated PIBF file.  The number 
of items in PXF file will be a configurable parameter at the CHI. 
 
Posting Image 
Binary File 
 The Posting Image Binary File (PIBF) contains the image binary data for every 
item view described in corresponding PXF file and the digital signatures of image 
views.  
Every PXF file shall have at least one associated PIBF file. 
 
Return Request 
File 
The Return Request file (RRF) is provided to the CHI by the receiving bank’s return 
processing system. The Return Request file consists of a list of items that are to be 
returned unpaid by the receiving bank, with a return reason for each item. These 
items do not need to be sorted by presenting bank. The return request files have no 
associated image files as returns are MICR data only.

<!-- Page 73 -->

 
CTS Clearing House Interface – Specification 
 
 
73 
 
Return File 
Return File (RF) is generated by the CHI system for the Presenting bank’s Return / 
Exception processing system using the return data received from the clearing 
house system. 
CHI generates three types of Return files: Master Return files for all items received 
at the CHI, Bank Return file for every bank within the CHI and Branch Return file for 
every branch configured within every bank. In case of branch Return file, a 
separate file is created for every unique transaction code. 
 
RF contains only the MICR financial data of items along with their Return Reason 
code. 
Return file has no associated images. 
 
 
Extension 
Request File 
The Extension Request file (ERF) is generated by the drawee bank when it needs 
an extension for an item or needs the physical paper item. The extension required 
could be a result of: 
1) fail to process inward clearing for whatever reason and desire extension on 
return time,  
2) Need extra day for cash,  
3) item needs to be researched,  
4) bad image need paper etc.   
The file will include extension period and extension reason. 
 
Extension File 
Drawee Extension 
File 
Extension File (EF) is generated by the CHI system for the Presenting bank’s 
capture system. Extension File (DREF) is generated by the Drawee CHI system for 
the Drawee bank’s drawee system.  The file will have items that require the 
physical paper to be sent, and items that need extensions on return period and can 
be used by the bank/branch to hold credit on the customer account.  
 
Outward 
Acknowledgement 
File 
 
The Outward Acknowledgement (OACK) File  consists of a list of all items that were 
successfully added to a session and settled at the CH. Outward Acknowledgement 
Files are generated for all outward files that affect the settlement of a session i.e. 
capture file (CXF) and Return Request File (RRF).  
OACK files are created in the same directory in which the CHI receives its 
corresponding CXF / RRF file. 
CH Master Data 
File 
The following Clearing House Master data shall be available for use by the capture 
systems.   
 
Clearing House and Clearing Center, including Bank/Branch and 
blockages 
 
Item Return Reason 
 
Calendar 
 
Bundle Collection 
 
Session Definition and Collection Type 
 
Clearing Type and DocType definitions 
 
Item Extension Reason

<!-- Page 74 -->

 
CTS Clearing House Interface – Specification 
 
 
74 
 
Translation Rules 
 
Transaction Code 
 
City Master 
 
AtParBank Master 
End of Session 
File 
The End of Session file (.eos) is created by the CHI after creating all the applicable 
PXF/PIBF and RF files for a session. 
These are 0KB files created to signal the bank modules that all the PXF and PIBF 
Files have been created for a session. 
Unwound Item File The Unwound item(s) file notifies the bank of items that have been unwound at the 
CH due to a Clearing House Notification. This file will be generated and given to 
each affected bank directly by the CH.  
► Unlike other interface files, this file will not be created at the CHI, and is 
not a part of the normal CHI interface.

<!-- Page 75 -->

 
CTS Clearing House Interface – Specification 
 
 
75 
Appx 3 
File Transmission Specifications 
Appx 3.1 Presentment and Return Files deposit time 
Presentment and Return files from the bank must be received at the CH via the CHI prior to the clearing 
session deadline. A capture file has been sent to a CHI only when the entire file has been transmitted 
and delivered to the CHI folder.  Based on the size of the file, there may be a significant delay between 
the time you begin to send a file and the completion of the file transmission. The CHI must load, validate 
and process this file for onward transmission to the CH (outward file). Files that are received by the CHI 
after a session deadline will be considered deposited for the next session deadline. Outward files 
received at the CH after a session deadline will be rejected and will have to be reattached to a new 
session at the CHI.  
 
Appx 3.2 Connectivity for Files Transfer 
Bank will send its presentment and return files to CHI using predefined folders. Banks also have an 
option to send presentments and returns on a media (CD/DVD).  The files on the media must be copied 
to the appropriate predefined folders. 
Banks will receive presentments and returns from the predefined folders on CHI. The files can be 
received either using ftp, file-copy, or shared-drive, but ftp (secure FTP) is the preferred method for 
ECPIX.  Banks have an option to receive presentments and returns on a media (CD/DVD). 
Appx 3.3 File Transfer  
In order to ensure files are completely transferred to CHI before CHI can start processing, the capture 
systems will ftp or copy a semaphore file with the same file name as the data file with “.done” extension 
at the end E.g. after ftp’ing a given capture file “CXF*”, the capture will ftp an empty file with name 
“CXF*.done” indicating CXF* file can now be used for processing. This is required for any file sent to 
CHI. For completeness, all *.done files will be included on the media as well. 
The CHI shall ensure that any file it creates are complete when they appear in the predefined directory, 
so the inclearing or return processing system can pull them using ftp. Once the files are picked up from 
the CHI, the files must be validated to ensure they were not corrupted or interrupted during transmission, 
and then they must be renamed to *.done by the bank’s inclearing or return processing system.  
Inclearing systems may decide to pickup PXF files first, and then the PIBF files for better exception 
handling. 
The files renamed as *.done shall be purged by the CHI from the output folder. 
In order for bank modules to determine that the CHI has created all the inward files (PXF/PIBF and RF) 
for a session, then the CHI will create empty semaphore files.  The file is named as follows: 
 
<session_no>_<session_date>.eos 
- indicates the end-of-session 
This file is created in the same folder location as the PXFs and RFs that they are semaphoring. 
 
Appx 3.4 File Folder 
The CHI has file folders for use by all the systems that connect to the CHI to perform tasks related to the 
Clearing System.  This section describes the various folders and indicates how they are used in 
interacting with the CHI. 
 
For use by participating banks and remote branches.  These are the main folders where the 
clearing data goes.

<!-- Page 76 -->

 
CTS Clearing House Interface – Specification 
 
 
76 
 
For providing the necessary ClearingHouse Master data, that can be used by the presenting bank 
and drawee bank modules for their clearing operations 
 
For use by the CHI in communications with the CH 
 
Appx 3.4.1 Participating Bank and Remote Branch Folders 
CHI will have file folders created for the participating banks and remote branches. The banks/branches 
will send their files to these folders as well as receive their files from these folders.  
The folder structure for capture and bank level posting files are: 
<ftp_root>/users/<CHI_RT_number>/<bank1_RT_number> 
<ftp_root>/users/<CHI_RT_number>/<bank2_RT_number> 
 
The folder structure for capture and city level posting files are: 
<ftp_root>/users/<CHI_RT_number>/<bank1_RT_number>/<city1>/<branch1_RT_number> 
<ftp_root>/users/<CHI_RT_number>/<bank1_RT_number>/<city1 >/<branch2_RT_number> 
<ftp_root>/users/<CHI_RT_number>/<bank1_RT_number>/<city2>/<branch3_RT_number> 
<ftp_root>/users/<CHI_RT_number>/<bank1_RT_number>/<city2 >/<branch4_RT_number> 
 
The folder structure for capture and branch level posting files are: 
<ftp_root>/users/<CHI_RT_number>/<bank1_RT_number>/<branch1_RT_number> 
<ftp_root>/users/<CHI_RT_number>/<bank1_RT_number>/<branch2_RT_number> 
 
The “<root ftp>” folder will be configurable on the CHI, and Valid ‘users’ are created in it. 
“<CHI_RT_number>” refers to Routing Number of CHI. 
“<bank1_RT_number>” refers to Routing Number of Bank. 
“<city2 >” refers to city code. 
“<branch1_RT_number>” refers to Routing Number of Branch. 
 
The following table lists the input and output folders that are used by the Presenting Bank module, and 
the Drawee Bank module.  Further it explains the folder use for situations where the module exists in an 
‘centralised’ fashion, and in a ‘distributed’ fashion. 
 
PRESENTING BANK MODULE 
FILE TYPE 
CENTRALISED 
DISTRIBUTED 
CXF 
CIBF 
1. FTP to Bank folder and transfer 
files 
2. Directly copy to shared Bank 
folder 
1. FTP to City/Branch folder and 
transfer files 
2. Directly copy to shared 
City/Branch folder  
 
RES (for CXF) 
Shall be placed in the same folder 
where CXF is received 
 
Shall be placed in the same 
folder where CXF is received 
 
OACK (for 
Shall be placed in the same folder 
Shall be placed in the same

<!-- Page 77 -->

 
CTS Clearing House Interface – Specification 
 
 
77 
CXF) 
where CXF is received 
 
folder where CXF is received 
 
EF 
1. FTP Login to Bank folder and 
pick up files 
2. Pick up files directly from 
shared Bank folder 
 
1. FTP Login to Branch folder 
and pick up files 
2. Pick up files directly from 
shared Branch folder 
 
RF 
.eos 
1. FTP Login to Bank folder and 
pick up files 
2. Pick up files directly from 
shared Bank folder 
 
1. FTP Login to Branch folder 
and pick up files 
2. Pick up files directly from 
shared Branch folder 
 
DRAWEE BANK MODULE 
FILE TYPE 
CENTRALISED 
DISTRIBUTED 
PXF 
PIBF 
.eos 
1. FTP Login to Bank folder and 
pick up files 
2. Pick up files directly from 
shared Bank folder 
 
1. FTP Login to Branch folder 
and pick up files 
2. Pick up files directly from 
shared Branch folder 
 
ERF 
1. FTP to Bank folder and transfer 
files 
2. Directly copy to shared Bank 
folder  
 
1. FTP to City/Branch folder and 
transfer files 
2. Directly copy to shared 
City/Branch folder  
 
RES (for ERF) 
Shall be placed in the same folder 
where ERF is received 
 
Shall be placed in the same 
folder where ERF is received 
 
DREF 
1. FTP Login to Bank folder and 
pick up files 
2. Pick up files directly from 
shared Bank folder 
 
1. FTP Login to Branch folder 
and pick up files 
2. Pick up files directly from 
shared Branch folder 
 
RRF 
1. FTP to Bank folder and transfer 
files 
2. Directly copy to shared Bank 
folder  
 
1. FTP to City/Branch folder and 
transfer files 
2. Directly copy to shared 
City/Branch folder  
 
RES (for RRF) 
Shall be placed in the same folder 
where RRF is received 
 
Shall be placed in the same 
folder where RRF is received 
 
OACK (for 
RRF) 
Shall be placed in the same folder 
where RRF is received 
 
Shall be placed in the same 
folder where RRF is received 
 
 
Appx 3.4.2 Clearing House Master Data Folder 
The folder structure for Clearing House Master data file is: 
<ftp_root>/users/CHMaster

<!-- Page 78 -->

 
CTS Clearing House Interface – Specification 
 
 
78 
Appx 3.4.3 CHI and CH Data Folder 
CHI will also have file folders created for exchanging files with the CH (these folders are ECPIX system 
folders, and are not exposed or used by the presenting/drawee systems).  
The folder structures for exchange files between the CHI and CH are: 
<system path>/date/exchangeout 
<system path>/date/exchangein 
 
 
Appx 3.5 Duplicate Files 
CHI will prevent duplicate files having the same filename from being processed again. Duplicate file will 
be rejected with reject reason.  
 
Appx 4 
Interface Files 
All systems across the Cheque truncation System should uniquely identify items by using the Unique 
Document Key (UDK).  The UDK used in ECPIX is defined in section Appx 4.1.3.3. 
Appx 4.1 CAPTURE EXCHANGE FILE (CXF) 
Capture eXchange files are provided by the Capture to CHI with forward presentment data for clearing 
purposes.  
One CXF File will contain a group of items (typically 250 items) of the same presentment date and from 
the same bank. The bank may present more than one CXF file at any time. 
CHI will be performing IQA on the items, and will digitally sign the items. In addition the capture system 
must include the following before sending the data to the CHI 
 
digitally signed MICR data and images  
 
IQA results for the images  
There can be only one MICRDS tag for an item in the CXF file. There can be only one ImageDS tag and 
ImageViewAnalysis tag for an image view in the CXF file. 
Appx 4.1.1 File Name Convention 
B1 
The Capture eXchange File name shall use the following naming convention: 
 
CXF_nnnnnnnnn_ddmmyyyy_hhmmss_xx_bbbbbbbbbb.XML 
Where: 
 
CXF   
Capture eXchange File 
 
nnnnnnnnn 
Capturing bank/branch Routing Number  
 
ddmmyyyy 
Creation Date (same as in File Header) 
 
hhmmss 
Creation Time (same as in File Header) 
 
xx 
 
Clearing Type (see Appendix CC for details) 
 
bbbbbbbbbb File ID  
 
.XML  
Is a mandatory file type suffix 
B2 
File ID shall be a minimum of 1 character and a maximum of 10 characters and must be unique in 
a processing day for a given bank.

<!-- Page 79 -->

 
CTS Clearing House Interface – Specification 
 
 
79 
Appx 4.1.2 File Structure 
ImageDS
AddendA
FileSummary
FileHeader
Item
ImageViewAnalysis
ImageViewDetail
Capture eXchange File Structure
Mandatory 
Element
Multiple 
Elements
Optional 
Element
MICRDS
ImageViewData
 
A1 
The Capture eXchange file structure shall be: 
<FileHeader …   > 
<Item …   > 
  <AddendA …       /> 
                                         <MICRDS …    /> 
                                         <ImageViewDetail …   > 
                                                            <ImageViewData …   /> 
                                                            <ImageDS … />                   
                                                            <ImageViewAnalysis …   /> 
                                         </ImageViewDetail> 
                                              : 
</item> 
<FileSummary …   /> 
</FileHeader> 
A2 
Elements “FileHeader”, “Item”, “MICRDS”, “AddendA”, “ImageViewDetail”, “ImageViewData”, 
“ImageDS”, “ImageViewAnalysis” and “FileSummary” are mandatory 
A3 
Ordering of tags is critical, to avoid penalty of additional SQL update for every image view for 
every item.

<!-- Page 80 -->

 
CTS Clearing House Interface – Specification 
 
 
80 
 
A sample Capture eXchange File is shown in (Appendix AA) 
Appx 4.1.3 Elements and Attributes 
FileHeader Must be greater than  
Appx 4.1.3.1 FileHeader 
 
Attributes of FileHeader 
Attribute Name 
Description/ 
Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
Xmlns 
Schema definition 
For CXF, must 
be 
 
for SHA256 
algorithm support 
 
urn:schemas-
ncr-
com:ECPIX:CX
F:FileStructure:
010005 
 
For RRF, must 
be  
for SHA256 
algorithm support 
 
urn:schemas-
ncr-
com:ECPIX:RR
F:FileStructure:
010004 
 
For RF, must 
be 
urn:schemas-
ncr-
com:ECPIX:RF:
FileStructure:01
0001 
 
For ERF, must 
be 
urn:schemas-
ncr-
com:ECPIX:ER
F:FileStructure:
010002 
 
For EF, must 
ANS 
48 
50 
M

<!-- Page 81 -->

 
CTS Clearing House Interface – Specification 
 
 
81 
Attribute Name 
Description/ 
Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
be 
urn:schemas-
ncr-
com:ECPIX:EF:
FileStructure:01
0001 
 
For DREF, 
must be 
urn:schemas-
ncr-
com:ECPIX:DR
EF:FileStructur
e:010001 
 
VersionNumber 
Version of this 
Interface definition– 
Xxyyyy 
xx = country 
(01=RBI/NPCI) 
yyyy = version 
0005 
NS 
6 
6 
M 
TestFileIndicator 
 
P ( Production 
Must be   P 
A 
1 
1 
M 
CreationDate 
File creation date  
Should be same as 
in the filename. 
Date should be 
in DDMMYYYY 
format 
DATE 
8 
8 
M 
CreationTime 
File creation time  
Should be same as 
in the filename. 
Time should be 
HH24MISS 
format 
TIME 
6 
6 
M 
FileID 
A number that 
uniquely identifies 
the items in this 
file. Should be 
same as in the file 
name. 
Must be greater 
than 0 
AN 
1 
10 
M 
 
** When CHI detects CXF version 010005, those items will be validated as per version 010005

<!-- Page 82 -->

 
CTS Clearing House Interface – Specification 
 
 
82 
Appx 4.1.3.2 FileSummary 
Attributes of FileSummary 
 
Attribute Name 
Description/ 
Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
TotalItemCount 
Total number of 
items in file 
Must be greater 
than 0. 
N 
1 
8 
M 
TotalAmount 
Total amount of 
items in the file 
Must be greater 
than 0. 
N 
1 
18 
M 
Appx 4.1.3.3 Item 
 
Note: The fields with * in item table form the Unique Document Key (UDK) for that item and 
consists of: 
 <PresentmentDate>< PresentingBankRoutNo>< CycleNo>< ItemSeqNo> 
 
It is capture system’s responsibility to ensure these fields give uniqueness over a day for a given 
bank.  Items that fail this constraint are considered duplicates and will be rejected/returned to the 
capture system. 
 
Attributes of Item 
 
Attribute Name 
Description/ 
Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
ItemSeqNo* 
 
 
This is a unique 
identifier for the 
bank for a 
“PresentmentDate” 
Suggested 
combination: 
<SorterID(6)><Run
No(2)><Sequence
No(6)> 
Must be greater 
than 0. 
NS 
14 
14 
 
 
M 
PayorBankRoutNo 
Drawee Bank 
Routing number 
Must be greater 
than 0 
NS 
9 
9 
M 
Amount 
Check amount 
Must be greater 
than 0 
N 
1 
18 
M 
AccountNo8 
Drawee account 
number 
 
NS 
6 
7 
M12 
                                               
12 NPCI will inform the effective date for mandatory 
8 The capture system must consider special case for Short Account Number (SAN).  They are: 
 
Account Number value shall be mandatory 6 digits for 2 digits Transcode. Example SAN 123456 and 
Transcode 78 is valid scenario. 
 
Account Number value shall be mandatory 7 digits for 3 digits Transcode. Example SAN 1234567 and 
Transcode 890 is valid scenario. 
 
 If SAN is “1”for a particular account number then banks are expected to give AccountNo as “000001” i.e. 1 
is padded with 5 times zero.

<!-- Page 83 -->

 
CTS Clearing House Interface – Specification 
 
 
83 
Attribute Name 
Description/ 
Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
SerialNo 
Check number 
Must be greater 
than 0 
NS 
6 
6 
M 
TransCode 
(see also footnote for 
AccountNo) 
Transaction code 
Must be greater 
than 0 
NS 
1 
3 
M 
PresentingBankRoutNo* 
Routing number of 
the presenting 
bank 
Must be greater 
than 0 
NS 
9 
9 
M 
PresentmentDate* 
Date of capture of 
checks 
Date should be 
in DDMMYYYY 
format 
DATE 
8 
8 
M 
CycleNo* 
Capture cycle 
number. 
Must be greater 
than 0 
NS 
 
2 
2 
M 
NumOfImageViews 
Number of image 
views for an item 
(3) 
N 
1 
1 
M 
ClearingType 
See Appendix CC 
for details 
Must be greater 
than 0 
NS 
2 
2 
M 
DocType 
 
 
The documentation 
type indicates 
the electronic 
versus physical 
cheque. 
A – ECP with 
Paper to Follow 
(no images) 
B – Image to 
Follow without 
paper 
C – Image to 
Follow with 
Paper to 
Follow–D - 
Image 
Presentment–E 
- Image 
Presentment 
with Paper to 
Follow. 
F – ECP 
A|B|C|D|E|F 
 
(B) 
 
A 
1 
1 
M 
                                                                                                                                                                     
 
 If SAN is not present, banks must capture default value as "000000”.

<!-- Page 84 -->

 
CTS Clearing House Interface – Specification 
 
 
84 
Attribute Name 
Description/ 
Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
MICRRepairFlags9 
 
 
Flags to be set if 
the read code line 
has been 
corrected.   
‘xxxxy1’: if any field 
of the code line 
is corrected. 
‘xxxx9x’: if account 
is new. 
‘xxxx5x’: if account 
is old. 
 
‘xxx1y1’: if 
transaction 
code is repaired 
‘xx1xy1’: if account 
code is repaired 
‘x1xxy1’: if sort 
code is repaired 
‘1xxxy1’: if serial 
number is 
repaired 
x: could be ‘0’ or ‘1’ 
y: could be ‘0’ or ‘9' 
or ‘5’ 
 (000000) 
NS 
6 
6 
M 
SpecialHandling 
SpecialHandling 
indicator is 
reserved for future 
use. 
0 = Normal 
(0) 
 
N 
1 
2 
O 
TruncatingRTNo 
RT number of the 
truncating branch 
 
NS 
9 
 
9 
O 
UserField 
RBI/NPCI 
requested for use 
by the banks 
String validation 
is as per RBI 
Guidelines. 
ANS 
1 
25 
M 
IQAIgnoreInd10 
To allow capture 
system to send bad 
image when image 
cannot be 
improved.   
0 – perform IQA 
to detect bad 
images.  
1 – Accept the 
image 
irrespective of 
its quality. 
(0) 
N 
1 
1 
O 
                                               
9 Validations for MICR flag - If the last digit is '0', then none of the preceding first 4 digits should be '1' and If the last 
digit is '1', then at least one or more value of 1st to 4th digit should have value '1'. Value of the 5th digit should have 
value '0' or '9' or ‘5’.  
For e.g: 
Valid values - 010001 000101 001001 100001 000191 010091 001091 100091 000090 000000 000050 111051 
Invalid values - 000001 100000 001000 000100 000010 000091 100090 001090 000190 100010 010000 010090 
000150 000051

<!-- Page 85 -->

 
CTS Clearing House Interface – Specification 
 
 
85 
Attribute Name 
Description/ 
Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
CurrencyInd 
 
 
To indicate the 
currency of the 
item. 
See ISO standa– -- 
ref[3] 
CAD: is for 
Canadian Dollar 
USD: is for US 
Dollar 
INR: is for Indian 
Rupee 
(INR) 
AN 
3 
3 
O 
 
 
                                                                                                                                                                     
10 CHI performs IQA on every image. An item is rejected if the image is detected to be bad. Normally capture 
should attempt to re-scan the item to get a better image.  But if capture cannot provide a better image that will pass 
IQA, then capture must use this flag along with a DocType that requires ‘paper to follow’ and resubmit the item to 
the CHI where it will then be processed.

<!-- Page 86 -->

 
CTS Clearing House Interface – Specification 
 
 
86 
Appx 4.1.3.4 MICRDS 
It is mandatory for capture to provide a MICR digital signature for every item in the CXF file.   
The source attribute in the MICRDS tag supplied in CXF file should have the value set as 
“Capture” e.g.Source=”Capture”.  
 
Attributes of MICRDS 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
Source 
Indicates if digital 
signature is coming 
from the capture 
system or from the 
CHI (or from 
Drawee in the case 
of RRF).  
Capture | 
ECP.PBCC | 
Drawee 
 
ANS 
6 
16 
M 
DigitalSignatureMethod 
 
 
DSA_with_SHA1 
RSA_with_MD5 
RSA_with_MDC2 
RSA_with_SHA1 
ECDSA_with_SHA
1 
RSA_with_SHA256 
RBI/NPCI 
requires 
‘RSA_with_SH
A256’  
ANS 
15 
15 
M 
SecurityKeySize 
1024 
2048 
RBI/NPCI 
requires ‘2048’ 
N 
4 
4 
M

<!-- Page 87 -->

 
CTS Clearing House Interface – Specification 
 
 
87 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
MICRFingerPrint 
 
  
Indicates the 
combination of 
fields from item tag 
which is used to 
create Digital 
Signature 
 
If “source” is 
“Capture” then this 
field is capture 
defined and should 
cover a minimum of 
the following fields 
from the MICR line 
SerialNo;PayorBan
kRoutNo;TransCod
e;Amount. 
 
If “source” is 
ECP.PBCC then 
the format is: 
“PresentmentDate;Pr
esentingBankRoutNo
;CycleNo;ItemSeqNo;
Amount;SerialNo;Tra
nscode” 
 
See NOTE: at end 
of section. 
 
ANS 
1 
256 
M 
DigitalSignatureLength 
 
Must be greater 
than 0.  
For 2048 Bit 
Key size =344 
N 
3 
3 
M 
SignatureData11 
Base 64 encoded 
MICR digital 
signature 
 
ANS 
1 
350 
M 
                                               
11 RSA digital signatures result in largest SignatureData size.  RSA at 1024 bits, then base64 encoded results in 
172 characters of data.  RSA at 2048 bits, then base64 encoded results in 344 characters of data.  The size is set 
to 350 for safety.

<!-- Page 88 -->

 
CTS Clearing House Interface – Specification 
 
 
88 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
SecurityOriginatorName 
 
 
If “source” is 
Capture this must 
be the common 
name of the 
certificate / key 
used. 
(unique designation 
of the entity that 
created the digital 
signature) 
 
If “source” is 
ECP.PBCC this will 
be the common 
name of the 
certificate / key 
used. 
(unique designation 
of the entity that 
created the digital 
signature) 
 
ANS 
1 
16 
M 
SecurityAuthenticatorName 
 
 
If “source” is 
Capture this must 
be set to provide 
additional 
uniqueness of 
Originator/KeyNam
e. 
(unique designation 
of the entity that 
authenticates the 
digital signature) 
 
If “source” is 
ECP.PBCC this will 
be set to provide 
additional 
uniqueness of 
Originator/KeyNam
e. 
(unique designation 
of the entity that 
authenticates the 
digital signature) 
 
ANS 
1 
16 
M

<!-- Page 89 -->

 
CTS Clearing House Interface – Specification 
 
 
89 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
SecurityKeyName 
If “source” is 
Capture this must 
be the serial 
number of the 
certificate / key 
used. 
 
If “source” is 
ECP.PBCC this will 
be the serial 
number of the 
certificate / key 
used. 
 
ANS 
1 
16 
M 
 
NOTE: The MICRFingerPrint attribute identifies the fields that are used in the creation of a digitally 
signed MICR Fingerprint.  As an illustrative example, the MICRFingerPrint could be 
“TransCode;Amount”. 
ECPIX will use the values of the identified fields in order to create and then digitally sign the 
MICR FingerPrint.  Again, as an illustrative example, assume that the TransCode for the item is 
“35” and the Amount is “24680”.  The steps taken in creating the digitally signed MICR FingerPrint 
are: 
 
make a message using the values for the identified fields, in order.  The values for each field 
are terminated by a semicolon.  Thus the message in the example is: 
“35;24680;” 
 
perform a digital signature on this message, from the first character (the ‘3’) for the whole 
length of  the message (which is a length of 9 and includes the final ‘;’) 
 
store the resulting digital signature and relevant data in the remaining attributes of the 
MICRDS element. 
Appx 4.1.3.5 AddendA 
AddendA is a Bank Of First Deposit (BOFD) record. 
 
Attributes of AddendA 
Attribute Name 
Description/ Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
BOFDRoutNo 
Bank of First Deposit 
RT number 
Must be greater 
than 0 
NS 
9 
9 
M 
BOFDBusDate 
Endorsement Date 
when check was 
received at BOFD 
Date should be 
in DDMMYYYY 
format 
DATE 
8 
8 
M 
DepositorAcct 
Depositor account 
number 
 
NS 
1 
25 
O 
IFSC 
Indian Financial 
System Code 
 
AN 
11 
11 
M

<!-- Page 90 -->

 
CTS Clearing House Interface – Specification 
 
 
90 
Appx 4.1.3.6 ImageViewDetail 
Attributes of ImageViewDetail 
Attribute Name 
Description/ Format 
Value 
(default) 
Type 
Size 
Usag
e 
Min 
Max 
ViewFormat 
The image format 
used in the related 
ImageViewData 
element 
TIFF|JFIF 
ANS 
4 
4 
M 
CompressionType 
The image 
compression algorithm 
used in the related 
ImageViewData 
element 
None | G4 | 
JPEG 
ANS 
2 
4 
M 
ViewSideIndicator 
The image view 
conveyed in the 
related 
ImageViewData 
element 
Front BW| 
Back BW | 
Front Gray  
ANS 
4 
10 
M 
ViewDescriptor 
The nature of the 
image view conveyed 
in the related 
ImageViewData 
element 
(Full)  
ANS 
1 
16 
M 
ImageAvailable 
Indicates an image 
available in the related 
ImageViewData 
element 
Y | N (Y) 
A 
1 
1 
M 
ImageReproducable 
Indicates the sender 
has the ability to 
recreate the image 
view 
Y | N (Y) 
A 
1 
1 
O 
ReplacementDocIndicato
r 
Indicates if the image 
is of the original (N) or 
is a substitute (Y) 
Y | N (N) 
A 
1 
1 
O 
ImageCreatorRoutNo 
Indicates the financial 
institution that created 
the image. 
 
NS 
9 
9 
O 
ImageCreationDate 
Date assigned by the 
financial institution 
when creating the 
image. 
Date should 
be in 
DDMMYYYY 
format 
DATE 
8 
8 
O 
UserField 
 
 
ANS 
1 
256 
O 
 
Appx 4.1.3.7 ImageDS 
It is mandatory for capture to provide digital signature for each image view in the CXF file.   
The source attribute in the ImageDS tag supplied by capture should have the value set as 
“Capture” e.g.Source=”Capture”.

<!-- Page 91 -->

 
CTS Clearing House Interface – Specification 
 
 
91 
Attributes of ImageDS 
Attribute Name 
Description/ Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
max 
Source 
Indicates if digital 
signature coming from 
capture system or from 
the CHI. 
Capture | 
ECP.PBCC 
ANS 
7 
8 
M 
DigitalSignatureMethod 
 
 
DSA_with_SHA1 
RSA_with_MD5 
RSA_with_MDC2 
RSA_with_SHA1 
ECDSA_with_SHA1 
RSA_with_SHA256 
RBI/NPCI 
requires 
‘RSA_with_SH
A256’- v0004 
 
ANS 
15 
15 
M 
SecurityKeySize 
1024 
2048 
RBI/NPCI 
requires 
‘2048’- v0004  
Must be greater 
than 0 
N 
4 
4 
M 
StartOfProtectedData 
offset in bytes from the 
first byte (counted as 
byte 1) of the protected 
data that is signed 
Must be greater 
than 0 
N 
8 
8 
M 
ProtectedDataLength 
Length of the data that 
is signed. 
Must be greater 
than 0 
N 
1 
8 
M 
DigitalSignatureDataOffset Offset of the digital 
signature in the file 
Must be greater 
than 0 
N 
1 
10 
M 
DigitalSignatureLength 
Length of digital 
signature. 
It is assumed that the 
digital signature is 
stored in binary form in 
the file; it is not 
encoded. 
Must be greater 
than 0 
For 2048 Bit 
Key size =256 
N 
3 
3 
M 
FileName 
File name where 
signature is stored.  
This is the same file 
where the image data 
is stored. 
 
ANS 
1 
256 
M 
SecurityOriginatorName 
 
 
If “source” is Capture 
this will be the 
common name of the 
certificate / key used. 
(unique designation of 
the entity that created 
the digital signature) 
 
If “source” is 
ECP.PBCC this will be 
the common name of 
the certificate / key 
used. 
(unique designation of 
 
ANS 
1 
16 
M

<!-- Page 92 -->

 
CTS Clearing House Interface – Specification 
 
 
92 
Attribute Name 
Description/ Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
max 
the entity that created 
the digital signature) 
SecurityAuthenticatorNam
e 
 
 
If “source” is Capture 
this will be set to 
provide additional 
uniqueness of 
Originator/KeyName. 
(unique designation of 
the entity that 
authenticates the 
digital signature) 
 
If “source” is 
ECP.PBCC this will be 
set to provide 
additional uniqueness 
of 
Originator/KeyName. 
(unique designation of 
the entity that 
authenticates the 
digital signature) 
 
ANS 
1 
16 
M 
SecurityKeyName 
If “source” is Capture 
this will be the serial 
number of the 
certificate / key used. 
 
If “source” is 
ECP.PBCC this will be 
the serial number of 
the certificate / key 
used. 
 
ANS 
1 
16 
M 
 Note: The Digital Signatures of the image view are part of the image binary data files and 
not this tag.  
 
Appx 4.1.3.8 ImageViewData 
Attributes of ImageViewData 
 
Attribute Name 
Description/ Format 
Value 
(default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
ImageDataLength 
Length of the image 
Must be 
greater than 0 
N 
1 
10 
M 
ImageDataOffset 
Offset for the image 
data 
 
N 
1 
10 
M

<!-- Page 93 -->

 
CTS Clearing House Interface – Specification 
 
 
93 
Attribute Name 
Description/ Format 
Value 
(default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
FileName 
Image file name 
 
ANS 
1 
256 
M 
ImageReferenceKeyLengt
h 
The number of 
characters in the 
associated 
ImageReferenceData. 
 
N 
4 
4 
O 
ImageReferenceData 
Designator assigned 
by the presenting bank 
that uniquely identifies 
the item image 
 
ANS 
1 
256 
O 
ClippingOrigin 
Indicator if image is 
clipped. For full image 
this is “0” 
0 
N 
1 
1 
M 
 
Appx 4.1.3.9 ImageViewAnalysis 
It is mandatory for capture to perform IQA for each image view in the CXF file.   
The source attribute in the ImageViewAnalysis tag supplied by capture should have the value 
set as “Capture”e.g.Source=”Capture”. 
 
Attributes of ImageViewAnalysis 
Attribute Name 
Description/ Format Value 
(default) 
Special 
Condition 
Type 
Size 
Usag
e 
Man Max 
Source 
Indicates if IQA is 
from capture system 
or from the CHI. 
Capture | 
ECP.PBCC 
ANS 
7 
8 
M 
ImageQuality 
A ‘global’ indicator for 
the individual 
ImageQuality tests. 
‘0’ == The image was 
not tested for any of 
the the image defect 
conditions 
‘1’ == The image was 
tested and one-or-
more image defect 
conditions were 
reported 
‘2’ == The image was 
tested and no image 
defect conditions 
were reported 
0 | 1 | 2  
N 
1 
1 
M

<!-- Page 94 -->

 
CTS Clearing House Interface – Specification 
 
 
94 
Attribute Name 
Description/ Format Value 
(default) 
Special 
Condition 
Type 
Size 
Usag
e 
Man Max 
ImageUsability 
A ‘global’ indicator for 
the individual 
ImageUsability tests. 
‘0’ == The image was 
not tested for any of 
the the image 
usability conditions 
‘1’ == The image was 
tested and one-or-
more image quality 
conditions were 
reported 
‘2’ == The image was 
tested and no image 
quality conditions 
were reported 
 
N 
1 
1 
M 
ImagingBankSpecificTest 
A ‘global’ indicator for 
the individual Bank 
Specific Image tests. 
‘0’ == The image was 
not tested for any of 
the the image defect 
conditions 
‘1’ == The image was 
tested and one-or-
more image defect 
conditions were 
reported 
‘2’ == The image was 
tested and no image 
defect conditions 
were reported 
0 | 1 | 2 (0) 
N 
1 
1 
M 
PartialImage 
A specific 
ImageQuality test 
 
-1 – Test configured 
but could not be 
performed (Test 
Failure scenario) 
0 – Test not 
configured hence not 
performed 
1 – Test performed 
but failed.(Test failure 
scenario) 
2 – Test performed 
and passed. 
-1 | 0 | 1 | 2 (0) N 
1 
1 
O

<!-- Page 95 -->

 
CTS Clearing House Interface – Specification 
 
 
95 
Attribute Name 
Description/ Format Value 
(default) 
Special 
Condition 
Type 
Size 
Usag
e 
Man Max 
ExcessiveImageSkew 
A specific 
ImageQuality test. 
 
-1 – Test configured 
but could not be 
performed (Test 
Failure scenario) 
0 – Test not 
configured hence not 
performed 
1 – Test performed 
but failed.(Test failure 
scenario) 
2 – Test performed 
and passed. 
-1 | 0 | 1 | 2 (0) N 
1 
1 
O 
PiggybackImage 
A specific 
ImageQuality test. 
 
-1 – Test configured 
but could not be 
performed (Test 
Failure scenario) 
0 – Test not 
configured hence not 
performed 
1 – Test performed 
but failed.(Test failure 
scenario) 
2 – Test performed 
and passed. 
-1 | 0 | 1 | 2 (0) N 
1 
1 
O 
LightOrDark 
A specific 
ImageQuality test 
 
-1 – Test configured 
but could not be 
performed (Test 
Failure scenario) 
0 – Test not 
configured hence not 
performed 
1 – Test performed 
but failed.(Test failure 
scenario) 
2 – Test performed 
and passed. 
-1 | 0 | 1 | 2 (0) N 
1 
1 
O

<!-- Page 96 -->

 
CTS Clearing House Interface – Specification 
 
 
96 
Attribute Name 
Description/ Format Value 
(default) 
Special 
Condition 
Type 
Size 
Usag
e 
Man Max 
Streaks-Bands 
A specific 
ImageQuality test. 
 
-1 – Test configured 
but could not be 
performed (Test 
Failure scenario) 
0 – Test not 
configured hence not 
performed 
1 – Test performed 
but failed.(Test failure 
scenario) 
2 – Test performed 
and passed. 
-1 | 0 | 1 | 2 (0) N 
1 
1 
O 
BelowMinimumImageSize 
A specific 
ImageQuality test. 
 
-1 – Test configured 
but could not be 
performed (Test 
Failure scenario) 
0 – Test not 
configured hence not 
performed 
1 – Test performed 
but failed.(Test failure 
scenario) 
2 – Test performed 
and passed. 
-1 | 0 | 1 | 2 (0) N 
1 
1 
O 
ExceedsMaximumImageSize 
A specific 
ImageQuality test. 
 
-1 – Test configured 
but could not be 
performed (Test 
Failure scenario) 
0 – Test not 
configured hence not 
performed 
1 – Test performed 
but failed.(Test failure 
scenario) 
2 – Test performed 
and passed. 
-1 | 0 | 1 | 2 (0) N 
1 
1 
O 
ImageEnabledPOD 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O 
SourceDocumentBad 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O

<!-- Page 97 -->

 
CTS Clearing House Interface – Specification 
 
 
97 
Attribute Name 
Description/ Format Value 
(default) 
Special 
Condition 
Type 
Size 
Usag
e 
Man Max 
DateUsability 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O 
PayeeUsability 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O 
ConvenienceAmountUsability 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O 
LegalAmountUsability 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O 
SignatureUsability 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O 
PayorNameAndAddressUsabili
ty 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O 
MICRLineUsability 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O 
MemoLineUsability 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O 
PayorBankNameAnd 
AddressUsability 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O 
PayeeEndorsementUsability 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O 
BOFDEndorsementUsability 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O 
TransitEndorsementUsability 
A specific 
ImageUsability test 
0 | 1 | 2 (0) 
N 
1 
1 
O 
ImageAnalysisUserInformation Not required – the 
UserField will contain 
an encoded string 
 
N 
1 
1 
O 
UserField 
An encoded string 
conveying the results 
of individual Bank 
Specific Image tests. 
 
ANS 
1 
24 
O 
 
For any of the individual tests performed, there can be a resulting code of -1|0|1|2.  These codes are 
interpreted as follows: 
 
‘-1’= Test configured but could not be performed (e.g fail) 
‘0’ = The image was not tested for the conditions 
‘1’ = The image was tested and the condition is present (e.g fail) 
‘2’ = The image was tested and the condition is not present (e.g. pass) 
 
For any of the ‘global’ indicators (ImageQuality, ImageUsability, ImagingBankSpecificTest) the following 
table shows the resulting code (0|1|2) for a number of scenarios of individual tests. 
Note that this table is intentionally generic – you should extend the concept for all applicable tests for the 
‘global’ flag of interest to your application. 
 
Individual test 
#1 
Individual test 
#2 
Individual test 
#3 
Individual test 
#4 
Global Result 
0 
0 
0 
0 
0

<!-- Page 98 -->

 
CTS Clearing House Interface – Specification 
 
 
98 
2 
2 
2 
2 
2 
2 
1 
1 
1 
1 
2 
2 
2 
1 
1 
2 
2 
1 
0 
1 
1 
1 
1 
0 
1 
1 
0 
0 
0 
1 
2 
2 
2 
0 
2 
2 
0 
0 
0 
2 
 
For the IQA tests mandated by RBI/NPCI, the specific ImageQuality tests cannot convey all the tests 
being performed in the solution.  Therefore the ImagingBankSpecificTest is the global indicator, and the 
UserField conveys the full set of test results.  The UserField is encoded with a very simple structure as 
follows: 
“mmm:ABCDEFGHIJLKMNOPQ where 
- 
‘mmm’ is a marker to indicate how the remaining chars A…Q are interpreted 
- 
‘:’ is fixed to separate the marker from the results 
- 
‘A’…’Q’ take the values ‘0’, ‘1’, ‘2’ for their individual tests 
For example, the UserField might have the following value: 
“BS1:20000222222222202” where 
‘BS1:’ is the marker string and separator for BankSpecific testset #1 
A: is the Partial Image test (-1|0|1|2) 
B: is the Excessive Image Skew test (-1|0|1|2) 
C: is the Piggyback Image test (-1|0|1|2) 
D: is the Streaks and|or Banks test (-1|0|1|2) 
E: is the Bent Corners test (0|1|2) 
F: is the Below Minimum Image Size test (-1|0|1|2) 
G: is the Exceeds Maximum Image Size test (-1|0|1|2) 
H: is the Binary Too Light test (-1|0|1|2) 
I: is the Binary Too Dark test (-1|0|1|2) 
J: is the Image Height Mismatch test (0|1|2) 
K: is the Image Length Mismatch test (0|1|2) 
L: is the Below Minimum Image Length test (0|1|2) 
M: is the Exceeds Maximum Image Length test (0|1|2) 
N: is the Below Minimum Image Height test (0|1|2) 
O: is the Exceeds Maximum Image Height test (0|1|2) 
P: is the Torn Corner test (0|1|2) 
Q: is the ImageFormat test (note: this is a bank specific test that the image format must meet 
certain specifications as defined by the bank – e.g. JFIF 100dpi) (0|1|2)

<!-- Page 99 -->

 
CTS Clearing House Interface – Specification 
 
 
99 
Appx 4.2 CAPTURE IMAGE BINARY FILE (CIBF) 
 
Appx 4.2.1 File Name Convention 
A1 
Capture image binary files shall follow the same naming convention as its corresponding 
Capture eXchange file , except that the prefix “CXF_” shall be replaced with the “CIBF_” 
followed by rest of the text and then appended by unique modifier. The unique modifier 
can be text indicating anything (e.g. sequence number), provided this makes the 
filename unique for the given business day. The extension shall be “.img” 
 
 CIBF_ nnnnnnnnn_ddmmyyyy_hhmmss_xx_bbbbbbbbbb _nn.img  
Where: 
 
CIBF  
Capture Image Binary File 
 
nnnnnnnnn       from capture exchange file (CXF) 
             ddmmyyyy       from capture exchange file (CXF) 
             hhmmss            from capture exchange file (CXF) 
             xx                     from capture exchange file (CXF) 
             bbbbbbbbbb     from capture exchange file (CXF) 
             nn                       Unique modifier  (e.g. “01” then “02” etc)  
 
.img 
 
Is a mandatory file type suffix 
Appx 4.2.2 File Structure 
The binary image file contains concatenated single page images.   The required image 
parameters and format is covered in Appendix EE: Image Detail Specification. 
For RBI/NPCI, each item will have three image views, two B/W CCITT G4 TIFF images for front 
and back and a single Grayscale image compressed in JPEG for front. Each Image is 
referenced by its offset in the corresponding XML file. The order of items in the image binary file 
(CIBF) should match the order in the capture file (CXF). It is capture’s responsibility to match the 
information of image views in capture file (CXF) to the contents in capture image binary file 
(CIBF) 
The layout of the binary image file is given below.

<!-- Page 100 -->

 
CTS Clearing House Interface – Specification 
 
 
100 
The digital signature is stored as a part of the image file. 
The image file layout with digital signatures: 
TIFF Image Item 1
 (Front, B/W)
TIFF Image Item 1
 (Back, B/W)
JPEG Image Item 1
 (Front, Gray)
TIFF Image Item 2
 (Front, B/W)
:
JPEG Image Item 2
 (Front, Gray)
TIFF Image Item 2
 (Back, B/W)
:
DS Offset Item1 front
DS Offset Item1 back
DS Offset Item1 front
DS Offset Item2 front
DS Offset Item2 back
DS Offset Item2 front
DS Offset Item”n” front
Dig-Sign for Item1 Front
Dig-Sign for Item1 Back
Dig-Sign for Item2 Front:
Dig-Sign for Item2 Back
Dig-Sign for Item2 Front
Dig-Sign for Item1 Front
:
:
Offset Item1 front
Offset Item1 front
Offset Item1 front
Offset Item1 front
Offset Item1 back
Offset Item1 front
Offset Item1 front
Offset Item1 front

<!-- Page 101 -->

 
CTS Clearing House Interface – Specification 
 
 
101 
Appx 4.3 POSTING EXCHANGE FILE (PXF) 
The Posting eXchange files are created by the CHI as inward presentment to the bank. The 
posting files can be generated either as: 
1) Master Posting eXchange File that includes items for all banks associated with that CHI 
2) Bank Posting eXchange File containing only the items presented to the specific bank  
3) BRanch Posting eXchange File containing only the items presented to the specific branches. 
Within branches, files can be generated per transcode. In case the CHI is configured city wise, 
the branch folder (in which the branch posting file is generated) will be located in the respective 
city folder within the bank folder. 
4) All Other Posting eXchange File containing all other items.  
It is mandatory that the capture and the Presenting CHI will perform IQA on each image view, 
and will digitally sign the MICR and each image view.  This means that there will be multiple 
MICRDS, IMAGEDS and ImageViewAnalysis elements for each item.  Therefore the items in 
posting files will: 
 always have digital signatures for MICR data and each image view from capture. 
 always have digital signatures for MICR data and each image view from Presenting CHI. 
 always have IQA for each image view from capture. 
 always have IQA for each image view from Presenting CHI.   
Appx 4.3.1 File Name Convention 
A1 
The Posting eXchange File name shall  use the following naming convention: 
 
wPXF_nnnnnnnnn_<session_nos>_<session_date>_ddmmyyyy_hhmmss_xxxxxxx
xxx.XML 
Where: 
 
w 
 
Type 
 
 
–M - Master (all banks using CHI) 
 
 
–B - Bank (one bank) 
 
 
 
–BR - Branch of a bank 
 
 
 
–O - Any Other items 
 
 
PXF   
Posting eXchange File 
 
nnnnnnnnn 
CHI / Payor Bank / Payor Branch Routing Number (depending upon value of 
w) 
            <session_nos> The clearing session number 
            <session_date> The clearing session date 
 
ddmmyyyy 
File Creation Date 
 
hhmmss 
File Creation Time 
 
xxxxxxxxxx 
File ID Modifier  
 
.XML  
Is a mandatory file type suffix 
A2 
The value for the File Creation Date, File Creation Time and File ID Modifier in the file 
name shall be the same as in the File Header.

<!-- Page 102 -->

 
CTS Clearing House Interface – Specification 
 
 
102 
B3 
The All Other Posting eXchange File (AOPXF) shall be used for items that cannot be 
assigned to a Branch Posting file. These items may have an invalid or non-configured 
drawee bank sort code. 
AOPXF will not be needed under RBI/NPCIs processing rules. 
A4 
For the Payor Bank Routing Number, PXF file will contain: 
 
CHI routing number (of the receiving CHI) for Master Posting eXchange File 
 
Receiving Bank routing number for Bank and All Other Posting eXchange File. 
 
 
Payor Bank routing number for Branch Posting File. 
 
Appx 4.3.2 Master/Bank Posting eXchange File Structure 
ImageViewAnalysis
ImageViewData
AddendA
FileSummary
FileHeader
Item
ImageViewAnalysis
ImageViewDetail
Master/Bank Posting eXchange File Structure
Mandatory 
Element
Multiple 
Elements
Optional 
Element
Multiple 
Optional 
Elements
MICRDS
ImageDS

<!-- Page 103 -->

 
CTS Clearing House Interface – Specification 
 
 
103 
C1 
The Master and Bank Posting eXchange file structure shall be: 
<FileHeader …   > 
<Item …   > 
<AddendA …       /> 
                                         <MICRDS Source=”Capture” …    /> 
                                         <MICRDS Source=”ECP.PBCC” …    /> 
                                         <ImageViewDetail …   > 
     <ImageViewData …   /> 
                                                                    <ImageDS Source=”Capture” … /> 
                                                                    <ImageDS Source=”ECP.PBCC” … /> 
                                                                   <ImageViewAnalysis Source=”Capture” …   /> 
                                                                   <ImageViewAnalysis Source=”ECP.PBCC” …   
/> 
                                         </ImageViewDetail> 
                                             : 
</item> 
<FileSummary …   /> 
            </FileHeader> 
B2 
Elements “FileHeader”, “Item”, “AddendA”, “ImageViewDetail”, “ImageViewData”, 
“FileSummary”, “MICRDS”, “ImageDS” and “ImageViewAnalysis” are mandatory

<!-- Page 104 -->

 
CTS Clearing House Interface – Specification 
 
 
104 
Appx 4.3.3 Branch/Trancode/AO Posting File Structure  
ImageViewData
AddendA
FileSummary
FileHeader
Item
ImageViewAnalysis
ImageViewDetail
Mandatory 
Element
Multiple 
Elements
Optional 
Element
MICRDS
ImageDS
Branch/Tr/AO Posting File Structure

<!-- Page 105 -->

 
CTS Clearing House Interface – Specification 
 
 
105 
C1 
The Branch/Trancode/AO Posting  eXchange file structure shall be: 
<FileHeader …   > 
<Item …   > 
<AddendA …       /> 
                                         <MICRDS Source=”Capture” …    /> 
                                         <MICRDS Source=”ECP.PBCC” …    /> 
                                         <ImageViewDetail …   > 
         <ImageViewData …   /> 
                                                                       <ImageDS Source=”Capture” … /> 
                                                                       <ImageDS Source=”ECP.PBCC” … /> 
                                                                       <ImageViewAnalysis Source=”Capture” …   
/> 
                                                                       <ImageViewAnalysis Source=”ECP.PBCC” 
…   /> 
                                         </ImageViewDetail> 
                                                : 
</item> 
<FileSummary …   /> 
</FileHeader> 
 
 
C2 
Elements “FileHeader”, “Item”, “AddendA”, “ImageViewDetail”, “ImageViewData”, 
“FileSummary”, “MICRDS”, “ImageDS” and “ImageViewAnalysis” are mandatory 
 
Appx 4.3.4 Elements and Attributes 
Appx 4.3.4.1 FileHeader 
 
Attributes of FileHeader 
 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
Xmlns 
Schema definition 
 
For PXF, must 
be 
urn:schemas-
ncr-
com:ECPIX:PX
F:FileStructure:
010001 
 
ANS 
 
256 
M

<!-- Page 106 -->

 
CTS Clearing House Interface – Specification 
 
 
106 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
VersionNumber 
Version of this 
Interface definition 
xxyyyy 
xx = country 
(01=RBI/NPCI) 
yyyy = version 
(0001) 
NS 
4 
6 
M 
TestFileIndicator 
 
P --> Production 
Must be   P 
A 
1 
1 
M 
CreationDate 
File Creation Date 
  
Shall be same as in 
the filename 
Date should be 
in DDMMYYYY 
format 
DATE 
8 
8 
M 
CreationTime 
File Creation Time 
  
Shall be same as in 
the filename 
Time should be 
HH24MISS 
format 
TIME 
6 
6 
M 
FileID 
File ID  
 
A number that 
uniquely identifies 
the items in this 
file. Shall be same 
as in the filename. 
 
AN 
1 
10 
M 
SessionNumber 
Session number to 
which the items 
were available. 
 
Shall be same as in 
the filename. 
 
N 
1 
2 
M 
SessionDate 
Date of the session 
to which the items 
were available.  
 
Shall be same as in 
the filename 
Date should be 
in DDMMYYYY 
format 
DATE 
8 
8 
M 
SettlementDate 
 
Value Date – Date 
on which the Items 
shall be posted in 
books of account. 
Date should be 
in DDMMYYYY 
format 
DATE 
8 
8 
M 
SessionExtensionHrs 
Default Extension 
Hours Granted at 
CH. 
0 
N 
1 
2 
M 
 
NOTE: Drawee Module shall use SessionDate, CLOSE_RECEIVING_TIME of the Session and 
SessionExtensionHrs for the session, to determine extension and return lengths for items in the 
session. 
 
Appx 4.3.4.1.1 
FileSummary 
 
Same as in section 4.1.3.2

<!-- Page 107 -->

 
CTS Clearing House Interface – Specification 
 
 
107 
 
Appx 4.3.4.1.2 
CashLetterHeader 
Appx 4.3.4.1.3 
CashLetterSummary 
Appx 4.3.4.1.4 
BundleHeader 
Appx 4.3.4.1.5 
BundleSummary 
Appx 4.3.4.1.6 
Item 
NOTE: These fields come from the capture data.  All fields marked * represent the UDK for each 
item. 
 
Attribute Name 
Description/ 
Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
ItemSeqNo* 
This is a unique 
identifier for the 
bank for a 
“PresentmentDate” 
 
Same as in 
CXF file Appx 
4.1.3.3 
NS 
14 
14 
M 
PayorBankRoutNo 
Drawee Bank 
Routing number 
Must be greater 
than 0 
NS 
9 
9 
M 
Amount 
Check amount 
Must be greater 
than 0 
N 
18 
18 
M 
AccountNo 
Drawee account 
number 
 
NS 
1 
25 
O 
SerialNo 
Check number 
Must be greater 
than 0 
NS 
6 
6 
M 
TransCode 
Transaction code 
 
NS 
1 
3 
M 
PresentingBankRoutNo* 
Routing number of 
the presenting 
bank 
 
Must be greater 
than 0 
NS 
9 
9 
M 
PresentmentDate* 
Date of capture of 
checks  
 
Date should be 
in DDMMYYYY 
format 
DATE 
8 
8 
M 
CycleNo* 
Capture cycle 
number 
 
Must be greater 
than 0 
NS 
2 
2 
M 
NumOfImageViews 
Number of image 
views for an item 
(3) 
N 
1 
1 
M 
ClearingType 
See Appendix CC 
for details. 
Must be greater 
than 0 
NS 
2 
2 
M 
DocType 
From Capture file 
 
A 
1 
1 
M 
MICRRepairFlags 
From Capture file 
 
NS 
6 
6 
M 
SpecialHandling 
From capture file 
0 = Normal 
(0) 
 
N 
1 
2 
O

<!-- Page 108 -->

 
CTS Clearing House Interface – Specification 
 
 
108 
Attribute Name 
Description/ 
Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
TruncatingRTNo 
RT number of the 
truncating bank 
 
NS 
9 
9 
O 
UserField 
From Capture file 
 
ANS 
1 
25 
O 
IQAIgnoreInd 
From Capture file.   0 – Ignore this 
field  
1 – Accept the 
image 
irrespective of 
its quality. 
N 
1 
1 
O 
CurrencyInd 
From Capture file 
 
AN 
3 
3 
O 
ItemStatus 
CH will set this 
field.  
Used to indicate to 
the drawee bank 
the status of the 
item being 
presented. 
For list of status 
codes see 
section 
4.3.4.7.1  
(0) 
N 
1 
2 
M 
 
Appx 4.3.4.1.6.1 
ItemStatus 
ItemStatus Codes 
Status Code 
Description 
0 
Cleared by CH  
8 
Failed Digital Signature validation.  The failure could have resulted in any 
of the MICRDS or the individual IMAGEDS’s. 
9 
Detected as Duplicate MICR Fields (SerialNo, TransCode, 
PayorBankRoutNo) 
 
 
Appx 4.3.4.1.7 
MICRDS 
Attributes of MICRDS are same as in section 4.1.3.4 
Appx 4.3.4.1.8 
AddendA 
Same as in section 4.1.3.5 
Appx 4.3.4.1.9 
ImageViewDetail 
Same as in section 4.1.3.6 
Appx 4.3.4.1.10 
ImageDS 
Attributes of ImageDS are same as in section 4.1.3.7 
Appx 4.3.4.1.11 
ImageViewData

<!-- Page 109 -->

 
CTS Clearing House Interface – Specification 
 
 
109 
Same as in section 4.1.3.8 
Appx 4.3.4.1.12 
ImageViewAnalysis 
Attributes of ImageViewAnalysis are same as in section 4.1.3.9

<!-- Page 110 -->

 
CTS Clearing House Interface – Specification 
 
 
110 
 
Appx 4.3.5 POSTING IMAGE BINARY FILE (PIBF) 
 
Appx 4.3.5.1 File Name Convention 
A1 
Posting binary image files shall follow the same naming convention as the posting 
exchange file except that the prefix “wPXF” shall be replaced with the “wPIBF” followed by 
rest of the text and then appended by unique modifier. The unique modifier can be text 
indicating view, data format or just a sequence number, provided this makes the 
filename unique for the given business day. The extension shall be “.img” 
 
 wPIBF_<filestring>_nn.img  
Where: 
 
wPIBF  
Posting Image Binary File 
 
<filestring>       This is acquired from the master posting file    
             nn                       Unique modifier  
                                       (e.g. if one bundle has 2 associated image files then nn is “01” and “02”)      
 
.img 
 
Is a mandatory file type suffix 
 
 
Appx 4.3.5.2 File Structure 
 
The image file layout will look like: 
TIFF Image Item 1
 (Front, B/W)
TIFF Image Item 1
 (Back, B/W)
Offset Item1 front
Dig-Sign for Item1 Front 
(Capture and ECP.PBCC)
:
TIFF Image Item ‘n’
 (Front, B/W)
JFIF Image Item 1
 (Front, Gray)
:
DS Offsets Item1 front
Offset Item1 back
Offset Item1 front
Offset Item”n” front
Dig-Sign for Item1 Back 
(Capture and ECP.PBCC)
DS Offsets Item1 back
Dig-Sign for Item1 Front 
(Capture and ECP.PBCC)
DS Offsets Item1 front
Dig-Sign for Item1 Front 
(Capture and ECP.PBCC)
DS Offsets Item ’n’ front
 
 
The order of items in the image binary file (PIBF) will match the order in the posting file (wPXF).

<!-- Page 111 -->

 
CTS Clearing House Interface – Specification 
 
 
111 
The order and information of image views of an item in PXF and PIBF will be same as received from 
capture file.

<!-- Page 112 -->

 
CTS Clearing House Interface – Specification 
 
 
112 
 
Appx 4.3.6 RETURN REQUEST FILE (RRF) 
The Return Request files are provided to the CHI system by the Bank's Return Processing 
system. The Return Request file consists of a list of all items that are to be returned unpaid by 
the receiving bank, with a return reason for each item. The items in the return request file do not 
need to be sorted by Presenting Bank or by clearing type.  
 
The contents of an RRF file does not have to correspond to any one PXF file.  
 
Appx 4.3.6.1 File Name Convention 
A1 
The Return Request file name shall use the following naming convention: 
RRF_ nnnnnnnnn _ddmmyyyy_hhmmss_xxxxxxxxxx.XML 
 
 
Where: 
 
RRF 
 
Return Request File 
 
nnnnnnnnn 
CHI / Payor Bank / Payor Branch Routing Number 
 
ddmmyyyy  
File Creation Date   
 
hhmmss  
File Creation Time   
            xxxxxxxxxx    FileID 
             .XML                is a mandatory file type suffix 
 
Appx 4.3.6.2 File Structure 
FileSummary
FileHeader
Item
Return Request File Structure
Mandatory 
Element
Multiple 
Elements
AddendA
MICRDS
Optional 
Element

<!-- Page 113 -->

 
CTS Clearing House Interface – Specification 
 
 
113 
C1 
The Return Request file structure shall be: 
<FileHeader …   > 
<Item …   > 
<AddendA …       /> 
                                         <MICRDS …    /> 
</item> 
<FileSummary …   /> 
</FileHeader> 
 
 
C2 
Elements “FileHeader”, “Item”, “AddendA”, “FileSummary” are mandatory 
 
Note: Bank’s system can digitally sign the MICR data in return request file. If so, the MICRDS 
will be passed thru CH to the presenting bank. CHI will NOT digitally sign MICR data for returns.   
Appx 4.3.6.3 Elements and Attributes 
Appx 4.3.6.3.1 
FileHeader 
 
Attributes of FileHeader are same as in section 4.1.3.1 
Appx 4.3.6.3.2 
FileSummary 
 
Same as in section 4.1.3.2 
Appx 4.3.6.3.3 
Item 
NOTE: All fields marked * must be the exact same as were given in the PXF.  These fields are 
used to find the corresponding item and apply the status. 
 
 
Attribute Name 
Description/ 
Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
ItemSeqNo* 
This is a unique 
identifier for the 
bank for a 
“PresentmentDate” 
 
Same as in 
posting file 
 
NS 
14 
14 
M 
PayorBankRoutNo 
Drawee Bank 
Routing number 
Same as in 
posting file 
NS 
9 
9 
M 
Amount 
Check amount 
Same as in 
posting file 
N 
1 
18 
M 
AccountNo 
Drawee account 
number 
Same as in 
posting file 
NS 
1 
25 
O 
SerialNo 
Check number 
Same as in 
posting file 
NS 
6 
6 
M

<!-- Page 114 -->

 
CTS Clearing House Interface – Specification 
 
 
114 
Attribute Name 
Description/ 
Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
TransCode 
Transaction code 
Same as in 
posting file 
NS 
1 
3 
M 
PresentingBankRoutNo* 
Routing number of 
the presenting 
bank 
 
Same as in 
posting file 
NS 
9 
9 
M 
PresentmentDate* 
Date of capture of 
checks 
 
Same as in 
posting file 
DATE 
8 
8 
M 
CycleNo* 
Capture cycle 
number  
 
Same as in 
posting file 
NS 
1 
2 
M 
ClearingType 
See Appendix CC 
 
NS 
2 
2 
M 
ReturnReason 
For return files 
A code that 
indicates the 
reason for non-
payment. Codes 
and reasons should 
be established as 
part of the clearing 
rules.  
For list of reason 
codes see section 
4.5.3.3.1 
 
NS 
2 
3 
M 
ReturnReasonComment 
Free format, for 
use by drawee 
 
ANS 
1 
25 
O 
 
Appx 4.3.6.3.3.1 
Return Reason 
 
The following are a core set of Return Reason codes. Additional codes (if necessary) will be added by 
RBI/NPCI in Appendix DD and communicated to the banks. 
 
Code   
Reason for Return 
No. 
Funds 
Funds insufficient 
01 
Exceeds arrangement 
02 
Effects not cleared, present again. 
 
Reference to Drawer 
03 
Refer to drawer

<!-- Page 115 -->

 
CTS Clearing House Interface – Specification 
 
 
115 
(10-19)      Signature 
10 
Drawer’s signature incomplete 
11 
Drawer’s signature illegible 
12 
Drawer’s signature differs 
13 
Drawer’s signature required 
14 
Drawer’s signature not as per mandate 
15 
Drawer’s signature to operate account not received 
16 
Drawer’s authority to operate account not received 
17 
Alteration require drawer’s authentication 
 
(20-29) 
Stop Payment 
20 
Payment stopped by drawer 
21 
Payment stopped by attachment order 
22 
Payment stopped by court order 
23 
Withdrawal stopped owing to death of account holder 
24 
Withdrawal stopped owing to lunacy of account holder 
25 
Withdrawal stopped owing to insolvency of account holder 
 
(30-49) 
Instrument 
30 
Instrument post dated 
31 
Instrument out dated / stale 
32 
Instrument undated / without proper date 
33 
Instrument mutilated; requires Bank’s guarantee 
Cheque irregularly drawn / amount in words and figures differ 
Clearing House stamp/ date required 
34 
Wrongly delivered/ Not drawn on us 
35 
Present in proper zone 
36 
Instrument contains extraneous matter 
37 
Image not clear, present again with paper 
38 
Present with document 
 
(50-59) 
Account 
50 
Account closed 
51 
Account transferred to another branch 
52 
No such account 
53 
Title of account required 
54 
Title of account wrong/ incomplete 
55 
Account blocked (situation covered in 21-25) 
 
(60-69) 
Crossing/ Endorsement 
60 
Crossed to two banks 
61 
Crossing stamp not cancelled 
62 
Clearing stamp not cancelled 
63 
Instrument specially crossed to another bank 
64 
Amount in protective crossing incorrect 
65 
Amount in protective crossing required/ illegible 
66 
Payee’s endorsement required 
67 
Payee’s endorsement irregular / requires collecting bank’s confirmation 
68 
Endorsement by mark/ thumb impression requires attestation by Magistrate with seal. 
69 
Advice not received 
 
(70-79) 
RBI/ Government 
70 
Amount / Name differs on advice 
71 
Drawee bank’s funds with sponsor bank insufficient 
72 
Payee’s separate discharge to bank required

<!-- Page 116 -->

 
CTS Clearing House Interface – Specification 
 
 
116 
73 
Not payable till 1st proximo 
74 
Pay order/ cheque requires counter signature 
 
(80-89) 
Miscellaneous 
Bank’s certificate ambiguous / incomplete/ required 
80 
Draft lost by issuing office / confirmation required from issuing office 
81 
Bank / Branch Blocked 
 
 
Appx 4.3.6.3.4 
MICRDS 
In the event that the drawee bank choses to sign MICR data in the RRF file, attributes of 
MICRDS are same as in section 4.1.3.4.  The drawee bank shall set source = “Drawee”. 
 
Appx 4.3.6.3.5 
AddendA 
This should be same as in the posting file. 
Same as in section 4.1.3.5

<!-- Page 117 -->

 
CTS Clearing House Interface – Specification 
 
 
117 
 
Appx 4.3.7 RETURN FILE (RF) 
The Return Files are created by the CHI as inward returns to the bank. The return files can be 
generated either as: 
1) Master return file that includes items from all banks associated with that CHI 
2) Bank return files containing only the data for items presented by the specific banks (as 
defined by CHI option) 
3) Branch return files containing only the data for items presented by the specific branches (as 
defined by CHI option).  
4) All Other Return File containing all other items.  
 
Appx 4.3.7.1 File Name Convention 
A1 
      The Return File name shall use the following naming convention: 
  
wRF_nnnnnnnnn_ddmmyyyy_hhmmss_xxxxxxxxxx.XML 
 
Where: 
 
w 
 
Type 
 
– 
M - Master (all banks using CHI) 
 
– 
B - Bank (one bank) 
 
 
–BR - Branch of a bank 
 
 
–AO - Any Other items 
 
 
RF  
 
Return File 
 
nnnnnnnnnn CHI / Bank / Branch Routing Number (depending upon value of w) 
 
 
ddmmyyyy 
File Creation Date 
 
hhmmss 
File Creation Time 
 
xxxxxxxxxx 
File ID Modifier  
 
.XML  
Mandatory file type suffix 
A2 
The value for the File Creation Date, File Creation Time and File ID Modifier in the file 
name shall be the same as the in the File Header. 
A3 
For the  Routing Number, RF file will contain use: 
 
CHI routing number (of the receiving CHI) for Master Return File 
 
Bank routing number for Bank Return File.  
 
Branch routing number for Branch Return File.

<!-- Page 118 -->

 
CTS Clearing House Interface – Specification 
 
 
118 
Appx 4.3.7.2 Master and Bank Return File Structure 
AddendA
FileSummary
FileHeader
Item
Master/Bank Return File Structure
MICRDS
Mandatory 
Element
Multiple 
Elements
Optional 
Element
 
 
 
A1 
The Master and Bank Return file structure shall be: 
<FileHeader …   > 
<Item …   > 
<AddendA …       /> 
                                         <MICRDS …    /> 
                            </item> 
<FileSummary …   /> 
            </FileHeader> 
B2 
Elements “FileHeader”, “Item”, “AddendA” and “FileSummary” tags are mandatory

<!-- Page 119 -->

 
CTS Clearing House Interface – Specification 
 
 
119 
Appx 4.3.7.3 Branch and AO Return File Structure 
FileSummary
FileHeader
Item
Branch/AO Return File Structure
AddendA
MICRDS
Mandatory 
Element
Multiple 
Elements
Optional 
Element
 
 
 
 
 
A1 
The Branch and All Other Return file structure shall be: 
<FileHeader …   > 
    <Item …   > 
<AddendA …       /> 
                                         <MICRDS …    /> 
             </item> 
<FileSummary …   /> 
            </FileHeader> 
C2 
Elements “FileHeader”, “Item”, “AddendA” and “FileSummary” tags are mandatory 
 
Appx 4.3.7.4 Elements and Attributes 
Appx 4.3.7.4.1 
FileHeader 
Xmlns=”urn:schemas-ncr-com:ECPIX:RF:FileStructure:010001” 
 
Other attributes of FileHeader are same as in section 4.1.3.1 
 
Appx 4.3.7.4.2 FileSummary 
Same as in section 4.1.3.2

<!-- Page 120 -->

 
CTS Clearing House Interface – Specification 
 
 
120 
 
Appx 4.3.7.4.3 
CashLetterHeader 
Appx 4.3.7.4.4 
CashLetterSummary 
Appx 4.3.7.4.5 
BundleHeader 
Appx 4.3.7.4.6 
BundleSummary 
Appx 4.3.7.4.7 
AddendA 
Same as in section 4.1.3.5 
Appx 4.3.7.4.8 
MICRDS 
If the drawee bank has signed the MICR data, attributes of MICRDS are same as in section 
4.1.3.4. 
Appx 4.3.7.4.9 
Item 
Same as in section 4.5.3.3

<!-- Page 121 -->

 
CTS Clearing House Interface – Specification 
 
 
121 
 
Appx 4.3.8 EXTENSION REQUEST FILE (ERF) 
Drawee CHI can request for extension for items drawn on it. The extension request will include 
the extension period required and the reason for extension. This file can also be used to make 
paper requests if images are bad or not sufficient for processing. 
The extension required could be a result of : 
1) bank/branch is on holiday 
2) bad image need paper, (to be handled as per established clearing house guidelines) 
The extension request has to be made within “x” hrs (configurable as per clearing rules, typically 
24 hrs) of the inward presentment.  If paper is requested, then the presenting bank is expected 
to send the paper item within “x” hrs (configurable as per clearing rules, typically 24 hrs) of the 
request received. The extension request will extend the return cycle period based on the 
clearing rules and the holiday calendar.  
The extension request file is in XML format and contains list of items for which extension is 
desired. The extension request file does not affect the settlement.  
Extension request files will be approved by CH based on the RBI/NPCI set rules.  
 
Appx 4.3.8.1 File Name Convention 
 
A1 
The Extension Request File shall use the following naming convention: 
ERF_nnnnnnnnnn_ddmmyyyy_hhmmss_xxxxxxxxxx.XML 
 
 
Where: 
              ERF  
Extension Request File 
              nnnnnnnnnn CHI / Payor Bank / Payor Branch Routing Number  
 
 ddmmyyyy  
File Creation Date   
             hhmmss  
File Creation Time   
 
             xxxxxxxxxx   FileID 
             .XML             Is a mandatory file type suffix

<!-- Page 122 -->

 
CTS Clearing House Interface – Specification 
 
 
122 
Appx 4.3.8.2 File Structure 
FileSummary
FileHeader
Item
Extension Request File Structure
Mandatory 
Element
Multiple 
Elements
 
 
C1 
The Extension Request file structure shall be: 
 
<FileHeader …   > 
      <Item …   /> 
      <Item …   /> 
<FileSummary … /> 
</FileHeader> 
 
C2 
Elements “FileHeader”, “Item” and “FileSummary” tags are mandatory 
Appx 4.3.8.3 Elements and Attributes 
Appx 4.3.8.3.1 
FileHeader 
Xmlns=”urn:schemas-ncr-com:ECPIX:ERF:FileStructure:010002” 
 
Other attributes of FileHeader are same as in section 4.1.3.1 
Appx 4.3.8.3.2 
FileSummary 
 
Same as in section 4.1.3.2 
Appx 4.3.8.3.3 
Item 
NOTE: All fields marked * must be the exact same as were given in the PXF.  These fields are 
used to find the corresponding item and apply the status. 
 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max

<!-- Page 123 -->

 
CTS Clearing House Interface – Specification 
 
 
123 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
ItemSeqNo* 
This is a unique 
identifier for the 
bank for a 
“PresentmentDate” 
 
Same as in 
posting file 
NS 
14 
14 
M 
PayorBankRoutNo 
Drawee Bank 
Routing number 
 
NS 
9 
9 
M 
Amount 
Check amount 
 
N 
1 
18 
M 
AccountNo 
Drawee account 
number 
 
NS 
1 
25 
O 
SerialNo 
Check number 
 
NS 
6 
6 
M 
TransCode 
Transaction code 
 
NS 
1 
3 
M 
PresentingBankRoutNo* 
Routing number of 
the presenting 
bank 
 
Same as in 
posting file 
NS 
9 
9 
M 
PresentmentDate* 
Date of capture of 
checks  
 
Same as in 
posting file 
DATE 
8 
8 
M 
CycleNo* 
Capture cycle 
number. 
 
Same as in 
posting file 
NS 
1 
2 
M 
ExtensionPeriod 
Extension required 
in hrs 
Must be greater 
than 0 
N 
1 
3 
M 
ExtensionReason 
The reason for 
requesting 
extension. See 
section 4.7.3.3.1 
 
NS 
2 
2 
M 
                                   
Appx 4.3.8.3.3.1 
Extension Reason 
Extension Reason Codes 
Extension Reason 
Description 
01 
Funds insufficient 
02 
Exceeds arrangement 
03 
Effects not cleared, present again 
04 
Bad image, paper requested 
05 
Item a suspect, paper is requested 
06 
Branch not in operation 
07 
Extensions Orginated from CH due Blockage

<!-- Page 124 -->

 
CTS Clearing House Interface – Specification 
 
 
124 
 
Appx 4.3.9 EXTENSION FILE (EF) 
Extension file informs the bank/branch of items that have been allowed extensions for the return 
period, so the bank can use the information to hold credit on those customer accounts. Drawee 
Extension file informs the Drawee bank module of items that have been extended at the CH on 
behalf of the CHI.  The file includes the extension period and the extension reason. Extension 
files can be generated either as: 
1) Master Extension File that includes items for all banks associated with the CHI 
 2) Bank Extension File containing only the items associated with the specific bank  
3) BRanch Extension File containing only the items associated with the specific branch. 
Appx 4.3.9.1 File Name Convention 
 
C1 
The Extension File or Drawee Extension File shall use the following naming convention: 
 
wEF_nnnnnnnnn_ddmmyyyy_hhmmss_xxxxxxxxxx.XML (for Presenting module) 
 
wDREF_nnnnnnnnn_ddmmyyyy_hhmmss_xxxxxxxxxx.XML (for Drawee module) 
 
 
Where: 
 
 
w 
 
Type 
 
– 
M - Master (all banks using CHI) 
 
- 
B - Bank (one bank) 
 
- 
BR - Branch of a bank 
 
– 
AO - Any Other items 
 
 
EF or DREF 
Extension File or Drawee Extension File 
 
nnnnnnnnn 
CHI / Bank / Branch Routing Number (depending upon value of w) 
 
ddmmyyyy  
File Creation Date   
 
hhmmss  
File Creation Time   
 
xxxxxxxxxx 
File ID 
      .XML                 Is a mandatory file suffix 
 
 
A2 
The value for the File Creation Date, File Creation Time and File ID in the file name shall 
be the same as the in the File Header. 
C3 
For the Routing Number, EF or DREF file will contain: 
 
CHI routing number (of the receiving CHI) for Master Extension File 
 
Bank routing number for Bank Extension File. 
Branch routing number for Branch Extension File.

<!-- Page 125 -->

 
CTS Clearing House Interface – Specification 
 
 
125 
Appx 4.3.9.2 File Structure 
FileSummary
FileHeader
Item
Extension File Structure
Mandatory 
Element
Multiple 
Elements
 
 
A1 
The Extension file structure shall be: 
 
<FileHeader …   > 
      <Item …   /> 
      <Item …   /> 
<FileSummary … /> 
            </FileHeader> 
 
B2 
Elements “FileHeader”, “Item” and “FileSummary” tags are mandatory 
Appx 4.3.9.3 Elements and Attributes 
Appx 4.3.9.3.1 
FileHeader 
Xmlns=”urn:schemas-ncr-com:ECPIX:EF:FileStructure:010001” 
 
Other attributes of FileHeader are same as in section 4.1.3.1 
Appx 4.3.9.3.2 
FileSummary 
 
Same as in section 4.1.3.2 
Appx 4.3.9.3.3 
Item 
NOTE: All fields marked * must be the exact same as were given in the PXF.  These fields are 
used to find the corresponding item and apply the status. 
 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max

<!-- Page 126 -->

 
CTS Clearing House Interface – Specification 
 
 
126 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
ItemSeqNo* 
This is a unique 
identifier for the 
bank for a 
“PresentmentDate”  
Same as in 
extension 
request file 
NS 
14 
14 
M 
PayorBankRoutNo 
Drawee Bank 
Routing number 
 
NS 
9 
9 
M 
Amount 
Check amount 
 
N 
1 
18 
M 
AccountNo 
Drawee account 
number 
 
NS 
1 
25 
O 
SerialNo 
Check number 
 
NS 
6 
6 
M 
TransCode 
Transaction code 
 
NS 
1 
3 
M 
PresentingBankRoutNo* 
Routing number of 
the presenting 
bank  
Same as in 
extension 
request file 
NS 
9 
9 
M 
PresentmentDate* 
Date of capture of 
checks  
 
Same as in 
extension 
request file 
DATE 
8 
8 
M 
CycleNo* 
Capture cycle 
number. 
 
Same as in 
extension 
request file  
NS 
1 
2 
M 
ExtensionPeriod 
Extension period 
requested in hours 
 
N 
1 
3 
M 
ExtensionReasonCode 
The reason for 
requesting 
extension. See 
section 4.7.3.3.1  
 
NS 
2 
2 
M 
                                   
Appx 4.3.10 
RESPONSE FILE (.RES) 
When CHI detects invalid files, invalid MICR data, any syntax error at item level or bad images, 
it creates Response file for the received file.   
 If the file is invalid then whole file is rejected.  
 If items are invalid then only those items are rejected.  
 A Response file with no items included and FileStatus set to indicate success is a 
positive acknowledgement that the file is successfully processed by CHI.  
The Response file is in XML format and consists of a list of all items that are returned by the CHI 
with reject reason. These items are not included in the clearing or settlement. Response files 
are generated for capture file (CXF), Return Request File (RRF), and Extension Request File 
(ERF). CHI can send multiple response files for a single CXF, RRF, or ERF file.

<!-- Page 127 -->

 
CTS Clearing House Interface – Specification 
 
 
127 
Appx 4.3.10.1 
File Name Convention 
C1 
The Response file name shall use the following naming convention: 
w_<filestring>.XML.<f>.RES 
 
Where: 
 
w is:  
             CXF for Capture file reject 
             RRF for Return Request file rejects  
             ERF for Extension Request file rejects and 
 
<filestring>       is same as in the received file 
             .XML                  is a mandatory file suffix 
            <f>                    is file id of the Response file.  This is unique for a particular 
 
 
 
  CXF/RRF/ERF file as there can be multiple Response files 
 
 
 
  for a single CXF/RRF/ERF file. 
            . RES                    is a mandatory file suffix for the Response file 
 
Appx 4.3.10.2 
File Structure 
FileSummary
FileHeader
Item
Response File Structure
Mandatory 
Element
Multiple 
Elements
Optional 
Element
Multiple 
Optional 
Elements
 
 
A1 
The response file structure shall be: 
 
<FileHeader …   > 
      <Item …   /> 
      <Item …   /> 
<FileSummary … /> 
</FileHeader> 
 
C2 
Element “FileHeader” is mandatory. 
NOTE: FileSummary element is mandatory only if Item element is present in the 
response file.

<!-- Page 128 -->

 
CTS Clearing House Interface – Specification 
 
 
128 
Appx 4.3.10.3 
Elements and Attributes 
Appx 4.3.10.3.1 
FileHeader 
 
Attributes of FileHeader 
 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
Xmlns 
Schema definition 
Must be 
urn:schemas-
ncr-
com:ECPIX:RE
S:FileStructure:
010001 
ANS 
48 
256 
M 
VersionNumber 
Version of this 
Interface definition– 
xxyyyy 
xx=country 
(01=RBI/NPCI) 
yyyy=version 
(0001) 
NS 
4 
6 
M 
TestFileIndicator 
 
P --> Production 
Must be   P 
A 
1 
1 
M 
CreationDate 
Response File 
creation date  
 
Date should be 
in DDMMYYYY 
format 
DATE 
8 
8 
M 
CreationTime 
Response File 
creation time  
 
Time should be 
HH24MISS 
format 
TIME 
6 
6 
M 
FileID 
A number that 
uniquely identifies 
the items in this 
file. Should be 
same as in the file 
name. 
Must be greater 
than 0 
AN 
1 
10 
M 
FileStatus 
Indicate file loading 
status. 
0 – File loaded 
successfully and all 
items pass 
validation 
1 – File loaded 
successfully but 
some items failed 
validation 
2 – File Header 
invalid 
3 – File format 
incorrect 
See sect 
4.3.10.3.3.1 
(0) 
N 
1 
2 
M

<!-- Page 129 -->

 
CTS Clearing House Interface – Specification 
 
 
129 
Appx 4.3.10.3.2 
FileSummary 
 
Attributes of FileSummary 
 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
TotalItemCount 
Total number of 
items in file 
 
N 
1 
8 
M 
TotalAmount 
Total amount in the 
file 
 
N 
1 
18 
M 
Appx 4.3.10.3.3 
Item 
NOTE: All fields marked * must be the exact same as were given in the PXF.  These fields are 
used to find the corresponding item and apply the status. 
 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
ItemSeqNo* 
This is a unique 
identifier for the 
bank for a 
“PresentmentDate” 
Special 
Condition 
NS 
14 
14 
M 
PayorBankRoutNo 
Drawee Bank 
Routing number 
 
NS 
9 
9 
M 
Amount 
Check amount 
 
N 
1 
18 
M 
AccountNo 
Drawee account 
number 
 
NS 
1 
25 
O 
SerialNo 
Check number 
 
NS 
6 
6 
M 
TransCode 
Transaction code 
 
NS 
1 
3 
M 
PresentingBankRoutNo* 
Routing number of 
the presenting 
bank 
 
NS 
9 
9 
M 
PresentmentDate* 
Date of capture of 
checks  
 
 
DATE 
8 
8 
M 
CycleNo* 
Capture cycle 
number. 
 
 
NS 
1 
2 
M 
RejectReason 
For rejected files 
A code that 
indicates the 
reason for rejecting 
an item or a file.  
See sect 
4.3.10.3.3.1 
 
NS 
1 
2 
M

<!-- Page 130 -->

 
CTS Clearing House Interface – Specification 
 
 
130 
Appx 4.3.10.3.3.1 
Reject Reason 
The following chart provides StatusCode and Reject Reasons along with the suggested resolution for the error. 
 
FILE 
STATUS 
(CODE) 
FILESTATUS 
(DESCRIPTION) 
REJECT 
REASON 
(CODE) 
REJECT REASON 
(DESCRIPTION) 
CXF RRF ERF 
Error Resolution to be done by Presenting / Drawee Bank 
Module 
0 
File Loaded successfully and 
All items passed validation 
at CHI  
N.A. 
N.A. 
√ 
√ 
√ 
 
1 
Invalid file name 
N.A. 
N.A. 
√ 
√ 
√ 
Rectify file naming convention as per IFS and resubmit the 
file with a new file name 
2 
Invalid file format 
N.A. 
N.A. 
√ 
√ 
√ 
Rectify File format as per IFS and resubmit the file with a new 
file name.  Possible errors include: 
- 
content failures as a result of XSD validation 
- 
items with ClearingType other than stated in filename 
3 
Invalid total item count 
N.A. 
N.A. 
√ 
√ 
√ 
Rectify TotalItemCount field in FileSummary so that it 
matches with the total count of all items in the file and 
resubmit the file with a new file name 
4 
Invalid total amount 
N.A. 
N.A. 
√ 
√ 
√ 
Rectify TotalItemAmount field in FileSummary so that it 
matches with the total amount of all items in the file and 
resubmit the file with a new file name 
5 
Invalid total number of item 
image elements 
N.A. 
N.A. 
√ 
X 
X 
Rectify number of ImageViewDetail element tags so that 
there are 3 image views as mandated per item and it matches 
with the field NumOfImageViews in item tag and resubmit the 
file with a new file name 
6 
Invalid image file name 
N.A. 
N.A. 
√ 
X 
X 
Rectify the value of FileName field of ImageViewData tag so 
that it matches with the CXF file name and resubmit the file 
with a new file name 
7 
Items Rejected 
1 
Items rejected by CHI 
Operator/Supervisor user 
post intimation by bank 
√ 
√ 
X 
Recapture the items after confirming with CHI Supervisor and 
resubmit the deleted items in a new file 
7 
Items Rejected 
2 
Item failed city validation 
√ 
X 
X 
These items were rejected as BOFD city does not fall within 
city master for intercity clearing or drawee city does not fall 
within city master for intercity clearing or drawee city does

<!-- Page 131 -->

 
CTS Clearing House Interface – Specification 
 
 
131 
not fall within city master for local clearing or BOFD city 
equals drawee city for intercity clearing. Please refer the 
latest version of CH Master file. 
7 
Items Rejected 
3 
PresentingBankRoutNo for 
item not found under this 
CHI 
√ 
X 
X 
Recapture the rejected items and resubmit them in a new file 
at the correct CHI after referring to the latest version of CH 
Master file. 
7 
Items Rejected 
4 
PresentingBankRoutNo for 
Item is in not-clearing 
mode or has been blocked 
or suspended 
√ 
√ 
√ 
These items were rejected as the Presenting bank was put in 
NOT CLEARING mode or has been blocked or has been 
suspended at the Clearing House. Please refer the latest 
version of CH Master file. 
7 
Items Rejected 
5 
Drawee Branch has been 
blocked 
√ 
√ 
√ 
These items were rejected as the drawee branch was blocked 
/ suspended at the Clearing House. Please refer the latest 
version of CH Master file. 
7 
Items Rejected 
6 
Bank or CHI does not allow 
ON US items 
√ 
X 
X 
These items were rejected as the Bank or CHI was set as not 
to send ON US items at the Clearing House. Please refer the 
latest version of CH Master file. 
7 
Items Rejected 
7 
Wrongly Presented item 
√ 
X 
X 
These items were rejected as they were wrongly Presented. 
Please refer the latest version of CH Master file. 
7 
Items Rejected 
8 
Drawee bank for Item is in 
not-clearing mode or has 
been blocked or suspended 
√ 
√ 
√ 
These items were rejected as the Drawee bank was put in 
NOT CLEARING mode or has been blocked or has been 
suspended at the Clearing House. Please refer the latest 
version of CH Master file. 
7 
Items Rejected 
9 
Returns Rejected at CH due 
to Bank Exclusion / 
Unwinding 
X 
√ 
X 
These returns were rejected due to Bank Exclusion / 
Unwinding at the CH. 
7 
Items Rejected 
10 
Extension Period of Item 
falls beyond CH permissible 
period 
X 
X 
√ 
These items were rejected as their Extension Period falls 
outside of the Max ExtensionPeriod set at the CH. Please refer 
the latest version of CH Master file. 
7 
Items Rejected 
11 
Return Period of item has 
expired 
X 
√ 
√ 
These returns / extension request were rejected as their 
Return Period falls outside of the Max Return Period set at the 
CH. Please refer the latest version of CH Master file. 
7 
Items Rejected 
12 
Extension Reason code not 
valid 
X 
X 
√ 
These items were rejected as their Extension Reason code is 
invalid. Please refer the latest version of CH Master file. 
7 
Items Rejected 
13 
Return Reason code not 
valid 
X 
√ 
X 
These items were rejected as their Return Reason code is 
invalid. Please refer the latest version of CH Master file.

<!-- Page 132 -->

 
CTS Clearing House Interface – Specification 
 
 
132 
7 
Items Rejected 
14 
Item can not be attached to 
any Payment Type 
√ 
X 
X 
These items were rejected as there is no Payment Type 
defined with the given combination of item details. Please 
refer the latest version of CH Master file. 
7 
Items Rejected  
15 
Item failed Short Account 
Number validation. 
√ 
X 
X 
These items were rejected as Account Number is Invalid or 
Invalid Documentation Type for government cheque  
 
7 
Items Rejected 
16 
IQA validation failure 
√ 
X 
X 
These items were rejected as the image view(s) of item failed 
IQA validations specified. Please re-present the item by 
correcting the IQA failure(s) mentioned in the exception 
report. 
7 
Items Rejected 
17 
Invalid Transaction Code 
√ 
X 
X 
These items were rejected as their Transaction Code does not 
match with the clearing type. Please refer the latest version 
of CH Master file. 
7 
Items Rejected 
18 
Capture Date not valid for 
Presentment 
√ 
X 
X 
These items were rejected as the presentment date of the 
items were older than permissable backward window set in 
the system or the presentment date of the items had a 
value greater than clearing date. 
7 
Items Rejected 
19 
Item was duplicate 
√ 
X 
X 
These items were rejected as an item with the same UDK 
value is already present. 
7 
Items Rejected 
20 
Item has duplicate views 
√ 
X 
X 
These items were rejected as there were more than one view 
having same ImageViewIndicator. 
7 
Items Rejected 
21 
Original item not found 
X 
√ 
√ 
The original item was not found in the system 
7 
Items Rejected 
22 
Extension requested 
outside CH configured 
period 
X 
X 
√ 
Request for extension can be sought only within "x" hrs 
configured by CH. Please refer the latest version of CH Master 
file. 
7 
Items Rejected 
23 
Invalid Documentation Type 
for IQAIgnoreInd=1 
√ 
X 
X 
These items were rejected as the Documentation Type should 
be Image-to-follow-with-Paper-to-Follow when IQAIgnoreInd 
= 1. Please re-present the cheque with a proper 
documentation type as prescribed in the CHI IFS. 
7 
Items Rejected 
24 
Item already extended 
X 
X 
√ 
These extension requests were rejected as an extension 
request has already been done on this item previously. 
7 
Items Rejected 
25 
Items already returned 
X 
√ 
√ 
These return request (in case of RRF) or extension request (in 
case of ERF) were rejected as the original item has already

<!-- Page 133 -->

 
CTS Clearing House Interface – Specification 
 
 
133 
been returned. 
7 
Items Rejected 
26 
Item failed AT-PAR 
Validation 
√ 
X 
X 
These items were rejected as they failed At-Par validation. 
Please refer the latest version of CH Master file. 
7 
Items Rejected 
27 
Item Failed Government 
Cheque Validation  
 
√ 
X 
X 
These items were rejected as they failed Government Cheque 
validation. Please refer the latest version of CH Master file 
and CHI Specification for details.  
7 
Items Rejected 
28 
Item Failed Paper to Follow 
city validation 
√ 
X 
X 
These items were rejected as the BOFD city does not equal 
drawee city for Paper to Follow cheques. 
7 
Items Rejected 
34 
Payor Branch not 
available in BOFD city for 
P2F instruments  
 
√ 
 
X 
 
X 
Payor branch not available in the BOFD city, please process 
this cheque from the Payor branch city only so that the P2F 
instrument will be exchanged for processing. 
7 
Items Rejected 
35 
Item failed with return 
reason comment validation 
X 
√ 
X 
These items with return reason ‘88’ were rejected as the 
return reason comment is either empty or does not match 
with validation criteria

<!-- Page 134 -->

 
CTS Clearing House Interface – Specification 
 
 
134 
Appx 4.3.11 
OUTWARD ACKNOWLEDGEMENT FILE (.OACK) 
When the CHI gets end of session information from CH it generates an Outward Acknowledgement File.  
The Outward Acknowledgement File is in XML format and consists of a list of all items that were 
successfully settled in a session at the CH. Outward Acknowledgement Files are generated for all 
outward files that affect the settlement of a session i.e. capture file (CXF) and Return Request File 
(RRF).  
Capture shall use SessionDate, CLOSE_RECEIVING_TIME of the Session and SessionExtensionHrs 
for the Session to calculate the maximum return period. 
Appx 4.3.11.1 
File Name Convention 
B1 
The Outward Acknowledgement file name shall use the following naming convention: 
w.<SessionNumber>.<SessionDate>.OACK 
 
Where: 
 
 
W is  
name of the original outward file (CXF or RRF) 
.<SessionNumber> 
is 
Session number to which the items were added. 
.<SessionDate> is 
Date of the session to which the items were added. 
.OACK is 
a mandatory file suffix for the outward acknowledgment file 
              
  
 
Appx 4.3.11.2 
File Structure 
FileSummary
FileHeader
Item
Outward Acknowledgement File Structure
Mandatory 
Element
Multiple 
Elements
 
B1 
The outward acknowledgement file structure shall be: 
 
<FileHeader …   > 
      <Item …   /> 
      <Item …   /> 
<FileSummary … /> 
</FileHeader> 
 
C2 
Elements “FileHeader”, “Item” and “FileSummary” tags are mandatory

<!-- Page 135 -->

 
CTS Clearing House Interface – Specification 
 
 
135 
Appx 4.3.11.3 
Elements and Attributes 
Appx 4.3.11.3.1 
FileHeader 
Attributes of FileHeader 
 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
Xmlns 
Schema definition 
Must be 
urn:schemas-
ncr-
com:ECPIX:OA
CK:FileStructur
e:010001 
ANS 
52 
256 
M 
VersionNumber 
Version of this 
Interface definition 
xxyyyy 
xx=country 
(01=RBI/NPCI) 
yyyy=version 
(0001) 
NS 
4 
6 
M 
TestFileIndicator 
 
P --> 
PRODUCTION 
Must be P 
A 
1 
1 
M 
CreationDate 
File creation date.  
 
Note: 
This is the creation 
date of this OACK 
file, and is not the 
session date as 
given in the 
filename. 
Date should be 
in DDMMYYYY 
format 
DATE 
8 
8 
M 
CreationTime 
File creation time.  
 
Note: 
This is the creation 
time of this OACK 
file. 
Time should be 
HH24MISS 
format 
TIME 
6 
6 
M 
SessionNumber 
Session number to 
which the items 
were added. 
 
Shall be same as in 
the filename. 
 
N 
1 
2 
M 
SessionDate 
Date of the session 
to which the items 
were added. 
 
Shall be same as in 
the filename. 
Date should be 
in DDMMYYYY 
format 
DATE 
8 
8 
M 
SettlementDate 
Value Date – Date 
on which the Items 
shall be posted in 
books of account. 
Date should be 
in DDMMYYYY 
format 
DATE 
8 
8 
M

<!-- Page 136 -->

 
CTS Clearing House Interface – Specification 
 
 
136 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
SessionExtensionHrs 
Default Extension 
Hours Granted at 
CH. 
0 
N 
1 
2 
M 
 
 
Appx 4.3.11.3.2 
FileSummary 
Attributes of FileSummary 
 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
TotalItemCount 
Total number of 
items in file 
Must be greater 
than 0 
N 
1 
8 
M 
 
 
Appx 4.3.11.3.3 
Item 
Attribute Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
ItemSeqNo 
This is a unique 
identifier for the 
bank for a 
PresentmentDate. 
 
NS 
14 
14 
M 
PresentingBankRoutNo 
Routing number of 
the presenting 
bank 
 
NS 
9 
9 
M 
PresentmentDate 
Date of capture of 
checks  
 
DATE 
8 
8 
M 
CycleNo 
Capture cycle 
number. 
 
NS 
1 
2 
M 
ItemStatus 
CH will set this 
field.  
Used to indicate to 
the drawee bank 
the status of the 
item being 
presented. 
For list of status 
codes see 
section 
4.10.3.3.1  
(0) 
N 
1 
2 
M 
                                   
 
Appx 4.3.11.3.3.1 
ItemStatus 
ItemStatus Codes

<!-- Page 137 -->

 
CTS Clearing House Interface – Specification 
 
 
137 
Status Code 
Description 
0 
Cleared by CH  
9 
Detected as Duplicate MICR Fields (SerialNo, TransCode, 
PayorBankRoutNo) 
 
Appx 4.3.12 
CH MASTER DATA FILE 
The following Clearing House Master data shall be available for use by the capture systems.   
 
 
Clearing House and Clearing Center, including Bank/Branch and blockages 
 
Item Return Reason 
 
Calendar 
 
Bundle Collection 
 
Session Definition and Collection Type 
 
Clearing Type and DocType definitions 
 
Item Extension Reason 
 
Translation Rules 
 
Transaction Codes 
 
City Master 
 
Appx 4.3.12.1 
File Name Convention 
A1 
The CHMaster Data file name shall use the following naming convention: 
CHM_ddmmyyyy_hhmmss_<SeqNo>.xml 
 
Where: 
 
ddmmyyyy    is the creation date (same as in the CHMasterHeader) 
            hhmmss         is the creation time (same as in the CHMasterHeader) 
            SeqNo            is a file sequence number (same as in the CHMaster element) 
            . xml               is a mandatory file suffix for the file 
 
Note: to determine the ‘latest’ instance of the file, use the combination of creation date, creation 
time and sequence_number.  Capture Systems (Presenting and Drawee) Modules could detect 
if they have the ‘latest’ instance of the file as a start-of-day activity, or they could be directed 
manually to get the ‘latest’ as a result of message, phone call etc by the CHI Supervisor. 
Appx 4.3.12.2 
File Structure

<!-- Page 138 -->

 
CTS Clearing House Interface – Specification 
 
 
138 
CHMaster 
CHMasterHeader 
CHMasterBody 
ClearingHouse 
ItemReturnReason 
Calendar 
BundleCollectionTyp
e 
SessionDefinition 
ItemExtensionReason 
TranslationRule 
TransactionCode 
CityMaster 
ClearingHouseInterfa
ce 
CalendarDetail 
SessionDefnCollectio
nType 
Blockage 
Bank 
Blockage 
DesignatedBranchFor
Bank 
Branch 
Blockage 
AtP
 
 
The CH Master Data File holds all the clearing house master elements, which are arranged in 
a specific order, and must be loaded in that order into the bank’s capture and drawee 
modules.

<!-- Page 139 -->

 
CTS Clearing House Interface – Specification 
 
 
139 
A1 
The Clearing House Master structure shall be: 
<CHMaster…   > 
<CHMasterHeader…   /> 
<CHMasterBody…   > 
        <ClearingHouse…   > 
             <ClearingHouseInterface…   > 
                   <Blockage …   /> 
                   <Bank…   > 
                         <Blockage …   /> 
                         <DesignatedBranchforTransCode …   /> 
                         <Branch…   > 
                               <Blockage…   /> 
                         </Branch> 
                   </Bank> 
             </ClearingHouseInterface> 
        </ClearingHouse> 
        <ItemReturnReason…   /> 
        <ItemExtensionReason…   /> 
        <Calendar…   > 
             <CalendarDetail…   /> 
        <Calendar/> 
        <BundleCollectionType…   /> 
        <SessionDefinition 
             <SessionDefnCollectionType…   /> 
        </SessionDefinition> 
        <TranslationRule…   /> 
        <TransactionCode…   /> 
        <CityMaster…   /> 
        <AtParBankMaster … /> 
</CHMasterBody> 
</CHMaster>  
 
 
Appx 4.3.12.3 
Elements and Attributes 
Appx 4.3.12.3.1 
CHMaster element 
The CH Master Element is the root element of the CH Master XML Document.  
It contains its own attributes and one CHMasterHeader Element and one CHMasterBody Element. Its 
attributes are defined as follows:

<!-- Page 140 -->

 
CTS Clearing House Interface – Specification 
 
 
140 
 
Element Name: CHMaster 
Attribute 
Data 
Type 
Size 
Usage 
Value/Format 
Description 
xmlns 
ANS 
 
256 
 
Not Null 
Urn:schemas-ncr-
com:ECPIX:CHM:File
Structure:010001 
 
Schema Definition 
SeqNo 
ANS 
 
6 
 
Not Null 
‘000001’~’999999’ 
 
Document Sequence Number 
that is equal to the File 
Sequence Number defined in 
the File Name.  
Version  
ANS 
6 
Not Null 
‘4.0’ 
The NCR ECPIX Master File 
layout/structure version. 
 
Appx 4.3.12.3.2 
CHMasterHeader element 
The CHMasterHeader Element is a required element and generated per CH Master File (document).  
It contains information about the sender and file creation details. Its attributes are defined as follows: 
 
Element Name: CHMasterHeader 
 Attribute 
Data 
Type 
Siz
e 
Usage 
Value/Format 
Description 
ClearingHouseRout
No 
NS 
9 
Not Null 
 
The routing number of 
Clearing House wherein 
the data in the CHMaster 
file originated.  
TestInd 
A 
1 
Not Null 
‘P’:   
Production 
‘T’:   Test 
MUST BE “P” 
An indicator of whether 
the file being transmitted 
is a test file or a 
production file.  
CreationDate 
DATE 
8 
Not Null 
 
The file creation date. 
CreationTime 
TIME 
6 
Not Null 
 
The file creation time. 
 
Appx 4.3.12.3.3 
CHMasterBody element 
The CHMasterBody Element is a required element and generated by the Clearing House. This 
element holds all the clearing house master elements, which are arranged in a specific order, 
and must be loaded in that order into the bank’s capture and drawee modules. 
 
Element Name: CHMasterBody

<!-- Page 141 -->

 
CTS Clearing House Interface – Specification 
 
 
141 
This element doesn’t have any attributes but contains child elements arranged in the following order: 
 
one ClearingHouse Element 
 
zero or more ClearingHouseInterface Elements 
 
zero or more blockage elements 
 
zero or more Bank Elements 
 
zero or more DesignatedBranchforTransCode 
 
zero or more blockage elements 
 
zero or more Branch Elements 
 
zero or more blockage elements 
 
 
one or more ItemReturnReason Elements 
 
one or more Calendar Elements 
 
zero or more CalendarDetail Elements 
 
one or more BundleCollectionType Elements 
 
 one or more SessionDefinition Elements 
 
one or more SessionDefnCollectionType Elements 
 
one or more ItemExtensionReason Elements 
 
one or more TranslationRule Elements 
 
one or more TransactionCode Elements 
 
one or more CityMaster Elements 
 
one or more AtParBankMaster Elements 
 
 
Appx 4.3.12.3.4 
ClearingHouse element 
ClearingHouse Element describes the routing information of the clearing house(s). It is a required 
element.  
Each ClearingHouse element may contain one or more child elements—ClearingHouseInterface 
elements. Its attributes are defined as follows:  
 
Element Name: ClearingHouse  
Attribute 
Data 
Type 
Size 
Usage 
Value/Form
at 
Description 
CH_ROUTING_NBR 
NS 
9 
NOT 
NULL 
 
Routing number of the clearing 
house. 
 
Appx 4.3.12.3.5 
ClearingHouseInterface element 
ClearingHouseInterface Element describes the routing and address information of clearing house 
interface institutions belonging to a particular clearing house. It is required element and a child of 
ClearingHouse element.  
ClearingHouseInterface element may contain zero or more child elements—Bank elements and 
Blockage elements. Its attributes are defined as follows:

<!-- Page 142 -->

 
CTS Clearing House Interface – Specification 
 
 
142 
 
Element Name: ClearingHouseInterface 
Attribute 
Data 
Type 
Size 
Usage 
Value/Form
at 
Description 
CC_ROUTING_NBR 
NS 
 9 
NOT 
NULL 
 
Routing number of the clearing 
house interface. 
NAME 
ANS 
 50 
NOT 
NULL 
 
Name of the clearing house 
interface. (used in reports) 
STREET_ADDRESS 
ANS 
 50 
 
 
Street address of a location or 
mailing address. 
CITY 
ANS 
 50 
 
 
City in which the clearing house 
interface is located. 
STATE_PROVINCE 
ANS 
 50 
 
 
State in which the clearing 
house interface is located. 
COUNTRY 
ANS 
 10 
 
 
Country in which the clearing 
house interface is located. 
POSTAL_ZIP_CODE 
ANS 
 10 
 
 
Postal authority location 
address or identifier for mailing 
purposes. 
CLEARING_STATUS_
CODE 
ANS 
 10 
NOT 
NULL 
 
Code that uniquely identifies 
the clearing state or status of 
this clearing house interface. 
 
The possible values are 
CLEARING & 
NOT_CLEARING. 
NOTE 
ANS 
1000 
 
 
Miscellaneous details or notes 
as added by the CH 
Superintendant. Free format 
text. 
 
Appx 4.3.12.3.6 
Bank element 
Bank Element describes the attributes of banks belonging to a particular clearing house interface. It is a 
required element and a child of the ClearingHouseInterface element.  
The Bank element contains zero or more child elements—Branch elements, Blockage elements and 
DesignatedBranchforTransCode elements. Its attributes are defined as follows:  
 
Element Name: Bank  
Attribute 
Data 
Type 
Siz
e 
Usage 
Value/Format Description 
BANK_ROUTING_N
BR 
NS 
9 
NOT 
NULL 
 
Routing number of the bank.

<!-- Page 143 -->

 
CTS Clearing House Interface – Specification 
 
 
143 
NAME 
ANS 
 50 
NOT 
NULL 
 
Name of the bank. (used in 
reports) 
STREET_ADDRESS 
ANS 
 50 
 
 
Street address of a location or 
mailing address. 
CITY 
ANS 
 50 
 
 
City in which the bank is 
located. 
STATE_PROVINCE 
ANS 
 50 
 
 
State in which the bank is 
located. 
COUNTRY 
ANS 
 10 
 
 
Country in which the bank is 
located. 
POSTAL_ZIP_CODE 
ANS 
 10 
 
 
Postal authority location 
address or identifier for mailing 
purposes. 
CLEARING_STATUS
_CODE  
ANS 
 10 
NOT 
NULL 
 
Code that uniquely identifies a 
bank clearing state or status. 
The possible values are 
CLEARING, NOT_CLEARING 
and SUSPENDED 
SERVICE_BRANCH_
ROUTING_NBR 
NS 
9 
 
 
Service Branch for this bank. 
DESIGNATED_BRAN
CH_ROUTING_NBR 
NS 
9 
 
 
Designated Branch for this 
bank. 
NOTE 
ANS 
100
0 
 
 
Miscellaneous details or notes 
as added by the CH 
Superintendant. Free format 
text. 
CBS ENABLED 
N 
1 
Not Null 
'1' (Bank 
supports 
Speed 
Clearing) or 
'0' (Bank does 
not support 
Speed 
Clearing) 
Identifies whether the bank 
can clear Inter-regional items 
locally (a.k.a “Speed 
Clearing”). Banks may use this 
field for speed clearing 
validations in their Capture 
Systems or may choose to 
ignore this field. 
 
Appx 4.3.12.3.7 
DesignatedBranchForTransCode element 
DesignatedBranchforTransCode Element describes a bank’s branch designated to receive wrongly 
presented cheques for a particular combination of clearing type and transaction code.  
It is a child element of the Bank element. Its attributes are defined as follows:  
 
Element Name: DesignatedBranchforTransCode 
Attribute 
Data 
Siz
Usage 
Value/Format Description

<!-- Page 144 -->

 
CTS Clearing House Interface – Specification 
 
 
144 
Type 
e 
CLEARING_TYPE_C
ODE 
NS 
9 
NOT 
NULL 
 
Code that uniquely identifies 
the clearing type to which this 
designated branch belongs. 
 
See Appendix C for 
applicable values. 
 
DESIGNATED_BRAN
CH_ROUTING_NBR 
NS 
9 
NOT 
NULL 
 
Routing Number of the branch 
that is designated to receive 
wrongly presented cheques for 
this particular combination of 
clearing type and transcode 
TRANSCODE 
NS 
3 
NOT 
NULL 
 
Transaction Code No. 
 
Appx 4.3.12.3.8 
Branch element 
Branch Element describes the information of branches belonging to a particular bank.  
It is a required element and is a child element of a Bank element.  
The Branch element contains zero or more Blockage elements.  Its attributes are defined as follows:  
 
Element Name: Branch  
Attribute 
Data 
Type 
Siz
e 
Usage 
Value/Format Description 
BRANCH_ROUTING
_NBR 
NS 
9 
NOT 
NULL 
 
Routing number of the 
branch. 
NAME 
ANS 
 50 
NOT 
NULL 
 
Name of the branch. (used in 
reports) 
STREET_ADDRESS 
ANS 
 50 
 
 
Street address of a location or 
mailing address. 
CITY 
ANS 
 50 
 
 
City in which the branch is 
located. 
STATE_PROVINCE 
ANS 
 50 
 
 
State in which the branch is 
located. 
COUNTRY 
ANS 
 10 
 
 
Country in which the branch is 
located. 
POSTAL_ZIP_CODE 
ANS 
 10 
 
 
Postal authority location 
address or identifier for mailing 
purposes. 
BRANCH_NUMBER 
ANS 
10 
NOT 
NULL 
 
Number uniquely identifying a 
branch. 
NOTE 
ANS 
 
 
 
Miscellaneous details or notes

<!-- Page 145 -->

 
CTS Clearing House Interface – Specification 
 
 
145 
100
0 
as added by the CH 
Superintendant. Free format 
text. 
 
Appx 4.3.12.3.9 
ItemReturnReason element 
ItemReturnReason Element describes return code and reason for the returned items.  
It is a required element, and its attributes are described as follows:  
 
Element Name: ItemReturnReason 
Attribute 
Data 
Type 
Siz
e 
Usage 
Value/Format Description 
RETURN_REASON
_CODE 
NS 
10 
NOT 
NULL 
 
Code that uniquely identifies 
an item return reason. 
DESCRIPTION 
ANS 
100 
 
 
Free format text describing an 
item return reason code. 
 
Appx 4.3.12.3.10 
Calendar element 
The Calendar Element shall be a required element.  
It describes a new type of calendar and shall contain one or more child elements--CalendarDetail 
elements. Its attributes are defined as follows:   
 
Element Name: Calendar 
Attribute 
Data 
Type 
Siz
e 
Usage 
Value/Format Description 
CALENDAR_CODE 
ANS 
10 
NOT 
NULL 
 
Code that uniquely identifies 
a calendar  
DESCRIPTION 
ANS 
50 
 
 
Text description or name of a 
particular calendar, such as 
“Local” or “National”. 
 
Appx 4.3.12.3.11 
CalendarDetail element 
The CalendarDetail Element shall be a required element.  
It describes all the business / working days and non-business / non-working days for a particular 
calendar. Its attributes are defined as follows:   
 
Element Name: CalendarDetail 
Attribute 
Data 
Type 
Siz
e 
Usage 
Value/Format Description 
CALENDAR_ID 
ANS 
10 
NOT 
NULL 
 
Unique identifier of this detail 
for the particular calendar. 
DESCRIPTION 
ANS 
50 
 
 
Text description or name of a 
particular calendar day, such

<!-- Page 146 -->

 
CTS Clearing House Interface – Specification 
 
 
146 
as Christmas or Easter. 
VALID_WORK_DAY 
N 
1 
NOT 
NULL 
 
Indicates whether a calendar 
day is a valid business 
working day or non-business 
working day 
 
Appx 4.3.12.3.12 
BundleCollectionType element 
A BundleCollectionType is synonymous with a PaymentType within the Indian Cheque Processing 
scenario.  For consistency, this CHI Specification will describe the solution using the term 
“PaymentTypes”. 
The BundleCollectionType element contains the various attributes that describe a specific “payment 
type” that is supported by the ECPIX system. Several different BundleCollectionType elements allow the 
definition of all possible ‘PaymentTypes’ that are processed by the system.  Some examples of payment 
types are “Local-Paper to Follow”, “Local-No Paper to Follow”, “High Value-Paper to Follow”, “High 
Value-No Paper to Follow”, “Intercity-Paper to Follow” and “Intercity-No Paper to Follow”. 
 
Each item in the CXF file sent to the CHI must correspond to a payment type that is supported by the 
system.  
The following checks are done by the CHI to verify whether an item corresponds to a payment type: 
 
Amount of the item should fall between “ITEM_AMOUNT_UPPER_LIMIT” and 
“ITEM_AMOUNT_LOWER_LIMIT” of the payment type 
 
“ClearingType” of the item should be equal to the “CLEARING_TYPE_CODE” of the payment 
type 
 
“DocType” of the item should be equal to the “DOCN_TYPE_IND_CODE” of the payment type 
 
When requesting an extension for an item, the CHI verifies that the extension duration requested for the 
item falls within “MAX_ITEM_EXTENSION_DURATION” period defined for the payment type. 
 
When an item is returned, the CHI verifies that the return has been made within the 
“CLEARING_CYCLE_DURATION” period defined for the payment type. 
 
Payment Types can be used to identify the session an item will get attached to. Please refer Appx 
4.11.3.13 to understand session definition and Appx 4.11.3.14 to understand payment types associated 
with a session. 
 
The attributes of BundleCollectionType Element are described as follows.  
 
Element Name: BundleCollectionType 
Attribute 
Data 
Type 
Size 
Usage 
Value/Forma
t 
Description 
BUNDLE_COLLECTI
ON_TYPE_CD 
ANS 
10 
NOT 
NULL 
 
Code that uniquely 
identifies this payment type 
DESCRIPTION 
ANS 
50 
 
 
Free format text describing 
this payment type 
DISPLAY_NAME 
ANS 
15 
NOT 
NULL 
 
Short name (abbreviation), 
for display purposes, of this 
payment type.

<!-- Page 147 -->

 
CTS Clearing House Interface – Specification 
 
 
147 
CLEARING_CYCLE_
DURATION 
N 
10 
NOT 
NULL 
 
Cycle Length or Duration of 
time (in hours) in which an 
item corresponding to this 
payment type must be 
returned back to the 
presenting financial 
institution. 
MAX_ITEM_EXTEN
SION_DURATION 
N 
10 
NOT 
NULL 
 
Maximum Duration of time 
(in hours) beyond which an 
item corresponding to this 
payment type cannot be 
extended. 
MAX_DURATION_F
OR_SNDNG_EXTNS
N 
N 
10 
NOT 
NULL 
 
Maximum duration of time 
(in hours) within which 
extension for an item should 
be requested by Drawee 
Bank module 
RTN_BUNDLE_COL
LECTION_TYPE_CD 
ANS 
10 
 
 
If this payment type is 
“Presentment”, this field will 
contain the 
“BUNDLE_COLLECTION_T
YPE_CD” of its 
corresponding Return 
Payment type.  
 
Note: Every Presentment 
payment type will be linked 
to a Return payment type 
ITEM_AMOUNT_UP
PER_LIMIT 
N 
18 
NOT 
NULL 
 
Maximum amount value of 
an item corresponding to 
this payment type 
ITEM_AMOUNT_LO
WER_LIMIT 
N 
18 
NOT 
NULL 
 
Minimum amount value of 
an item corresponding to 
this payment type 
CLEARING_TYPE_C
ODE 
ANS 
10 
NOT 
NULL 
 
Code that uniquely 
identifies the ”ClearingType” 
attribute of an item 
corresponding to this 
payment type 
 
See See Appendix C for the 
list of values applicable for 
this column

<!-- Page 148 -->

 
CTS Clearing House Interface – Specification 
 
 
148 
CORE_COLLECTIO
N_TYPE_CD 
ANS 
10 
NOT 
NULL 
 
Code that uniquely 
identifies whether the item 
corresponding to this 
payment type should be a 
debit / credit instrument. 
The following values shall 
be applicable to this 
column: 
”DR” => DEBIT 
”CR” => CREDIT 
DOCN_TYPE_IND_
CODE 
ANS 
10 
NOT 
NULL 
 
Code that uniquely 
identifies the ” DocType” 
attribute of an item 
corresponding to this 
payment type 
 
The possible values for this 
column are: 
“B” – Image to Follow 
without paper 
“C” – Image to Follow with 
Paper to Follow 
 
 
Appx 4.3.12.3.13 
SessionDefinition element 
SessionDefinition Element describes the various sessions defined and supported by the system. There 
will be a session definition element for every session defined in the system.It shall be a required element.  
 
SessionDefinition contains one or more child elements--SessionDefnCollectionType elements. Its 
attribute are described as follows: 
 
Element Name: SessionDefinition 
Attribute 
Data 
Type 
Size 
Usage 
Value/Forma
t 
Description 
SESSION_NBR  
N 
5 
NOT 
NULL 
 
Unique identifier (primary 
key) of a session  
DESCRIPTION 
ANS 
50 
 
 
Free format text describing 
the session. 
VALID_MON 
N 
1 
NOT 
NULL 
 
Indicates whether the 
session operates on 
Monday. 
VALID_TUE 
N 
1 
NOT 
NULL 
 
Indicates whether the 
session operates on 
Tuesday. 
VALID_WED 
N 
1 
NOT 
NULL 
 
Indicates whether the 
session operates on 
Wednesday.

<!-- Page 149 -->

 
CTS Clearing House Interface – Specification 
 
 
149 
VALID_THU 
N 
1 
NOT 
NULL 
 
Indicates whether the 
session operates on 
Thursday. 
VALID_FRI 
N 
1 
NOT 
NULL 
 
Indicates whether the 
session operates on Friday. 
VALID_SAT 
N 
1 
NOT 
NULL 
 
Indicates whether the 
session operates on 
Saturday. 
VALID_SUN 
N 
1 
NOT 
NULL 
 
Indicates whether the 
session operates on 
Sunday. 
OPEN_RECEIVING_
TIME 
Time 
4 
NOT 
NULL 
 
Time of day that the session 
opens to receive items (24-
hour clock). 
OPEN_RECEIVING_
OFFSET_DAYS 
N 
1 
 
 
Offset in days from session 
date when the session will 
open and receive data. 
CLOSE_RECEIVING
_TIME 
N 
4 
NOT 
NULL 
 
Time of day that the session 
closes receiving window for 
Presentment (24-hour 
clock) 
CALENDAR_CODE 
ANS 
10 
NOT 
NULL 
 
Code that identifies the 
calendar as per which this 
session will operate. 
Refer Appx 4.12.3.10 for 
calendars definition 
SESSION_OPERATI
ON_MODE_CODE 
ANS 
1 
NOT 
NULL 
 
Defines whether the 
session is operating in 
TEST / PRODUCTION 
mode.  
 
T => TEST 
P => PRODUCTION 
CURRENCY_CODE 
ANS 
10 
NOT 
NULL 
 
ISO code of the currency 
associated with the session 
 
Appx 4.3.12.3.14 
SessionDefnCollectionType element 
SessionDefnCollectionType Element describes the payment types associated with a clearing session. It 
links the item processing attributes that are specified by the BundleCollectionType (e.g. min & max 
amount) to a specific session. 
It is a required element and is a child of Session Definition Element.  Its attribute are described as 
follows:  
 
Element Name: SessionDefnCollectionType

<!-- Page 150 -->

 
CTS Clearing House Interface – Specification 
 
 
150 
Attribute 
Data 
Type 
Size 
Usage 
Value/Forma
t 
Description 
SESSION_NBR  
N 
 
5 
NOT 
NULL 
 
Unique identifier (primary 
key) of a session definition 
record.  
BUNDLE_COLLEC
TION_TYPE_CD 
ANS 
10 
NOT 
NULL 
 
Code that uniquely 
identifies a (financial data) 
bundle type. 
 
Appx 4.3.12.3.15 
ItemExtensionReason element 
ItemExtensionReason Element describes extension codes and reasons for extending items.  
 
It is a required element, and its attributes are described as follows:  
 
Element Name: ItemExtensionReason 
Attribute 
Data 
Type 
Siz
e 
Usage 
Value/Format Description 
EXTENSION_REAS
ON_CODE 
ANS 
10 
NOT 
NULL 
 
Code that uniquely identifies 
an item extension reason. 
DESCRIPTION 
ANS 
100 
 
 
Free format text describing an 
item extension reason code. 
 
Appx 4.3.12.3.16 
TranslationRule element 
TranslationRule Element describes the various translation rules for bank merger and sub-member bank 
movement. It is a required element, and its attributes are described as follows:  
 
Element Name: TranslationRule 
Attribute 
Data 
Type 
Siz
e 
Usage 
Value/Format Description 
PAYOR_BANK_RO
UTING_NBR 
N 
9 
NOT 
NULL 
 
The Routing Number located 
on cheque that is supposed to 
be translated 
LOGICAL_ROUTING
_NBR 
N 
9 
NOT 
NULL 
 
The Routing Number to which 
the cheque is supposed to be 
routed 
FROM_DATE 
Date 
8 
NOT 
NULL 
 
The start date from which this 
translation rule is applicable 
TO_DATE 
Date 
8 
 
 
The end date to which this 
translation rule is applicable 
DESCRIPTION 
ANS 
250 
 
 
Free format text describing the 
translation rule

<!-- Page 151 -->

 
CTS Clearing House Interface – Specification 
 
 
151 
Appx 4.3.12.3.17 
Blockage element 
Blockage element allows a Clearing Center / Bank / Branch to be blocked for a defined period of time so 
as to take care of situations like strikes, natural disasters or any other reason deemed suitable by the 
central bank. It is a required element, can be a child of Clearing House Interface, Bank and Branch 
Element and its attributes are described as follows:  
Element Name: Blockage 
 
Attribute 
Data 
Type 
Siz
e 
Usage 
Value/Format Description 
FROM_DATE 
Date 
8 
NOT 
NULL 
 
The start date from which this 
blockage is applicable  
Note – This is Value Date and 
not System Date. 
TO_DATE 
Date 
8 
NOT 
NULL 
 
The end date to which this 
blockage rule is applicable 
Note – This is Value Date and 
not System Date. 
DESCRIPTION 
ANS 
250 
 
 
Free format text describing the 
blockage 
 
 
Appx 4.3.12.3.18 
TransactionCode element 
TransactionCode Element describes the valid Transaction Codes that the CHI will accept. It is a required 
element, and its attributes are described as follows:  
 
Attribute 
Data 
Type 
Siz
e 
Usage 
Value/Format Description 
CODE 
NS 
3 
NOT 
NULL 
 
Code No. 
DESCRIPTION 
ANS 
100 
NOT 
NULL 
 
Description of Code 
 
Appx 4.3.12.3.19 
CityMaster element 
CityMaster Element describes the valid city codes for every clearingtype. It is a required element, and its 
attributes are described as follows:  
 
Attribute 
Data 
Type 
Siz
e 
Usage 
Value/Format Description 
CITYCODE 
NS 
3 
NOT 
NULL 
 
3 digit City code

<!-- Page 152 -->

 
CTS Clearing House Interface – Specification 
 
 
152 
CITYNAME 
ANS 
25 
NOT 
NULL 
 
Name of the city 
CLEARINGTYPE 
NS 
2 
NOT 
NULL 
 
See Appendix C for details 
 
Appx 4.3.12.3.20 
AtParBankMaster element 
AtParBankMaster Element designates the clearing types to which AtPar cheques for a bank can be 
attached.  It is a required element, and its attributes are described as follows:  
 
Attribute 
Data 
Type 
Siz
e 
Usage 
Value/Format Description 
BANKCODE 
NS 
3 
NOT 
NULL 
 
3 digit Bank code 
CLEARINGTYPE 
NS 
2 
NOT 
NULL 
 
See Appendix C for details 
Note - AtParBankMaster Element designates the clearing types (LOCAL / HIGHVALUE / INTERCITY) to 
which AtPar cheques belonging (drawn) to a bank non-participating in CTS can be attached to. Such 
banks should have a correspondent relationship with a bank participating in CTS. Additionally a 
translation rule needs to be added to direct AtPar cheques of non-participating bank to participating 
bank's branch. AtPar cheques belonging (drawn) to a bank participating in CTS can presented only using 
LOCAL / HIGHVALUE clearing types. 
 
Appx 4.3.13 
UNWOUND ITEM(S) FILE 
Unwound item(s) file notifies the bank of items that have been unwound at the CH due to a Clearing 
House Notification. This file will be generated and given to each affected bank directly by the CH.  
► Unlike other interface files, this file will not be created at the CHI, and is not a part of the 
normal CHI interface. 
 
Unwound Item(s) File will be a comma separated value (csv) file with the following naming convention: 
 
Appx 4.3.13.1 
File Name Convention 
B1 
The Unwound Item(s) file name shall use the following naming convention: 
 
UIF_nnnnnnnnn_<session_nos>_<session_date>_ddmmyyyy_hhmmss.CSV 
 
Where: 
 
UIF  
 
Unwind Item(s) File 
 
nnnnnnnnn 
Bank Routing Number (same as in File Summary Record) 
 
<session_nos> The clearing session number 
            <session_date> The clearing session date 
 
ddmmyyyy 
Creation Date (same as in File Summary Record) 
 
hhmmss 
Creation Time (same as in File Summary Record) 
 
.CSV  
Is a mandatory file type suffix

<!-- Page 153 -->

 
CTS Clearing House Interface – Specification 
 
 
153 
B2 
The value for the Bank Routing Number, Creation Date and Creation Time in the file name shall 
be the same as the contents of the File Summary record within the file. 
 
Appx 4.3.13.2 
File Structure 
B1 
The Unwound Item(s) file shall contain one File Summary Record followed by one or more item 
detail Record. 
B2 
The structure of the file shall be: 
 
File Summary Record 
 
 
Item Record (for item 1) 
 
 
Item Record (for item 2) 
 
 
. 
 
 
. 
 
 
Item Record (for item n) 
 
B3 
Each record in the file shall contain alphanumeric data and will be terminated by a carriage return 
and line feed. 
B4 
The first line of the Unwound Item(s) file shall always be the File Summary Record.  
B5 
 
The File Summary Record shall consist of data fields related to the entire Unwound Item(s) file 
separated by commas. The data fields of File Summary Record are defined in Section 1.1.3.1. 
B6 
Item Records shall follow the File Summary Record. 
B7 
The Item Record shall consist of the data fields related to one item, separated by commas. All 
data fields of the Item Record are defined in Section 1.1.3.2. 
 
Appx 4.3.13.3 
Record Formats 
Appx 4.3.13.3.1 
File Summary Record 
 
B1 
Data fields of the File Summary Record shall be as described in the following table: 
 
Data Field Name 
Description/ 
Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
Record type 
File Summary 
 
Shall be ‘FS’ 
A 
2 
2 
M 
Creation date 
File creation 
date 
Date should be 
in DDMMYYYY 
format 
DATE 
8 
8 
M 
Creation time 
File creation 
time 
Time should be 
HH24MISS 
format 
TIME 
6 
6 
M

<!-- Page 154 -->

 
CTS Clearing House Interface – Specification 
 
 
154 
Data Field Name 
Description/ 
Format 
Value (default) 
Special 
Condition 
Type 
Size 
Usag
e 
Min 
Max 
SessionNumber 
Session 
number in 
which the items 
were cleared. 
 
Shall be same 
as in the 
filename. 
 
N 
1 
2 
M 
SessionDate 
Date of the 
session in 
which the items 
were cleared.  
 
Shall be same 
as in the 
filename 
Date should be 
in DDMMYYYY 
format 
 
DATE 
8 
8 
M 
Total Items 
The total 
number of 
items within the 
file 
 
N 
 1 
8 
M 
Total Amount 
The sum of the 
value of all 
items within the 
file. 
 
N 
1 
18 
M 
 
Appx 4.3.13.3.2 
Item Record 
 
Data Field Name 
Description/ Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
Record type 
Item Record 
 
Shall be ‘PI’ to 
indicate 
Presentment 
Item 
Shall be “RI” to 
indicate Return 
Item 
A 
2 
2 
M 
ItemSeqNo* 
This is a unique identifier for 
the bank for a 
“PresentmentDate” 
 
NS 
14 
14 
M 
PayorBankRoutNo 
Drawee Bank Routing 
number 
 
NS 
9 
9 
M 
Amount 
Check amount 
 
N 
1 
18 
M 
AccountNo 
Drawee account number 
 
NS 
1 
25 
O 
SerialNo 
Check number 
 
NS 
6 
6 
M 
TransCode 
Transaction code 
 
NS 
1 
3 
M

<!-- Page 155 -->

 
CTS Clearing House Interface – Specification 
 
 
155 
Data Field Name 
Description/ Format 
Value (default) Type 
Size 
Usag
e 
Min 
Max 
PresentingBankRou
tNo* 
Routing number of the 
presenting bank 
 
NS 
8 
9 
M 
PresentmentDate* 
Date of capture of checks  
 
Date should be 
in DDMMYYYY 
format 
DATE 
8 
8 
M 
CycleNo* 
Capture cycle number. 
 
 
NS 
1 
2 
M 
 
Appx 4.4 CHI BRANCH INTERFACE MODULE'S BULK SEARCH INPUT FILE 
User provides the file containing inward items serial numbers to CHI Branch interface module. The CHI 
Branch interface module searches the specified item Serial numbers and displays it on screen. This 
allows multiple items to be returned manually after verification by operator.  
 
Appx 4.4.1 File Name Convention 
A1 
The Item bulk search file name shall use the following naming convention: 
 
<File Name>.CSV 
Where: 
 
<File Name>   Name of the file. It should not execced 30 characters. 
                                   File name should not contain any special character except “_”.  
 
.CSV  
Is a mandatory file type suffix. 
 
Appx 4.4.2 Elements 
A1 
The Item bulk search file structure shall contain “,” separated serial number in single line. 
A2 
All serial numbers shall be 6 digits Alpha Numeric. 
A3 
Serial number shall not contain any alaphabates and special charater.  
A4 
File shall not contain ” ” in between serial number.  
A5 
File shall not contain new multiple characters. 
A6 
File shall not contain not more than 250 Serial Number.

<!-- Page 156 -->

 
CTS Clearing House Interface – Specification 
 
 
156 
Appx 5 
Appendix  AA -  ECPIX File Examples 
This appendix contains a number of sample files used in the normal Clearing and Exchange processing. 
 
Appx 5.1 Capture Exchange File Example  
 
Capture digitally signing MICR and images and with IQA tests. 
 
File name: CXF_110002001_01042006_160000_02_5.XML 
 
<?xml version="1.0" encoding="UTF-8"?> 
<FileHeader xmlns="urn:schemas-ncr-com:ECPIX:CXF:FileStructure:010005" VersionNumber="010005"  
TestFileIndicator="P" CreationDate="01042006" CreationTime="160000" FileID="5"> 
<Item ItemSeqNo="00000101123456" PayorBankRoutNo="110229001" Amount="10000"  
AccountNo="123456" SerialNo="123456" TransCode="10" PresentingBankRoutNo="110002000"  
PresentmentDate="01042006" CycleNo="1" NumOfImageViews="3" ClearingType="02" DocType="C" 
MICRRepairFlags="000000" SpecialHandling="0" TruncatingRTNo="110002001" UserField="For My 
Use" IQAIgnoreInd="0" CurrencyInd="INR"> 
<AddendA BOFDRoutNo="110002001" BOFDBusDate="01042006" DepositorAcct="987654321" 
IFSC="xxxxxxxxxxx" /> 
<MICRDS Source="Capture" DigitalSignatureMethod=“RSA_with_SHA256” SecurityKeySize=“2048”  
MICRFingerPrint="PresentmentDate;PresentingBankRoutNo;CycleNo;ItemSeqNo;Amount;SerialNo;Tran
scode" DigitalSignatureLength="344"  
SignatureData="shdgskhfidsfidfifdsshgsgdklsksdfihydshvkjhvdkjdshkjdshkfdhkdshffdhydhdsfhkduyhuskh
gjguluklyuklliuy" SecurityOriginatorName="CaptureCert1" SecurityAuthenticatorName="CaptureCert1" 
SecurityKeyName="127f" /> 
      
<ImageViewDetail ViewFormat="TIFF" CompressionType="G4" ViewSideIndicator="Front BW" 
ViewDescriptor="Full" ImageAvailable="Y" ImageReproducable="Y" ReplacementDocIndicator="N"> 
<ImageViewData ImageDataLength="6400" ImageDataOffset="156780" FileName="  
CIBF_110002001_01042006_160000_02_5_00.img" ClippingOrigin="0" /> 
<ImageDS Source="Capture" DigitalSignatureMethod=“RSA_with_SHA256” SecurityKeySize=“2048” 
StartOfProtectedData="1" ProtectedDataLength="6400" DigitalSignatureLength="256" 
DigitalSignatureDataOffset="156280" FileName=" CIBF_110002001_01042006_160000_02_5_00.img" 
SecurityOriginatorName="CaptureCert1" SecurityAuthenticatorName="CaptureCert1" 
SecurityKeyName="127f"/> 
<ImageViewAnalysis Source=”Capture” ImageQuality="2" ImageUsability="2" 
ImagingBankSpecificTest="0" PartialImage="2" ExcessiveImageSkew="2" PiggybackImage="2" 
LightOrDark="2" Streaks-Bands="2" BelowMinimumImageSize="2" ExceedsMaximumImageSize="2" 
ImageEnabledPOD="2" SourceDocumentBad="2" DateUsability="2" PayeeUsability="2" 
ConvenienceAmountUsability="2" LegalAmountUsability="2"  
 SignatureUsability="2" PayorNameAndAddressUsability="2" MICRLineUsability="2" 
MemoLineUsability="2" PayorBankNameAndAddressUsability="2" PayeeEndorsementUsability="2" 
BOFDEndorsementUsability="2" TransitEndorsementUsability="2" ImageAnalysisUserInformation="2" 
UserField="string"/> 
         </ImageViewDetail> 
<ImageViewDetail ViewFormat="TIFF" CompressionType="G4" ViewSideIndicator="Back BW" 
ViewDescriptor="Full" ImageAvailable="Y" ImageReproducable="Y" ReplacementDocIndicator="N"> 
<ImageViewData ImageDataLength="6400" ImageDataOffset="256780" 
FileName="CIBF_110002001_01042006_160000_02_5_00.img" ClippingOrigin="0" /> 
<ImageDS Source="Capture" DigitalSignatureMethod=“RSA_with_SHA256” SecurityKeySize=“2048” 
StartOfProtectedData="1" ProtectedDataLength="6400" DigitalSignatureLength="256" 
DigitalSignatureDataOffset="256280" FileName="CIBF_110002001_01042006_160000_02_5_00.img"

<!-- Page 157 -->

 
CTS Clearing House Interface – Specification 
 
 
157 
SecurityOriginatorName="CaptureCert1" SecurityAuthenticatorName="CaptureCert1" 
SecurityKeyName="127f" /> 
<ImageViewAnalysis Source="Capture " ImageQuality="2" ImageUsability="2" 
ImagingBankSpecificTest="0" PartialImage="2" ExcessiveImageSkew="2" PiggybackImage="2" 
LightOrDark="2" Streaks-Bands="2" BelowMinimumImageSize="2" ExceedsMaximumImageSize="2" 
ImageEnabledPOD="2" SourceDocumentBad="2" DateUsability="2" PayeeUsability="2" 
ConvenienceAmountUsability="2" LegalAmountUsability="2" SignatureUsability="2" 
PayorNameAndAddressUsability="2" MICRLineUsability="2" MemoLineUsability="2"  
PayorBankNameAndAddressUsability="2" PayeeEndorsementUsability="2" 
BOFDEndorsementUsability="2" TransitEndorsementUsability="2" ImageAnalysisUserInformation="2" 
UserField="string"/> 
</ImageViewDetail> 
<ImageViewDetail ViewFormat="JFIF" CompressionType="JPEG" ViewSideIndicator="Front Gray" 
ViewDescriptor="Full" ImageAvailable="Y" ImageReproducable="Y" ReplacementDocIndicator="N"> 
<ImageViewData ImageDataLength="6400" ImageDataOffset="356780" 
FileName="CIBF_110002001_01042006_160000_02_5_00.img" ClippingOrigin="0" /> 
<ImageDS Source="Capture" DigitalSignatureMethod=“RSA_with_SHA256” SecurityKeySize=“2048” 
StartOfProtectedData="1" ProtectedDataLength="26400" DigitalSignatureLength="256" 
DigitalSignatureDataOffset="356280" FileName="CIBF_110002001_01042006_160000_02_5_00.img"  
SecurityOriginatorName="CaptureCert1" SecurityAuthenticatorName="CaptureCert1" 
SecurityKeyName="127f"/> 
<ImageViewAnalysis Source=”Capture” ImageQuality="2" ImageUsability="2" 
ImagingBankSpecificTest="0" PartialImage="2" ExcessiveImageSkew="2" PiggybackImage="2" 
LightOrDark="2" Streaks-Bands="2" BelowMinimumImageSize="2" ExceedsMaximumImageSize="2" 
ImageEnabledPOD="2" SourceDocumentBad="2" DateUsability="2" PayeeUsability="2" 
ConvenienceAmountUsability="2" LegalAmountUsability="2" SignatureUsability="2" 
PayorNameAndAddressUsability="2" MICRLineUsability="2" MemoLineUsability="2"  
PayorBankNameAndAddressUsability="2" PayeeEndorsementUsability="2" 
BOFDEndorsementUsability="2" TransitEndorsementUsability="2" ImageAnalysisUserInformation="2" 
UserField="string"/> 
        </ImageViewDetail> 
</Item> 
<FileSummary TotalItemCount="1" TotalAmount="10000"/> 
</FileHeader>

<!-- Page 158 -->

 
CTS Clearing House Interface – Specification 
 
 
158 
 
Appx 5.2 Posting Exchange File Example 
 
  
File name: BPXF_110229001_01_01042006_01042006_200000_23.XML 
 
<?xml version="1.0" encoding="UTF-8"?> 
<FileHeader xmlns="urn:schemas-ncr-com:ECPIX:PXF:FileStructure:010001" VersionNumber="010001"  
TestFileIndicator="P" CreationDate="01042006" CreationTime="200000"  FileID="23" 
SessionNumber="01" SessionDate="01042006" SettlementDate="01042006" SessionExtensionHrs="0" 
> 
    <Item ItemSeqNo="00000101123456" PayorBankRoutNo="110229001" Amount="10000"  
AccountNo="123456" SerialNo="123456" TransCode="10" PresentingBankRoutNo="110002000"  
PresentmentDate="01042006" CycleNo="1" NumOfImageViews="3" ClearingType="02" DocType="C" 
MICRRepairFlags="000000" SpecialHandling="0" TruncatingRTNo="110002001" UserField="" 
IQAIgnoreInd="0" CurrencyInd="INR" ItemStatus="0"> 
     <MICRDS Source="Capture" DigitalSignatureMethod=“RSA_with_SHA256” SecurityKeySize=“2048”  
MICRFingerPrint="PresentmentDate;PresentingBankRoutNo;CycleNo;ItemSeqNo;Amount;SerialNo;Tran
scode" DigitalSignatureLength=“344”  
SignatureData="shdgskhfidsfidfifdsshgsgdklsksdfihydshvkjhvdkjdshkjdshkfdhkdshffdhydhdsfhkduyhuskh
gjguluklyuklliuy" SecurityOriginatorName="CaptureCert1" SecurityAuthenticatorName="CaptureCert1" 
SecurityKeyName="127f" /> 
    <MICRDS Source="ECP.PBCC" DigitalSignatureMethod=“RSA_with_SHA256” 
SecurityKeySize=“2048”  
MICRFingerPrint="PresentmentDate;PresentingBankRoutNo;CycleNo;ItemSeqNo;Amount;SerialNo;Tran
scode" DigitalSignatureLength="344"  
SignatureData="shdgskhfidsfidfifdsshgsgdklsksdfihydshvkjhvdkjdshkjdshkfdhkdshffdhydhdsfhkduyhuskh
gjguluklyuklliuy" SecurityOriginatorName="ECPIXCert1" SecurityAuthenticatorName="ECPIXCert1" 
SecurityKeyName="9887" />  
     <AddendA BOFDRoutNo="110002001" BOFDBusDate="01042006" DepositorAcct="987654321"  
IFSC="xxxxxxxxxxx"/> 
     <ImageViewDetail ViewFormat="TIFF" CompressionType="G4" ViewSideIndicator="Front BW"  
ViewDescriptor="Full" ImageAvailable="Y" ImageReproducable="Y" ReplacementDocIndicator="N"> 
        <ImageViewData ImageDataLength="6400" ImageDataOffset="156780" FileName="  
BPIBF_110229001_01042006_200000_00_23_00.img" ClippingOrigin="0" /> 
        <ImageDS Source="Capture" DigitalSignatureMethod=“RSA_with_SHA256” 
SecurityKeySize=“2048” StartOfProtectedData="1" ProtectedDataLength="6400" 
DigitalSignatureLength=“256” DigitalSignatureDataOffset="156280" FileName=" 
BPIBF_110229001_01042006_200000_00_23_00.img"  
SecurityOriginatorName="CaptureCert1" SecurityAuthenticatorName="CaptureCert1" 
SecurityKeyName="127f" /> 
        <ImageDS Source="ECP.PBCC" DigitalSignatureMethod=“RSA_with_SHA256” 
SecurityKeySize=“2048” StartOfProtectedData="1" ProtectedDataLength="6400" 
DigitalSignatureLength=“256” DigitalSignatureDataOffset="156280" FileName=" 
BPIBF_110229001_01042006_200000_00_23_00.img"  
SecurityOriginatorName="ECPIX_Cert1" SecurityAuthenticatorName="ECPIX_Cert1" 
SecurityKeyName="9887" /> 
        <ImageViewAnalysis Source="Capture" ImageQuality="2" ImageUsability="2" 
ImagingBankSpecificTest="0" PartialImage="2" ExcessiveImageSkew="2" PiggybackImage="2" 
LightOrDark="2" Streaks-Bands="2" BelowMinimumImageSize="2" ExceedsMaximumImageSize="2" 
ImageEnabledPOD="2" SourceDocumentBad="2" DateUsability="2" PayeeUsability="2" 
ConvenienceAmountUsability="2" LegalAmountUsability="2" SignatureUsability="2" 
PayorNameAndAddressUsability="2" MICRLineUsability="2" MemoLineUsability="2"

<!-- Page 159 -->

 
CTS Clearing House Interface – Specification 
 
 
159 
PayorBankNameAndAddressUsability="2" PayeeEndorsementUsability="2" 
BOFDEndorsementUsability="2" TransitEndorsementUsability="2" ImageAnalysisUserInformation="2" 
UserField="string"/> 
        <ImageViewAnalysis Source="ECP.PBCC" ImageQuality="2" ImageUsability="0" 
ImagingBankSpecificTest="2" PartialImage="2" ExcessiveImageSkew="2" PiggybackImage="0" 
LightOrDark="0" Streaks-Bands="0" BelowMinimumImageSize="0" ExceedsMaximumImageSize="0" 
ImageEnabledPOD="0" SourceDocumentBad="0" DateUsability="0" PayeeUsability="0" 
ConvenienceAmountUsability="0" LegalAmountUsability="0" SignatureUsability="0" 
PayorNameAndAddressUsability="0" MICRLineUsability="0" MemoLineUsability="0"  
PayorBankNameAndAddressUsability="0" PayeeEndorsementUsability="0" 
BOFDEndorsementUsability="0" TransitEndorsementUsability="0" ImageAnalysisUserInformation="0" 
UserField="BS1:20000222222222202"/> 
        </ImageViewDetail> 
 
<ImageViewDetail ViewFormat="TIFF" CompressionType="G4" ViewSideIndicator="Back BW" 
ViewDescriptor="Full" ImageAvailable="Y" ImageReproducable="Y" ReplacementDocIndicator="N"> 
        <ImageViewData ImageDataLength="6400" ImageDataOffset="256780" FileName="  
BPIBF_110002001_01042006_160000_00_5_00.img" ClippingOrigin="0" /> 
                <ImageDS Source="Capture" DigitalSignatureMethod=“RSA_with_SHA256” 
SecurityKeySize=“2048” StartOfProtectedData="1" ProtectedDataLength="6400" 
DigitalSignatureLength=“256” DigitalSignatureDataOffset="256280" FileName=" 
BPIBF_110002001_01042006_160000_00_5_00.img"  
SecurityOriginatorName="CaptureCert1" SecurityAuthenticatorName="CaptureCert1" 
SecurityKeyName="127f" /> 
        <ImageDS Source="ECP.PBCC" DigitalSignatureMethod=“RSA_with_SHA256” 
SecurityKeySize=“2048” StartOfProtectedData="1" ProtectedDataLength="6400" 
DigitalSignatureLength=“256” DigitalSignatureDataOffset="256280" FileName=" 
BPIBF_110002001_01042006_160000_00_5_00.img"  
SecurityOriginatorName="ECPIX_Cert1" SecurityAuthenticatorName="ECPIX_Cert1" 
SecurityKeyName="9887" /> 
        <ImageViewAnalysis Source="Capture" ImageQuality="2" ImageUsability="2" 
ImagingBankSpecificTest="0" PartialImage="2" ExcessiveImageSkew="2" PiggybackImage="2" 
LightOrDark="2" Streaks-Bands="2" BelowMinimumImageSize="2" ExceedsMaximumImageSize="2" 
ImageEnabledPOD="2" SourceDocumentBad="2" DateUsability="2" PayeeUsability="2" 
ConvenienceAmountUsability="2" LegalAmountUsability="2" SignatureUsability="2" 
PayorNameAndAddressUsability="2" MICRLineUsability="2" MemoLineUsability="2" 
PayorBankNameAndAddressUsability="2" PayeeEndorsementUsability="2" 
BOFDEndorsementUsability="2" TransitEndorsementUsability="2" ImageAnalysisUserInformation="2" 
UserField="string"/> 
        <ImageViewAnalysis Source="ECP.PBCC" ImageQuality="2" ImageUsability="0" 
ImagingBankSpecificTest="2" PartialImage="2" ExcessiveImageSkew="2" PiggybackImage="0" 
LightOrDark="0" Streaks-Bands="0" BelowMinimumImageSize="0" ExceedsMaximumImageSize="0" 
ImageEnabledPOD="0" SourceDocumentBad="0" DateUsability="0" PayeeUsability="0" 
ConvenienceAmountUsability="0" LegalAmountUsability="0" SignatureUsability="0" 
PayorNameAndAddressUsability="0" MICRLineUsability="0" MemoLineUsability="0"  
PayorBankNameAndAddressUsability="0" PayeeEndorsementUsability="0" 
BOFDEndorsementUsability="0" TransitEndorsementUsability="0" ImageAnalysisUserInformation="0" 
UserField="BS1:20000222222222202"/> 
        </ImageViewDetail> 
<ImageViewDetail ViewFormat="JFIF" CompressionType="JPEG" ViewSideIndicator="Front Gray"  
ViewDescriptor="Full" ImageAvailable="Y" ImageReproducable="Y" ReplacementDocIndicator="N"> 
        <ImageViewData ImageDataLength="6400" ImageDataOffset="356780" FileName="  
BPIBF_110002001_01042006_160000_00_5_00.img" ClippingOrigin="0" /> 
        <ImageDS Source="Capture" DigitalSignatureMethod=“RSA_with_SHA256” 
SecurityKeySize=“2048” StartOfProtectedData="1" ProtectedDataLength="26400" 
DigitalSignatureLength=“256” DigitalSignatureDataOffset="356280" FileName="

<!-- Page 160 -->

 
CTS Clearing House Interface – Specification 
 
 
160 
BPIBF_110002001_01042006_160000_00_5_00.img" SecurityOriginatorName="CaptureCert1" 
SecurityAuthenticatorName="CaptureCert1" SecurityKeyName="127f" /> 
        <ImageDS Source="ECP.PBCC" DigitalSignatureMethod=“RSA_with_SHA256” 
SecurityKeySize=“2048” StartOfProtectedData="1" ProtectedDataLength="26400" 
DigitalSignatureLength=“256” DigitalSignatureDataOffset="356280" FileName=" 
BPIBF_110002001_01042006_160000_00_5_00.img" SecurityOriginatorName="ECPIX_Cert1" 
SecurityAuthenticatorName="ECPIX_Cert1" SecurityKeyName="9887" /> 
        <ImageViewAnalysis Source="Capture" ImageQuality="2" ImageUsability="2" 
ImagingBankSpecificTest="0" PartialImage="2" ExcessiveImageSkew="2" PiggybackImage="2" 
LightOrDark="2" Streaks-Bands="2" BelowMinimumImageSize="2" ExceedsMaximumImageSize="2" 
ImageEnabledPOD="2" SourceDocumentBad="2" DateUsability="2" PayeeUsability="2" 
ConvenienceAmountUsability="2" LegalAmountUsability="2" SignatureUsability="2" 
PayorNameAndAddressUsability="2" MICRLineUsability="2" MemoLineUsability="2" 
PayorBankNameAndAddressUsability="2" PayeeEndorsementUsability="2" 
BOFDEndorsementUsability="2" TransitEndorsementUsability="2" ImageAnalysisUserInformation="2" 
UserField="string"/> 
        <ImageViewAnalysis Source="ECP.PBCC" ImageQuality="2" ImageUsability="0" 
ImagingBankSpecificTest="2" PartialImage="2" ExcessiveImageSkew="2" PiggybackImage="0" 
LightOrDark="0" Streaks-Bands="0" BelowMinimumImageSize="0" ExceedsMaximumImageSize="0" 
ImageEnabledPOD="0" SourceDocumentBad="0" DateUsability="0" PayeeUsability="0" 
ConvenienceAmountUsability="0" LegalAmountUsability="0" SignatureUsability="0" 
PayorNameAndAddressUsability="0" MICRLineUsability="0" MemoLineUsability="0"  
PayorBankNameAndAddressUsability="0" PayeeEndorsementUsability="0" 
BOFDEndorsementUsability="0" TransitEndorsementUsability="0" ImageAnalysisUserInformation="0" 
UserField="BS1:20000222222222202"/> 
        </ImageViewDetail> 
</Item> 
<FileSummary TotalItemCount="1" TotalAmount="10000"/> 
</FileHeader>

<!-- Page 161 -->

 
CTS Clearing House Interface – Specification 
 
 
161 
Appx 5.3 Return Request File Example 
 
 
File name: RRF_110229001_01042006_180922_234.XML 
 
<?xml version="1.0" encoding="UTF-8"?> 
<FileHeader  xmlns="urn:schemas-ncr-com:ECPIX:RRF:FileStructure:010004" 
VersionNumber="010004" TestFileIndicator="P" CreationDate="01042006" CreationTime="180922" 
FileID="234" > 
    <Item ItemSeqNo="00000101123456" PayorBankRoutNo="110229001" Amount="10000"  
AccountNo="123456" SerialNo="123456" TransCode="10" PresentingBankRoutNo="110002000" 
PresentmentDate="01042006" CycleNo="1" ClearingType="02" ReturnReason="01" 
ReturnReasonComment="A/c not under operation"> 
     <AddendA BOFDRoutNo="110002001" BOFDBusDate="01042006" DepositorAcct="987654321" 
IFSC="xxxxxxxxxxx"/> 
<MICRDS Source="Drawee" DigitalSignatureMethod=“RSA_with_SHA256” SecurityKeySize="2048" 
MICRFingerPrint="PresentmentDate;PresentingBankRoutNo;CycleNo;ItemSeqNo;Amount;SerialNo;Tran
scode"  DigitalSignatureLength="344" 
SignatureData="shdgskhfidsfidfifdsshgsgdklsksdfihydshvkjhvdkjdshkjdshkfdhkdshffdhydhdsfhkduyhushgj
guluklyuklliuy" SecurityOriginatorName="DraweeCert1" SecurityAuthenticatorName="DraweeCert1" 
SecurityKeyName="127f" />  
    </Item>  
 
<FileSummary TotalItemCount="1" TotalAmount="10000"/> 
</FileHeader>

<!-- Page 162 -->

 
CTS Clearing House Interface – Specification 
 
 
162 
 
Appx 5.4 Return File Example  
 
File name: MRF_110002001_01042006_190922_245.XML 
 
<?xml version="1.0" encoding="UTF-8"?> 
<FileHeader  xmlns="urn:schemas-ncr-com:ECPIX:RF:FileStructure:010001" VersionNumber="010001"  
TestFileIndicator="P" CreationDate="01042006" CreationTime="190922"  FileID="245"> 
    <Item ItemSeqNo="00000101123456" PayorBankRoutNo="110229001" Amount="10000"   
AccountNo="123456" SerialNo="123456" TransCode="10" PresentingBankRoutNo="110002000"  
PresentmentDate="01042006" CycleNo="1" ClearingType="02" ReturnReason="01"  
ReturnReasonComment="A/c not under operation"> 
     <AddendA BOFDRoutNo="110002001" BOFDBusDate="01042006" DepositorAcct="987654321"  
IFSC="xxxxxxxxxxx"/> 
     <MICRDS Source="Drawee" DigitalSignatureMethod=“RSA_with_SHA256” SecurityKeySize="2048"  
MICRFingerPrint="PresentmentDate;PresentingBankRoutNo;CycleNo;ItemSeqNo;Amount;SerialNo;Tran
scode"  DigitalSignatureLength="344"  
SignatureData="shdgskhfidsfidfifdsshgsgdklsksdfihydshvkjhvdkjdshkjdshkfdhkdshffdhydhdsfhkduyhushgj
guluklyuklliuy" SecurityOriginatorName="DraweeCert1" SecurityAuthenticatorName="DraweeCert1" 
SecurityKeyName="127f"  />  
    </Item> 
<FileSummary TotalItemCount="1" TotalAmount="10000"/> 
</FileHeader> 
 
 
Appx 5.5 Extension Request File Example  
 
File name: ERF_110229001_01042006_190922_454.XML 
 
<?xml version="1.0" encoding="UTF-8"?> 
<FileHeader xmlns="urn:schemas-ncr-com:ECPIX:ERF:FileStructure:010002" VersionNumber="010002"  
TestFileIndicator="P" CreationDate="01042006" CreationTime="190922" FileID="454"  > 
     <Item ItemSeqNo="00000101123456" PayorBankRoutNo="110229001" Amount="10000"   
AccountNo="123456789" SerialNo="123456" TransCode="10" PresentingBankRoutNo="110002000"   
PresentmentDate="01042006" CycleNo="1" ExtensionPeriod="24" ExtensionReason="04"/> 
<FileSummary TotalItemCount="1" TotalAmount="10000"/> 
</FileHeader>

<!-- Page 163 -->

 
CTS Clearing House Interface – Specification 
 
 
163 
 
Appx 5.6 Extension File Example  
 
File name: MEF_110229001_01042006_204034_545.XML 
 
<?xml version="1.0" encoding="UTF-8"?> 
<FileHeader xmlns="urn:schemas-ncr-com:ECPIX:EF:FileStructure:010001" VersionNumber="010001"   
TestFileIndicator="P" CreationDate="01042006" CreationTime="204034"  FileID="545"> 
     <Item ItemSeqNo="00000101123456" PayorBankRoutNo="110229001" Amount="10000"   
AccountNo="123456" SerialNo="123456" TransCode="10" PresentingBankRoutNo="110002000"   
PresentmentDate="01042006" CycleNo=“1” ExtensionPeriod="24" ExtensionReasonCode="04"/> 
<FileSummary TotalItemCount="1" TotalAmount="10000"/> 
</FileHeader>

<!-- Page 164 -->

 
CTS Clearing House Interface – Specification 
 
 
164 
Appx 5.7 Response File Example  
 
File name: CXF_110002001_01042006_160000_02_5.XML.1.RES 
 
<?xml version="1.0" encoding="UTF-8"?> 
<FileHeader xmlns="urn:schemas-ncr-com:ECPIX:RES:FileStructure:010001" VersionNumber="010001"   
TestFileIndicator="P" CreationDate="01042006" CreationTime="160000" FileID="02" FileStatus="0"> 
<FileSummary TotalItemCount="1" TotalAmount="10000"/> 
</FileHeader>

<!-- Page 165 -->

 
CTS Clearing House Interface – Specification 
 
 
165 
Appx 5.8 Outward Acknowledgement File Example  
 
File Name: CXF_110002001_09072007_223122_1_57.XML.1.09072007.OACK 
 
<?xml version="1.0" encoding="UTF-8"?> 
<FileHeader xmlns="urn:schemas-ncr-com:ECPIX:OACK:FileStructure:010001" 
VersionNumber="010001" TestFileIndicator="P" CreationDate="09072007" CreationTime="214322" 
SessionNumber="1" SessionDate="09072007" SettlementDate="09072007" SessionExtensionHrs="0"> 
<Item ItemSeqNo="00000101000000" PresentingBankRoutNo="110002001" 
PresentmentDate="09072007" CycleNo="1" ItemStatus="0"/> 
<FileSummary TotalItemCount="1"/> 
</FileHeader> 
 
Appx 5.9 Unwound Item File Example 
File name: UIF_110002000_1_21102007_22102007_201133.CSV 
 
FS,22102007,201133,1,21102007,2,2500000 
PI,1982,110287007,1500000,00987667,0014567,11,110002000,21102007,01 
PI,56789,110287082,1000000,567009,0897609,11,110002000,21102007,01 
 
Appx 5.10 Example of FILE for CHI Branch interface module’s bulk search 
File name: BULK_SERACH_ITEM_12_June_2013.CSV 
 
020302,020303,020304,020305,020306,020307,020308,020309,020310,020311,020312,020313,02031
4,020315,020316

<!-- Page 166 -->

 
CTS Clearing House Interface – Specification 
 
 
166 
Appx 6 
Appendix  BB – CH Master Data File Example 
 
<?xml version="1.0" encoding = "UTF-8"?> 
<CHMaster xmlns="urn:schemas-ncr-comECPIX:CHM:FileStructure:010001" SeqNo="01" Version="4.0"> 
<CHMasterHeader ClearingHouseRoutNo="110999999" TestInd="P" CreationDate="06302006” 
CreationTime=”132555" /> 
<CHMasterBody> 
<ClearingHouse CH_ROUTING_NBR="110999999"> 
<ClearingHouseInterface CC_ROUTING_NBR="110029000" NAME=" Punjab National Bank CHI" 
STREET_ADDRESS="Janpath" CITY="NEW DELHI" STATE_PROVINCE ="DELHI" COUNTRY=" INDIA" 
POSTAL_ZIP_CODE="110002" CLEARING_STATUS_CODE="CLEARING" NOTE=""> 
<Bank BANK_ROUTING_NBR="110029001" NAME="Punjab National Bank" STREET_ADDRESS="Janpath" 
CITY="NEW DELHI" STATE_PROVINCE ="DELHI" COUNTRY ="INDIA" POSTAL_ZIP_CODE="110002" 
CLEARING_STATUS_CODE="CLEARING" NOTE="" SPEED_CLEARING=”0” > 
<DesignatedBranchforTransCode CLEARING_TYPE_CODE="01" 
DESIGNATED_BRANCH_ROUTING_NBR="110029099" TRANSCODE="11"/> 
<Branch BRANCH_ROUTING_NBR="110029099" NAME="PNB Janpath Branch" 
STREET_ADDRESS="Janpath" CITY="NEW DELHI" STATE_PROVINCE ="DELHI" COUNTRY ="INDIA" 
POSTAL_ZIP_CODE="110002" BRANCH_NUMBER="099" NOTE=""> 
 
<Blockage FROM_DATE="09072006" TO_DATE="10072006" DESCRIPTION="Branch blocked due to 
system up-gradation" /> 
 
</Branch> 
</Bank> 
</ClearingHouseInterface > 
</ClearingHouse> 
<ItemReturnReason RETURN_REASON_CODE="01" DESCRIPTION="In-sufficient Funds"/> 
<ItemExtensionReason EXTENSION_REASON_CODE="04" DESCRIPTION="Bad image, paper requested"/> 
<Calendar CALENDAR_CODE="01" DESCRIPTION="Local Calendar"> 
<CalendarDetail CALENDAR_ID="23062006" DESCRIPTION="" VALID_WORK_DAY="0"/> 
</Calendar> 
<BundleCollectionType BUNDLE_COLLECTION_TYPE_CD="72" DESCRIPTION="Local Presentment Items" 
DISPLAY_NAME="LOCAL_PRESENTMENT" CLEARING_CYCLE_DURATION="1" 
MAX_ITEM_EXTENSION_DURATION="1" RTN_BUNDLE_COLLECTION_TYPE_CD="82" 
ITEM_AMOUNT_UPPER_LIMIT="999999999999999" ITEM_AMOUNT_LOWER_LIMIT="0" 
CLEARING_TYPE_CODE="02" CORE_COLLECTION_TYPE_CD="DR" DOCN_TYPE_IND_CODE="B"/> 
<SessionDefinition SESSION_NBR="1" DESCRIPTION="Local Session" VALID_MON="1" VALID_TUE="0" 
VALID_WED="0" VALID_THU="0" VALID_FRI="0" VALID_SAT="0" VALID_SUN="0" 
OPEN_RECEIVING_TIME="915" OPEN_RECEIVING_OFFSET_DAYS="0" CLOSE_RECEIVING_TIME="915" 
SESSION_OPERATION_MODE_CODE="P" CALENDAR_CODE="01" 
CLOSE_RECEIVING_RETURNS_OFFSET_DAYS="3" CLOSE_RECEIVING_RETURNS_TIME="2030" 
CURRENCY_CODE="SR" DO_SAME_SESSION_RETURNS ="1"> 
<SessionDefnCollectionType SESSION_NBR="1" BUNDLE_COLLECTION_TYPE_CD="72"/> 
</SessionDefinition> 
<TranslationRule PAYOR_BANK_ROUTING_NBR="110879" LOGICAL_ROUTING_NBR="110002987" 
FROM_DATE="20062006" TO_DATE="20082006" DESCRIPTION="ABC bank has been merged with SBI and all 
branches of ABC shall clear as SBI Branch No. 987"/> 
<TransactionCode CODE="10" DESCRIPTION="Savings Bank Account Cheque"/> 
<TransactionCode CODE="11" DESCRIPTION="Current Account cheque"/> 
<CityMaster CITYCODE="110" CITYNAME="DELHI" CLEARINGTYPE="01"/> 
<CityMaster CITYCODE="400" CITYNAME="MUMBAI" CLEARINGTYPE="03"/> 
<AtParBankMaster BANKCODE="002" CLEARINGTYPE="01"/> 
<AtParBankMaster BANKCODE="003" CLEARINGTYPE="01"/> 
</CHMasterBody> 
</CHMaster>

<!-- Page 167 -->

 
CTS Clearing House Interface – Specification 
 
 
167 
Appx 7 
Appendix CC – ClearingType 
The clearing types identified for the RBI/NPCI are as follows: 
NOTE: The ClearingTypes are set by the capture systems, along with the DocType to indicate the 
handling of the paper documents. 
 
Clearing Type 
Description 
 
DocType 
 
00 
Clearing Type is Unknown.  
This value is applicable for filename only (Appx 4.1.1), indicating, the file 
has mixed items with more than one clearing type in it. This value cannot 
be used at item level. 
 
 
LOCAL CHEQUES 
01 
Local Debit presentment – GOOD IQA 
“B” – Image To Follow 
without paper 
 
Local Debit presentment – BAD IQA 
“C” – Image To Follow with 
Paper To Follow 
 
Government debit presentment – GOOD 
IQA 
“B” – Image To Follow 
without Paper 
 
Government debit presentment – BAD IQA “C” – Image To Follow with 
Paper To Follow 
 
 
 
 
NON CTS 2010 CHEQUES 
11 
Local (NON CTS 2010 CHEQUES) Debit 
presentment – GOOD IQA 
“B” – Image To Follow 
without paper 
 
Local (NON CTS 2010 CHEQUES) Debit 
presentment – BAD IQA 
“C” – Image To Follow with 
Paper To Follow 
 
Government debit presentment – GOOD 
IQA 
“B” – Image To Follow 
without paper 
 
Government debit presentment – BAD IQA “C” – Image To Follow with 
Paper To Follow 
 
 
 
 
LOCAL HIGH VALUE CHEQUES 
02 
Local High Value Debit presentment – 
GOOD IQA 
“B” – Image To Follow 
without paper 
 
Local High value Debit presentment – BAD 
IQA 
 
 
“C” – Image To Follow with 
Paper To Follow 
 
High Value Government debit presentment 
– GOOD IQA 
 
High Value Government debit presentment 
– BAD IQA 
“B” – Image To Follow 
without paper  
 
“C” – Image To Follow with 
Paper To Follow 
 
 
 
INTERCITY CHEQUES 
03 
InterCity Debit presentment – GOOD IQA 
“B” – Image To Follow 
without paper 
 
InterCity Debit presentment – BAD IQA 
“C” – Image To Follow with 
Paper To Follow 
 
InterCity Government Debit presentment – “B” – Image To Follow

<!-- Page 168 -->

 
CTS Clearing House Interface – Specification 
 
 
168 
GOOD IQA  
 
without paper 
 
 
InterCity Government Debit presentment – 
BAD IQA  
 
“C” – Image To Follow with 
Paper To Follow 
 
Capture system has to identify the clearing type for each item in the capture file.  
Clearing type is also used in the capture exchange file name. If capture sorts items by clearing type, then 
it will use clearing type from the above table. If items are unsorted in capture then the value of clearing 
type in the filename is “00”. 
The capture system must ensure that items presented with a DocType of “C – Image To Follow with 
Paper to Follow” mode also follow the RBI/NPCI clearing house procedures for presenting and routing 
the physical cheque.

<!-- Page 169 -->

 
CTS Clearing House Interface – Specification 
 
 
169 
Appx 8 
Appendix DD – Return Reason Codes 
For RBI/NPCI, the return reason codes defined in section 4.6.3.3.1 are used. 
There are no additional RBI/NPCI specific return reason codes defined at this time.

<!-- Page 170 -->

 
CTS Clearing House Interface – Specification 
 
 
170 
Appx 9 
Appendix EE – IMAGE DETAIL SPECIFICATIONS 
RBI/NPCI has set their detailed image requirements that are necessary for smooth operation of all 
parties participating in the Clearing House. 
A1 
Each item shall have exactly three image views, as follows: 
 
B/W CCITT G4 TIFF images for front 
 
B/W CCITT G4 TIFF images for back 
 
Grayscale JPEG image compressed in JPEG format for front. 
 
B2 
The B/W TIFF images shall: 
 
be at 200 dpi 
 
follow the TIFF 6.0 standard.  
 
B3 
The grayscale images shall: 
 
JPEG images compressed in JPEG format (aka JFIF files) 
 
be a single frame, 8 bit Grayscale image (256 level) at 100 dpi 
 
The following subsections provide any necessary further clarifications and requirements for the image 
standards supported by the Clearing House System.

<!-- Page 171 -->

 
CTS Clearing House Interface – Specification 
 
 
171 
Appx 9.1 Required TIFF Tags for Black/White G4 Images  
 
 
Required Tags  
Tag 
Number  
Write 
Required 
Value(s) 
Comment 
A3 
ImageWidth 
256 
Note 2 
 
A4 
ImageLength 
257 
Note 2 
Note 1 
A5 
Compression 
259 
4  
4 = Group 4 Fax (T.6) 
A6 
Photometric 
Interpretation 
262 
0  
0 = White is zero 
 
A7 
StripOffsets 
273 
Note 2 
This array has only 1 entry (for single-strip images) 
A8 
Orientation 
274 
1 (new) 
3 and 4 
(grandfathered
) 
Tag may be absent if value = 1 (default). 
Transports are required to write images in orientation 1 (front 
and back) except for older transports that do not support 
orientation 1.  
A9 
RowsPerStrip 
278 
Note 2 
Note 1 
A10 
StripByteCounts 
279 
Note 2 
This array will have only one entry (for single-strip images).  
C11 
XResolution 
282 
200 dpi 
240 dpi 
 
XResolution value shall equal YResolution value. 
 
A12 
YResolution 
283 
200 dpi 
240 dpi 
Same comments as for XResolution 
The following tags need not be present since the default value equals the required value; However, if present, they shall 
have the default value. 
A13 
NewSubfileType 
254 
0  
0 = full resolution, single image per TIFF file  
A14 
BitsPerSample 
258 
1 
 
A15 
Thresholding 
263 
1 
1 = no dithering or halftoning has been applied to the image 
data 
A16 
FillOrder 
266 
1 
1 = pixels with lower column values are stored in the higher-
order bits of the byte 
A17 
SamplesPerPixel 
277 
1 
 
A18 
MinSampleValue 
280 
0 
 
A19 
MaxSampleValue 
281 
1 
 
A20 
PlanarConfiguratio
n 
284 
1 
1 = chunky format. The component values for each pixel are 
stored contiguously.  
A21 
T6 Options 
293 
0  
0 = no T6 options 
C22 
ResolutionUnit 
296 
2  
2 = inch  
 
A23 
Note 1 
This specification supports "single strip" images only which requires that the value of the 
"RowsPerStrip" tag is equal to the value of the "ImageLength" tag.  
A24 
Note 2 
This tag shall have a value that is valid for the associated image data.

<!-- Page 172 -->

 
CTS Clearing House Interface – Specification 
 
 
172 
Appx 9.2 Required TIFF Tags for Grayscale JPEG Images 
 
THIS IS NO LONGER PROVIDED.  RBI/NPCI DOES NOT SUPPORT JPEG IMAGES IN TIFF FILES. 
 
 
Appx 9.3 Extra TIFF Tags 
 
A1 
Extra tags are valid tags that are present in TIFF files and not included in the tables contained in 
sections 5.1.1 and 5.1.2. 
C2 
TIFF writers that create new TIFF images may create extra tags where there is a business 
reason to do so.  
A3 
If a TIFF writer inserts extra tags, it must make them syntactically correct and cannot demand 
that any other TIFF reader processes these extra tags. 
 
Appx 9.4 Private TIFF Tags 
 
A1 
Private tags are TIFF tags numbered 32768 or higher that are assigned to organizations that 
might wish to store information meaningful only to that organization. 
C2 
DELETED.  
A3 
If a TIFF writer inserts private tags, it must make them syntactically correct and cannot demand 
that any other TIFF reader processes these private tags.  
 
Appx 9.5 Support for other TIFF Parameters 
 
C1 
DELETED 
 
 
Parameter Name 
NCR Required Value (WRITE) 
Comment 
A3 
Byte Order 
Little-endian (II) 
Byte Order is defined in TIFF file bytes 0-1 
A4 
Sort Order 
The entries in an IFD must be sorted in 
ascending order by Tag.  
The Values to which directory entries 
point need not be in any particular order 
in the file.

<!-- Page 173 -->

 
CTS Clearing House Interface – Specification 
 
 
173 
Appx 9.6 Required JFIF Markers and tags for Grayscale JFIF Images 
 
C1 
JFIF image shall contain the JPEG Baseline Sequential Process 
C2 
JPEGs are assumed to be Orientation ‘1’ (left-to-right, top-to-bottom) 
C3 
JFIF requires the mandatory presence of the APP0 marker immediately after the SOI marker.  
The JFIF APP0 marker is identified by the zero terminated string “JFIF” 
C4 
JFIF APP0 marker provides the following information about the JPEG stream: 
 
‘version’ shall be ‘0101’ or ‘0102’ 
 
‘units’ for the X and Y pixel density, shall be either ‘1’ for dots-per-inch, or ‘2’ for dots-
per-cm 
 
‘Xdensity’ shall equal ‘Ydensity’ 
 
In the event that the APP0 ‘units’ or ‘density’ were not specified then the usual 
assumption by an application reading the JFIF will be 200dpiX200dpi 
 
Thumbnails are not mandatory, but if present are to be ignored

<!-- Page 174 -->

 
CTS Clearing House Interface – Specification 
 
 
174 
Appx 9.7  
Note - Calculation of Extensions and Returns 
 
Note Maximum duration for sending extensions denoted by 
MAX_DURATION_FOR_SNDNG_EXTNSN in BundleCollectionType element will start from 
Session Close time (SessionDefinition.CLOSE_RECEIVING_TIME) and will also include 
SessionExtensionHrs provided in PXF file. 
For example: Lets say for July 1 Session that closes at 1:00 PM if  
MAX_DURATION_FOR_SNDNG_EXTNSN is set as 2 hours and SessionExtensionHrs is 1 
hour, Drawee bank module has time till 1:00 PM + 2 hours + 1 hour i.e. 4:00 PM to send 
extensions to CHI.  
Note The calculation for maximum period for sending returns starts from Session Close time 
(SessionDefinition.CLOSE_RECEIVING_TIME) and will include SessionExtensionHrs and 
CLEARING_CYCLE_DURATION defined in BundleCollectionType element  
For example: Lets say for July 1 Session that closes at 1:00 PM if  
MAX_DURATION_FOR_SNDNG_EXTNSN is set as 3 hours and SessionExtensionHrs is 1 
hour, Drawee bank module has time till 1:00 PM + 3 hours + 1 hour i.e. 5:00 PM to send returns 
to CHI.

<!-- Page 175 -->

 
CTS Clearing House Interface – Specification 
 
 
175 
Appx 10 List of Paper to Follow (P2F) Items 
 
P2F Item(s) file notifies the bank of Paper to Follow items that have been processed at CHI and settled 
at CH on a business date. This file will be a comma separated value (csv) file generated at CHI by 
execution of a script. The file will be in the ascending order of Itemsequencenumber (ItemSeqNo). 
 
P2F Item(s) File will have the following naming convention: 
 
Appx 10.1 File Name Convention 
B1 
The P2F Item(s) file name shall use the following naming convention: 
 
P2F_nnnnnnnnn_<business_date>_ddmmyyyy_hhmmss.CSV 
 
Where: 
 
P2F  
Paper to Follow Item(s) File 
 
nnnnnnnnn 
Bank Routing Number (same as in File Summary Record) 
 
<business_date> The business date for which the file is generated 
 
ddmmyyyy 
Creation Date (same as in File Summary Record) 
 
hhmmss 
Creation Time (same as in File Summary Record) 
 
.CSV  
Is a mandatory file type suffix 
B2 
The value for the Bank Routing Number, Creation Date and Creation Time in the file name shall 
be the same as the contents of the File Summary record within the file. 
 
Appx 10.2 
File Structure 
B1 
The P2F Item(s) file shall contain one File Summary Record followed by one or more item detail 
Record. 
B2 
The structure of the file shall be: 
 
File Summary Record 
 
 
Item Record (for item 1) 
 
 
Item Record (for item 2) 
 
 
. 
 
 
. 
 
 
Item Record (for item n) 
 
B3 
Each record in the file shall contain alphanumeric data and will be terminated by a carriage return 
and line feed. 
B4 
The first line of the P2F Item(s) file shall always be the File Summary Record.  
B5 
 
The File Summary Record shall consist of data fields related to the entire P2F Item(s) file 
separated by commas. The data fields of File Summary Record are defined in Section 1.1.3.1. 
B6 
Item Records shall follow the File Summary Record. 
B7 
The Item Record shall consist of the data fields related to one item, separated by commas. All 
data fields of the Item Record are defined in Section 1.1.3.2.

<!-- Page 176 -->

 
CTS Clearing House Interface – Specification 
 
 
176 
Appx 10.3 Record Formats 
 
Appx 10.3.1 
File Summary Record 
 
B1 
Data fields of the File Summary Record shall be as described in the following table: 
 
Data Field Name 
Description/ 
Format 
Value (default) Type 
Size 
Usag
e 
Record type 
File Summary 
 
Shall be ‘FS’ 
A 
2 
M 
Creation date 
File creation 
date 
 
DATE 
8 
M 
Creation time 
File creation 
time 
 
TIME 
6 
M 
BusinessDate 
Business Date 
for which the 
list of items 
were 
generated.  
 
Shall be same 
as in the 
filename 
 
DATE 
8 
M 
Total Items 
The total 
number of 
items within the 
file 
 
N 
 8 
M 
Total Amount 
The sum of the 
value of all 
items within the 
file. 
 
N 
18 
M 
 
Appx 10.3.2 
Item Record 
 
Data Field Name 
Description/ Format 
Value (default) Type 
Size 
Usag
e 
Record type 
Item Record 
 
Shall be ‘I’ to 
indicate Item 
A 
2 
M 
ItemSeqNo* 
This is a unique identifier for 
the bank for a 
“PresentmentDate” 
 
NS 
14 
M 
PayorBankRoutNo 
Drawee Bank Routing 
number 
 
NS 
9 
M

<!-- Page 177 -->

 
CTS Clearing House Interface – Specification 
 
 
177 
Data Field Name 
Description/ Format 
Value (default) Type 
Size 
Usag
e 
Amount 
Check amount 
 
N 
18 
M 
AccountNo 
Drawee account number 
 
NS 
25 
O 
SerialNo 
Check number 
 
NS 
6 
M 
TransCode 
Transaction code 
 
NS 
3 
M 
PresentingBankRou
tNo* 
Routing number of the 
presenting bank 
 
NS 
9 
M 
PresentmentDate* 
Date of capture of checks  
 
 
DATE 
8 
M 
CycleNo* 
Capture cycle number. 
 
 
NS 
2 
M 
ItemType 
Indicates whether the item is 
outward(O) or inward(I) 
 
A 
1 
M
