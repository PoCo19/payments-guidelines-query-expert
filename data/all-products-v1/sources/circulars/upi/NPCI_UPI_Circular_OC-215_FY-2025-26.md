# UPI | OC No. 215| FY 2025-26 | Streamlining the initiation of Check Transaction in UPI and misuse of APIs

Circular/reference number: OC-215
Date: 26th April, 2025

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
NPC/UP//OC/215/2025-26 26th April,2025
To
All UPI Members,
Subject: Initial Streamlining the Check Transaction usage in UPl and overuse / misuse of all UPl APls
This circular is issued to address the situation that has been resulted due to initiation of high number of "Check
Transaction Status" APls by PsP banks at a very high Transactions Per Second (TPS) rate in repetitive
manner. To ensure that UPl system is able to operate as per ecosystem expectations, following are the
guidelines to be adhered by UPI members:
1. PsP banks/Acquiring Banks shall ensure that all the APl requests (traffic) sent to UPI is monitored
and moderated in terms of appropriate usage for e.g. restricting high number of repeat APl's for
same transactions or older transactions etc.
2. PsP bankslAcquiring Banks shall ensure that there is no batch processing (by processing file and
converting to online request at high TPS) of any of the non-financial APls sent to UPl Online systems.
3. PsP banks / Acquiring banks shal initiate the first check transaction status APl after 90 seconds from
the initiation/authentication of the original transaction. After the timers are changed (ref. UPI OC 214,
dated 26th April, 2025), members may initiate the same after 45 to 60 seconds of the
initiation/authentication of original transaction, after NPCl revised communication.
within 2 hours from the initiation/authentication of the original transaction.
5. Subsequently, in case of U48 error (Transaction ID not present or not found in UPI System) within
first two 2 hours from initiation of the original transaction, then PsP banks / Acquiring banks shall refer
the NPCl settlement files (available to Payee, Payer or PsP banks) after the settlement cycle is
completed, alternatively members may initiate a maximum of one check transaction statuis APl on
UDiR (Unified Dispute and Issue Resolution) which in turn checks URCS (UPI Backoffice) to fetch
the final settlement status of the transaction.
6. PsP banks / Acquiring banks shall consider the transaction failed, if they receive an error from the
list mentioned in Annexure 1 and shall not initiate further check transaction status APl.
7. PsP banks / Acquiring banks shall audit their systems by Cert-in empanelled auditor on an immediate
basis, to review the APl usage and existing systems behaviour, and annually hereafter.
8. The remitter bank/PsP shall have visibility over specific UPl APls and are responsible for regularly
reviewing their usage. Any exceptions or anomalies observed shall be reported to NPCl.
9. NPCI may also consider implementing rate limiters on select UP1 API's in consultation with steering
committee and subject to other approvals in due course.
Above measures to be implemented by the PSP banks / Acquiring banks on immediate basis. NPCi may also
review the APl requests on ongoing basis and work with Members to ensure that usage of UPl system API's
is responsible and measured.
1001A, The Capital, B Wing, 10th Floor.
Bandra Kurla Complex, Bandra (E), Mumbai 400 051.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
Members are also requested to reach out for any further suggestions and changes in above, after reviewing
the feedback and data in next 4 weeks' time to upi.compliance@npci.org.in so that they are incorporated and
revised guidelines in this regard can be issued, if necessary.
Further, reiterating the earier compliance, as per NPCI UPI operating circular no. 95 dated 25th September
action, including penal provisions, if any.
Yours sincerely,
SD/-
Kunal Kalawatia
Chief of Products
Weethia

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure 1:Errors/Conditions where check transactionAPl shall notbe initiated
1. Connection timeout
2. Connection refused
3. No route to host
4. Unknown host
5. Port unreachable
6. TLS handshake error
7. HTTP Status code: 501
8. HTTP Status code: 503
9. HTTP Status code: 403
10. HTTP Status code: 417
11. HTTP Status code: 404
12. HTTP Status code: 429
13. HTTP Status code: 413
14. Any Negative ACK from NPCI
15.Transaction Success/Failure confirmation fromNPCl
Together
WeBuild
