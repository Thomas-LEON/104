# LEDGER CYBER INCIDENT OVERVIEW: CRYPTOBILIS COMPROMISE

### What happened
Between March 2026 and October 9, 2026, a highly sophisticated physical supply chain attack occurred targeting Ledger hardware wallets. Unidentified threat actors discreetly purchased the authorized Southeast Asian reseller, CryptoBilis. Once in control of the local warehouses, these actors physically opened legitimate Ledger devices and implanted malicious hardware designed to steal cryptocurrency. By intercepting users' recovery phrases entirely off-grid via cellular networks, the attackers successfully bypassed Ledger's software security checks, resulting in the theft of approximately $93 million USD.

1.  **Covert Acquisition (March 2026):** Unidentified threat actors acquired the reseller CryptoBilis, operating under a Non-Disclosure Agreement (NDA) to prevent the manufacturer (Ledger) from detecting the ownership change.
2.  **Physical Tampering in Warehouses:** Devices were physically implanted with LTE (Long-Term Evolution - standard 4G cellular data) and eSIM (Embedded Subscriber Identity Module) modules, microcontrollers, and display readers hidden behind the device screen.
3.  **Authentication Bypass:** Because the core Secure Element chip remained unaltered, Ledger Live's software (the "Genuine Check") processed the compromised devices as authentic official orders.
4.  **Out-of-Band Exfiltration:** The implants captured the 24-word seed phrase directly from the display during initialization and transmitted it via cellular networks, entirely independent of the user's internet connection.

### What was the business impact
While Ledger's core infrastructure and direct-sale devices remain secure, the targeted hardware tampering of reseller batches has led to massive, irreversible financial losses for end-users.

1.  **Financial Losses:** Estimated stolen assets range from $72 million to approximately $92.9 million USD.
2.  **Affected Scope:** Approximately 311 to 315 wallets were compromised across multiple blockchains (Tron, Bitcoin, Ethereum, BNB Chain, and Polygon). 
3.  **High-Profile Targets:** A single user suffered a confirmed loss of 80 BTC. In another instance, 111 Bitcoin wallets were emptied within a single block.
4.  **Asset Laundering:** Stolen funds were quickly routed through anonymizing protocols (such as Tornado Cash) and converted into stablecoins to obscure tracking.

---

### What is being done & next steps (Status as of Oct 2026)

**Ledger Actions (Manufacturer):**
1.  **Affiliation Suspension:** Ledger immediately suspended all sales, shipments, and reseller affiliations with CryptoBilis (effective October 9, 2026).
2.  **Distribution Audit:** Ledger has launched a formal investigation and is auditing its broader distribution chain to verify the operational security of other resale channels.

**CryptoBilis Actions (Compromised Reseller):**
1.  **Operations Halted:** All sales and shipments of Ledger devices from CryptoBilis facilities have been stopped following Ledger's mandate.

**Ecosystem & Third-Party Actions:**
1.  **Asset Mitigation:** The stablecoin issuer Tether proactively intervened and successfully froze approximately $10 million USD in stolen USDT linked to the attackers.
2.  **Independent Investigations:** External cybersecurity experts and on-chain analysts (e.g., Bitquery) are conducting trace investigations to track the stolen funds.
3.  **Security Advisories:** The community is advising customers who bought from CryptoBilis to migrate funds using a newly generated seed phrase on a verified safe device, or to physically inspect the internal PCB (Printed Circuit Board - the main electronic circuitry) for unauthorized components.

---

### Potential Root Causes
1.  **Supply Chain Vulnerability:** Over-reliance on the perceived security of an authorized reseller, lacking deep visibility into third-party ownership changes and physical warehouse security.
2.  **Physical Design Exploitation:** The internal casing of the hardware wallet provided sufficient empty space for miniaturized cellular components to be added without triggering existing anti-tamper mechanisms on the main board.

---

### Sources & References
*   **Bitquery Investigation (On-chain Analysis):** Ledger CryptoBilis Hack: $92.9M Drained, Where It Went - [Link](https://bitquery.io/investigations/ledger-cryptobilis-hack)
*   **Global Sources / Sourcing Digest:** Ledger investigates CryptoBilis wallet drains - [Link](https://www.globalsources.com/sourcing-digest/ledger-investigates-cryptobilis-wallet-drains-with-estimated-losses-of-92-9-million/)
*   **Crypto Briefing:** Hackers reportedly drain up to $93 million through compromised Ledger reseller - [Link](https://cryptobriefing.com/ledger-reseller-supply-chain-hack-implants/)
*   **KuCoin / MarsBit News:** Ledger supply chain attack steals mnemonic phrases - [Link](https://www.kucoin.com/news/flash/ledger-supply-chain-attack-steals-mnemonic-phrases-from-users-via-cryptobilis)
*   **CoinTribune:** Hack Ledger à 86 millions $ : CZ alerte sur une menace invisible - [Link](https://fr.tradingview.com/news/cointribune:84f679885b858:0/)
*   **Reddit (r/Bitcoin):** Technical discussions and user reports - [Link](https://www.reddit.com/r/Bitcoin/comments/1x2fdyc/why_were_only_ledger_devices_purchased_through/?tl=fr)