# og-casb

Ordering Guide
FortiCASB
Available in
Appliance Virtual Cloud
Welcome to the Fortinet CASB Ordering Guide. This guide is designed to help customers
understand and navigate the various options available for deploying Fortinet’s Cloud
Access Security Broker (CASB) solutions, including FortiCASB and FortiGuard CASB
Services.
As organizations increasingly rely on SaaS applications to support a remote and
distributed workforce, securing user access and protecting cloud data becomes critical.
Fortinet delivers a robust, multilayered approach to SaaS security through a tightly
integrated portfolio of products and services that can be deployed individually or in
combination to meet specific security and compliance needs.
This guide outlines:
• Key CASB capabilities and delivery models
• Licensing options and entitlement details
• Product-specific features across FortiGate, FortiProxy, FortiSASE, ZTNA, and
FortiCASB
• A comparison of in-line versus API-based CASB approaches

FortiCASB Ordering Guide
AUTHENTICATION AND POSTURE SAAS SECURITY, VISIBILITY, AND DATA SECURITY AND CONTENT
FORTINET PRODUCT
ASSESSMENT CONTROL SCANNING (DLP)
FortiClient Yes TCP Forwarding1 In Device / In motion2
FortiProxy Authentication Inline In motion
FortiGate Authentication Inline In motion
FortiSASE Authentication Inline In motion
FortiCASB N/A API At rest and collaboration
1. Forwarded to FortiSASE or FortiGate to perform inline CASB functionality.
2. Roadmap
Fortinet offers a comprehensive portfolio of security products designed to secure SaaS applications and support work from
anywhere transformation. This ordering guide provides quick reference to different options customers would have and
respective capabilities when they are looking to purchase a CASB solution.
Purchase Options
The following describes purchase options with capability mapping.
FortiClient ZTNA + FortiGate or FortiProxy Appliances
These customers are entitled to the most complete set of SaaS security capabilities offered by Fortinet products including
FortiClient ZTNA authentication and posture assessment based on number of FortiClient license seats, FortiOS Inline-CASB
monitoring and enforcement, FortiCASB API CASB monitoring (based on number of FortiClient license seats, and FortiCASB Data
Security Management based on number of FortiClient license seats x 1GB of data security scanning per seat).
FortiSASE
These customers are entitled to the same capability set as the above, however all the inline capabilities are delivered with
FortiSASE instead of FortiGate and/or FortiProxy. Overall capabilities including FortiClient, FortiSASE, and FortiCASB seats are
based on the number of FortiSASE license seats.
FortiGate or FortiProxy
Customers that only have FortiGate and/or FortiProxy are entitled to Inline CASB capabilities that are part of FortiOS, these
licenses do not entitle usage of FortiClient and FortiCASB enhanced SaaS Security functionality.
FortiCASB
Customers are entitled to use FortiCASB SaaS Security application to monitor SaaS applications at the API level, these
customers are entitled to the number of FortiCASB seats based on the number of ZTNA seats they purchased or where entitled
to from their SASE purchase.
The following table outlines the capabilities available to customers based on product purchase.
CASB DELIVERY OPTIONS
FORTIGATE FORTIPROXY UNIVERSAL ZTNA FORTISASE FORTICASB
AND CAPABILITIES
Add-on required
Inline-CASB Included No Included No
(SWG Protection Bundle)
Add-on required Add-on required Included Included
API-CASB Included
(FortiCASB) (FortiCASB) (FortiCASB part of bundle) (FortiCASB part of bundle)
* Would require either a FortiGate-HW, FortiGate-VM, or FortiProxy with SWG bundle to enable Inline-CASB.
2


**Table 2.1**

| FORTINET PRODUCT | AUTHENTICATION AND POSTURE ASSESSMENT | SAAS SECURITY, VISIBILITY, AND CONTROL | DATA SECURITY AND CONTENT SCANNING (DLP) |
| --- | --- | --- | --- |


**Table 2.2**

| CASB DELIVERY OPTIONS AND CAPABILITIES | FORTIGATE | FORTIPROXY | UNIVERSAL ZTNA | FORTISASE | FORTICASB |
| --- | --- | --- | --- | --- | --- |


**Table 2.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiCASB Ordering Guide
Product Capabilities
All FortiOS (FortiGate, FortiSASE, FortiProxy) customers have access to CASB features. Following is the mapping of capabilities
by product purchase.
1. FortiGate
All FortiGate models provide support for in-line CASB without any additional license needed. This feature means that in-line
CASB is available when you purchase the FortiGate appliance. All FortiGate hardware models including virtual form factors
(public/private cloud) are supported. The inline CASB feature comes as part of the FortiOS which is the core foundation of
Fortinet devices.
FortiGate ordering guide can be referenced for purchasing details here.
2. FortiProxy
FortiProxy delivers next generation secure web gateway capabilities that protect employees from Internet-borne threats.
FortiProxy is available in two forms, FortiProxy-HW and FortiProxy-VM. Hardware appliances include models such as 400E/G,
2000E/G, and 4000E/G. FortiProxy-HW licenses are paired with user licenses that can range from 500 and up to 50,000 users.
FortiProxy-VM provides support for private and public clouds (AWS, Azure, and GCP). FortiProxy-VM is yearly subscription for
IaaS/private cloud and is also paired with a user license. SWG protection bundle is required to enable inline CASB with FortiProxy
(HW or VM).
FortiProxy ordering guide can be referenced for purchasing details here.
PRODUCT HARDWARE ACCELERATED SUBSCRIPTIONS
MODEL 400E 400G 2000E 2000G 4000E 4000G
FC1-10-XY400-514- FC1-10-XY40G-514- FC1-10-XY2KE-514- FC1-10-XY2KG-514- FC1-10-XY4KE-514- FC1-10-XY4KG-514-
SWG Protection Bundle
02-DD 02-DD 02-DD 02-DD 02-DD 02-DD
PRODUCT VIRTUAL MACHINE SUBSCRIPTIONS
MODEL VM02 VM04 VM08 VM16 VMUL
SWG Protection Bundle FC1-10-XYVM2-515-02-DD FC1-10-XYVM4-515-02-DD FC1-10-XYVM8-515-02-DD FC1-10-XYV16-515-02-DD FC1-10-XYVUL-515-02-DD
3. Fortinet Zero Trust Network Access (ZTNA)
Fortinet ZTNA portfolio is an integrated component of Fortinet security fabric, giving administrators the ability to control which
users/devices can access what resources from sensitive data stored in corporate applications through SaaS applications and
internet website categories from anywhere. This ability to support users in dense campuses and remote locations, and to control
access to applications located in the cloud, in data centers, and on-premises makes Fortinet offering a Universal ZTNA solution.
FortiClient (ZTNA agent) is an integral part of the ZTNA solution, which can be provisioned on a per-user or per-endpoint basis
and managed from cloud-based console (SaaS) or on-premises depending on corporate requirements. Customers purchasing
ZTNA are entitled to use FortiCASB with the same seat count, furthermore these customers are entitled to the equivalent of
1GB of Data at Rest protection for their SaaS applications per user per year – entitlement is at the customer level multiplying the
number of seats by 1GB per year and are not tied to a specific user. Please see FortiCASB documentation for more details.
ZTNA ordering guide can be referenced for purchasing details here.
FORTITRUST USER RANGE SKUS USER QUANTITY ZTNA AGENT MANAGED ZTNA AGENT
100-499 FC2-10-EMS05-509-02-DD FC2-10-EMS05-556-02-DD
500-1999 FC3-10-EMS05-509-02-DD FC3-10-EMS05-556-02-DD
Per User
2000-9999 FC4-10-EMS05-509-02-DD FC4-10-EMS05-556-02-DD
10 000 + FC5-10-EMS05-509-02-DD FC5-10-EMS05-556-02-DD
PACK SKUS PACK QUANTITY ZTNA AGENT MANAGED ZTNA AGENT
25-pack FC1-10-EMS05-428-01-DD FC1-10-EMS05-485-01-DD
500-pack FC2-10-EMS05-428-01-DD FC2-10-EMS05-485-01-DD
Per Endpoint
2000-pack FC3-10-EMS05-428-01-DD FC3-10-EMS05-485-01-DD
10 000-pack FC4-10-EMS05-428-01-DD FC4-10-EMS05-485-01-DD
3


**Table 3.1**

| PRODUCT | HARDWARE ACCELERATED SUBSCRIPTIONS |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| MODEL | 400E | 400G | 2000E | 2000G | 4000E | 4000G |


**Table 3.2**

| PRODUCT | VIRTUAL MACHINE SUBSCRIPTIONS |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| MODEL | VM02 | VM04 | VM08 | VM16 | VMUL |


**Table 3.3**

| FORTITRUST USER RANGE SKUS | USER QUANTITY | ZTNA AGENT | MANAGED ZTNA AGENT |
| --- | --- | --- | --- |


**Table 3.4**

| PACK SKUS | PACK QUANTITY | ZTNA AGENT | MANAGED ZTNA AGENT |
| --- | --- | --- | --- |


**Table 3.5**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiCASB Ordering Guide
4. FortiSASE
FortiSASE is Fortinet’s cloud-based firewall and secure web gateway as a service, delivered as a hosted service; that provides
security driven by FortiGuard labs for remote users regardless of location when accessing the internet, SaaS, or private
applications. FortiSASE licensing is based upon user-range (same as ZTNA); and includes Inline CASB and FortiCASB as part of
the product. No additional licenses are required to enable CASB when you deploy FortiSASE.
FortiSASE ordering guide can be referenced for purchasing details here.
REMOTE USERS BANDS USER LICENSE
50-499 FC2-10-EMS05-547-02-DD
500-1999 FC3-10-EMS05-547-02-DD
FortiSASE User Subscription
2000-9999 FC4-10-EMS05-547-02-DD
10 000 + FC5-10-EMS05-547-02-DD
5. FortiCASB
FortiCASB is a Fortinet-developed cloud-native Cloud Access Security Broker (CASB) solution designed to provide visibility,
compliance, data security, and threat protection for cloud-based services employed by an organization. FortiCASB licensing
is based upon user-range. These user SKUs include data security scanning (data amount varies) per year. Additionally, users
purchasing the FortiCASB SKU directly are entitled to the equivalent of 10GB of data protection per user per year. Additional
data protection is available as an add-on. In-line CASB is not available with FortiCASB; you would require purchasing a FortiOS
based solution for In-line CASB functionality.
UNIT SKU DESCRIPTION
FC1-10-FCASB-145-02-DD FortiCASB SaaS Protection 100 User SKU. Includes 1TB of Data Security scanning capacity per year
FortiCASB SaaS Protection
FC2-10-FCASB-145-02-DD FortiCASB SaaS Protection 500 User SKU. Includes 5TB of Data Security scanning capacity per year
FortiCASB Data Protection 100GB, add-on subscription license for malware/sensitive data scan/DLP on SaaS
FC1-10-FCASB-307-02-DD
platforms, requires one of FC1-10-FCASB-145-02-DD or FC2-10-FCASB-145-02-DD or FortiClient ZTNA licenses.
FortiCASB Data Protection
FortiCASB Data Protection 1 TB, add-on subscription license for malware/sensitive data scan/DLP on SaaS
FC5-10-FCASB-307-02-DD
platforms, requires one of FC1-10-FCASB-145-02-DD or FC2-10-FCASB-145-02-DD or FortiClient ZTNA licenses.
4


**Table 4.1**

| REMOTE USERS | BANDS | USER LICENSE |
| --- | --- | --- |


**Table 4.2**

| UNIT | SKU | DESCRIPTION |
| --- | --- | --- |


**Table 4.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiCASB Ordering Guide
Frequently Asked Questions
What options would I have in order to obtain CASB from Fortinet?
There are five delivery models by which CASB can be obtained from Fortinet, and each has unique licensing model.
1. FortiGate (HW or VM)
2. FortiProxy
3. Fortinet Universal ZTNA
4. FortiSASE
5. FortiCASB
With the FortiGate model to obtain CASB, would one require to purchase any additional license add-on to enable full CASB
capabilities?
With the FortiGate model, in-line CASB comes with FortiGate since it is embedded within the FortiOS. To obtain API-CASB, you
would have to purchase FortiCASB license.
What CASB delivery model would provide holistic CASB feature set?
FortiSASE user-based licensing included both in-line CASB as well as API-CASB leveraging FortiCASB.
FortiSASE would be the most comprehensive offering which includes all CASB features.
Is CASB licensed per user or per device?
Depending on how CASB is deployed; with FortiGate and FortiProxy, one can purchase device-based licenses. ZTNA, FortiSASE,
and FortiCASB are per user base.
Is there any difference between CASB offering for the five options listed above?
CASB functionalities can be delivered from multiple models listed, but the features and capabilities would stay the same per
model.
What is the difference between inline CASB and API CASB?
Inline CASB would enforce security inspection in line with the traffic that is accessing cloud applications. API based CASB are
out of band, directly integrating with the SaaS application which allows data visibility residing on SaaS applications. Both In line
and API CASB are necessary to provide holistic enterprise grade protection.
www.fortinet.com
Copyright © 2025 Fortinet, Inc. All rights reserved. Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product or
company names may be trademarks of their respective owners. Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other condi-
tions may affect performance results. Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s SVP Legal and above, with a purchaser
that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet. For absolute clarity, any
such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify, transfer, or otherwise
revise this publication without notice, and the most current version of the publication shall be applicable.
FCASB-OG-R03-20250724
