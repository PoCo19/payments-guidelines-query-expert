# NPCI 2015-16/CTS/Circular no. 52 - CPPS-Circular on Concept Note - All

Circular/reference number: NPCI/2015-16/CTS/052

<!-- Page 1 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2015-16/CTS/052 September 08, 2015
To
AllCTSMemberBanks
CPPS:CentralisedPositivePaySystem
Dear Sir/Madam,
Positive Pay is an automated system where the customers and banks can upload the
details of the cheques/instruments issued by them. This database will be used to verify
the credentials of instruments at the time of processing the instruments through CTs
payee name, amount, and date of the instrument. This will be the centralized system,
which will be available for the banks. Banks should collate the data from their retail and
corporate customers and upload the same into CPpS.
A separate working group comprising of 6 banks was formed to deliberate and finalize
implementing CPPS.A high level process flow document (Annexure I) is attached.
The system will be made available to the members on cost sharing basis. The cost sharing
detailsareasfollows
SI. No Category Inward(Average Onetimecost(lncluding5years
monthly volume) maintenance)
Large Banks 5 Lakhs and above Rs.10Lakhs
OtherBanks Below 5 lakhs Rs.5Lakhs
As this is a system for the banks, we seek your feedback on your willingness to make use of
this system as per the process and criteria detailed above. You are advised to submit, in
writing, your willingness/unwillingness to join the system before September 30, 2015.
Based on the feedback received from the member banks NPCl will decide on further
course of action.
Yourresponseon letter head may pleasebe sent toouraddressgivenbelow.
Addressfor despatchingtheoriginal letters
National Payments Corporation of india, VBC Solitaire, 8th Floor, No. 47 & 49, Bazullah
Road, T. Nagar, Chennai - 600 017.
Scanned copy of the letter be sent to the email ids given below
KSakthi.Krishnan@npci.org.in
ganesh.a@npci.org.in
Yours faithfully,
GiridharGM
α fc(YP & Head Operations - CTS and NACH),
The'Capital, rHTT/Phone:02240009100
1001 Unit No.1001A, B Wing, /Fax:02240009101
10,-70 10thFloor,PlotNo.C-70, 专-/email:contact@npci.org.in
GBlock,BandraKurlaComplex, aarc/Website:www.npci.org.in
Bandra (E),Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
CentralizedPositivePaySystem(CPPS)conceptnote
CPpS is a platform for the member banks and their customer (Corporate & Retail) for
notifying or uploading the details of the cheques issued. A separate application will be
created which can be accessed via internet for member banks, corporates and retailers.
ThissystemwillbecommonforallGRIDs.
Process
1. Customers after issuance of cheques will provide the detail of the instruments so
various modes like internet banking, direct file upload.Necessary authentication
process will be followed by the banks. The data so received will be uploaded in to
CPpS system by the banks through an APl or any other mechanism as may be
decided.
2. The file uploaded will be validated for syntax and whether all mandatory fields are
present. If mandatory field/s is/are not available then the file will be rejected.
3. Addition/ modification/ deletion of records in CPPs can be done by the customer
through their bank if the instruments are not cleared already.
4. After validation, the data will be updated in the CPPS database.
5. The cheques presented by the banks will be validated against the CPPS data base in
either of the following methods
a. During the session when the files are presented by the banks, the system
apart from othervalidations will perform CPpS validations.
b. Post completion of the session, system will do the CPPS validations.
6. System will provide the CPpS updated data in either of the following two ways
a. If online validation is performed during the session then a new flag will be
enabledinthefileformattoindicateCPPSstatus.
b. if the processing is done in batch mode, post session completion and inward
generation then a separate instrument wise report will be generated with
CPPS status.
7.The following can be the flags
a. Exact match found
b.Partial match found
C.RelevantdatanotavailableinCPPs
(Separate technical specification document will be shared with member
banks)
confirmations from the customer on the issuance of the instruments.
9. The return and the re-presentation of the CPps enabled instruments will also be
flagged in CPPs. This will enable member banks to be more cautious during the
time of presenting or paying the instrument.
The Capital, HTqT / Phone: 022 4000 9100
1001 Unit No.1001A, B Wing, q/Fax:02240009101
10th Floor, Plot No.C-70, 专-/email: contact@npci.org.in
GBlock,BandraKurlaComplex, q专/Website:www.npci.org.in
Bandra(E),Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
DOWNLOADFILE
CORPORATE CHEQUE SSUANCE FRE
The
Clearing
House CHEQUESSUANCE FLE
CHECUJEGSUANCE
UPLOAD
CHECUE GSUANCE FILE
VERIFICATIONI
VALIDATION OFFILE
Features
User creations
1. There will be provision for user creation. End customer from whom the data is
being received will be authenticated by their bankers using their own internal
mechanism.
Data upload
1. There will be interface for the banks for updating the instrument details. System
shall accept CSV file and XML format for upload for inputs.
2.Options tofacilitate upload/download/update/delete of data will be available
3.Therewill be a filed identifierforAddition/Modification/Deletion of records.
Data field
The input filewill containthefollowingfields
AccountNumber
2. ChequeNumber
3. cheque date
4. Amount
5. DraweeBankName
6. DraweeBankCode (all9digitstobeaccepted)
7. Payee Name.
8. Transaction code
Validations
1.The Drawee bank code will be validated against the masters (both 3 digit as well as
6 digit regional MICR codes).
2.File validation will be available for syntax and mandatoryfields.
3.Following itemvalidationsshall becarriedout:
a. Duplicate instruments.
b. Drawee bank code shall be validated against the masters (both 3 and 6
digits)
C. Already paid items
TheCapital, FHTT/Phone:02240009100
1001 Unit No. 1001A, B Wing, qT/Fax:02240009101
104.-70 10thFloor,Plot No.C-70, 专-/email:contact@npci.org.in
GBlock,BandraKurlaComplex, aac/Website:www.npci.org.in
Bandra (E),Mumbai400051
CIN:U74990MH2008NPL189067

<!-- Page 4 -->

NPCI
d. Present of data in Mandatory Fields
e.Stale cheque
Reports
Reportswill bemadeavailableto thebanks.
AdvantagesofCPPS
1. As CPpS proposed to be a central system provided by NPCl, banks need not bother
about system maintenance, DR etc.
2. This will provide an opportunity to the presenting bank to get the details of the
instruments they are presenting (if available in CPpS) thereby mitigate the risk of
fraud before the payment is released
3. If the customers can provide the details, the banks will have advantage of having
additional information in place for cross verification before paying the instruments.
4. Beneficial to the smaller banks who cannot afford to invest and lack in technical
skills to build such systems.
TheCapital, PHrT/Phone:02240009100
1001 Unit No.1001A,BWing, /Fax:02240009101
1070 10th Floor, Plot No.C-70, -/email:contact@npci.org.in
GBlock,BandraKurlaComplex, aq/Website:www.npci.org.in
400051 Bandra(E),Mumbai400051
CIN：U74990MH2008NPL189067
