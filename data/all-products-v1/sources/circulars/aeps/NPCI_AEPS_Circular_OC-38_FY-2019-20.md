# AePS | OC 38| FY 18 19 | Best Practices to reduce declines

Circular/reference number: OC-38
Date: 6th March, 2019

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPC//2018-19/AePS/014 6th March, 2019
To,
Member Bank - Aadhaar Enabled Payment Systems
Subject: 1) Best Practices to reduce Technical Declines
2) Best Practices to reduce Biometric Mismatch
ecosystem to reduce the technical decline count and improving the customer serviceability at the field level.
To meet the above objective, we suggest banks/ end customers to adopt the following best practices:
Sr. No. Proposal/ Development For detailed process, refer
Best practices to be followed to reduce technical declines Annexure-l
Best practices to reduce the count of biometric mismatch Annexure-ll
Other key requirements:
Robust Infrastructure: A major bottleneck in the widespread usage for AePS and BHIM Aadhaar are
due to technical declines. Hence, to increase the usage of AePs & BHiM Aadhaar, it is recommended
that all AePs members should improve their system capacity (switching capacity, network bandwidth &
server/DB capacity, application capacity etc.) to match the volume of transactions they are processing.
We request you to ensure that your Bank's system should have 150 transactions per second (TPs) &
process 0.5 million transactions per day. If system utilisation at bank end reaches 60% of the existing
TPs, then bank must take proactive action to increase the capacity accordingly. We request you to
ensure that your systems i.e. Production (PR), Backup system & Disaster Recovery (DR) systems are in
sync and DR should be ready in case of any issue in Production/Primary system.
- Minimum hops between beneficiary switch & CBS: It is advised that all members should have
minimum hops between issuer switch and CBs so that the request & response messages reach to the
source & destination within the TAT and helps in avoiding declined transactions. All members are
requested to take a note of the above and ensure to put in place proper processes so as to reduce the
declines and increase approval ratio.
With kind regards,
Ram Sundaresan
SvP & Head -Operations
1001A,The Capitat,BWing,10th Floor,Bandra Kurla Complex,Bandra (E),Mumbai 400051.T:+912240009100 F:+912240009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure!
NPCI has issued a circular number NPCl/2018-19/AePS/004 in the month of Sept, 2018 advising banks to
undertake scheduled downtime activities only during non-peak hours i.e. 00:00 to 05:00 hours. It improves the
approval rate as most of the customer initiated AePs transactions are performed during day time.
Further, based on our experience and also after discussing with major issuer banks which had high technical
below such best practices to be followed by banks to reduce technical declines:
To reduce timeout (declined by response code 08) scenario, additional/separate Issuer & Acquirer port may
be configured at bank's switch level to handle peak volume.
 Bank must send AePs transactions as per latest AePs Specifications to reduce instances of transactions
declined due to format error.
 Additional GL accounts may be configured to minimize Account lock declines at issuer end.
Banks should ensure that scheduled maintenance activity should be done during non-peak hours.
DR drills should be conducted during non-peak hours (between 00:00 hours and 05:00 hours).
Bank may consider availing multiple link (through service providers) connectivity between NPCl &
Bank's DC (both PR and DR).
If the primary link is down bank can consider routing the transaction internally through DR.
We have observed that technical declines have reduced substantially after implementing above suggested
changes by some of the issuer banks.
1001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051. T:+91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 3 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure II
Biometric mismatch (RC U3) has been the major contributor for declines in AePS. We are highlighting few best
practices to reduce the declines due to biometric mismatch at field level and which in turn will enhance the
serviceability for end consumers. Banks are advised to share the below guidelines to their business
correspondents and customers:
Sr. No. Do's Don'ts
Clean the Finger and Finger print scanner Using greasy, sweat and dry finger while
before performing the bio-metric authentication performing the bio-metric authentication based
based transaction. transaction.
Micro ATM Application deployed in production Performing transaction while the hands are
must support dual/fusion finger authentication. painted (e.g. Mehndi, Tattoo etc.)
It improves success percentage
Best Finger Detection must be performed Using the same finger once the transaction got
before authentication to identify the best finger declined with response code: U3
and henceforth customers should be advised to
use the same finger to perform transactions.
Correct Aadhaar number is entered.
Ensure proper placement of finger on scanner.
Micro ATM scanner must be of standard 1.5.1 &
STQC certified.
1001A, The Capital, B Wing, 10th Floor, Bandra Kurla Complex, Bandra (E), Mumbai 400 051. T: +91 22 40009100 F: +91 22 40009101 www.npci.org.in
CIN:U74990MH2008NPL189067
