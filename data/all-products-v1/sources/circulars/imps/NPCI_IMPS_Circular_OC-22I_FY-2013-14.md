# IMPS I OC 22 I FY 13-14 I Regarding the IMPS - Technical Issues

Circular/reference number: OC-22I

<!-- Page 1 -->

NPCi
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI:OCNo.22:IMPS:2013-14 August 1, 2013
All MemberBanks/RBIauthorizedPrepaidPaymentInstrumentIssuers(PPls)ofIMPS
DearSir/Madam,
Subject:Regarding the IMPS-Technical Issues
1. Freguent Time-out Issues
The IMps transaction volumes are increasing day-by-day. We observe that the number of transactions
with“Time-out" response have also increased to the extent 0.82% of total transaction in the month of
July 13. In the case of ‘Time-out' response, the transaction may eventually go into a Dispute Redressal
Process and such disputes will take maximum 5 days resolution period. This may result in customer
dissatisfaction.
In view of the above, we suggest that remedial steps need to be taken by Member Banks to take care of
this time-out issue.Wegive below some of the indicative measures the memberbanks can adopt:
a.The member banks are requested to ascertain infrastructure capabilities to support the
additional load of transaction volumes. We request member banks to check the hardware,
network and application capabilities to handle increased volumes so as to avoid time-out
cases.
b. The utilization levels of hardware, application and network need to be continuously
monitored. Ideally if the utilization level exceeded by 50% then bank can start the up
gradation process.
c.Software patches released by the switch vendor should be tested in the test environment
before applying to the production system.All schedule activities need to be carried out only
between 00:00Hrs and 06:00Hrs on any day. Member Banks to avoid any maintenance
activityduring thehighvolumetime/days.
d.Planned DR drill should be carried out during the night time between 0O:0OHrs to O6:00Hrs
to ensure that the customer impactis minimized.
e. Bank should have strong reconciliation system in place.Three way settlement need to be
donewithNPCIdata, Mobilebanking serverdataand CBSdata.
Member Banks are requested to initiate necessary action to take care of this issue and work towards
reducing the instances of'Time-out' Issues.
C-9, 8th Floor PHqT/Phone:02226573150
RBIPremises /Fax:02226571001
Bandra-Kurla Complex 专-/email:contact@npci.org.in
Bandra East a/Website:www.npci.org.in
-400 051 Mumbai400051

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
:2:
2.Duplicate RRN
Wehaveobservedan issuein IMPS transactionsdueto'DuplicateRRN'.
a. The Beneficiary Bank receives transactions from various Remitter Banks, and can receive
multiple transactions with same RRN, if these transactions are getting generated at same time at
the respective Remitter Banks. In this case, the Beneficiary Bank identifies these transactions as
'Duplicate',and does not credit into the Beneficiary account for these transactions.
b. To solve this issue, Member Banks are requested to identify the transaction as'Duplicate'only if
NBIN+RRN combination is duplicate, otherwise the transaction may be considered as 'Unique
andprocessedaccordingly.
We request you to take steps towards implementation of the above at the earliest.
3. Orieinating Channel
We have observed that the Initiating Bank is not populating 'Originating Channel' correctly at their end.
Channel' field, depending on the channel that was used for originating the channel.
Channel Description
ATM FromATM channel
INET From Internet Banking Channel
SMS FromSMSmode
IVR From IVRchannel
USDC FromNUUP(on*99#)
USDB FrombankprovidedUSSDchannel (bank'sownUSSDcode)
POS FromPointof SaleDevice
MOB From Mobile Banking Application
MAT FromMicro-ATM
WAP FromInterneton MobilePhone
Member Banks are requested to populate the same as per the specifications.We request you to take
steps towards implementation of the same,at the earliest.
Yours sincerely,
SD/-
DilipAsbe
Chier Operating Officer
