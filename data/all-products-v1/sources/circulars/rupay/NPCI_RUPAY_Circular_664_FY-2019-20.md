# 11-Oct-2019 - NPCI/2019-20/RuPay/047 - Migration to Bharat eCommerce Payment Gateway (BEPG) from existing eCommerce platform

Date: 11th October, 2019

<!-- Page 1 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
Circular: NPCl/2019-20/RuPay/047 11th October, 2019
To All Member Banks - RuPay
Dear Sir/Madam,
Subiect - Migration to Bharat eCommerce Payment Gateway (BEPG) from existing
eCommerce platform
In 2018, NPCl worked with member Banks to upgrade eCom transactions workflow from
iFrame based methodology to URL redirection and during the same time RBl mandate w.r.t
supporting Hashing' capabitities for eCom transactions were also certified for the member
Banks. To further improve the consumer experience and overall performance, NPCl has
created a new e-Commerce solution BEPG to enhance the customer experience and to
change ourselves according to the market trends. Apart from supporting existing features of
current eCommerce platform, BEPG will support a host of additional features.
Benefits of BEPG:
Enhanced consumer experience
Additional payment options on RuPay cards
No compromise on security and risk
Simplified architecture
Improvement in success rate
Self-healing system
Highlights of BEPG:
Sr. What's New?
No.
Platform BEPG provides currently available functionalities of
Enhancements eCommerce system
Server to server API for 'OTP Generation and OTP
Validation' during 'Authentication' of transactions.
Tokenization for In-App merchants and 'Card on File' to
simplify consumer experience.
Quick checkout functionality where registered RuPay
consumers can do transactions without Additional Factor of
Authentication (AFA)
Connected checkout functionality where Trusted Merchants
can participate to register RuPay consumers to facilitate
transactions without Additional Factor of Authentication
(AFA).
1001A,TheCapital,BWing,10thFloor,
Bandra Kuria Complex, Bandra (E), Mumbai 400 O51.
T: +91 22 40009100 F: +91 22 40009101 www.npci.0rg.in
CIN: U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONAL PAYMENTS CORPORATION OF INDIA
Feature Amount and merchant name has been added to Issuer
Enhancements Authentication System (IAS) API call for consumer friendly
OTP delivery.
Online reversal message for payment gateways have been
introduced to facilitate CNP reversals..
Subscription based transaction lifecycle has been added,
which is aligned with policies that are discussed with
regulatorfor approvals.
Equated Monthly Instalments (EMi) solutions introduced for
both Credit and Debit products.
10 Refund based on Original Credit Transfers (OCT) for
quicker refund process to consumers
11 Card to card payments for Credit card payments and
balance transfer transactions for Credit cards
Implementation Details:
BEPG migration will have two phase implementation approach as described below
Sr. No. Phase I -Phase II
"As Is" Migration Features Enhancements
All features as supported by New  featureenhancements to be
existing eCommerce platform will developed by. member banks and
be  extended through BEPG certified through BEPG platform
platform.
Issuer Consume new IP Addresses (of Develop and certify new features as per
Bank BEPG platform) as given by NPCI specifications anytime post 12th
Actionable NPCI on or before the 12th November, 2019
November, 2019
Acquiring Consumer new IP Addresses (of Develop and certify new features as per
Bank BEPG platform) as given by NPCI specifications anytime post 12th
Actionable NPCI post 12th November, 2019 November, 2019
as per NPCl communications
NPCI wil! separately
communicate with acquiring
banks batches for due
migration between 12th
November, 2019 iun 15th
January, 2020.
Note: - The migration will be "As is" i.e. the specification will remain the same as it is
on existing eCommerce platform. No deveiopment is required on both Issuing and
Acquiring side required for "As is" migration.

<!-- Page 3 -->

NPCL
NATIONALPAYMENTS CORPORATIONOFINDIA
Phase I- From Issuer perspective following changes have to be implemented
Initially, all Issuer Banks who are enabled in the current eCommerce platform will be on-
boarded to the new BEPG System with following pointers:
current eCommerce platform credentials before acquirers start migrating to BEPG.
Issuer must not delete the existing credentials while adding the new ones.
b. Until all acquiring Banks are migrated to BEPG platform, for a limited period of time,
Issuer will get the transactions from both BEPG and existing eCommerce platforms.
c. E Existing eCommerce platforms will continue to process domestic transactions for
acquirer which are yet to be migrated to BEPG system until all acquiring banks are
migrated to BEPG platform.
103.14.161.111
Issuer
103.14.162.111
Issuer needs to whitelist the new BEPG credentials on or before 12th November, 2019
Phase I-From Acguirer perspective following changes have to be implemented
Acquirer migration will begin once all the issuers have whitelisted the required credentials
with following pointers: -
a. Acquirer needs to whitelist the new BEPG URL and IP address.
b. Acquirer.Banks will be migrated in phases, one after the other based on volume.
NPCl will separately communicate with acquiring banks in batches for due migration
between 12th November, 2019 until 15th January, 2020.
C. Acquirer needs to ensure that all the necessary pre requisites are in place (within 15
communication from NpC!.
nttps://bepg.npci.org.in/bepg/online/api/chkout/xml/soapservice
Acquirer 103.14.161.113
103.14.162.113
Phase Il-From Issuer and Acguirerperspective
Necessary development as per NPCl specification needs to be done by the member banks
will be released shortly.
All Member Banks are requested to kindly take a note of the aforesaid. For any queries, you
may please contact your relationship manager. .
Yours faithfully,
Praveena Rai
Chief Operating Officer
1001A,The Capital, BWing,10thFloor,
Bandra Kurla Complex, Bandra (E), Mumbai 4oO 051.
T: +91 22 40009100 F: +91 22 40009101
contact@npci.org.inwww.npci.org.in
CIN:U74990MH2008NPL189067
