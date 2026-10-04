# 15-Jun-2021 - NPCI/2021-22/RuPay/012- Tokenized Transaction Identifier in ...

<!-- Page 1 -->

NPCL
NATIONALPAYMENTSCORPORATIONOFINDIA
NPCl/2021-22/RuPay/012
June 15, 2021
Tokenized Transaction Identifier in the BCS RGCS application (Domestic)
In reference to the RuPay Tokenization Program, We are introducing an identifier in the settlement files for the
identification of the Tokenized Transactions. The identifier will enable the Issuing and Acquiring banks to
acquiring banks and will be de-tokenized before they are forwarded to the issuing bank.
To incorporate the indicator for tokenized transactions, Subfield 2 in the existing tag "nATD" will be used
Subfield 2 is provided in the data files for DMs transactions to both Acquirers and Issuers, Presentment, Offline
Presentment and Presentment reversals to issuers.
Existing Field for Utilization
Field Name : Additional Transaction Data
Xml Tag : <nATD>
Type : ANS16
Subfield 2: Tokenised transaction identifier
Value Description
Tokenised Transaction
Space Not a Tokenised Transaction
The nATD field will be populated as below scenarios:
Transaction Type
Subfield 2 nATD tag values
Not a small scale merchant but a Tokenised transaction
Neither a small scale merchant nor a tokenized transaction Space
Small scale merchant tokenized transaction
"ST"
Small scale merchant but not a tokenized transaction Space "S
Page 1 of 2

<!-- Page 2 -->

NPCI
NATIONALPAYMENTS CORPORATIONOFINDIA
The nTAD tags shall be made available in the following Clearing Reports for RuPay:
87 - DMS Approved Transactions -Acquirer
i. 88 - DMS Approved Transactions -Issuer
o1 -Online Presentment and Presentment Reversal Transactions
iv. o5-OfflinePresentment and Presentment Reversal Transactions
Apart from above files, a new column has been introduced in the "Money Add Report" to identify tokenised
transaction:
File Name Transaction Type Value
Money Add Report Indicator to identify tokenised transactions:
1. T- Tokenized Transaction
2. Space - Not a tokenized transaction (Value would be "
We request participating member banks to take a note of the above and disseminate the changes
implemented to the officials concerned.
Yours faitkfuly
Praveena Rai
Page 2 of 2
