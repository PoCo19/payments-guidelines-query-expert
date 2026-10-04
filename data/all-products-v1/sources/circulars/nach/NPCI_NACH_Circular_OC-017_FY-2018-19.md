# Circular No.017 - Change in eSign creation and validation process as per regulatory requirement

Circular/reference number: NPCI/2018-19/NACH/CircularNo.017

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2018-19/NACH/CircularNo.017 July 17, 2018
To
AllNACHMemberbanks
Change in eSign creation andvalidation process as per regulatory requirement
Reference may be taken from our Circular no.226 on“eSign mandate variant live in MMs"
dated May04,2017.UIDAl, vide their circular no.06 dated January 10,2018 on
“Implementation of Virtual ID, UID token & Limited KYC",has advised user agencies to
discontinuetheusageof Aadhaarnumberforconsumptionandtransmissionacross systems.
The eSign variant of E-Mandate was introduced on May 05, 2017.With this a customer can
digitally sign themandate using his/her Aadhaar number, which in turn, is validated at the
bank end for further processing,approval and registration of E-Mandates.Currently 122
banksand50corporates arelive inthismoduleof NACHplatform.
As per the revised directions issued by UiDAl, in the digital certificate issued based on
Aadhaar authentication,onlythelast4digitsoftheAadhaarnumber(first8digitswill be
masked).It may pleasebe noted that despitethis change the combinationof account
number and the last 4 digits of the Aadhaar number continue to be unique.
In compliance to the above regulatory requirement, a few modifications are made in the
existing eSign creation and validation process.Themodifications are detailed below:
Corporate/SponsorBank
Last four digit of Aadhaar number prefixedwithzero shouldbe captured inopen
content of the XML format of NPCl.
E-SigntagsinXMLformat
a. Digital certificate will contain last four digit of Aadhaar.
b. Signed content should not contain theAadhaarnumber.
DestinationBank
Cross checkopencontent data mandate withSigned content except Aadhaar
number
Match last 4 digit of Aadhaar in digital signature with the last 4 digits of the
Aadhaarnumberlinkedtothebankaccount.
1001A,TheCapital,BWing,10thFlo0r,Bandra Kurla Complex,Bandra (E),Mumbai400051.T:+912240009100 F:+912240009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Excluding the above,the other process of mandate management and validations remain
unaltered.
We areworking withthe stakeholder on additionalfactors like Demographic authentication
for verification of the DN qualifier provided in digital certificate and othermeasures.In
view of the time required for the changes we are releasing specifications for immediate
changes so that the processing will not be impacted on August 01,2018.We shall release
next phase of changes once a workable solution with additional factors is finalized.
Member banks and user agencies are advised to incorporate these new changes in their
process effectivefrom August 01,2018 and disseminate theinformation to all the concerned
fornecessary action.
Forclarifications,pleasewritetoach@npci.org.in
With warm regards,
GiridharG.M
(SVP-NACH&CTS Operations)
1001A,TheCapital,BWing.10thFloor,Bandra Kurla Complex,Bandra(E),Mumbai400051.T:+912240009100F:+912240009101 www.npci.erg.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

Annexure.I - Existin process vs revised process
Particulars Entity. Existing process Revised process
No.
Last 4 digit. of Aadhaar
12 digit Aadhaar number number preceding with
Create file Sponsor in Aadhaar' field. 'of xm! zero to be captured in
format bank. and hashed. value in Aadhaar field in xml and no
digital certificate Aadhaar hashed value in
digital certificate
Mandatory fields in Mandatory fields in
encoded format (base 64) encoded format (base -64)
Verification Destination
with the data mandate with the data mandate.
of data bank
(including 12 digit excluding the Aadhaar
Aadhaar number) number
Retrieve:Aadhaar number Retrieve 'the last 4 digit of
of account in CBs and Aadhaar number of the
Aadhaar Destination convert to hash yalue and account in CBs and cross
validation bank cross'check withn Aadhaar check with last 4. digit of
hash value available in Aadhaar number in digital
digital certificate certificate
