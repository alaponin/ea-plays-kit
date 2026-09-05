# Key State Registries — PAERA Annex 3

Source: https://paera.govstack.global/8.-annex-3-main-state-registries

State registries are a foundational component of national digital infrastructure (Section 3.4.2).
They serve as the authoritative source of truth and enable the Once-Only principle.

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

## Assessment Questions for State Registries

When assessing a country's registry landscape, check:
1. **Existence**: Does the registry exist in digital form?
2. **Authority**: Is it the official authoritative source (not a copy)?
3. **Quality**: Is data current, accurate, and regularly maintained?
4. **Access**: Can other agencies query it via API/interoperability platform?
5. **Legal basis**: Is the registry legally established?
6. **Once-Only**: Does it eliminate re-collection of the same data elsewhere?
7. **Privacy**: Is access controlled and logged?

## Maturity Indicators for Registries

| Level | Description |
|-------|-------------|
| Paper-based | Records exist only on paper |
| Digitised | Scanned or entered into a database, not queryable via API |
| Digital | Queryable via API, real-time, authoritative |
| Interoperable | Connected to national interoperability platform (Information Mediator) |
| Once-Only compliant | Proactively shared so no MDA needs to re-collect the data |
