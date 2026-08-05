# og-fortiextender

Ordering Guide
FortiExtender
FortiExtenders are secure 5G/LTE gateways from Fortinet. They offer secure
connectivity and enhanced network resiliency for businesses, supporting critical features
such as wireless WAN, carrier failover, out of band management, LAN extensions via
VxLAN over IPsec, WAN extensions, active/active connections, VRRP, split tunneling, and
more. In this guide, you will find essential information about each FortiExtender model to
help you appropriately size and scope your environment.

FortiExtender Ordering Guide
Product Offerings
ENTRY-LEVEL MID-RANGE HIGH-END
Appliances 101G 211G 50G 511G 511G-WiFi
Number of Modems Single Modem Single Modem Single Modem Single Modem Single Modem
Module Category CAT-6/LTE CAT-12/LTE 5G 5G 5G
SIM Slots Dual SIM + eSIM Dual SIM + eSIM Dual SIM + eSIM Dual SIM + eSIM Dual SIM + eSIM
CONNECTIVITY
Dedicated WAN Ports 1 1 1 (5Gig) 1 (2.5Gig) 1 (2.5Gig)
LAN/Switch Ports 4 4 1 1-SFP+RJ45 and 3-LAN 1-SFP+RJ45 and 3-LAN
Wi-Fi (Built-in AP) NO NO NO NO Wi-Fi6
FortiGate LAN Extension YES YES NO YES YES
FortiGate WAN Extension 2 per FGT 2 per FGT 2 per FGT 2 per FGT 2 per FGT
HARDWARE VARIANTS
North America - - FEW-50G-AM - -
EMEA/APAC/LATAM - - FEW-50G-EA - -
Global FEX-101G FEX-211G - FEX-511G FEX-511G-WiFi-x
FORTIGATE-MANAGED
- - FC-10-FA50G-247-02-DD - -
FC Premium Support - - FC-10-FE50G-247-02-DD - -
FC-10-X101G-247-02-DD FC-10-X211G-247-02-DD FC-10-FX51G-247-02-DD FC-10-XW51G-247-02-DD
FORTIEDGE CLOUD
MANAGED
- - FC-10-FEXC0-583-02-DD - -
FC Support + Management - - FC-10-FEXC0-583-02-DD - -
FC-10-FEXC0-583-02-DD FC-10-FEXC0-583-02-DD - FC-10-FEXC2-583-02-DD FC-10-FEXC2-583-02-DD
2


**Table 2.1**

|  | ENTRY-LEVEL | MID-RANGE | HIGH-END |
| --- | --- | --- | --- |


**Table 2.2**

| CONNECTIVITY |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |


**Table 2.3**

| HARDWARE VARIANTS |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |


**Table 2.4**

| FORTIGATE-MANAGED |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |


**Table 2.5**

| FORTIEDGE CLOUD MANAGED |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |


**Table 2.6**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiExtender Ordering Guide
Order Information
FORTIEXTENDER VEHICLE FORTIEXTENDER RUGGED
APPLIANCES 211F 212F 511G 511G
Number of Modems Single Modem Dual Modem Single Modem Single Modem
Module Category CAT-12/LTE CAT-12/LTE 5G 5G
SIM Slots Dual SIM Two-Dual SIM Dual SIM + eSIM Dual SIM + eSIM
CONNECTIVITY
Dedicated WAN Ports 1 1 1x 2.5G 1x 2.5G/PoE
LAN/Switch Ports 4 4 4 1
Wi-Fi (Built-in AP) YES YES Wi-Fi6 Wi-Fi6
FortiGate LAN Extension YES YES YES YES
FortiGate WAN Extension 2 per FGT 2 per FGT 2 per FGT 2 per FGT
HARDWARE VARIANTS
North America FEV-211F-AM-x FEV-212F-AM-x - -
EMEA/APAC/LATAM FEV-211F-x FEV-212F-x - -
Global - - FEV-511G-x FER-511G-x
FORTIGATE-MANAGED
FC-10-FV21F-247-02-DD FC-10-FV22F-247-02-DD - -
FC Premium Support FC-10-FG21F-247-02-DD FC-10-FG22F-247-02-DD - -
- - FC-10-FV51G-247-02-DD FC-10-XR51G-247-02-DD
FORTIEDGE-CLOUD MANAGED
FC-10-FEXC2-583-02-DD FC-10-FEXC2-583-02-DD - -
FC Support + Management FC-10-FEXC2-583-02-DD FC-10-FEXC2-583-02-DD - -
- - FC-10-FEXC2-583-02-DD FC-10-FEXC2-583-02-DD
3


**Table 3.1**

|  | FORTIEXTENDER VEHICLE |  |  | FORTIEXTENDER RUGGED |
| --- | --- | --- | --- | --- |
| APPLIANCES | 211F | 212F | 511G | 511G |


**Table 3.2**

| CONNECTIVITY |  |  |  |  |
| --- | --- | --- | --- | --- |


**Table 3.3**

| HARDWARE VARIANTS |  |  |  |  |
| --- | --- | --- | --- | --- |


**Table 3.4**

| FORTIGATE-MANAGED |  |  |  |  |
| --- | --- | --- | --- | --- |


**Table 3.5**

| FORTIEDGE-CLOUD MANAGED |  |  |  |  |
| --- | --- | --- | --- | --- |


**Table 3.6**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiExtender Ordering Guide
Frequently Asked Questions
What is the difference between dual SIM and dual modem?
All FortiExtender models support dual SIM slots to enable redundancy between carriers based on various metrics like signal strength and data plan. Single
modem units may only initiate a connection to one carrier at a time. Dual modem models are indicated by the “2” in the model number (i.e. 202F,212F) and
allow you to have two active wireless connections for faster failover and path selection.
What are FortiGate and FortiSASE LAN extensions?
FortiGate LAN extension allows you to seamlessly connect from your FortiExtender locations into a remote FortiGate at a HQ or centralized location via
VxLAN. From your connected FortiGate, you can control the ports and connectivity of FortiExtender locations. FortiSASE LAN extension works similarly, but
with your connection to the FortiSASE Cloud account. FortiExtender 200F supports FortiSASE LAN extension to easily connect your microbranch locations
into SASE for cloud- delivered security and connectivity. We will be introducing three new models in 2024 for Thin Edge deployments, called FortiBranchSASE.
Can I use a FortiExtender Vehicle at fixed sites?
Yes, FortiExtender Vehicle is a great device for fixed sites with harsh environmental conditions. As an IP64 ruggedized device, FortiExtender Vehicle offers
protection against extreme temperatures, shock, vibration, humidity, and are dust and splash tight. In addition, you can leverage LAN extension with your
FortiExtender Vehicle, deploying FortiGuard protections, including the OT Security Service, from a centralized FortiGate at the remote FortiExtender Vehicle
site.
www.fortinet.com
Copyright © 2026 Fortinet, Inc. All rights reserved. Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product or
company names may be trademarks of their respective owners. Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other condi-
tions may affect performance results. Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s SVP Legal and above, with a purchaser
that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet. For absolute clarity, any
such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify, transfer, or otherwise
revise this publication without notice, and the most current version of the publication shall be applicable.
FEX-OG-R18-20250626

FortiExtender Ordering Guide
www.fortinet.com
Copyright © 2026 Fortinet, Inc. All rights reserved. Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product or
company names may be trademarks of their respective owners. Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other condi-
tions may affect performance results. Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s SVP Legal and above, with a purchaser
that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet. For absolute clarity, any
such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify, transfer, or otherwise
revise this publication without notice, and the most current version of the publication shall be applicable.
FEX-OG-R18-20250626
