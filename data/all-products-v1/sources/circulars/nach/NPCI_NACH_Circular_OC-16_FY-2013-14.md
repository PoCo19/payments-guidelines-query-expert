# Circular No 16 - NACH Debit Mandate Validation Service.

Circular/reference number: NPCI/NACH/2013-14/Circular16
Date: 3rd October, 2013

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/NACH/2013-14/Circular16 3rd October, 2013
To,
All Member Banks of NACH System
Madam/Dear Sir,
NACHDebit-MandateValidation Service made available tothe Banks
A number of NACH member banks have expressed their interest in participating in the
NACH Debit ecosystem and have requested NPCi to implement a process to validate the
Mandate.Based on the inputs received from the banks and subsequent deliberations,NPC!
is offering the"Mandate Validation Service'for NACH Debit participating banks w.e.f 7th
October 2013.
2. All debit transactions processed on the NACH platform from 7th of October 2013 will be
validated by NPCl against the available mandate data as per the details in Annexure.Only
those transactions which successfully clear stated validations will be forwarded to the
destination bank for onward processing.
3. The complete repository of bank relevant mandate data along with the images can be
made available to the Bank, on request.
4. We urge all the banks to initiate on-boarding process on NACH debit at the earliest. we
look forward for your continuous support to make NACH system a success. For ay
queries/further help, please email us at ach@npci.org.in
WithWarmRegards
VipinSurelia
SVP & Head - NACH & Cheque Clearing
Page 1 of 3
-9,8 C-9, 8th Floor ql/Phone:02226573150
RBIPremises a/Fax:02226571001
Bandra-Kurla Complex 专-/email:contact@npci.org.in
Bandra East aa/Website:www.npci.org.in
400051 Mumbai400051

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Annexure
Following fields will be validated on submission of the INPUT file by the sponsor bank,
in addition to the ActiveUMRNvalidation currently inplace
Sr. Field to be ValidationDescription Reject reason to be
no Validated communicated to
sponsor bank by NPCI on
validation failure
Customer The customer a/c no.has to be the "Customer a/c no.
Account same as recorded on the Mandate mismatch with mandate"
Number
Destination Should be same as recorded on the "Destination Bank
BankIFSC/MICR Mandate IFSC/MICR mismatch
with mandate"
Amounta Transaction amount should be same as "Amount mismatch with
recorded on the Mandate, in case where mandate"
this is mentioned on the mandate
4. Maximum Transactionamount shouldbe less than "Amount exceeds
Amount# equaltothemaximumamountrecorded customer mandate"
in the Mandate
5. Start Date Transaction date should be greater than "Transaction cannot be
or equal to the Start date recorded in initiated before Start
the Mandate Date"
6. EndDate/Until Transaction date should be less than or "Transaction cannot be
cancelled equal to the End date recorded in the initiated after End Date"
Mandate.
The status of field Until Cancelled'
should be checked in case the end date
field is NULL
UMRN status 'Active'signifies that the destination bank has validated the details of the mandate raised by
the sponsor bank and hasAccepted/Approved'the mandate for debit transaction initiation. It also signifies
that the mandate has not been cancelled.
of mandate creation.
Page 2 of 3

<!-- Page 3 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Responsibility of NPCI in providing this service
Maintain repository of mandate information
Maintain scanned copy of all mandates as submitted by the sponsor bank.
Validate details submitted in each and every transaction against the information
recorded in the mandate. Fields to be validated are as mentioned in section above.
Reject the transaction at NPCl without sending it the destination bank, in case where
the validation of mandate has failed on any one of the criteria mentioned above.
Provide relevant return reason code to the sponsor bank in all cases of validation
failure.
Handover data and image dump to the bank on request.
Responsibility of Destination Bank
Process the NACH Dr. inward file with the understanding that the file is a pre-validated
file on the mandate variables and good to be debited
Banks may Develop the utility for in-house validating the mandate in the longer run
Banks who have mandate management internally can do validation in addition, which
is optional.
Use NACH GUl utility to approve/reject/cancel/amend a mandate or have the utility to
generate XML file formats for mandate uploading.
Benefits to the Bank
Following are the benefits to the Destination and the Sponsor bank:
1. Destination bank will get pre-validated transactions, these will be good to debit
mandates, and so the bank can rely on NPCl for validating the transaction.
2. Destination bank need not store the mandate information or the image of the mandate
on its servers, as the same will be done by NPCl and handed over to the bank as and
whenrequired.
3. The validation process will also reduce the number of returns to be processed by the
destination bank, as the transactions failing the mandate validation will not be sent to
the destination bank.
4.Cost incurred by the bank for joining NACH Debit platform as a destination bank will be
minimized.
5. On boarding process on NACH Debit will be quickened as there is minimal integration
required with the CBS at the destination bank end.
6. Sponsor bank will be able to immediately identify any transaction failing the mandate
validation in the ACK/NACK file and will be able to make the required rectifications
and upload these validation failed transactions with corrected data.
XX
Page 3of 3
