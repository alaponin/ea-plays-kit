# The PAERA sections, and what this kit carries

## The version that this kit records

This kit records **PAERA v1.0**, at **paera.govstack.global**. Confirm the version when you
run the skill. If the published version is different, use the published version and say so.
A change of PAERA version is a minor version bump for this kit, and it goes in the
CHANGELOG.

## Why the text of the annex is not in this file

The plan for this kit left one question open. It is not confirmed that the licence of PAERA
v1.0 permits a verbatim copy of its annexes. Until a person confirms this, the kit
**references each section by its number and reads the published specification again when the
skill runs**. The plan gives this as its fallback. It also has an advantage: the check is
against the current text, and not against a copy that becomes old.

When a person confirms the licence, a copy of Annex 2, Annex A1.2 and §5.2 in this file is a
minor version bump.

## The five foundations and their sections

The August 2026 run made this map. This skill makes the map again and verifies it.

| Foundation, as play 1.5 teaches it | PAERA section | What to check there |
| --- | --- | --- |
| **Taxonomy** — how a government classifies its public bodies | **§4.6**, with **Annex A1.2** | The seven types of body and their definitions |
| **Metamodel** — the shared vocabulary | **Annex 2** | The entity types, the relationship types, and what is *not* in the metamodel |
| **Building blocks** — the capabilities that a country reuses | The **GovStack building-block catalogue** | Which blocks have a specification, and at which maturity |
| **Principles** — the ten principles that govern a design | **§5.2** | The ten principles, as they are worded |
| **Methodology** — how a team does the work | **§5.1, §5.4, §5.7** | The approach, and the phases of the recommended roadmap |

Cite the section each time. "PAERA says" with no section is the failure that the safeguard
of play 1.5 catches.

## Other sections to know

| Section | Content |
| --- | --- |
| **§2.1** | The problem statement. Module 1 rests on this argument about fragmentation |
| **§2.3** | The role of enterprise architecture |
| **§4.6** | The taxonomy of bodies |
| **§5.2** | The ten principles, which include #5 Once-Only and #7 Natural Digital Environment |
| **§5.7** | The phases of the recommended roadmap |
| **Annex 2** | The metamodel |
| **Annex A1.2** | The full taxonomy of bodies |

## The three simplifications, in one place

| Where | Taught | Specification | How to report it |
| --- | --- | --- | --- |
| 2.2 | Six entity types and five relationships | Annex 2 in full | Write "conformant to the teaching subset only", and give the Annex 2 element that it must become |
| 2.4, 2.5, 4.1, 4.8 | Five types of body | The seven types in Annex A1.2 | Give the full type first and the teaching type in brackets. See `ea-institution-mapper` |
| 1.5 | "Five foundations" | The sections above | Make the map before the assessment |

None of the three is an error in the course. Each one is a deliberate reduction for an
explanation of four minutes. Each one stops being correct when the output becomes a
deliverable.
