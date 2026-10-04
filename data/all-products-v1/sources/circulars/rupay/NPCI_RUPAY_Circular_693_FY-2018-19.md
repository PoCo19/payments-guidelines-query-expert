# 13-Mar-2018 - NPCI/2017-18/RuPay/040 - Change in response of "Auth_Result" Parameter - "Error Code"

Circular/reference number: NPCI/2017-18/RuPay/040
Date: 01 August 2013

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/2017-18/RuPay/040 March 13,2018
MOST CRITICAL
To,
AllIssuingMemberBanksand IssuerAuthentication Servers (IAS)-RuPay
Dear Sir/ Madam,
Subject:Changeinresponse of"Auth_Result"Parameter-"Error Code"
1.RuPay has established a strong presence in card space in the country.These RuPay cards are
accepted at all ATMs in the countryandon all PoS and ecommerce merchants. In our continued
efforts to ensure secure payment platform and avoid any possibility of'Man in Middle'attack,
we propose Banks to implement changes suggested below.
2. In existing PaySecure platform, we have two APl calls between PaySecure to Issuer
Authentication Server (IAS)vendors, i.e.,"Auth_Initiate"and"Auth_Result"."Auth_Initiate"
allows PaySecure to begin the Cardholder Authentication process with the issuer authentication
server based on the card holder details (Card number, Expiry Date & CVD2) captured at the
merchant / acquiring PG's end, for checking Card Status and Mobile no availability at bank IAS
system.
3. If"Auth_Initiate"APl is successful then PaySecure will open Issuer OTP Page and OTP get
validated successfullybyIssuerAuthenticationServerandreturn thestatustoPaySecure.After
successful validation of the OTP,"Auth_Result"APl call will be triggered to securely query the
resultofauthentication.
4. In all our suspected transactions, post validating OTP, Issuer is responding with status
"issUER1oo",which means'OTPis invalid',butwereceived inPaySecure systemresponsecode
as"issUERooo", which means'Authentication Successful.Further to this, it was also observed
that for"Auth_Result"calls, IAS is responding in parameterfor'Status'tag as"Failure", but for
theError Code'tag lASis sending value of"o/oo",which means successful.Hence, PaySecure is
continuingwithtransactionstoproceedforAuthorizationleg.
5. It may be noted that as per"RuPay-eCommerce Issuer Integration Guide Version 1.2", dated
01 August 2013 (Page # 45 & 46), clearly highlights the expectations from 1AS vendors w.r.t
responses for the two calls"Auth_Initiate"and"Auth_Result"mentionedabove.
6.In case of all suspected transactions, it was observed that the IAS vendors of all impacted Banks
were responding to “Auth_Initiate" calls correctly by declining the transactions with 'Invalid
OTp' error code, however, NPCl PaySecure systems were not getting such transactions as
InvalidOTp'errorcode,instead,thetransactionswerereceivedwithsuccessful response.Due
1001A,TheCapital,BWing.10thFloor.Bandra Kurla Complex,Bandra(E),Mumbai400051.T:+912240009100F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

to this successful response, as per PaySecure flow,“Auth_Result" calls were made to IAs
vendors and it is here that the responses given by the IAs vendors were not as per the
specifications.
7.We havevalidated the logs submitted by the IAS vendors on behalf of few member Banks and
fraudulent transactions,"Auth_Initate"calls were responded by the IASvendor as"ssuerloo",
which means'oTP invalid,however, NPCl PaySecure system received these responses with
response code"issuerooo",which means successful.This could have been possible onlyif there
is"ManinMiddle"(MiM)attack.
8. While there are appropriate rules implemented by all Banks and their vendors, to curb frauds
and bring transparency & control, we request all Banks and vendors to respond to any such
"Auth_Result"call from Paysecure to IAS where IAS has recorded the OTP validation result as
anything otherthan"isSUERooo"with'ErrorCode' in response as'96'(System Error).This would
be monitored at PaySecure for necessary course correction.
We request members to take a note of the same and bring the contents of this circular to the
implementation at the earliest. Do advice if any support is required from our end. For any queries
please feelfreeto contact MrNeelesh Gupta (neelesh.gupta@npci.org.in/9082741856).
Yours Faithfully,
VishalAnandKanvaty
Svp-Product&Innovation
