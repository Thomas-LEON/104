# 0. Title: Hotel & Tourism - Sector Cyber Resilience & Credit Intelligence Research Q01-Q15 (merged)

# 1. Merge Statement
*   **Source Files:** File A (Q01-Q09) and File B (Q10-Q15).
*   **Research Dates & Cut-offs:** Both files share an evidence cut-off and research date of 3 November 2026.
*   **Merged Cut-off:** 3 November 2026.
*   **Scope Adopted:** Hotel & Tourism worldwide (with EU, UK, and US analysis), covering six subsectors: Lodging & Hotel Operators; Online Travel Agencies (OTAs) & Intermediaries; Cruise Lines; Tour Operators & DMCs; Theme Parks, Gaming & Integrated Resorts; and Corporate Travel Management (TMC).
*   **No New Research:** This document is a direct merge of File A and File B. No external web searches were performed; no new facts, figures, sources, cases, dates, or ratings were added.

# 2. Executive Summary for Senior Credit Officers
The Hotel & Tourism sector exhibits distinct vulnerabilities across four inherent exposure dimensions, reflecting a high-volume, asset-light, and digitally interdependent operating model:
*   **Fraud:** High (Provisional, Confidence: Medium). Driven by decentralized property procurement, high-velocity card payments, and unmonitored extranets enabling credential-harvesting.
*   **Cyber / ICT:** Very High (Provisional, Confidence: High). Driven by absolute room inventory perishability and vulnerable identity platforms exposing operations to ransomware.
*   **Operational Resilience / TPRM:** High (Provisional, Confidence: High). Rooted in oligopolistic concentration in Property Management Systems (PMS) and Global Distribution Systems (GDS).
*   **Governance Structure / Operating Model:** High (Provisional, Confidence: High). Fragmented accountability across franchisors, real estate owners, and local property managers obscures security governance.

**Five Most Important Findings:**
1.  **Absolute Perishability:** Operational downtime is immediately destructive; an unbooked room night cannot be recaptured post-restoration.
2.  **Identity Bottleneck:** Social engineering targeting IT helpdesks frequently bypasses standard multi-factor authentication (MFA), enabling rapid hypervisor encryption (e.g., 10-day, $100m EBITDA outages).
3.  **Cascading Vendor Dependency:** Core operations rely completely on external PMS and central reservation engines; single-vendor failures paralyze worldwide check-ins.
4.  **Extranet Exploitation:** Front-desk endpoint compromise allows threat actors to hijack partner-portal sessions, redirecting guest deposits without breaching core brand perimeters.
5.  **Liquidity Shock:** Recovery costs combined with lost revenue frequently exceed standard cyber insurance sub-limits, threatening interest coverage covenants within a single quarter.

**Three Priority Questions to Ask Borrowers:**
1.  Can your properties execute manual check-in, keycard issuance, and offline payment batching for seven consecutive days during a total enterprise IT failure?
2.  What independent, out-of-band protocols protect your IT helpdesk from social engineering and unauthorized administrative credential resets?
3.  How do your dedicated cyber insurance sub-limits and unencumbered revolving credit facilities compare to an estimated 30-day business interruption loss?

# 3. Question-by-Question Research

## Q01 - Sector Operating Model & Key Dependencies
Hospitality revenue relies on real-time room night perishable inventory, dynamic rate distribution, food and beverage (F&B) point-of-sale transactions, and ancillary event spend. The sector's transition to asset-light franchising separates brand marketing and central reservation infrastructure from legal property ownership and local property-level IT administration. This architecture creates deep operational interconnections and single points of failure across legacy operational technology (OT) and enterprise cloud systems.

**Subsector Dependency Matrix:**
*   *Hotels & Lodging:* Central Reservation System (CRS) / Channel Manager. SPoF: Yes. Switching Time: 3-6 months. Pathway: API compromise injects malicious rates. [S-019, S-009]
*   *Hotels & Lodging:* Property Management System (PMS). SPoF: Yes. Switching Time: 6-12 months. Pathway: Domain controller encryption renders PMS database inaccessible. [S-002, S-006]
*   *Integrated Resorts:* Electronic Keycard & Lock Management (RFID/BLE). SPoF: Yes. Switching Time: 1-3 months. Pathway: Local server compromise disables master keys. [S-021, S-022]
*   *Hotels & Lodging:* Identity Provider (IdP) & SSO (Okta, Entra ID). SPoF: Yes. Switching Time: 2-4 months. Pathway: IT helpdesk social engineering yields tenant-wide admin rights. [S-023, S-001]
*   *Cruise Lines:* Satellite Comms (LEO/GEO) & Onboard Maritime PMS. SPoF: Yes. Switching Time: Weeks to months. Pathway: VSAT bridge intrusion bridges air-gap. [S-024, S-025]
*   *OTAs:* Partner Extranet Portals. SPoF: High Concentration. Switching Time: Immediate loss. Pathway: Infostealer malware compromises extranet credentials. [S-005, S-012]
*   *Theme Parks:* Casino Management System & Slot Controller. SPoF: Yes. Switching Time: 6-18 months. Pathway: Lateral movement to gaming VLAN shuts down slots. [S-026, S-001]
*   *Corporate Travel (TMC):* Global Distribution Systems (Sabre, Amadeus, Travelport). SPoF: High Concentration. Switching Time: 12+ months. Pathway: Supply-chain compromise exposes itineraries. [S-027, S-028]
*(Cross-references: DEP register; Q12 TPRM Concentration; Q13 Governance)*

## Q02 - Cyber Incidents & Case Studies
*   **MGM Resorts (Sep 2023):** $100m EBITDA loss, 10-day outage via helpdesk social engineering and ESXi encryption. [S-001]
*   **Omni Hotels & Resorts (Mar 2024):** 5-day outage across 50 properties, manual room escorts required due to unsegmented OT locks. [S-006]
*   **Booking.com Extranet Wave (2024-2025):** £370k reported UK loss, global guest payment diversion via infostealers bypassing MFA on partner portals. [S-005, S-012]
*   **Caesars Entertainment (Aug 2023):** $15m extortion payment following outsourced IT helpdesk vishing to prevent operational shutdown. [S-029]
*   **Marriott/Starwood (2014-2018):** £18.4m UK ICO fine for post-M&A due diligence failure on legacy IT access. [S-004]
*   **IHG (Sep 2022):** 72-hour wiper/disruption via stolen credentials lacking MFA. [S-030]
*(Cross-references: INC register; Q03 Threat Scenarios; Q05 Financial Impact)*

## Q03 - Threat Scenarios, Attack Pathways & Exploited Weaknesses
*   **SCN-01: Enterprise Identity Takeover & Ransomware.** Vishing IT helpdesk -> IdP takeover -> hypervisor mass encryption. Exploits ineffective helpdesk caller validation and lack of FIDO2 hardware MFA. Trend: Increasing. Confidence: High.
*   **SCN-02: Partner Portal Hijack & Payment Fraud.** Phishing front desk -> infostealer extracts cookies -> extranet takeover -> guest payment diversion. Exploits lack of application whitelisting and session-cookie binding. Trend: Increasing. Confidence: High.
*   **SCN-03: OT Lockout & Building Paralyzation.** Remote vendor interface -> VLAN hopping -> door lock/BMS lockout. Exploits lack of segmentation between IT, guest Wi-Fi, and OT. Trend: Stable. Confidence: Medium.
*   **SCN-04: CRS API Disruption.** Cloud API compromise -> inventory/rate manipulation -> outage. Exploits unmonitored API keys. Trend: Stable. Confidence: High.
*(Cross-references: THR, CTL registers; Q11 Cyber Exposure)*

## Q04 - Resilience Capabilities & Sector Control Benchmarks
*   **Priority 1 (Survival):** Phishing-Resistant MFA (FIDO2), Immutable Offline Backups, Strict Helpdesk Identity Validation. *Benchmark:* Sector lag - <25% use FIDO2; helpdesks highly vulnerable.
*   **Priority 2 (Containment):** Strict IT/OT/Guest Network Segmentation, EDR & App Whitelisting, Third-Party Privileged Access Management. *Benchmark:* Pervasive gap in local property network segmentation.
*   **Priority 3 (Recovery):** Manual Offline Continuity Procedures (Cold-Start Kits), Disaster Recovery Rehearsals. *Benchmark:* Inconsistent property-level drill execution.
*(Cross-references: CTL register; Q08 Questionnaire Mapping; Q12 Resilience)*

## Q05 - Financial Impact, Disruption & Credit Transmission
*   **Average Cost of Data Breach:** $4.73m (2025 Hospitality Benchmark). [S-003]
*   **Mean Breach Lifecycle:** 254-267 days. [S-003]
*   **Average Ransomware Incident Cost:** $5.13m (excluding ransom). [S-003]
*   **Business Interruption Duration:** 7-14 days. [S-031]
*   **1-Week Outage Scenario:** Central reservation offline; manual check-in. 40% weekly revenue drop; $1.5m recovery cost. $2.75m cash drain. EBITDA falls but covenant stays compliant.
*   **4-Week Outage Scenario:** Domain controllers encrypted; zero web bookings. 75% monthly revenue drop. $6.0m recovery cost. $15.5m cash drain. Triggers technical breach of quarterly Interest Coverage covenants.
*   **8-Week Outage Scenario:** Extended directory rebuild; lost histories. 60% sustained 2-month revenue reduction. $12.0m recovery cost. $32.0m cash drain. Total working capital exhaustion and potential debt default.
*(Cross-references: FIN, SCN registers; Q10 Fraud Consequences)*

## Q06 - Regulation & Resilience Expectations
*   **EU NIS2 Directive:** 24h early warning, 72h notification. Mandates supply-chain risk management. Fines up to €7m or 1.4% turnover. High indirect pressure as corporate clients mandate audits. [S-007]
*   **EU GDPR / UK GDPR:** 72h reporting. Marriott fined £18.4m. Fines up to 4% global turnover. [S-004]
*   **US SEC Rules (Form 8-K):** 4 business days to report material incidents. Requires annual cyber risk governance disclosure. [S-032]
*   **PCI DSS v4.0:** Mandatory MFA and P2PE for cardholder data environments (enforced Mar 2025). Loss of merchant acquiring capability means instant insolvency. [S-008]
*(Cross-references: REG register)*

## Q07 - Geopolitical Cyber Threats & Systemic Exposure
*   **Russian Regional Confrontation:** Pro-Russian hacktivists (NoName057(16)) targeting EU/Baltic hotel booking engines with DDoS during diplomatic summits. [S-027]
*   **Strategic Espionage:** State-sponsored APTs (e.g., Silk Typhoon) compromising luxury hotel Wi-Fi to track VIPs and diplomatic delegations. [S-033]
*   **Middle East Instability:** Iranian-aligned wiper attacks targeting regional tourism and logistics. [S-034]
*(Cross-references: GEO register)*

## Q08 - Questionnaire-to-Sector Mapping & Credit Officer Engagement
*(Provisional mapping - see QMP Register for full list)*
*   **PROV-001:** Helpdesk identity validation mechanisms (targets SCN-01).
*   **PROV-002:** PMS backup immutability (targets SCN-01, SCN-03).
*   **PROV-003:** OT and keycard network isolation (targets SCN-03).
*   **PROV-004:** POS P2PE encryption (targets PCI DSS compliance).
*   **PROV-005:** Front-desk extranet safeguards (targets SCN-02, fraud against customers).
*   **PROV-006:** Third-party vendor access monitoring.
*   **PROV-007:** Executive tabletop drills & cold-start manual procedures.
*   **PROV-008:** Cyber insurance limit adequacy.
*(Cross-references: QMP register; linking THR, CTL, INC, FRD)*

## Q09 - Assembly Draft
*(Replaced by the finalized Section 5 - Updated Q09 Assembly)*

## Q10 - Fraud Exposure
**Q10.1 Typology Screen:**
*   *Payment Diversion:* Material (Hybrid). Supplier instruction interception.
*   *BEC:* Material (Hybrid). Targeting TMCs and franchisors.
*   *Invoice/Procurement:* Material (Non-cyber). Fictitious billing at integrated resorts.
*   *Account Takeover / Portals:* Material (Cyber-enabled). Hijacking OTAs.
*   *Insider Fraud / Embezzlement:* Material (Non-cyber). General managers overriding logs.
*   *Financial Statement Fraud:* Possible (Non-cyber). Aggressive RevPAR accounting.

**Q10.2 Documented Cases:**
*   *Booking.com Partner Extranet Fraud (2024-2025):* UK Action Fraud reported 532 complaints, £370k loss. Hybrid cyber-enabled fraud. [S-012, S-005, S-016]
*   *US v. Tran (2014-2022):* $1m+ insider embezzlement by hotel GM. [S-013]
*   *US v. Baroni (2010-2016):* $1m+ tour operator phony check/invoice collusion. [S-015]
*   *US v. Simontacchi (2009-2016):* $1m+ hotel controller bank fraud. [S-014]
*   *Cendant Corp (1995-1998):* $500m historical financial statement manipulation of franchise reserves. [S-020]

**Q10.3 & Q10.4 Metrics & Structural Drivers:**
*   Median occupational fraud loss (Food Service & Hospitality): $100,000 [S-011]. Structural drivers include high-velocity CNP transactions, supplier churn, decentralized property banking authority, and extranet interdependence.

**Q10.5 & Q10.6 Controls & Consequences:**
*   Recurring weaknesses: Inadequate segregation of duties in localized franchise accounting, unchecked manual overrides of night-audits, unverified supplier change details. Consequences: Direct balance sheet erosion, consumer chargebacks, franchise revocation.

**Q10.7 Rules:**
*   UK ECCTA (Failure to Prevent Fraud, 2025); EU CSDDD; US SOX 404; NACHA Credit-Push monitoring.

**Q10.8 Emerging Techniques:**
*   Multi-stage reception phishing delivering infostealers to hijack OTA portal cookies (IRONSCALES Oct 2026). [S-016]
*(Cross-references: FRD, FIN, REG registers)*

## Q11 - Cyber / ICT Exposure & Maturity
*   **Dependency:** Total reliance on PMS and CRS/GDS infrastructures.
*   **Attack Surface:** Extensive legacy on-premises installations for door locks and building management; high exposure of front-desk endpoints to social engineering.
*   **Maturity:** Sector bifurcated between Tier-1 brands utilizing cloud PMS and independent franchisees running unpatched local infrastructure. Substantial sector-wide deficit in FIDO2 adoption compared to finance.
*(Cross-references: BMK, CTL registers)*

## Q12 - Operational Resilience and Third-Party Concentration
*   **Concentration:** Lodging relies on an oligopoly (Oracle OPERA, Agilysys for PMS; Sabre, Amadeus for GDS). Substitutability is very low. Switching times exceed 6-12 months.
*   **Disruptions:** CrowdStrike (July 2024 global IT halt), Sabre SynXis historical outages, Omni lock failures.
*   **Third-Party Propagation:** Contagion passes via outsourced service providers and shared vendor portals without directly bridging internal corporate firewalls.
*(Cross-references: DEP register)*

## Q13 - Governance Structure & Operating-Model Complexity
*   **Structural Division:** The asset-light model separates the Brand Franchisor (IT standards), the Property Owner/REIT (capital expenditure), and the Management Company (daily operations).
*   **Governance Failure:** This fragmentation obscures accountability for capital investments in hardware lifecycle management, leaving legacy systems unpatched. It exacerbates M&A integration lags (e.g., Marriott/Starwood).
*(Cross-references: BMK register)*

## Q14 - Cross-Sector Comparison
*   **Fraud:** Median loss ($100k) exceeds retail due to larger procurement volumes, though lower than financial sector wire fraud. [S-011]
*   **Cyber/ICT:** Revenue perishability makes exposure absolute (unlike manufacturing, which can catch up via overtime). Data breach costs ($4.73m) exceed retail but trail healthcare. [S-003]
*   **TPRM:** Extreme concentration in specialized GDS software mirrors commercial aviation.
*(Cross-references: BMK register)*

## Q15 - Four-Dimension Classification
*(See Executive Summary and RAT Register for drivers and justifications)*
*(Cross-references: RAT register)*

---

# 4. Unified Registers

*   **INC (Incident Register):**
    *   MGM Resorts (Sep 2023) | Last 12m | Intrusion/Outage | S-001 | Top-5 Case Study
    *   Omni Hotels (Mar 2024) | Last 12m | Ransomware/Outage | S-006 | Top-5 Case Study
    *   Caesars (Aug 2023) | Last 12m | Extortion | S-029 | Top-5
    *   IHG (Sep 2022) | Historical | Wiper | S-030
    *   Marriott/Starwood (2014-2018) | Historical | APT | S-004 | Top-5
    *   Booking.com Fraud Wave (2024-2025) | Last 12m | Cyber-enabled Fraud | S-005, S-012, S-016 | Top-5 Case Study
    *   Holiday Inn Vilnius (Sep 2026) | Last 12m | Intrusion | S-010
    *   Kord Hotels (Oct 2026) | Last 30d | Intrusion | S-010
    *   CrowdStrike Outage (Jul 2024) | Last 12m | ICT Failure | B-file
    *   Sabre SynXis (Historical) | Historical | Vendor Outage | S-019
*   **FRD (Fraud Register):**
    *   Booking.com Partner Extranet: Hybrid cyber-enabled | Ext. Syndicates | £370k (UK subset) | Tip/Complaints | Weakness: Endpoint / Cookie Auth | S-012, S-005 (Linked to INC Booking.com)
    *   US v. Tran (2014-2022): Non-cyber Insider | General Manager | $1m+ | IRS Audit | Weakness: Night audit override | S-013
    *   US v. Baroni (2010-2016): Non-cyber Collusion | Account Mgr | $1.01m | Mgmt Review | Weakness: No countersignature | S-015
    *   US v. Simontacchi (2009-2016): Non-cyber Insider | Controller | $1m+ | External Audit | Weakness: Unsegregated ledger | S-014
    *   Cendant Corp (1995-1998): Non-cyber Mgmt | Execs | $500m | Post-M&A Audit | Weakness: Mgmt override | S-020
*   **THR (Threat Scenarios):** SCN-01 (Identity/Hypervisor Ransomware); SCN-02 (Partner Portal Hijack); SCN-03 (OT Lockout); SCN-04 (API Disruption).
*   **CTL (Control Weakness & Capability):** Lack of FIDO2, lack of OT segmentation, weak helpdesk ID verification, absent immutable backups.
*   **DEP (Dependency Matrix):** PMS (Oracle/Agilysys); GDS (Sabre/Amadeus); IdP (Okta); Electronic Locks (Assa Abloy). All characterized by High Concentration and low substitutability.
*   **GEO (Geopolitical Register):** Pro-Russian DDoS (Booking engines); East Asian APT (VIP tracking via hotel Wi-Fi); Middle East regional wiper activity.
*   **FIN (Metrics):** Breach cost $4.73m [S-003]; Ransomware cost $5.13m [S-003]; Median fraud loss $100k (Investigated cases) [S-011]; APP Fraud UK total [S-018].
*   **SCN (Disruption Scenarios):** 1-Week ($2.75m drain); 4-Week ($15.5m drain, covenant breach); 8-Week ($32.0m drain, default risk).
*   **REG (Regulatory Register):** NIS2 (Binding Directive, EU); GDPR (Regulation, EU/UK); SEC Form 8-K (Binding Regulation, US); ECCTA 2023 (Legislation, UK); SOX 404 (Legislation, US).
*   **BMK (Cross-Sector Benchmarks):** Hospitality median fraud $100k vs Retail $48k [S-011]. Hospitality breach cost $4.73m vs Healthcare $10.93m [S-003].
*   **RAT (Rating Matrix):** Fraud (High, Prov, Med Conf); Cyber (Very High, Prov, High Conf); TPRM (High, Prov, High Conf); Governance (High, Prov, High Conf).
*   **QMP (Questionnaire Map):** PROV-001 (Helpdesk); PROV-002 (Backups); PROV-003 (OT segments); PROV-004 (PCI/P2PE); PROV-005 (Extranet endpoint); PROV-006 (Third-party access); PROV-007 (Drills); PROV-008 (Insurance).

---

# 5. Updated Q09 Assembly

### 5.1 Report Outline
1. **Executive Sector Assessment:** The Hotel & Tourism sector faces acute cash-flow and credit vulnerability due to 100% perishable room inventory and systemic legacy IT interdependencies.
2. **Sector Operating Model & Dependencies:** Asset-light franchising fragments IT control, centralizing risk onto oligopolistic PMS and GDS SaaS platforms.
3. **Cyber Threat Landscape & Attack Scenarios:** Financially motivated groups exploit front-desk social engineering (helpdesk vishing, infostealers) as primary access paths.
4. **Geopolitical Cyber Exposure:** State actors utilize luxury hospitality networks for VIP surveillance; hacktivists target booking engines.
5. **Major Cyber Incidents & Case Studies:** Case studies (MGM, Omni, Booking.com extranet) demonstrate 10-figure revenue disruptions and immediate physical operational paralysis.
6. **Control Weaknesses & Resilience Priorities:** The sector fundamentally lacks phishing-resistant MFA, immutable backups, and property-level network segmentation.
7. **Regulatory & Supervisory Resilience Expectations:** Non-compliance with SEC, NIS2, and PCI DSS mandates direct financial liability and loss of merchant status.
8. **Operational & Financial Consequences and Credit Transmission:** Outages degrade EBITDA, exhaust working capital, and trigger technical debt covenant breaches rapidly.
9. **Questionnaire Mapping & Credit Officer Engagement:** Structured borrower evaluation relies on key control markers (PROV-001 to PROV-008).
10. **Methodology, Confidence & Limitations:** Sector analysis triangulates SEC 8-K filings and empirical vendor telemetry; ratings carry High confidence for Cyber/TPRM/Governance and Medium for Fraud.
11. **References:** Unified source register.

### 5.2 12-Slide Narrative
*   **Slide 01 Sector Intelligence Cover:** Hotel & Tourism. Cut-off: 3 Nov 2026. Global.
*   **Slide 02 Executive Sector Risk Snapshot:**
    *   *Ratings:* Fraud: High (Prov, Med Conf) - extranet fraud/decentralization. Cyber: Very High (Prov, High Conf) - inventory perishability/identity weakness. TPRM: High (Prov, High Conf) - oligopolistic PMS/GDS. Governance: High (Prov, High Conf) - franchisor/owner/manager fragmentation.
    *   *Significance:* Immediate revenue destruction during outages.
*   **Slide 03 Sector Anatomy: Key Operations & Dependencies:** Franchising separates marketing from property IT.
*   **Slide 04 Cyber Threat Landscape & Attack Scenarios:** Vishing and infostealers bypass firewalls via human deception.
*   **Slide 05 Geopolitical Cyber Threat Outlook:** Espionage and hacktivism correlate with diplomatic summits.
*   **Slide 06 Major Cyber Incidents & Lessons Learned:** Financial recovery hinges on offline operational readiness.
*   **Slide 07 Control Weaknesses & Resilience Priorities:** True resilience requires FIDO2 MFA and OT segmentation.
*   **Slide 08 Regulatory & Supervisory Resilience Expectations:** Strict incident reporting regimes enforce corporate liability.
*   **Slide 09 Financial Impact of Cyber Incidents:** Direct remediation is <15% of cost; business interruption accounts for >85%. Fraud subset: $100k median occupational loss [S-011].
*   **Slide 10 Cyber-to-Credit Risk Transmission & Stress Scenarios:** *(Illustrative - not a forecast or loss estimate)*. A 4-week outage drains $15.5m cash, breaching covenants.
*   **Slide 11 Questionnaire-to-Sector Intelligence Mapping:** *(Provisional)*. Non-technical questions identify material vulnerabilities.
*   **Slide 12 Credit Officer Engagement: Key Questions & Actions:** Proactive lending requires validated offline continuity plans.

### 5.3 Evidence Annex Outline
*   A1 Incident Register; A2 Detailed Case Studies; A3 Sector Fraud, Cyber & Resilience Metrics; A4 Regulatory Requirements by Jurisdiction; A5 Exposure Rating Methodology & Justification; A6 Questionnaire-Control-to-Threat Mapping; A7 Confidence, Assumptions, Sources & Methodology.

---

# 6. Conflict Register
| Item | File A Value & Source | File B Value & Source | Treatment | Status |
| :--- | :--- | :--- | :--- | :--- |
| Extranet Attacks (Booking.com) | Classified under cyber intrusions (S-005, S-012) | Classified under Account Takeover Fraud (S-012, S-005, S-016) | Linked. Cyber covers the technical session hijack; Fraud covers the deception/theft from guests. | Resolved |
| MGM Resorts Incident | Cyber incident / Ransomware (S-001) | TPRM/Governance operational disruption consequence (S-001) | Maintained in both domains reflecting structural failure compounding cyber execution. | Resolved |

# 7. Merge Log
*   **Duplicates Merged:** MGM SEC 8-K, CISA Advisory, IBM Ponemon 2025, Marriott ICO Notice, Action Fraud/Microsoft Threat intel regarding Booking.com, ACFE 2024. All mapped to singular S- IDs.
*   **Language Controls Applied:** "Verified" altered to "confirmed" (e.g., HR-confirmed, confirmed government intelligence). "Critical" altered to "essential" or "key". Em-dashes converted to spaced hyphens.
*   **Out of Scope Flagged:** Wirecard AG and Fat Leonard Navy Bribery cases explicitly noted as out of scope in File B and excluded from primary findings.

# 8. Gaps and Limitations
*   *Private Operator Under-Reporting (Affects Q02, Q05, Q10):* Mid-market franchisees are not obliged to disclose extortion payments or fraud losses publicly; loss data skews heavily toward large-cap SEC-regulated entities.
*   *Patch Latency Obscurity (Affects Q11):* Precise vulnerability compliance rates on localized on-premises PMS (legacy Oracle OPERA) remain commercially confidential.
*   *Fragmented Fraud Data (Affects Q10):* Extranet fraud losses are dispersed across individual consumer chargebacks, precluding a definitive absolute sector total.
*   *Rating Change Triggers:* Sector adoption of mandatory FIDO2 and standardized IT capital expenditure agreements between franchisors and REITs would substantially lower Cyber and Governance inherent risk ratings.

# 9. Completeness Check Table
| Question | Covered in A | Covered in B | Merged Status | Note |
| :--- | :--- | :--- | :--- | :--- |
| Q01 | Yes | No | Complete | Sourced from A |
| Q02 | Yes | No | Complete | Sourced from A |
| Q03 | Yes | No | Complete | Sourced from A |
| Q04 | Yes | No | Complete | Sourced from A |
| Q05 | Yes | No | Complete | Sourced from A |
| Q06 | Yes | No | Complete | Sourced from A |
| Q07 | Yes | No | Complete | Sourced from A |
| Q08 | Yes | No | Complete | Sourced from A |
| Q09 | Yes | No | Complete | File A assembly updated with File B ratings |
| Q10 | No | Yes | Complete | Sourced from B |
| Q11 | No | Yes | Complete | Sourced from B |
| Q12 | No | Yes | Complete | Sourced from B |
| Q13 | No | Yes | Complete | Sourced from B |
| Q14 | No | Yes | Complete | Sourced from B |
| Q15 | No | Yes | Complete | Sourced from B |

# 10. Reference Mapping Table & Unified Source Register

| Original Ref (File A / File B) | New S- ID | Title / Publisher | Dataset Type / Tier | Confidence | Temporal Class |
| :--- | :--- | :--- | :--- | :--- | :--- |
| File A: 1 / File B: 6 | **S-001** | MGM Resorts Form 8-K (SEC) | Official Filing / Tier 1 | High | Historical Precedent |
| File A: 2 / File B: 7 | **S-002** | Advisory AA23-320A (CISA/FBI) | Government Alert / Tier 1 | High | Contextual Benchmark |
| File A: 3 / File B: 12 | **S-003** | Cost of Data Breach 2025 (IBM) | Industry Research / Tier 2 | High | Current Rolling 12M |
| File A: 4 / File B: 8 | **S-004** | Marriott Penalty Notice (UK ICO) | Enforcement / Tier 1 | High | Historical Precedent |
| File A: 5 | **S-005** | Phishing Campaign Alert (Microsoft) | Threat Telemetry / Tier 2 | High | Current Rolling 12M |
| File A: 6 | **S-006** | Omni Data Breach Notice (Maine AG) | Official Notice / Tier 1 | High | Contextual Benchmark |
| File A: 7 | **S-007** | NIS2 Directive (EU) | Legislation / Tier 1 | High | Current Binding |
| File A: 8 | **S-008** | PCI DSS v4.0.1 (PCI SSC) | Contractual Standard / Tier 1 | High | Current Binding |
| File A: 9 | **S-009** | Hospitality Threat Landscape (Trustwave)| Threat Research / Tier 2 | Medium | Contextual Benchmark |
| File A: 10 | **S-010** | Threat Intelligence Registry (SOCRadar) | Secondary Feed / Tier 3 | Medium | Current Last 30 Days |
| File B: 1 | **S-011** | Occupational Fraud 2024 (ACFE) | Investigated Cases / Tier 2 | High | Contextual Benchmark |
| File B: 2 | **S-012** | Booking.com Scam Warning (Action Fraud)| Law Enforcement / Tier 1 | High | Current Rolling 12M |
| File B: 3 | **S-013** | US v. Tran Tax Fraud (DOJ) | Court Record / Tier 1 | High | Historical Precedent |
| File B: 4 | **S-014** | US v. Simontacchi Bank Fraud (DOJ) | Court Record / Tier 1 | High | Historical Precedent |
| File B: 5 | **S-015** | US v. Baroni Indictment (DOJ) | Court Record / Tier 1 | High | Historical Precedent |
| File B: 9 | **S-016** | Hospitality Phishing (IRONSCALES) | Threat Telemetry / Tier 2 | High | Current Last 30 Days |
| File B: 10 | **S-017** | 2024 Internet Crime Report (FBI IC3) | Law Enforcement / Tier 1 | High | Current Rolling 12M |
| File B: 11 | **S-018** | Annual Fraud Report 2025 (UK Finance) | Industry Data / Tier 2 | High | Current Rolling 12M |
| Text Ref (File A & B) | **S-019** | Sabre SynXis Incidents (Historical) | Historical / Tier 2 | High | Historical Precedent |
| Text Ref (File B) | **S-020** | Cendant Litigation 16587 (SEC) | Enforcement / Tier 1 | High | Historical Precedent |
| Text Ref (File A) | **S-021** | Assa Abloy / Dormakaba Security Rpts | OT Hardware / Tier 2 | High | Contextual Benchmark |
| Text Ref (File A) | **S-022** | Mandiant M-Trends 2024 | Threat Research / Tier 2 | High | Contextual Benchmark |
| Text Ref (File A) | **S-023** | Okta Security Advisories | Vendor Notice / Tier 1 | High | Current Rolling 12M |
| Text Ref (File A) | **S-024** | USCG Maritime Cyber Advisory 2023 | Government Alert / Tier 1 | High | Contextual Benchmark |
| Text Ref (File A) | **S-025** | DNV Maritime Cyber Study 2024 | Industry Research / Tier 2 | High | Contextual Benchmark |
| Text Ref (File A) | **S-026** | Nevada Gaming Control Board Filings | Regulatory / Tier 1 | High | Contextual Benchmark |
| Text Ref (File A) | **S-027** | ENISA Threat Landscape 2024 | Government Report / Tier 1 | High | Current Rolling 12M |
| Text Ref (File A) | **S-028** | US DoT Cyber Review 2023 | Government Report / Tier 1 | High | Contextual Benchmark |
| Text Ref (File A) | **S-029** | Caesars SEC 8-K (Sep 2023) | Official Filing / Tier 1 | High | Contextual Benchmark |
| Text Ref (File A) | **S-030** | IHG London Stock Exchange Rpt 2022 | Official Filing / Tier 1 | Medium | Historical Precedent |
| Text Ref (File A) | **S-031** | Sbit Hospitality Intelligence 2025 | Industry Data / Tier 2 | High | Current Rolling 12M |
| Text Ref (File A) | **S-032** | US SEC Cybersecurity Rules | Regulation / Tier 1 | High | Current Binding |
| Text Ref (File A) | **S-033** | CISA APT Hospitality Alert | Government Alert / Tier 1 | High | Contextual Benchmark |
| Text Ref (File A) | **S-034** | Recorded Future Intel (Iran) 2024 | Threat Research / Tier 2 | Medium | Current Rolling 12M |

*(Completeness check confirmed: All Q01-Q15 sections successfully generated, total 34 unique merged sources mapped.)*