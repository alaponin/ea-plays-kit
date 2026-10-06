# PAERA glossary — in the kit's own words

Use this file to read PAERA's terms, and to map them to another model: GovStack building
blocks, a national architecture framework, or the teaching set of the EA course. The
meanings below are written in the kit's own words. They are not PAERA's definitions. To
quote a definition, open the page and quote one sentence, with the address.

## Abbreviations

The list is on the page *Abbreviations*, under chapter 1:
https://paera.govstack.global/1.-introduction-to-paera/abbreviations

| Short form | Long form, or what it means |
| --- | --- |
| BB | Building Block |
| BO | Back Office |
| DPG | Digital Public Goods |
| DPI | Digital Public Infrastructure |
| EA | Enterprise Architecture |
| ERP | Enterprise Resource Planning |
| FO | Front Office |
| G2G | Government to Government |
| GS | GovStack |
| KPI | Key Performance Indicator |
| MDA | Ministries, Departments and Agencies |
| PAERA | Public Administration Ecosystem Reference Architecture |
| PAO-CC | Public Administration Core Components |
| PAR | Public Administration Reform |
| PCI DSS | Payment Card Industry Data Security Standard |
| PDU | Policy Development Unit: the type of body that makes policy |
| RA | Regulatory agency: the type of body that regulates one area of the economy |
| SDA | Service delivery authority: the type of body that delivers services, for example a police or a customs department |
| SLA | Service Level Agreement |
| WoG | Whole of Government |

## The classes of the metamodel (Annex 2)

Page: https://paera.govstack.global/7.-annex-2-metamodel-of-reference-architecture

Annex 2 describes an architecture in the terms of TOGAF and models it in ArchiMate. Its
main concern is the **business** and the **application** architecture. It has six
classes:

| Class (Annex 2 name) | What it means, in the kit's words |
| --- | --- |
| Customer | A person or an organisation that a public body serves |
| Service | What a body does for a customer, to meet a need |
| Business process | The ordered work inside one body that delivers one or more services |
| Workflow | The ordered steps that one unit inside a body carries out, as its part of a service |
| Application function | A group of functions of an application that supports the work |
| Application component | The software that gives the functions |

The chain to keep in mind when you read a PAERA architecture:

> Customer → Service → Business process → Workflow → Application function → Application component

**The teaching set is different.** Play 2.2 of the EA course teaches six entity types:
Capability, Service, Application, Data Domain, Technology Component and Organisation.
Only *Service* has the same name in Annex 2. A check against Annex 2 gives the verdict
*conformant to the teaching subset only* to an element that has a place in the teaching
set and none in Annex 2. See `SKILL.md`, step 3.

## Terms that PAERA defines in its chapters

| Term | Section | Page |
| --- | --- | --- |
| Public administration | §2.4 | https://paera.govstack.global/2.-state-of-digital-transformation |
| Digital government; the digital governance model | §2.5 | same page |
| Outcome architecture | §2.1 | same page |
| Digital culture | §3.1.2 | https://paera.govstack.global/3.-national-level |
| The four foundational pillars: access, digital data, interoperability, digital identity | §3.4 | same page |
| Chief digitalisation officer | §4.2.1 | https://paera.govstack.global/4.-organisation-level |
| The organisational taxonomy | §4.6, and Annex 1, A1.2 | same page, and https://paera.govstack.global/6.-annex-1-digital-infrastructure |
| The capability levels | §5.1 | https://paera.govstack.global/5.-implementation-framework |

**Pillars are not building blocks.** The pillars of §3.4 are national preconditions. A
GovStack building block is a reusable software component. A review that mixes the two
gives a wrong finding.

## The twelve main state registries (Annex 3)

Page: https://paera.govstack.global/8.-annex-3-main-state-registries

Population Registry · Business Registry · Cadastre/Land register · Official Publications ·
Securities Register · Registry of economic activities, licenses and permissions · Vehicle
Register · Health Registers · Social Insurance Register · Education Register · Criminal
Register · Procurement Register.

These are the names as the page gives them. For what each registry holds, read the page.
