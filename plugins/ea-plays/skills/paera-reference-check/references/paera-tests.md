# PAERA as a test — the ten principles, the capability ladder, the roadmap phases

Use this file to **apply** PAERA to a design, a plan or a roadmap. Each principle and each
level is written here as a test, in the kit's own words. This file is not PAERA's text.
Before you write a finding, open the section on the public page and read it. The
*Implications* of a principle carry the detail that a reviewer will ask for.

Addresses are in `paera-index.md`. The page for all three parts of this file is
https://paera.govstack.global/5.-implementation-framework

## Part A — The ten principles (§5.2)

Each principle on the page has three parts: *Motivation*, *Rationale* and
*Implications*. The titles below are the §5.2 titles as published on 6 October 2026.

| # | §5.2 title | The test | What failing looks like |
| --- | --- | --- | --- |
| 1 | Rule of Law | Each digital function, data use and automated decision has a legal basis. A public body does only what the law gives it to do. | A service or a data use with no legal basis; an automated decision with no route to hold someone to account |
| 2 | Whole of Government | The body is part of the national ecosystem. It connects to it and uses the national infrastructure that exists. | A body builds its own identity, registry or integration layer beside the national one |
| 3 | Digital by Default | A new process or service is designed to be digital from start to end. Paper is the exception. | A web form that copies a paper form; a paper process that is only scanned |
| 4 | No legacy software | A new system is built so that it can be extended and maintained. It does not become the next system that nobody can change. | No upgrade path; custom code where a building block exists; no budget for maintenance |
| 5 | Once-Only | A person or a business gives a piece of information once. Public bodies reuse it. | A screen asks for data that the state already holds |
| 6 | Customer-centricity | The service is designed from the user's need, not from the organisation chart. | The user must know which department does what |
| 7 | Natural Digital Environment | The service reaches people where they already are, before a new portal is built. | "We need our own portal" as the first answer |
| 8 | Public and Private Sector Co-creation | The change creates value with the private sector. It does not only automate an old internal procedure. | An old procedure is automated step by step and called transformation |
| 9 | Cross-border by Default | The service works for a person wherever they are. | Identity, payment or notice that assumes the person lives in the country |
| 10 | Intrinsic Security & Privacy | Security and privacy are part of the design from the start. | A security review after the design is fixed; a privacy assessment after launch |

**Where else the principles appear.** §3.3.2 (*Principles & Policies*) lists the same ten
for national digital infrastructure, with some titles worded differently — for example
"User-Centric Government" for Customer-centricity. §3.2.1 lists the principles of the
legal framework, which is a different and shorter list. Cite §3.3.2 for a national
policy, §5.2 for the roadmap of one body, and §3.2.1 for the legal framework.

**A principle with another name is not a §5.2 principle.** If a draft or a course page
names a principle that is not one of the ten titles above — for example *technology
neutrality* or *data as a managed asset* — say so. Give the nearest §5.2 principle, if
there is one. Do not quote §5.2 for a principle that it does not contain.

## Part B — The capability ladder (§5.1)

§5.1 assesses a body on five **dimensions**. They are also the sections of Chapter 4, so
the assessment and the reference architecture line up.

| Dimension | Chapter 4 section |
| --- | --- |
| Management | §4.2.1 |
| Architecture | §4.2.2 |
| Digital Services | §4.3 |
| Data-driven Decisions | §4.4 |
| Digital Co-creation | §4.5 |

The **levels**, in the kit's words. Read the indicators of each level on the page before
you assign one.

| Level (§5.1 title) | In short |
| --- | --- |
| Ground floor | The body has not yet delivered an automation project. A team of experienced people who have not yet delivered a project together also starts here. |
| 1st Level – Trust of Data | Management commits to IT investment; the architecture is documented; the body trusts its data, because its data is consolidated and its quality is managed. |
| 2nd Level – Process Management | All core and support processes are digital; services have service levels and processes have performance indicators, and both are reviewed. |
| 3rd Level – Change Management | The body can analyse the impact of a policy change and carry out a plan for the change. |
| 4th Level – Compliance Management | The body proposes policy changes itself; its platform is part of the national ecosystem. |

**The tests.**

- **The levels add up.** A body is at a level only when all indicators of the level
  below are met. So assess each dimension on its own, and take the **lowest** dimension as
  the level that limits the plan.
- **A level cannot be skipped.** §5.1 says that a body cannot jump a level. Capability
  comes from projects that the body has delivered, not from a budget or an order.
- **The common finding.** A roadmap that promises the results of level 3 to a body on the
  ground floor is not ambitious. It cannot be carried out. Name the level that the plan
  needs, the level that the body has, and the levels between them.

## Part C — The roadmap phases (§5.7)

§5.1 says what one body can absorb. §5.7 says how a country moves. Use it to test the
timeline of a national plan.

| Phase | § | What to check in the plan |
| --- | --- | --- |
| Inception | 5.7.2 | The plan starts with an honest assessment and with the legal and governance changes. §5.7.2 names three building blocks for this phase: identity, payment, and no-code/low-code development. |
| High-priority use cases | 5.7.3 | A few use cases are built fast, to show the value. §5.7.3 puts a consolidated portal for citizens and businesses here, if the country does not have one. |
| Initial transformation | 5.7.4 | §5.7.4 limits this phase to two to three years, and asks that all the main state registries of Annex 3 become digital in it. |
| Mass-scale transformation | 5.7.5 | All government services become digital. |

**The tests.**

- **The consolidated portal is national.** §5.7.3 puts it at the national level. One
  ministry that plans its own citizen portal fails Principle #7 and also takes on a
  national task.
- **Two to three years is one phase.** A plan that promises the whole transformation in
  three years puts four phases into the time that §5.7.4 gives to one. The plan must
  explain why.
