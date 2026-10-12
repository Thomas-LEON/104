# LEDGER CYBER INCIDENT OVERVIEW: CRYPTOBILIS COMPROMISE

### What happened
A sophisticated supply chain attack occurred within the Ledger distribution network, where unauthorized actors acquired an authorized reseller (CryptoBilis) to physically compromise hardware wallets before shipment. The attackers successfully intercepted users' recovery phrases entirely off-grid, bypassing Ledger's software-based security checks.

1.  **The attackers utilized a covert acquisition** of the reseller CryptoBilis (around March 2026), operating under a Non-Disclosure Agreement (NDA) to prevent Ledger from detecting the ownership change.
2.  **Hardware tampering occurred in warehouses**, where devices were physically implanted with LTE/eSIM modules, microcontrollers, and display readers hidden behind the device screen.
3.  **The incident bypassed technical authentication** (Ledger's "Genuine Check"). Because the core Secure Element remained unaltered, Ledger Live processed the devices as authentic. 
4.  **The exfiltration was entirely out-of-band.** The implants captured the 24-word seed phrase directly from the display during initialization and transmitted it via cellular networks, never relying on the user's internet connection.

### What was the impact
While Ledger's core infrastructure and direct-sale devices remain secure, the targeted hardware tampering of reseller batches has led to massive, irreversible financial losses for end-users across multiple blockchains.

1.  **Financial Losses:** Estimated stolen assets range from $72 million to approximately $92.9 million USD.
2.  **Affected Scope:** Approximately 311 to 315 wallets were compromised across Tron, Bitcoin, Ethereum, BNB Chain, and Polygon. 
3.  **High-Profile Losses:** A single user suffered a confirmed loss of 80 BTC. In another instance, 111 Bitcoin wallets were emptied within a single block, and 25 Tron wallets were compromised within three seconds.
4.  **Asset Laundering:** Stolen funds were quickly routed through anonymizing protocols (such as Tornado Cash) and converted into stablecoins to obscure tracking.

---

### What is being done & next step (Status as of Oct 2026)

**Internal Actions (Ledger):**
1.  **Partnership Suspension:** Ledger immediately suspended all sales, shipments, and affiliations with CryptoBilis (effective Oct 9, 2026).
2.  **Investigation & Auditing:** Ledger has launched a formal internal investigation and is auditing its broader distribution chain to verify the integrity of other resale channels.

**External Actions (Ecosystem & Partners):**
1.  **Asset Mitigation:** Tether proactively intervened and successfully froze approximately $10 million USD in stolen USDT linked to the attackers.
2.  **Independent Investigations:** External cybersecurity experts and on-chain analysts (e.g., Bitquery) are conducting independent trace investigations.
3.  **Security Advisories:** The wider security community is advising customers who purchased from CryptoBilis to migrate funds using a newly generated seed phrase on a verified safe device, or to physically inspect the internal PCB for anomalies.

---

### Potential Root Causes
1.  **Supply Chain Vulnerability:** Lack of visibility into the ownership changes and operational security of authorized third-party resellers.
2.  **Physical Design Exploitation:** The physical casing allowed sufficient internal space for miniaturized LTE components to be added without triggering the Secure Element's anti-tamper mechanisms.

---

### Sources & References
*   **Bitquery Investigation (On-chain Analysis):** Ledger CryptoBilis Hack: $92.9M Drained, Where It Went - [Link](https://bitquery.io/investigations/ledger-cryptobilis-hack)
*   **Global Sources / Sourcing Digest:** Ledger investigates CryptoBilis wallet drains - [Link](https://www.globalsources.com/sourcing-digest/ledger-investigates-cryptobilis-wallet-drains-with-estimated-losses-of-92-9-million/)
*   **Crypto Briefing:** Hackers reportedly drain up to $93 million through compromised Ledger reseller - [Link](https://cryptobriefing.com/ledger-reseller-supply-chain-hack-implants/)
*   **KuCoin / MarsBit News:** Ledger supply chain attack steals mnemonic phrases - [Link](https://www.kucoin.com/news/flash/ledger-supply-chain-attack-steals-mnemonic-phrases-from-users-via-cryptobilis)
*   **CoinTribune:** Hack Ledger à 86 millions $ : CZ alerte sur une menace invisible - [Link](https://fr.tradingview.com/news/cointribune:84f679885b858:0/)
*   **Reddit (r/Bitcoin):** Technical discussions and user reports - [Link](https://www.reddit.com/r/Bitcoin/comments/1x2fdyc/why_were_only_ledger_devices_purchased_through/?tl=fr)