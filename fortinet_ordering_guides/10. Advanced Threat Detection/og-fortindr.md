# og-fortindr

Ordering Guide
FortiNDR
FortiNDR Cloud and FortiNDR On-premise represent the future of artificial-intelligence (AI)-
driven, network-based breach protection technology designed to detect sophisticated and
hidden threat and malware on network, with supervised and unsupervised machine learning (ML)
continuously analyze metadata, especially east-west data in datacenters, to identify threats,
especially those which may be already persistent in the network.
Two different NDR deployments are available:
• FortiNDR Cloud: Processes network traffic in the cloud and provides 365-day retention and
advanced network detection and threat hunting functionality. Provides SaaS console for
customers to monitor detections and threat hunting. FortiNDR Cloud is SOC II compliant.
• FortiNDR On-premise: Stores and processes all data locally. Nothing leaves the network.
Standalone, center and sensor mode available to suit distributed sites deployment.

FortiNDR Ordering Guide
FortiNDR Cloud
FortiNDR Cloud is a cloud-based SaaS offering that leverages AI, ML, and behavioral and static analysis to assess network
traffic and spot threats early in the attack lifecycle.
FortiNDR Cloud includes a Technical Success Manager* to assist each deployment and has regular cadence calls with users to
optimize solution deployment.
Apart from receiving traffic using FortiNDR cloud hardware sensors and VMs, FortiNDR Cloud also allows third-party log
ingestion with Zscaler and NetFlow. This functionality requires the third-party logs ingestion SKU, while Netskope integration
uses the normal bandwidth SKU by deploying AWS sensors for ingestion.
Fortinet Security Automation service allows FortiNDR to integrate with SOAR cloud service to enable Fortinet connectors and
third-party integrations. Please refer to the product documentation for details.
Following is the FortiNDR Cloud architecture diagram:
*For customers with bandwidth at 1Gbps or above.
For hardware sensor technical specifications, see the datasheet.
2


**Table 2.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FortiNDR Cloud Order Information
FORTINDR CLOUD - SAAS SERVICE
DESCRIPTION SKU STACKABLE UNIT
FortiNDR Cloud Base Subscription (includes
FC1-10-NDRCL-1244-02-DD 2 Yes 100Mbps
100 Mbps throughput)1 MANDATORY
Log Ingestion (100 EPS) 3 FC1-10-NDRCL-1247-02-DD 2 Yes 100 Events per Sec
Fortinet Security Automation Service FC1-10-NDRCL-1300-02-DD 2 Yes 10,000 playbooks per month
Throughput True-up4 NDRC-TRUE-UP-1MTH100M Yes 100Mbps
1 Measure of total throughput by all sensors. For example, five sensors sending a total combined throughput of 10 Gbps throughput requires 100 x 100 Mbps of the SaaS SKU.
2 ”DD” specifies the contract length in months. Available terms are 1, 3, and 5 years (i.e. 12, 36, and 60 months).
3 Zscaler and Netflow ingestion supported ingestion supported. 100 Events per second (EPS) SKU is stackable, i.e., QTY of 2 equals 200 EPS. Must be purchased with bandwidth SKU
4 Not to be used in initial quote/order. True up are used for overages during the contract period. Fortinet reviews and reports usage regularly.
All initial orders must include cloud services with data throughput. Customers may purchase hardware sensors or use the free virtual sensors to provide data. Hardware sensors include
transceivers. See the FortiNDR Cloud datasheet.
FORTINDR CLOUD - SENSORS
HARDWARE OR VM AVAILABLE DESCRIPTION SKU
FORTINDR CLOUD-500F
FNRC-500G
(SMALL SENSOR)
Sensor hardware FORTINDR CLOUD-900F
FNRC-900G
(For tranceivers and cables pls refer to (Large SENSOR)
FortiNDR Acceosories section) FORTINDR CLOUD-2540F
FNRC-2540G
(Extra Large SENSOR)
PRMA availale Refer to Price List for details
Annual license for support for FNRC-500G
(small) sensor and forwarding traffic to the
FC-10-NDR5G-247-02-DD
FortiNDR Cloud SaaS Platform, includes
FortiCare premium.
Annual license for support for FNRC-900G
Sensor hardware Support and License to (large) sensor and forwarding traffic to the
FC-10-NDR9G-247-02-DD
forward traffic FortiNDR Cloud SaaS Platform, includes
FortiCare premium.
Annual license for support for FNRC-2540G
(Extra large) sensor and forwarding traffic to
FC-10-ND25G-247-02-DD
the FortiNDR Cloud SaaS Platform, includes
FortiCare premium.
Free of charge
Sensor Virtual Virtual Sensors (VM / KVM / Public Cloud)
(download from portal)
FortiAI
FORTIAI TOKENS TOP-UP LICENSE
SKU DESCRIPTION
LIC-FAITOKEN-1M FortiAI-Assist top-up SKU license for adding 1,000,000 AI tokens valid for 3 years.
LIC-FAITOKEN-5M FortiAI-Assist top-up SKU license for adding 5,000,000 AI tokens valid for 3 years.
LIC-FAITOKEN-10M FortiAI-Assist top-up SKU license for adding 10,000,000 AI tokens valid for 3 years.
3


**Table 3.1**

| FORTINDR CLOUD - SAAS SERVICE |  |  |  |
| --- | --- | --- | --- |
| DESCRIPTION | SKU | STACKABLE | UNIT |


**Table 3.2**

| FORTINDR CLOUD - SENSORS |  |  |  |
| --- | --- | --- | --- |
| HARDWARE OR VM AVAILABLE | DESCRIPTION | SKU |  |


**Table 3.3**

| FORTIAI TOKENS TOP-UP LICENSE |  |
| --- | --- |
| SKU | DESCRIPTION |


**Table 3.4**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FortiNDR Cloud example orders
Example of Order:
Monitoring of traffic with 1 Gbps bandwidth on AWS infrastructure.
• Cloud services (10 x FC1-10-NDRCL-1244-02-12) (10 x 100Mbps with 12 months subscription).
• Term: 1 year
• Public cloud sensors (supports AWS, Azure, OCI and GCP). Can be downloaded free of charge after cloud SaaS services are
provisioned.
• FortiAI natural language assistance (required) 1mil tokens (1 x LIC-FAITOKEN-1M )
Examples of larger and distributed deployment:
Monitoring multiple office locations and cloud traffic along with Zscaler remote access.
• Total bandwidth: 6 Gbps
• Zscaler and Netflow combined log rate: 3000 EPS
• Term: 3 years
• 2 large physical sensors, 3 virtual sensors (monitoring of 5 locations)
• FortiAI natural language assistance - required
• Cloud services: FC1-10-NDRCL-1244-02-36 x60 (60 units of 100Mbps with 3 years term [36])
• Large sensors: FNRC-900G x2
• Sensor subscription and support: FC-10-NDR9G-247-02-36 x 2 (for two senors)
• Zscaler and Netflow log ingestion: FC1-10-NDRCL-1247-02-36 x30 (30 units of 100 EPS with 3 years term [36])
• Virtual sensors: Downloaded free of charge (x3)
• FortiAI: 5 mil tokens (1 x LIC-FAITOKEN-5M )
4


**Table 4.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FortiNDR on-premise
FortiNDR on-premise is suitable for customers with on-premise SOC capacity or to satisfy air-gap or high compliance
deployments where all data remains on-premise. Leveraging Fortinet Security Fabric integration, FortiNDR can automatically
discover and classify every device communicating across the network, including east/west traffic in the data center. FortiNDR
also supports high throughput malware scanning with ANN and supports various Fabric integrations.
Here is a reference architecture diagram with FortiNDR:
FortiNDR on-premise hardware and virtual machines can run in three modes:
• Standalone (VM16, VM32, FortiNDR-1000F, FortiNDR-2500G)
• Center (supported on FNR-3600G, and Center VM models only)
• Sensors (VM08, VM16, VM32, FortiNDR-1000F, FortiNDR-2500G)
Center and sensors modes are used for deploying distributed deployment. See the following table or datasheet for mode
support for different models.
5


**Table 5.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FortiNDR Hardware Order Information
SOLUTION BUNDLE FORTINDR-1000F FORTINDR-2500G FORTINDR-3600G
Hardware Bundles Hardware Bundle FNR-1000F-BDL-331-DD2 FNR-2500G-BDL-331-DD2 FNR-3600G-BDL-331-DD
Renewal FC-10-AI1KF-331-02-DD2 FC-10-AI25G-331-02-DD2 FNR-3600G-BDL-1024-DD
Deploy Mode Standalone, Sensor Standalone, Sensor Center only
Sensors Managed1 N/A N/A Up to 50
High Availability Support Active-passive Active-passive
Dual center support (center mode)
(for all models) (standalone mode) (standalone mode)
Netflow Support
FC-10-AI1KF-588-02-DD2 FC-10-AI25G-588-02-DD2
(licensed separately)
N/A (license on sensors)
OT Security Services
FC-10-AI1KF-723-02-DD2 FC-10-AI25G-723-02-DD2
(licensed separately)
PRMA available Available, please refer to price list for PRMA options
1 For cases that require more than the specified number of sensors, consult your local Fortinet engineering team.
2 ”DD” specifies the contract length in months. Available terms are 1, 3, and 5 years (i.e. 12, 36, and 60 months). All non-standard terms more than 1 year require co-term
FortiNDR VM Order Information
SOLUTION BUNDLE VM08 VM16 VM32 VM CENTER
Sensor only
Deploy Mode Standalone, Sensor Standalone, Sensor Center
(requires center)
Sensors Managed1 N/A N/A N/A Up to 20
Active-passive Active-passive
High Availability Support Not supported Dual center support (center mode)
(standalone mode) (standalone mode)
FC1-10-AIVMC-757-02-DD (up to
10 sensors)
Annual Subscription FC2-10-AIVMS-461-02-DD2 FC3-10-AIVMS-461-02-DD2 FC4-10-AIVMS-461-02-DD2
FC5-10-AIVMC-757-02-DD
(unlimited sensors)
Netflow Support
Not supported FC3-10-AIVMS-588-02-DD2 FC4-10-AIVMS-588-02-DD2
(licensed separately)
Licensed on sensors
OT Security Services
FC2-10-AIVMS-723-02-DD2 FC3-10-AIVMS-723-02-DD2 FC4-10-AIVMS-723-02-DD2
(licensed separately)
1 For cases that require more than the specified number of sensors, consult your local Fortinet engineering team.
2 “DD” specifies the contract length in months. Available terms are 1, 3, and 5 years (i.e. 12, 36, and 60 months). All non-standard terms more than 1 year require co-term
6


**Table 6.1**

| SOLUTION BUNDLE |  | FORTINDR-1000F | FORTINDR-2500G | FORTINDR-3600G |
| --- | --- | --- | --- | --- |


**Table 6.2**

| SOLUTION BUNDLE | VM08 | VM16 | VM32 | VM CENTER |
| --- | --- | --- | --- | --- |


**Table 6.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FortiNDR Cloud and FortiNDR accessories
PRODUCT SKU DESCRIPTION
ACCESSORIES
10GE SFP+ transceiver module, 10km long range for systems with SFP+ and SFP/SFP+
10GE SFP+ Transceiver Module, Long Range FN-TRAN-SFP+LR
slots.
10GE SFP+ Transceiver Module, Short Range FN-TRAN-SFP+SR 10GE SFP+ transceiver module, short range for systems with SFP+ and SFP/SFP+ slots.
10GE copper SFP+ RJ45 Transceiver (30m range) FN-TRAN-GC 10GE copper SFP+ RJ45 transceiver module (30m range) for systems with SFP+ slots.
1GE SFP RJ45 Transceiver Module FN-TRAN-GC 1GE SFP RJ45 transceiver module for systems with SFP and SFP/SFP+ slots.
APPLICABLE TO FNR-2500G ONLY
25 GE / 10 GE SFP28 transceiver module, long range 10km, LC connector, SMF, 1310nm,
25GE SFP28 Transceiver Module, Long Range FN-TRAN-SFP28-LR
0°C to 70°C, for systems with SFP28 slots.
25 GE / 10 GE SFP28 transceiver module, short range 100m, LC connector, MMF, 850nm,
25GE SFP28 Transceiver Module, Short Range FN-TRAN-SFP28-SR
0°C to 70°C, for systems with SFP28 slots.
40G/100G QSFP+ to 4x SFP+/SFP28 Optical Breakout Cable 40G/100G QSFP+/QSFP28 to SFP+/SFP28 parallel breakout MPO to 4xLC connectors,
FN-CABLE-QSFP-4XSFP
1m OM3 MMF, 1m, transceivers not included.
40G/100G QSFP+ to 4x SFP+/SFP28 Optical Breakout Cable 40G/100G QSFP+/QSFP28 to SFP+/SFP28 parallel breakout MPO to 4xLC connectors,
FN-CABLE-QSFP-4XSFP-5
5m OM3 MMF, 5m, transceivers not included.
25 GE SFP28 passive direct attach cable, 1m, -40°C to 85°C, transceivers included, for
25 GE SFP28 Passive Direct Attach Cable FN-CABLE-SFP28-1
systems with SFP28 slots.
25 GE SFP28 passive direct attach cable, 3m, -40°C to 85°C, transceivers included, for
25 GE SFP28 Passive Direct Attach Cable FN-CABLE-SFP28-3
systems with SFP28 slots.
25 GE SFP28 passive direct attach cable, 5m, -40°C to 85°C, transceivers included, for
25 GE SFP28 Passive Direct Attach Cable FN-CABLE-SFP28-5
systems with SFP28 slots.
7


**Table 7.1**

| PRODUCT | SKU | DESCRIPTION |
| --- | --- | --- |
| ACCESSORIES |  |  |


**Table 7.2**

| APPLICABLE TO FNR-2500G ONLY |  |  |
| --- | --- | --- |


**Table 7.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FortiNDR and FortiNDR Cloud Licensing FAQs
General FAQ:
Are there any device limits in the FortiNDR On-premise and FortiNDR Cloud solutions?
No, there are no device limits. FortiNDR Cloud, being a SaaS solution, is licensed on bandwidth.
When do customers require the 3rd party log ingestion SKU for FortiNDR Cloud?
If customer requires to ingest of Zscaler (cloud to cloud) and Netflow logs (to sensors), SKU based on 100EPS (events per
second) of the required quantity are required to be purchased.
How is FortiNDR Cloud licensed?
FortiNDR Cloud is licensed based on total aggregated bandwidth for all sensors sending traffic to the cloud. For example, five
sensors sending 10Gbps to cloud. Physical sensors are ordered separately with support. Virtual and public cloud sensors are
free of charge.
How can I upgrade bandwith license for FortiNDR Cloud?
FortiNDR Cloud license can be upgrade via Fortinet co-term tool.
How is FortiNDR On-premises licensed?
FortiNDR is licensed based on number of appliance/VM purchased, with additional NetfFlow and OT security services licenses
on sensors. Center can be purchased to manage/provide single point of view of sensors.
For central management:
For FortiNDR On-premise, do I need to purchase an additional license when using FNR-3600G or central management VM as
a center to manage sensors?
No. The FNR-3600G or Central Manager VM operates in center mode managing sensors with no additional license required for
sensor management. Starting v7.6.3 both FNR-3600G and Centralized Management VM supports global investigation which
provides ability to query network meta data. A demo can be seen here.
For FortiNDR On-premise, do I need to purchase a NetFlow license for center management?
No. NetFlow is licensed on sensors only.
For FortiNDR On-premise, do I need to purchase an OT license for center management?
No. OT Security is licensed on sensors only.
For FortiNDR centralized VM center, what are the differences between the two center VM SKUs?
The difference is in the number of devices managed. SKU FC1-10-AIVMC-757-02-DD can allow management of up to ten
devices, and SKU SKU FC5-10- AIVMC-757-02-DD can allow management of unlimited sensors.
For FortiNDR centralized VM center, what if I need an upgrade to manage more than ten sensors?
You will need to purchase a new subscription of unlimited sensors.
8


**Table 8.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FORTINET TRAINING AND CERTIFICATION
FortiNDR On-Premises Administrator Training and Certification
This course covers the administration, management, and troubleshooting of an on-premises FortiNDR deployment. It explores
various use cases and examines the diverse source feeds utilized by FortiNDR. The integration of FortiNDR within the Fortinet
Security Fabric and its collaboration with other products to enhance malware detection and enable automated responses are
also highlighted. Additionally, the course delves into FortiNDR’s features, providing administrators with a comprehensive view of
detected anomalies and tools for forensic analysis.
FortiNDR Cloud Workshop
This workshop introduces the fundamentals of using FortiNDR Cloud. Participants will learn to identify and investigate Incidents
of Compromise using the tools available within the platform. Through interactive labs, attendees will explore configuration
options and settings in FortiNDR Cloud.
Course Details
For prerequisites, agenda topics, and learning objectives, visit:
FortiNDR On-Premises Administrator:
https://training.fortinet.com/local/staticpage/view.php?page=library_fortindr-on-premises-administrator
FortiNDR Cloud Workshop:
https://training.fortinet.com/local/staticpage/view.php?page=library_fortindr-cloud
Training SKUs for FortiNDR and FortiNDR Cloud
For training SKUs, purchasing, and delivery options, visit:
https://training.fortinet.com/local/staticpage/view.php?page=purchasing_process
www.fortinet.com
Copyright © 2025 Fortinet, Inc. All rights reserved. Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product or
company names may be trademarks of their respective owners. Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other condi-
tions may affect performance results. Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s SVP Legal and above, with a purchaser
that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet. For absolute clarity, any
such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify, transfer, or otherwise
revise this publication without notice, and the most current version of the publication shall be applicable.
FNDR-OG-R35-20251126
