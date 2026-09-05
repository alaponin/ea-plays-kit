<!-- fixture: Progressa (fictional) · canonical: tests/progressa.md · keep consistent with it -->
# A worked example: the education sector of Progressa

Each fact here comes from `tests/progressa.md` §1, §6, §7, and the paragraph about the
problem of the sector. Progressa is fictional, so this example carries no sources.

Use it as a concrete model. Follow it, or compare your assessment of a real sector against
it.

---

## The bodies in the scope

| Body | Classification | Expected profile |
|------|---------------|-----------------|
| Ministry of Education, Youth and Skills (MoEYS) | Policy Unit | Sets the education policy and funds the schools. It operates the district EMIS, which has its own numbers for the learners |
| Progressa National Examination Authority (PNEA) | Service-Delivery Authority, with a regulatory role | Runs the examinations and certifies the results. It holds a list of candidates on its own numbers |
| Progressa Learner Registry (PLR) | State Registry | It must become the single list of the learners. Its status is **planned**. The Education Sector Plan 2023–2028 asks for it, and the government has not started it. It operates nothing and holds nothing now |
| Progressa National ID Authority (PNIA) | State Registry and Shared Platform | Owns the identity of a person. The National ID exists since 2018, and it covers 78% of the adults. e-KYC exists since 2024. It issues an ID only at 16 years |
| Progressa Digital Government Authority (PDGA) | Shared Platform | Coordinates the digital government and operates the shared data exchange, Linkup. Its mandate coordinates. It does not bind. It is a unit under the Ministry of ICT |
| Social Protection Agency | Service-Delivery Authority | Social grants. A vendor built its register of beneficiaries in 2016, under a World Bank programme |
| Civil Registration Department (Ministry of Interior) | State Registry | Registration of births and deaths. It works on paper first. It registers 71% of the births |
| Central Bank of Progressa | Shared Platform | Operates PayPro, the national system for fast payments |

The classification takes one minute. It tells you what to expect before the first interview.

**Read the PLR row two times.** The registry that would solve the problem of the sector does
not exist. Each finding below comes from its absence. No finding comes from its design.

**Read the Civil Registration row also.** Under the Civil Registration Act, it is the legal
anchor of the identity of a child. PNIA issues no ID before 16 years. Therefore the National
ID cannot be the key for a learner in a primary school.

---

## The Business layer

**Capabilities.** What each body can do:

| Capability | Owner |
|-----------|-------|
| Set the education policy and fund the schools | MoEYS |
| Run an examination | PNEA |
| Certify the result of an examination | PNEA |
| Prove the identity of a person of 16 years or more | PNIA |
| Establish the legal identity of a child | Civil Registration Department |
| Decide the eligibility for a social grant | Social Protection Agency |
| Exchange data between the bodies | PDGA |
| Settle a payment between two accounts | Central Bank of Progressa |
| Register a learner | **no owner.** The PLR that would own it is not started |

**Services.** How a capability reaches a citizen or another body:

| Service | Capability that it serves | Delivered by |
|---------|------------------|-------------|
| Enrol a child in a school | Register a learner | The school, on paper. The head teacher then types it into the district EMIS |
| Sit a national examination | Run an examination | PNEA, from its own list of candidates |
| Receive a certificate for an examination | Certify a result | PNEA |
| Receive a scholarship | Decide the eligibility, and settle a payment | MoEYS, by cheque |

**The result of the quality test**: ⚠️ The capabilities describe what each body does. One
capability has no owner. That is the finding. It is not an error of format.

**A gap that is confirmed**: MoEYS and PNEA each hold learner data, because their own
capabilities need it. The Social Protection Agency holds a third list. No body says that
"register a learner" is its capability. Nobody owns this capability, and three bodies hold
it. Nobody designed this.

---

## The Data layer

| Domain | Owner | Where the authoritative copy is | Bodies that use it |
|--------|-------|----------------------------|-----------------|
| Person of 16 years or more | PNIA | The National ID register | The tax authority, the business register, the members of Linkup |
| The legal identity of a child | Civil Registration Department | The civil register, on paper first | None, electronically |
| Learner | **none** | Three partial copies. None of them is authoritative | — |
| The result of an examination | PNEA | The Examination Authority | MoEYS |
| School | MoEYS | The school census | — |
| A beneficiary of a grant | Social Protection Agency | The register of beneficiaries (2016) | — |

**Is the once-only rule applied?** No. A parent proves the identity of the child on paper at
each counter, because no system trusts the record of another system.

**The result of the quality test**: ❌ One domain, the Learner, has no owner and no
authoritative copy.

**A gap that is confirmed, not suspected**: three systems hold the learner data. They are the
district EMIS, the list of candidates of PNEA, and the register of beneficiaries of the
Social Protection Agency. Each one uses its own numbers. The three lists do not agree.

---

## The Application layer

| Application | Capability that it serves | Data domains that it uses | Owner |
|------------|------------------|------------------|-------|
| District EMIS | Fund the schools; the school census | Learner (partial), School | MoEYS |
| Candidate management system | Run an examination; certify a result | Learner (partial), the result of an examination | PNEA |
| The National ID and e-KYC platform | Prove an identity, for 16 years and more | Person | PNIA |
| Linkup (X-Road 7.x) | Exchange data | All domains, for its four members | PDGA |
| Register of beneficiaries | Decide the eligibility | Learner (partial), a beneficiary of a grant | Social Protection Agency |
| PayPro | Settle a payment | — | Central Bank of Progressa |
| — | Register a learner | Learner | No application exists |

**The result of the quality test**: ⚠️ Each application points to a capability. The three
applications that hold the Learner domain each hold a different partial copy.

**The check across the layers**: three applications carry learner data, and no one of them
uses the data of another. There is no application to use, because the PLR is not started.

**A gap that is confirmed**: this is a duplicate registry, in the Data layer. It is also a
point-to-point problem, in the Technology layer, because a person reconciles the copies by
hand or in a spreadsheet.

---

## The Technology layer

| Component | Role | Standard |
|-----------|------|----------|
| The National ID and e-KYC platform (PNIA) | Issues and verifies an identity, for 16 years and more | It has a documented API. There is no framework for a sector to adopt it |
| Linkup (PDGA) | Routes data between the members, with an audit trail | X-Road 7.x. It is a live pilot with four members: PNIA, the business register, the tax authority, and PDGA |
| PayPro (Central Bank of Progressa) | Settles a payment between two accounts | The tax authority uses it. The scholarship programme still pays by cheque |
| e-Government Interoperability Framework 2021 | Names the message formats and the list of approved standards | It is published. Nobody applies it. Its governance committee does not meet |
| Government hosting | Hosts the systems of the sector | It has no standard |

**The result of the quality test**: ❌ An instrument for the standards exists, and nobody
applies it. The layer for exchange exists, and the education sector is not on it. **MoEYS is
not a member of Linkup.**

**The point-to-point finding is confirmed. It is not a risk.** A team built the link from the
tax authority to the business register as a direct link between two databases in 2022, before
Linkup existed. Nobody migrated it. MoEYS and the Ministry of Health exchange data in a
spreadsheet, on request. Both are point-to-point integrations, and they run next to a layer
for exchange that can carry them.

**The single points of failure**: Linkup and the National ID platform. No flow of the
education sector goes through them now. Therefore the risk to the sector is not that they
stop. The risk is that the sector is absent from them.

---

## The full trace

The service is: **sit an examination and receive a certificate**.

```
Service: Sit an examination; receive a certificate
  ↓ delivered by
Capability: Run-an-examination + Certify-a-result (owner: PNEA)
  ↓ supported by
Application: Candidate management system (owner: PNEA)
  ↓ uses
Data Domains: Examination result (owner: PNEA)
            + Learner — no owner; PNEA keeps its own candidate numbering
            + legal identity of the child (owner: Civil Registration Department, on paper)
  ↓ reached via
Technology: none — MoEYS is not a Linkup member; the school file reaches PNEA on paper
  ↓ running on
Technology: government hosting, not standardised
```

The trace is a complete architectural reading because it breaks. Two links are empty: the
owner of the Learner domain, and the route for the exchange. Each symptom that the minister
describes comes from those two gaps.

---

## The universal gaps in Progressa

| Gap | Status | Evidence |
|-----|--------|---------|
| Duplicate registries | **Confirmed** | Three systems hold a learner: the district EMIS, the list of candidates of PNEA, and the register of beneficiaries of the Social Protection Agency. Each one uses its own numbers, and the lists do not agree |
| Orphan systems | **Risk** | Section §3 names the files of the provincial secondary schools and the records at the school level. Nobody put them in an inventory |
| Point-to-point integration | **Confirmed** | The tax authority and the business register use a direct link between databases since 2022, and nobody migrated it. MoEYS and Health use a spreadsheet. Linkup has four members, and MoEYS is not one of them |
| No clear owner | **Confirmed** | The Learner domain has no owner. The PLR that would own it is not started |
| No function for standards | **Confirmed** | Section §6 records no function for data standards in the education sector. The 2021 Interoperability Framework is published, and nobody applies it |

---

## The architecture traps in Progressa

**The bespoke trap is present.** A vendor built the register of beneficiaries of the Social
Protection Agency in 2016, under a World Bank programme. The team did not assemble it from
the registries that the country shares. It is now the third place where a learner appears.
Four more systems that a donor funded have the same shape: five programmes across four
ministries, each one with its own needs for identity and for exchange, funded by three donors
on separate timetables. The National Learner Registry, at USD 6.5m, is the next system to
procure. Nothing yet obliges it to use PNIA and the civil register instead of building a
sixth list.

**The vendor-driven trap is present.** The same register from 2016 has one vendor for its
maintenance: the vendor that built it still holds the only maintenance contract. This is the
case of vendor lock-in in the fixture. It already happened. It is not a risk to prevent
later. Require an open format for export, and a market of more than one maintainer, before a
person signs the contract for the PLR. The counter-example already operates in the same
sector.
