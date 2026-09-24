# Daily Threat Intel Report
**Date:** September 24, 2026

🔴 **Threat Score:** 86/100
*(Auditable Metrics - Threat Capability: 8/10 | Event Frequency: 9/10 | Business Impact: 9/10)*

**Executive Summary - Incidents:**
* Revolut Customer Data Breach via Impersonated Government Requests and Subsequent Phishing Campaign
* "Dark Sourcery" Threat Actors Poison OpenAI and Google AI Chatbots Targeting Chase and Bank of America
* Active Exploitation of Check Point VPN and Management Server Zero-Days (CVE-2026-85102, CVE-2026-93616)
* Threat Actors Exploit F5 BIG-IP APM OAuth Zero-Day (CVE-2026-94127) for Remote Code Execution
* N-able Patches Maximum Severity Pre-Authentication RCE (CVE-2026-86218) in N-central Platform

---

## Revolut Customer Data Breach via Impersonated Government Requests and Subsequent Phishing Campaign
**Incident Metadata:**
* **Primary Category:** DATA LEAK
* **News Nature:** New Attack / Post-mortem
* **Timeline:** Incident Date: Early September 2026 | Source Publication Date: September 21, 2026
* **Impacted Country:** Global
* **Geolocation / Cloud Region:** Lithuania / European Economic Area (EEA)
* **List of Companies Impacted:** Revolut, Italian Ministry of the Interior

**Overview**
Revolut, a major digital banking platform regulated in Lithuania, fell victim to an advanced external impersonation scam that compromised 0.16% of its customer base (approximately 50,150 individuals, including 20,687 in the EEA), specifically targeting high-net-worth cryptocurrency holders. Threat actors successfully bypassed standard internal compliance verification controls by submitting fraudulent Know Your Customer (KYC) and data extraction requests using legitimate, compromised email accounts belonging to the Italian Ministry of the Interior. Starting September 14, 2026, these actors leveraged the exfiltrated data to execute a highly credible SMS phishing (smishing) campaign designed to harvest full login credentials and defeat biometric liveness checks.

**The Breach Mechanism**
* **Exploitation of Law Enforcement Trust Mechanisms:** Threat actors initially compromised official Italian government email infrastructure using credentials harvested from infostealer malware logs. Utilizing these authenticated domain accounts, they submitted fraudulent European Investigation Orders (EIOs) to Revolut's compliance department. Because the emails passed DMARC and SPF checks, Revolut employees processed them as legitimate law enforcement activities.
* **SMS Thread Hijacking and Liveness Bypass:** Following the exfiltration, attackers initiated a targeted smishing campaign. Utilizing SMS spoofing, malicious messages appeared within the exact same conversational thread as historic Revolut notifications. Victims clicking the links were redirected to a fraudulent web application that requested camera access, fabricating a live-video identity check to harvest biometric media and plaintext passwords.

**Impact and Consequences**
* **Systemic Reputational and Regulatory Damage:** The breach exposes fundamental flaws in the manual verification of third-party data requests. Under GDPR and DORA, the failure to authenticate inbound government requests introduces massive regulatory liability.
* **Long-Term Identity Theft and Account Takeover Risks:** The threat actors successfully exfiltrated complete identity kits. The granularity of the stolen data provides attackers with the exact collateral required to socially engineer telecommunications providers (SIM swapping) or defeat secondary banking verification protocols.

**Proposed Control: Mitigating Threats**
* **I. Governance & Containment (Prevention):** Mandate out-of-band verification protocols (e.g., secure portal communication, direct legal counsel liaison) for all inbound law enforcement and government data requests.
* **II. Identity & Access Management (Containment):** Implement continuous behavioral biometric profiling during the authentication lifecycle to detect anomalies indicative of injected or hijacked biometric video streams.
* **III. Infrastructure Intelligence (Detection):** Deploy advanced mobile threat defense (MTD) SDKs within the core banking application to detect concurrent SMS spoofing attempts.
* **IV. Operational Resilience:** Establish a rapid-response data quarantine protocol that instantly forces password resets and flags accounts queried by a compromised external entity.
* **V. Simulation environment:** Conduct quarterly red-team exercises simulating authenticated compliance channel hijacking.

**Conclusion**
The Revolut incident illustrates a paradigm shift where attackers bypass hardened technical perimeters by exploiting the legal and compliance obligations of financial institutions. By weaponizing the inherent trust in sovereign government communications, threat actors have established a highly effective pathway to orchestrate large-scale account takeovers.

**Further Reading**
https://www.infosecurity-magazine.com/news/revolut-customers-targeted-wave/

---

## "Dark Sourcery" Threat Actors Poison OpenAI and Google AI Chatbots Targeting Chase and Bank of America
**Incident Metadata:**
* **Primary Category:** AI
* **News Nature:** New Attack
* **Timeline:** Incident Date: September 2026 | Source Publication Date: September 23, 2026
* **Impacted Country:** Global
* **Geolocation / Cloud Region:** Global
* **List of Companies Impacted:** OpenAI, Google, Chase, Bank of America, Delta, Lufthansa, Qatar Airways, Airbnb, TripAdvisor

**Overview**
A massive, ongoing disinformation and phishing campaign dubbed "Dark Sourcery" has successfully poisoned the retrieval mechanisms of major AI chatbots, including ChatGPT, Google Gemini, and Google AI Overview, forcing them to serve malicious links and fraudulent support numbers directly to users interacting with major banking and travel brands.

**The Breach Mechanism**
* **Exploitation of AI Source Authority:** Attackers utilized advanced SEO and content-distribution techniques to seed malicious data across high-authority domains (.edu, .gov). AI models, algorithmically weighted to trust information originating from authoritative entities, ingested the poisoned data as highly credible factual knowledge.
* **Bypassing Instruction-Level Defenses:** Unlike traditional prompt injection attacks, this attack is completely passive. The model natively retrieves the poisoned data during its background web search and embeds the fraudulent contact details directly into the conversational output, bypassing all instruction-level AI defenses.

**Impact and Consequences**
* **High-Fidelity Social Engineering at Scale:** Over 90% of users blindly trust AI-generated answers without verifying sources. Victims dialing the AI-provided fraudulent phone numbers have their credit card details systematically harvested.
* **Brand Reputation and Liability Crisis:** Financial institutions face immense reputational damage as their customers are directly defrauded by trusted, centralized AI platforms. External brand integrity is now subject to automated manipulation outside the bank's traditional perimeter.

**Proposed Control: Mitigating Threats**
* **I. Governance & Containment (Prevention):** Legal and brand protection teams must aggressively monitor major AI platforms for hallucinations regarding the bank's customer service channels, initiating immediate takedown requests.
* **II. Identity & Access Management (Containment):** Enhance in-app authenticated communication channels, educating the customer base to only use the secure mobile banking application for support.
* **III. Infrastructure Intelligence (Detection):** Deploy autonomous digital risk protection (DRP) agents that continuously query public LLMs to detect poisoned contact information in real-time.
* **IV. Operational Resilience:** Integrate dynamic warning banners across all customer-facing digital properties explicitly advising users against relying on third-party AI chatbots.
* **V. Simulation environment:** Test internal enterprise RAG systems against "Dark Sourcery" style data poisoning by deliberately injecting contradictory information into the internal knowledge base.

**Conclusion**
The "Dark Sourcery" campaign proves that the integrity of AI-generated knowledge is highly susceptible to external manipulation, shifting the attack surface for social engineering directly into the algorithmic reasoning of the chatbot.

**Further Reading**
https://www.darkreading.com/threat-intelligence/attackers-manipulate-ai-chatbots-mass-disinformation-phishing-campaign

---

## Active Exploitation of Check Point VPN and Management Server Zero-Days (CVE-2026-85102, CVE-2026-93616)
**Incident Metadata:**
* **Primary Category:** CRITICAL INFRASTRUCTURE
* **News Nature:** Patch Update / New Attack
* **Timeline:** Incident Date: July 23 - September 12, 2026 | Source Publication Date: September 22, 2026
* **Impacted Country:** Global
* **Geolocation / Cloud Region:** Unknown
* **List of Companies Impacted:** Check Point Software, Global Enterprise Customers

**Overview**
Check Point Software released emergency hotfixes for two critical, actively exploited zero-day vulnerabilities affecting its Security Gateway VPN and Security Management Server products. The flaws allow unauthenticated remote attackers to execute arbitrary code and upload malicious scripts, leading to full systemic network compromise.

**The Breach Mechanism**
* **Pre-Authentication Path Traversal (CVE-2026-93616):** Unauthenticated attackers upload and execute arbitrary scripts on port TCP/19009 by sending anomalous login requests featuring massively padded username strings exceeding 1,000 characters.
* **VPN Certificate Handling RCE (CVE-2026-85102):** By routing traffic through proxy networks and leveraging specifically crafted certificates, attackers achieved remote code execution prior to any authentication mechanism, bypassing MFA prompts.

**Impact and Consequences**
* **Total Security Perimeter Collapse:** The compromise of a Security Management Server allows threat actors to arbitrarily modify firewall rules, intercept clear-text traffic, deploy malicious firmware updates, and pivot directly into the internal corporate network.
* **Widespread Exploitation Campaign:** The dual-pronged approach of targeting both the VPN gateway and the centralized management console maximizes the probability of establishing persistent, highly privileged access.

**Proposed Control: Mitigating Threats**
* **I. Governance & Containment (Prevention):** Immediately apply Check Point LivePatch Take 26 (or subsequent Jumbo Hotfixes) across all supported gateways. If impossible, disable VPN implied rules.
* **II. Identity & Access Management (Containment):** Ensure that access to the Security Management Server (TCP/19009) is strictly limited to heavily authenticated, internal administration subnets via jump hosts with mandatory MFA.
* **III. Infrastructure Intelligence (Detection):** Query SIEM platforms for anomalous login requests exceeding 1,000 characters in the cpm.elg logs.
* **IV. Operational Resilience:** Segment the management plane from the data plane across all critical security appliances.
* **V. Simulation environment:** Conduct assumed-breach tabletop exercises detailing the immediate revocation and rebuilding of the entire perimeter security policy.

**Conclusion**
The concurrent active exploitation of both the enforcement gateway and the central management server represents a worst-case scenario for enterprise perimeter defense.

**Further Reading**
https://www.bleepingcomputer.com/news/security/check-point-warns-of-hackers-exploiting-security-gateway-vpn-rce-flaw/

---

## Threat Actors Exploit F5 BIG-IP APM OAuth Zero-Day (CVE-2026-94127) for Remote Code Execution
**Incident Metadata:**
* **Primary Category:** CRITICAL INFRASTRUCTURE
* **News Nature:** New Attack
* **Timeline:** Incident Date: September 2026 | Source Publication Date: September 23, 2026
* **Impacted Country:** Global
* **Geolocation / Cloud Region:** Unknown
* **List of Companies Impacted:** F5 Networks, Global Enterprise Customers

**Overview**
F5 Networks disclosed a critical zero-day vulnerability (CVE-2026-94127) within its BIG-IP Access Policy Manager (APM) module, which is being actively exploited in the wild to achieve Remote Code Execution (RCE) on enterprise networks. The flaw is specifically triggered in environments where the APM is configured to act as an OAuth Authorization Server.

**The Breach Mechanism**
* **OAuth Profile Exploitation:** Threat actors exploit this configuration by sending maliciously crafted, oversized network requests that trigger a heap-based buffer overflow in the memory space allocated for the OAuth transaction. This allows the attacker to execute arbitrary commands at the system level or trigger a fatal abort signal (TMM SIGABRT).

**Impact and Consequences**
* **Authentication Proxy Compromise:** By hijacking the OAuth token generation process, attackers can mint golden tickets, effectively bypassing all primary enterprise authentication checks and assuming the identity of any user in the network.
* **Widespread Denial of Service:** In high-availability banking environments, repeated crashes of the APM module will result in a catastrophic denial of service.

**Proposed Control: Mitigating Threats**
* **I. Governance & Containment (Prevention):** Immediately deploy the official F5 security updates or directly apply the F5-provided mitigation iRule to all affected virtual servers.
* **II. Identity & Access Management (Containment):** Audit all BIG-IP APM configurations. Instances operating as an OAuth Authorization Server must be tightly monitored or temporarily isolated behind additional WAF inspection layers.
* **III. Infrastructure Intelligence (Detection):** Configure SIEM rules to alert on the sequence of multiple OAuth authentication failures immediately followed by TMM SIGABRT core dump events.
* **IV. Operational Resilience:** Ensure robust High Availability (HA) failover clustering is active, and configure rate-limiting on inbound OAuth requests.
* **V. Simulation environment:** Replicate the OAuth authorization flow within a staging environment to safely test the performance and stability impacts of the mitigation iRule.

**Conclusion**
Defending edge access devices requires a zero-tolerance policy for unpatched vulnerabilities, as they represent the single point of failure for zero-trust architectures.

**Further Reading**
https://www.bleepingcomputer.com/news/security/f5-warns-of-big-ip-apm-remote-code-execution-zero-day-exploited-in-attacks/

---

## N-able Patches Maximum Severity Pre-Authentication RCE (CVE-2026-86218) in N-central Platform
**Incident Metadata:**
* **Primary Category:** SUPPLY CHAIN
* **News Nature:** Patch Update
* **Timeline:** Incident Date: September 6, 2026 | Source Publication Date: September 7, 2026
* **Impacted Country:** Global
* **Geolocation / Cloud Region:** Unknown
* **List of Companies Impacted:** N-able, Managed Service Providers (MSPs)

**Overview**
N-able released an emergency hotfix to address a maximum-severity (CVSS 10) Remote Code Execution vulnerability in its N-central remote monitoring and management (RMM) platform, posing an imminent threat to global IT supply chains.

**The Breach Mechanism**
* **Pre-Authentication Remote Code Execution:** The vulnerability allows an entirely unauthenticated, remote attacker to execute arbitrary code directly on the central N-central server without user interaction.
* **Complete Infrastructure Subversion:** Because the N-central server maintains persistent, highly privileged administrative connections to thousands of downstream client endpoints, achieving RCE provides the attacker with automatic access to deploy payloads simultaneously.

**Impact and Consequences**
* **Cascading Supply Chain Compromise:** A compromise of the RMM server allows threat actors to mass-deploy ransomware to all downstream clients, utilizing the MSP as a distribution conduit.
* **Bypass of Perimeter Defenses:** The administrative tunnel created by the RMM agent inherently bypasses downstream client firewalls.

**Proposed Control: Mitigating Threats**
* **I. Governance & Containment (Prevention):** Mandate immediate cryptographic verification that N-central 2026.3 Hotfix 4 has been successfully deployed.
* **II. Identity & Access Management (Containment):** Restrict internet exposure of the N-central web interface and implement strict IP allow-listing.
* **III. Infrastructure Intelligence (Detection):** Monitor child processes spawned by the N-central agent (N-able.exe) on all banking endpoints.
* **IV. Operational Resilience:** Enforce stringent vendor risk management (VRM) policies requiring rapid SBOM and patch compliance disclosure.
* **V. Simulation environment:** Conduct purple-team exercises simulating an RMM supply-chain compromise.

**Conclusion**
Securing the enterprise requires rigorous policing of the administrative tools used by third-party vendors, as trust is the most exploited vulnerability.

**Further Reading**
https://www.infosecurity-magazine.com/news/nable-hotfix-critical-rce/
