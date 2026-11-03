**INCIDENT REPORT: Coordinated Cyber Attacks on Commercial Refrigeration Systems Across Europe**

**What happened**
A coordinated cyber campaign targeted commercial refrigeration infrastructure across Europe, directly expanding upon an October 11, 2026 attack that compromised ~700 French supermarkets (including Intermarché, Carrefour, and Leclerc) and destroyed tens of millions of euros in inventory by forcing temperatures up to 50°C.

Replicating these tactics, threat actors broadened the offensive across Belgium, Sweden, Ireland, the Netherlands, Luxembourg, Finland, Estonia, and Portugal. By targeting internet-exposed web interfaces and unsegmented cellular connections on industrial controllers—primarily legacy Danfoss (AK-SM/SC series) and Copeland/Dixell XWEB systems—attackers remotely altered temperature setpoints and triggered continuous overnight defrost cycles without deploying custom malware.

**What was the business impact**

* **Massive Inventory Spoilage:** Catastrophic inventory loss spanning fresh meats, dairy, frozen foods, and temperature-sensitive goods across impacted retailers (including Delhaize, ICA, Coop, Carrefour Belgium, and SuperValu), amounting to millions of euros in damaged stock.
* **Operational Disruption:** Aisle closures, emergency mobilization of field technicians to physically disconnect control units from electrical grids, and the requirement for store personnel to conduct hourly manual temperature checks.
* **Regulatory & Compliance Risks:** Immediate violation of HACCP and cold-chain safety regulations, mandating the destruction and haul-away of spoiled goods to prevent compromised food from reaching consumers.
* **Food Supply Chain & National Security Concerns:** The attacks raised severe concerns among European and defense authorities regarding hybrid threats and the vulnerability of foundational food supply networks.

**What is being done / Next Step (Status as of today: November 03, 2026)**

* **Current Actions:** Cooling system contractors (such as Sabcobel) and in-house technical teams have physically isolated affected control units, disconnected compromised cellular/grid connections, and initiated thorough cleaning and inventory disposal. Emergency firmware updates are being pushed to supported controller series (e.g., Danfoss AK-SM 800A release 4.3.1 and Copeland XWEB patches).
* **Next Steps:** Enforcing complete removal of refrigeration controllers from public IP addressing, placing all remote management strictly behind enterprise-grade VPNs with multi-factor authentication (MFA) per CERT-FR guidance, replacing discontinued legacy units (such as Danfoss AK-SM 800 and AK-SC 355), and deploying IoT network telemetry at the edge.
* **Status as of Today (November 03, 2026):** Active rogue intrusion traffic has been suppressed across affected chains. Retailers in Sweden, Belgium, and Ireland have moved into the active restocking and system-recommissioning phase. National cybersecurity agencies (including France's ANSSI/CERT-FR, Belgium's CCB, Sweden's NCSC, and the UK NCSC) alongside law enforcement are actively investigating attribution, assessing whether the campaign is financially motivated cyber sabotage or state-aligned hybrid disruption.

**Potential root causes**

* **Publicly Exposed Industrial Controllers:** Field units deployed with public IP addresses or connected via stand-alone 4G cellular modems outside corporate firewalls, leaving web management dashboards visible on scanning engines like Shodan and Censys.
* **Weak or Default Authentication:** Factory-default or predictable credentials (e.g., administrative accounts with simple or date-based passwords) on embedded web servers.
* **Lack of OT/IT Network Segmentation:** Flat network architectures allowing external connections directly into physical temperature controllers without perimeter firewalls, jump boxes, or zero-trust controls.
* **Legacy and Unpatched Controllers:** Widespread use of discontinued controllers running outdated firmware or end-of-life hardware that no longer receives vendor security updates.

**Sources & references**

* **The Guardian:** [Shop fridges and freezers across Europe hit by fresh suspected cyber-attack](https://www.theguardian.com/world/2026/nov/02/supermarket-freezers-across-europe-hit-by-second-suspected-cyber-attack)
* **CBC News / Reuters:** [Another cyberattack on supermarket fridges sweeps Europe, leaving food spoiled](https://www.cbc.ca/news/business/europe-fridge-cyber-incident-9.7405834)
* **SecurityWeek:** [Supermarket Refrigeration Attack Widens to Copeland, Dixell Controllers](https://www.securityweek.com/supermarket-refrigeration-attack-widens-to-copeland-dixell-controllers/)
* **Courthouse News Service / AFP:** [Fridge cyberattack hits supermarkets across Europe](https://www.courthousenews.com/fridge-cyberattack-hits-supermarkets-across-europe/)
* **CBS News:** [More grocery stores in Europe report fridge and freezer temperature spikes as apparent cyberattacks continue](https://www.cbsnews.com/news/europe-grocery-store-refrigerator-freezer-cyberattack-hack-food-wasted/)
* **Wikipedia:** [2026 French supermarket refrigerator hack](https://en.wikipedia.org/wiki/2026_French_supermarket_refrigerator_hack)
* **The Times of India:** [Weeks after hackers hit hundreds of French supermarkets, freezers at Sweden, Belgium and Luxembourg grocery stores overheat](https://timesofindia.indiatimes.com/technology/tech-news/weeks-after-hackers-hit-hundreds-of-french-supermarkets-freezers-at-sweden-belgium-and-luxembourg-grocery-stores-overheat/articleshow/135460702.cms)
