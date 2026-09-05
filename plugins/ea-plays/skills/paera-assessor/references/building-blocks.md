# GovStack Building Blocks Reference

Source: https://specs.govstack.global and https://paera.govstack.global

## Infrastructure Building Blocks (always needed)

| Building Block | Purpose | Typical Trigger |
|---------------|---------|-----------------|
| **Identity BB** | Digital identity, authentication, e-signature | Any personalised or legally binding transaction |
| **Payment BB** | Digital payment processing | Any transaction involving a fee |
| **Information Mediator (IM)** | Secure, decentralised data exchange between agencies (X-Road model) | Cross-agency data sharing; interoperability |
| **Registration BB** | Object and entity registration (businesses, land, vehicles, etc.) | Any registry function |
| **Workflow BB** | Business process automation, case management | Multi-step administrative processes |
| **Messaging BB** | Notifications (SMS, email, push) to citizens/businesses | Any service requiring status updates |
| **GIS BB** | Geographic data and mapping | Location-based services, land management |
| **Consent BB** | Citizen consent management for data sharing | GDPR/data protection compliance |
| **E-signature BB** | Electronic signing and verification | Legal documents, contracts, approvals |
| **QR Code BB** | Generation and verification of QR codes | Document verification, mobile access |
| **Adapters BB** | Legacy system integration | Connecting existing systems to BB ecosystem |
| **No-code/Low-code Development BB** | Rapid application development | Prototyping; fast-track delivery; quick wins |

## Functional Building Blocks (Phase 2+)

| Building Block | Purpose |
|---------------|---------|
| **MyGov / Citizen Portal** | One-stop-shop digital front-end for citizens and businesses |
| **Digital Wallet** | Citizen-held digital credentials and documents |
| **Analytics BB** | Data analytics and reporting |
| **Scheduler BB** | Appointment and scheduling services |
| **eMarketplace** | Government procurement and catalogues |
| **AI/ML BB** | Machine learning services for automation and decision support |

## Building Block Adoption by Phase

### Phase 1 (Inception)
- Identity BB
- Payment BB  
- No-code/Low-code Development BB

### Phase 2 (High-priority Use Cases)
- MyGov portal
- Information Mediator
- Registration BB
- GIS BB
- Workflow BB
- Messaging BB
- QR Code BB
- E-signature BB
- Adapters BB
- Consent BB

### Phase 3 (Initial Transformation)
- All infrastructure BBs above, at scale
- State registries digitalised

### Phase 4 (Mass Scale)
- All GovStack BBs deployed across entire public sector

## Key Selection Criteria for Building Blocks
A GovStack Building Block must be:
- Reusable across multiple sectors/use cases
- Interoperable via open APIs
- Based on open standards
- Cloud-deployable
- Independently deployable (loosely coupled)
- Compliant with GovStack specs (testable against defined specs → GS Marketplace)

## Red Flags (Anti-Patterns)
- Custom-building something a BB already covers → increases fragmentation
- Single-agency, single-use systems → silo development  
- No API layer → limits future interoperability
- No lifecycle/decommissioning plan → future legacy risk
- No alignment with national interoperability platform → island system
