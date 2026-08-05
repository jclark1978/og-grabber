# og-operational-technology

Ordering Guide
®
Operational Technology (OT)
Industry’s Most Advanced and Integrated
OT Security Platform
The Fortinet OT Security Platform delivers a comprehensive suite of integrated security solutions
specifically engineered for operational technology (OT) environments.
It encompasses secure networking, unified secure access service edge (SASE), security operations,
dedicated threat intelligence, and a robust technology alliance ecosystem. The platform’s seamless
integration enables vendor consolidation, centralized visibility and control, and seamless IT/OT
convergence—driving operational efficiency, strengthening cyber resilience, and lowering total
cost of ownership.
The Fortinet OT Security Platform


**Table 1.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |


**Table 1.2**

|  |  |
| --- | --- |

Operational Technology (OT) Ordering Guide
Product Offerings
Fortinet offers a broad range of cybersecurity solutions The Security Platform approach for IT/OT minimizes
that deliver visibility, control, and actionable intelligence complexity, streamlines security operations, and reduces
across OT and converged IT/OT environments, while operational expenses (OpEx) for asset owners and
supporting compliance with industry regulations, standards, operators—offering a more efficient alternative to siloed
and best practices. point security solutions in separate IT and OT environments.
Fortinet OT Security Platform Use Cases to Solution Mapping
Solutions and Use Cases
Each solution offering is based on a single product or a
The Fortinet OT Security Platform supports a wide range of use combination of multiple products from Fortinet, and these
cases for securing industrial automation and control systems, solutions can be deployed either as standalone or integrated
cyber-physical systems, and critical infrastructure sectors. This with other products to meet the intended use case.
ordering guide provides a quick reference to the most widely The following table lists the specific Fortinet products that
deployed OT Security Platform solutions aligned with key make up each solution offering, mapped to the relevant use
cybersecurity use cases across both IT and OT environments. cases. These use cases correspond to the most commonly
The following sections present the OT Security Platform deployed products in the “Recommended Solutions” column,
solutions mapped to these use cases, based on industry guiding customers in selecting the right solution for their
best practices and cybersecurity requirements—serving as a needs. Additional products can be chosen from the “Optional
practical reference for navigating the guide. Solutions” column based on the organization’s risk exposure
and maturity level.
2


**Table 2.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

Operational Technology (OT) Ordering Guide
Use Cases to Solution Mapping
Secure Digital Networks
USE CASES DESCRIPTION RECOMMENDED SOLUTIONS OPTIONAL SOLUTIONS
Logical and physical division of a network into multiple segment or zones, FortiGate
Network Segmentation interconnected by a next generation firewall (NGFW) with single-pane-of-glass FortiSwitch FortiManager
management for network and security operations. FortiAP
Logical and physical division of a network into multiple microsegments or sub-zones,
FortiGate FortiManager
Network Microsegmentation interconnected by an NGFW with single-pane-of-glass management for network and
FortiSwitch FortiGuard Services
security operations.
Network access control solution that enhances the visibility, control, and automated
Network Access Control FortiNAC FortiGuard Services
response for everything that connects to the network.
Security and SD-WAN bundled in a single WAN-edge device, powered by a unified FortiSwitch
operating system, FortiOS. Integrated with FortiSwitch and FortiAP, it can offer FortiGate FortiAP
Secure SD-WAN/SD-Branch
complete network and security solution for remote site or branch with single-pane- FortiManager FortiExtender
of-glass management for network and security operations. FortiSASE
FortiGate
Enable secure remote access to critical IT/OT assets with VPN, multi-factor
FortiAuthenticator
Secure Remote Access authentication, network traffic inspection, and advanced threat protection to secure FortiPAM
FortiToken
the organizations and its remotely accessed digital assets.
FortiGuard Services
Protect web applications and APIs from internal and external attacks that target
Web Application Security FortiWeb FortiGuard Services
applications using known vulnerabilities and zero-day threats.
Secure Service Edge
USE CASES DESCRIPTION RECOMMENDED SOLUTIONS OPTIONAL SOLUTIONS
Implement enhanced user verification controls and go beyond username and
password to provide user verification requiring another factor.
FortiAuthenticator FortiGate
Identity and Access Management Multi-factor authentication (MFA) such as a one-time passcode (OTP) is a key
FortiToken FortiToken
security feature of the Fortinet IAM solution because it requires verification of
multiple credentials.
FortiGate
Take control of privileged accounts and enable monitoring of elevated user access, FortiPAM
Privileged Access Management FortiAuthenticator
processes, and critical systems across the IT/OT environments. FortiClient
FortiToken
FortiGate
Enforce authorization for users based on their roles through centrally defined access FortiPAM
Role Based Access Control FortiAuthenticator
control policy for accessing network resources. FortiClient
FortiToken
Deploy single sign-on (SSO) with centralized identity management and centrally
FortiGate
Single Sign-On manage user identities and their access to assets. SSO authenticates users with FortiAuthenticator
FortiToken
both traditional and modern web and cloud authentication protocols.
Critical assets need to be protected with the highest level of security. Fortinet
FortiPAM
IAM solutions allow for enhanced security including zero-trust network access
FortiClient FortiGate
(ZTNA) controls when users try to access critical assets. Zero trust starts with user
Zero Trust Network Access FortiNAC FortiAnalyzer
identities. Fortinet IAM product portfolio offers an end-to-end solution to implement
FortiAuthenticator FortiManager
least-privilege access to assets with enterprise-grade MFA. Plus, improve user
FortiToken
experience with SSO.
3


**Table 3.1**

| USE CASES | DESCRIPTION | RECOMMENDED SOLUTIONS | OPTIONAL SOLUTIONS |
| --- | --- | --- | --- |
| Network Segmentation | Logical and physical division of a network into multiple segment or zones, interconnected by a next generation firewall (NGFW) with single-pane-of-glass management for network and security operations. | FortiGate FortiSwitch FortiAP | FortiManager |
| Network Microsegmentation | Logical and physical division of a network into multiple microsegments or sub-zones, interconnected by an NGFW with single-pane-of-glass management for network and security operations. | FortiGate FortiSwitch | FortiManager FortiGuard Services |
| Network Access Control | Network access control solution that enhances the visibility, control, and automated response for everything that connects to the network. | FortiNAC | FortiGuard Services |
| Secure SD-WAN/SD-Branch | Security and SD-WAN bundled in a single WAN-edge device, powered by a unified operating system, FortiOS. Integrated with FortiSwitch and FortiAP, it can offer complete network and security solution for remote site or branch with single-pane- of-glass management for network and security operations. | FortiGate FortiManager | FortiSwitch FortiAP FortiExtender FortiSASE |
| Secure Remote Access | Enable secure remote access to critical IT/OT assets with VPN, multi-factor authentication, network traffic inspection, and advanced threat protection to secure the organizations and its remotely accessed digital assets. | FortiPAM | FortiGate FortiAuthenticator FortiToken FortiGuard Services |
| Web Application Security | Protect web applications and APIs from internal and external attacks that target applications using known vulnerabilities and zero-day threats. | FortiWeb | FortiGuard Services |


**Table 3.2**

| USE CASES | DESCRIPTION | RECOMMENDED SOLUTIONS | OPTIONAL SOLUTIONS |
| --- | --- | --- | --- |
| Identity and Access Management | Implement enhanced user verification controls and go beyond username and password to provide user verification requiring another factor. Multi-factor authentication (MFA) such as a one-time passcode (OTP) is a key security feature of the Fortinet IAM solution because it requires verification of multiple credentials. | FortiAuthenticator FortiToken | FortiGate FortiToken |
| Privileged Access Management | Take control of privileged accounts and enable monitoring of elevated user access, processes, and critical systems across the IT/OT environments. | FortiPAM FortiClient | FortiGate FortiAuthenticator FortiToken |
| Role Based Access Control | Enforce authorization for users based on their roles through centrally defined access control policy for accessing network resources. | FortiPAM FortiClient | FortiGate FortiAuthenticator FortiToken |
| Single Sign-On | Deploy single sign-on (SSO) with centralized identity management and centrally manage user identities and their access to assets. SSO authenticates users with both traditional and modern web and cloud authentication protocols. | FortiAuthenticator | FortiGate FortiToken |
| Zero Trust Network Access | Critical assets need to be protected with the highest level of security. Fortinet IAM solutions allow for enhanced security including zero-trust network access (ZTNA) controls when users try to access critical assets. Zero trust starts with user identities. Fortinet IAM product portfolio offers an end-to-end solution to implement least-privilege access to assets with enterprise-grade MFA. Plus, improve user experience with SSO. | FortiPAM FortiClient FortiNAC FortiAuthenticator FortiToken | FortiGate FortiAnalyzer FortiManager |


**Table 3.3**

|  |  |
| --- | --- |
|  |  |
|  |  |

Operational Technology (OT) Ordering Guide
Use Cases to Solution Mapping
Secure IT/OT Convergence
OPTIONAL
USE CASES DESCRIPTION RECOMMENDED SOLUTIONS
SOLUTIONS
Identify and stop endpoint breaches automatically in real-time while reducing the
Endpoint Detection & Response overhead of false alarms and supporting the security teams with forensic analysis and FortiEDR FortiClient
investigation without disrupting business operations.
Keep up with the volume, sophistication, and speed of today’s cyberthreats, using
FortiAnalyzer
security operations that can function at machine speed, providing advanced threat
Logging, Monitoring and Reporting FortiManager FortiGuard Services
detection and response capabilities, centralized security monitoring, and automation
FortiSIEM
across the entire Fortinet Security Fabric.
Enable automation-driven centralized management of Fortinet solutions from a single
console, supporting visibility and administration of network devices through unified
Network Operations Center FortiManager FortiAnalyzer
dashboards, streamlined provisioning for software updates, and automation tools for
troubleshooting network issues.
Security orchestration, automation and response (SOAR) providing management,
FortiAnalyzer
Security Automation and Orchestration automation, and orchestration across the entire security infrastructure to reduce the FortiSOAR
FortiSIEM
mean time to respond to security issues and incidents.
Enable unified data collection and analytics from diverse information sources including
Security Operations Center FortiSIEM FortiSOAR
logs, performance metrics, SNMP, security alerts, and configuration changes.
Detect & Protect
USE CASES DESCRIPTION RECOMMENDED SOLUTIONS OPTIONAL SOLUTIONS
FortiSandbox
Detect and stop zero-day threats and intrusions using a combination of proactive
FortiDeceptor FortiGate
Advanced Threat Protection detection and mitigation tools with actionable threat insight and integrated
FortiGuard Services FortiNDR
deployment architecture.
FortiRecon
Fortinet soltuions include hundreds of pre-built, ready-to-use reports and enables
easy-to-schedule delivery of reports. The report builder comes with 400+ charts
FortiGate
and 35+ templates for report customization. Risk scoring and assessment provides
Analytics & Compliance FortiAnalyzer FortiManager
risk assessment across a variety of Fortinet practices, NIST, and CIS best practices.
FortiGuard Services
The Fortinet Security Rating Service can also be used to compare against
specific industries.
Automatically discover and identify devices, support asset visibility for enforcing
appropriate security policies, including virtual patching. Furthermore, the Security FortiGate
Device Detection Service FortiManager
Rating Service assists in establishing and maintaining an optimal security posture by FortiGuard Services
detecting vulnerabilities and configuration issues through audit checks.
Monitor, detect, and protect against network-level threats targeting OT
FortiGate
OT Security Service environments, support virtual patching, and provide extensive visibility into OT FortiManager
FortiGuard Services
applications and protocols.
Virtual Patching or Vulnerability Shielding acts as a compensating security control
against threats that have the potential to exploit known or unknown vulnerabilities.
Virtual patching works by implementing layers of security controls that intercept
and prevent an exploit from compromising the vulnerable assets connected on
the network(s). OT-specific IPS signatures can provide a virtual patch to the FortiGate
Virtual Patching FortiManager
environment so that unpatched systems can continue to operate within the OT FortiGuard Services
network with minimized risk of exploitation. A security team can wait until the
next scheduled outage to apply an underlying patch or continue to operate the
vulnerable OT systems with a virtual patch in place in case no security fix is
available for it.
4


**Table 4.1**

| USE CASES | DESCRIPTION | RECOMMENDED SOLUTIONS | OPTIONAL SOLUTIONS |
| --- | --- | --- | --- |
| Endpoint Detection & Response | Identify and stop endpoint breaches automatically in real-time while reducing the overhead of false alarms and supporting the security teams with forensic analysis and investigation without disrupting business operations. | FortiEDR | FortiClient |
| Logging, Monitoring and Reporting | Keep up with the volume, sophistication, and speed of today’s cyberthreats, using security operations that can function at machine speed, providing advanced threat detection and response capabilities, centralized security monitoring, and automation across the entire Fortinet Security Fabric. | FortiAnalyzer FortiManager FortiSIEM | FortiGuard Services |
| Network Operations Center | Enable automation-driven centralized management of Fortinet solutions from a single console, supporting visibility and administration of network devices through unified dashboards, streamlined provisioning for software updates, and automation tools for troubleshooting network issues. | FortiManager | FortiAnalyzer |
| Security Automation and Orchestration | Security orchestration, automation and response (SOAR) providing management, automation, and orchestration across the entire security infrastructure to reduce the mean time to respond to security issues and incidents. | FortiSOAR | FortiAnalyzer FortiSIEM |
| Security Operations Center | Enable unified data collection and analytics from diverse information sources including logs, performance metrics, SNMP, security alerts, and configuration changes. | FortiSIEM | FortiSOAR |


**Table 4.2**

|  | Detect & Protect |  |  |  |
| --- | --- | --- | --- | --- |
| USE CASES |  | DESCRIPTION | RECOMMENDED SOLUTIONS | OPTIONAL SOLUTIONS |
| Advanced Threat Protection |  | Detect and stop zero-day threats and intrusions using a combination of proactive detection and mitigation tools with actionable threat insight and integrated deployment architecture. | FortiSandbox FortiDeceptor FortiGuard Services FortiRecon | FortiGate FortiNDR |
| Analytics & Compliance |  | Fortinet soltuions include hundreds of pre-built, ready-to-use reports and enables easy-to-schedule delivery of reports. The report builder comes with 400+ charts and 35+ templates for report customization. Risk scoring and assessment provides risk assessment across a variety of Fortinet practices, NIST, and CIS best practices. The Fortinet Security Rating Service can also be used to compare against specific industries. | FortiGate FortiAnalyzer FortiGuard Services | FortiManager |
| Device Detection Service |  | Automatically discover and identify devices, support asset visibility for enforcing appropriate security policies, including virtual patching. Furthermore, the Security Rating Service assists in establishing and maintaining an optimal security posture by detecting vulnerabilities and configuration issues through audit checks. | FortiGate FortiGuard Services | FortiManager |
| OT Security Service |  | Monitor, detect, and protect against network-level threats targeting OT environments, support virtual patching, and provide extensive visibility into OT applications and protocols. | FortiGate FortiGuard Services | FortiManager |
| Virtual Patching |  | Virtual Patching or Vulnerability Shielding acts as a compensating security control against threats that have the potential to exploit known or unknown vulnerabilities. Virtual patching works by implementing layers of security controls that intercept and prevent an exploit from compromising the vulnerable assets connected on the network(s). OT-specific IPS signatures can provide a virtual patch to the environment so that unpatched systems can continue to operate within the OT network with minimized risk of exploitation. A security team can wait until the next scheduled outage to apply an underlying patch or continue to operate the vulnerable OT systems with a virtual patch in place in case no security fix is available for it. | FortiGate FortiGuard Services | FortiManager |


**Table 4.3**

|  |  |
| --- | --- |

Operational Technology (OT) Ordering Guide
Product Offerings and Ordering Information
FortiGate is the flagship NGFW product family from Fortinet that delivers best-in-class security, high-speed networking,
hardware-accelerated performance features for NGFW/NGIPS, and built-in market-leading SD-WAN. FortiGate comes
in different form factors and sizes, including ruggedized appliances to withstand harsh environmental conditions and
support industrial applications.
FortiGuard provides security services that keep FortiGate products up-to-date with the latest security updates
and threat intelligence. FortiGuard security services are offered through subscription bundles and include several
advanced threat protection services for enterprise networks, web, cloud, OT, and so on. The OT Security Service is
part of the FortiGuard subscription offering.
ENTERPRISE RENEWAL
FORTIGATE BASE PRODUCT ENTERPRISE HARDWARE BUNDLE OT SECURITY SERVICE
BUNDLE
FGR-50G-5G FGR-50G-5G FGR-50G-5G-BDL-809-DD FC-10-FR5G5-809-02-DD FC-10-FR5G5-159-02-DD
FGR-60F FGR-60F FGR-60F-BDL-809-DD FC-10-0069F-809-02-DD FC-10-0069F-159-02-DD
FGR-60F-3G4G FGR-60F-3G4G FGR-60F-3G4G-BDL-809-DD FC-10-F60FI-809-02-DD FC-10-F60FI-159-02-DD
FGR-60G FGR-60G FGR-60G-BDL-809-DD FC-10-GR60G-809-02-DD FC-10-GR60G-159-02-DD
FGR-60G-5G FGR-60G-5G FGR-60G-5G-BDL-809-DD FC-10-R60G5-809-02-DD FC-10-R60G5-159-02-DD
FGR-60G-M12 FGR-60G-M12 FGR-60G-M12-BDL-809-DD FC-10-R60GM-809-02-DD FC-10-R60GM-159-02-DD
FGR-70F FGR-70F FGR-70F-BDL-809-DD FC-10-F70FB-809-02-DD FC-10-F70FB-159-02-DD
FGR-70G FGR-70G FGR-70G-BDL-809-DD FC-10-GR70P-809-02-DD FC-10-GR70P-159-02-DD
FGR-70F-3G4G FGR-70F-3G4G FGR-70F-3G4G-BDL-809-DD FC-10-F70FM-809-02-DD FC-10-F70FM-159-02-DD
FGR-70G-5G FGR-70G-5G FGR-70G-5G-BDL-809-DD FC-10-R70GM-809-02-DD FC-10-R70GM-159-02-DD
FGR-70G-5G-DUAL FGR-70G-5G-DUAL FGR-70G-5G-DUAL-BDL-809-DD FC-10-F70G5-809-02-DD FC-10-F70G5-159-02-DD
FG-40F-3G4G FG-40F-3G4G FG-40F-3G4G-BDL-809-DD FC-10-F40FG-809-02-DD FC-10-F40FG-159-02-DD
FG-100F FG-100F FG-100F-BDL-809-DD FC-10-F100F-809-02-DD FC-10-F100F-159-02-DD
FG-120G FG-120G FG-120G-BDL-809-DD FC-10-F120G-809-02-DD FC-10-F120G-159-02-DD
FG-200G FG-200G FG-200G-BDL-809-DD FC-10-FG2HG-809-02-DD FC-10-FG2HG-159-02-DD
FG-1000F FG-1000F FG-1000F-BDL-809-DD FG-1000F-BDL-809-DD FC-10-F1K0F-159-02-DD
FG-1800F FG-1800F FG-1800F-BDL-809-DD FC-10-F18HF-809-02-DD FC-10-F18HF-159-02-DD
FG-VM FG-VM02 - FC-10-FVM02-812-02-DD FC-10-FVM02-159-02-DD
FortiSwitch is a secure access switch family that delivers outstanding performance, scalability, and manageability.
FortiSwitch allows OT customers to extend networking and security across their network infrastructure. FortiSwitch
seamlessly integrates with the Security Fabric via FortiLink. FortiCloud or FortiGate can manage FortiSwitch. The unified
management of FortiSwitch via FortiGate offers complete visibility and control of users and devices in the network.
FORTISWITCH BASE PRODUCT SUPPORT
FSR-108F FSR-108F FC-10-S08FN-247-02-DD
FSR-112F-POE FSR-112F-POE FC-10-SR2FP-247-02-DD
FSR-216F-POE FSR-216F-POE FC-10-SR16F-247-02-DD
FSR-424F-POE FSR-424F-POE FC-10-R24FP-247-02-DD
FS-110G-FPOE FS-110G-FPOE FC-10-M10GF-247-02-D
FS-448E-FPOE FS-448E-FPOE FC-10-S448F-247-02-DD
FS-548D-FPOE FS-548D-FPOE FC-10-W0501-247-02-DD
FS-648F-FPOE FS-648F-FPOE FC-10-648FF-247-02-DD
FS-1048E FS-1048E FC-10-1E48F-247-02-DD
FS-1048G FS-1048G FC-10-FSG48-247-02-DD
5


**Table 5.1**

|  |  |
| --- | --- |
|  |  |


**Table 5.2**

| FORTIGATE | BASE PRODUCT | ENTERPRISE HARDWARE BUNDLE | ENTERPRISE RENEWAL BUNDLE | OT SECURITY SERVICE |
| --- | --- | --- | --- | --- |
| FGR-50G-5G | FGR-50G-5G | FGR-50G-5G-BDL-809-DD | FC-10-FR5G5-809-02-DD | FC-10-FR5G5-159-02-DD |
| FGR-60F | FGR-60F | FGR-60F-BDL-809-DD | FC-10-0069F-809-02-DD | FC-10-0069F-159-02-DD |
| FGR-60F-3G4G | FGR-60F-3G4G | FGR-60F-3G4G-BDL-809-DD | FC-10-F60FI-809-02-DD | FC-10-F60FI-159-02-DD |
| FGR-60G | FGR-60G | FGR-60G-BDL-809-DD | FC-10-GR60G-809-02-DD | FC-10-GR60G-159-02-DD |
| FGR-60G-5G | FGR-60G-5G | FGR-60G-5G-BDL-809-DD | FC-10-R60G5-809-02-DD | FC-10-R60G5-159-02-DD |
| FGR-60G-M12 | FGR-60G-M12 | FGR-60G-M12-BDL-809-DD | FC-10-R60GM-809-02-DD | FC-10-R60GM-159-02-DD |
| FGR-70F | FGR-70F | FGR-70F-BDL-809-DD | FC-10-F70FB-809-02-DD | FC-10-F70FB-159-02-DD |
| FGR-70G | FGR-70G | FGR-70G-BDL-809-DD | FC-10-GR70P-809-02-DD | FC-10-GR70P-159-02-DD |
| FGR-70F-3G4G | FGR-70F-3G4G | FGR-70F-3G4G-BDL-809-DD | FC-10-F70FM-809-02-DD | FC-10-F70FM-159-02-DD |
| FGR-70G-5G | FGR-70G-5G | FGR-70G-5G-BDL-809-DD | FC-10-R70GM-809-02-DD | FC-10-R70GM-159-02-DD |
| FGR-70G-5G-DUAL | FGR-70G-5G-DUAL | FGR-70G-5G-DUAL-BDL-809-DD | FC-10-F70G5-809-02-DD | FC-10-F70G5-159-02-DD |
| FG-40F-3G4G | FG-40F-3G4G | FG-40F-3G4G-BDL-809-DD | FC-10-F40FG-809-02-DD | FC-10-F40FG-159-02-DD |
| FG-100F | FG-100F | FG-100F-BDL-809-DD | FC-10-F100F-809-02-DD | FC-10-F100F-159-02-DD |
| FG-120G | FG-120G | FG-120G-BDL-809-DD | FC-10-F120G-809-02-DD | FC-10-F120G-159-02-DD |
| FG-200G | FG-200G | FG-200G-BDL-809-DD | FC-10-FG2HG-809-02-DD | FC-10-FG2HG-159-02-DD |
| FG-1000F | FG-1000F | FG-1000F-BDL-809-DD | FG-1000F-BDL-809-DD | FC-10-F1K0F-159-02-DD |
| FG-1800F | FG-1800F | FG-1800F-BDL-809-DD | FC-10-F18HF-809-02-DD | FC-10-F18HF-159-02-DD |
| FG-VM | FG-VM02 | - | FC-10-FVM02-812-02-DD | FC-10-FVM02-159-02-DD |


**Table 5.3**

| FORTISWITCH | BASE PRODUCT | SUPPORT |
| --- | --- | --- |
| FSR-108F | FSR-108F | FC-10-S08FN-247-02-DD |
| FSR-112F-POE | FSR-112F-POE | FC-10-SR2FP-247-02-DD |
| FSR-216F-POE | FSR-216F-POE | FC-10-SR16F-247-02-DD |
| FSR-424F-POE | FSR-424F-POE | FC-10-R24FP-247-02-DD |
| FS-110G-FPOE | FS-110G-FPOE | FC-10-M10GF-247-02-D |
| FS-448E-FPOE | FS-448E-FPOE | FC-10-S448F-247-02-DD |
| FS-548D-FPOE | FS-548D-FPOE | FC-10-W0501-247-02-DD |
| FS-648F-FPOE | FS-648F-FPOE | FC-10-648FF-247-02-DD |
| FS-1048E | FS-1048E | FC-10-1E48F-247-02-DD |
| FS-1048G | FS-1048G | FC-10-FSG48-247-02-DD |

Operational Technology (OT) Ordering Guide
Product Offerings and Ordering Information
FortiAP is a series of secure Wi-Fi access points managed through FortiManagement Cloud or FortiGate.
FortiAPs provide high throughput, optimal coverage, and enterprise-class Wi-Fi 6E and Wi-Fi 7 connectivity.
FortiAPs integrate seamlessly with the Security Fabric and enable security and access-control policy enforcement
for end users as devices attempt to access the network.
FORTIAP BASE PRODUCT SUPPORT
FAP-222KL FAP-222KL-X* FC-10-F22KL-247-02-DD
FAP-231K FAP-231K-X* FC-10-P231K-247-02-DD
FAP-234G FAP-234G-X* FC-10-P234G-247-02-DD
FAP-241K FAP-241K-X* FC-10-P241K-247-02-DD
FAP-244K FAP-244K-X* FC-10-F244K-247-02-DD
FAP-432FR FAP-432FR-X* FC-10-F432FR-247-02-DD
FAP-432G FAP-432G-X* FC-10-P432G-247-02-DD
FAP-441K FAP-441K-X* FC-10-FP41K-247-02-DD
* Replace X with the country code.
FortiExtender provides a bridge between local Ethernet LANs and wireless LTE/5G WAN connections. FortiExtender
can support diverse wireless applications with a high level of backhaul redundancy using a single LTE/5G modem
platform over redundant SIM cards attaching to different mobile networks. You can use FortiExtender as the LTE/5G
backhaul of an on-premise FortiGate with maximum wireless LTE/5G signal strength. FortiGate can centrally
manage FortiExtender.
FORTIEXTENDER BASE PRODUCT SUPPORT
FEX-101G FEX-101G-X* FC-10-X101G-247-02-DD
FER-511G FER-511G-X* FC-10-XR51G-247-02-DD
FEV-211F FEV-211F-X* FC-10-FG21F-247-02-DD
FEV-211F-AM FEV-211F-AM FC-10-FV21F-247-02-DD
FEV-212F FEV-212F-X* FC-10-FG22F-247-02-DD
FEV-212F-AM FEV-212F-AM FC-10-FV22F-247-02-DD
FEV-511G FEV-511G-X* FC-10-FV51G-247-02-DD
FEX-200F FEX-200F FC-10-X200F-247-02-DD
FEX-211G FEX-211G-X* FC-10-X211G-247-02-DD
FEX-311F FEX-311F FC-10-X311F-247-02-DD
FEX-511F FEX-511F FC-10-X511F-247-02-DD
FEX-511G FEX-511G-X* FC-10-FX51G-247-02-DD
FEX-511G-WIFI FEX-511G-WIFI-X* FC-10-XW51G-247-02-DD
* Replace X with the country code.
6


**Table 6.1**

| FORTIAP | BASE PRODUCT | SUPPORT |
| --- | --- | --- |
| FAP-222KL | FAP-222KL-X* | FC-10-F22KL-247-02-DD |
| FAP-231K | FAP-231K-X* | FC-10-P231K-247-02-DD |
| FAP-234G | FAP-234G-X* | FC-10-P234G-247-02-DD |
| FAP-241K | FAP-241K-X* | FC-10-P241K-247-02-DD |
| FAP-244K | FAP-244K-X* | FC-10-F244K-247-02-DD |
| FAP-432FR | FAP-432FR-X* | FC-10-F432FR-247-02-DD |
| FAP-432G | FAP-432G-X* | FC-10-P432G-247-02-DD |
| FAP-441K | FAP-441K-X* | FC-10-FP41K-247-02-DD |


**Table 6.2**

| FORTIEXTENDER | BASE PRODUCT | SUPPORT |
| --- | --- | --- |
| FEX-101G | FEX-101G-X* | FC-10-X101G-247-02-DD |
| FER-511G | FER-511G-X* | FC-10-XR51G-247-02-DD |
| FEV-211F | FEV-211F-X* | FC-10-FG21F-247-02-DD |
| FEV-211F-AM | FEV-211F-AM | FC-10-FV21F-247-02-DD |
| FEV-212F | FEV-212F-X* | FC-10-FG22F-247-02-DD |
| FEV-212F-AM | FEV-212F-AM | FC-10-FV22F-247-02-DD |
| FEV-511G | FEV-511G-X* | FC-10-FV51G-247-02-DD |
| FEX-200F | FEX-200F | FC-10-X200F-247-02-DD |
| FEX-211G | FEX-211G-X* | FC-10-X211G-247-02-DD |
| FEX-311F | FEX-311F | FC-10-X311F-247-02-DD |
| FEX-511F | FEX-511F | FC-10-X511F-247-02-DD |
| FEX-511G | FEX-511G-X* | FC-10-FX51G-247-02-DD |
| FEX-511G-WIFI | FEX-511G-WIFI-X* | FC-10-XW51G-247-02-DD |

Operational Technology (OT) Ordering Guide
Product Offerings and Ordering Information
FortiManager provides automation-driven centralized management. FortiManager allows end users to
centrally manage FortiGate, FortiSwitch, and FortiAP devices in their network with a single-console centralized
management platform.
VM SUBSCRIPTION LICENSE WITH
FORTIMANAGER BASE PRODUCT HW SUPPORT
SUPPORT
FMG-200G FMG-200G FC-10-M200G-247-02-DD
FMG-410G FMG-410G FC-10-FM41G-247-02-DD
FMG-1000G FMG-1000G FC-10-FM1KG-247-02-DD
FMG-VM FC2-10-FMGVS-258-01-DD
FortiNAC offers network access control that enhances the Security Fabric with visibility, control, and automated
response for everything that connects to the network. FortiNAC provides protection against malicious access,
extends access control to third-party devices, offers greater visibility for devices, supports dynamic network access
control, and orchestrates automatic responses to a wide range of networking events.
PLUS LICENSE
PLUS LICENSE PERPETUAL
FORTINAC BASE PRODUCT SUPPORT SUBSCRIPTION
1000 ENDPOINTS
500 ENDPOINTS*
FNC-CA-VM FNC-CAX-VM FC-10-FNVXA-248-02-DD LIC-FNAC-PLUS-1K FC5-10-FNAC1-213-01-DD
FNC-CA-700F FNC-CA-700F FC-10-NF700-247-02-DD LIC-FNAC-PLUS-1K FC5-10-FNAC1-213-01-DD
* Minimum order quantity 500
7


**Table 7.1**

| FORTIMANAGER | BASE PRODUCT | VM SUBSCRIPTION LICENSE WITH SUPPORT | HW SUPPORT |
| --- | --- | --- | --- |
| FMG-200G | FMG-200G |  | FC-10-M200G-247-02-DD |
| FMG-410G | FMG-410G |  | FC-10-FM41G-247-02-DD |
| FMG-1000G | FMG-1000G |  | FC-10-FM1KG-247-02-DD |
| FMG-VM |  | FC2-10-FMGVS-258-01-DD |  |


**Table 7.2**

| FORTINAC | BASE PRODUCT | SUPPORT | PLUS LICENSE PERPETUAL 1000 ENDPOINTS | PLUS LICENSE SUBSCRIPTION 500 ENDPOINTS* |
| --- | --- | --- | --- | --- |
| FNC-CA-VM | FNC-CAX-VM | FC-10-FNVXA-248-02-DD | LIC-FNAC-PLUS-1K | FC5-10-FNAC1-213-01-DD |
| FNC-CA-700F | FNC-CA-700F | FC-10-NF700-247-02-DD | LIC-FNAC-PLUS-1K | FC5-10-FNAC1-213-01-DD |


**Table 7.3**

|  |  |
| --- | --- |

Operational Technology (OT) Ordering Guide
Product Offerings and Ordering Information
FortiClient includes the ZTNA, SASE, and EPP capabilities:
• ZTNA enables remote users to access their corporate applications while ensuring strict authentication
and verifiable endpoint security posture before any access is granted.
• SASE ensures remote users can securely connect to the corporate following the same corporate security
policies regardless of their location. SASE integrates seamlessly with ZTNA to deliver a transparent user
experience while offering security protection for all endpoints from advanced threats.
• EPP offers vulnerability detection and protection, auto-patching AV, application firewall, antiransomware,
and endpoint management.
FORTICLIENT 25-PACK (ADD-ON) 500-PACK (ADD-ON) 2000-PACK (ADD-ON)
EPP/ATP (On-premises) FC1-10-EMS04-429-01-DD FC2-10-EMS04-429-01-DD FC3-10-EMS04-429-01-DD
EPP/ATP (Cloud) FC1-10-EMS05-429-01-DD FC2-10-EMS05-429-01-DD FC3-10-EMS05-429-01-DD
EPP/ATP Managed FC1-10-EMS05-485-01-DD FC2-10-EMS05-485-01-DD FC3-10-EMS05-485-01-DD
FortiSASE integrates networking and security for secure access and connectivity anywhere. It ensures enterprise-
grade security and user experience across physical and virtual networks, addressing the limitations of many cloud-
delivered solutions for hybrid IT/OT environments. FortiSASE extends FortiGuard services to remote users, edge
computing environments, and cloud deployments delivering consistent security posture.
FORTISASE SUBSCRIPTION
FortiSASE User Subscription - 50 to 499 Users FC2-10-EMS05-547-02-DD
FortiSASE User Subscription - 500 to 1999 Users FC3-10-EMS05-547-02-DD
FortiWeb offers security protection for business-critical web applications and APIs from attacks that target known
and unknown vulnerabilities. Using an advanced multilayered approach backed by a sophisticated machine learning
engine, FortiWeb protects against the OWASP Top 10 and more. The FortiWeb product line offers solutions and
deployment options across SaaS, VMs, and hardware appliances.
FORTIWEB BASE PRODUCT ADVANCED HARDWARE BUNDLE ADVANCED BUNDLE RENEWAL
FWB-1000F FWB-1000F FWB-1000F-BDL-580-DD FC-10-FV1KF-580-02-DD
FWB-4000F FWB-4000F FWB-4000F-BDL-580-DD FC-10-FW4KF-580-02-DD
FWB-VM08 FWB-VM08 - FC-10-VVM08-581-02-DD
8


**Table 8.1**

| FORTICLIENT | 25-PACK (ADD-ON) | 500-PACK (ADD-ON) | 2000-PACK (ADD-ON) |
| --- | --- | --- | --- |
| EPP/ATP (On-premises) | FC1-10-EMS04-429-01-DD | FC2-10-EMS04-429-01-DD | FC3-10-EMS04-429-01-DD |
| EPP/ATP (Cloud) | FC1-10-EMS05-429-01-DD | FC2-10-EMS05-429-01-DD | FC3-10-EMS05-429-01-DD |
| EPP/ATP Managed | FC1-10-EMS05-485-01-DD | FC2-10-EMS05-485-01-DD | FC3-10-EMS05-485-01-DD |


**Table 8.2**

| FORTISASE | SUBSCRIPTION |
| --- | --- |
| FortiSASE User Subscription - 50 to 499 Users | FC2-10-EMS05-547-02-DD |
| FortiSASE User Subscription - 500 to 1999 Users | FC3-10-EMS05-547-02-DD |


**Table 8.3**

| FORTIWEB | BASE PRODUCT | ADVANCED HARDWARE BUNDLE | ADVANCED BUNDLE RENEWAL |
| --- | --- | --- | --- |
| FWB-1000F | FWB-1000F | FWB-1000F-BDL-580-DD | FC-10-FV1KF-580-02-DD |
| FWB-4000F | FWB-4000F | FWB-4000F-BDL-580-DD | FC-10-FW4KF-580-02-DD |
| FWB-VM08 | FWB-VM08 | - | FC-10-VVM08-581-02-DD |


**Table 8.4**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

Operational Technology (OT) Ordering Guide
Product Offerings and Ordering Information
FortiToken enables two-factor authentication with One-Time Password (OTP) Application with Push Notifications
or a Hardware Time-Based OTP Token. FortiToken Mobile (FTM) and hardware OTP Tokens are fully integrated with
FortiClient, secured by FortiGuard, and leverage direct management and use within the FortiGate and FortiAuthenticator
security solutions. FortiGate, FortiToken, and FortiAuthenticator integrated solution is easy to implement, use, and manage
for multi-factor authentication use case.
FORTITOKEN BASE PRODUCT
FTM-ELIC FTM-ELIC-XX *
FTK-210 FTK-210-XX*
* Replace XX with the number of tokens.
FortiAnalyzer offers a centralized log management, analytics, and reporting platform, providing customers with
single-pane orchestration, automation, and response for simplified security operations, proactive identification, risk
remediation, and complete visibility of the entire attack surface. FortiAnalyzer can collect different types of logs and
events from Fortinet products via Security Fabric integration.
FORTIANALYZER BASE PRODUCT HW/VM BUNDLE OT SECURITY SERVICE SUPPORT
FAZ-300G FAZ-300G FAZ-300G-BDL-466-DD FC-10-L03HG-159-02-DD FC-10-L03HG-466-02-DD
FAZ-1000G FAZ-1000G FAZ-1000G-BDL-466-DD FC-10-AZ1KG-159-02-DD FC-10-AZ1KG-466-02-DD
FAZ-3100G FAZ-3100G FAZ-3100G-BDL-466-DD FC-10-AZ31G-159-02-DD FC-10-AZ31G-466-02-DD
FAZ-VM - FC1-10-AZVMS-465-01-DD FC1-10-LV0VM-159-02-DD -
FortiSIEM provides unified event correlation and risk management for multivendor implementations. It enables analytics
from diverse information sources including logs, performance metrics, SNMP traps, security alerts, and configuration
changes. It feeds all the information into an event-based analytics engine and supports real-time searches, rules,
dashboards, and ad hoc queries.
FORTISIEM BASE PRODUCT SUPPORT
FSM-2200G FC-10-FM22G-247-02-DD
FSM-2200G
FSM-AIO-2200-BASE FC[2-Y]-10-FSM99-240-02-DD
FSM-AIO-BASE FSM-AIO-BASE FC-10-FM22G-247-02-DD
FSM-AIO-UG FSM-AIO-XX-UG* Included with FC[1-Y]-10-FSM97-248-02-DD and FC[2-Y]-10-FSM99-240-02-DD
FSM-EPD-UPG FSM-EPD-XX-UG* –
* Replace XX with the number of devices.
FortiSOAR offers a holistic security orchestration, automation, and response workbench designed for SOC teams
to efficiently respond to the ever-increasing influx of alerts, repetitive manual processes, and resource shortages.
Its patented and customizable security operations platform provides automated playbooks and incident triaging,
and real-time remediation for enterprises to identify, defend, and counter attacks. FortiSOAR optimizes SOC team
productivity by seamlessly integrating with over 300+ security platforms and 3000+ actions. This results in faster
responses, streamlined containment, and reduces mitigation times from hours to seconds.
FORTISOAR BASE PRODUCT +1 ANALYST ADD-ON
FortiSOAR Starter Edition FC-10-SRVMS-1023-02-DD –
Multi Tenant Edition FC-10-SRVMS-390-02-DD FC-10-SRVMS-384-02-DD
9


**Table 9.1**

| FORTITOKEN | BASE PRODUCT |
| --- | --- |
| FTM-ELIC | FTM-ELIC-XX * |
| FTK-210 | FTK-210-XX* |


**Table 9.2**

| FORTIANALYZER | BASE PRODUCT | HW/VM BUNDLE | OT SECURITY SERVICE | SUPPORT |
| --- | --- | --- | --- | --- |
| FAZ-300G | FAZ-300G | FAZ-300G-BDL-466-DD | FC-10-L03HG-159-02-DD | FC-10-L03HG-466-02-DD |
| FAZ-1000G | FAZ-1000G | FAZ-1000G-BDL-466-DD | FC-10-AZ1KG-159-02-DD | FC-10-AZ1KG-466-02-DD |
| FAZ-3100G | FAZ-3100G | FAZ-3100G-BDL-466-DD | FC-10-AZ31G-159-02-DD | FC-10-AZ31G-466-02-DD |
| FAZ-VM | - | FC1-10-AZVMS-465-01-DD | FC1-10-LV0VM-159-02-DD | - |


**Table 9.3**

| FORTISIEM | BASE PRODUCT | SUPPORT |
| --- | --- | --- |
| FSM-2200G | FSM-2200G FSM-AIO-2200-BASE | FC-10-FM22G-247-02-DD FC[2-Y]-10-FSM99-240-02-DD |
| FSM-AIO-BASE | FSM-AIO-BASE | FC-10-FM22G-247-02-DD |
| FSM-AIO-UG | FSM-AIO-XX-UG* | Included with FC[1-Y]-10-FSM97-248-02-DD and FC[2-Y]-10-FSM99-240-02-DD |
| FSM-EPD-UPG | FSM-EPD-XX-UG* | – |


**Table 9.4**

| FORTISOAR | BASE PRODUCT | +1 ANALYST ADD-ON |
| --- | --- | --- |
| FortiSOAR Starter Edition | FC-10-SRVMS-1023-02-DD | – |
| Multi Tenant Edition | FC-10-SRVMS-390-02-DD | FC-10-SRVMS-384-02-DD |

Operational Technology (OT) Ordering Guide
Product Offerings and Ordering Information
FortiSandbox provides a top-rated AI-powered breach protection that integrates with the Security Fabric platform to
address the rapidly evolving and targeted threats, including ransomware, cryptomalware, and others across a broad
digital attack surface. Specifically for OT, it delivers real-time actionable intelligence through automating zero-day
advanced malware detection and response for detecting threats targeting OT systems and protocols.
FORTISANDBOX BASE PRODUCT UPGRADE THREAT INTELLIGENCE AND SUPPORT
FSA-500G FSA-500G FSA-500G-UPG-LIC-BYOL FC-10-FS5HG-499-02-DD
FSA-3000G FSA-3000G FC1-10-SA3KG-1035-02-DD FC-10-SA3KG-499-02-DD
FSA-VM - FC1-10-SAVMS-1146-02-DD FC1-10-SAVMS-1035-02-DD
FortiDeceptor offers honeypot and deception technology to deceive, expose, and eliminate external and internal
threats early in the attack kill chain and it proactively blocks these threats before any significant damage occurs. It
automates blocking of the attackers targeting IT and OT systems and devices by laying out a layer of decoys and
lures that helps with redirecting attackers focus while revealing their presence on the network.
ADD 1 VLAN CENTRAL
FORTIDECEPTOR BASE PRODUCT SUPPORT WINDOWS DECOYS
SUBSCRIPTION * MANAGEMENT
FDR-100G FDR-100G FC-10-DR1HG-247-02-DD FC1-10-DR1HG-495-02-DD FC1-10-FDCCM-497-02-DD LIC-FDC-WIN
FDC-1000G FDC-1000G FC-10-DC1KG-247-02-DD FC1-10-DC1KG-495-02-DD FC1-10-FDCCM-497-02-DD LIC-FDC-WIN
FDC-VMS Subscription Included with subscription FC1-10-DCVMS-496-02-DD FC1-10-FDCCM-497-02-DD LIC-FDC-WIN
FDC-as-a-Service Subscription Included with subscription FC1-10-DCDAS-496-02-DD FC1-10-FDCCM-497-02-DD LIC-FDC-WIN
* Minimum order of two VLANs.
FortiEDR delivers real-time automated endpoint protection with orchestrated incident response across IT and OT
endpoints. All in a single integrated platform, with flexible deployment options, and a predictable operating cost,
FortiEDR provides real-time proactive risk mitigation, endpoint security, preinfection protection via a kernel-level next
generation antivirus (NGAV) engine, postinfection protection, and forensics.
BEST PRACTICES SERVICE
FORTIEDR FORTIEDR DISCOVER, PROTECT & RESPOND
FIRST-TIME DEPLOYMENT
25 endpoints * FC1-10-FEDR1-348-01-DD * FC1-10-EDBPS-310-02-DD
500 endpoints FC2-10-FEDR1-348-01-DD FC1-10-EDBPS-310-02-DD
2000 endpoints FC3-10-FEDR1-348-01-DD FC2-10-EDBPS-310-02-DD
* Add-on option. Minimum Order Quantity (MOQ) 500 seats.
FortiAuthenticator offers single sign-on and user authorization into the Fortinet secured enterprise network
identifying users, querying access permissions from third-party systems, and communicating the access requests
to FortiGate to implement identity-based security policies. FortiAuthenticator supports wide array of methods and
tools for authentication and authorization, such as Active Directory, RADIUS, LDAP, SAML SP/IdP, PKI, and
multi-factor authentication.
FORTIAUTHENTICATOR BASE PRODUCT SUPPORT
FAC-300F FAC-300F FC-10-AC3HF-247-02-DD
FAC-800F FAC-800F FC-10-AC8HF-247-02-DD
FAC-VM FAC-VM-BASE FC1-10-0ACVM-248-02-DD
10


**Table 10.1**

| FORTISANDBOX | BASE PRODUCT | UPGRADE | THREAT INTELLIGENCE AND SUPPORT |
| --- | --- | --- | --- |
| FSA-500G | FSA-500G | FSA-500G-UPG-LIC-BYOL | FC-10-FS5HG-499-02-DD |
| FSA-3000G | FSA-3000G | FC1-10-SA3KG-1035-02-DD | FC-10-SA3KG-499-02-DD |
| FSA-VM | - | FC1-10-SAVMS-1146-02-DD | FC1-10-SAVMS-1035-02-DD |


**Table 10.2**

| FORTIDECEPTOR | BASE PRODUCT | SUPPORT | ADD 1 VLAN SUBSCRIPTION * | CENTRAL MANAGEMENT | WINDOWS DECOYS |
| --- | --- | --- | --- | --- | --- |
| FDR-100G | FDR-100G | FC-10-DR1HG-247-02-DD | FC1-10-DR1HG-495-02-DD | FC1-10-FDCCM-497-02-DD | LIC-FDC-WIN |
| FDC-1000G | FDC-1000G | FC-10-DC1KG-247-02-DD | FC1-10-DC1KG-495-02-DD | FC1-10-FDCCM-497-02-DD | LIC-FDC-WIN |
| FDC-VMS | Subscription | Included with subscription | FC1-10-DCVMS-496-02-DD | FC1-10-FDCCM-497-02-DD | LIC-FDC-WIN |
| FDC-as-a-Service | Subscription | Included with subscription | FC1-10-DCDAS-496-02-DD | FC1-10-FDCCM-497-02-DD | LIC-FDC-WIN |


**Table 10.3**

|  |
| --- |
|  |


**Table 10.4**

| FORTIEDR | FORTIEDR DISCOVER, PROTECT & RESPOND | BEST PRACTICES SERVICE FIRST-TIME DEPLOYMENT |
| --- | --- | --- |
| 25 endpoints * | FC1-10-FEDR1-348-01-DD * | FC1-10-EDBPS-310-02-DD |
| 500 endpoints | FC2-10-FEDR1-348-01-DD | FC1-10-EDBPS-310-02-DD |
| 2000 endpoints | FC3-10-FEDR1-348-01-DD | FC2-10-EDBPS-310-02-DD |


**Table 10.5**

| FORTIAUTHENTICATOR | BASE PRODUCT | SUPPORT |
| --- | --- | --- |
| FAC-300F | FAC-300F | FC-10-AC3HF-247-02-DD |
| FAC-800F | FAC-800F | FC-10-AC8HF-247-02-DD |
| FAC-VM | FAC-VM-BASE | FC1-10-0ACVM-248-02-DD |


**Table 10.6**

|  |  |
| --- | --- |
|  |  |
|  |  |

Operational Technology (OT) Ordering Guide
Product Offerings and Ordering Information
FortiPAM is a robust privileged access and session management solution designed to secure critical assets across
both IT and OT environments. It combines secure remote access with advanced control over privileged accounts —
all within a unified, integrated solution. Whether supporting third-party contractors or remote employees, FortiPAM
ensures that access to sensitive systems is secure, monitored, and tightly controlled. Key features include session
monitoring and auditing, web-based antivirus scanning, and secure file exchange — all working together to reduce
cybersecurity risks from both internal and external users. With FortiPAM, organizations gain complete visibility and
control over privileged access, enhancing security, compliance, and operational resilience.
FORTIPAM SUBSCRIPTION
FortiPAM-VM - 5 to 9 users FC1-10-PAVUL-591-02-DD
FortiPAM-VM - 50 to 99 users FC4-10-PAVUL-591-02-DD
FortiPAM-VM - 250 or more users FC6-10-PAVUL-591-02-DD
FortiRecon scans the organization’s attack surface and identifies risks to assets. FortiGuard Threat intelligence
delivers early warning of risks to the organization through targeted, curated intelligence. It provides visibility into the
diverse threats to the organization and brand reputation, allowing customers to respond more quickly to incidents,
better understand attackers, and safeguard assets while expanding view and early warning of adversarial activity
from Dark Web and other sources.
FORTIRECON 500 ASSETS 1000 ASSETS 50000 ASSETS
FortiRecon EASM FC2-10-RNSVC-533-02-DD FC3-10-RNSVC-533-02-DD FC6-10-RNSVC-533-02-DD
FortiRecon EASM+BP+ACI FC2-10-RNSVC-535-02-DD FC3-10-RNSVC-535-02-DD FC6-10-RNSVC-535-02-DD
FortiNDR offers next-generation AI-driven breach protection technology to defend against various cyberthreats,
including advanced persistent threats through a trained Virtual Security AnalystTM. The virtual analyst helps with
identifying, classifying, and responding to threats including those well-camouflaged. Employing – patent-pending
– Deep Neural Networks based on Advanced AI and Artificial Neural Network, it provides sub-second security
investigation by harnessing deep learning technologies that assist in an automated response to remediate
different types of attacks.
APPLIANCE BUNDLE WITH NDR
FORTINDR BASE PRODUCT SUPPORT WITH NDR AND ANN NETFLOW AND OT SECURITY
AND ANN
FC3-10-AIVMS-588-02-DD - Netflow
FortiNDR-VM - FC3-10-AIVMS-461-02-DD -
FC3-10-AIVMS-723-02-DD - OT Security
FC-10-AI25G-588-02-DD - Netflow
FNR-2500G - FNR-2500G-BDL-331-DD -
FC-10-AI25G-723-02-DD - OT Security
Fortinet Accessories include several standard and rugged hardware accessories designed specifically for Fortinet products.
See the Additional Information and Resources section for more details.
11


**Table 11.1**

|  |
| --- |
|  |


**Table 11.2**

| FORTIPAM | SUBSCRIPTION |
| --- | --- |
| FortiPAM-VM - 5 to 9 users | FC1-10-PAVUL-591-02-DD |
| FortiPAM-VM - 50 to 99 users | FC4-10-PAVUL-591-02-DD |
| FortiPAM-VM - 250 or more users | FC6-10-PAVUL-591-02-DD |


**Table 11.3**

| FORTIRECON | 500 ASSETS | 1000 ASSETS | 50000 ASSETS |
| --- | --- | --- | --- |
| FortiRecon EASM | FC2-10-RNSVC-533-02-DD | FC3-10-RNSVC-533-02-DD | FC6-10-RNSVC-533-02-DD |
| FortiRecon EASM+BP+ACI | FC2-10-RNSVC-535-02-DD | FC3-10-RNSVC-535-02-DD | FC6-10-RNSVC-535-02-DD |


**Table 11.4**

| FORTINDR | BASE PRODUCT | APPLIANCE BUNDLE WITH NDR AND ANN | SUPPORT WITH NDR AND ANN | NETFLOW AND OT SECURITY |
| --- | --- | --- | --- | --- |
| FortiNDR-VM | - | FC3-10-AIVMS-461-02-DD | - | FC3-10-AIVMS-588-02-DD - Netflow FC3-10-AIVMS-723-02-DD - OT Security |
| FNR-2500G | - | FNR-2500G-BDL-331-DD | - | FC-10-AI25G-588-02-DD - Netflow FC-10-AI25G-723-02-DD - OT Security |

Operational Technology (OT) Ordering Guide
Typical Deployment of FortiGate NGFWs in IT/OT Networks
IT Information
Technology
FortiGate FortiSwitch FortiGuard
Services
Intranet Remote Site 1
Server Server
The Internet
Client Client
To Remote Site N
PLC RTU IED
Historian Historian Operator HMI
DMZ Network Process Network Control Network
Field Network
OT Operational
Technology
FortiGate FortiSwitch FortiGuard
Rugged Rugged Services
12


**Table 12.1**

| The Internet |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  | To Remote Site N |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table 12.2**

|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |


**Table 12.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |


**Table 12.4**

|  |  |
| --- | --- |
|  |  |


**Table 12.5**

|  |  |
| --- | --- |


**Table 12.6**

|  |  |
| --- | --- |


**Table 12.7**

|  |  |
| --- | --- |
|  |  |
|  |  |

Operational Technology (OT) Ordering Guide
FortiGuard OT Security Service Coverage – July 2026
OT Application Control Signatures
No arrow: Only application/protocol detection → One arrow: Application/protocol and message inspection
[N]: Number of IPS signatures available ⇒Double arrows: Application/protocol, message, and parameter inspection
Allen-Bradley CSP EtherCAT UDP [2] Modbus RTU [8] → Rockwell FactoryTalk Live Data
Allen-Bradley DF1 [46] → Ethernet POWERLINK [63] Modbus TCP/IP [118] ⇒ Rockwell FactoryTalk RNA Alarming
Allen-Bradley PCCC [12] → Ethernet POWERLINK UDP Moxa UDP Device Discovery Rockwell FactoryTalk RNA Server Ping
Aveva PI System EtherNet/IP [11] ⇒ MTConnect Rockwell FactoryTalk View Point
BACnet [130] → Ewon M2web Niagara Fox Rockwell FactoryTalk View SE
Beckhoff AMS [9] → Ewon Talk2M Access oBIX SafetyNET p RTFN CDC [1]
Bristol BSAP Ewon Talk2M VPN OCPP [125] → SafetyNET p RTFN CMS [6]
CC-Link IE Field Basic SLMP EMT [2] FactorySuite NMXSVC Omron FINS [59] → SafetyNET p RTFN MSC [6]
CC-Link IE Field Basic SLMP MT [2] FANUC FOCAS [33] → OPC AE [67] → SECS-II/GEM [240] →
CC-Link IE Field Basic SLMP ST [2] FL-NET [30] → OPC DA [110] → SEL Fast Messaging [33] →
CC-Link IE TSN [8] GE EGD [8] → OPC HDA [66] → Siemens Epoc EDM
CIP [129] GE SRTP [20] → OPC HDA Automation [11] → Siemens LOGO [6] →
Cisco CDP GOOSE OPC IOPCCommon [5] Siemens OCG ATCS [562] →
CN/IP CEA-852 [14] → HART-IP [29] → OPC IOPCEnumGUID [4] Siemens S7 [46] ⇒
CoAP [4] → IEC 60870-5-104 [86] ⇒ OPC IOPCServerList [3] Siemens S7 1200 [3] →
CODESYS [101] → IEC 60870-6 (ICCP/TASE.2) [41] → OPC IOPCServerList2 [3] Siemens S7 Plus [22] →
DDSI-RTPS IEC 61850 [44] → OPC IOPCShutdown Siemens SIMATIC CAMP [6]
Device Level Ring [10] → IEC 61850-90-5 R-GOOSE OPC UA [44] → STANAG 4406 Military Messaging [1]
Digi ADDP [8] → IEC 61850-90-5 R-SV OpenADR [28] STANAG 5066
Digi RealPort (Net C/X) IEC 62056 DLMS/COSEM [8] → OSIsoft Asset Framework SUS Ethernet IO Protocol [66]
Digi RealPort (Net C/X) DNP3 [37] ⇒ IEEE 1278.2 DIS [46] → Panasonic MEWTOCOL [22] → ToolsNet Open Protocol
Direct Message Profile [5] → IEEE C37.118 Synchrophasor [13] → Panasonic MEWTOCOL-DAT [4] TRDP [10] →
DNP3 [57] Inductive Automation Ignition PLANET Management Protocol Triconex TSAA [8] →
ECHONET Lite [138] → ISO 9506 MMS [85] → Profinet CBA [27] → TriStation [212] →
ECOM100 ITCM [21] → Profinet IO [4] → Unitronics PCOM [40] →
ELCOM 90 [9] → KNXnet/IP (EIBnet/IP) [15] → Profinet RT [18] → V2G EXI
Emerson DeltaV LonTalk IEC14908-1 CNP [4] → RaSTA [17] V2G SDP
Emerson ROC Matrikon OPC Tunneller Raymond iWarehouse Gateway Veeder-Root ATG
Ether-S-Bus [119] → Matter Protocol PBKDFParamRequest Rockwell Drive Peripheral Interface [7] Vnet/IP
Ether-S-I/O [3] → Mitsubishi MELSEC [41] → Rockwell FactoryTalk AssetCentre WITS0
EtherCAT [13] → Mitsubishi MESOFT Rockwell FactoryTalk Diagnostic WITSML [7] →
OT Vulnerability Protection Signatures
Advantech [108] Inductive Automation [15] Schneider Electric [87]
ABB [50] InduSoft [11] Siemens [32]
CODESYS [12] LAquis [6] Scada-LTS [11]
Delta Electronics [50] Moxa [31] Socomec [11]
DNP3 [6] mySCADA [9] Sierra Wireless [7]
Eaton [9] Mitsubishi [7] Voltronic [6]
Fuji [8] Omron [13] WECON [23]
Growatt [13] Planet Technologies [8]
GE [10] Rockwell [36]
For an up-to-date list of supported signatures, please visit https://www.fortiguard.com/services/ots.
Click here to submit a new signature request.
13


**Table 13.1**

|  |  |
| --- | --- |
|  |  |
|  |  |

Operational Technology (OT) Ordering Guide
Additional Information and Resources
PRODUCT DATASHEET
FortiGate https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/Fortinet_Product_Matrix.pdf
FortiGate Rugged https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiGate_Rugged_Series.pdf
FortiGate VM https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortigate-vm.pdf
FortiSwitch https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiSwitch_Secure_Access_Series.pdf
FortiAP https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortiap-series.pdf
FortiGuard https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiGuard_Security_Services.pdf
FortiExtender https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiExtender.pdf
FortiExtender Rugged https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortiextender-rugged.pdf
FortiAnalyzer https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortianalyzer.pdf
FortiManager https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortimanager.pdf
FortiSIEM https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiSIEM.pdf
FortiSOAR https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortisoar.pdf
FortiSandbox https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiSandbox.pdf
FortiDeceptor https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiDeceptor.pdf
FortiEDR https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortiedr.pdf
FortiClient https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/forticlient.pdf
FortiNAC https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortinac.pdf
FortiAuthenticator https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiAuthenticator.pdf
FortiToken https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortitoken.pdf
FortiPAM https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortipam.pdf
FortiRecon https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortirecon.pdf
FortiSASE https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortisase.pdf
FortiWeb https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiWeb.pdf
FortiNDR https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortindr.pdf
FortiAP Antennas: https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortinet-antennas.pdf
Fortinet Accessories FortiExtender Antennas: https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortiextender-accessories.pdf
Rugged Power Supply: https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/pdf/fortinet-rugged-accessories.pdf
Visit the OT Security Solutions Hub for additional technical information on Fortinet solutions for operational technology.
14


**Table 14.1**

| PRODUCT | DATASHEET |
| --- | --- |
| FortiGate | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/Fortinet_Product_Matrix.pdf |
| FortiGate Rugged | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiGate_Rugged_Series.pdf |
| FortiGate VM | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortigate-vm.pdf |
| FortiSwitch | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiSwitch_Secure_Access_Series.pdf |
| FortiAP | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortiap-series.pdf |
| FortiGuard | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiGuard_Security_Services.pdf |
| FortiExtender | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiExtender.pdf |
| FortiExtender Rugged | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortiextender-rugged.pdf |
| FortiAnalyzer | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortianalyzer.pdf |
| FortiManager | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortimanager.pdf |
| FortiSIEM | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiSIEM.pdf |
| FortiSOAR | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortisoar.pdf |
| FortiSandbox | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiSandbox.pdf |
| FortiDeceptor | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiDeceptor.pdf |
| FortiEDR | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortiedr.pdf |
| FortiClient | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/forticlient.pdf |
| FortiNAC | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortinac.pdf |
| FortiAuthenticator | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiAuthenticator.pdf |
| FortiToken | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortitoken.pdf |
| FortiPAM | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortipam.pdf |
| FortiRecon | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortirecon.pdf |
| FortiSASE | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortisase.pdf |
| FortiWeb | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiWeb.pdf |
| FortiNDR | https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortindr.pdf |
| Fortinet Accessories | FortiAP Antennas: https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortinet-antennas.pdf FortiExtender Antennas: https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortiextender-accessories.pdf Rugged Power Supply: https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/pdf/fortinet-rugged-accessories.pdf |


**Table 14.2**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

Operational Technology (OT) Ordering Guide
Frequently Asked Questions
Can FortiGuard OT Security Service be purchased without the Enterprise Protection subscription?
Yes. FortiGuard OT Security Service is not offered as part of the Enterprise Protection bundle and only as à la carte. However,
it is recommended to acquire it with Enterprise Protection or Advanced Threat Protection subscription as this approach
enables leveraging the full spectrum of threat protection capabilities and accessing other FortiGuard services when using
FortiGate hardware or VM appliance.
Where can I find the information about latest Application Control and IPS signatures available in the FortiGuard OT
Security Service? Where can I find the information about Attack Surface Security Service coverage?
The up-to-date information and latest release of Application Control and IPS signatures for FortiGuard OT Security
Service can be found on the FortiGuard website. The information about Attack Surface Security Service is available on
the FortiGuard website.
If the license on FortiGate hardware or VM appliance has expired, can the IPS signature database get signature updates?
No. Once the license on FortiGate hardware or VM appliance has expired, the appliance will not get any future updates for
the IPS signatures from the date of license expiry until the license is renewed. However, the IPS signatures existing in the
appliance’s database will still function while the license has expired although the database will not be up to date.
Does FortiGate rugged hardware appliances come with a power supply unit?
No. The FortiGate rugged hardware appliances are equipped with power input connectors only and the customers would be
required to purchase a suitable external power supply unit from third-party suppliers to power the appliances.
What license or subscription is required for running the OT decoys and lures in FortiDeceptor?
The “Deceptor Bundle Contract” subscription for FortiDeceptor includes the OT decoys and lures.
Why are some products listed as “Optional” in the use case to solution mapping in the Ordering Guide?
The “Optional” products can be integrated with the “Recommended” products and offer added value for the use case
implementation. In addition, the customers can benefit additional features and functionalities offered in the "Optional" products
such as, centralized management, monitoring, logging, etc. and extend the solution capabilities beyond "Recommended"
products in their projects.
Why does the Ordering Guide only list limited SKUs for each Fortinet product line?
The SKUs that are listed in the Ordering Guide are representing the most deployed products for the use case implementations
from our current customer base. However, additional information on the other SKUs can be obtained from the Fortinet website
Are all Fortinet products available in rugged hardware appliance form?
No. Currently, only the select Fortinet products are offered in the rugged hardware appliance form, such as FortiGate Rugged,
FortiSwitch Rugged, and FortiDeceptor Rugged. Additionally, the customers have option to use a third-party Fortinet certified
Industrial PC (IPC) hardware to host VM appliance of Fortinet products.
Where can I find more information about product installation and configuration?
The product installation manuals, user guides, and quick start guides are available on the Fortinet website.
Where can I find more information about product certifications?
The information on product certifications is available on the Fortinet website.
15


**Table 15.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

Operational Technology (OT) Ordering Guide
Industry Awards | Fortinet Accolades
Learn about our industry awards for our innovations, solutions, and programs.
FortiGate Rugged FortiGate Rugged FortiGate Rugged FortiGate Rugged
70F 70G 70G-5G Dual 50G-5G / 70G-5G
Fortinet Training and Certification
FCSS – OT Security Training and Certification
This course focuses on securing OT infrastructures using Fortinet solutions. It covers designing, deploying, administering,
and monitoring FortiGate, FortiNAC, FortiAnalyzer, and FortiSIEM devices to secure OT infrastructures. These skills provide a
comprehensive understanding of designing, implementing, and operating an OT security solution based on Fortinet products.
Course Details
For prerequisites, agenda topics, and learning objectives, visit the Fortinet training website.
Training Offering
For training SKUs, purchasing, and delivery options, visit the Fortinet training website.
www.fortinet.com
®
Copyright © 2026 Fortinet, Inc. All rights reserved. Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product
or company names may be trademarks of their respective owners. Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other
conditions may affect performance results. Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s General Counsel, with a purchaser
that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet. For absolute clarity, any
such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify, transfer, or otherwise
revise this publication without notice, and the most current version of the publication shall be applicable.
July 17, 2026 3:34 PM
OT-OG-R25-170726
