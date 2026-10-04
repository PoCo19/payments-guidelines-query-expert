# Circular 56 – Rollout of UPI 2.0

Circular/reference number: NPCI/UPI/OCNo.56/2018-19

<!-- Page 1 -->

NPCI
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCI/UPI/OCNo.56/2018-19 August 14,2018
To,
AllMemberBanks-UnifiedPaymentsInterface(UPl)
Dear Sir/Madam,
Subiect:Roll out of the features of Unified Payments Interface (UPl) 2.0
1)Onetimemandatewithblockfunctionality:
With this feature, consumer can pre-authorise a transaction and block the funds in his account for a
debit to be initiated later. UPl Mandate can be used in scenarios where money is to be paid later
after obtaining the service; however the money in the account gets blocked instantaneously. The
customer's account shall get debited when the UPl Mandate is executed by the merchant or payee.
The mandate is digitally signed and stored at customer's account holding bank and also with
customer's PsP bank (app providing bank). During the debit, the customer's account holding bank
and customer's PsP bank need to validate the digital signature and verify the parameters.
Details:
The mandate shall have key parameters such as"purpose code",“from & to date","amount"&
"frequency" (set to 'One time").
Customer can authorize one time use mandates to different or same payee's at the same time.
UPI mandate can be created by push or pull transactions i.e. QR, Intent, Collect or by create
(P2P)transaction.
A UPl Mandate creation is fully authorized by the consumer by two factor authentication using
“what you know' (UPI Pin) and ‘what you have'(Device binding).
User/Merchant can Create, Modify or revoke the UPi Mandate as per defined rules. For some
use cases themodificationmaynotbe allowed or allowed only upto specific date
UPl mandate can be executed up to the amount authorized by the consumer. Once executed
and if partial, the remaining amount is returned to the customer's account. The customer's bank
shall remove the block after expiry of the mandate.
Till the time mandate is executed, the funds remain in blocked condition in customer's account
and he/she continues to earn an interest depending on the type of underlying account.
mandatory.
1001A,The Capital,BWing.10thFloor,Bandra Kurla Complex,Bandra(E),Mumbai 400051.T:+912240009100 F:+912240009101www.npci.org.in
CIN:U74990MH2008NPL189067

<!-- Page 2 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
In case of revocation (wherever permissible), the block on the money should be released
immediately reinstating the money to the customer's account. The revocation date should be
prior to the execution date/ expiry date.
The bank providing mandate with block functionality shall return 2 amounts on balance inquiry
i.e.available and actual/usablebalanceor SanctionedLimit andDrawingPower.All UPlApps
needto display the same1.
2)Over-Draft (OD)accountas an underlyingaccount in UPl
Currently savings and Current account addition is permissible in UPl. Now, with this additional
feature, the user can also link an overdraft account provided he/she is found eligible to avail an OD
byhis/herbank.
For any OD accounts, whenever a customer needs to check balance of his OD account, customer's
bank shall return 2 balances i.e.available & actual/usable balance.All UPl Apps need to display the
same1.
Details:
UPl acts as a digital channel for accessing the OD account. On-boarding and registration
processes forOD account remains same as the existing CASA accounts.
Customer discovers/fetches the existing OD account and links to UPIfor transaction.
Customer has a choice to set new UPI ID/UPIPin or use existing UPI ID/UPI Pin (used for
current linked UPl account), as decided by his/her bank.
A transaction to OD linked UPI ID would mean a repayment of OD by the customer.
accounts, only P2M transactions are permissible (excluding the categories prohibited by any
regulator).
Bank is responsible to get agreement on terms and conditions agreed with the customer.
All existing UPl dispute management rules shall apply for the transactions.
The OD providing bank must take the required consumer consent and make him aware about
the terms and conditions of taking OD from the bank.
The OD providing banks must communicate to the customer the due dates, outstanding amount
interest charges or any such information required atregular basis.
'Customer Sensitive payment data'. Members may refer UPI circular no NPCI/UPI/OC No. 44/2017-18 dated January 11h
2018.ThisappliestoUPI2.0equally

<!-- Page 3 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
3)InvoiceintheInbox(Viewattachment&pay)
Using this feature customer can check/verify the invoice or attachment prior to authorizing the
availedbyverifiedmerchants.
Details:
This creates a provision by which the merchants can share Invoices with customers before
the transaction is authorized.
This provision requires all UPl Apps to display an option -'Click on attachment to view
details' or equivalent and open the same in a browser or equivalent display with the facility
of'Return'backtothemain app,totheuser.
This option is feasibleforcollect, intent and QR code based transactions.
Transaction history details should also reflect the link under which the Invoice was
presented and the same should be retained for at least 2 months by the merchant.
4)SignedIntent/QR
Signing of Intent / QR provides more security while making payment by the customer. Member
banks shall convert software based UPI QR codes (dynamic and static) by December 31, 2018 and
physical UPIQRcodes (static)byMarch31,2019.
5) UPlpertransactioncapmovedto2L
User can now use higher amount on transaction for specific use cases as agreed by the steering
committee of UPl.
For any clarifications on the features you may please contact the following:
>Upi.product@npci.org.in
Yours faithfully,
Vishal Anand Kanvaty
SVPand Head-Products andInnovations
