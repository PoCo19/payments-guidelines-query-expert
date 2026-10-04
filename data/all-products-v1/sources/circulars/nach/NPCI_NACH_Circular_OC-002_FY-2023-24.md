# Circular No. 002 - Introduction to IQA validation on MMS mandates

Circular/reference number: NPCI/2023-24/NACH/002

<!-- Page 1 -->

NACH
NATIONALAUTOMATEDCLEARINGHOUSE
NPCI/2023-24/NACH/002 May 04, 2023
To,
All NACH Member banks,
IntroductiontoIQAvalidationonMMSmandates
Mandate Management System (MMS) helps in the creation, amendment, and cancellation of
mandates used for NACH debit transactions. In order to ensure better quality of images to
facilitate processing, it has been decided to introduce Image Quality Assurance (IQA).
Technical specifications for IQA validation are provided in Annexure I. The images that are
not in compliance with the standards will be rejected by the system.
The validation will be implemented with effect from July 01, 2023
Member banks may please take note and disseminate the information herein to ali the
concerned. If any clarification is required you may please raise the same through CRM.
With warm regards,
Giridhar G.M
(Chief Offline Products Operations & Technology)

<!-- Page 2 -->

NACH
NATIONAL AUTOMATED CLEARING HOUSE
Annexure 1:
Following validations will be done for the images uploaded in Mandate process.
Image Size -- Image Size validation continues as we have in current system.
Max allowed size of front Image: 100000 bytes
Max allowed size of detail Front Image: 100000 bytes
Height - Height of the image will be validated by MMS application, if Height of the
image exceeds defined value then mandate will be rejected with reason "lmage Height
should be less than or Equal To Allowed Height"
o  Max allowed height of Images: 2000 Pixels
Width -- Width of the image will be validated by MMS application, if Width of the image
exceeds defined value then mandate will be rejected with reason "Image Width should
be less than or Equal To Allowed Width".
o Max allowed width of Images: 4000 Pixels
x_resolution- DPl values will be calculated for X resolution (Horizontal resolution).
Image's horizontal resolution should be between the defined value. If the DPl values
of X resolution is not meet the criteria, it will reject with respective reason.
Reasons
Image X Resolution Should be less than or Equal To Allowed Value
Image X Resolution Should be more than or Equal To Allowed Value
Minimum X resolution of images: 60 DPls
Maximum X resolution of images: 500 DPls
y_resolution- DPl values will be calculated for Y resolution (Vertical resolution).
Image's vertical resolution should be between the defined value. If the DPI values of X
resolution is not meet the criteria, it will reject with respective reason.
 Reasons
Image Y Resolution Should be less than or Equal To Allowed Value
Image Y Resolution Should be more than or Equal To Alowed Value
Minimum Y resolution of images: 60 DPls
Maximum Y resolution of images: 500 DPls

<!-- Page 3 -->

NACHV
NATIONAL AUTOMATED CLEARING HOUSE
Image type should be same as the extension - tiff or jpeg application
Too light- Brightness of image will be validated, If the Image Brightness is more than
defined parameter value it will reject with "Image is Too Bright"
Maximum Luminance of image: 1.0 (Average of all the RGB values of pixels in
the image)
Too dark - Darkness of image will be validated, If the Image Darkness is more than
defined parameter value it will reject with "Image is Too Dark".
Minimum Luminance of image: 0.6 (Average of all the RGB values of pixels in
the image)
