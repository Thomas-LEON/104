# Daily Threat Intel Report
**Date:** September 24, 2026

🟠 **Threat Score:** 73/100
*(Auditable Metrics - Threat Capability: 8/10 | Event Frequency: 6/10 | Business Impact: 8/10)*

**Executive Summary - Incidents:**
* Threat Actors Exploit F5 BIG-IP APM OAuth Zero-Day (CVE-2026-94127) for Remote Code Execution
* "Dark Sourcery" Threat Actors Poison OpenAI and Google AI Chatbots Targeting Chase and Bank of America
* Compromised MemTensor Packages Deliver sckit Credential Stealer via npm and PyPI
* Malicious AI Agents Steal 600K Credit Cards and Infect 100+ Sites

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

## Compromised MemTensor Packages Deliver sckit Credential Stealer via npm and PyPI
**Incident Metadata:**
* **Primary Category:** SUPPLY CHAIN
* **News Nature:** New attack
* **Timeline:** Incident Date: September 2026 | Source Publication Date: September 23, 2026
* **Impacted Country:** Global
* **Geolocation / Cloud Region:** npm and PyPI repositories
* **List of Companies Impacted:** MemTensor (package maintainers)

**Overview**
Threat actors compromised legitimate MemTensor packages on npm and PyPI to distribute a Go-based credential stealer named "sckit". This malware targets Windows, Linux, and macOS environments to exfiltrate sensitive data.

**The Breach Mechanism**
* **Repository Poisoning:** Attackers gained unauthorized access to the MemTensor account or infrastructure to push malicious versions of the `@memtensor/memos-cloud-openclaw-plugin` package to npm and PyPI.
* **Cross-Platform Payload:** The "sckit" implant is designed to execute on multiple operating systems, leveraging the trust inherent in software supply chains to deliver malware to developers and automated build systems.

**Impact and Consequences**
* **Credential Theft:** The malware is specifically engineered to harvest credentials, potentially leading to lateral movement within corporate networks.
* **Supply Chain Contamination:** Downstream users who updated their dependencies automatically may have inadvertently executed the malicious code within their CI/CD pipelines.

**Proposed Control: Mitigating Threats**
* **I. Governance & Containment (Prevention):** Implement strict dependency pinning and hash verification for all third-party packages.
* **II. Identity & Access Management (Containment):** Enforce Multi-Factor Authentication (MFA) for all developer accounts with publishing rights to public repositories.
* **III. Infrastructure Intelligence (Detection):** Deploy automated Software Composition Analysis (SCA) tools to scan for anomalous code changes in dependencies.
* **IV. Operational Resilience:** Isolate build environments from the production network to limit the blast radius of compromised dependencies.
* **V. Simulation environment:** Conduct regular "Dependency Confusion" and "Supply Chain" attack simulations to test detection capabilities.

**Conclusion**
This incident highlights the persistent risk of supply chain attacks targeting open-source repositories. Organizations must treat third-party code as untrusted and implement rigorous validation processes.

**Further Reading**
https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html

---

## Malicious AI Agents Steal 600K Credit Cards and Infect 100+ Sites
**Incident Metadata:**
* **Primary Category:** AI
* **News Nature:** New attack
* **Timeline:** Incident Date: September 2026 | Source Publication Date: September 23, 2026
* **Impacted Country:** Global
* **Geolocation / Cloud Region:** Unknown
* **List of Companies Impacted:** 100+ online retailers

**Overview**
A financially motivated threat actor is utilizing open-source AI agent frameworks to automate the infection of online retail websites with digital skimmers, resulting in the theft of over 600,000 credit card records.

**The Breach Mechanism**
* **AI-Driven Automation:** The attackers weaponized autonomous AI agents to automate the reconnaissance and exploitation phases, significantly increasing the speed and scale of the campaign to identify vulnerabilities in more than 100 e-commerce platforms.
* **Digital Skimming:** Once a site is compromised, the agents inject scripts designed to intercept and exfiltrate payment information entered by customers during checkout.

**Impact and Consequences**
* **Massive Data Theft:** The exfiltration of 600,000 credit card records represents a significant financial and regulatory risk for the affected retailers and their payment processors.
* **Operational Disruption:** Affected sites must undergo extensive remediation to remove the malicious scripts and ensure the integrity of their payment processing systems.

**Proposed Control: Mitigating Threats**
* **I. Governance & Containment (Prevention):** Implement Content Security Policy (CSP) headers to restrict the execution of unauthorized scripts on payment pages.
* **II. Identity & Access Management (Containment):** Restrict administrative access to e-commerce platforms and enforce strict API key management.
* **III. Infrastructure Intelligence (Detection):** Deploy real-time monitoring for unauthorized changes to website source code and outbound network traffic.
* **IV. Operational Resilience:** Maintain offline backups of website configurations to facilitate rapid recovery in the event of a compromise.
* **V. Simulation environment:** Use AI-based security agents to perform red-teaming exercises against the organization's own web infrastructure.

**Conclusion**
The weaponization of AI agents for large-scale cybercrime marks a significant evolution in the threat landscape, requiring more proactive and automated defense mechanisms.

**Further Reading**
https://www.bleepingcomputer.com/news/security/malicious-ai-agents-steal-600k-credit-cards-infect-100-plus-sites-with-skimmers/
