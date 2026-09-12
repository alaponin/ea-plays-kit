# The four layers — grading rules

The four layers are the European Interoperability Framework's (Commission Communication
COM(2017) 134, the interoperability layers): legal, organisational, semantic, technical,
under an overarching interoperability governance. Cite the EIF for the frame; cite the
registers for the grades.

| Layer | The question | Ready — needs all of | Partial | Missing | The register that answers |
| --- | --- | --- | --- | --- | --- |
| Technical | is there a shared bus or standard both sides can use? | a shared exchange layer **live** (not pilot, not planned); an approved transport standard (REST/OpenAPI or SOAP per the framework); both bodies able to connect (a Security Server or equivalent) | the bus is live but one or both bodies are not members; or the bus is in pilot | no bus; or the exchange is a database link or a file transfer | BB status register (data exchange row); A0 §1, §8 |
| Semantic | do both sides agree on the meaning, the identifiers and the code lists? | a published vocabulary or national standard for the entity, adopted by both, cited; one identifier both hold for the entity | one side documents its schema; a vocabulary is named but not adopted; the identifier is shared but its coverage is partial | different identifiers for the same entity; no documented schema; no vocabulary | A0 §1 (identifier landscape); the sector's data-standards function in A0 §6 (often absent) |
| Organisational | is there an agreement on who provides what, at what service level, under which governing body? | the provider's mandate to serve the data to other bodies; a governing body that meets; an agreement or service level between the two | a mandate exists but no agreement; a body exists but does not meet | no mandate; no body; no agreement | Bodies register; A0 §4, §6 |
| Legal | is there a lawful basis and a mandate to exchange, with data protection? | an instrument in force that gives the provider a basis to disclose and the consumer a basis to process this entity for this purpose; the data-protection act's conditions for this entity met (a statutory basis for a minor's data, for example); an operating DPA if the act requires one | an instrument exists but is not commenced, or covers the provider but not the consumer, or covers adults and not minors | no instrument; consent is the only basis and the use is statutory | Legal register; A0 §7, §10 |

## Rules

- **Evidence, not description.** A grade without a cited register row or source carries ⚠.
- **Live means live.** A pilot is Partial. Planned is Missing.
- **The identifier is a semantic fact.** If the entity is a person and the two bodies
  number people differently, the semantic layer is at best Partial regardless of the
  vocabulary.
- **Legal Ready is rare on a first pass.** Most countries have a data-protection act and
  no once-only basis; write Partial and name the gap the decree must close.
- **The binding constraint is the layer with the longest path to Ready**, measured in
  calendar time (legislation and budget cycles do not hurry), unless another layer stops
  the exchange outright today.

## The typical one action, by layer

| Layer | The one action | KP2 builds it in |
| --- | --- | --- |
| Technical | connect the two bodies to the live bus; or adopt the transport standard | Module 4 (4.1, 4.7), Module 5 (5.4) |
| Semantic | agree the vocabulary and the identifier in a semantic map | Module 4 (4.4) |
| Organisational | give the provider the mandate; charter the governing body; sign the agreement | Module 3 (3.1–3.4) |
| Legal | enact the lawful basis — the decree's once-only and data-protection articles | Module 2 (2.4), 4.8 |
