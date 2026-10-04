# UPI OC 123 - Industry best practice to handle Mandate Digital Signature Certificate (DSC)

Circular/reference number: OC-123

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTSCORPORATION OF INDLA
NPCI/UP//OC123/2021-22 03rd November,2021
To,
All Member Banks, Unified Payments Interface (UPl)
Dear Sir / Madam,
Subject: Industry best practices to handle Mandate Digital Signature Certificate (DsC)
Unified Payments Interface (UPl) platform has become the most preferred retail payment option
for Users. UP has registered over 4.21 bilion transactions in October 2021 and the same is
expected to grow significantly in the current financial year (F.Y 21-22).
Mandates are an important feature in UPl having multiple use cases. Recurring payments is one
such use case that has a lot of potential to grow significantly. Proper controls have to be put in
place by all the stakeholders while creating recurring mandate and executing the same.
The following are advisory which the banks needs to follow:
1. Validity of UPl Recurring Mandate
The PsPs of the Merchants and Aggregators are advised to create the Recurring Mandates
with a maximum validity of 30 years. As the Recurring Mandates shall be valid for 30 years,
an Issuer Bank can implement the below mentioned best practices while creating and
processing Recurring Mandates.
2. Mandate Creation:
a. Issuer Bank has to ensure that the signatures for Recurring Mandate are affixed by
using a 'valid' Digital Signature Certificate (DSC) only.
b. Issuer Bank shall renew the DSC well before its expiry of the DSC.
C. The PKI Certificates Algorithm and Key strength should be RSA (SHA 256) / 2048
or above.
1001A, The Capital, B Wing, 10th Floor,
BandraKurla Complex, Bandra(E), Mumbai4oo O51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.inwww.npci.org.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
3.Mandate Execution:
a. Issuer bank has to verify the DsC by using the same Public key that was used to
create/ apply the DSC.
b. Issuer bank may develop the capability to maintain multiple public keys even after
the DsC is expired to use for the purpose of validation only.
c. Once the DsC is expired, Issuer Bank shall have a provision to focally store the
DSC's issuer certificate and Certificate Revocation List (CRL) at the time when the
Recurring Mandate was created. For verification purposes, it is recommended to
use long term archival signature format.
d. As a best practice, CRL and Online Certificate Status Protocol (OCSP) shall be
maintained by lssuer Bank to ensure that revoked certificates are formally listed with
respective Certifying Authorities or as recommended by the banks.
Member are requested to inform to the relevent stakeholders to ensure that the above mentioned
best practices are followed.
Yours truly,
SD/-
Praveena Rai
Chief Operating Officer
1001A, The Capital, B Wing, 10th Floor,
BandraKurlaComplex,Bandra(E),Mumbai4oOo51.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.in www.npci.org.in
CIN: U74990MH2008NPL189067
