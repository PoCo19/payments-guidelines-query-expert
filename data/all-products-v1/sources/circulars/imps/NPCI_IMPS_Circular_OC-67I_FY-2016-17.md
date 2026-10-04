# IMPS I OC 67 I FY 15-16 I Migration from DMS to RGCS w.e.f 27th Feb 2016

Circular/reference number: OC-67I

<!-- Page 1 -->

N?Cl 
mv-fhr  T7cTR f.'rT,-r 
NATIONAL PA'rMENTS CORPORATION OF /NOIA 
NPCI/IMPS/OC No 67/2015-16 
Feb 17, 2016 
To, 
All Members of IMPS (Immediate Payment Service) 
Dear Sir/Madam, 
Sub: IMPS Operations Process -
Migration from OMS to RGCS w.e.f. 27th Feb 2016 
Presently, all IMPS members are accessing OMS application for IMPS related operational activities (viz. 
clearing & settlement, dispute management, downloading settlement files, reports, raising disputes, 
service tax reports, etc.}. 
We are pleased to inform that NPCI will be migrating from DMS to RGCS w.e.f. 27th Feb 2016. 
After migrating from OMS to RGCS (scheduled on 27th Feb 2016), NPCI will decommission the IMPS OMS. 
Since raw data and other settlement file formats are same in RGCS, there should not be any impact in 
reconciliation process. 
Training to all IMPS members 
. 
NPCI has given training on RGCS to all IMPS members with demo on test system. There are no changes 
required at bank end because RGCS has been developed similar to DMS and file formats for all settlement 
reports and adjustments are same. 
RGCS user manual has been sent to all participants who have attended RGCS training program and the 
same has also been uploaded in OMS application (Service tax folder}. 
Changes between OMS & RGCS (IMPORTANT) 
A.
Admin Access: In OMS, admin access for the bank is with NPCI. In RGCS, NPCI will give one admin
access which will allow banks to create, modify, delete, user ID & reset or create password.
B.
Maker & Checker Concept: There is no maker & checker concept in OMS. RGCS has Maker &
Checker Concept - Refer note 1 below.
C.
Encryption of bulk file: In OMS, bulk file is not having encryption option. In RGCS, bulk file has to
be encrypted using PGP tool as mandatory process (PGP tool has been uploaded in OMS under
service tax menu} - Refer note 2 below.
Once we migrate the settlement & dispute management process from OMS to RGCS, following are the 
benefits:-
•
Increased processing speed.
•
Members will be provided with admin IDs. Admin can create/delete user IDs and reset the
passwords.
Members can view transaction and corresponding adjustments (if any} in single window.
B 
. 
40(.' 
Page No - 1/4 
N 
9 1M lO SM L 
0

<!-- Page 2 -->



<!-- Page 3 -->

Process to connect NPCI IMPS RGCS Application 
A.
How to access IMPS RGCS
N?C/ 
"fmfr,;,- ?7-.;,!tzr '!.f7@T'f  
NATIONAL PAYMENTS CORPORATION OF IND/A 
Annexure-1 
For accessing IMPS RGCS, members has to use the below given RGCS URL/link 
https://192.168.171.6/RGCSIMPS/ 
Currently banks are using below link to access DMS application 
https://192.168.171.6/ 
NPCI WILL PROVIDE ADMIN USER ID THROUGH E-MAIL AND PASSWORD IN SEPARATE E-MAIL. IMPS 
MEMBERS HAS TO LOGIN IN TO RGCS USING ADMIN USER ID. ONCE ADMIN LOGS IN TO RGCS 
SUCCESSFULLY, ADMIN HAS TO CREATE MAKER & CHECKER USER ID & PASSWORDS. MAKER & CHECKER 
HAS TO LOGIN TO RGCS. KINDLY KEEP NPCI INFORMED ON CREATION OF IDs & PASSWORDS. 
B. System Requirements for accessing IMPS RGCS
RGCS IMPS is a web-based application that can be used on any desktop having following specifications: 
RAM 
Minimum 1 GB RAM 
Operating 
Microsoft Windows 2003 onwards 
System 
Supported 
Microsoft Internet Explorer 7.0 or upper. If you are using an older browser, some aspects 
Browser 
of the RGCS IMPS site may not function properly. 
Screen 
To make best use of RGCS IMPS, we recommend a monitor of 1024x768 pixels or greater, 
Resolution 
and 32 bit colour or greater. 
JavaScript 
JavaScript is used in RGCS IMPS to enhance the user experience and provide advanced 
functionality. RGCS IMPS requires that Java is installed and turned on. 
Cookies 
RGCS IMPS application requires cookies enabled within your browser. 
Pop-up 
RGCS IMPS uses 'pop-up' windows to display some content. If you are using a browser that 
Control 
offers pop-up control or are running an add-on program to control pop-ups, you may need 
to take steps to allow pop-ups for this site. 
C.
Accessing RGCS application
Banks can start accessing RGCS application using existing PCs which are used to access DMS
(Please enter the RGCS URL instead of DMS). This does not required any changes at bank/PP ls end.
D.
Download Public & Private keys
NPCI has placed public & private keys in DMS portal in service tax folder for accessing RGCS
application, please download the same from DMS and connect to RGCS.
Page No - 3/4

<!-- Page 4 -->

E.
RGCS User Manual
RGCS User Manual document has been uploaded in DMS. This can downloaded from DMS under 
service tax menu. 
F.
PGP Tool
Banks have to download the PGP tool from DMS application (from service tax folder) and save it on 
your PC to encrypt the bulk adjustment file (.CSV) before uploading in RGCS. 
G. Public & Private Key:
This is one time activity where IMPS members has to save the folder in any of the desire drive in 
computer (example: C drive/D drive etc.). 
Steps to be performed for setting up PGP encryption tool on PC are as follows, 
1.
Copy and paste the zip file in the desired location
2.
Unzip the file
3.
Enter password (NPCI will provide password through e-mail)
4.
Select location to extract and store the unzip file
5.
Open and double click the PGPEncryption.exe file and follow the instructions as prompted.
PRE REQUISITES TO ACCESS RGCS 
IMPS Members should ensure to implement below specified software 
to access RGCS as mandatory process 
S. No 
List of Software 
1 
Silver light 4.1.1.329 and above 
2 
.Net Framework 4.0 and above 
3 
Internet Explorer Version 7 and above 
H. Process for downloading RGCS user manual/RGCS PPT / Process manual to integrate RGCS -
Public and Private Keys/ PGP encryption tool:
PROCECSS FLOW FOR DOWNLOADING FILES 
DOWNLOAD 
CLICK SERVICE 
.ZIP FILES 
LOGIN DMS 
. 
CLICK FILES 
. 
TAX REPORT 
SAVE IT 
ON YOUR PC 
Page No - 4/4
