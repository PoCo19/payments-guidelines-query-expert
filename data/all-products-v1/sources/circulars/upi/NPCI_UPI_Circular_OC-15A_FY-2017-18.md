# Circular 15A - Checklist for PSP SDK - Addendum to circular 15

Circular/reference number: NPCI/UPI/OC-15A/2016-17

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/UPI/OC-15A/2016-17 January27th,2017
To,
All MemberBanks-UnifiedPaymentsInterface
DearSir/Madam,
Checklist for PSP SDK-Addendum to circular 15
As discussed in IBA meeting & UPI Steering Committee, NPCI had issued broad guidelines for merchant on-boarding to
member Banks on 3oth November 2016.It was followed up with UPI Circular No.NPCI/UPI/OC-13/2016-17 dated
8/12/16 &NPCl/UPl/0C-15/2016-17 dated 18/1/2017 respectively, reiterating compliance to 'Merchant on-boarding
guideline&SDKChecklist'.
Matter has been reviewed in consultation with Reserve Bank of India. Accordingly the following checklist should be
submitted to NPCl on a signed letter-head, both for existing and new merchants/P2P providers.
Compliance
Sr. No. UPl Interoperability principals for SDK integration&web enablement status (Y/N)
Bank Board approval in place for distribution of SDKs to large merchants or P2P provider.(As
1) bank needs to assume all liabilities due to breach / security issues in merchant or P2p
providerapp).
2) Name of the merchant/P2P provider:
3) "payby Upl"is equally placed along with other payment options (such as cards /net banking
etc)on merchant/P2p provideronApp/Web.
PSP SDK app should not mandate the customer to register for UPI or create VPA to avail
4) product or services provided.(Enabling condition for other VPA's to be accepted)
Merchant/P2P provider mustgive equal choice to the customer to pay by VPA of his choice
i.e.registered VPA in SDK or any other VPA customer has. (Merchant/P2P provider to use
intent or collect call on App and collect call on web to facilitate customer to use VpA of his
5) choice)
Psp sDK must respond (once customer has registered successfully)to intent calls and collect
6) calls.
PSp SDK must provide an option to customer to de-register & delete VPA (life cycle
7) management)
Psp sDk to provide an option to customer to register the handle as 'defauit'for payment on
8) this specific app during on-boarding process.
a) The'Default'optionprovided shouldbepre-checkedon'No'
If customer has chosenYes',then the Psp sDk is absolved from mandated intent/ collect
b) call onlyforthat"merchantorP2Pproviderservices",
Page 1of 2
1001A,TheCapital,B Wing,10thFloor,Bandra Kurta Complex,Bandra (E).Mumbai 400051.T:+912240009100F:+9122 40009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
Compliance
Sr. No. UPl Interoperability principals for SDK integration &web enablement status (Y/N)
Provision to allow customer to alter the 'Default' option during the life cycle (Change the
c) optionchosenearlier)
9) pSP sDK on-boarding and payment pages should only have branding of the Psp bank.
Pspbank is not sharing any customer data with themerchant/P2P provider,unless specified
10) by industry regulator.E.g.SEBl, IRDA etc. (permitted only for specific regulated merchants).
Noauthenticationdatashared outsidePspbank.
Sharing of NPCI common library is within a wrapper in the SDK for integration purpose (and
11) notgiven'open")
PSP banks should ensure that Merchant/P2P provider Apps are calledas"UPICompliant
12) Apps"andnot"UPIPSPApps"
All above features, must be verified by"Bank's Compliance Team"and given their sign off in
writing to bank's UPI business/technology team to on-board this merchant/P2P provider
13) withPSPSDK.
Compliance
Sr. No. Securitycompliancesand otheressentials status (Y/N)
Bankstoconductthird party (list guidedbyNPCl circular)securityauditof PsPSDK codebase
and submit the clean audit report to NPCl (one time activity unless major changes done
thereafter). If major changes done, it is mandatory for bank do redo the activity.
1)
a) First time report
b) Next release
"Bank's Audit Team" must have given signoff in writing to bank Upi business/technology
team to go live for this merchant/P2P provider.(The PSP SDK integrated merchant orP2P
2) provider final app, must go through the third party security audit and Bank audit team must
haveverified the complianceand obtained clean report)
The data pertaining to customer (including the account details) & device finger printing,
3) resides in bank Data Centre or bank controlled Data centres / Servers with access by bank
authorised personnel only.
As indicated in the circular NPCI/UPI/OC - 15/2016-17 dated 18th January 2017 that merchants /P2P provider not
following guidelines on interoperability or security,transactions shall be declined by NPCl centrally.
Kindlyensurecompliance.
Yours faithfully,
Dilip Asbe
ChiefOperating Officer
Page 2 of 2
