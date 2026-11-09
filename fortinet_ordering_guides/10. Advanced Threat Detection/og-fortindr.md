# og-fortindr

Ordering Guide
FortiNDR
FortiNDR Cloud and FortiNDR on-premises represent the future of artificial intelligence (AI)-
driven, network-based breach protection technology designed to detect sophisticated and hidden
threats and malware on the network. It uses supervised and unsupervised machine learning (ML)
to continuously analyze metadata, especially east-west data in data centers, to identify threats,
especially threats that may already be persistent in the network.
Two different NDR deployments are available:
• FortiNDR Cloud: Processes network traffic in the cloud and provides 365-day retention and
advanced network detection and threat hunting functionality. Provides SaaS console for
customers to monitor detections and threat hunting. FortiNDR Cloud is SOC II compliant.
• FortiNDR on-premises: Stores and processes all data locally. Nothing leaves the network.
Standalone, center and sensor mode available to suit distributed sites deployment.

FortiNDR Ordering Guide
FortiNDR Cloud
FortiNDR Cloud is a cloud-based SaaS offering that leverages AI, ML, and behavioral and static analysis to assess network
traffic and spot threats early in the attack lifecycle.
FortiNDR Cloud includes a Technical Success Manager* to assist each deployment and has regular cadence calls with users to
optimize solution deployment.
Apart from receiving traffic using FortiNDR cloud hardware sensors and VMs, FortiNDR Cloud also allows third-party log
ingestion with NetFlow, Zscaler and AWS VPC logs. This functionality requires the third-party logs ingestion SKU, while
Netskope integration uses the normal device-based SKU by deploying AWS sensors for ingestion.
Fortinet Security Automation service allows FortiNDR to integrate with SOAR cloud service to enable Fortinet connectors and
third-party integrations. Please refer to the product documentation for details.
Following is the FortiNDR Cloud architecture diagram:
*For customers with 5,000+ devices (FC2 tier and above)
For FortiNDR Cloud hardware sensor technical specifications, see the datasheet.
2


**Table 2.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FortiNDR Cloud Order Information
FORTINDR CLOUD - SAAS SERVICE (DEVICES BASED SUBSCRIPTION)
LICENSE FOR NUMBER OF
SKU DESCRIPTION UNIT
DEVICES
FortiNDR Cloud Subscription for 150-5000 unique devices/IPs. Includes FortiCare
FC1-10-NDRCD-1418-02-DD 150 (minimum) – 5,000 Price per endpoint
premium. Includes unlimited VM sensors. Physical Sensors purchased separately.
FortiNDR Cloud Subscription for 5001-20,000 unique devices/IPs. Includes
FC2-10-NDRCD-1418-02-DD 5,001 – 20,000 FortiCare premium. Includes unlimited VM sensors. Physical Sensors purchased
separately.
FortiNDR Cloud Subscription for 20,001-50,000 unique devices/IPs. Includes
FC3-10-NDRCD-1418-02-DD 20,001-50,000 FortiCare premium. Includes unlimited VM sensors. Physical Sensors purchased
separately.
FortiNDR Cloud Subscription for 50,001 - 100,000 unique devices/IPs. Includes
FC4-10-NDRCD-1418-02-DD 50,001 - 100,000 FortiCare premium. Includes unlimited VM sensors. Physical Sensors purchased
separately.
FortiNDR Cloud Subscription for 100,001 to 150,000 unique devices/IPs. Includes
FC5-10-NDRCD-1418-02-DD 100,001 to 150,000 FortiCare premium. Includes unlimited VM sensors. Physical Sensors purchased
separately.
FortiNDR Cloud Subscription for 150,001 to unlimited unique devices/IPs. Includes
FC6-10-NDRCD-1418-02-DD 150,001 to unlimited FortiCare premium. Includes unlimited VM sensors. Physical Sensors purchased
separately.
FORTINDR CLOUD - SAAS SERVICE (SECURITY AUTOMATION & 3RD PARTY LOGS ADD-ONS)
SKU DESCRIPTION STACKABLE (QTY > 1) EXAMPLES
Security Automation Service providing 500 playbooks QTY = 1 enables 500 playbooks per day
FC1-10-NDRCD-1300-02-DD executions per day capacity. Increase quantity to Yes QTY = 2 enables 1000 playbooks per day
enable additional playbooks executions. (Mandatory)
FortiNDR Cloud add on: Adds 1GB/day of licensed
ingestion (Zscaler/AWS VPC/NetFlow). Requires QTY = 1 enables 1GB/day
FC1-10-NDRCD-1419-02-DD Yes
FortiNDR devices based licensing subscription. (default QTY = 5 enables 5GB/day
1 month for Zscaler/AWS VPC/NetFlow).
QTY = 1 enables one additional months
FortiNDR Cloud add on: Adds 1 month of archive (e.g. 2 months of retention) for 1GB/day)
retention for 3rd party logs (Zscaler/AWS VPC/NetFlow)
FC1-10-NDRCD-1420-02-DD Yes
per GB/day of licensed inspection. Requires at least 1 QTY = 5 * 2 = 10, enables five additional
GBs/day ingestion months (e.g. 6 months of retention) for 2GB/
day
1 Measure of total devices by all sensors. For example, five sensors combined with 10K devices license requires 10K licensing tier times number of endpoints.
2 ”DD” specifies the contract length in months. Available terms are 1, 3, and 5 years (i.e. 12, 36, and 60 months). Any order e.g. 2 or 4 years will require the same QTY in same order for
registration.
All initial orders must include cloud services with at least one devices based tier. Customers may purchase hardware sensors or use the free virtual sensors to provide traffic ingest into
SaaS. For Tranceivers required please see the FortiNDR Cloud datasheet.
3


**Table 3.1**

| FORTINDR CLOUD - SAAS SERVICE (DEVICES BASED SUBSCRIPTION) |  |  |  |
| --- | --- | --- | --- |
| SKU | LICENSE FOR NUMBER OF DEVICES | DESCRIPTION | UNIT |


**Table 3.2**

| FORTINDR CLOUD - SAAS SERVICE (SECURITY AUTOMATION & 3RD PARTY LOGS ADD-ONS) |  |  |  |
| --- | --- | --- | --- |
| SKU | DESCRIPTION | STACKABLE (QTY > 1) | EXAMPLES |


**Table 3.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FortiAI tokens for FortiNDR Cloud
FORTIAI TOKENS TOP-UP LICENSE
SKU DESCRIPTION
LIC-FAITOKEN-1M FortiAI-Assist top-up SKU license for adding 1,000,000 AI tokens valid for 3 years.
LIC-FAITOKEN-5M FortiAI-Assist top-up SKU license for adding 5,000,000 AI tokens valid for 3 years.
LIC-FAITOKEN-10M FortiAI-Assist top-up SKU license for adding 10,000,000 AI tokens valid for 3 years.
Examples of FortiAI Token usage:
COMPLEXITY QUESTION AVERAGE TOKENS (INPUT + OUTPUT)
Simple What can I do with FortiAI? 5,000
Moderate Show me the latest critical detections in my network. 30,000
Moderate What suspicious activities have been detected in my network recently? 50,000
Complex Investigate IP x.x.x.x 300,000
Complex Investigate a detection ABC 300,000
Note: Token usage varies depending on the size of the customer’s data. The table above shows usage for an average-sized customer.
4


**Table 4.1**

| FORTIAI TOKENS TOP-UP LICENSE |  |
| --- | --- |
| SKU | DESCRIPTION |


**Table 4.2**

| COMPLEXITY | QUESTION | AVERAGE TOKENS (INPUT + OUTPUT) |
| --- | --- | --- |


**Table 4.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FortiNDR Cloud example orders
Example Order:
Monitoring traffic with 3,500 IPs on AWS infrastructure over a one-year period. A SOC analyst would like to use FortAI to simplify
operations. The Security Automation Service is required to deploy FortiDeceptor decoys (Dynamic Deception).
• Term: 1 year (12 months)
• Total Devices: 3,500 IPs
• All virtual sensors are free of charge
• FortiAI natural language assistance – required (light SOC usage)
SKUs required:
• Cloud services (3500 x FC1-10-NDRCD-1418-02-12), using 1st licensing tier 150-5000 endpoints
• Security Automation Service required: FC1-10-NDRCD-1300-02-12 * 1 (enables FortiDeceptor integration of 500 playbooks
per day)
• Public cloud sensors (supports AWS, Azure, OCI and GCP). Can be downloaded free of charge after cloud SaaS services are
provisioned.
• FortiAI (required) 1mil tokens (1 x LIC-FAITOKEN-1M) for light/moderate usage.
Examples of larger and distributed deployment:
Monitoring multiple office locations and cloud traffic along with NetFlow & Zscaler Ingest (3 months retention required).
Integration with third-party NGFW (e.g. Palo Alto) required for endpoint isolation, and for Jira/ServiceNow integration.
• Term: 3 years (36 months SKU)
• Total Devices: 80,000 IPs
• Zscaler and NetFlow combined log rate: 10K EPS (at approx. 432GB/day, with 500bytes/1000bytes for NetFlow and Zscaler
record size respectively)
• 2 large physical sensors, 3 virtual sensors (monitoring of 5 locations)
• FortiAI natural language assistance – required (moderate SOC usage)
SKUs required:
• Cloud services: 80,000 times FC4-10-NDRCD-1418-02-36 (80K endpoints using tier4 [50,001 to 100,000 devices] with 3
years term -36months)
• Large hardware sensors: FNRC-900G x2
• Hardware sensor subscription and support: FC-10-NDR9G-247-02-36 x 2 (for two sensors)
• Virtual sensors: Downloaded free of charge (x3)
• Security Automation Service required: FC1-10-NDRCD-1300-02-36 * 1 (enables Palo Alto firewall quarantine and Jira/
ServiceNow integration of 500 playbooks per day)
• Zscaler and NetFlow log ingestion: FC1-10-NDRCD-1419-02-36 x 432 (432 GB/day required for 3 years, default to 1 month
storage
• Zscaler and NetFlow log retention: FC1-10-NDRCD-1420-02-36 x 432 * 2 (2 additional months, total 3 months of retention
for 432 GB/day required for 3 years)
• FortiAI: 5 mil tokens (1 x LIC-FAITOKEN-5M )
5


**Table 5.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FortiNDR On-premises
FortiNDR on-premises is suitable for customers with on-premises SOC capacity or to satisfy air-gap or high compliance
deployments where all data remains on-premises. Leveraging Fortinet Security Fabric integration, FortiNDR can automatically
discover and classify every device communicating across the network, including east/west traffic in the data center. FortiNDR
also supports high throughput malware scanning with ANN and supports various Fabric integrations.
Here is a reference architecture diagram with FortiNDR:
FortiNDR on-premises hardware and virtual machines can run in three modes:
• Standalone (VM16, VM32, FortiNDR-1000F, FortiNDR-2500G)
• Center (supported on FNR-2500G, FNR-3600G, and Center VM models only)
• Sensors (VM08, VM16, VM32, FortiNDR-1000F, FortiNDR-2500G)
Center and sensors modes are used for deploying distributed deployment. See the following table or datasheet for mode
support for different models.
6


**Table 6.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FortiNDR Hardware Order Information
SOLUTION BUNDLE FORTINDR-1000F FORTINDR-2500G FORTINDR-3600G
Hardware Bundles Hardware Bundle FNR-1000F-BDL-331-DD2 FNR-2500G-BDL-331-DD2 FNR-3600G-BDL-331-DD
Renewal FC-10-AI1KF-331-02-DD2 FC-10-AI25G-331-02-DD2 FNR-3600G-BDL-1024-DD
Deploy Mode Standalone, Sensor Standalone, Sensor, Center Center only
Sensors Managed1 N/A Up to 10 Up to 50
Active-passive
High Availability Support Active-passive
(standalone mode) Dual center support (center mode)
(for all models) (standalone mode)
Dual center support (center mode)
NetFlow Support FC-10-AI25G-588-02-DD2
FC-10-AI1KF-588-02-DD2
(licensed separately) Not required in center mode
N/A (license on sensors)
OT Security Services FC-10-AI25G-723-02-DD2
FC-10-AI1KF-723-02-DD2
(licensed separately) Not required in center mode
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
NetFlow Support
Not supported FC3-10-AIVMS-588-02-DD2 FC4-10-AIVMS-588-02-DD2
(licensed separately)
Licensed on sensors
OT Security Services
FC2-10-AIVMS-723-02-DD2 FC3-10-AIVMS-723-02-DD2 FC4-10-AIVMS-723-02-DD2
(licensed separately)
1 For cases that require more than the specified number of sensors, consult your local Fortinet engineering team.
2 “DD” specifies the contract length in months. Available terms are 1, 3, and 5 years (i.e. 12, 36, and 60 months).
7


**Table 7.1**

| SOLUTION BUNDLE |  | FORTINDR-1000F | FORTINDR-2500G | FORTINDR-3600G |
| --- | --- | --- | --- | --- |


**Table 7.2**

| SOLUTION BUNDLE | VM08 | VM16 | VM32 | VM CENTER |
| --- | --- | --- | --- | --- |


**Table 7.3**

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
8


**Table 8.1**

| PRODUCT | SKU | DESCRIPTION |
| --- | --- | --- |
| ACCESSORIES |  |  |


**Table 8.2**

| APPLICABLE TO FNR-2500G ONLY |  |  |
| --- | --- | --- |


**Table 8.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FortiNDR On-Premises Ordering Examples
Order example:
Monitor traffic in an OT environment with FortiNDR, with a FortiGate sending NetFlow data to this standalone deployment. The
deployment consists of two independently operated sites: one using a FortiNDR-1000F and the other using a FortiNDR-VM. Site
1 requires hardware due to throughput requirements, while Site 2 has a throughput requirement of 3 Gbps and can use a VM.
• Term: 3 years (36 months)
• Total Devices: approximately 2,000 IPs (FortiNDR On-Premises is licensed based on monitored throughput rather than the
number of devices, similar to FortiGate licensing.)
SKUs required:
• Site 1: FortiNDR-1000F (FNR-1000F x 1 base hardware)
Forticare support for FNR-1000F (FC-10-AI1KF-331-02-36 x 1)
Netflow support for FortiNDR-1000F (FC-10-AI1KF-588-02-36 x 1)
OT security service for FortiNDR-1000F (FC-10-AI1KF-723-02-36 x 1)
(Note: Transceivers quoted separately)
(Note: Bundle (BDL) SKUs can be used when the customer requires both NetFlow and OT Security services.)
• Site 2: FortiNDR-VM (16 CPU, FC3-10-AIVMS-461-02-36, 36 months term, includes FortiCare)
Netflow support FortiNDR-VM16 ( FC3-10-AIVMS-588-02-36 x 1)
OT security service for FortiNDR VM16 (FC3-10-AIVMS-723-02-36 x 1)
Examples of large distributed deployments:
Monitor traffic across five office locations using a dual-center deployment for redundancy, with hardware sensors and centers at
all sites. NetFlow and OT Security services are not required. FortiAnalyzer Cloud is required for alert response and reporting. The
SOC team also wants to use FortiAI on the FNR-3600G.
Site throughput as follows:
Term: 1 year (12-month SKU)
Site 1-4: 3-5 Gbps (FNR-1000F is sufficient)
Site 5: 12 Gbps (FNR-2500G is sufficient)
SKUs required:
• Sensors (site 1-4): FNR-1000F x 4
FortiCare support for FNR-1000F (FC-10-AI1KF-331-02-12 x 4)
Sensors (site 5): FNR-2500G x 1
FortiCare support for FNR-2500G (FC-10-AI25G-331-02-DD)
(Note: Rransceivers quoted separately)
• Dual center FNR-3600G x 2
FortiCare for FNR-3600G: FC-10-AI36G-1024-02-12
• FortiAnalyzer Cloud 5 GB/Day for Central logging and Analytics
FC1-10-AZCLD-463-01-12 x 1
9


**Table 9.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FortiNDR and FortiNDR Cloud Licensing FAQs
General FAQ:
How is FortiNDR Cloud licensed?
Starting in Q4 2026, FortiNDR Cloud is licensed based on the total number of unique devices across all sensors, with additional
SKUs available for the Security Automation Service (mandatory) and optional third-party log ingestion for NetFlow, Zscaler, and
AWS VPC.
When do customers require the third-party log ingestion SKU for FortiNDR Cloud?
If a customer requires ingestion of Zscaler and AWS VPC (cloud-to-cloud) logs and NetFlow logs (to sensors), they must
purchase the appropriate SKU based on the required GB/day ingestion volume.
How can I upgrade a device-based license for FortiNDR Cloud?
A FortiNDR Cloud device-based license can be upgraded using the Fortinet co-term tool.
How is FortiNDR On-premises licensed?
FortiNDR is licensed based on the number of appliances/VMs purchased, with additional NetFlow and OT security services
licenses on sensors. A Center can be deployed to manage sensors and provide a single point of management.
Are there any device limits in both FortiNDR Cloud and FortiNDR On-Premises solutions?
No, there are no device limits. FortiNDR On-Premises solutions are licensed based on appliance throughput, and FortiNDR Cloud
is licensed based on devices, with a minimum of 150 devices and no upper limit.
For FortiNDR On-premises central management
For FortiNDR On-premises, do I need to purchase an additional license when using FNR-2500G, FNR-3600G, or central
management VM as a center to manage sensors?
No. The FNR-2500G, FNR-3600G, or Central Manager VM operates in center mode managing sensors with no additional license
required for sensor management. Starting v7.6.3, all center mode units support global investigation which provides the ability to
query network metadata. A demo can be seen here.
For FortiNDR On-premises, do I need to purchase a NetFlow license for center management?
No. NetFlow is licensed on sensors only.
For FortiNDR On-premises, do I need to purchase an OT license for center management?
No. OT Security is licensed on sensors only.
For FortiNDR centralized VM center, what are the differences between the two center VM SKUs?
The difference is in the number of devices managed. SKU FC1-10-AIVMC-757-02-DD can allow management of up to ten
devices, and SKU FC5-10- AIVMC-757-02-DD can allow management of unlimited sensors.
For FortiNDR centralized VM center, what if I need an upgrade to manage more than ten sensors?
You will need to purchase a new subscription of unlimited sensors.
Does FortiAI Sovereign using GPU on FNR-3600G require any tokens purchase?
No, FortiAI Sovereign on FNR-3600G has local LLM model which can run without Internet and has unlimited token usage.
10


**Table 10.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiNDR Ordering Guide
FORTINET TRAINING AND CERTIFICATION
FortiNDR On-premises Administrator Training and Certification
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
FortiNDR On-premises Administrator:
https://training.fortinet.com/local/staticpage/view.php?page=library_fortindr-on-premises-administrator
FortiNDR Cloud Workshop:
https://training.fortinet.com/local/staticpage/view.php?page=library_fortindr-cloud-analyst
Training SKUs for FortiNDR and FortiNDR Cloud
For training SKUs, purchasing, and delivery options, visit:
https://training.fortinet.com/local/staticpage/view.php?page=purchasing_process
11


**Table 11.1**

|  |  |
| --- | --- |
|  |  |
|  |  |
