What happened ?
 * Supply Chain Attack: The authorized reseller CryptoBilis was discreetly acquired by new owners under a Non-Disclosure Agreement (NDA). Ledger was not informed of this ownership change.
 * Hardware Tampering: The new owners physically compromised Ledger hardware wallets within their warehouses prior to shipment.
 * Technical Methodology: Devices were implanted with an LTE/eSIM module, a microcontroller, and a display reader. This hardware intercepted the recovery phrase (seed phrase) directly from the device screen during initial setup and exfiltrated the data via cellular networks, entirely bypassing the user's internet connection.
 * Security Bypass: Because the Ledger Secure Element remained unaltered, the official Ledger Live software ("Genuine Check") continued to validate the compromised devices as authentic.
What is the Impact ?
 * Financial Losses: Total stolen assets exceed $90 million USD.
 * Scope: The attack affected approximately 315 wallets across multiple blockchains, including Tron, Bitcoin, Ethereum, BNB Chain, Polygon, and Solana. A single user suffered a confirmed loss of 80 BTC (approximately $6.6 million USD).
 * Asset Laundering: The stolen funds were routed through anonymizing protocols, such as Tornado Cash and Zcash, and subsequently converted into stablecoins.
What is being done & next step
 * Immediate Actions: Ledger has launched a formal investigation and suspended all sales and affiliations with CryptoBilis. Concurrently, Tether successfully froze approximately $10 million USD in stolen USDT.
 * Security Recommendations: Potentially affected customers are advised to immediately migrate their funds to verified, uncompromised wallets. Since software detection is ineffective, hardware experts recommend physically opening the casing to compare the internal circuit board (PCB) with official models, or checking the precise weight of the device to detect extra components.
 * Ongoing Investigation: Independent security experts are currently auditing the broader distribution chain to determine if other resale channels or batches have been compromised.
Sources & references
 * On-chain Analysis: Bitquery, Galaxy Research.
 * Financial Press: CoinDesk, BigGo Finance.
 * Technical Incident Reports: Reddit (r/CryptoCurrency, r/Bitcoin, r/ledgerwallet).
