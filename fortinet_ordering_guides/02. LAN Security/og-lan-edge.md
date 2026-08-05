# og-lan-edge

Ordering Guide
FortiGate Secure LAN
Controller
Available in
Appliance Cloud
Welcome to the Fortinet FortiGate Secure LAN Controller Ordering Guide. This guide is
designed to help customers understand and navigate the various options available for
deploying FortiGate as a fully capable Wi-Fi and Switch Controller, in addition to its full
suite of security functions, able to manage FortiAPs, FortiSwitches, and extend Network
Access Control (FortiLink NAC) throughout the LAN.
This guide outlines:
• Key Capabilities: FortiGate Secure LAN Controller offers features such as managing
FortiAP and FortiSwitch units via FortiLink, extending the Fortinet Security Fabric to
the LAN, and simplifying network management with a single console for security and
network functions.
• FortiLink Technology: Explains how FortiLink enables FortiAPs and FortiSwitches to
become extensions of the FortiGate security appliance.
• FortiLink NAC: Details how FortiLink NAC enhances network access control throughout
the LAN.
• Considerations for NGFW Selection: Includes factors such as security requirements,
throughput, interface connectivity, and redundancy (WAN, power, IPsec VPN tunnels,
device).
• FortiAP Deployment Guidelines: Provides estimations for FortiAP density
(approximately one FortiAP for 1500 sq ft or 150 sq m, and about 60 active devices
per FortiAP), and explains the difference between 4x4 and 2x2 MIMO in FortiAPs
regarding antenna alignment and performance benefits for client devices.

FortiGate Secure LAN Controller Ordering Guide
FortiGate Secure LAN Controller
FortiGate, a Dedicated LAN Controller
The FortiGate, in addition to its full suite of security functions, is a fully capable Wi-Fi and Switch Controller, able to manage
FortiAPs, FortiSwitches, and extend Network Access Control (FortiLink NAC) throughout the LAN — Fortinet’s Secure LAN
solution.
The Fortinet Secure LAN solution consolidates network management into our industry-leading FortiGate. This solution provides
comprehensive security for the LAN and WLAN infrastructure. With a single console for security and network functions,
management is greatly simplified on a day-to-day basis, and security is fully integrated with every part of the network.
FortiGate Secure LAN Functions
All FortiGates include the following Secure LAN functions out of the box. No additional licensing is needed.
The FortiGate Wi-Fi and Switch Controller
The FortiGate Wi-Fi and Switch Controller manages FortiAP and FortiSwitch units in the network via FortiLink, extending the
Fortinet security fabric throughout the LAN, where end-devices connect to the network. A single pane of glass manages all the
LAN access ports — FortiSwitch physical, FortiAP virtual.
FortiLink
FortiLink technology enables FortiAPs and FortiSwitches to become extensions of the FortiGate security appliance. When
connected via FortiLink, traffic is tunneled to the FortiGate for full security inspection without the need to configure trunk lines
on the FortiSwitches. FortiAPs do not require FortiSwitches to connect via FortiLink to their FortiGate controller. FortiAPs and
FortiSwitches are complementary, but not mutually required.
FortiLink NAC
FortiLink NAC can dynamically assign devices to VLANs based on multiple criteria detected by FortiAPs or FortiSwitches. It can
identify devices by multiple criteria, including device pattern (such as OS, MAC address, or hardware vendor), user identity,
VLAN attributes, IoT/OT vulnerabilities, or integration with FortiClient EMS tags. For example, Internet of Things (IoT) sensors
could be automatically identified and assigned to a specific VLAN with targeted policies that only allow communication with
their control server. FortiLink NAC also generates an inventory of connected devices, providing network administrators greater
visibility.
2

FortiGate Secure LAN Controller Ordering Guide
PRODUCT OFFERINGS
FortiAP—Standard and Unified Threat Protection Models
FortiAP devices come in a variety of models that support the latest Wi-Fi technologies, including Wi-Fi 6 (F series), 6E (G
series), and even Wi-Fi 7 (K series). Indoor, outdoor, and high-density models are available, as well as wall-plate models for the
hospitality industry.
FortiAP product family is Wi-Fi7 ready and are available in 2x2 (two MIMO stream) and 4x4 (four MIMO stream) models. Several
G series models support dual 5 GHz operation mode for the most demanding Wi-Fi environments. The FAP-831F is an 8x8
Multi-User MIMO model for high density cases, such as lecture halls or auditoriums. FortiGates require no additional licenses to
manage FortiAPs, although there are FortiGate model-specific AP limits.
FortiAP K series Wi-Fi 7 models, along with support for 6 GHz spectrum, are designed to meet the next generation of wireless
connectivity needs by supporting generational improvements of Wi-Fi 7 (802.11be) over Wi-Fi 6/6E (802.11ax), which includes
4K-QAM, support for 320 MHz, Multi-Link Operation (MLO), Multi-RU, and puncturing capability for better use of spectrum.
To support these multi-gig over-the-air transmissions, these APs can be powered by FortiSwitch with 802.3bt PoE and Multi-
Gigabit connectivity.
FortiSwitch—Ethernet Switching
Reliable, highly-performing, and purpose-built, Ethernet FortiSwitches are available in a variety of models to address needs from
the small office access layer to the datacenter. All models support FortiLink and can be managed and configured directly from a
FortiGate. MCLAG (Multi-Chassis Link Aggregation Group) is supported on most models for network redundancy.
In a Secure LAN deployment, it is vital to align the switch uplink speed with the capacity of the FortiGate. Avoid too little
FortiGate with too much FortiSwitch. PoE (Power over Ethernet) access switches can provide power for FortiAPs. FortiGates
require no additional licenses to manage FortiSwitches, although there are FortiGate model-specific switch limits.
3

FortiGate Secure LAN Controller Ordering Guide
PRODUCT OFFERINGS
Secure LAN Design
Fortinet Secure LAN Solutions are very flexible and can be adapted to a wide variety of network needs. Some guidelines follow,
but it is best to work with an experienced Fortinet reseller to ensure the chosen products align with your networking needs.
Dedicated vs Perimeter Secure LAN Controller
There are two broad design approaches to using a FortiGate as a Secure LAN Controller: SD-Branch and Dedicated Controller.
SD Branch/Branch
The SD-Branch/Branch design is built around the main internet access FortiGate also directly controlling any Secure LAN
devices. This design is typical of Branch and SMB offices. Total number of FortiAPs should initially be around 50% of the
FortiGates listed tunneled-traffic maximum. That quantity leaves capacity for growth and new, advanced Wi-Fi technologies.
FortiSwitches in these type of deployments will be access layer models that deliver PoE (Power overEthernet) to the FortiAPs
and connect directly to the FortiGate.
4


**Table 4.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
Dedicated Secure LAN Controller/ISFW Firewall
The dedicated Secure LAN Controller/ISFW Firewall, also sometimes called an overlay design is typical for campus
networks with larger numbers of FortiAPs and a pre-existing switching network. The FortiGate Secure LAN Controller is usually
dedicated to the Wi-Fi traffic. The FortiGate provides Wi-Fi controller functions, and serves as a Wi-Fi traffic concentrator and
security inspection point, but is an ISFW (Internal Segmentation Firewall), rather than the primary Internet uplink. FortiAPs can
tunnel FortiLink to the FortiGate Secure LAN Controller through an existing switch network, or FortiSwitches may be deployed
specifically to support the FortiAPs.
5


**Table 5.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
FortiAP Requirements
Determine the number of FortiAPs needed first, which is primarily driven by how much floor space needs to be covered, with
adjustments to the local wireless conditions. Wi-Fi design is highly location dependent, and a wireless site- survey from your
reseller is always recommended.
For planning purposes, a FortiAP typically covers 1500 sq ft (150 sq m) and accommodates 60 active devices per service radio,
or 120 devices per FortiAP. The 2x2 models are common in retail, public access, and similar lighter use. The 4x4 models are
more common in offices and heavier use environments. However, all devices will perform well with all FortiAP models. Consult a
Fortinet reseller about external antenna or specialty models, such as the FAP-23JF.
The UTP (Unified Threat Protection) models can deliver FortiGuard services on the FortiAP itself, offloading from the FortiGate.
FortiAPs can be powered by standards-based PoE access switches that match the requirements of the particular model. Power
injectors or AC power can be used when PoE switches are unavailable. FortiAPs can connect to a FortiGate via FortiLink over
any IP network with full functionality, including providing FortiLink NAC for wireless devices; FortiSwitches are not necessary but
can optionally be added if required.
More in depth wireless design resources can be found here.
Number of FortiSwitches — Access Ports
Start with the determining the number of access ports for your needs, both for the FortiAPs and for any other wired devices.
PoE access layer FortiSwitches can be used to power the FortiAPs as well as power other devices such as IoT devices or desk
phones. The total power budget needs to be aligned with the powered device needs.
FortiSwitches can also provide the wired port-based FortiLink NAC function, identifying devices by various criteria and assigning
them to policy determined VLANs automatically. If such devices need PoE power, that must be covered by the access switch
PoE power budget.
A switch FortiLink uplink must be directly connected to either a FortiGate Secure LAN Controller or another FortiSwitch that is, in
turn, FortiLink connected to a FortiGate.
In an SD-Branch design, a single access FortiSwitch connected directly to a FortiGate may be all that is needed. However, a
large campus with hundreds or thousands of FortiAPs will certainly require core and distribution switch layers with MCLAG
redundancy. Full Ethernet switch network design is beyond the scope of this document, but more in depth wired design
resources can be found here.
Size the Secure LAN Controller FortiGate
The scale of the FortiAP and FortiSwitch network will determine the necessary sizing of the FortiGate Secure LAN Controller.
The FortiGate should be sized as usual, based on throughput (by inspection type), but with the addition of accounting for the
tunneled FortiAP and FortiSwitch limits.
In order to leave room for growth, we recommend the FortiGate have a capacity for twice the number of FortiAPs (tunneled)
and FortiSwitches to be deployed. Because of the different ways traffic is handled on the FortiGate, the FortiAP and FortiSwitch
numbers are independent and can be evaluated separately. One Secure LAN device type does not affect the limit on the other
type.
The most conservative FortiGate throughput number is the Threat Protection Throughput (Enterprise Mix), and that will be cited
in the following examples. However, keep in mind that FortiAP-U series APs can offload FortiGuard Services. When that is the
case, the higher NGFW number should be used for the FortiGate. In a branch deployment, the throughput should be more than
the Internet uplink. In a dedicated controller environment, it is likely to be the same number in that the wireless end users are
probably the primary Internet users.
Finally, the more critical and larger the Secure LAN Network, the more likely the Secure LAN Controller should actually be a pair
of FortiGates in High Availability (HA) mode.
6


**Table 6.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
Cloud Management and Network Transition Options
Fewer and fewer networks of any size are deployed as pure greenfield. Most are established and have a refresh cycle with the
NGFW, Ethernet, and Wi-Fi — all refreshed at different times. Fortinet has options for those who want to transition to our Secure
LAN solution but are unable to do so all at once.
FortiEdge Cloud provides central cloud management for FortiAPs, FortiSwitches and FortiExtenders without an onsite FortiGate.
Fortinet Secure LAN equipment can be deployed to a site and managed in FortiEdge Cloud, and later transitioned to FortiGate in
the future.
FortiGate Cloud also provides cloud-based and remote management of FortiGates, and is completely compatible with everything
above. FortiGate Cloud, via cloud management of a FortiGate, in turn manages the Secure LAN FortiAPs and FortiSwitches.
FortiGate Cloud also adds one year of cloud log storage and backups, and is included in the FortiGate SMB bundles.
Example Specs/BoMs — FortiGate, FortiAP, FortiSwitch
NB – these are example BoMs, and should not be used as strict ‘recipes.’ Customer environments vary, and a full network design
will be necessary to get the right number of FortiAPs, FortiSwitches, ports, and power requirements.
Light Retail / Small Branch
An open area allows wider FAP coverage, Wi-Fi use is light, one wired register, one wireless printer, cost conscious, SMB Bundle.
LIGHT RETAIL / SMALL BRANCH
PRODUCTS NEED SUGGESTED SOLUTIONS
FortiAPs 4000 square feet, no walls, light Wi-Fi 241K, 231K, 243K
Access FSW 8 PoE ports, at power FS-108F-FPOE
Aggregation FSW Not needed —
FortiGate SMB class firewall + WiFi and switch controller FGT-50G
SFP Not needed —
Mid Size Branch
Thirty thousand square feet, multi-gig access switches in a redundant MCLAG pair, extra PoE ports for PoE desk phones,
redundant FortiGates as dedicated Wi-Fi and Switch controllers (ISFW), Enterprise Bundle.
MID SIZE BRANCH
QTY SKU SUPPORT
FortiAPs 30,000 square feet (20 FAP) FAP-441K/241K/231K/23JK
Access FSW Multi-Gig switches, bt/at PoE FS-110G-FPOE, FS-M426E-FPOE, FS-648F-FPOE or similar
Aggregation FSW MCLAG, SFP+ connectors FS-1024E, 1048E, 2048F
FortiGate Enterprise package, redundant pair Dual FGT-120G, HA mode
SFPs 10GE copper 10GE SFP+ copper connectors
Mid Range Enterprise
Large office building, multiple floors, 225 000 sq ft (150 FAPs), switch redundancy, redundant FortiGates as dedicated WiFi and
Switch controllers (ISFW), Enterprise bundle.
MID RANGE ENTERPRISE
QTY SKU SUPPORT
FortiAPs 225 000 sq ft (150 FAP) FAP-441K/241K
Access FSW Multi-Gig switch, bt PoE FS-M426E-FPOE, FS-648F, or similar
Aggregation FSW MCLAG, SFP+ connectors FS-1024E, 1048E, 2048F
FortiGate Enterprise package, redundant pair 2 FGT-600F, HA mode
SFPs SFP 10GE SFP+ copper connectors
7


**Table 7.1**

| LIGHT RETAIL / SMALL BRANCH |  |  |
| --- | --- | --- |
| PRODUCTS | NEED | SUGGESTED SOLUTIONS |


**Table 7.2**

| MID SIZE BRANCH |  |  |
| --- | --- | --- |
| QTY | SKU | SUPPORT |


**Table 7.3**

| MID RANGE ENTERPRISE |  |  |
| --- | --- | --- |
| QTY | SKU | SUPPORT |


**Table 7.4**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
Large Campus / School District
Eight hundred Indoor FortiAPs, 100 outdoor FortiAPs, Multi-Gig PoE access switches, aggregation switches, switch redundancy,
redundant FortiGates as dedicated Wi-Fi and Switch controllers (ISFW), Enterprise Bundle.
LARGE CAMPUS / SCHOOL DISTRICT
QTY SKU SUPPORT
FortiAPs Indoor and outdoor coverage FAP-441K/443K + FAP-432G/234G
FS-110G-FPOE, FS-M426E-FPOE, FS-648F, FS-T1024F-
Access FSW Multi-Gig switch, bt PoE
FPOE, or similar
Aggregation FSW MCLAG, SFP+ connectors FS-1024E/1048E/2048F/3032G
FortiGate Enterprise package, redundant pair 2 FGT-1800F, or similar
SFPs SFP 10/40 GE fiber
Top Sellers
Secure LAN FortiGates
RECOMMENDED MAX
MAX RECOMMENDED
BASE PRODUCT FORTIAP FORTIAP SUPPORT BUNDLE RENEWAL
FORTISWITCH BUNDLE
(TUNNELED) (TUNNELED)
SMALL RETAIL / BRANCH
FG-30G 4 8 8 Enterprise FG-30G-BDL-809-DD FC-10-0030G-809-02-DD
FG-50G 4 8 8 Enterprise FG-50G-BDL-809-DD FC-10-0050G-809-02-DD
FG-70G 24 48 24 Enterprise FG-70G-BDL-809-DD FC-10-0070G-809-02-DD
FG-80F 24 48 24 Enterprise FG-80F-BDL-809-DD FC-10-0080F-809-02-DD
FG-90G 64 128 24 Enterprise FG-90G-BDL-809-DD FC-10-0090G-809-02-DD
LARGE BRANCH / MID RANGE
FG-120G 32 64 48 Enterprise FG-120G-BDL-809-DD FC-10-F120G-809-02-DD
FG-200G 64 128 64 Enterprise FG-200G-BDL-809-DD FC-10-F200G-809-02-DD
FG-400F 128 256 96 Enterprise FG-400F-BDL-809-DD FC-10-0400F-809-02-DD
FG-600F 256 512 128 Enterprise FG-600F-BDL-809-DD FC-10-0600F-809-02-DD
FG-900G 1024 2048 196 Enterprise FG-900G-BDL-809-DD FC-10-FG9H0-809-02-DD
HIGH END / LARGE CAMPUS / SCHOOL DISTRICT
FG-1000F 1024 2048 196 Enterprise FG-1000F-BDL-809-DD FC-10-F1K0F-809-02-DD
FG-1800F 1024 2048 196 Enterprise FG-1800F-BDL-809-DD FC-10-F18HF-809-02-DD
FG-2600F 1024 2048 196 Enterprise FG-2600F-BDL-809-DD FC-10-F26HF-809-02-DD
FG-3000F 1024 2048 300 Enterprise FG-3000F-BDL-809-DD FC-10-F3K0F-809-02-DD
FG-3200F 1024 2048 300 Enterprise FG-3200F-BDL-809-DD FC-10-F3K2F-809-02-DD
FG-3500F 1024 2048 300 Enterprise FG-3500F-BDL-809-DD FC-10-F3K0F-809-02-DD
FG-3700F 1024 2048 300 Enterprise FG-3600E-BDL-809-DD FC-10-F3K6E-809-02-DD
FG-4200F 2048 4096 300 Enterprise FG-4200F-BDL-809-DD FC-10-F42HF-809-02-DD
FG-4400F 2048 4096 300 Enterprise FG-4400F-BDL-809-DD FC-10-F44HF-809-02-DD
FG-4800F 2048 4096 300 Enterprise FG-4800F-BDL-809-DD FC-10-F48HF-809-02-DD
Visit https://www.fortinet.com/products/next-generation-firewall for related FortiGate datasheets.
8


**Table 8.1**

| LARGE CAMPUS / SCHOOL DISTRICT |  |  |
| --- | --- | --- |
| QTY | SKU | SUPPORT |


**Table 8.2**

| BASE PRODUCT | RECOMMENDED FORTIAP (TUNNELED) | MAX FORTIAP (TUNNELED) | MAX FORTISWITCH | RECOMMENDED BUNDLE | SUPPORT BUNDLE | RENEWAL |
| --- | --- | --- | --- | --- | --- | --- |
| SMALL RETAIL / BRANCH |  |  |  |  |  |  |


**Table 8.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
Top Sellers
FORTIAP
PRODUCT SKU SUPPORT
STANDARD MODELS
FAP-441K FAP-441K-suffix* FC-10-FP431-247-02-DD
FAP-443K FAP-443K-suffix* FC-10-FP43K-247-02-DD
FAP-231K FAP-231K-suffix* FC-10-P231K-247-02-DD
FAP-23JK FAP-23JK-suffix* FC-10-P23JK-247-02-DD
FAP-241K FAP-241K-suffix* FC-10-FP21K-247-02-DD
FAP-243K FAP-243K-suffix* FC-10-FP23K-247-02-DD
FAP-432G FAP-432G-suffix* FC-10-P432G-247-02-DD
FAP-234G FAP-234G-suffix* FC-10-P234G-247-02-DD
FAP-432FR FAP-432FR-suffix* FC-10-FR432-247-02-DD
Visit https://www.fortinet.com/products/wireless-access-points for related FortiAP datasheets.
* FortiAP country code suffix explanation.
A country suffix code (-A, -B, -C, -D, -E, -F, -I, -J, -K, -N, -P, -S, -T, -U, -V, -W, or -Y) applies to all FortiAP models based upon country of deployment. Work with your local supplier for the
correct model in your regulatory domain.
** C1D2 certified for hazardous conditions.
FPoE FORTISWITCH
PRODUCT SKU SUPPORT
MODELS
FortiSwitch-108F-FPOE FS-108F-FPOE FC-10-F108F- 247-02-DD
FortiSwitch-110G-FPOE FS-110G-FPOE FC-10-M10GF-247-02-DD
FortiSwitchRugged-112D-POE FSR-112D-POE FC-10-W112D-247-02-DD
FortiSwitch-124F-FPOE FS-124F-FPOE FC-10-S124F-247-02-DD
FortiSwitch-124G-FPOE FS-124G-FPOE FC-10-S24GF-247-02-DD
FortiSwitch-148F-FPOE FS-148F-FPOE FC-10-148FF-247-02-DD
FortiSwitchRugged-216F-POE FSR-216F-POE FC-10-SR16F-247-02-DD
FortiSwitch-224D-FPOE FS-224D-FPOE FC-10-W0226-247-02-DD
FortiSwitch-248E-FPOE FS-248E-FPOE FC-10-W248E-247-02-DD
FortiSwitch-424E-FPOE FS-424E-FPOE FC-10-S424F-247-02-DD
FortiSwitch-M426E-FPOE FS-M426E-FPOE FC-10-M426E-247-02-DD
FortiSwitchRugged-424F-POE FSR-424F-POE FC-10-R24FP-247-02-DD
FortiSwitch-448E-FPOE FS-448E-FPOE FC-10-S448F-247-02-DD
FortiSwitch-548D-FPOE FS-548D-FPOE FC-10-W0501-247-02-DD
FortiSwitch-624F-FPOE FS-624F-FPOE FC-10-624FF-247-02-DD
FortiSwitch-648F-FPOE FS-648F-FPOE FC-10-648FF-247-02-DD
FortiSwitch-T1024F-FPOE FS-T1024F-FPOE FC-10-TF124-247-02-DD
Visit https://www.fortinet.com/products/ethernet-switches for related FortiSwitch datasheets.
9


**Table 9.1**

| PRODUCT | SKU | SUPPORT |
| --- | --- | --- |
| STANDARD MODELS |  |  |


**Table 9.2**

| PRODUCT | SKU | SUPPORT |
| --- | --- | --- |
| MODELS |  |  |


**Table 9.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
Order Information: FortiGate as a Secure LAN Controller
The Fortinet Secure LAN solution consolidates network management into our industry leading FortiGate. This solution provides
comprehensive security for the LAN infrastructure and simpler management on a day-to-day basis. Fortinet enables the
deployment of large-scale networks with minimal technical expertise via built-in best-practice configurations. Zero-touch
provisioning delivers quick and easy application of device templates to sites at scale. FortiLink NAC creates improved visibility
and segmentation, enabling auto-discovery of devices to implement “least privilege” access.
FORTIGATE
FG/FWF-30G FG/FWF-50G FG-70G FG/FWF-80F FG-90G
APPLIANCES
NGFW / PERIMETER FIREWALLS
Maximum FortiAPs
16 / 8 16 / 8 96 / 48 96 / 48 128 / 64
(Total/Tunnel)
Max FortiSwitches 8 8 24 24 24
Firewall Throughput
4/ 4/ 3.9 Gbps 5 / 5 / 4 Gbps 10 / 10 / 10 Gbps 10 / 10 / 7 Gbps 28 / 28 / 27.9 Gbps
(1518/512/64 byte UDP)
BRANCH AND MID RANGE BUNDLES
FortiGate FG/FWF-30G FG/FWF-50G FG-70G FG/FWF-80F FG-90G
FG-30G-BDL-809-DD FG-50G-BDL-809-DD FG-80F-BDL-809-DD
Enterprise Bundle FG-70G-BDL-809-DD FG-90G-BDL-809-DD
FWF-30G-code*-BDL-809-DD FWF-50G-code*-BDL-809-DD FWF-80F-code*-BDL-809-DD
Enterprise Renewal FC-10-0030G-809-02-DD FC-10-0050G-809-02-DD FC-10-0070G-809-02-DD FC-10-0080F-809-02-DD FC-10-0090G-809-02-DD
FortiGate Cloud alone FC-10-0030G-131-02-DD FC-10-0050G-131-02-DD FC-10-0070G-131-02-DD FC-10-0080F-131-02-DD FC-10-0090G-131-02-DD
SELECT BRANCH VARIANTS
Variant 51G Storage 71G Storage 81F storage 90G storage
Enterprise Bundle FG-51G-BDL-809-DD FG-71G-BDL-809-DD FG-81F-BDL-809-DD FG-91G-BDL-809-DD
Enterprise Renewal FC-10-0051G-809-02-DD FC-10-0071G-809-02-DD FC-10-0081F-809-02-DD FC-10-0091G -809-02-DD
FortiGate Cloud alone FC-10-0051G-131-02-DD FC-10-0071G-131-02-DD FC-10-0081F-131-02-DD FC-10-0091G -131-02-DD
Variant FortiWiFi 30G FortiWiFi 50G FortiWiFi 70G FortiWiFi 80F-2R
FWF-80F-2R-code*-BDL-
Enterprise Bundle FWF-30G-code*-BDL-809-DD FWF-50G-code*-BDL-809-DD FWF-70G-code*-BDL-809-DD
809-DD
Enterprise Renewal FC-10-W030G-809-02-DD FC-10-W050G-809-02-DD FC-10-W070G-809-02-DD FC-10-W080F-809-02-DD
FortiGate Cloud alone FC-10-W030G-131-02-DD FC-10-W050G-131-02-DD FC-10-W070G-131-02-DD FC-10-W080F-131-02-DD
Variant FortiWiFi 51G storage FortiWiFi 71G storage FortiGate 80F-PoE
FG-80F-POE-BDL-809-DD
Enterprise Bundle FWF-51G-code*-BDL-809-DD FWF-71G-code*-BDL-809-DD
FG-81F-POE-BDL-809-DD
FC-10-F80FP-809-02-DD.
Enterprise Renewal FC-10-W051G-809-02-DD FC-10-W071G-809-02-DD
FC-10-F81FP-809-02-DD
FC-10-F80FP-131-02-DD.
FortiGate Cloud alone FC-10-W051G-131-02-DD FC-10-W071G-131-02-DD
FC-10-F81FP-131-02-DD
* FortiWiFi country code suffix explanation.
A country code (-A, -B, -C, -D, -E, -F, -I, -J, -K, -N, -P, -S, -T, -U, -V, -W, or -Y) applies to all FortiWiFi models based upon country of deployment. Work with your local supplier for the
correct model in your regulatory domain.
10


**Table 10.1**

| FORTIGATE APPLIANCES | FG/FWF-30G | FG/FWF-50G | FG-70G | FG/FWF-80F | FG-90G |
| --- | --- | --- | --- | --- | --- |
| NGFW / PERIMETER FIREWALLS |  |  |  |  |  |


**Table 10.2**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
FortiGate Appliances
FORTIGATE
FG/FWF-30G FG/FWF-50G FG/FWF-70G FG/FWF-80F FG-90G
APPLIANCES
SELECT BRANCH VARIANTS
Variant FortiGate 50G-SFP-PoE FortiWiFi 81F-2R storage
FG-50G-SFP-POE-BDL- FWF-81F-2R-code*-BDL-
Enterprise Bundle
809-DD 809-DD
Enterprise Renewal FC-10-F50GP-809-02-DD FC-10-W081F-809-02-DD
FortiGate Cloud alone FC-10-F50GP-131-02-DD FC-10-W081F-131-02-DD
FortiGate 51G-SFP-PoE
Variant FortiWiFi 80F-PoE
storage
FG-51G-SFP-POE-BDL- FWF-81F-2R-POE-code*-
Enterprise Bundle
809-DD BDL- 809-DD
Enterprise Renewal FC-10-F51GP-809-02-DD FC-10-WP81F-809-02-DD
FortiGate Cloud alone FC-10-F51GP-131-02-DD FC-10-WP81F-131-02-DD
FORTIGATE
FG-120G FG-200G FG-400F FG-600F FG-900G FG-1000F
APPLIANCES
NGFW / PERIMETER FIREWALLS
Maximum FortiAPs
128 / 64 256 / 128 512 / 256 1024 / 512 2048 / 1024 4096 / 2048
(Total/Tunnel)
Max FortiSwitches 48 64 96 128 196 196
Firewall Throughput
39 / 39 / 28 Gbps 39 / 39 / 26.5 Gbps 78.5 / 78.5 / 70 Gbps 139 / 137.5 / 70 Gbps 164 / 163 / 153 Gbps 196 / 196 / 134 Gbps
(1518/512/64 byte UDP)
MID RANGE AND HIGH END BUNDLES
Enterprise Protection Bundle
Enterprise Bundle FG-120G-BDL-809-DD FG-200G-BDL-809-DD FG-400F-BDL-809-DD FG-600F-BDL-809-DD FG-900G-BDL-809-DD FG-1000F-BDL-809-DD
FC-10-F120G-809- FC-10-F200G-809- FC-10-0400F-809- FC-10-0600F-809- FC-10-FG9H0-809- FC-10-F1K0F-809-
Enterprise Renewal
02-DD 02-DD 02-DD 02-DD 02-DD 02-DD
FortiGate Cloud
FC-10-F200G-131- FC-10-FG9H0-131- FC-10-F1K0F-131- 02-
-Management, Analysis, FC-10-F120G-131-02-DD FC-10-0400F-131-02-DD FC-10-0600F-131-02-DD
02-DD 02-DD DD
1y Log Retention
Unified Threat Protection Bundle
UTP Bundle FG-120G-BDL-950-DD FG-200G-BDL-950-DD FG-400F-BDL-950-DD FG-600F-BDL-950-DD FG-900G -BDL-950-DD FG-1000F-BDL-950-DD
FC-10-F120G-950- FC-10-F200G-950- FC-10-0400F-950- FC-10-F6H0F-950- FC-10-F9H0G-950- FC-10-F1K0F-950-
UTP Bundle Renewal
02-DD 02-DD 02-DD 02-DD 02-DD 02-DD
FortiGate Cloud
FC-10-F200G-131- FC-10- F9H0G -131- FC-10-F1K0F-131- 02-
-Management, Analysis, FC-10-F120G-131-02-DD FC-10-0400F-131-02-DD FC-10-0600F-131-02-DD
02-DD 02-DD DD
1y Log Retention
* FortiWiFi country code explanation.
A country code (-A, -B, -C, -D, -E, -F, -I, -J, -K, -N, -P, -S, -T, -U, -V, -W, or -Y) applies to all FortiWiFi models based upon country of deployment. Work with your local supplier for the
correct model in your regulatory domain.
11


**Table 11.1**

| FORTIGATE APPLIANCES | FG/FWF-30G | FG/FWF-50G | FG/FWF-70G | FG/FWF-80F | FG-90G |
| --- | --- | --- | --- | --- | --- |
| SELECT BRANCH VARIANTS |  |  |  |  |  |


**Table 11.2**

| FORTIGATE APPLIANCES | FG-120G | FG-200G | FG-400F | FG-600F | FG-900G | FG-1000F |
| --- | --- | --- | --- | --- | --- | --- |
| NGFW / PERIMETER FIREWALLS |  |  |  |  |  |  |


**Table 11.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
FortiGate Appliances
FORTIGATE
FG-1800F FG-2600F FG-3000F FG-3200F FG-3500F
APPLIANCES
NGFW / PERIMETER FIREWALLS
Maximum FortiAPs (Total/
4096 / 2048 4096 / 2048 4096 / 2048 4096 / 2048 4096 / 2048
Tunnel)
Max FortiSwitches 196 196 300 300 300
Firewall Throughput
198 / 197 / 140 Gbps 198 / 196 / 120 Gbps 397 / 389 / 221 Gbps 387 / 385 / 178.5 Gbps 595 / 590 / 420 Gbps
(1518/512/64 byte UDP)
MID RANGE AND HIGH END BUNDLES
Enterprise Protection Bundle
Enterprise Bundle FG-1800F-BDL-809-DD FG-2600F-BDL-809-DD FG-3000F-BDL-809-DD FG-3200F-BDL-809-DD FG-3500F-BDL-809-DD
Enterprise Renewal FC-10-F18HF-809-02-DD FC-10-F26HF-809- 02-DD FC-10-F3K0F-809-02-DD FC-10-F3K2F-809-02-DD FC-10-F3K0F-809-02-DD
FortiGate Cloud
-Management, Analysis, 1y FC-10-F18HF-131-02-DD FC-10-F26HF-131-02-DD FC-10-F3K0F-131-02-DD FC-10-F3K2F-131-02-DD FC-10-F3K5F-131-02-DD
Log Retention
Unified Threat Protection Bundle
UTP Bundle FG-1800F-BDL-950-DD FG-2600F-BDL-950-DD FG-3000F-BDL-950-DD FG-3200F-BDL-950-DD FG-3500F-BDL-950-DD
UTP Bundle Renewal FC-10-F18HF-950- 02-DD FC-10-F26HF-950- 02-DD FC-10-F3K0F-950- 02-DD FC-10-F3K2F-950- 02-DD FC-10-F3K5F-950- 02-DD
FortiGate Cloud
-Management, Analysis, 1y FC-10-F18HF-131-02-DD FC-10-F26HF-131-02-DD FC-10-F3K0F-131-02-DD FC-10-F3K2F-131-02-DD FC-10-F3K5F-131-02-DD
Log Retention
FORTIGATE
FG-3700F FG-4200F FG-4400F
APPLIANCES
NGFW / PERIMETER FIREWALLS
Maximum FortiAPs (Total/Tunnel) 4096 / 2048 8192 / 4096 8192 / 4096
Max FortiSwitches 300 300 300
Firewall Throughput (1518/512/64 byte
589 / 589 / 420 Gbps 800 / 788 / 400 Gbps 1.15 / 1.14 / 0.5 Tbps
UDP)
MID RANGE AND HIGH END BUNDLES
Enterprise Protection Bundle
Enterprise Bundle FG-3600E-BDL-809-DD FG-4200F-BDL-809-DD FG-4400F-BDL-809-DD
Enterprise Renewal FC-10-F3K6E-809-02-DD FC-10-F42HF-809-02-DD FC-10-F44HF-809-02-DD
FortiGate Cloud -Management, Analysis, 1y
FC-10-F3K7F-131-02-DD n/a n/a
Log Retention
Unified Threat Protection Bundle
UTP Bundle FG-3600E-BDL-950-DD FG-4200F-BDL-950-DD FG-4400F-BDL-950-DD
UTP Bundle Renewal FC-10-F3K6E-950- 02-DD FC-10-F42HF-950-02-DD FC-10-F44HF-950-02-DD
FortiGate Cloud -Management, Analysis, 1y
FC-10-F3K7F-131-02-DD n/a n/a
Log Retention
* FortiWiFi country code explanation.
A country code (-A, -B, -C, -D, -E, -F, -I, -J, -K, -N, -P, -S, -T, -U, -V, -W, or -Y) applies to all FortiWiFi models based upon country of deployment. Work with your local supplier for the
correct model in your regulatory domain.
12


**Table 12.1**

| FORTIGATE APPLIANCES | FG-1800F | FG-2600F | FG-3000F | FG-3200F | FG-3500F |
| --- | --- | --- | --- | --- | --- |
| NGFW / PERIMETER FIREWALLS |  |  |  |  |  |


**Table 12.2**

| FORTIGATE APPLIANCES | FG-3700F | FG-4200F | FG-4400F |
| --- | --- | --- | --- |
| NGFW / PERIMETER FIREWALLS |  |  |  |


**Table 12.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
FortiGate VM Virtual Machines
FORTIGATE VM
VM-01S VM-02S VM-04S VM-08S
VIRTUAL MACHINES
NGFW / PERIMETER FIREWALLS
Maximum FortiAPs (Total/Tunnel) 64 / 32 1024 / 512 1024 / 512 4096 / 1024
Max FortiSwitches Implementation dependent Implementation dependent Implementation dependent Implementation dependent
Firewall Throughput (1518/512/64
12 Gbps 15 Gbps 28 Gbps 33 Gbps
byte UDP)
PRIVATE CLOUD
ATP bundle FC1-10-FGVVS-993-02-DD FC2-10-FGVVS-993-02-DD FC3-10-FGVVS-993-02-DD FC4-10-FGVVS-993-02-DD
UTP Bundle FC2-10-FGVVS-990-02-DD FC2-10-FGVVS-990-02-DD FC3-10-FGVVS-990-02-DD FC4-10-FGVVS-990-02-DD
Enterprise bundle FC2-10-FGVVS-814-02-DD FC2-10-FGVVS-814-02-DD FC3-10-FGVVS-814-02-DD FC4-10-FGVVS-814-02-DD
NB - FortiGate VM does not have a ForitGate Cloud option
FORTIGATE VM
VM-16S VM-32S VM-ULS
VIRTUAL MACHINES
NGFW / PERIMETER FIREWALLS
Maximum FortiAPs (Total/Tunnel) 4096 / 1024 4096 / 1024 4096 / 1024
Max FortiSwitches Implementation dependent Implementation dependent Implementation dependent
Firewall Throughput (1518/512/64 byte
36 Gbps 50 Gbps Resource dependent
UDP)
PRIVATE CLOUD
ATP bundle FC5-10-FGVVS-993-02-DD FC6-10-FGVVS-993-02-DD FC7-10-FGVVS-993-02-DD
UTP Bundle FC5-10-FGVVS-990-02-DD FC6-10-FGVVS-990-02-DD FC7-10-FGVVS-990-02-DD
Enterprise bundle FC5-10-FGVVS-814-02-DD FC6-10-FGVVS-814-02-DD FC7-10-FGVVS-814-02-DD
NB - FortiGate VM does not have a ForitGate Cloud option
13


**Table 13.1**

| FORTIGATE VM VIRTUAL MACHINES | VM-01S | VM-02S | VM-04S | VM-08S |
| --- | --- | --- | --- | --- |
| NGFW / PERIMETER FIREWALLS |  |  |  |  |


**Table 13.2**

| FORTIGATE VM VIRTUAL MACHINES | VM-16S | VM-32S | VM-ULS |
| --- | --- | --- | --- |
| NGFW / PERIMETER FIREWALLS |  |  |  |


**Table 13.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
FORTIAP
FORTIAP FAP-441K FAP-443K FAP-241K FAP-243K
STANDARD
Wi-Fi Generation 7 7 7 7
MIMO/Antennas 4x4, Internal 4x4 External 2x2, Internal 2x2 External
Use Indoor Indoor Indoor Indoor
Majority of clients Laptops, all Laptops, all Laptops, all Laptops, all
Radios 4 4 4 4
Ethernet ports 2x 10GE 2x 10GE 1x 10GE, 1x 1GE 1x 10GE, 1x 1GE
PoE (802.3xx) 1bt, or 2at 1bt, or 2at 1bt 1bt
Hardware FAP-441K-suffix* FAP-443K-suffix* FAP-241K-suffix* FAP-243K-suffix*
NB - no license required for
— — — —
FortiGate management
FortiEdge Cloud Management
(when NOT managed by FC-10-90AP1-639-02-DD FC-10-90AP1-639-02-DD FC-10-90AP1-639-02-DD FC-10-90AP1-639-02-DD
FortiGate)*
FortiCare Premium FC-10-FP41K-247-02-DD FC-10-FP43K-247-02-DD FC-10-FP21K-247-02-DD FC-10-FP23K-247-02-DD
FortiCare Elite FC-10-FP41K-284-02-DD FC-10-FP43K-284-02-DD FC-10-FP21K-284-02-DD FC-10-FP23K-284-02-DD
FortiCare Essential FC-10-FP41K-314-02-DD FC-10-FP43K-314-02-DD FC-10-P241K-314-02-DD FC-10-P243K-314-02-DD
* FortiCare is included in the FortiEdge Cloud Management license.
FORTIAP FAP-231K FAP-23JK
STANDARD
Wi-Fi Generation 7 7
MIMO/Antennas 2x2, Internal 2x2, Internal
Use Indoor Indoor wall plate
Majority of clients Laptops, all Hotel Rooms
Radios 3 3
Ethernet ports 1x5GE 1x10GE, 3xGE
PoE (802.3xx) 1at bt
Hardware FAP-231K-suffix FAP-23JK-suffix*
NB - no license required for FortiGate management
FortiEdge Cloud Management (when NOT managed by FC-10-90AP1-639-02-DD
FC-10-90AP1-639-02-DD
FortiGate)*
FortiCare Premium FC-10-P231K-247-02-DD FC-10-P23JK-247-02-DD
FortiCare Elite FC-10-P231K-284-02-DD FC-10-P23JK-284-02-DD
FortiCare Essential FC-10-P231K-314-02-DD FC-10-P23JK-314-02-DD
* FortiCare is included in the FortiEdge Cloud Management license.
14


**Table 14.1**

| FORTIAP | FAP-441K | FAP-443K | FAP-241K | FAP-243K |
| --- | --- | --- | --- | --- |
| STANDARD |  |  |  |  |


**Table 14.2**

| FORTIAP | FAP-231K | FAP-23JK |
| --- | --- | --- |
| STANDARD |  |  |


**Table 14.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
FortiAP
FORTIAP FAP-432G FAP-234G
STANDARD
Wi-Fi Generation 6E 6E
MIMO/Antennas 4x4 External 2x2, External
Use Outdoor Outdoor
Majority of clients Phones/Tablets, all Phones/Tablets, all
Radios 3 3
Ethernet ports 1 x 10GE, 1GE 1x 5GE, 1GE
PoE (802.3xx) bt bt
Hardware FAP-432G-suffix* FAP-234F-suffix*
NB - no license required for FortiGate management — —
FortiEdge Cloud Management (when NOT managed by
FC-10-90AP1-639-02-DD FC-10-90AP1-639-02-DD
FortiGate)*
FortiCare Premium FC-10-P432G-247-02-DD FC-10-P234G-247-02-DD
FortiCare Elite FC-10-P432G-284-02-DD FC-10-P234G-284-02-DD
FortiCare Essential FC-10-P432G-314-02-DD FC-10-P234G-314-02-DD
UTP Subscription FC-10-APGIS-768-02-DD FC-10-APGIS-768-02-DD
* FortiCare is included in the FortiEdge Cloud Management license.
FORTIAP FAP-831F FAP-432FR
STANDARD
Wi-Fi Generation 6 6
MIMO/Antennas 8x8, internal 4x4 External
Use stadium/auditorium Outdoor/Hazardous
Majority of clients Phones/Tablets, all Laptops, all
Radios 3 3
Ethernet ports 1 x 5GE, 1GE 1 x 2.5GE, 1GE
PoE (802.3xx) 2at/bt (30W) bt
Hardware FAP-831F-suffix* FAP-432FR-suffix*
NB - no license required for FortiGate management — —
FortiEdge Cloud Management (when NOT managed by
FC-10-90AP1-639-02-DD FC-10-90AP1-639-02-DD
FortiGate)*
FortiCare Premium FC-10-F831F-247-02-DD FC-10-PF432-247-02-DD
FortiCare Elite FC-10-P831F-284-02-DD FC-10-PF432-284-02-DD
FortiCare Essential FC-10-P831F-314-02-DD FC-10-FR432-314-02-DD
* FortiCare is included in the FortiEdge Cloud Management license.
* FortiAP country code explanation.
A country code (-A, -B, -C, -D, -E, -F, -I, -J, -K, -N, -P, -S, -T, -U, -V, -W, or -Y) applies to all FortiAP models based upon country
of deployment. Work with your local supplier for the correct model in your regulatory do-main.
** C1D2 certified for hazardous conditions.
15


**Table 15.1**

| FORTIAP | FAP-432G | FAP-234G |
| --- | --- | --- |
| STANDARD |  |  |


**Table 15.2**

| FORTIAP | FAP-831F | FAP-432FR |
| --- | --- | --- |
| STANDARD |  |  |


**Table 15.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
FortiAP
FORTIAP FAP-23JF
STANDARD
Wi-Fi Generation 6
MIMO/Antennas 2x2, Internal
Use Indoor wall plate
Majority of clients Hotel Rooms
Radios 3
Ethernet ports 4 x GE
PoE (802.3xx) at
Hardware FAP-23JF-suffix*
NB - no license required for FortiGate management —
FortiEdge Cloud Management (when NOT managed by FortiGate)* FC-10-90AP1-639-02-DD
FortiCare Premium FC-10-P23JF-247-02-DD
FortiCare Elite FC-10-P23JF-284-02-DD
FortiCare Essential FC-10-P23JF-314-02-DD
* FortiCare is included in the FortiEdge Cloud Management license.
* FortiAP country code suffix explanation.
A country code (-A, -B, -C, -D, -E, -F, -I, -J, -K, -N, -P, -S, -T, -U, -V, -W, or -Y) applies to all FortiAP models based upon country
of deployment. Work with your local supplier for the correct model in your regulatory domain.
16


**Table 16.1**

| FORTIAP | FAP-23JF |
| --- | --- |
| STANDARD |  |


**Table 16.2**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
FortiSwitch
FORTISWITCH 100 SERIES 200 SERIES 400 SERIES 500 SERIES 600 SERIES 1000 SERIES 2000 SERIES 3000 SERIES
Main Port Speed 1G/2.5G/5G 1 Gbps 1 Gbps 1 Gbps 1G/2.5G/5G 10/40 Gbps 10/25 Gbps 40/100 Gbps
Main Port Count
8, 24, 48 24, 48 24, 48 24, 48 24, 48 24, 48 48 32
Options
Uplink Port Speed 1 or 10 Gbps 1 Gbps 10 Gbps 10 Gbps 25 Gbps 40 or 100 Gbps 40 or 100 Gbps n/a
Redundant Power
n/a Some Models Some Models Optional PSU Yes Yes Yes Yes
Supplieas
PoE Options Yes Yes Yes Yes Yes Yes n/a n/a
EXAMPLES FULL POE FORTISWITCHES
8-port FPoE
Hardware Bundle FS-108F-FPOE
FC-10-F108F-247-
FortiCare Premium
02-DD
FC-10-F108F-284-
FortiCare Elite
02-DD
FortiCare FC-10-F108F-314-
Essential 02-DD
10-port FPoE
Hardware Bundle FS-110G-FPOE
FC-10-M10GF-
FortiCare Premium
247-02-DD
FC-10-M10GF-
FortiCare Elite
284-02-DD
FortiCare FC-10-M10GF-
Essential 314-02-DD
24-port FPoE
FS-124F-FPOE
Hardware Bundle FS-224D-FPOE FS-M426E-FPOE FS-624F-FPOE FS-T1024F-FPOE
FS-124G-FPOE
FC-10-S124F-247-
02-DD FC-10-W0226- FC-10-M426E- FC-10-624FF-247- FC-10-TF124-247-
FortiCare Premium
FC-10-S24GF- 247-02-DD 247-02-DD 02-DD 02-DD
247-02-DD
FC-10-S124F-284-
02-DD FC-10-W0226- FC-10-M426E- FC-10-624FF-284- FC-10-TF124-284-
FortiCare Elite
FC-10-S24GF- 284-02-DD 284-02-DD 02-DD 02-DD
284-02-DD
FC-10-S124F-314-
FortiCare 02-DD FC-10-W0226- FC-10-M426E- FC-10-624FF-314- FC-10-TF124-314-
Essential FC-10-S24GF- 314-02-DD 314-02-DD 02-DD 02-DD
314-02-DD
48-port FPoE
Hardware Bundle FS-148F-FPOE FS-248E-FPOE FS-448E-FPOE FS-548D-FPOE FS-648F-FPOE
FC-10-148FF-247- FC-10-W248E- FC-10-S448F- FC-10-W0501- FC-10-648FF-247-
FortiCare Premium
02-DD 247-02-DD 247-02-DD 247-02-DD 02-DD
FC-10-148FF-284- FC-10-W248E- FC-10-S448F- FC-10-W0501- FC-10-648FF-
FortiCare Elite
02-DD 284-02-DD 284-02-DD 284-02-DD 284-02-DD
FortiCare FC-10-148FF-314- FC-10-W248E- FC-10-S448F-314- FC-10-W0501- FC-10-648FF-314-
Essential 02-DD 314-02-DD 02-DD 314-02-DD 02-DD
17


**Table 17.1**

| FORTISWITCH | 100 SERIES | 200 SERIES | 400 SERIES | 500 SERIES | 600 SERIES | 1000 SERIES | 2000 SERIES | 3000 SERIES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |


**Table 17.2**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
FORTISWITCH 100 SERIES 200 SERIES 400 SERIES 500 SERIES 600 SERIES 1000 SERIES 2000 SERIES 3000 SERIES
NB - no license
required for
— — — — — — — —
FortiGate
management
FortiEdge Cloud
Management
FC-10-FSW00- FC-10-FSW10- FC-10-FSW10- FC-10-FSW20- FC-10-FSW20- FC-10-FSW30- FC-10-FSW30- FC-10-FSW30-
(when not
628-02-DD 628-02-DD 628-02-DD 628-02-DD 628-02-DD 628-02-DD 628-02-DD 628-02-DD
managed by
FortiGate)
FortiCare when
managed by FortiCare included in the FortiEdge Cloud license.1
FortiEdge Cloud
1 FortiCare only applicable when used with FortiEdge Cloud
For additional models, accessories, and advanced licenses, please see the FortiSwitch Ordering Guide: https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/og-fortiswitch.pdf.
Additional Secure LAN Management Products
PRODUCT DESCRIPTION SKU LICENSE
FORTIGATE CLOUD / FORTIEDGE CLOUD - MULTI TENANCY ACCOUNT
FortiGate Cloud or FortiEdge Cloud Multi Tenancy service for a Managed Service Provider (MSP) to create and manage FCLE-10-FCLD0-161-02-DD
multiple SubAccounts.
FORTIAIOPS MONITORING
FortiAIOps Monitoring subscription for 25 extension device. Includes FortiCare Premium FC1-10-AOVMS-668-01-DD
FortiAIOps Monitoring subscription for 25 extension device. Includes FortiCare Premium FC2-10-AOVMS-668-01-DD
FortiAIOps Monitoring subscription for 25 extension device. Includes FortiCare Premium FC3-10-AOVMS-668-01-DD
FortiAIOps Monitoring subscription for 25 extension device. Includes FortiCare Premium FC4-10-AOVMS-668-01-DD
FORTIAIOPS AI INSIGHTS
FortiAIOps AI Insights subscription for 25 extension device. Includes FortiCare Premium
FortiAIOps AI Insights subscription for 25 extension device. Includes FortiCare Premium
FortiAIOps AI Insights subscription for 25 extension device. Includes FortiCare Premium
FortiAIOps AI Insights subscription for 25 extension device. Includes FortiCare Premium
FORTIAIOPS MONITORING AND AI INSIGHTS
FortiAIOps Monitoring & AI Insights subscription for 25 extension device. Includes FortiCare Premium FC1-10-AOVMS-670-01-DD
FortiAIOps Monitoring & AI Insights subscription for 25 extension device. Includes FortiCare Premium FC2-10-AOVMS-670-01-DD
FortiAIOps Monitoring & AI Insights subscription for 25 extension device. Includes FortiCare Premium FC3-10-AOVMS-670-01-DD
FortiAIOps Monitoring & AI Insights subscription for 25 extension device. Includes FortiCare Premium FC4-10-AOVMS-70-01-DD
TRAINING SERVICES
NSE 6/Secure Wireless LAN (FortiWiFi, FortiGate, FortiAP) FT-FWF
NSE 6 Exam Voucher NSE-EX-SPL6
NSE 6 Exam Bundle NSE-EX-BUN6
ADDITIONAL ORDERING GUIDES
All https://www.fortinet.com/resources/ordering-guides
NGFW https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/og-next-generation-firewall.pdf
FortiAP https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/og-wireless.pdf
FortiSwitch https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/og-fortiswitch.pdf
FortiEdge Cloud https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/og-fortiedge.pdf
Visit https://www.fortinet.com/resources/ordering-guides for related ordering guides.
18


**Table 18.1**

| FORTISWITCH | 100 SERIES | 200 SERIES | 400 SERIES | 500 SERIES | 600 SERIES | 1000 SERIES | 2000 SERIES | 3000 SERIES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |


**Table 18.2**

| PRODUCT | DESCRIPTION | SKU LICENSE |
| --- | --- | --- |
| FORTIGATE CLOUD / FORTIEDGE CLOUD - MULTI TENANCY ACCOUNT |  |  |


**Table 18.3**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
Frequently Asked Questions
What makes a FortiGate a Secure LAN Controller?
A FortiGate combines security enforcement, FortiAP management, FortiSwitch management and secure network fabric traffic
into a unified whole — Security Driven Networking. Security is enforced not only at the perimeter, but extended out to the edge
of the network — where the clients connect to FortiAPs and FortiSwitches.
What is the difference between FortiGate Cloud and FortiEdge Cloud?
With FortiGate as a Secure LAN Controller it manages the on-site FortiAPs and FortiSwitches, so FortiGate Cloud manages the
Secure LAN devices via the managed FortiGate. For locations that need Fortinet Secure LAN devices that are not associated
with a FortiGate (for whatever reason), FortiEdge Cloud can directly manage the FortiAPs and FortiSwitches.
How can an MSSP use FortiGate or FortiEdge Cloud with multiple customers?
They can add a multi-tenancy license to either, which will enable the creation of sub-accounts with full data isolation.
What are typical licenses for customer deployments with NGFW with FortiGates?
The Unified Threat Protection (UTP) and the Enterprise bundles, which provide extensive coverage for device-, content-, and
web-based threats, comprehensively cover most customer use cases.
See FortiGuard Security Services here.
What does the Enterprise bundle include?
• The Enterprise bundle includes IPS, Advanced Malware Protection, Application Control, URL, DNS and Video Filtering,
Antispam, Security Rating, IoT Detection, Industrial Security, FortiConverter Service, and FortiCare Premium
• FortiGate cloud must be added when purchasing enterprise bundle
What does the UTP license include?
• The UTP license includes IPS, advanced malware protection, application control, botnet DB, mobile malware, outbreak
prevention, web and video filtering, Cloud Sandbox, secure DNS filtering, antispam service, and 24x7 support. For more
information click here.
• FortiGate Cloud would need to be added
Why the difference between “Tunnel vs Total” FortiAPs?
On a per SSID basis, FortiAPs can tunnel traffic back to the FortiGate for a full security stack inspection – the default behavior.
However, some customer environments may have a need for local-only Wi-Fi or low inspection guest traffic. Under such
circumstances, more FortiAPs.
How do I license FortiAPs and FortiSwitches on the FortiGate?
No need. There are no licensing limits for on any FortiGate for Secure LAN devices. Each one comes out of the box able to
manage the full number of FortiAPs and FortiSwitches, with only the hardware-based limits above.
How many FortiAPs does my customer need?
Every physical site is different. Any FortiAP deployment should have a site survey and a wireless deployment plan from a capable
Wi-fi engioneer to insure good coverage and performance over a site. As an estimate for planning purposes, most sites require
approximately one for FortiAP for 1500 sq ft (150 sq m) and about 60 active devices per FortiAP (30 devices per service radio).
19


**Table 19.1**

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |

FortiGate Secure LAN Controller Ordering Guide
What is the difference between 4x4 vs 2x2?
MIMO is a feature of Wi-Fi that uses multiple antennas to send simultaneous signals and so increase throughput. However,
the number of antennas must align on both the client and the FortiAP to maximize the potential benefits. Phones and tablets
normally have one antenna, at most two, and so cannot take significant advantage of a 4x4 FortiAP vs a 2x2, while laptops,
which usually have three antennas, get a significant boost from a 4x4 FortiAP. Of course, all FortiAPs work with all Wi-Fi
client devices, so sometimes budget is the deciding factor or 2x2 performance is plenty. The FAP-831F is an 8x8 FortiAP
that supports Multi-User MIMO, able to divide its multiple traffic streams among clients simultaneous, boosting total Wi-Fi
performance and is meant for high density environments such as auditoriums and stadiums.
www.fortinet.com
Copyright © 2026 Fortinet, Inc. All rights reserved. Fortinet®, FortiGate®, FortiCare® and FortiGuard®, and certain other marks are registered trademarks of Fortinet, Inc., and other Fortinet names herein may also be registered and/or common law trademarks of Fortinet. All other product or
company names may be trademarks of their respective owners. Performance and other metrics contained herein were attained in internal lab tests under ideal conditions, and actual performance and other results may vary. Network variables, different network environments and other condi-
tions may affect performance results. Nothing herein represents any binding commitment by Fortinet, and Fortinet disclaims all warranties, whether express or implied, except to the extent Fortinet enters a binding written contract, signed by Fortinet’s SVP Legal and above, with a purchaser
that expressly warrants that the identified product will perform according to certain expressly-identified performance metrics and, in such event, only the specific performance metrics expressly identified in such binding written contract shall be binding on Fortinet. For absolute clarity, any
such warranty will be limited to performance in the same ideal conditions as in Fortinet’s internal lab tests. Fortinet disclaims in full any covenants, representations, and guarantees pursuant hereto, whether express or implied. Fortinet reserves the right to change, modify, transfer, or otherwise
revise this publication without notice, and the most current version of the publication shall be applicable.
SLC-OG-R13-20260408
