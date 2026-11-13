A major global outage has been affecting Microsoft's cloud ecosystem since Thursday, November 12, 2026, at approximately 16:17 **UTC** (*Coordinated Universal Time*, or 11:17 **EST** — *Eastern Standard Time*) and is ongoing on the morning of Friday, November 13, 2026. Microsoft is officially tracking the incident under tracking IDs **EX1550543** (*Exchange Online*, Microsoft's hosted enterprise email service) and **MO1550821** (*Microsoft Office / Microsoft 365*, designating the broader multi-service outage).

---

## What Happened

### What Is Confirmed (Established Facts)
* **Onset and Propagation:** The incident began with mailbox connection failures in **Exchange Online** in North America around 16:17 UTC on November 12, before spreading globally (Europe, Asia-Pacific, and the Americas) within two hours. At the peak of the disruption, the outage-tracking platform **Downdetector** logged over 130,000 user reports for the Outlook email client alone.
* **Affected Services:** The outage primarily impacts the enterprise **M365** (*Microsoft 365*, cloud-based productivity and collaboration suite) ecosystem, alongside certain consumer services:
  * **Email (Exchange Online / Outlook):** Users have been unable to access mailboxes via Outlook on the web, desktop, and mobile apps, as well as through **MAPI** (*Messaging Application Programming Interface*, Microsoft's client messaging protocol), **Exchange ActiveSync** (mobile synchronization protocol), and **REST APIs** (*Representational State Transfer Application Programming Interfaces*, web programming interfaces). Outgoing emails are experiencing delivery delays due to queuing on **SMTP** (*Simple Mail Transfer Protocol*, the standard email routing protocol) servers, though no permanent data loss has been reported.
  * **Collaboration and Productivity:** Disruptions across **Microsoft Teams** (primarily affecting calendar and meeting scheduling features, while basic chat and calls remained largely functional or recovered earlier), **SharePoint Online**, **OneDrive**, **OneNote**, **Microsoft To Do**, and **Microsoft 365 for the web**.
  * **Artificial Intelligence and Integrations:** Service failures affecting **Microsoft 365 Copilot** and **Microsoft Graph** (the unified API gateway for M365 data) calls. Third-party AI providers **OpenAI** and **Anthropic** also confirmed disruptions to their Microsoft 365 connectors.
  * **Security, Governance, and Analytics:** Intermittent unavailability of portals and features across **Microsoft Purview** (permissions, auto-labeling, classification, and **DLP** — *Data Loss Prevention*), **Microsoft Defender XDR** (*Extended Detection and Response*, Microsoft's threat detection and response platform, including **URL** — *Uniform Resource Locator* — verification via *Safe Links*), **Microsoft Intune** (endpoint management), and **Power BI** (failures when exporting reports to **PDF** — *Portable Document Format* — protected by **MIP** — *Microsoft Information Protection* — sensitivity labels).

### What Remains Uncertain (Unknowns)
* **Exact Scope of Affected Users:** Microsoft has not disclosed the exact number of impacted organizations or user accounts; Downdetector metrics reflect voluntary user submissions rather than the total volume of affected cloud tenants.
* **Exact Resolution Timeline:** As of 09:00 UTC on Friday, November 13, 2026 (more than 16 hours after the incident began), recovery remains partial and gradual, with no officially guaranteed timestamp for full restoration.

---

## What Was the Business Impact

* **Paralysis of Communications and Operational Workflows:** Thousands of enterprises, government agencies, courts, and educational institutions (notably across North America, Europe, Australia, Japan, Taiwan, and Singapore) were cut off from email and scheduling tools for a full business day.
* **Financial Sector and Public Markets:** Several major banking institutions (including DBS, UOB, and OCBC in Singapore) reported disruptions to their email systems. In the United States, electric vehicle manufacturer **Workhorse Group** officially postponed the release of its third-quarter financial results (originally scheduled for November 12) to November 16, 2026, citing operational inability caused by the outage.
* **Macroeconomic Cost:** According to expert estimates cited by Australian media, the prolonged disruption to corporate and public-sector productivity represents billions of dollars in lost economic output at a national scale.
* **Critical Infrastructure Preserved:** Affected governments (including in Singapore and Australia) confirmed that emergency services and vital public infrastructure remained operational despite the degradation of office productivity tools.
* **Secondary Cybersecurity Risk:** Government authorities (such as the state of Victoria in Australia) issued warnings against opportunistic threat actors exploiting the outage to launch phishing and social engineering campaigns targeting disoriented employees and customers.

---

## What Is Being Done and Next Steps (November 13, 2026)

### Ongoing Technical Actions (as of November 13, 2026)
1. **Deployment Freeze:** Microsoft has halted all software deployments and configuration changes across its infrastructure to stabilize the environment.
2. **Isolation, Restarts, and Rollbacks:** Engineering teams are isolating unhealthy servers, restarting them in controlled batches, and rebuilding portions of the fleet from a previously known-good software configuration.
3. **Health Check Bypass:** Microsoft validated an alternative server health verification method, allowing engineers to gradually reintroduce a subset of infrastructure back into the production pool.
4. **Capacity Expansion via Virtualization:** Large-scale provisioning of new **VMs** (*Virtual Machines*) to absorb excess load and compensate for temporarily offline servers.
5. **Traffic Throttling and Failover Routing:** Deliberate rate-limiting of incoming traffic allowed onto newly recovered servers, protocol adjustments, and traffic re-routing (*failover routing*) to prevent sudden reconnection surges from crashing them again.

### Next Steps
* **Short Term (Throughout November 13, 2026):** Continued, controlled scaling up of frontend and backend servers on a region-by-region basis, accompanied by regular status bulletins on the public `status.cloud.microsoft` portal and inside the M365 Admin Center.
* **Medium Term (Post-Resolution):** Microsoft has committed to publishing an official **PIR** (*Post-Incident Report*) detailing the exact timeline, confirmed root cause, and architectural defense-in-depth remediations.

---

## Potential Root Causes

### What We Know (Confirmed Technical Mechanism)
* **Cascading Capacity Failure:** Microsoft confirmed that the overload was not triggered by an abnormal spike in user traffic, but rather by a large number of servers unexpectedly going offline. Traffic was automatically redistributed across the remaining servers, overloading them in a chain reaction.
* **Saturation of the Secure Connection Process:** Internal investigation established that a core process on the affected servers—responsible for establishing secure connections—became overwhelmed, preventing servers from responding to requests.
* **Routing Rebound Effect:** During restoration efforts on the morning of November 13, routing services generated a surge of outbound calls to backend servers, causing several newly recovered servers to crash again.

### What Has Been Ruled Out (So Far)
* **Cyberattack or Rogue AI:** Contrary to viral online rumors alleging a coordinated cyberattack or a malfunctioning artificial intelligence agent (*rogue AI*), Charles Lamanna (**EVP** — *Executive Vice President* at Microsoft) as well as government officials (including Australian Home Affairs Minister Tony Burke) explicitly stated there is no evidence of malicious activity or intrusion.

### What Is Hypothesis or Remains Unknown
* **Hypothesis 1 — Faulty Network Configuration Update:** Although Microsoft initially stated it had identified no recent changes correlated with the start of the outage, subsequent updates revealed that engineers are evaluating and reverting a small number of recent changes (specifically involving network configuration) whose timestamps align with the onset of the incident. However, certain machines stuck in an unhealthy state are slowing down the synchronization of this rollback.
* **Hypothesis 2 — Logic Flaw in Automated Health Probes:** External infrastructure analysts hypothesize that latency or a bug in the automated health-check system may have falsely flagged healthy servers as offline, triggering a *failover storm* that surviving servers lacked the physical capacity to absorb.
* **Major Unknown:** The exact initial trigger (*root cause*) that knocked the very first group of servers offline has not yet been officially confirmed by Microsoft and will only be established upon release of the PIR.

---

## Sources and References

* **Microsoft (Official Cloud Service Health Portal):** [Microsoft Service Health Status](https://status.cloud.microsoft) *(official tracking for incidents EX1550543 and MO1550821)*
* **Microsoft Learn / Q&A (Technical Documentation on EX1550543 / MO1550821):** [Technical Diagnostic and Recovery Recommendations for Exchange Online Incident EX1550543 / MO1550821](https://learn.microsoft.com/en-nz/answers/questions/6070072/technical-diagnostic-and-recovery-recommendations)
* **The Guardian (Live Coverage and Technical Analysis):** [Microsoft outage live: 'positive results for server stability' reported](https://www.theguardian.com/technology/live/2026/nov/13/microsoft-outage-down-today-live-update-outlook-teams-365-when-fixed-latest-status-cause-news) & [A global Microsoft 365 outage has hit millions – what happened and when will it be fixed?](https://www.theguardian.com/australia-news/2026/nov/13/global-microsoft-outage-what-happened-and-why)
* **CIO (Infrastructure and Backend Routing Analysis):** [Microsoft struggles to get M365 services back online after widespread outage](https://www.cio.com/article/4248249/microsoft-struggles-to-get-m365-services-back-online-after-widespread-outage.html)
* **The Independent (Health Check Analysis and OpenAI / Anthropic Impact):** [I’m a tech expert. This is the likely cause of the global Microsoft outage](https://www.independent.co.uk/tech/microsoft-outage-cause-outlook-down-b3084285.html) & [Is Outlook down? Widespread outage hits Microsoft and OpenAI](https://www.independent.co.uk/news/world/americas/microsoft-outage-today-latest-outlook-teams-down-openai-fixed-b3084265.html)
* **Mashable (Timeline of Official Microsoft Statements):** [Microsoft global outage: What the company has said so far](https://mashable.com/tech/microsoft-outage-what-company-has-said) & [Microsoft Outlook outage cause: What happened today](https://mashable.com/tech/microsoft-outlook-outage-cause-revealed-nov-12-2026)
* **Channel News Asia / CNA (Impact on Banks and Governments in Asia):** [Microsoft Outlook outage: Governments, businesses affected worldwide as tech giant struggles to restore services](https://www.channelnewsasia.com/world/microsoft-outlook-outage-email-teams-live-6548071)
* **Forbes Australia (2026 M365 Outage History and Impact):** [Microsoft Outage: Outlook and Teams still down as fixes stall](https://www.forbes.com.au/news/world-news/microsoft-servers-crash-in-global-outage/)
* **Times of India (Charles Lamanna's Denial of Cyberattack / AI Theories):** [Microsoft outage: As cyberattack and rogue AI theories go viral, Copilot EVP Charles Lamanna reveals what likely didn't cause it](https://timesofindia.indiatimes.com/technology/tech-news/microsoft-outage-as-cyberattack-and-rogue-ai-models-attack-theories-go-viral-copilot-evp-charles-lamanna-confirms-what-has-not-likely-caused-the-outage/articleshow/135793367.cms)
* **Sangfor Technologies (Detailed UTC/EST Timeline):** [Microsoft Outage: Outlook and Microsoft 365 Down Worldwide](https://www.sangfor.com/blog/cybersecurity/microsoft-outage-outlook-365-november-2026)