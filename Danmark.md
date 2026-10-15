# DANFOSS CYBER INCIDENT OVERVIEW: FRENCH RETAILERS REFRIGERATION COMPROMISE

## What happened
In the night of October 11 to 12, 2026, cybercriminals compromised refrigeration control systems across several major French supermarket chains[span_0](start_span)[span_0](end_span). Attackers remotely triggered continuous defrost cycles and forced temperatures up to 50°C, causing widespread destruction of fresh and frozen goods, material damage, and commercial disruption[span_1](start_span)[span_1](end_span).

* **Remote Access:** Investigations point toward connected refrigeration controllers from Danish manufacturer Danfoss, where older or insufficiently secured devices were accessed remotely[span_2](start_span)[span_2](end_span).
* **Defrost Manipulation:** Threat actors altered temperature setpoints and extended standard defrost cycles from one hour up to eight hours[span_3](start_span)[span_3](end_span).
* **Physical & Inventory Damage:** Sustained heat ruined perishable stocks, damaged cooling units, and prompted reported fire starts[span_4](start_span)[span_4](end_span).
* **Attribution & Motive:** No cybercrime group has claimed responsibility at this stage, and no ransom demands were issued, pointing toward a purely disruptive motive[span_5](start_span)[span_5](end_span).

## What was the business impact
The attack affected more than 500 retail locations nationwide, with collective losses potentially reaching tens of millions of euros[span_6](start_span)[span_6](end_span).

* **Affected Retail Scope[span_7](start_span)[span_7](end_span):**
  * **Intermarché / Netto:** At least 300 stores impacted, facing heavy fresh and frozen food destruction, financial losses, and temporary department or store closures[span_8](start_span)[span_8](end_span).
  * **Coopérative U (Super U, Hyper U, U network):** Approximately 100 stores affected by refrigeration disruption and stock write-offs[span_9](start_span)[span_9](end_span).
  * **Carrefour:** 80 stores affected with refrigeration disruptions; financial impact not yet detailed[span_10](start_span)[span_10](end_span).
  * **Monoprix:** 25 to 30 stores affected, suffering localized inventory losses[span_11](start_span)[span_11](end_span).
  * **E.Leclerc:** Multiple stores disrupted due to third-party equipment failure; financial losses unquantified[span_12](start_span)[span_12](end_span).
  * **Metro France:** Operations impacted via an external provider, triggering inventory conservation checks[span_13](start_span)[span_13](end_span).

* **Documented Store-Level Damages:**
  * **Intermarché Gradignan (Gironde):** €21,000 in merchandise losses at cost price certified by a bailiff after a cold storage room hit 50°C, triggering the fire sprinkler system and flooding the warehouse[span_14](start_span)[span_14](end_span).
  * **Intermarché La Haye (Manche):** Equipment reportedly reached temperatures up to 80°C, causing physical components to melt[span_15](start_span)[span_15](end_span).
  * **Hyper U Bourgueil (Indre-et-Loire):** Total unavailability of fresh product inventory announced on October 12[span_16](start_span)[span_16](end_span).

## What is being done & next steps (Status as of Oct 2026)

### Government & Law Enforcement Actions
* **Judicial Investigation:** The Paris Public Prosecutor's Office opened an official inquiry and referred the case to the French Anti-Cybercrime Office (OFAC)[span_17](start_span)[span_17](end_span).
* **Regulatory Guidance:** The French national cybersecurity agency (ANSSI) intervened and recommended disconnecting Danfoss AK-SM and AK-SC controllers from the internet or enforcing restrictive network filtering[span_18](start_span)[span_18](end_span).

### Manufacturer Actions (Danfoss)
* **Hardware Assessment:** Danfoss stated that the targeted equipment ran obsolete firmware versions and that many compromised units had reached end-of-life status[span_19](start_span)[span_19](end_span).

### Ecosystem & Third-Party Actions
* **International Coordination:** Threat intelligence analysts (including Sekoia) flagged similar incidents in Spain, Portugal, Poland, Germany, and Belgium[span_20](start_span)[span_20](end_span).
* **Recovery & Restocking:** Critical cooling units are gradually being brought back online, though inventory reconstitution is expected to require several days[span_21](start_span)[span_21](end_span).
* **Insurance Considerations:** Retailers highlighted that certain operational insurance policies might not cover physical damages resulting from cyber compromises[span_22](start_span)[span_22](end_span).

## Potential Root Causes
* **Third-Party & Concentration Risk:** Widespread reliance on a single technology provider (Danfoss) across competing retail groups created a single point of failure, transforming a software-level compromise into a systemic sector-wide disruption[span_23](start_span)[span_23](end_span).
* **Legacy OT Vulnerabilities:** Continued deployment of end-of-life controllers operating with unpatched firmware left facilities directly vulnerable to remote network exploitation[span_24](start_span)[span_24](end_span).
* **External Attack Surface Blind Spots:** Facility management systems and technical OT assets connected to the public internet often bypass standard IT asset inventories and EASM monitoring[span_25](start_span)[span_25](end_span).

## Sources & References
* **Reuters:** [French supermarket chain Intermarché hit by cyberattack, 150 stores targeted](https://www.reuters.com/business/retail-consumer/french-supermarket-chain-intermarche-hit-by-cyberattack-150-stories-targeted-2026-10-12/)
* **Le Monde:** [Journée noire dans les supermarchés français après une cyberattaque massive](https://www.lemonde.fr/economie/article/2026/10/12/journee-noire-dans-les-supermarches-francais-apres-une-cyberattaque-massive_6792763_3234.html)
* **AFP / TV5Monde:** [Des supermarchés français touchés par une cyberattaque inédite de leurs installations frigorifiques](https://information.tv5monde.com/economie/des-supermarches-francais-touches-par-une-cyberattaque-inedite-de-leurs-installations-frigorifiques-2841301)
