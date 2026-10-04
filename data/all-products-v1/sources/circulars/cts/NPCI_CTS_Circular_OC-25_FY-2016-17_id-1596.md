# NPCI/2015-16/CTS/Circular No.25 - Circular No. 25-Release of New Specification Doc Version 2.4 - All

Circular/reference number: NPCI/2015-16/CTS/CircularNo.25

<!-- Page 1 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2015-16/CTS/CircularNo.25 March09,2016
To，
AllCTSMemberBanks
ReleaseofNewspecificationdocumentversion2.4
As part of the CTS system improvement, there various changes is getting introduced and the following are the
1.Govt.ChequeValidations
2.MICRRepairFlagValidations
3. Return reason description made mandatory for reason code : 88 (Others)
presented with the Schema 010005 only. For the benefit all member banks the new schema 010005 will be
made mandatory with effect from April 01, 2016. The new schema is deployed in CH and CHl with effect from
March 01, 2016 and system will accept both old and new schemas till April 30, 2016.
The summary of changes enclosed in the Annexure I. Updated CHl specification (version 2.4) is also enclosed
alongwiththiscircular.
All the member banks are advised to take a note of the same and do necessary changes accordingly.
Thanks&Regards
GiridharGM
VP&HeadOperations-CTS&NACH
1001A, The Capital,BWing,10th Floor, Bandra Kurla Complex, Bandra (E),Mumbai 400051.T:+912240009100 F:+912240009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure l:
SI. CHI Spec Detail Changes
No. Section
Section Government Cheque validation: Document type C validation exists only for the
3.7.1 This validation ensures that if transaction code 20.The validation for the codes 21-27
the cheque is a government &49areremoved.
cheque, it should be processed
as“lmage ToFollowwithPaper
To Follow".
Section 8.b Report of items detected as IQA Report will continue as it is, based on Document type C
(CHI) andGovernmentcheques
Contains the list of government
cheques and IQA failure cheques
Section 8.h New report-"SANValidation Cheque details on SAN validation rejected items
(CHI) Report"contains item details available in this report. As such this is an optional field
which got rejected due to short only.
account validationfailures
Appx New Reject reason codes Reject reason Code - 34 - Payor Branch not available in
4.3.10.3.3.1 introduced BOFDcityforP2Finstruments.
Reject reason Code - 35 - Item failed with return reason
comment validation for cheques returned with reason
code 88 (other reason).
Reject reason description Reject reason code 15 - These items were rejected as
updated Account Number is Invalid or Invalid Documentation
Type for government cheque.
Reject reason code 27 - These items were rejected as
they failed Government Cheque validation.Please refer
the latest version of CH Master file and CHI
Specificationfordetails.
Appx Newschemaintroduced to for
4.1.3.1 File enable new validations onMiCR CXF from 010003 to 010005
header Repair Flags attribute of item RRF from 010003 to 010004
element. ERFfrom010003to010005

<!-- Page 3 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Appx 7 digit account number and a 3 Document type Cvalidation exists only for the
4.1.3.3 Item digittrancode. transaction code 20.The validation for the codes 21-27
& 49 are removed.
Example1234567and987from
the MiCR line are formed into
the account number 1234567,
and trancode 987.
6 digit account number and
trancode in the range 20-27.
Example876543and21fromthe
MICR line are formed into the
account number 876543, and
trancode 21
.AccountNumbervalueshallbe a. SAN and Trancode validation added i.e. system will
mandatory 6 digits for 2 digits validate whether appropriate digits of short account
Transcode.ExampleSAN123456 number (SAN) was provided. For example if 2 digit tran
and Transcode78 is valid code selected then system will expect the 6 digit SAN
scenario. else system will reject the same. In case of 3 digit tran
code system will look for the 7 digit SAN. Earlier this
·AccountNumbervalueshallbe validationwas not available.
mandatory 7 digits for 3 digits
Transcode.Example SAN b. SAN will be kept optional till further communication.
1234567 and Transcode 890 is It canbe leftblank howeverif theSAN isgiventhenthe
valid scenario. same should subjected to the validation detailed in
point a above.
Attribute name -MICR Repair Flags to be set if the read code line has been
Flags corrected.
‘xxxxy1': if any field of the code line is corrected.
‘xxxx9x':if Account is new
‘xxxx5x':if old account
‘xxx1y1': if transaction code is repaired
‘xx1xy1':if account code is repaired
‘x1xxy1': if sort code is repaired
“1xxxy1': if serial number is repaired
y :could be“0'or“9'or“5"
