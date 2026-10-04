# UPI | OC No. 215 A | FY 2025-26 | Guidelines on usage of UPI APIs

Circular/reference number: OC-215A
Date: 21st May 2025

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/UP//OC/215A/2025-26 21st May 2025
To
All UPI Members,
Subject: Guidelines on usage of UPI AP]
With reference to NPCl/UP/OC/215/2025-26 dated 26th April 2025 PSP Banks and/or Acquiring Banks shall
ensure all the API requests (in terms of velocity and TPs - transactions per second limitations) sent to UPl is
monitored and moderated in terms of appropriate usage (customer-initiated and PsP system-initiated).
With the objective of improving the performance of UPl, following are the additional set of guidelines to be
adhered by UPl ecosystem members:
SN APl / Use Purpose Frequency / TPS (per IP Usage guidelines
Case Limits address)
Balance To check balance 50 per app per NPC1 may a) These requests shall be only
Enquiry available through UPl customer per deploy rate initiated by the customer
apps day (rolling 24 limiters for this b) UPI Apps shall have the
hours) API capability to limit or stop
balance enquiry requests, if
needed to reduce the load in
peak hours
c) Issuer Banks shall add the
available balance with every
successful UP! financia!
transaction communication.
List Keys This APl allows the Only once per NPCI may a) Minimum page size of 1000 to
(for type PsPs to reguest the PsP per day deploy rate be used while initiating the
ListKeys and list of public keys at (rolling 24 limiters for this request
PSPKeys) NPCI. hours) AP! b) To be done in non-peak hours
List Account Allows customer to 25 per app per NPCI may a) These requests are to be
find the list of customer per deploy rate initiated only once the
accounts linked to day (rolling 24 limiters for this customer selects the issuer
their mobile by hours) AP! bank in the UPI App.
particular account b) In case of failure to list
provider. account, every re-try should
be done only with customer
consent.
1001A, The Capital, B Wing, 1oth Floor.
BandraKurlaComplex,Bandra(E),Mumbai4ooO51-
T:+9122 40009100F:+912240009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTS CORPORATION OFNDIA
SN APl Use Purpose Frequency TPS (per IP Usage guidelines
Case Limits address)
Check This AP allows the Refer to NPCI may The PsPs shall request for status
transaction PsPs to request for NPCI/UPI/OC deploy rate only after the specified period.
status the status of the /215/2025-26 fimiters for this ReferNPC1/UP1/OC/215/2025-26
transaction. dated 26th API dated 26th April 2025
April 2025
Autopay Executing UP[ Maximum of 1 NPCI may a) Initiator PsPs to ensure UPl
Mandate Autopay mandates attempt and 3 deploy rate Autopay executions shall be
Execution retries per limiters for this initiated at moderated TPS
mandate (per API b) To be initiated in non-peak
sequence hours
number) shall
be permitted
List verified Through this APl, the Once per PsP NPCI may a) Minimum page size of 1000
merchants PSPs can  manage, per day deploy rate to be used while initiating the
and access the (rolling 24 limiters for this request
verified address hours) API b) To be done in non-peak
entries. Verified hours
merchants)
Penny Drop Transactions initiated Queueing NPCI may a) This shall be extended only
to verity the validity should be deploy rate to entities where it is a
and ownership of an maintained at limiters for this regulatory requirerment. Ref
account initiating PSP API UPI OC 95.
end b) This shall be initiated only
basis explicit customer
consent (Initiating bank shall
have the formal undertaking
from the requestor and in full
compliance of DPDP Act.)
c) Merchant Category Code
7413 and separate
dedicated UPI ID shall be
assigned by the entity for
such transactions. Separate
pricing for such transactions
shall be assigned in due
course.
Together
WeBuild

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
SN API Use Purpose Frequency TPS (per IP Usage guidelines
Case Limits address)
d) To be initiated in non-peak
hours
ValCust APl Service is used to Service shall NPCI may a) For IPO, PANvalidation shal!
validate the customer be only deploy rate only be initiated where the
details, pre-debit allowed to be limiters for this mandate has been
notification, customer used for valid API successfully created
activation for FIR etc. use cases b) For other use case it shall be
initiated in limited attempts
and at moderate TPS
APl Header PsPs to ensure that Permitted NPCI wil!  All members shall update
format only the mentioned headers: block such their production APl clients
headers shall be a) Host requests in and reverse proxies to
leveraged in UPI API b) Content- due course whitelist only the permitted
traffic. Length that are in headers
c) Content- non- b)  Preventive mechanisms
type/Acce conformance should  be configured at
pt appropriate [evel (e.g..
d) User- reverse proxies, API
Agent gateways) to reject or strip
out unauthorized neaders
10 Validate Used for validating (NPCI NPCI may a) To be used oniy when the
Address UPI IDs or Virtual may release deploy rate customer intends to pay
Payment Addresses updated limits limiters for this b) Stand-aione use of valadd is
(VPAs) before later) AP[ not permitted
initiating a payment c) In the scenario, where valadd
or transaction is used for penny drop use
case, the new MCC (7413)
defined for penny drop
should be used for valadd as
well
d) Appropriate credentiais of
the initiator (mobile number,
UPI ID, MCC etc.) should be
populated in payer details
APl fields.
Togethen
WeBuild

<!-- Page 4 -->

NPC
NATIONALPAYMENTSCORPORATIONOFINDIA
In addition to the above guidelines, members to note the following:
1. It is re-iterated that PsPs need to monitor usage as specified in this circular (and the relevant ones
referred) that the stand-alone use of APls for purposes other than intended is prohibited, uniess
approved specificallybyNPCl.
2. PsPs shall monitor and have a queueing of system-initiated APls to ensure moderated TPS or in other
words PsP systems are not a pass through for back-end generated API transactions to UPI systems
in all conditions. PsP's shall give the undertaking to NPCl in this regard on or before 31 st Aug 2025
3. Peak hours are defined as the period during the day when UPl financial transactions reach the
highest transactions per second, observed from 10:00 hrs to 13:00 hrs and from 17:00 hrs to
21:3o hrs. Any other time shall be referred as non-peak hour. During peak hours, UPl members are
required to restrict non-customer-initiated APls.
4. With reference to NPCI/UPI/OC/215/2025-26 dated 26th April 2025, point number 7, ‘PSP banks /
Acquiring banks shall audit their systems by Cert-in empanelled auditor on an immediate basis, to
review the APl usage and existing systems behaviour, and annually hereafter'. For the audit scope,
PsP banks/ Acquiring banks shall refer to Annexure A, where the minimum scope of audit has been
outlined.
5. The audit reports shall be shared with upi.compliance@npci.org.in by 31st August 2025.
Members are requested to take note of this compliance requirement and communicate it to relevant
stakeholders and their respective partners for implementation by 31st July 2025. In the event of non-
compliance to the above guidelines, NPCl may take necessary action including UPI API restrictions. penaities,
Yours sincerely,
SD/-
Kunal Kalawatia
Chief of Products
