# og-fortisoar

Ordering Guide
FortiSOAR
Available in
Virtual
FortiSOAR is a leading Security Orchestration, Automation, and Response (SOAR)
platform designed to integrate seamlessly with SIEM, UEBA, EDR, and other threat
detection and response systems. It provides centralized automation, case management,
and incident response capabilities that empower security teams to efficiently detect,
investigate, and mitigate threats.
This Ordering Guide, used in conjunction with the FortiSOAR Datasheet, helps you plan
your purchase, deployment, and scaling strategy. It outlines the various license options,
deployment models, and system components available to fit diverse organizational
needs—from small security teams to large, distributed SOC environments.
The following sections walk you through the key considerations that influence
purchasing decisions, including platform architecture, user tiers, add-on modules,
and integration options, ensuring that you can select the right configuration for your
operational and business requirements.
Start Here:
To help simplify your
FortiSOAR purchase and
deployment planning,
Fortinet offers five guided
steps. Each step guides
you in selecting the right
deployment type, licensing
model, training, and
professional services to
ensure a successful rollout.

FortiSOAR Ordering Guide
Step 1 – Select Deployment Model
“Where will it run?”
Start by identifying where the FortiSOAR should run based on customer infrastructure, compliance, and operational preferences.
FortiSOAR is available as a virtual appliance that can be deployed in various environments, including on-premises, Fortinet-
hosted (PaaS), and public cloud platforms.
OPTION WHEN TO CHOOSE KEY BENEFIT
On-Prem VM Appliance Customer has data residency, compliance, or high-throughput
Full control and scalability.
(Customer-hosted) needs
PaaS Customer wants a dedicated environment without Simplified operations with Fortinet-managed hosting and
(Fortinet-hosted) infrastructure maintenance.
Step 2 – Size the Deployment
“How big does it need to be?”
Align the solution to the customer’s scale, performance needs, and SOC maturity. FortiSOAR is offered in several node types to
accommodate different use cases and operational scales:
ENVIRONMENT RECOMMENDATION WHAT IS INCLUDED
Designed for accelerating self-managed SOC operations. It includes all FortiSOAR features except those
Mid-size and Large Enterprise Enterprise Edition
specific to multi-tenant or remote SOC environments.
Intended for Managed Security Service Providers (MSSPs) delivering SOCaaS or Managed SOAR services.
MSSP Multi-Tenant FortiSOAR Also suitable for large enterprises managing multiple SOCs that require dedicated SOAR instances under
centralized management.
A cost-effective option that includes essential Enterprise features with a daily allowance of 10,000 actions,
Small SOC Starter Edition
ideal for smaller teams or pilot deployments.
Step 3 – Determine Add-on Requirements
“What requirements are we solving?”
Determine features for resiliency and accessibility.
FEATURES WHAT IT DOES WHEN TO USE
Deploys FortiSOAR as a single-node instance for centralized automation Ideal for smaller SOCs, pilot deployments, or environments without HA/
Standalone
and case management DR requirements
Adds redundancy and failover capabilities to maintain service continuity Recommended for production SOC environments requiring high uptime
High Availability
during node or infrastructure failures and operational resilience
Enables recovery capabilities across geographically separate environments Recommended for organizations with strict recovery objectives or
Disaster Recovery
to support business continuity compliance requirements
Supports isolated deployments without internet connectivity for highly Ideal for government, defense, critical infrastructure, or restricted
Air-gapped
secure or regulated environments operational networks
Number of FortiSOAR Nodes: Begin with a single node and scale out to additional nodes for HA/DR or increased capacity.
Number of Concurrent User Seats: Defines how many users can be simultaneously logged in and operating the system.
HA (High Availability): Available for Enterprise Edition and Multi-Tenant “Manager” or “Regional SOC” deployments to ensure
redundancy and operational continuity.
2


**Table 2.1**

| OPTION | WHEN TO CHOOSE | KEY BENEFIT |
| --- | --- | --- |


**Table 2.2**

| ENVIRONMENT | RECOMMENDATION | WHAT IS INCLUDED |
| --- | --- | --- |


**Table 2.3**

| FEATURES | WHAT IT DOES | WHEN TO USE |
| --- | --- | --- |


**Table 2.4**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiSOAR Ordering Guide
Step 4 – Select procurement model
“How would the customer like to consume FortiSOAR?”
Finally, choose the licensing and consumption model that best aligns with the customer’s budgeting, operational, and
procurement preferences.
SUBSCRIPTION WHAT IT DOES WHEN TO USE
Annual or multi-year licensing that includes software entitlement and Best for customers seeking predictable budgeting and simplified lifecycle
Subscription
support services management
Flexible consumption-based licensing model that allows customers to Ideal for customers requiring operational flexibility, variable scaling, or
FortiFlex *
allocate usage dynamically across eligible Fortinet services centralized consumption management across deployments
* Supported from FortiSOAR 7.6.1 onward for Enterprise and Multi-Tenant node types.
Step 5 – Select Training and Professional Services
“How will the customer accelerate adoption and operational success?”
This aligns better with business outcomes rather than just training procurement.
TRAINING OFFERING WHAT IT DOES
FortiSOAR Administrator Learn FortiSOAR architecture, deployment, configuration, RBAC security management, HA setup, and system monitoring. View Course
Master playbook creation—from simple to complex workflows—and learn to build dashboards, automate threat responses, and integrate
FortiSOAR with FortiGate, FortiSIEM, and FortiMail. View Course For training SKU details, visit the Training Purchase Process Page.
FortiSOAR Design and Development
Additional Resources: FortiSOAR Platform Documentation, FortiSOAR Content Hub, FortiSOAR Connectors List, FortiSOAR Public GitHub,
FortiSOAR Community Forum.
Security automation maturity evolves over time, and Fortinet offers tailored professional services to help customers deploy,
operationalize, and optimize FortiSOAR effectively.
• Quick-Start Service:
A guided onboarding package using standardized best practices to help you set up and begin realizing value quickly. Includes
knowledge transfer to empower your team to manage the environment independently.
• Scoped SoW Engagements:
Customized, Statement of Work–based engagements for tactical needs such as module development, playbook creation, or
integration support.
• Resident Engineer Program:
Long-term engagements (typically 6–12 months) that provide a dedicated Fortinet SOAR expert to support your SOC
operations and maturity journey
FortiSOAR Agentic AI Licensing
FortiSOAR v8.0 introduces Agentic AI capabilities that enhance security operations with AI-powered investigation, reasoning,
and autonomous response.
Customers with an active FortiSOAR subscription can access Agentic AI capabilities without purchasing an additional feature
license. Each FortiSOAR device includes 5 million FortiAI tokens per month, which provides approximately 60 AI investigations
depending on investigation complexity and usage.
For organizations requiring additional AI capacity, FortiAI token top-up licenses are available. FortiAI tokens are account-based
and can be shared across Fortinet products that support FortiAI capabilities.
3


**Table 3.1**

| SUBSCRIPTION | WHAT IT DOES | WHEN TO USE |
| --- | --- | --- |


**Table 3.2**

| TRAINING OFFERING | WHAT IT DOES |
| --- | --- |


**Table 3.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiSOAR Ordering Guide
Deployment Bundles
These sample deployment bundles demonstrate how FortiSOAR components can be combined to address different operational
and organizational requirements.
Customer 1: Enterprise HA Deployment
An enterprise customer requires an on-premise FortiSOAR deployment with 10 analysts, 2 years of support, FortiGuard Threat
Intelligence integration, and developer training. Also, requiring a separate development node for playbook and connector
creation.
Steps Requirement SKUs
Step 1 - Select Deployment Model On-Prem VM Appliance FC-10-SRVMS-389-02-24 – FortiSOAR Enterprise Edition (2
Step 2 - Size the Deployment Enterprise Edition seats included) (2 years)
8xFC-10-SRVMS-384-02-24 – 8 Additional User Seats (2
10 analysts years)
FC-10-SRVMS-592-02-24 – FortiSOAR Threat Intel
Step 3 – Determine Add-on Requirements FortiGuard TIM Management Service with FortiGuard Premium Threat Feed
(2 years)
Development Instance FC-10-SRVMS-1023-02-24 – FortiSOAR Starter Edition (2
years) (for development)
Step 4 – Select procurement model Subscription
FT-FSR-DEV – NSE 7 FortiSOAR Design & Development
Training
Step 5 – Select Training and Professional services Developer Training
(If professional services are required, a custom quote can be
requested from the PS team.)
Customer 2: MSSP Multi-tenant Deployment
An enterprise customer requires an on-premise FortiSOAR deployment with 30 analysts, 3 years of support, FortiGuard Threat
Intelligence integration, and developer training. Also, requiring a dedicated node for a tenant and development node for
playbook and connector creation.
Steps Requirement SKUs
Step 1 - Select Deployment Model On-Prem VM Appliance FC-10-SRVMS-390-02-36 – FortiSOAR Enterprise Edition (2
Step 2 - Size the Deployment Enterprise Edition seats included) (3 years)
28xFC-10-SRVMS-384-02-36 – 28 Additional User Seats (3
years)
FC-10-SRVMS-592-02-36 – FortiSOAR Threat Intel
Management Service with FortiGuard Premium Threat Feed
10 analysts
(3 years)
Step 3 – Determine Add-on Requirements FortiGuard TIM
FC-10-SRVMS-1023-02-24 – FortiSOAR Starter Edition (3
Development Instance
years) (for development)
FC-10-SRVMS-387-02-24 – FortiSOAR Starter Edition (3
years) (for development)
Step 4 – Select procurement model Subscription
Developer Training
FT-FSR-DEV – NSE 7 FortiSOAR Design & Development
Step 5 – Select Training and Professional services (If professional services are required, a custom quote can be
Training
requested from the PS team.)
4


**Table 4.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiSOAR Ordering Guide
Customer 3: Fortinet-Hosted Cloud Deployment
A customer selects the Fortinet-hosted cloud option for 10 analysts, 1 years of support and requires developer training.
Steps Requirement SKUs
Step 1 - Select Deployment Model PaaS FC-10-SRCLD-386-02-12 – FortiSOAR Hosted Cloud
Subscription (Enterprise Edition with 2 seats and support
Step 2 - Size the Deployment Mid-sized Enterprise
included) (1 year)
8x FC-10-SRCLD-384-02-12 – 8 Additional User Seats (1
Step 3 – Determine Add-on Requirements 10 analysts
year)
Step 4 – Select procurement model Subscription
FT-FSR-DEV – NSE 7 FortiSOAR Design & Development
Training
Step 5 – Select Training and Professional services Developer Training
(If professional services are required, a custom quote can be
requested from the PS team.)
Sizing Quick Reference
The following reference sizing guidance helps align FortiSOAR infrastructure requirements with expected user scale, workload
volume, and deployment maturity.
ENVIRONMENT SIZE USERS RECOMMENDED VCPU RAM STORAGE
Small SOC 5–10 8 24 GB 500 GB
Mid-Size 25–50 12 32 GB 1 TB
Large Enterprise and MSSP 100+ 24 48 GB 2 TB+
5


**Table 5.1**

| ENVIRONMENT SIZE | USERS | RECOMMENDED VCPU | RAM | STORAGE |
| --- | --- | --- | --- | --- |


**Table 5.2**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiSOAR Ordering Guide
Ordering Information
DEPLOYMENT OPTIONS AND LICENSING MODEL
FORTISOAR VM FORTISOAR CLOUD
(SUBSCRIPTION ) (PaaS)
DEPLOYMENT
License Type Subscription or via FortiFlex Subscription
Hosting Type On Premise or Public Cloud Fortinet Hosted
EDITIONS
Enterprise Edition FC-10-SRVMS-389-02-DD FC-10-SRCLD-385-02-DD*
Multi Tenant Edition - Manager Node FC-10-SRVMS-390-02-DD FC-10-SRCLD-386-02-DD*
Multi-Tenant - Dedicated Node FC-10-SRVMS-387-02-DD FC-10-SRCLD-387-02-DD
Multi-Tenant - Regional Node FC-10-SRVMS-388-02-DD FC-10-SRCLD-388-02-DD
HA Node FC-10-SRVMS-1121-02-DD
Starter Edition FC-10-SRVMS-1023-02-DD
ADD-ON
Threat Intel Management Module (includes FortiGuard Threat Feed) FC-10-SRVMS-592-02-DD FC-10-SRCLD-592-02-DD
User Seat FC-10-SRVMS-384-02-DD FC-10-SRCLD-384-02-DD
Cloud Storage (additional 1TB Storage, 8GB RAM, and 4 vCPU) FC1-10-SRCLD-584-01-DD
PROFESSIONAL AND TRAINING SERVICES
FortiMonitor - subscription for Advanced Health Monitoring FC2-10-MNCLD-437-01-DD **
Per Day Charge for Resource Service (SOW) FP-10-00000-M08-00-00
Per Hour Charge for Service Delivered After-Hours/Weekend. Must order a
FP-PS001-HR
minimum of four hours, and must use a minimum of four hours at a time
Custom Travel and Expenses for On Site Professional Services FP-MISC-TE
Deployment Quick Start Service FP-10-QSSOAR-DP1-00-00
NSE 6 FortiSOAR Administration Training FT-FSR-ADM
NSE 6 FortiSOAR Administration Exam Voucher NSE-EX-SPL6
NSE 7 FortiSOAR Design and Development Training FT-FSR-DEV
NSE 7 FortiSOAR Design and Development Exam Voucher NSE-EX-CERT
NSE 7 FortiSOAR Design and Development Lab Access FT-FSR-DEV-LAB
FORTIAI-ASSIST TOP-UP LICENSE
1,000,000 AI tokens valid for 3 years LIC-FAITOKEN-1M
5,000,000 AI tokens valid for 3 years LIC-FAITOKEN-5M
10,000,000 AI tokens valid for 3 years LIC-FAITOKEN-10M
6


**Table 6.1**

| DEPLOYMENT OPTIONS AND LICENSING MODEL |  |  |
| --- | --- | --- |
|  | FORTISOAR VM (SUBSCRIPTION ) | FORTISOAR CLOUD (PaaS) |
| DEPLOYMENT |  |  |


**Table 6.2**

| FORTIAI-ASSIST TOP-UP LICENSE |  |
| --- | --- |


**Table 6.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiSOAR Ordering Guide
Frequently asked questions
Licensing and User Management
What type of user licensing model does FortiSOAR use?
FortiSOAR licensing supports both named users and concurrent active sessions.
A named user is an individual account created within the platform that is intended for human access to the system.
In most deployments:
• Each unique human operator typically consumes one license
• Shared accounts are generally discouraged for auditability and RBAC reasons
• Login frequency does not usually change license consumption
While concurrent active users define the maximum number of users who can be simultaneously logged in and actively using the
platform.
As an example, a SOC with:
• 30 analysts
• operating across 3 shifts
• but only 10 analysts online simultaneously.
With concurrent active users, only 10 licenses are needed. Whereas Named user requires 30 licenses.
FortiSOAR does not impose any restrictions on creating a user. Technically, your entire organization can log in to FortiSOAR. The
only restriction is how many of them can log in at the same time (aka concurrently).
This model comes in handy to optimize the number of user licenses you need. For example, let’s assume you have 2 admins
and 30 analysts across 3 shifts. In this case, you could reduce the number of seats to 12 (2 reserved for admins and 10 floating
amongst the analysts).
Do disabled/inactive, API, and Automation users accounts consume licenses?
The disabled or inactive accounts won’t consume licenses. Even though, Organizations should periodically review stale accounts
as best practice.
The non-human integration accounts are treated differently from analyst users.
While Automation users are counted as concurrent users.
What happens if the licensed user count is exceeded?
Only the allowable concurrent user is able to use the system.
How does licensing work for MSSPs?
FortiSOAR Multi-Tenant deployments are designed to support MSSP operational models where multiple customer environments
are centrally managed. Licensing is typically aligned to the deployment architecture, node types, and the number of concurrent
user seats required across operational teams. Dedicated tenant environments can be deployed for customer isolation, while
centralized manager or regional SOC nodes can be used to streamline administration and content management across multiple
customers.
Contact your Fortinet representative for guidance on sizing and designing MSSP-specific deployments.
What do I need to create a basic highly available environment?
Assuming a basic HA design, VM based deployment, enterprise edition subscription licenses, with 5 user seats:
• 1x FortiSOAR Enterprise subscription license (incl. 2 users)
• 1x FortiSOAR HA-only subscription license
• 3x FortiSOAR user seat license subscription
Contact your local FortiSOAR expert to discuss advanced HA and clustering designs, scalability, and other architectural
considerations.
7


**Table 7.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiSOAR Ordering Guide
Do I need an additional license to use FortiSOAR Agentic AI?
No. FortiSOAR v8.0 customers with an active subscription can use Agentic AI capabilities with the included monthly FortiAI token
entitlement. Additional FortiAI tokens can be purchased as top-ups if higher AI usage capacity is required.
Deployment
What is included in the FortiSOAR Starter Edition?
FortiSOAR Starter Edition carries all the features of the FortiSOAR Enterprise Edition, only limited in allowing 10,000 automation
actions/day. It comes with 2 default users, allows you to add more user seats and can be setup in an HA cluster. An automation
action is roughly defined as a step in a playbook, except that it does not account certain utility actions like Decision, Trigger etc.
Do I need a FortiCloud Premium Account to use FortiSOAR Cloud?
As of Q1 2025, a FortiCloud Premium account is no longer required to use FortiSOAR Cloud
What deployment platforms are supported?
FortiSOAR has ready-made images available for VMware Hypervisor and Amazon AWS AMI. For any other physical, virtual, or
cloud hosting you can install FortiSOAR on top of Rocky Linux 9.x or RHEL 9.x.
Do I need a node for development and testing?
You can leverage the FortiSOAR Free Trial license or Starter Edition for such dev/test work based on the capacity required. The
FortiSOAR Trial license is perpetually valid, allowing 2 user accounts as well as 1000 playbook actions/day whereas the Starter
Edition allows 10,000 actions/day without posing any user limitations as such.
I need more information about Fortinet’s hosted deployment option.
Refer to FortiCloud Datasheet: https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiCloud.pdf
Connectors and Playbook
Is there any charge for using a connector?
FortiSOAR does not impose any charge on installing/using a connector. However please note that the target application (for
example VirusTotal) might need you to procure their service/API, etc. for being consumed by the connector.
What options exist to build or customize connectors?
Option 1 – FortiSOAR provides full IDE to build, test, and publish connectors. Leverage that to build a new or enhance an existing
connector. You can also submit the one that you built to the FortiSOAR Community.
See the instructions here: https://github.com/fortinet-fortisoar/how-tos
Option 2 – Request your Account Manager to create a task for FortiSOAR R&D to build the connector. The success of this option
is dependent on various aspects, some of which are:
• Access/Availability of target application to Test
• Access/Availability of target application’s API
• Demand for the desired integration
Several such criteria would be applied by the FortiSOAR PM to decide the timeline of delivery for the requested integration
Option 3 – Leverage FortiSOAR Professional Services (PS) to quickly build the integration scoped to your needs. This option
requires you to purchase PS and it is likely to have the fastest turnaround time. It is suitable if you urgently need an integration
that is not on the store.
8


**Table 8.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiSOAR Ordering Guide
Threat Intelligence Management (TIM)
What does the TIM SKU include?
This SKU unlocks full access to FortiGuard’s uncapped daily threat intelligence feeds in FortiSOAR (limited to 100 feeds/day
without it). These curated feeds include IPs, URLs, domains, and malicious hashes labeled by threat type and Lockheed Martin
Kill Chain phase for deeper context.
Key benefits:
• Contextual Sightings: Automatically links indicators to FortiGuard feeds, providing richer context and dashboards showing
intelligence relevance by sighting frequency.
• Unlimited Ingestion: Removes the 1,000-record daily limit for the Threat Intel Management module; without it, ingestion stops
once the limit is reached.
• Unlimited Sharing: Allows unrestricted export of processed feeds via the FortiSOAR TAXII API (otherwise capped at 100
records per response).
For more details, refer to the Threat Intel Management Solution Pack documentation in the FortiSOAR Content Hub.
What limits exist without the SKU?
Without the Threat Intelligence Management (TIM) SKU:
• FortiSOAR is limited to 100 FortiGuard threat feeds per day
• Threat intelligence ingestion is capped at 1,000 records per day
• TAXII export responses are limited to 100 records per request
Organizations with high-volume intelligence workflows or external sharing requirements should consider the TIM SKU to remove
these operational limits.
What ingestion/export restrictions apply?
Without the TIM SKU, FortiSOAR enforces daily ingestion and export limitations to manage threat intelligence processing
capacity. These restrictions primarily affect:
• the number of records ingested from external feeds,
• the number of FortiGuard feeds processed daily,
• and the number of records exported through TAXII APIs.
The TIM SKU removes these limitations and enables unrestricted ingestion and sharing workflows for enterprise-scale threat
intelligence operations.
www.fortinet.com
Copyright © 2026 Fortinet, Inc. All rights reserved. Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product or
company names may be trademarks of their respective owners. Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other condi-
tions may affect performance results. Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s SVP Legal and above, with a purchaser
that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet. For absolute clarity, any
such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify, transfer, or otherwise
revise this publication without notice, and the most current version of the publication shall be applicable.
July 7, 2026 3:41 PM
FSR-OG-R21-20260707
