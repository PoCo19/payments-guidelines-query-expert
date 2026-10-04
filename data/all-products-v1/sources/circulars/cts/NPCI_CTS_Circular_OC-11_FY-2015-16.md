# NPCI/2015-16/CTS/CIRCULAR NO. 11 - Circular No.11-Validations on return description field for reason code 88 - All

Circular/reference number: NPCI/2015-16/CTS/CircularNo.11

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2015-16/CTS/CircularNo.11
April09,2015
To,
AllthememberbanksofCTSclearing
Southern/Western/Northerngrids
RespectedMadam/Sir,
Sub:Return reason88-Others-Validationsofdescriptionfield
Uniform Rules and Regulations for Bankers Clearing House (URRBCH),provides for the list of
reasons that can be used by participating banks for returns. One of such reason codes is 88 -
"Others". This reason is expected to be used only under exceptional circumstances wherein
provides for a free text field for the banks when they select the return reason code 88 -
Others.Thisfieldcanaccommodateupto25characters.
It is observed that banks while choosing this reason are not providing meaningful text in the
editable filed so that the presenting bank can communicate such reason to their customers.
Further there are instances of special characters are being used in the text field. To
overcome this issue and as part of quality initiative, system changes will be done to make
input in the text filed mandatory, also the system will not accept a set of special characters.
Thetechnical specifications areprovidedinAnnexurel.
The system will validate the other reasons description, if the input is invalid or contains the
special characters that are black listed then rejects such records at CHi itself. Bank has to
rectify and reprocess such rejected cases to ensure the returns are passed through the
appropriatesession.
The new validations on the return description field for reason code 88 (other reasons) will be
implemented by May 2015.The exact go live date will be communicated shortly.Member
banks are requested to take a note of the new validations and do necessary changes in the
capture system.
Incaseof anyclarifications,pleasefeel freetowritetous.
With Warm Regards,
(GiridharG.M)
VP&HeadCTSandNACHOperations
-9.8
C-9.8thFloor m/Phone:02226573150
RBi Premises /Fax:02226571001
Bandra-Kura Complex 专-ta1email:contac@npdi.org.in
BandraEast
-400051 turs/Website:www.npdi.org.in
Mumbai400051
CINU74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure1
Technical specificationon return description fieldfor reason code 88
1.Minimumrequirements
a.Contain minimum 6charactersand maximum of 25 characters
b. Necessary to give the reason in the text field as it will be mandatory at both Ul
andtheRRFfilesupload
2.Thefield should not
a.Containonlynumbers
b.Start with a numberhowever it can have numbers in between
Containonlyspaces
d。 Startwithspace
Containonlythephrase“"otherreason"
f.Containrepetitivespecialcharacters
3.Thebelowspecial characterswillnotbeallowed
a. Less than symbol - (<)
b. Greater than symbol - (>)
c.Ampersand-(&t)
d.Apostrophe-(")
e.Doubleapostrophe_(")
