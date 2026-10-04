# Circular No.218 - API based E Mandate Process

Circular/reference number: NPCI/2016-17/NACH/Circular

<!-- Page 1 -->

NPCI
NATIONALPAYMENTS CORPORATIONOFINDIA
NPCI/2016-17/NACH/Circular No.218 March 27, 2017
To
AllNACHmemberbanks
APlbasedE-mandateprocess
Refer to our Circular No.214 "Introduction of two Variants in API based mandate", NPCI is
providing an interface for the banks to connect through APl to enable the customer to
authenticate the mandates using either internet banking credentials or debit/credit card
credentials. Accordingly member banks were advised to build the system for authenticating
boththemandatevariantsas desired belowbyNPCl.
APIMandate
Electronically initiated mandate through web where the customer authenticates the
credentials digitally is called APl based mandate.
Once customer submits the mandate for through merchant site the browser will be directed
through NPCi to the destination bank for authentication. On selecting the bank, user will be
given option for authentication either through (i) Net banking or (i) debit / credit card
based on the ability of the banks to offer either or both the services. In case of bank is
offering only one of the services then only that service should be displayed.
The following are the 2 methods to allow the customer to digitally authenticate the
mandates
1. Net banking credentials
2. Debit / Credit card
It is expected that the corporate (Utility company / BFsl institutions) will provide a web
page enabling the customer to set up the mandates digitally, while designing the web page
the corporate should take care of the followings.
1.Customerwill log in to the corporate website.
2. Key in all the mandatory fields required for a mandate as per the guidelines of NPCl.
3. Post confirmation, the customer should be directed to the bank's site for
authentication using
a. Net banking credentials
b. Debit / Credit card
The detailed points to be noted is enclosed herewith for the ready reference.
1001A,The Capital, B Wing,10th Floor,Bandra Kurla Comptex,Bandra (E),Mumbai 400051.T:+91.22 40009100 F:+91 2240009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NCI
NATIONAL PAYMENTSCORPORATIONOFINDIA
Authorisation through Net banking:
When customer selects desired bank and authorisation mode as“Netbanking", request will
be sent to the bank for internet banking login page, the page should be designed in such a
waythat
Ensure account number given by customer in the mandate form is valid and"Active"
In case account number is invalid / Inactive, bank should redirect the failed
authentication to NPCl interface with reason“Account Invalid / Inactive".
If account is active, allow customer to login net banking web site. After
predetermined unsuccessful login attempts, bank has to redirect to NPCl interface
with reason"Invalid login credentials".
also add oTP or any other authentication mechanism as may be required.
Provision should be made so that customer can reject the mandate with reason
"Mandate information mismatch",
Bank can also reject the customer mandate based on internal policies defined at
bank end with appropriate reject reasons.
Bank should redirect the success or failure authentication to NpCl interface with
appropriate reason/s as may be defined by NPCl.
Bank to preserve the mandate information and the status for future reference.This
is applicable even for rejected mandates.
All the regulations governing the internet banking as per the internet policy of the
bank or RBl should be followed.
Authorisation through Debit / Credit card:
Ensure card number given by customer in the mandate form is valid and "Active", In
case account number is invalid / Inactive, bank should redirect the failed authentication
toNPCIinterface
If card is active,the following details should be accepted from the customer:
a. Expiry of card and CVV
b. OTP
On successful validation of details provided, bank should display information given by
customer in theonline mandateform for confirmation.
Provision should be made so that customer can reject the mandate with reason“Mandate
information mismatch".
Bank can also reject the customer mandate based on internal policies defined at bank
end with appropriate reject reasons.
Bank should redirect the success or failure authentication to NpCl interface with
appropriate reason/s as may be defined by NPCl.
1001A,The Capital, B Wing,10thFloor,Bandra Kurla Complex, Bandra (E),Mumbai 400 051.T: +9122 40009100 F:+9122 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Bank to preserve the mandate information and the status for future reference. This is
applicableevenforrejectedmandates.
All the regulations governing the card based authentication as per the internet policy of
thebankorRBl shouldbefollowed.
The technical specification is provided in annexure IAll the memberbanks are advised to
start working on this on priority.
Forany clarificationspleasewritebacktoach@npci.org.in
With warm regards
(Giridhar G M)
VP&Head-NACH&CTSOperations
1001A,The Capitat.B Wing, 10th Floor,Bandra Kurla Complex, Bandra (E), Mumbai 400051.T:+9122 40009100 F:+91 22-40009101 www.npci.org.in
CIN:U74990MH2008NPL189067
