# og-fortiddos

Ordering Guide
FortiDDoS
Available in
Appliance Virtual Hybrid
FortiDDoS is an advanced inline distributed denial of service (DDoS) mitigation system
that ensures network, resource, and application availability and security, protecting from
known and zero-day Layer 3 to Layer 7 DDoS attacks.
FortiDDoS’s massively parallel architecture delivers the most advanced and lowest-
latency DDoS attack mitigation on the market today without the packet-rate
performance compromises of other vendors.
FortiDDoS’s 100% packet inspection for more than 200 000 parameters, inbound and
outbound, at the highest packet rates, results in the fastest and most accurate detection
and mitigation in the industry with extensive forensics visibility.
In place of predefined or subscription-based signatures to identify attack patterns,
FortiDDoS uses autonomous machine learning to build an adaptive baseline of normal
activity from hundreds of thousands of parameters and then monitors traffic patterns
against those baselines. Should an attack begin, FortiDDoS sees the deviation and
immediately takes action to mitigate it, often from the first packet with no operator
intervention.
FortiDDoS uses unmatched “state awareness” of TCP, DNS, NTP; plus DTLS and QUIC
to stop the most frequent and largest attack types (DNS and NTP reflection floods and
SYN-ACK floods) from the first packet, while competitive options are forced to create
overly broad “signatures” after many seconds or minutes, or resort to manual NoC
intervention.
You can deploy FortiDDoS as a physical or virtual machine (VM):
• Inline on-premise appliance
• Inline on-premise VM on bare-metal servers
• Hybrid on-premise/Cloud DDoS mitigation through our Cloud DDoS partners
Major customer verticals include enterprise, education, government, and hosting
providers. FortiDDoS is not usually applicable to ISP deployments. Contact CSEs/PLM
before presenting, responding to RFPs, or quoting.


**Table 1.1**

|  |  |
| --- | --- |

FortiDDoS Ordering Guide
Product Offerings
DPDK/TP3 ACCELERATED DEVICES AND VIRTUAL MACHINES
1500F
VM04 VM08 VM16 200F 2000F 3000G
1500F-LR
RECOMMENDED CONNECTIVITY FOR ENTERPRISE DATACENTER ENVIRONMENTS
GE or 2xGE BGP ⃝✓ ⃝✓ ⃝✓ ⃝✓
2-4x GE LACP ⃝✓ (2x GE) ⃝✓ ⃝✓
10GE or 2x 10GE BGP Capped at 4-5Gbps ⃝✓ ⃝✓ ⃝✓
10GE or 2x 10GE BGP ⃝✓ ⃝✓ ⃝✓ ⃝✓
2x10GE LACP ⃝✓ ⃝✓ ⃝✓
2x10GE + 2x10GE BGP ⃝✓ ⃝✓
4x10GE LACP
40GE or 2x40GE BGP ⃝✓ ⃝✓
100GE or 2x 100GE BGP ⃝✓
PERFORMANCE
Enterprise Inspected Throughput (Gbps) 3 5 10 8 22 39 85
Small UDP Inspected Throughput (Mpps) 4 6 10 9 27 52 104
SYN Validation Throughput (Mpps) 2.6 5 5 5.3 19 40 55
OTHER CAPACITIES
Max Service Protection Profiles (SPP) 4 8 16 8 16 16 16
Max Protected Subnets 512 per SPP 512 per SPP 512 per SPP 512 per SPP 1024 per SPP 1024 per SPP 1024 per SPP
Dual Power Supplies AC AC AC AC
Form Factor 1 RU 2 RU 2 RU 2 RU
INTERFACES
10/100/1000 Mbps 8
MAXIMUM 8 PORTS WITH NATIVE DATA RATES
GE SFP 4
BASED ON THE RECOMMENDED CONNECTIVITY
GE LC SR with Optical Bypass 4
ABOVE.
10GE SFP+ 4 4 4
10GE LC SR with Optical Bypass 4
40GE QSFP+ 4
4
100GE QSFP28
Optical Bypass for 10GE/40GE LC
4
1310/1550nm
Optical Bypass for 10GE/40GE/100GE LC
4
1310/1550nm
SECURITY SERVICES
IP and Domain Reputation Subscriptions Optional and not required for enterprise DDoS mitigation
ADDITIONAL SERVICES
24x7 Support ⃝✓ ⃝✓ ⃝✓ ⃝✓ ⃝✓ ⃝✓ ⃝✓
To download datasheets, case studies, and other product information, see https://www.fortinet.com/products/ddos/fortiddos.
VM Notes:
• Stated Specifications require DPDK CPUs and SR-IOV NICs with PCIe x8 busses. Failure to use these results in significantly
lower performance.
• Without the above, VMs are limited to GE links no matter the number of CPUs licensed.
• NICs should not share PCle busses with other applications. A bare-metal server is recommended.
• VMs do not support traffic bypass. External bypass is required for most deployments.
• VMs have less granular TCP and UDP Port and ICMP flood mitigation and graphing support than appliances.
• FortiDDoS is not able to extract transceiver information from server NICs making connectivity troubleshooting more difficult.
2


**Table 2.1**

| DPDK/TP3 ACCELERATED DEVICES AND VIRTUAL MACHINES |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | VM04 | VM08 | VM16 | 200F | 1500F 1500F-LR | 2000F | 3000G |
| RECOMMENDED CONNECTIVITY FOR ENTERPRISE DATACENTER ENVIRONMENTS |  |  |  |  |  |  |  |


**Table 2.2**

| OTHER CAPACITIES |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |


**Table 2.3**

| INTERFACES |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | MAXIMUM 8 PORTS WITH NATIVE DATA RATES BASED ON THE RECOMMENDED CONNECTIVITY ABOVE. |  |  |  |  |  |  |


**Table 2.4**

| SECURITY SERVICES |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |


**Table 2.5**

| ADDITIONAL SERVICES |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |


**Table 2.6**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiDDoS Ordering Guide
Order Information
DPDK/TP3 ACCELERATED DEVICES
PRODUCT 200F 1500F 1500F-LR 2000F 3000G
Device FDD-200F FDD-1500F FDD-1500F-LR FDD-2000F FDD-3000G
IP Reputation FC-10-FI2HF-140-02-DD FC-10-F1K5F-140-02-DD FC-10-F15SF-140- 02-DD FC-10-FD2KF -140-02-DD FC-10-FI3KG -140- 02-DD
Domain Reputation FC-10-FI2HF-191-02-DD FC-10-F1K5F-191-02-DD FC-10- F15SF--191- 02-DD FC-10-FD2KF -191-02-DD FC-10-FI3KG -191- 02-DD
SUPPORT
1/3/5-year 24x7 Support FC-10-FI2HF-247-02-DD FC-10-F1K5F-247-02-DD FC-10- F15SF-247- 02-DD FC-10-FD2KF -247-02-DD FC-10-FI3KG -247- 02-DD
VIRTUAL MACHINES
PRODUCT VM04 VM08 VM16
Perpetual VM License FDD-VM04 FDD-VM08 FDD-VM16
IP Reputation FC-10-FIM04- 140-02-DD FC-10-FIM08-140- 02-DD FC-10-FIM16-140- 02-DD
Domain Reputation FC-10-FIM04- 191-02-DD FC-10-FIM08-191- 02-DD FC-10-FIM16-191- 02-DD
SUPPORT
1/3/5-year 24x7 Support FC-10-FIM04- 248-02-DD FC-10-FIM08-248- 02-DD FC-10-FIM16-248- 02-DD
Fortinet Training and Certification
FortiDDoS-F Series Training
Learn how to form network baseline data, and how to recognize and mitigate individual and distributed denial of service attacks
while preserving service and network performance.
Course Details
For prerequisites, agenda topics, and learning objectives, visit: https://training.fortinet.com/local/staticpage/view.
php?page=library_fortiddos
Training Offering
For training SKUs, purchasing, and delivery options, visit: https://training.fortinet.com/local/staticpage/view.
php?page=purchasing_process
www.fortinet.com
Copyright © 2026 Fortinet, Inc. All rights reserved. Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product or
company names may be trademarks of their respective owners. Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other condi-
tions may affect performance results. Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s SVP Legal and above, with a purchaser
that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet. For absolute clarity, any
such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify, transfer, or otherwise
revise this publication without notice, and the most current version of the publication shall be applicable.
FDD-OG-R12-20260323


**Table 3.1**

| DPDK/TP3 ACCELERATED DEVICES |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| PRODUCT | 200F | 1500F | 1500F-LR | 2000F | 3000G |


**Table 3.2**

| VIRTUAL MACHINES |  |  |  |
| --- | --- | --- | --- |
| PRODUCT | VM04 | VM08 | VM16 |
