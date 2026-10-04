# IMPS I OC 16 I FY 13-14 I Immediate Payment System (IMPS) Merchant Payments - Alternative Flow

Circular/reference number: NPCI/IMPS/OCNo.16/2013-14/

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/IMPS/OCNo.16/2013-14/
June6,2013
To,
AllMemberBanks/PrepaidPaymentInstrumentIssuers(PPis)of IMPS
DearSir/Madam,
Immediate Payment Service (IMPS)Merchant Payments-AlternativeFlow
In the current IMps merchant payments model, the customer is able to do funds transfer to merchant
by providing his mobile number, MMID,and OTpthrough an merchant user interface comprising of
web, or IVR, or handheld device.Customer generates One Time Password (OTP) using the Bank's
Annexure I.
payment process as the OTP generation step is found cumbersome by the user and hence becoming
stumbling block in proliferation of pull based merchant payment.
Accordingly, an alternative transaction flow was suggested for low value transactions of ticket size of
Rs.500o/and below wherein the Acquiring Bank will berequired capturecustomer M-PIN instead of
OTP, via the IVR call. The detail of the above solution is as provided in Annexure Il and has been
approved byRBl.
From customer education point of view,this solution is very simple,as there will be standard process
irrespective of the customer Bank. Currently, for OTP generation, customer needs to follow the process
as defined by the Bank, and that is different for different Banks. Instead of OTp and MMID,we are
asking the customer to enter his M-PiN only,this eliminates the requirement for the customer to know
his MMiD and to generate OTp beforehand, hence making the transaction process easier for the
customer.
Following guidelines shall be applicable for security of M-PiN captured by Acquiring Bank:
a.M-PINshallbecapturedoverIVRcall
Page 1of2
C-9,8th Floor cT/Phone:02226573150
RBi Premises /Fax:02226571001
Bandra-Kurla Complex 专/email:contact@npci.org.in
Bandra East a/Website:www.npci.org.in
400051 Mumbai400051

<!-- Page 2 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
b. Two-factor authentication - IvR call shall be made to customer mobile number
registered with the Bank. Customer needs to enter M-PIN during IVR call. If the mobile
number of the customer is not registered with the Issuing Bank, then the transaction
will be declined;
C. Transactionlimitshall beRs5,ooo/-usingM-PiN,
For highertransaction limit,customerneeds to enterOTP generated through encrypted
means,
e. M-PINorOTPshallbecapturedbyAcquiringBankonly,
From Acquiring Bank,M-PIN or OTP shall beencrypted with Triple-DES using HSM
based on the same logic as followed by NFS. This shall be decrypted at NPCI HSM,
encrypted again at NPCI HSM with Issuing bankkey,and decrypted at Issuing bank (
Usageof HSMispreferablebutitisnotmandatory)
This transaction flow is similar to card-not-present transaction over IVR, hence all
relevant securityprotocolsshould beemployedas theyareemployed forprotectionof
card data traveling on IVR
h.Acquiring Bank shall notstoreM-PINorOTPcapturedduringIVRcall.
We request you to take steps towards implementation of the alternative flow.This solution can be used
very effectively for over-the-counter payments between customer and merchant and can help bring
manymerchantsuseelectronicpaymentsforreceivingfundsfromtheircustomers.
Yours sincerely
SD/-
Dilip Asbe
Chief Techhology Officer
Encl:As above.
Page 2 of 2
98价 C-9,8th Floor r/Phone:02226573150
RBIPremises q/Fax:02226571001
Bandra-Kurla Complex 专/email:contact@npci.org.in
ph Bandra East c/Website:www.npci.org.in
400051 Mumbai400051
