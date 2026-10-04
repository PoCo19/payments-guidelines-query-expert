# OC 147 - Handling of Transaction declines during address resolution authorisation leg

Circular/reference number: NPCI/UPI/OCNo.147/2022-23

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTSCORPORATIONOFINDIA
NPCI/UPI/OCNo.147/2022-23 April13,2022
AllmembersofUnifiedPaymentsInterface (UPl)
Madam/DearSir,
Subject:Handling of Transaction declines during address resolution /authorisation leg.
Upl is becoming most preferred payment mode. As volume is increasing, there are cases of
timeout transactions, which leads to customer complaints and disputes.In orderto address the
same,NPC hasenabled dynamicthrottling mechanism at central level, wherein NPCldeclinethe
transactionsbased onthefollowingparameters pertainingtobeneficiarybanks.
a.Maximumconnections/requestsopenatbeneficiarybank(U89)
b.No.of credit request open atbeneficiarybank (U84)
Cc. High response time at beneficiary bank (Ug1)
Throttling implementation helps in reduction of deemed approved transaction as potential
deemed approved transactions are treated as declined and not routed to beneficiary bank.
Throttling mechanism is being reviewed from time to time based on analysis and feedback from
theecosystemplayers.Additionally,NPCl isalsoworkingcloselywith memberbankstoaddress
thehightimeoutand declinetransactionsforachieving highsuccessrate.
Payer Psp(incase of Collect Transactions)andPayee Psp(incase of Pay Transactions)are
expected to provideunderlying accountinformation behind UPliD duringthe addressresolution
/authorisation leg and can decine the transaction with Business Decline (BD)or Technical
Decline(TD)responsecodeforthescenariosasdefined inUPi Specificationfromtimetotime.
Payer /Payee PsP or its partner Apps should not decline the transactions due to throttling at
their end and map such declines with existing response codes.Any such practices at any of Psp
or its partner Apps will defeat the purpose of interoperability.
Members may please make a note of the above and disseminate the information contained
hereinto all officialsconcerned.
Yours Sincerely,
S MN
SaiprasadNabar
Chief-OnlineProductOperationsandTechnology
1001A,TheCapital,BWing,1othFloor,
BandraKurlaComplex,Bandra(E),Mumbai400O51.
