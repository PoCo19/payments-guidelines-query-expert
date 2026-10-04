# NFS OC 69 Standards for correct identificationof ATM location

Circular/reference number: NPCI/NFS/OCNo69/2012-13

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NFS/OCNo69/2012-13 August 07, 2012
To
All MemberBanksofNational FinancialSwitch(NFS)
DearSir/Madam,
StandardsforcorrectidentificationofATM location
Please refer to our earlier letter dated 12th Jan, 2012 with reference no NPCI/2011-12/NFS/2102,
wherein we have stated that the ATM Details in field Data Element(DE) 43 has to be populated by
sending the full ATM location in this Data element. However it has been observed as follows as
regardstocontentsinfieldDE43
1.The Country Code & the City is not populated by some of the member banks.
2. Even if the city name is populated, the same (City name)is populated differently by different
Banks.For instance, Mumbai is populated as MUM, BOMBAY,and GREATERBOMBAY.
3.  Many banks are providing full name of their bank to fill the entire 4o characters, though a
separate field"ACQUIRER ID"(DE32)is already availablefor thepurposeand on thebasis of
which bank name can also be determined.
4. Many banks are providing random numbers in this field without the location.
It has therefore, been decided in the NFs Steering committee meeting held on 16/05/2012 NPCl
would propose and lay down standards for correct identification of ATM location, proper generation
of MIS.
Discussions were held with major switch vendors to evaluate the feasibility of standardisation on DE
41, DE 43, and sending Pin code in online message. These message specifications were finalized in
NFS technical group meeting held on 1ith July, 2012.
NPClis thereforeproposing asfollows:
1.DE43shouldincludeasfollows:
Position Length Field Name Description
01-23 23 TerminalAddress ATMAddressalongwithTalukanameasallocatedby
General PostOffice(GPO).
24-36 13 Terminal city DistrictNameshouldbepopulatedasallocated byGPo.
37-38 Terminalstate Statecodeshould bepopulatedasperAnnexurel.
39-40 Terminal country Countrycodeshould beprovided asperIso standards.
'IN'fordomestictransactions.
Page 1 of 2
C-9,8thFloor pTqT/Phone:02226573150
RBIPremises q/Fax:02226571001
Bandra-KurlaComplex 专/email:contact@npci.org.in
Bandra East aasc/Website:www.npci.org.in
400051 Mumbai400051

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
2.Pin code needs to be populated in DE-61 along with some other information as detailed in
Annexure-ll.
It is also observed that some Banks have more than 8 digits terminal id. The Banks that have more
than 8 digit terminal ids should populate it in DE42, in addition to DE41. In other words terminal ID
Would be populated inboth DE41 and DE42(DE41length is 8 characters andDE42length is 15
characters at NPCI end).
The sampledata forDE-43and DE-61of fiveATM locations isgiven inAnnexure-lll.
The standardization of the above mentioned Data Elements would be useful in getting complete
accurate data which in turn would be helpful for better Fraud management.
Depending on the quality of data sent, for a particular member Bank, NPCl will apply compliance
(after intimating and getting approval from member Bank), which will decline the transactions in
case Pin code, Statecode and Countrycodeare not populated with valid values.
After the changes are carried out at your end, the following officials can be contacted to carry out
UAT beforemovingthechanges on productionenvironment.
1.ShriAppala Reddyareddy@npci.org.in,MobileNo:09790932030
2. Shri Sumit Kashyap sumit.kashyap@npci.org.in, Mobile No:08108122872
Withkindregards
SM.Nala
SMNabar
Head - Technology
M:+918108108664
Enclosures:
1.Annexure-l(StateCodes)
2. Annexure-ll(DetailedspecificationofDE-61)
3.Annexure-Ill (SampledataforDE-43andDE-61)
Page 2 of 2
C-9,8thFloor pTqT/Phone:02226573150
RBIPremises hq/Fax:02226571001
Bandra-Kurla Conpiex -/email:contact@npci.org.in
Bandra East aawc/Website:www.npci.org.in
-400051 Mumbai400051

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure l
Two Letter Codefor State Names in India
State Two-letter Code
Andhra Pradesh AP
Arunachal Pradesh AR
Assam AS
Bihar BR
Chhattisgarh CG
Delhi DL
Goa GA
Gujarat GJ
Haryana HR
HimachalPradesh HP
Jammu&Kashmir JK
Jharkhand JH
Karnataka KA
Kerala KL
Madhya Pradesh MP
Maharashtra MH
Manipur MN
Meghalaya ML
Mizoram MZ
Nagaland
Orissa OR
Punjab PB
Rajasthan RJ
Sikkim SK
Tamil Nadu TN
Tripura TR
Uttarakhand
UK
(FormerlyUttaranchal)
UttarPradesh
WestBengal WB
Andaman&Nicobar AN
Chandigarh CH
DadraandNagarHaveli DN
Daman&Diu DD
Lakshadweep LD
Pondicherry PY
Page 1 of 1

<!-- Page 4 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure ll
DE61Format
DE-61PoSDataCode
Type ans...999
Format LLLVAR
Description This determinesthedatainputcapability
Subfield1:CardDataInputCapability
Value Description
Unknown
1 * Magnetic StripeRead capability
ICCCapability
Magneticstripeandkeyentrycapability
MagneticstripeandICCcapability
Manual, no terminal
Keyentered
Subfield2:CardholderAuthentication Capability
Value Description
Unknown
Noelectronicauthentication
2* PIN
Biometric
Subfield3:CardCaptureCapability
Value Description
0* Unknown
1* No capture capability
2* Capture Capability
Subfield4:TerminalOperatingEnvironment
Value Description
0* Unknown
Onpremisesofcardacceptor,attended
2* On premises of card acceptor,
unattended
Offpremisesofcard acceptor,attended
4* Off premises of card acceptor,
unattended
Onpremises ofcardholder,unattended
No terminal used
Subfield5:CardholderPresentData
Value Description
Unknown
1* Cardholderpresent
Cardholdernotpresent,unspecified
reason
Cardholder notpresent,Mail
Page1of4

<!-- Page 5 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
transaction
Cardholdernot present, telephone
transaction
Cardholder not present, standing
instruction
E-Commercetransaction
IVRtransaction
Subfield6:CardPresentData
Value Description
Unknown
Card not present
2 * CardPresent
Subfield7:CardDataInputMode
Value Description
Unknown
Manual Input, noterminal
2 * Magnetic Stripe read
OnlineChip
Offlinechip
Ecommerce
IVR
Key entered
Subfield 8:CardholderAuthentication method
Value Description
Unknown
Not authenticated
2* PIN
Signature
Biometric
OTP
E-CommerceType1Pin
E-CommerceType1OTP
E-com Type 2
IVR Type 2
Subfield 9: Cardholder Authentication Entity
Value Description
0* Unknown
ICC
CAD
Type3 (3D if issueropted forICs1
services)
Type4 (3D if issueroptedforICS2
services)
Type1(RuPayE-Commerce
Implementation)
Type2(3DifissueroptedforRuPay
Page 2 of 4

<!-- Page 6 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
services)
Subfield 10:Card Data Output Capability
Value Description
0* None
MagneticStripewrite
ICCWrite
Subfield11:Terminal Data Output Capability
Value Description
Unknown
Print capability
DisplayCapability
3* Printand Display Capability
Subfield12:PINCapturecapability
Value Description
NoPINcapturecapabilityl
4charsmaximum
5chars maximum
3* 6charsmaximum
7 charsmaximum
8charsmaximum
9 chars maximum
10charsmaximum
11charsmaximum
12charsmaximum
Subfield13-21:ZipCode
Sr No. ZipCode
1* Merchant Postal Code :ans 9, Left
padded with zeroes
If zip code contains all zeroes/all spaces
then the transaction will get rejected
Subfield22-41:POSAdditionalMerchantAddressdata
Sr No. AdditionalAddressdata
Address/merchant
telephone/mobile number
Ans2o(rightpadded withspaces/zero's)
Values with "*'should be used for ATM
FieldEdits/Compliance Thisfield remainsthe sameforaparticulartransaction.
Constraints Thisisnotto beechoed backinresponse.
Validations This field should be of the format as described in the above
description
Compliance This is mandatory field and acquirer has to populate values in this
field as per the values mentioned above.
Presence Mandatory-Shouldbepresentforallmessages
Conditional-None
Optional-None
Page3of4

<!-- Page 7 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
Subfield 1 Card DataInputCapability
Subfield 2 CardholderAuthenticationCapability
Subfield 3 CardCaptureCapability 0/1/2
Subfield4 Terminal OperatingEnvironment 0/2/4
Subfield5 CardholderPresentData
Subfield 6 CardPresentData
Subfield 7 Card Data InputMode
Subfield 8 CardholderAuthenticationmethod
Subfield 9 CardholderAuthenticationEntity
Subfield10 Card DataOutput Capability
Subfield11 Terminal Data Output Capability
Subfield 12 PINCapturecapability 1/3
Subfield13-21 Zip Code ZiPcodeleftpaddedwithO
AdditionalAddress(RightPadded
Subfield22-41 AdditionalAddressdata with20zeros)
Page 4of 4

<!-- Page 8 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
ATM location:-
Prakasam Road, T Nagar CHENNAl bepopulated byMemberBanks.
FORT MUMBAI, RBI PREMISMUMBAI HITEC CITY, MADHAPUR, HYDERABAD
Mayasandra, CHANNAPATNABANGALORE
Shahdara, DELHI EAST EAST DELHI Delhi India
CompleteATMlocation
TamilnaduIndia
MaharashtraIndia KarnatakaIndia AndhraPradeshIndia
600017 400001 562107 110032 500081 PINCode Member Banks are requested to send the ATM location. Please find some of the examples for DE-43 and DE-61 given below that are to ExamplesforDE43andDE61 Annexurelll
Page 1 of 2

<!-- Page 9 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
di
Subfiel 1-23
DE61indetail: Shahdara, DELHIEAST DE43indetail:
Subfiel Prakasam Road,TNagar HITEC CITY, MADHAPUR,
FORTMUMBAI,RBIPREMISES, Mayasandra, CHANNAPATNA
d3
Subfiel
d4
Subfiel
Subfiel CHENNAI MUMBAI 24-36
BANGALORE EASTDELHI HYDERABAD
d6 DE 43
Subfiel
d7 MH
Subfiel 37-38
(DE 32) is already available for the purpose and on the basis of which bank name can also be determined.
d8
Subfiel
6p Note: There is no need to populate the bank name in Terminal Address and Terminal City, as a separate field"ACQUIRER ID"
Subfiel 39-40
d10
Subfiel
d11
Subfiel
d 12
Subfiel
000600017 000400001 000562107 000110032 000500081 Subfield 13
Subfield14
00000000000000000000 00000000000000000000 00000000000000000000 00000000000000000000 00000000000000000000
Page 2 of 2
