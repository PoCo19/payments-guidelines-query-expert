# Circular No.190 Legacy mandate amendment Image format specification

Circular/reference number: NPCI/2016-17/NACH/Circular

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTS CORPORATIONOFINDIA
NPCI/2016-17/NACH/Circular No.190 October03,2016
To,
AllNACHmemberbanks
Legacymandateamendment-Imageformat specification
Refer to NPCl Circular No.180 on “Migration of ECS 156 format to ACH format". As per the
circular the member banks and corporates should first upload the data mandates and
amendment carried out for uploading the image for attaching to data mandate will be
auto accepted. The image format specification is provided in Annexure l.
The old Ecs mandate not being in standard size (often it is of A4 size) it may not be
possible for the banks to see the image by clicking on the icon in MMS GUl, image can be
viewed only afterdownloading the imageto the local disk.
Member Banks are advised to take note and disseminate the instructions contained herein
to all the concerned.
Forany clarifications please write back to ach@npci.org.in
With warm regards,
(GiridharGM)
VP & Head - NACH & CTS Operations
1001A,The Capital, BWing,10th Floor,Bandra Kurla Complex, Bandra (E).Mumbai 400 051.T:+9122 40009100 F:+9122 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
AnnexureI
Legacy Mandate Amendment Specification for Image Upload
Mandate Amendment through Front and XML file upload.
Response files will be generated to Receiver and sender respectively.
As part of Legacy Mandate Amendment, banks will be able to upload only legacy
mandates images and will not be able to amend any other fields (lncluding the
Mandate request ID).
While uploading amendment zip file for legacy mandate by modifying any of the
input fields other than image, ack file with reject reason “Amending <<Modified
field>> is not allowed for legacy mandates" will be sent to the user.
Member banks can use Mms front end for legacy mandate amendment, however the
bank can amend one mandate record at a time. Using XML file upload, banks can
raise bulk amendment request of 100 mandates in a Zip file.
Initiation of legacymandate amendment request will be continued as per the current XML
Mandate format using pain 010 Format.
Front Black&WhiteImage
The Image should be in black & white.
The Image should be in TIFFFormat
DPI for the Image is 200
The size of each image should not exceed 100 Kb
Front Grayscale Image
The Image should be in grayscale
The image should be in JPEG Format
DPifor the Image should be 100
The size of each image should not exceed 100 Kb
Note-For TiFF images,thebrowser needs to be compatible toview these images onto the
screen.
1001A,The Capital.B Wing.10th Floor,Bandra Kurla Complex, Bandra (E).Mumbai 400 051.T:+9122 40009100 F:+9122 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067
