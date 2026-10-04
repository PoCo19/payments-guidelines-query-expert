# IMPS | OC 124 | FY 25-26 | Implementation of Fraud Chargeback Option for Fraudulent Transaction

Circular/reference number: OC-124

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/IMPS/0C N0.124/2025-2026 April 02, 2025
To,
All Members of Immediate Payments System (IMPS)
Subject: Implementation of chargeback option for fraudulent transactions.
In order to facilitate the banks to raise chargeback under fraudulent transaction category it has been
decided to implement necessary changes in the IMPS chargeback flow.
Key Changes in the Revised Process:
Chargeback of fraudulent transaction can be raised by the remitting banks, front end and bulk,
both the options are made available in the IRCS.
Beneficiary bank will have to accept, reject with TAT otherwise on completion of TAT, the
chargeback shall be deemed accepted.
All the chargebacks raised on fraudulent transactions which are accepted, rejected and deemed
accepted are made available in the existing adjustment report.
Separate line item is updated in the DSR/NTSL for member banks to identify the settlement for
such chargebacks.
All the participant banks (as beneficiary) are advised to put best efforts to recover the funds and
accept the chargeback upon recovery.
IRCS will allow to raise re-presentment immediately after the chargeback is raised, there is no
minimum cooling period set for re-presenting the chargeback. Hence, participant banks are
advised not to reject the chargebacks immediately after chargeback is raised.
Remitting banks may provide the FIR copy to beneficiary banks for faster resolution of
chargebacks.
- Refer Annexure -- 1 for the rules set for handling the chargeback on fraudulent
transactions viz. TATs, adjustment lifecycle, adjustment flags, reason codes, fund
movement etc.
Refer Annexure - 2 for DSR/NTL line items
- Refer Annexure - 3 for Adjustment report.
The above functionality will be implemented in IRCS with effect from Apr 20, 2025.
Member banks are advised to take a note of the above and disseminate the infornation contained herein
to the officials concerned.
Warm Regards,
SD/-
Giridhar GM
Chief -- Customer Success
Annexure - I (Fraud Chargeback Rules)

<!-- Page 2 -->

NPCI
NATIONAL PAYMENTS CORPORATIONOFINDIA
Dispute Type Flag Reason Code Reason Code Description Actioned BY Fund Movement
Fraud Chargeback Chargeback on Fraudulent Remitting Debit Credit
Raise FC 128 Transaction 45 Bank Beneficiary Remitting
Bank Bank
Fraud Chargeback The amount has been recovered Beneficiar
Accept FCA 129 successfully from the fraudulent 25 y Bank NA NA
customer's account
Fraud Chargeback Lien marked; however, Beneficiar Debit Credit
Representment FCR 130 customer account is not having 25 y Bank Remitting Beneficiary
sufficientbalanceto debit Bank Bank
Fraud Chargeback FIR Copy not provided for the Beneficiar Debit Credit
Representment FCR 131 disputed transaction 25 y Bank Remitting Beneficiary
Bank Bank
Fraud Chargeback Beneficiar Debit Credit
Representment FCR 132 Others y Bank Remitting Beneficiary
Bank Bank
Fraud chargeback If fraud chargeback is not
deemed FCA 133 then same has to be settled on accepted rejected within TAT, 25 IRCS NA NA
acceptance deemed acceptancebasis.
Annexure - 2 (DSR NTSL Line Items)
National Payments Corporation of India
Immediate Payment Service
Daily Settlement Statement for ndlbank Updated-IMPs as 0n 11-03-2025(5c 09:00:00 To 11:00:00)
Description No of Txns Dehit Credit
Fraud Chargeback Raise
FraudChargebackRaiseFROMNT1 ddd/506414777091/2025-03-05/F3 200000
FraudChargebackRaiseFROMNT1 test/506212894995/2025-03-03/FC 009
Fraud Chargeback Raise TO NT1 Ccc/503618770148/2025-02-05/FC 50
Total Fraud Chargeback Raise Amount 200500 50
Fraud Chargeback Representment
FraudChargebackRepresentmentTONT1 dddd/5064147770912025-03-05/F3 200000
Total Fraud Chargeback Representnent Amount 200000
RepresentmenRaise
Representmer TO NT1 CCC/506414728946/2025-03-05/F3 200000
Total Re-presentment Ralse Amount 200000
Ainexure-3 (Adjustment Report ADJTYPES & REASON CODES)
Adjtype Reason Code
Fraud Chargeback Raise 128
Fraud Chargeback Representment 130
Fraud Chargeback Raise 128
Fraud Chargeback Raise 128
Fraud Chargeback Raise 128
Fraud Chargeback Raise 128
Fraud Chargeback Accept 129
Fraud Chargeback Representment 131
Fraud Chargeback Representment 132
