# og-fortiaigate

Ordering Guide
FortiAIGate
Container
OVERVIEW
FortiAIGate is an enterprise-grade LLM Security Gateway purpose-built to protect your
business-critical large language models (LLMs), model context protocol (MCP), agentic
AI applications, and AI Factory from modern AI-specific threats.
From corporate chatbots, customer support agents, and virtual assistants to fraud
detection, cybersecurity threat hunting, supply chain optimization, and healthcare
analytics, FortiAIGate delivers comprehensive protection against both known and
unknown vulnerabilities targeting LLMs, MCP servers, and agentic applications.
Backed by a multi-GPU–accelerated LLM/MCP inspection engine and a multi-layered
security framework, FortiAIGate safeguards your AI systems against select vulnerabilities
mentioned in the OWASP Top 10 for LLM Applications, OWASP Top 10 for MCP 2025, and
OWASP Top 10 for Agentic Applications 2026.


**Table 1.1**

|  |  |  |
| --- | --- | --- |

FortiAIGate Ordering Guide
KEY CAPABILITIES
Multi-Layered AI Protection
FortiAIGate employs multiple defense layers to detect and prevent:
• Direct and indirect prompt injections attacks
• Direct and indirect jailbreaking attempts
• Sensitive data exposure
• Data leakage in LLM responses
• MCP tool-related attacks
• Adversarial or malicious prompt patterns
Intelligent Reverse Proxy
Operates as a secure AI reverse proxy, filtering and mediating all communications between users, AI agents, and backend LLM
providers.
Smart Access Control and Governance
• Intelligent routing to direct requests to the most appropriate LLM backend based on the content of the requests.
• Static routing to deterministically direct requests to a pre-defined LLM backend.
• API key validation and custom allowlist/denylist policies for fine-grained access control.
• Usage and cost tracking for visibility, billing, and compliance across AI workloads.
Cloud-Native Security
Designed from the ground up for cloud-native Kubernetes (K8s) environments, FortiAIGate ensures scalable, fault-tolerant, and
GPU-optimized protection for modern AI pipelines.
SUPPORTED AI PROVIDERS
FortiAIGate integrates seamlessly with leading public and private AI providers, including:
• OpenAI
• AWS Bedrock Converse
• Microsoft Azure AI Foundry
• Anthropic
Note: Additional public and private AI providers will be introduced in future FortiAIGate releases.
2


**Table 2.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiAIGate Ordering Guide
DEPLOYMENT OPTIONS
DEPLOYMENT MODEL DESCRIPTION IDEAL FOR
Bare Metal Kubernetes Cluster High-performance, GPU-accelerated container deployment Organizations requiring maximum performance and direct hardware
with NVIDIA GPUs directly on bare metal servers equipped with NVIDIA GPUs. access.
Scalable deployment on private or public virtualized environments
Private/Public Virtual Cloud Kubernetes Cluster
(e.g., KVM, Amazon EC2, VMware ESXi) with GPU-enabled virtual Enterprises leveraging private or hybrid cloud infrastructure.
with NVIDIA GPUs
machines.
Fully managed container deployment on public managed
Managed Kubernetes Cloud Services Cloud-first organizations seeking simplified management and
Kubernetes services (e.g., Amazon EKS) supporting NVIDIA GPU-
with NVIDIA GPUs elasticity.
accelerated containers.
Regardless of environment — on-premises, private cloud, or public cloud — FortiAIGate delivers consistent protection,
visibility, and governance for all your Agentic AI applications that best matches your organization’s AI security, scalability, and
performance requirements.
SUMMARY
FortiAIGate combines advanced AI inspection, intelligent routing, and cloud-native security to form a comprehensive defense
layer for modern LLM-driven applications.
It ensures that your organization’s AI systems remain:
• Secure — protected from prompt injection and data leakage.
• Compliant — aligned with data governance and regulatory requirements.
• Optimized — leveraging NVIDIA GPU acceleration for real-time AI traffic protection.
FortiAIGate: Protecting the Intelligence Behind Your AI Factory.
3


**Table 3.1**

| DEPLOYMENT MODEL | DESCRIPTION | IDEAL FOR |
| --- | --- | --- |


**Table 3.2**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiAIGate Ordering Guide
PRODUCT OFFERINGS
FortiAIGate is available through an OPEX-based annual subscription model, offering flexible deployment of our containerized AI
Gateway across major hypervisors and public cloud providers.
Unlike traditional licensing schemes, FortiAIGate licensing is not based on:
• The number of Agentic AI requests, queries, or calls
• The number of users or seats
• The amount of infrastructure resources (CPU, RAM, or GPU)
Instead, licensing is per worker node, ensuring predictable and scalable costs aligned with your deployment footprint.
Each FortiAIGate worker node requires a separate license and is covered under an annual subscription plan. This subscription
provides continuous access to product updates, security enhancements, and technical support throughout the licensed term.
Note: FortiAIGate subscriptions are renewed annually. Advanced and Enterprise bundles will be introduced in future releases to
support expanded feature sets and environments.
FORTIAIGATE-LLM GATEWAY
RESOURCES VALUE
Max GPUs Unrestricted
Max CPUs Unrestricted
Max RAM Unrestricted
Query Per Second Throughput Unrestricted
Max LLM Sessions Unrestricted
Max LLM Users Unrestricted
Max Worker Nodes Unlimited (Each Worker Node Requires a Separate License)
DEPLOYMENT OPTION VALUE
Form Factor Container
Environment Kubernetes
SECURITY SERVICES BUNDLE
Prompt Injection/Jailbreaking Detection Standard
Data Leak Prevention Standard
Toxicity Detection Standard
Custom Blacklist/Whitelist Rules Standard
MCP Tool Scanning Standard
CORE SERVICES BUNDLE
Secure LLM Proxy Standard
One Unified Client API Standard
Many Providers and Models Standard
Static Routing Standard
Intelligent Routing Standard
Cost Tracking Standard
ADDITIONAL SERVICES BUNDLE
24x7 Support Included
4


**Table 4.1**

| FORTIAIGATE-LLM GATEWAY |  |
| --- | --- |
| RESOURCES | VALUE |


**Table 4.2**

| DEPLOYMENT OPTION | VALUE |
| --- | --- |


**Table 4.3**

| SECURITY SERVICES | BUNDLE |
| --- | --- |


**Table 4.4**

| CORE SERVICES | BUNDLE |
| --- | --- |


**Table 4.5**

| ADDITIONAL SERVICES | BUNDLE |
| --- | --- |


**Table 4.6**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiAIGate Ordering Guide
ORDER INFORMATION
LLM GATEWAY SKU DESCRIPTION
Standard subscription license of FortiAIGate-LLM Gateway for
Standard Subscription FC-10-AIGCN-1316-02-DD
1 worker node. Includes Premium FortiCare Support.
www.fortinet.com
Copyright © 2026 Fortinet, Inc. All rights reserved. Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product
or company names may be trademarks of their respective owners. Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other
conditions may affect performance results. Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s SVP Legal and above, with a
purchaser that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet. For absolute
clarity, any such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify, transfer,
or otherwise revise this publication without notice, and the most current version of the publication shall be applicable.
FAIG-OG-R07-20260706


**Table 5.1**

| LLM GATEWAY | SKU | DESCRIPTION |
| --- | --- | --- |
