# OC 115 - Rollout of “Numeric UPI ID Mapper” to enable “UPI Number”

Circular/reference number: NPCI/UPI/OC-115/2021-22
Date: 20th July, 2021

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
NPCI/UPI/OC-115/2021-22
To
All UPI Members, 20th July, 2021
Dear Sir / Madam,
Subject: Rollout of “Numeric UPI ID Mapper" to enable "UPI Number"
Introduction of UPl ID as a payment address has transformed real-time payments. With the defined
structure of "Username@Psp", the suffix after“@ "is used to point to the PsP for transaction routing. In
continuous endeavour to enhance user experience on UPl Apps and to accelerate adoption of feature
phone based UPl solutions, it is imperative to have a simple payment address such as numeric UPl ID
(referred to as UPI Number hereunder).
In thnis regard, a Numeric UPI ID mapper (referred as UPI iD mapper hereunder) is being introduced. This
mapper will host the UPI Number mapped against respective UPI ID and shall resolve the corresponding
mapping to the respective PSP/TPAP for the transaction routing. The UPI ID mapper shall be accessed
on API for the purpose of initiating transactions and UPl Number lifecycle management.
Few PSPs/TPAPs have been using mobile numbers as alias to UPI ID for P2P & P2M payments using
UPl apps, however users do not experience the interoperability between the PsPs / TPAPs. The
introduction of UPl Number shall provide the interoperability for such use cases too. Any token / payment
id / proprietary QR code not conforming to interoperable standards approved by the regulator and used
to send, receive money and provide services on UPl interoperable rails (including P2P, P2M and other
use cases), only between the users of one app (applicable to all UPl enabled apps) shall not be permitted.
Introduction of UPi Number:
1) UPl user will have a choice of 8-11 digits' numeric code as their UPl Number, in addition to the
existing alpha numeric UPIl ID (Username@PsP).
2) The UPI ID mapper shall host unique UPI Number across the UPI user base for all the PSPs. The
user can make a choice from eight to nine digits, however, in case of ten digits (and when mobile
number is extended to eleven digits in future), the sender/receiver shall be allowed to set oniy
their own mobile number (UPl app shall auto fetch instead of user input). This means when user
intends to set mobile number as UPl Number, the check for"own mobile number" shall be applied.
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex,Bandra(E), Mumbai 4ooO51.
T: +9122 40009100 F: +9122 40009101www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCL
NATIONALPAYMENTSCORPORATION OF INDIA
3) All the PSP's / TPAP's shall support entire lifecycle management for UPI Number i.e. register,
update, deletelderegister into the UPl ID mapper.
4) If the user intends to use the beneficiary's UPI Number for the UPl based payments, then during
the UPl payment transaction, the sending app shall ensure to take the beneficiary's UPI Number
twice and match before proceeding further. In spite of the above, if user happens to send the
money to a wrong mobile number, the responsibility of the same shall lie with the sending user.
to the dual entry method can be :
a.  User has saved the UPl Number in the sending app as beneficiary or,
b. The UPl Number of the beneficiary is picked up from the saved contact on the phone 
app or,
disputes shall be resolved by such PSPs/TPAPs.
5) It shall be mandatory for all UPI enabled apps (PSP / TPAPs) to participate in UPI ID mapper.
User Consent
6) Generation of UP Number is voluntary and explicit user consent is required to seed in UPI ID
mapper. The consent also can be taken as part of the Terms and Conditions of the PsP/TPAP.
7) ln case user does not want to receive money using UPl Number for any reason (i.e. declines the
consent in specific app for seeding into UPl ID mapper), they will not be able to receive money
However, they will continue to receive money using UPl ID or other payment address like Bank
Account number.
MapperManagement
8) _NPCl shall be responsible to maintain the UPI ID mapper in safe and secure manner.
9) All transactions using a UPl Number (including mobile number) irrespective of the transaction
type shall be resolved using UPl ID mapper online (caching at the UPl app is not permitted)
except,
a. If the sender and receiver are using the same UPl app
10) The tatest successful entry shall be used by the mapper to resolve the PsP
11) The user has a choice to have multiple UPI Numbers for different app providers
a. Where mobile number is used as the UPI Number, the same can be linked to a single
UPI ID only, at any instance.
1001A, The Capital, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 400 051.
CIN: U74990MH2008NPL189067

<!-- Page 3 -->

NPC
NATIONALPAYMENTSCORPORATIONOFINDIA
b. If the user intends(on choice) to use the same mobile number used as UPl Number seeded
into UPl ID mapper, then user will have to use the overwrite functionality which will need
uservalidation of last successful seeded UP PSP/TPAP.
C. The overwrite functionality shall not be permitted for any UPI Number other than mobile
number.
d. Customer shall be permitted to use the same UPI Number / UPI ID in the situations such
as the sIM change, handset change.
e. Any UPl Number, upon deregistration shall not be allowed to use for a period of 6 months.
Same user can reuse the UPI Number within this period.
f. For recycled mobile number, the usage of mobile number as UPi ID shall be permitted
after 6 months from the last active transactions or with full on-boarding whichever is earlier.
12) For new users at the time of on boarding, PSP/TPAP must provide option for UPI Number seeding
with consent as explained above. Similarly, for existing users, the PSP/TPAP shall provide options
for seeding as per their choice.
13) It shall be mandatory for all UPl enabled feature phone based solutions to support entire lifecycle
management for UPl Number i.e. register, update, deletelderegister into the UPI ID mapper.
14) The forthcoming UPI PPI interoperability may have some situations (as and when made live)
which the players having the same app as PsP/TPAP and the PPI (since most of the times the
mobile number the user is designated id for the wallet) will have to solve by creating appropriate
a. The receive transaction for such common customer shall be managed by such PsP/TPAP
to credit either of the bank account/wallet as per user choice
15) The sending and receiving PSPs / TPAPs shall ensure the UPI number respectively for the
receiver and sender must not be used for any purpose other than risk management, and stored
or displayed in encrypted /masked format only.
16) The sending PsPs / TPAPs must ensure that there are adequate risk measures applied such as
how many times a user can make "validate address APl" calls specifically to UPl Number.
17) The PsPs / TPAPs shall put in adequate efforts for user awareness to communicate that using
UPl Number; user can send or receive payment using any UPl enabled app.
Roll Out of NumericID Mapper
18) For all the existing users, the PSP's/TPAP's, shall start providing the option of UPi Number
registration by variety of push pull options for e.g. notifications, menu options and pop-ups during
the transactions.
19) The PSPs/TPAPs shall not incentivise the UPl user for an UPl ID mapper overwrite function
directly or indirectly.
1001A, The Capitat, B Wing, 10th Floor,
Bandra Kurla Complex, Bandra (E), Mumbai 4o0 051.
T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 4 -->

NPCI
NATIONALPAYMENTS CORPORATION OF INDIA
Existing guidelines as applicable on UPl ID such as interoperability, display on payment home page
(masked if the user has chosen the mobile number) and mandatory functionalities etc. shall also be
applicable on UPl Number too. Following compliance shall be noted by the members:
20) The UPI ID mapper pilot shall be launched with effect from 1st October 2021. During the pilot
period (before 1st December 2021), the participating PSP/TPAP shall on-board not more than 5
Mn users on the mapper per app.
have a compliance deadline to go live on or before 1st December 2021.
22) From 1st Jan 2022, the members are to start declining mobile number based transactions
(including intra app transactions), in the case of no consent for seeding of the mobile number as
UPI Number.
SD/-
Yours Faithfully,
Praveena Rai
Chief Operating Officer
1001A, The Capital, B Wing, 10th Floor,
BandraKurlaCompiex,Bandra(E),Mumbai 4ooo51.
T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN: U74990MH2008NPL189067
