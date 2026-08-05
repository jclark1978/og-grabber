# og-fortibranchsase

Ordering Guide
FortiBranchSASE
FortiBranchSASE (FBS) series devices are purpose-built to provide security and connectivity
for small remote sites where local security services are unlikely to be present. These devices help
streamline deployment by eliminating the complexity of managing a local security stack at each
remote branch.
Key aspects of FortiBranchSASE include:
• Connectivity: FBS (Thin-Edge) devices use LAN-Extension technology to connect to FortiGate,
whether it is a SASE POP (FortiGate VM) or a regular FortiGate managing an FBS in LAN-
Extension mode.
• Management:
• FBS devices can be provisioned and managed from the FortiSASE portal. Configurations in
FortiSASE are streamlined for ease of use.
• FBS devices can also be managed by any FortiGate in LAN-Extension mode. Provisioning and
management may differ due to GUI differences between FortiSASE and FortiGate/FortiOS.
• Security Services: Security services are delivered via SASE cloud or a FortiOS-based solution,
such as a remote FortiGate or a cloud-based virtual FortiGate. All traffic generated behind FBS
is secured by applying data protection measures at the FortiSASE POP or the remote FortiOS
instance, ensuring robust security for small remote sites.
• Ordering: Ordering is simple; customers select the Hardware FBS device and a FortiSASE
subscription bundle.
Note: The FEX-200F model does not have a FortiSASE bundle; equivalent bundle components
(595 and 247) must be selected separately.
• FortiSASE Managed: FortiSASE Subscription Bundles are available for FBS-10F-WIFI, FBS-20G,
and FBS-20G-WiFi. A-la-carte FortiSASE Subscription (FC-10-X200F-595-02-DD) and FortiCare
Premium Support (FC-10-X200F-247-02-DD) are available for FEX-200F.
• FortiGate Managed: FortiCare Premium Support SKUs are available for various models.

FortiBranchSASE Ordering Guide
Order Information
ALL THIN-EDGE MODELS
10F-WIFI 20G 20G-WIFI 200F
HARDWARE SPECIFICATIONS
Dedicated WAN Ports 1x 1G RJ45 WAN 1x SFP+1G RJ45 (Combo) 1x SFP+1G RJ45 (Combo) 1x 1G RJ45 WAN
LAN/Switch Ports 2x 1G RJ45 WAN/LAN 3x 1G LAN, 1x 1G WAN/LAN 3x 1G LAN, 1x 1G WAN/LAN 3x 1G LAN, 1x 1G WAN/LAN
Power over Ethernet (PoE) Powered Yes No No No
Power Required PoE 802.3at (25.5W) 12V/2A (24W) 12V/2A (24W) 12V/2A (24W)
Console Port 1x RJ45 1x RJ45 1x RJ45 1x RJ45
USB Ports USB2.0 - A USB2.0 - A USB2.0 - A USB2.0 - A
Bluetooth BLE 2.4G BLE 2.4G BLE BLE
CONNECTIVITY
4G-LTE/5G Modems No Modem No Modem No Modem No Modem
Wi-Fi (Built-in AP) WiFi6 No WiFi6 No
FortiGate LAN Extension Support Yes Yes Yes Yes
BANDWIDTH INFORMATION
IPsec Throughput 890Mbps 890Mbps 890Mbps 220Mbps
Lan-Extension Throughput 860Mbps DL/UL: 600Mbps/350Mbps DL/UL: 600Mbps/350Mbps 180Mbps
LAN-WAN, Layer-3 Throughput 900Mbps 900Mbps 900Mbps 900Mbps
HARDWARE MODEL
Global (Select the correct region code for Wi-Fi models) FBS-10F-WiFi-x FBS-20G FBS-20G-WiFi-x FEX-200F
FORTISASE MANAGED
FortiSASE Subscription Bundle FC-10-BS10F-1070-02-DD FC-10-BS20G-1070-02-DD FC-10-BS20W-1070-02-DD N/A
FortiSASE Subscription (A-la-carte) - - - FC-10-X200F-595-02-DD
FortiCare Premium Support (A-la-carte) - - - FC-10-X200F-247-02-DD
FORTIGATE MANAGED
FortiCare Premium Support FC-10-BS10F-247-02-DD FC-10-BS20G-247-02-DD FC-10-BS20W-247-02-DD FC-10-X200F-247-02-DD
2


**Table 2.1**

|  | ALL THIN-EDGE MODELS |  |  |  |
| --- | --- | --- | --- | --- |
|  | 10F-WIFI | 20G | 20G-WIFI | 200F |
| HARDWARE SPECIFICATIONS |  |  |  |  |


**Table 2.2**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiBranchSASE Ordering Guide
Frequently asked questions
Do FEX-200F and FBS devices provide LTE/5G WAN connectivity?
No. Thin Edge devices are Ethernet-only products in the FortiExtender line, supporting a cost-effective means of rolling out
Thin Edge devices via Ethernet, if LTE is not desired and internet connectivity is present at the branch locations for FortiSASE
service.
What is the “Thin Edge” concept?
Thin edge refers to a minimalistic approach to deployments where limited on-site equipment is used, focusing on centralized
security and control. It’s designed for small sites like micro-branches, home offices, and temporary setups that require
connectivity with minimal hardware.
What is “LAN-Extension” Technology with FortiGate?
The FortiGate LAN extension allows you to seamlessly connect FortiExtenders and FBS devices into a remote FortiGate at an
HQ or centralized location via VxLAN over IPSec. LAN-Extension technology allows FortiGate to extend its local LAN to a remote
location using FEX or FBS devices, and hosts connecting behind FBS logically appear as FortiGate’s internal LAN and managed
from FortiGate. FBS Thin-Edge devices also use LAN-Extension technology to connect to the FortiSASE PoP, from where FBS
devices are provisioned and managed, thus, connecting hosts behind FBS appliance receive security from FortiSASE cloud.
Does the FBS product line require FortiSASE to operate?
No, while FortiBranchSASE naturally fits with our FortiSASE solution for thin edge deployments, it can also operate with any
FortiOS based management solution, such as a remote FortiGate appliance, a FortiGate VM, or FortiGate-as-a-Service.
What licenses do I need to use FortiBranchSASE?
When using FortiBranchSASE units with FortiSASE, a FortiSASE device subscription is required. Select the FortiSASE
subscription bundle SKU with appropriate FBS Hardware, apart from 200F which does not have bundle SKU, select a-la-carte
SKUs for 200F.
What types of use cases are ideal for FortiBranch SASE?
FBS devices can be used in various use cases and deployment scenarios but three are highlighted below as an example:
• Micro-branches: small offices needing central management, visibility, and policy consistency without heavy investment.
• Home Offices: For executives or high-priority users with more equipment than a typical laptop, requiring secure, seamless
connectivity.
• Temporary Pop-ups: Sites like kiosks or event setups that need rapid deployment and takedown with secure connectivity.
How does FortiBranch SASE handles scalability?
Please check current updates for FEX/FBS supported in LAN-Extension mode with FortiGate, it varies between 16 to 1024
devices depending on FortiGate model and FortiGate VM.
www.fortinet.com
Copyright © 2026 Fortinet, Inc. All rights reserved. Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product or
company names may be trademarks of their respective owners. Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other condi-
tions may affect performance results. Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s SVP Legal and above, with a purchaser
that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet. For absolute clarity, any
such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify, transfer, or otherwise
revise this publication without notice, and the most current version of the publication shall be applicable.
FBS-OG-R03-20260318
