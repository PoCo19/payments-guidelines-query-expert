# NETC | OC 001 | FY 26-27 | System changes in NRCS to mandate submission of supporting evidence for Dispute Resolution

Circular/reference number: NPCI/2026-27/NETC/001
Date: 15th May 2026

<!-- Page 1 -->

NPCI/2026-27/NETC/001 
 
 
 
 
 
                  April 06, 2026 
To, 
All Members of NETC 
 
Subject: System changes in NRCS to mandate submission of supporting evidence for 
Dispute Resolution 
Reference may be taken from NPCI NETC Circular NPCI/2025-26/NETC/005 dated October 
28,2025 which listed the reason codes available in NRCS for Debit Adjustment and 
Chargebacks along with guidelines on evidence required for each reason code. It was also 
stated that NPCI would be implementing system controls to ensure compliance from the 
member banks to the referenced circular. In line with this notification, system controls are 
being implemented in NRCS to ensure disputes submitted with no evidence would be rejected 
with the following reject reason, for reason codes where submission of evidence is mandatory.  
NRCS Reject Reason code 
Reason Code Description 
5229 
Rejected as no evidence uploaded for the chargeback 
reason. 
It may also be noted that: 
• 
Above system control would be limited to the following three function codes – 
763(Debit Adjustment), 450(Debit Chargeback raise) and 205(Representment raise). 
• 
The above-mentioned system controls would also cover new reason codes that will be 
introduced in NRCS in future where evidence is required for raising or responding to 
chargebacks.  
The above controls shall be implemented in NRCS with effect from 15th May 2026. The dispute 
reason codes and details on whether evidence is mandatory or optional for the reason code 
is listed in Annexure – I. 
The information herein may please be disseminated to all the concerned officials. 
 
Regards, 
 
Sd/- 
Giridhar G M 
Chief – Customer Success

<!-- Page 2 -->

                                                 
 
 
Annexure I 
In the below table, wherever the evidence check is indicated as Optional, it implies that 
mandatory evidence submission is not mandated for those cases. However, this should not 
be construed to skip submission of evidence where it may be applicable. In scenarios where, 
based on the specific use case or dispute reason code, submission of evidence is required to 
raise a chargeback, the same should be provided to enable the Issuing Bank/Acquiring bank 
to clearly understand the dispute and take appropriate action. 
1) For raising Debit Adjustment - Function Code 763: 
Reason Code 
Reason Code Description 
Evidence submission 
(Mandatory/Optional) 
1008 
DA raised on vehicle class mismatch 
Mandatory 
1009 
DA raised on vehicle number mismatch 
Mandatory 
1010 
DA for plaza following non-standard Vehicle 
Classification 
Mandatory 
 
2) For raising Chargeback - Function Code 450: 
Chargeback 
Raise Reason 
Code 
Reason Code Description 
Evidence submission 
(Mandatory/Optional) 
3001 
NETC Toll services not availed/ Tag holder 
does not recognize the transaction 
Mandatory 
3002 
Duplicate transaction done at Toll Plaza 
Optional 
3003 
Vehicle was in exempted list 
Mandatory 
3004 
Vehicle was in blacklist 
Optional 
3005 
Vehicle was in low balance  
Optional 
3006 
Toll fare calculation error 
Optional 
3011 
Paid by other means 
Mandatory 
3023 
Wrong DA raised on vehicle class mismatch 
Mandatory 
3024 
Wrong DA raised on vehicle number mismatch 
Mandatory 
3025 
Wrong DA raised on plaza following non-
standard vehicle classification 
Mandatory 
3026 
Return Journey discount not provided 
Optional 
3027 
Toll Fare Calculation error on Closed loop 
plaza 
Optional 
3028 
Connecting Plaza benefit not provided 
Optional 
3029 
Pass benefit/Local discount not provided 
Mandatory 
3030 
Exemption not provided for EV vehicle at 
Exempted plazas 
Mandatory 
 
3) For representing Chargeback - Function Code 205: 
Reason 
Code 
Reason Code Description 
Evidence submission 
(Mandatory/Optional) 
4001 
Supporting Documents for services 
availed/valid transactions 
Mandatory 
4002 
Supporting Documents for multiple passing 
Mandatory 
4003 
Proof of Vehicle is not in exempted List 
Optional 
4004 
Proof of Vehicle is not in blacklist 
Optional 
4005 
Proof of Vehicle is not in low balance list 
Optional

<!-- Page 3 -->

                                                 
 
4006 
Proof of valid Toll Fare calculation 
Mandatory 
4007 
Proof of valid Vehicle class 
Optional 
4008 
Proof of successful response 
Optional 
4009 
Proof of successful signature validation 
Optional 
4011 
Valid DA, as vehicle passing is of higher class 
with same VRN 
Optional 
4012 
Valid DA, as vehicle passing is of higher class 
with different VRN 
Optional 
4013 
Valid DA, as plaza follows Non-standard 
Vehicle Classification 
Optional 
4014 
Return Journey discount provided 
Mandatory 
4015 
Return Journey discount not applicable at 
plaza 
Optional 
4016 
Return Journey Logic applicable for 24Hrs 
Optional 
4017 
Return Journey Logic applicable for 12Hrs 
Optional 
4018 
Return Journey Logic applicable for Same day 
Optional 
4019 
Toll Fare Calculation is correct for the 
Entry/Exit combination 
Mandatory 
4020 
Higher fare charged as per concessionaire 
agreement for missing Entry/Exit 
Mandatory 
4021 
Toll Fare for Connecting Plaza benefit is 
provided to Customer 
Mandatory 
4022 
Pass benefit/Local discount benefits provided 
Mandatory 
4023 
Pass/Local discount is expired or not 
applicable 
Optional 
4024 
Forged RC Copy/required document not 
submitted by the Issuer 
Optional 
4025 
Customer carrying Tag in Hand 
Mandatory 
4026 
CB on Return journey transaction raised on 
Incorrect Txn ID 
Optional 
4027 
CB on Duplicate transaction raised on 
Incorrect Txn ID 
Optional 
4028 
Not a duplicate transaction as per IHMCL 
duplicate transaction Policy 
Optional 
4029 
Vehicle passing has a VRN different compared 
to the Fastag 
Mandatory
