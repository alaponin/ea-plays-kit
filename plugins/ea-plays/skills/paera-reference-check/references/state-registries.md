# Key State Registries — PAERA Annex 3

Source: https://paera.govstack.global/8.-annex-3-main-state-registries

A state registry is a foundational component of the national digital infrastructure
(Section 3.4.2). It is the authoritative source of truth for its data, and it makes the
Once-Only principle possible.

## Core State Registries (Priority for Digitalisation)

### Population / Civil Registry
- **Data**: Citizens, residents, births, deaths, marriages, national IDs
- **Enables**: Digital identity, social services, voting, tax
- **Related BB**: Identity BB, Registration BB

### Business / Company Registry
- **Data**: Legal entities, ownership, directors, licenses
- **Enables**: Business services, regulatory compliance, tax collection
- **Related BB**: Registration BB, Workflow BB

### Land / Property Registry (Cadastre)
- **Data**: Land parcels, ownership, encumbrances, valuations
- **Enables**: Property transactions, urban planning, taxation
- **Related BB**: Registration BB, GIS BB

### Vehicle Registry
- **Data**: Vehicles, owners, insurance, technical inspections
- **Enables**: Road safety, law enforcement, taxation

### Tax Registry
- **Data**: Taxpayer IDs, filings, assessments, payments
- **Enables**: Revenue collection, compliance monitoring
- **Related BB**: Payment BB

### Health Registry / Patient Registry
- **Data**: Patients, health records, vaccinations, prescriptions
- **Enables**: Healthcare delivery, public health monitoring

### Education / Credentials Registry
- **Data**: Educational qualifications, certifications, diplomas
- **Enables**: Employment verification, regulatory compliance

### Social Benefits Registry
- **Data**: Beneficiaries, entitlements, payments
- **Enables**: Social protection programmes, duplicate detection

### Business Licensing Registry
- **Data**: Licenses, permits, validity, conditions
- **Enables**: Regulatory oversight, citizen verification

### Court / Legal Registry
- **Data**: Court decisions, enforcement orders, insolvencies
- **Enables**: Legal certainty, enforcement

## Questions to ask about a state registry

Ask these seven questions when you assess the registries of a country:

1. **Existence**: Does the registry exist in digital form?
2. **Authority**: Is it the official authoritative source, and not a copy?
3. **Quality**: Is the data current and accurate? Does somebody maintain it?
4. **Access**: Can another agency query it through an API or the interoperability platform?
5. **Legal basis**: Did an instrument establish the registry?
6. **Once-Only**: Does it stop another body from collecting the same data again?
7. **Privacy**: Does somebody control the access, and does the system log it?

## Maturity Indicators for Registries

| Level | Description |
|-------|-------------|
| Paper-based | The records are only on paper |
| Digitised | A person scanned the records or put them in a database. No API can query them |
| Digital | An API can query the registry. It answers in real time. It is authoritative |
| Interoperable | The registry connects to the national interoperability platform, the Information Mediator |
| Once-Only compliant | The registry gives the data to the bodies that need it, so that no MDA collects the data again |
