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

## The criteria that select a building block

A GovStack building block must have these six properties:

- more than one sector or use case can reuse it;
- it is interoperable through open APIs;
- it uses open standards;
- a team can deploy it to a cloud;
- a team can deploy it on its own, because it is loosely coupled;
- it conforms to the GovStack specifications, and a person can test it against them and
  then put it in the GovStack Marketplace.

## Red flags

- A team builds a function that a building block already covers. This increases the
  fragmentation.
- A system serves one agency and one use case. This builds a silo.
- The system has no API layer. This limits the interoperability in the future.
- The system has no plan for its lifecycle or for its decommissioning. This creates a legacy
  system.
- The system does not align with the national interoperability platform. This makes an
  island.
