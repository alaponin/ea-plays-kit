# Sources per building block — what each can and cannot prove

Organisations, not URLs, are the stable part. Where a URL is given it is a starting point;
if it has moved, search the organisation's name plus the dataset name, and record the new
URL here.

## Identity

| Source | Proves | Does not prove |
| --- | --- | --- |
| World Bank **ID4D** dataset and country diagnostics | Coverage rates, legal framework, capabilities | Whether a specific system is live *today* — diagnostics lag |
| The **national ID authority's own site** | Existence, enrolment figures, service catalogue | Interoperability with other sectors |
| **ID4Africa** country profiles | Implementation maturity across 48 African members | Current status between updates |
| **MOSIP deployment list** | That a country deployed MOSIP, and at what stage | Coverage; whether it is the *national* system |
| **UNECA Africa Digital ID Landscape** | Country-level profiles, legal frameworks | Anything after its publication year |

Watch for: a foundational ID and a functional (sectoral) ID being conflated. Ask which one
the claim is about. Age of issuance matters for education — an ID issued only at 16 cannot
anchor a learner registry.

## Civil registration

| Source | Proves |
| --- | --- |
| The national **CRVS agency** | The registration process, whether it is digital, coverage |
| **UNICEF** birth-registration data | The registration rate, by year |
| World Bank **ID4D** CRVS material | The link (or absence of one) between CRVS and the ID system |

Watch for: registration *rate* versus *certificate possession* rate — they differ, often
by a lot, and a design that assumes a certificate needs the second figure.

## Payments

| Source | Proves | Does not prove |
| --- | --- | --- |
| The **central bank's** instant-payment / national-switch page and **annual report** | That a switch exists, its operator, transaction volumes | Government access — a retail switch is not a G2P rail |
| World Bank **fast-payments** material | Cross-country status of fast-payment systems | Local participation detail |
| **GSMA** mobile-money data | Mobile-money accounts and agent networks | Anything about a government payment platform |

Watch for: "the country has mobile money" being read as "the government can disburse". G2P
capability needs a named government payment mechanism, not a retail one.

## Data exchange

| Source | Proves | Does not prove |
| --- | --- | --- |
| **NIIS X-Road world map** | That an X-Road instance is registered | Its member count, whether it is in production |
| **GovStack country engagements** | That the country engages with GovStack | That any building block is deployed |
| **UNDP DPI map** | A country's self-declared DPI status | Independent verification |
| The **operator's own member list / service catalogue** | The real answer: who is connected and to what | — this is the source to reach |

Watch for: an instance registered on a map years ago with four members still. Always find
the member count and its date; a data-exchange layer with no data catalogue is a pilot.

## Cloud and hosting

| Source | Proves |
| --- | --- |
| The **national data-centre or G-cloud operator's** own pages and service catalogue | Existence, tiers offered, who may host |
| The national **ICT agency's** annual report | Utilisation, whether ministries actually host there |

Watch for: a data centre that exists physically but has no service catalogue, no SLA and no
tenants. That is a building, not a building block.

## Consent and data sharing

| Source | Proves |
| --- | --- |
| The **data-protection regulator's** register and guidance | The legal basis regime, whether the regulator is operative |
| Any **published consent service** | A technical consent capability |

Watch for: a data-protection act in force with a regulator that has taken no action and has
a handful of staff. Record the act as *enacted* and the enforcement capability as *unclear* —
they are different facts and a design depends on both.

## Sector registries

The sector ministry's own systems list, and the donor project documents that built them.
A registry named in a sector plan is *planned*; a registry with an operator, a record count
and a maintenance contract is *live*.
