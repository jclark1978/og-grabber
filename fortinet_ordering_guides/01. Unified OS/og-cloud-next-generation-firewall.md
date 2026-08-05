# og-cloud-next-generation-firewall

Ordering Guide
Fortinet Cloud
NGFW Solutions
FortiOS powers all of Fortinet’s next generation firewall (NGFW) offerings, including
cloud network security solutions. Customers can purchase these solutions in flexible
ways that suit their requirements, such as virtual machines (VM) for private and public
cloud networks and software-as-a-service solutions for public cloud networks. They can
also buy subscription licenses from cloud marketplaces and choose between pay as you
go (PAYG) options or annual commitment contracts. To help customers select the most
suitable cloud network security solution, this guide provides different options:
• FortiGate-VM: for customers seeking to protect private cloud workloads or tailor
FortiGate-VM deployment to their needs in the public cloud, FortiGate-VM is the best
(and only) option. It allows them to specifically design network integration and use the
latest FortiOS enhancements. FortiGate-VM is the only cloud NGFW solution offering
NAT, VPN, and SD-WAN functionality.
• FortiFlex: allows customers to consume FortiGate-VM and other Fortinet products
on-demand using a points-based system, but does not provide unique technical
capabilities.

Fortinet Cloud NGFW Solutions Ordering Guide
FortiGate-VM Virtual NGFW
FortiGate is the flagship NGFW product family from Fortinet that delivers high-speed networking, increased scalability, and
optimized performance features. Operators using the FortiGate NGFW can manage all of their security risks with the industry’s
best-of-breed IPsec, GTP, PFCP, IPS, and TLS inspection; and threat protection. FortiGate comes in different form factors
and sizes and you can deploy it at the network edge, the core data center, and the public cloud. Fortinet offers FortiGate as
appliances or VMs with different options for interface types, port density, security efficacy, and throughput to keep your network
connected and secure wherever it is needed.
FortiGate-VM is available as a virtual appliance and for several cloud flavors, such as:
• Public clouds: Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP), Oracle Cloud Infrastructure (OCI),
IBM Cloud, and Alibaba Cloud (AliCloud)
• Private clouds/hypervisors: VMware (vSphere/NSX-T), OpenStack/KVM, Microsoft Hyper-V, Nutanix, and Citrix-Xen
2


**Table 2.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

Fortinet Cloud NGFW Solutions Ordering Guide
Product Offerings - Security
Fortinet offers FortiGate-VM in the following license schemes:
• Term-based subscription: FortiGate-VM s-series
• FortiFlex: points-based consumption model for enterprise and managed security service providers (MSSP) (12-, 36-, or
60-month subscription)
• Public cloud PAYG: per-hour priced (based in number of vCPUs) PAYG offers available in AWS, Azure, GCP, and OCI
marketplace
ATP UTP ENTERPRISE
SECURITY UPDATES AND SERVICES
Device/OS Detection   
SaaS Database (ISDB)   
Application Control   
Certificates   
IPS   
Antivirus   
Botnet DB   
Mobile Malware   
FortiGate Cloud Sandbox   
Outbreak Prevention   
Web Filtering  
Video Filtering  
Secure DNS Filtering  
AntiSpam  
IoT Mac Database  
IoT Query Service 
Fortinet Security Fabric Rating 
NETWORKING AND MANAGEMENT SERVICES
DDNS   
IPv6 DDNS   
GeoIP Updates   
FORTICARE SUPPORT SERVICES
Enhanced Support (24x7)   
FortiConverter 
FortiGate-VMs with eight or more vCPUs are eligible to run the full extended database (DB). Any FortiGate-VM with fewer than
eight cores receives a slim DB for performance, which is a smaller version of the full-extended DB that contains top active IPS
signatures. The customer can choose eight or more vCPUs for full IPS protection or lower vCPUs for cost and performance.
See Support full extended IPS database for FortiGate VMs with eight cores or more.
3


**Table 3.1**

|  | ATP | UTP | ENTERPRISE |
| --- | --- | --- | --- |
| SECURITY UPDATES AND SERVICES |  |  |  |


**Table 3.2**

| NETWORKING AND MANAGEMENT SERVICES |  |  |
| --- | --- | --- |


**Table 3.3**

| FORTICARE SUPPORT SERVICES |  |  |  |
| --- | --- | --- | --- |


**Table 3.4**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

Fortinet Cloud NGFW Solutions Ordering Guide
Product Offerings - Performance
FortiGate-VM delivers high performance by combining technologies such as single root I/O virtualization (SR-IOV) and Fortinet
vSPU. SR-IOV allows the partition of a single physical network controller into multiple virtual interfaces called virtual functions.
The Fortinet vSPU refers to the combination of FortiOS vNP and DPDK libraries in the FortiGate-VM. The vSPU enhances
FortiGate-VM performance by offloading part of packet processing to userspace while bypassing kernel within the operating
system. The vNP is the software emulation of a subset of Fortinet’s network processor (NP).
For performance information, see the FortiGate-VM on VMware ESXi datasheet and FortiGate-VM on Linux KVM datasheet.
Order Information - Public Cloud
PUBLIC CLOUD
1 VCPU ORDER INFORMATION RECOMMENDED INSTANCE*
AWS t2.small/c8gn.medium
Azure FC1-10-FGVVS-990-02-DD Standard_D2s_v5/Standard_D2ps_v6
GCP n1-standard-1/c4a-standard-1
2 VCPU
AWS c6in.large/c8gn.large
Azure Standard_D2s_v5/Standard_D2ps_v6
GCP FC2-10-FGVVS-990-02-DD c4-standard-2/c4a-standard-2
Oracle VM.Standard3.Flex (1 OCPU)/VM.Standard.A1.Flex (2 OCPU)
AliCloud ecs.c9i.large
4 VCPU
AWS c6in.xlarge/c8gn.xlarge
Azure Standard_D4s_v5/Standard_D4ps_v6
GCP FC3-10-FGVVS-990-02-DD c4-standard-4/n2-standard-4/c4a-standard-4
Oracle VM.Standard3.Flex(2 OCPU)/VM.Standard.A1.Flex (4 OCPU)
AliCloud ecs.c9i.xlarge
8 VCPU
AWS c6in.2xlarge/c8gn.2xlarge
Azure Standard_D8s_v5/Standard_D8ps_v6
GCP FC4-10-FGVVS-990-02-DD c4-standard-8/n2-standard-8/c4a-standard-8
Oracle VM.Standard3.Flex(4 OCPU)/VM.Standard.A1.Flex (8 OCPU)
AliCloud ecs.c9i.2xlarge
16 VCPU
AWS c6in.4xlarge/c8gn.4xlarge
Azure Standard_D16s_v5/Standard_D16ps_v6
GCP FC5-10-FGVVS-990-02-DD c4-standard-16/n2-standard-16/c4a-standard-16
Oracle VM.Standard3.Flex(8 OCPU)/ VM.Standard.A1.Flex (16 OCPU)
AliCloud ecs.c9i.4xlarge
32 VCPU
AWS c6in.8xlarge/c8gn.8xlarge
Azure Standard_D32s_v5/Standard_D32ps_v6
GCP FC6-10-FGVVS-990-02-DD c4-standard-32/c4a-standard-32
Oracle VM.Standard3.Flex 16 OCPU/VM.Standard.A1.Flex (32 OCPU)
AliCloud ecs.c9i.8xlarge
UNLIMITED CPU
AWS c6in.16xlarge/c8gn.16xlarge
GCP FC7-10-FGVVS-990-02-DD c4-standard-48, c4-standard-96, c4a-standard-48, c4a-standard-64, c4a-standard-72
Oracle VM.Standard3.Flex/VM.Standard.A1.Flex
* c6in.large to c6in.8xlarge support up to 12.5 Gbps.
4


**Table 4.1**

| PUBLIC CLOUD |  |  |
| --- | --- | --- |
| 1 VCPU | ORDER INFORMATION | RECOMMENDED INSTANCE* |


**Table 4.2**

| 2 VCPU |  |  |
| --- | --- | --- |


**Table 4.3**

| 4 VCPU |  |
| --- | --- |


**Table 4.4**

| 8 VCPU |  |
| --- | --- |


**Table 4.5**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

Fortinet Cloud NGFW Solutions Ordering Guide
Order Information - Public Cloud
PUBLIC CLOUD - PAYG
ARCHITECTURE ORDER INFORMATION RECOMMENDED INSTANCE MARKETPLACE PRODUCT
AWS c6in.xlarge (Intel) AWS FortiGate x64
AWS ARM c8gn.large (ARM) AWS FortiGate ARM
Dv5 Series (Intel)
Azure* Dasv5 Series (AMD) Azure FortiGate
Dpsv6 Series (ARM)
c4-standard-4 (Intel)
GCP PAYG GCP FortiGate x64
c4a-standard-4 (ARM)
OCI 2 OCPU x64
VM.Standard.3.Flex (Intel)
OCI 4 OCPU x64
OCI** VM.Standard.E5.Flex (AMD)
OCI 8 OCPU x64
VM.Standard.A1.Flex (ARM)
OCI 24 OCPU x64
AliCloud ecs.c9i Instance Family (Intel) AliCloud FortiGate x64
* Azure PAYG is selected on the portal GUI with the FortiOS version.
** In Oracle Cloud, note the following:
- AMD and Intel: 1 OCPU = 2 vCPU
- ARM: 1 OCPU = 1 vCPU
Plan deployments accordingly.
5


**Table 5.1**

| PUBLIC CLOUD - PAYG |  |  |  |
| --- | --- | --- | --- |
| ARCHITECTURE | ORDER INFORMATION | RECOMMENDED INSTANCE | MARKETPLACE PRODUCT |


**Table 5.2**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

Fortinet Cloud NGFW Solutions Ordering Guide
Order Information - Private Cloud
HYBRID CLOUD: VMWARE ESXI, KVM, MICROSOFT HYPER-V, AND XEN
1 VCPU TERM SUBSCRIPTION ORDER INFORMATION
ATP Bundle FC1-10-FGVVS-993-02-DD
UTP Bundle FC1-10-FGVVS-990-02-DD
Enterprise Bundle FC1-10-FGVVS-814-02-DD
2 VCPU
ATP Bundle FC2-10-FGVVS-993-02-DD
UTP Bundle FC2-10-FGVVS-990-02-DD
Enterprise Bundle FC2-10-FGVVS-814-02-DD
4 VCPU
ATP Bundle FC3-10-FGVVS-993-02-DD
UTP Bundle FC3-10-FGVVS-990-02-DD
Enterprise Bundle FC3-10-FGVVS-814-02-DD
8 VCPU
ATP Bundle FC4-10-FGVVS-993-02-DD
UTP Bundle FC4-10-FGVVS-990-02-DD
Enterprise Bundle FC4-10-FGVVS-814-02-DD
16 VCPU
ATP Bundle FC5-10-FGVVS-993-02-DD
UTP Bundle FC5-10-FGVVS-990-02-DD
Enterprise Bundle FC5-10-FGVVS-814-02-DD
32 VCPU
ATP Bundle FC6-10-FGVVS-993-02-DD
UTP Bundle FC6-10-FGVVS-990-02-DD
Enterprise Bundle FC6-10-FGVVS-814-02-DD
UNLIMITED CPU
ATP Bundle FC7-10-FGVVS-993-02-DD
UTP Bundle FC7-10-FGVVS-990-02-DD
Enterprise Bundle FC7-10-FGVVS-814-02-DD
VDOM SUBSCRIPTION OPTIONS
+5 VDOMs FC1-10-FGVVS-498-02-DD
FORTICARRIER UPGRADE SUBSCRIPTION
FortiCarrier Upgrade Subscription FC-10-FGVVS-948-02-DD
6


**Table 6.1**

| HYBRID CLOUD: VMWARE ESXI, KVM, MICROSOFT HYPER-V, AND XEN |  |
| --- | --- |
| 1 VCPU | TERM SUBSCRIPTION ORDER INFORMATION |


**Table 6.2**

| 2 VCPU |  |
| --- | --- |


**Table 6.3**

| 4 VCPU |  |
| --- | --- |


**Table 6.4**

| 8 VCPU |  |
| --- | --- |


**Table 6.5**

| 16 VCPU |  |
| --- | --- |


**Table 6.6**

| 32 VCPU |  |
| --- | --- |


**Table 6.7**

| UNLIMITED CPU |  |
| --- | --- |


**Table 6.8**

| VDOM SUBSCRIPTION OPTIONS |  |
| --- | --- |


**Table 6.9**

| FORTICARRIER UPGRADE SUBSCRIPTION |  |
| --- | --- |


**Table 6.10**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

Fortinet Cloud NGFW Solutions Ordering Guide
FortiFlex Program
Product Offering - Overview
FortiFlex allows customers to easily manage license entitlements for FortiGate-VM, FortiWeb-VM, FortiManager-VM, and
FortiAnalyzer-VM. You can use the FortiFlex portal or its API to create VM configurations, generate licensing entitlements, and
monitor resource consumption in the form of points. FortiFlex subscribers can create multiple sets of a single VM entitlement
that corresponds to a licensed VM. Each entitlement contains a base VM with the number of vCPUs, FortiGuard services
(bundles or à la carte), and FortiCare support services. Resource consumption is based upon predefined points that are
calculated daily.
Devices with usage entitlements require installing a one-time token on every VM. You can inject these tokens into the FortiGate-
VM via cloud-init or an OVF environment, once the VM configurations and vCPU quantities are defined in the FortiFlex portal,
and the VMs are deployed on the customer-managed platform in supported clouds and hypervisors.
FortiFlex is available as a prepaid service for enterprise customers and as a postpaid service for approved MSSP partners.
FortiFlex provides a powerful REST API that you can combine with the FortiOS REST API to provide a full automated VM lifecycle
management.
For information about the FortiFlex program, see its ordering guide.
Order Information
• You must register all SKU purchases within 365 days of the purchase date.
• For the MSSP program only, a minimum consumption of 50,000 points per year is required.
For Enterprise, in the case of excess consumption, there is a 90-day grace period to recover from a negative balance. VM
entitlements stop operation after the grace period ends. During the grace period, new entitlements cannot be created.
For MSSP, in the case of underconsumption, there is a true-up to meet the minimum annual consumption amount if usage is
lower. VM entitlements stop operation after the grace period ends.
FLEX-VM PROGRAMS SKU POINTS ROLLOVER POINTS EXPIRATION
FC-10-ELAVR-221-02-DD
Program N/A
(DD = 12, 36, or 60 months)
LIC-FLXPTS-1K
LIC-FLXPTS-10K
Stackable Packs 100% 3 years from purchase date
Prepaid - Enterprise LIC-FLXPTS-50K
LIC-FLXPTS-100K
LIC-FLXPTS-BULK-5K
100% 3 years from purchase date
BULK Packs (MOQ 50,000 points)
LIC-FLXPTS-BULK (MOQ 1,000,000 poins) 100% 5 years from purchase date
FC-10-ELAVS-221-02-DD
Program N/A
Postpaid - MSSP (DD = 12, 36, or 60 months)
Monthly Billing FCB-ELAVM-01 N/A
7


**Table 7.1**

| FLEX-VM PROGRAMS |  | SKU | POINTS ROLLOVER | POINTS EXPIRATION |
| --- | --- | --- | --- | --- |


**Table 7.2**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

Fortinet Cloud NGFW Solutions Ordering Guide
FortiFlex Program
FortiFlex Daily Points Pricing
You can calculate daily points pricing for both FortiGate-VM and FortiWeb-VM using the FortiFlex Calculator available on FNDN.
Select the product type, number of vCPUs, CPU size, and service bundle accordingly.
Fortinet Training and Certification
FCSS – Enterprise Firewall Administrator training
Learn how to use the most common FortiGate features.
In interactive labs, explore firewall policies, user authentication, high availability, SSL VPN, site-to-site IPsec VPN, Fortinet
Security Fabric, and how to protect your network using security profiles, such as IPS, antivirus, web filtering, application control,
and more. These administration fundamentals will provide a solid understanding of how to implement the most common
FortiGate features.
FCSS - Public Cloud Security Architect Training and Certification
This course teaches how to use various methods to deploy Fortinet solutions in the public cloud. It covers using third-party
automation tools to deploy and secure cloud resources, effectively troubleshooting common connectivity issues in Azure and
AWS, and leveraging FortiCNP to streamline risk management for cloud workloads.
Course Descriptions
For prerequisites, agenda topics, and learning objectives, visit:
https://training.fortinet.com/local/staticpage/view.php?page=library_enterprise-firewall
https://training.fortinet.com/local/staticpage/view.php?page=library_public-cloud-security
Training Offering
For training SKUs, purchasing, and delivery options, visit:
https://training.fortinet.com/local/staticpage/view.php?page=purchasing_process
8

Fortinet Cloud NGFW Solutions Ordering Guide
The Space Product Lineup
Virtualization and software-defined networks (SDN) FortiGate-VM product supports various cloud types
are rapidly transforming datacenters into agile, and providers:
innovative, software-defined, and cost-effective • Public clouds: AWS, GCP, Azure, OCI, IBM, and
clouds: public and private. AliCloud
Security is not guaranteed in these cloud environments • Private clouds: VMware, OpenStack/KVM,
and level of protection differs with various deployment Microsoft Hyper-V, and Citrix Xen
models.
Flex-VM adds flexibility on top of the FortiGate-VM
A virtual NGFW increases visibility and protection in and FortiWeb-VM offerings by providing a point
these cloud environments regardless of variations in consumption-based model for enterprise and MSSP.
deployments.
Ordering Guide Major Highlights
BYOL: you can use bring your own license (BYOL) for Fortinet has comprehensive security solutions for
FortiGate-VM in virtualized datacenter, private cloud, clouds covering the different network areas.
and public cloud deployments. We have a market-leading TCO and scaling for user
BYOL licensing types include term subscriptions plane use cases thanks to our vSPU (vNP + DPDK).
(12/36/60 months) and Flex-VM subscriptions This is key to match exponential traffic growth.
(12/36/60 months). The move to cloud and containers increases the attack
Cloud marketplace instance: customers can surface as the internals of the compute nodes are now
purchase FortiGate-VM PAYG instances from a cloud open.
service provider marketplace, such as AWS, Azure, In private networks, Fortinet has a single solution that
GCP, AliCloud, or OCI. These instances incur hourly can simultaneously secure the wired OT, the Wi-Fi,
charges and are payable monthly. Depending on the and 5G access.
cloud provider, customers can also enroll into annual
We have tools to detect zero-day attacks and lateral
contracts with better hourly pricing.
movements as they occur.
Major Competitors
PAN: provides an enterprise ELA program, which only
has a la carte. Lacks a program for MSSP. Daily points
are usually 30% more expensive.
Juniper: SecGW and NGFW primarily. Sales tied to
Ericsson. Worse performance than Fortinet.
Checkpoint: SecGW & NGFW primarily. Worse
performance than Fortinet.
www.fortinet.com
Copyright © 2026 Fortinet, Inc. All rights reserved. Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product or
company names may be trademarks of their respective owners. Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other condi-
tions may affect performance results. Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s SVP Legal and above, with a purchaser
that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet. For absolute clarity, any
such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify, transfer, or otherwise
revise this publication without notice, and the most current version of the publication shall be applicable.
July 9, 2026 9:27 AM
CNGFW-OG-R24-20260709
