# Executive Summary: The CryptoBilis Ledger Supply Chain Compromise

This document provides a factual overview of the supply chain compromise affecting Ledger hardware wallets distributed by the authorized reseller, CryptoBilis.

## What happened ?
*   **Supply Chain Attack:** The authorized reseller CryptoBilis underwent an ownership change around March 2026, which was not communicated to Ledger. 
*   **Hardware Tampering:** The attackers physically compromised Ledger hardware wallets within the supply chain prior to final delivery.
*   **Technical Methodology:** Implants with cellular capabilities (LTE/eSIM) were hidden behind the device screens. These modules captured the 24-word recovery phrase directly from the screen during setup and transmitted it over cellular networks, completely bypassing the user's internet connection.
*   **Security Bypass:** The implants were designed to monitor and extract data quietly without triggering Ledger's security protocols, meaning the official "Genuine Check" still validated the devices as authentic.

## What is the Impact ?
*   **Financial Losses:** Estimated stolen assets range from $72 million to approximately $92.9 million USD.
*   **Scope:** The attack affected roughly 311 to 315 wallets across multiple blockchains (Tron, Bitcoin, Ethereum, BNB Chain, and Polygon). In one instance, 111 Bitcoin wallets were emptied within a single block, and 25 Tron wallets approved a spender within three seconds. One single user lost 80 BTC.
*   **Asset Laundering:** Stolen funds were quickly moved into anonymizing services and mixers like Tornado Cash to obscure the trail.

## What is being done & next step
*   **Immediate Actions:** Ledger is actively investigating the incident and requested CryptoBilis to suspend all sales and shipments of Ledger devices on October 9, 2026. Concurrently, Tether successfully froze approximately $10 million in stolen USDT.
*   **Security Recommendations:** Customers who purchased from CryptoBilis in the past 90 days are strongly advised not to initialize new devices. Those already using potentially affected devices should migrate their funds immediately to a new wallet using a newly generated recovery phrase on a safe, uncompromised device. 
*   **Ongoing Investigation:** The investigation remains strictly focused on devices distributed by this specific Southeast Asian reseller channel. Currently, there is no evidence suggesting that Ledger's own core systems, direct sales, or manufacturing processes were compromised.

## Sources & references
*   **Bitquery Investigation (On-chain Analysis):** Ledger CryptoBilis Hack: $92.9M Drained, Where It Went - [Link](https://bitquery.io/investigations/ledger-cryptobilis-hack)
*   **Global Sources / Sourcing Digest:** Ledger investigates CryptoBilis wallet drains with estimated losses of $92.9 million - [Link](https://www.globalsources.com/sourcing-digest/ledger-investigates-cryptobilis-wallet-drains-with-estimated-losses-of-92-9-million/)
*   **Crypto Briefing:** Hackers reportedly drain up to $93 million through compromised Ledger reseller - [Link](https://cryptobriefing.com/ledger-reseller-supply-chain-hack-implants/)
*   **KuCoin / MarsBit News:** Ledger supply chain attack steals mnemonic phrases from users via CryptoBilis - [Link](https://www.kucoin.com/news/flash/ledger-supply-chain-attack-steals-mnemonic-phrases-from-users-via-cryptobilis)
*   **CoinTribune:** Hack Ledger à 86 millions $ : CZ alerte sur une menace invisible - [Link](https://fr.tradingview.com/news/cointribune:84f679885b858:0/)
*   **Reddit (r/Bitcoin):** Technical discussions and user reports on the CryptoBilis compromise - [Link](https://www.reddit.com/r/Bitcoin/comments/1x2fdyc/why_were_only_ledger_devices_purchased_through/?tl=fr)