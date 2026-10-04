# UPI OC 116 - Aadhaar OTP Authentication in lieu of Debit Card for Customer Onboarding on Unified Payments Interface (UPI)

Circular/reference number: NPCI/UPI/OC-116/2021
Date: 25th August 2016

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/UPI/OC-116/2021 gth September 2021
To,
All UPIMembers-Banks,PSP's&Third PartyApplications
Madam/ DearSir,
Subject: Aadhaar OTP Authentication in lieu of Debit Card for Customer Onboarding on
Unified Payments Interface (UPl)
Unified Payments Interface (UPl) was launched on 25th August 2016, and has since gained scale.
With a view to further expand the user base by offering simpified onboarding, a new option for
onboarding users on UPl is being introduced, whereby a customer can be authenticated on the
basis of the customer's Aadhaar with OTP. Customers who either do not have a debit card, or
whose debit card is not active, can easily set or reset his or her UPl PIN with this option.
This enablement would go a long way in increasing inclusion of customers across the country to
digital payments, since Aadhaar number is now available with almost all Indian citizens. Also
safe, secure and convenient alternative onboarding channel thereby increasing digital footprint.
With this roll out, the customer would have the choice to use Aadhaar with OTP for authentication
in lieu of Debit card. Annexure - A of this circular provides the detailed flow of the onboarding
process using Aadhaar authentication and OTP. In this architecture, NPCI shall connect to Unique
validation of Aadhaar OTP will be done as per UIDAl Guidelines.
UPl members shall continue to comply with two factor authentication guidelines of RBl and also
ensure the following
1. PSP/Banks should ensure that the facility of UPl on-boarding using Aadhaar with OTP is
made available only if the UPl application is being used on mobile having Aadhaar
registered mobile number and same mobile number is registered with bank.
1001A, The Capital, B Wing,10th Floor.
BandraKurla Complex,Bandra(E),Mumbai4ooo51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

2. Issuer banks shall verify Aadhaar holder's mobile number, in addition to OTp
authentication. In case of authentication failure appropriate error should be displayed to
Aadhaar holder.
UlDAl's Aadhaar authentication charges shall be applicable as per the provisions of Aadhaar
(Pricing of Aadhaar Authentication Services) Regulations, 2019 as amended from time to time.
All Banks, PsPs, and TPAPs shall ensure compliance with the rules, regulations and guidelines
issued by UIDAl as applicable in this regard.
UPl members shall comply with the provisions of this circular by 15t December 2021.
SD/-
Yours Faithfully,
PraveenaRai
Chief Operating Officer

<!-- Page 3 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
Annexure A
Detail flow - Set or Reset UPI PIN using Aadhaar with OTP
a) Customer selects the option of Aadhaar with OTP and provides his/her consent to set or rest
UPI PIN.
b) Issuer bank returns the Account Number and Aadhaar number from Core Banking System, if
customers Aadhaar is linked to bank account. If customer's Aadhaar is not linked, issuer bank
shall respond that no Aadhaar is linked to bank account.
UPl forwards the last 4 digit of the Aadhaar number received from issuer bank to the Payer
last 4 digits of the customer's Aadhaar number.
d) Payer UPl application validates the last 4 digits of Aadhaar number entered by the customer
with the number forwarded by UPI from issuer bank. if the numbers match, the Payer UPI App
confirms to UPi, and UPI in turn requests UIDAl to send the Aadhaar OTP to the customer's
registered mobile number stored in UIDAI's database/ repository.
Bank shall send OTP to customer's mobile number.
f)  Customer will enter both Aadhaar OTP and Issuer OTP on his UPI App received on his
registered mobile number. Post which the customer enters new UPI PIN which the customer
wants to set, & confirm the same. Payer PsP will share the above details to UPl for validation.
g) UPI will forward the details of OTP (Aadhaar OTP) and mobile number to UIDAl for
authentication. UIDAl shall authenticate OTP, and send the authentication flag ="y", if both
the UIDAl registered mobile number on which the OTP has been sent by UIDAl, and the one
sent in the APl are same.
h) However if authentication flag = “N", either due to OTP validation failure or due to mismatch
of mobile numbers NPCl shall decline the onboarding transaction.
1001A, The Capital, B Wing, 10th Floor,
BandraKurlaComplex,Bandra(E),Mumbai4ooO51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 4 -->

i) Post a success response is being received for Aadhaar OTP validation from UIDAl, UPl
shares the Issuer bank OTP to Issuer bank along with the new UPI PIN requested by customer
and UIDAl's OTP validation success response.
Now issuer bank verifies the issuer bank's OTP and confirms to UPl with a success or failure
response. Based on the issuer bank's final confirmation, the new requested UPl PiN is set/
reset successfully.
