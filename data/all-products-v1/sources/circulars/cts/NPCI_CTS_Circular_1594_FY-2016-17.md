# NPCI 2015-16/CTS/23 - Changes in MICR Repair Flag and Other Reason - All

Circular/reference number: NPCI/2015-16/CTS/CircularNo.23

<!-- Page 1 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2015-16/CTS/CircularNo.23 January14,2016
MemberbanksparticipatinginallGrids
CTSClearing:ChangesinMICRRepairFlag&OtherReason
Madam/ DearSir,
Refer to our circular dated October 7, 2014 (Ref NPCI/2014-15/CTS/036) on the MICR Rejects,
weareintheprocessofdevelopingthefollowingvalidations
1.MICRrepairflag
2.Returnreasoncomment incaseof otherreasons‘88'
The above said changes will require modification in the Capture system used by the member
functionalities are expected to go live by February 15th, 2016. The exact date of going live will
beintimated separately.
Member banks are advised initiate necessary changes at their end.
WithWarmRegards,
(GiridharGM)
VP&Head-NACH&CTSOperations
1001A, The Capital, B Wing,10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051. T:+91 22 40009100 F:+9122 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
AnnexureI-MICRRejectRepairflag
MICR Repair flag will be of 6 digits.Last digit of the MICR repair flag indicates if the MICR has
been corrected or not. Value ‘1' in last digit indicates that correction has been done in MiCR
while value ‘o' indicates that there is no correction made in MICR. 5th digit of the flag can
either have value 'o' or '5' or 'g'. The values of 5th digit will not be linked to the last digit
validation. Earlier 5th digit was used for amount field correction, now value in 5th digit will be
used to indicate the account status (O-not verified the status of account by bank, 5-Old
account, 9-New account).
1. Following are validations carried out in the MICR RepairFlags field.
Value of the first 4 digits and the sixth digit should be either '0' or'1'
Value of the fifth digit should be either'o'or'5'or'9'
(Note:Memberbanks are advisedtokeep thefunctionality ready and not enable
the same until confirmed by NPCl. In the interim banks should continue to send the
valueas‘o'bydefault)
If the last digit is 'o', then none of the first 4 digits should be'1'
If the last digit is '1', then at least one or more value of first 4 digits should have
value'1'
Fewexamplesare:
Valid values - 010001, 000101, 001001,100001,000191, 010091, 001091,100091,
000090,000000,000151,010051,001051,100051,000050
Invalidvalues-000001,100000,001000,000100,000010,000091,100090,001090,
000190,100010,010000,010090,010020
2. The validation shall be for element MICR Repair Flags in CXF.
3. The validation shall be carried out during CXF loading.
4. Files failing with MICR Repair Flags validation shall be rejected with File Format Error
andRejectreason2
5. The validation shall be carried out on only presentment files.
1001A, The Capital, B Wing,10thFloor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051.T:+9122 40009100 F:+9122 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NATIONALPAYMENTSCORPORATIONOFINDIA
Annexurell-Returnreasoncode:88 (Others)-Reasoncommentfieldwillbemade
mandatory
Introduction: Presenting bank CHl shall receive the return exchange file/s for each return
session containing returns on the presentation lodged by them. As per system design, a return
session may not necessarily have a direct one-to-one corresponding relationship to any
particular presentation session. An item may be returned as long as its clearing length has not
expired, and a session is available for the particular clearing type. The return file shall contain
the item detail and return reason code. It shall be the responsibility of the presenting bank to
generate the return memo from the information in the return file.
Approach is to make Return description to be mandatory for Return reason code 88,
currentlythisfieldisan optional field.
TechnicalApproach:
1. New parameter shall be introduced to enable validation of"Reason comment"field in
DraweeBranchmoduleUl
2. New validation shall be added on User Interface of Drawee Branch module to validate
enteredvaluesin"ReasonComment"field.
3.The newvalidation shall only be considered if theReturn Reason code entered is 88.
4.Special CharacterValidation will beas per theRTGs list
5.There shall be a new item level reject reason7/35introduced to handle rejected items
withspecialcharactervalidationfailures.
6. The response files with rejected items shall be created in ftproot folder
7. In case of return reason "88" Below validations shall be carried out in the return reason
comment field
a.ReturnReasonCommentshallnotbeempty
b.Thevalue shall not start withnumber
C. The value shall not start with space or contain only space
d. The value shall not have the word “other reason"
e.Special characters< &>""shall not be accepted
f. The value shall be minimum of six characters and maximum of 25 characters
g.Repetitive special characters shall not beallowed
AdditionalFeatures:
1. Mandatory should be applicable for both Front end of CH/CHI and RRF files received
fromCHI.
2. CHUl should have maker/checker functionality.
1001A, The Capital, B Wing,10th Floor, Bandra Kurla Complex, Bandra (E),Mumbai 400 051.T:+9122 40009100 F:+912240009101 www.npci.org.in
CIN:U74990MH2008NPL189067
