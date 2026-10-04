# Circular 95 - Guideline on usage of UPI APIs’

Circular/reference number: NPCI/UPI/OC-95/2020-21
Date: 25th September 2020

<!-- Page 1 -->

 
1001A, The Capital, B Wing, 10th Floor,  
BandraKurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101 
contact@npci.org.inwww.npci.org.in  
CIN: U74990MH2008NPL189067 
 
 
 
 
NPCI/UPI/OC-95/2020-21                                                                        25th September 2020 
To, 
All Members, Unified Payment Interface  
Dear Sir/Madam,  
Subject: Guideline on usage of UPI API’s 
Unified Payments Interface (UPI) provides a set of standard APIs to facilitate online immediate 
payments for both person to person (P2P) and person to merchant (P2M). The core features of 
UPI, both financial and non-financial, are delivered using these specific API’s. These API’s are 
consumed by the participating members in UPI to service customers using UPI enabled apps, 
Third Payment Application providers (TPAPs).  
2. From time to time, NPCI has issued guidelines defining the message specifications and 
intended purpose of these APIs and the usage of the information retrieved from these API’s. 
For e.g. List Account API should be used only for linking of account in the process of handle 
creation with device binding and not otherwise. Likewise, the Balance Inquiry API can be only 
initiated by the customer on the UPI app and the actual balance cannot be used or stored even 
in encrypted format by any player in the UPI chain for any purpose except customer’s bank 
(Ref UPI OC No. 44 dated 11th January 2018). The customer data (PII Data – Personally 
Identifiable Information such as account number etc.) to reside in bank or bank owned data 
center and the same should not be passed to any party including that of Merchant or 
Intermediary unless specified by the industry regulator (RBI, SEBI, IRDA, etc.) as the 
regulatory requirement or otherwise approved by NPCI specifically (Ref circular no UPI OC 
No.15 dated 18th January, 2017 & UPI OC No. 15A dated 27th January 2017). 
3. The use of the UPI set of APIs by the participating members should strictly follow the usage 
norms as is defined in the UPI Technical Specification Document and as mentioned below:- 
a) For the purpose of processing the financial or non-financial transaction initiated by the 
end UPI consumer 
b) For the purpose of Risk management and fraud prevention purpose 
c) Or otherwise specified by NPCI

<!-- Page 2 -->

 
1001A, The Capital, B Wing, 10th Floor,  
BandraKurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101 
contact@npci.org.inwww.npci.org.in  
CIN: U74990MH2008NPL189067 
 
 
 
Any other use of APIs especially, the stand-alone use of APIs for purposes other than it is 
intended for, is not permitted unless approved, other than above listed reasons. Non-
compliance to this guidelines shall be treated as breach of UPI operating guidelines and NPCI 
shall have the right to take suitable action against the member, if it is found in violation. 
Members are requested to take note of this compliance, and communicate this to their 
partners. 
 
Yours Faithfully,  
 
SD/- 
Praveena Rai  
Chief Operating Officer

<!-- Page 3 -->

 
1001A, The Capital, B Wing, 10th Floor,  
BandraKurla Complex, Bandra (E), Mumbai 400 051. 
T: +91 22 40009100 F: +91 22 40009101 
contact@npci.org.inwww.npci.org.in  
CIN: U74990MH2008NPL189067 
 
 
 
 
Annexure to NPCI/UPI/OC-95/2020-21 dated 25th September, 2020 
List of UPI API’s 
Reqpay  
List PSP 
RespAuthDetails 
List Account Providers  
ReqAuth 
List Keys 
ReqTxn 
List Account  
RespPay 
List Verified Address Entries 
  
Manage Verified Address Entries  
  
Validate Address 
  
Set Credentials  
  
Pan API, 
  
Bal Enquiry  API 
  
List  VAE 
  
Reqval customer  
  
Mandate API  
  
QR validation API  
  
Check Transaction 
  
Req OTP 
The circular extends to all future API’s released on UPI framework, unless specified otherwise.
