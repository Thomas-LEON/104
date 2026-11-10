# Threat Intelligence Report: Autonomous Red Teaming Execution (ARTEX) Abuse

Between August and November 2026, multiple state-sponsored and cybercriminal threat groups weaponized ARTEX (Autonomous Red Teaming Execution)—an open-source, artificial-intelligence-driven offensive agent framework—to execute fully automated credential harvesting, supply chain compromises, and intrusion campaigns against hundreds of global enterprises at machine speed.

---

## What Happened

On July 26, 2026, an open-source software developer using the pseudonym "Autumn-27" published the ARTEX framework under the Affero General Public License version 3 (AGPLv3) on GitHub. Written in the Go programming language with an embedded Next.js User Interface (UI), ARTEX was designed to conduct automated penetration testing using the Norma agent Software Development Kit (SDK) and a dual-graph memory structure (Asset Graph and Exploration Graph) to execute multi-step attack planning. Starting in August 2026, malicious threat actors modified this codebase, connecting it to commercial Large Language Model (LLM) Application Programming Interfaces (APIs)—including DeepSeek v4.1-flash, Grok, and Claude—to execute unattended, high-tempo intrusions.

### Confirmed Facts
* **Chronological Milestones (July 26 – November 9, 2026):**
  * **July 26, 2026:** Developer Autumn-27 released the ARTEX repository publicly on GitHub.
  * **August 2026:** Threat actors initiated early reconnaissance by directing ARTEX agents to scrape public GitHub repositories for hardcoded cloud credentials and access keys.
  * **October 8, 2026:** Following emerging reports of widespread exploitation, developer Autumn-27 posted a disclaimer disavowing malicious usage and made the GitHub repository private. By that date, third parties had generated more than 12,000 forks and independent derivatives.
  * **October 15–16, 2026:** The China-nexus threat actor tracked by Microsoft as Storm-0940 weaponized ARTEX to exploit compromised application credentials originating from ConnectWise Cloud Backup. Storm-0940 automated sign-ins and role escalations across more than 2,250 downstream Microsoft 365 customer tenants.
  * **October 17–28, 2026:** The China-nexus cyber espionage group tracked by CrowdStrike as VAPOR PANDA deployed ARTEX in an 11-day campaign targeting more than 200 government, defense, and telecommunications entities across 14 countries, successfully achieving post-exploitation execution in nine organizations.
  * **October 21, 2026:** Microsoft Threat Intelligence published initial telemetry confirming that Storm-0940 integrated ARTEX into supply chain intrusions.
  * **October 28, 2026:** Microsoft Threat Intelligence observed automated ARTEX instances authenticating from a single Internet Protocol (IP) address to execute mass credential validation against downstream cloud environments.
  * **November 4–6, 2026:** Microsoft Threat Intelligence, GitGuardian, and the Computer Emergency Response Team for the European Union (CERT-EU) published detailed technical findings confirming that financially motivated threat groups (tracked as Storm-3358) and independent actors expanded ARTEX abuse to financial institutions in Southeast Asia, Japan, and South Korea.
  * **November 9, 2026:** The Indian Computer Emergency Response Team (CERT-In) reported that a threat group tracked as Crafty Falcon used ARTEX alongside other agentic frameworks (PentAGI and Cairn) against Non-Banking Financial Companies (NBFCs) and digital lending platforms.
* **Machine-Speed Attack Timelines:** Microsoft Threat Intelligence and GitGuardian documented that an ARTEX agent took approximately five minutes to scan a public GitHub repository, extract an exposed Open Authorization (OAuth) secret, validate the credential against Microsoft Entra ID, and exfiltrate cryptographic keys from Azure Key Vault.
* **High-Frequency Authentication and Privilege Escalation:** During the ConnectWise Cloud Backup campaign on October 15–16, 2026, ARTEX agents initiated password spraying that peaked at 2,900 sign-in requests per minute and executed automated Microsoft Graph API calls to self-assign the Global Administrator role to attacker-controlled service principals.
* **Lateral Movement via Remote Access Trojans (RATs):** In financial sector compromises documented in early November 2026, the Cambodia-based threat cluster Storm-3358 used ARTEX agents to exploit Server-Side Request Forgery (SSRF) and file upload vulnerabilities. The agents executed native command-line utilities (`curl` and `netcat`) to download and establish persistence with the WISP, vshell, and AdaptixC2 Remote Access Trojans (RATs).

### Working Hypotheses
* **Human-in-the-Loop Operational Steering:** Threat intelligence researchers at CrowdStrike and Microsoft hypothesize that while reconnaissance, vulnerability exploitation, and token validation ran entirely autonomously, human operators monitored telemetry and manually steered agents at key decision gates (such as target prioritization and final data selection).
* **Proxy and Geofence Evasion:** Analysts hypothesize that threat actors utilized commercial reverse proxies, Virtual Private Networks (VPNs), and intermediate Large Language Model (LLM) API aggregators to bypass provider geoblocking and safety guardrails.
* **Dual-Use Intent of Original Author:** Security analysts evaluate with moderate confidence that developer Autumn-27 intended the project for defensive penetration testing rather than offensive malware distribution, supported by the presence of standard defensive authorization notices in the original July 2026 code release.

### Intelligence Gaps and Unknowns
* **Proliferation Volume of Unregulated Forks:** Security researchers have not verified the total number of private, customized variations derived from the 12,000 public forks (such as ScopeWeaver or "ARTEX PRO") currently operating across private infrastructure.
* **Total Downstream Exposure:** The exact aggregate number of downstream customer organizations that sustained data exfiltration through compromised ConnectWise vendor credentials remains undisclosed by affected service providers.
* **Identity of Independent Actors:** The physical identities and institutional affiliations of the non-state operators conducting opportunistic scanning remain unknown.

---

## What Was the Business Impact

The ARTEX campaigns invalidated conventional incident response models by compressing multi-week intrusion lifecycles into minutes, depriving Security Operations Center (SOC) personnel of manual detection and containment windows.

| Business Dimension | Verified Impact | Analytical Classification |
| :--- | :--- | :--- |
| **Identity & Secrets Compromise** | Exposure and compromise of programmatic service principals, allowing automated adversaries to extract API keys, database connection strings, and certificates from Azure Key Vault. | Confirmed Fact |
| **Supply Chain Contagion** | Compromise of trusted administrative tokens belonging to ConnectWise Cloud Backup, granting threat actors programmatic reach into over 2,250 downstream customer tenants. | Confirmed Fact |
| **Financial Sector Breaches** | Unauthorized intrusion into customer loan platforms and internet banking services across South Korea, India, and Southeast Asia, resulting in service disruption and extortion attempts. | Confirmed Fact |
| **SOC Alarm Flooding** | Security teams experienced alert fatigue caused by bursts of automated operations (such as 27 distinct cloud permission changes executed in under 30 seconds), obscuring secondary persistence mechanisms. | Confirmed Fact |
| **Cumulative Financial Losses** | Total monetary damages across impacted organizations, including incident response costs, regulatory penalties, and extortion demands, have not been calculated or published. | Confirmed Unknown |
| **Compliance & Regulatory Scrutiny** | Affected European entities face formal audit inquiries under the Digital Operational Resilience Act (DORA) and Network and Information Security Directive 2 (NIS-2) concerning supply chain oversight and third-party risk management. | Working Hypothesis |

---

## What Is Being Done / Next Steps (Status as of Today)

### Current Status (November 10, 2026)
* **Codebase Containment:** The original GitHub repository remains restricted by developer Autumn-27. Security teams at Google and Microsoft continue monitoring third-party code-hosting services to identify and flag unauthorized clones and derivative tools.
* **Revocation of Compromised Service Credentials:** ConnectWise and Microsoft revoked all exposed application credentials and OAuth tokens associated with the ConnectWise Cloud Backup platform, eliminating the primary access vector into downstream Microsoft 365 environments.
* **Detection Engineering Rules:** Microsoft Defender Extended Detection and Response (XDR), CrowdStrike Falcon, and CERT-EU published behavioral detection signatures, Kusto Query Language (KQL) queries, and Indicators of Compromise (IOCs) to detect high-frequency Key Vault reads, anomalous service principal sign-ins, and automated endpoint scripting.

### Immediate Defensive Next Steps
1. **Public Repository Secret Audits:** Security Operations Center (SOC) teams must scan public and private code repositories to identify hardcoded credentials, revoking and rotating any exposed OAuth application secrets or access keys immediately rather than waiting for confirmation of exploitation.
2. **Conditional Access for Service Principals:** Identity and Access Management (IAM) teams must implement Conditional Access policies for workload identities, restricting service principals to explicit, trusted Internet Protocol (IP) ranges and disallowing authentication from foreign or unverified infrastructure.
3. **Behavioral Telemetry on Key Vaults:** Cloud security teams must configure real-time alerting for rapid key access patterns, establishing threshold alerts when a single identity issues 20 or more `SecretGet` operations across Azure Key Vault instances within 15 minutes.
4. **Endpoint Behavioral Monitoring:** Detection engineers must enforce Endpoint Detection and Response (EDR) rules that flag native system utilities (`curl`, `netcat`, and `PowerShell`) spawned directly by web server user accounts.
5. **Perimeter Vulnerability Patching:** IT operations must prioritize patching web-facing applications against Server-Side Request Forgery (SSRF) and unauthenticated file upload vulnerabilities to prevent agentic tools from obtaining initial local execution.

---

## Potential Root Causes

* **Continuous Exposure of Secrets in Source Repositories:** Development teams regularly push live API tokens, OAuth secrets, and database credentials into public version control systems, supplying agentic scanners with immediate points of ingress.
* **Proliferation of Autonomous Agent Frameworks:** Open-source architectures such as ARTEX, PentAGI, and Cairn automate the translation of high-level goals into multi-stage exploit execution paths, lowering the technical skill required to execute complex attacks.
* **Over-Privileged Non-Human Cloud Identities:** Enterprise architectures routinely assign broad, persistent administrative roles (such as Global Administrator) to service accounts without IP address limitations or Multi-Factor Authentication (MFA) requirements, enabling privilege escalation once credentials are stolen.
* **Defensive Speed Asymmetry:** Traditional security operations rely on human analysts operating on schedules measured in hours or days, whereas autonomous agents discover credentials, authenticate, escalate privileges, and extract data in approximately five minutes.
* **Exposed Perimeter Weaknesses:** Unpatched legacy web vulnerabilities—specifically Server-Side Request Forgery (SSRF) and insecure file upload handlers—remain accessible on corporate perimeters, allowing automated agents to establish initial access without manual intervention.

---

## Sources & References

* **Microsoft Threat Intelligence (November 6, 2026):** "ARTEX abuse expands as cybercriminals target financial sector"  
  https://www.microsoft.com/en-us/security/blog/2026/11/06/artex-abuse-expands-as-cybercriminals-target-financial-sector/
* **Microsoft Threat Intelligence (October 21, 2026):** "Storm-0940 uses ARTEX agentic AI to accelerate ConnectWise supply chain compromise"  
  https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/
* **GitGuardian Security Research (November 6, 2026):** "ARTEX: AI Agents Find and Abuse Exposed GitHub Secrets"  
  https://blog.gitguardian.com/the-agents-have-now-found-your-secrets-on-github-artex-is-abusing-public-secrets-right-now/
* **CrowdStrike (October 29, 2026):** "VAPOR PANDA Uses AI-Driven ARTEX to Grow Global Espionage"  
  https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/
* **Computer Emergency Response Team for the European Union (CERT-EU) (November 5, 2026):** "From Penetration Testing to Cyber Threat: Beware of ARTEX"  
  https://cert.europa.eu/blog/from-penetration-testing-to-cyber-threat-beware-of-artex
* **Google Threat Intelligence Group & Mandiant (October 30, 2026):** "ARTEX and Friends: Enter Agentic Offensive Frameworks"  
  https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks
* **Help Net Security (November 9, 2026):** "ARTEX goes from pentesting tool to attacker staple in three months"  
  https://www.helpnetsecurity.com/2026/11/09/artex-goes-from-pentesting-tool-to-attacker-staple-in-three-months/
* **Cybersecurity Dive (November 6, 2026):** "Hackers enlist Artex to scan GitHub repositories for exposed secrets"  
  https://www.cybersecuritydive.com/news/hackers-artex-github-repositories-exposed-secrets/874007/
* **Cybersecurity Dive (November 9, 2026):** "Financially motivated threat cluster uses AI-enabled tools against banking sector"  
  https://www.cybersecuritydive.com/news/financially-motivated-threat-ai-tools-banking-artex/874116/