# The sources for each building block — what each one can prove

The organisations are stable. The URLs are not. A URL here is a start. If a URL moved,
search for the name of the organisation and the name of the dataset. Then record the new URL
in this file.

## Identity

| Source | Proves | Does not prove |
| --- | --- | --- |
| The **ID4D** dataset and country diagnostics of the World Bank | The rates of coverage, the legal framework, and the capabilities | Whether a system is live *today*. A diagnostic is some years behind |
| The **site of the national ID authority** | That the system exists, the enrolment figures, and the service catalogue | Interoperability with other sectors |
| The country profiles of **ID4Africa** | The maturity of the implementation, across 48 African members | The status between two updates |
| The **MOSIP deployment list** | That a country deployed MOSIP, and at which stage | The coverage. It also does not prove that MOSIP is the *national* system |
| The **UNECA Africa Digital ID Landscape** | Country profiles and legal frameworks | Anything after the year of publication |

Watch for this error: a foundational ID and a functional ID of one sector are two different
things. Ask which one the claim is about. For education, the age of issue matters. An ID
that a body issues only at 16 years cannot anchor a learner registry.

## Civil registration

| Source | Proves |
| --- | --- |
| The national **CRVS agency** | The registration process, whether it is digital, and the coverage |
| The birth-registration data of **UNICEF** | The registration rate, for each year |
| The CRVS material of **ID4D** at the World Bank | The link between CRVS and the ID system, or the absence of a link |

Watch for this error: the *rate of registration* and the rate of *possession of a
certificate* are different, and frequently they are very different. A design that assumes a
certificate needs the second figure.

## Payments

| Source | Proves | Does not prove |
| --- | --- | --- |
| The page of the **central bank** for instant payments or the national switch, and its **annual report** | That a switch exists, who operates it, and the transaction volumes | Access for the government. A retail switch is not a rail for government-to-person payments |
| The **fast-payments** material of the World Bank | The status of fast-payment systems across countries | The detail of who participates in the country |
| The mobile-money data of **GSMA** | The mobile-money accounts and the networks of agents | Anything about a payment platform of the government |

Watch for this error: "the country has mobile money" becomes "the government can pay
people". A government-to-person capability needs a named payment mechanism of the
government. A retail mechanism is not one.

## Data exchange

| Source | Proves | Does not prove |
| --- | --- | --- |
| The **X-Road world map** of NIIS | That somebody registered an X-Road instance | The number of members. It also does not prove that the instance is in production |
| The **country engagements of GovStack** | That the country works with GovStack | That the country deployed a building block |
| The **DPI map of UNDP** | The DPI status that the country declared for itself | An independent verification |
| The **member list or the service catalogue of the operator** | The true answer: who is connected, and to what | — this is the source to reach |

Watch for this error: somebody registered an instance on a map some years ago, and it still
has four members. Always find the number of members and its date. A data-exchange layer with
no catalogue of data is a pilot.

## Cloud and hosting

| Source | Proves |
| --- | --- |
| The pages and the service catalogue of the operator of the **national data centre or the G-cloud** | That it exists, which tiers it offers, and who can host on it |
| The annual report of the national **ICT agency** | The use of the service, and whether the ministries host their systems there |

Watch for this error: a data centre exists as a building, and it has no service catalogue,
no SLA and no tenants. That is a building. It is not a building block.

## Consent and data sharing

| Source | Proves |
| --- | --- |
| The register and the guidance of the **data-protection regulator** | The regime of legal bases, and whether the regulator operates |
| Any **consent service that is published** | A technical capability for consent |

Watch for this error: a data-protection act is in force, and its regulator has a few staff
and has taken no action. Record the act as *enacted* and the capability to enforce it as
*unclear*. These are two different facts, and a design depends on both.

## Sector registries

Use the systems list of the sector ministry, and the donor project documents that built the
systems. A registry that a sector plan names is *planned*. A registry with an operator, a
count of records and a maintenance contract is *live*.
