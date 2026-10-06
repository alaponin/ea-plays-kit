<!--
standard: SDD-07
title: The Screens of a Use Case
edition: "1.3"
document: SDD-07_The_Screens_of_a_Use_Case_v1.3.docx
sha256: edff1a9b30fa99a2f5737f572f477369bea31a3f2ea8de31254595c39c82f050
produced_by: _working/2026-08-31_house_rebuild/build_house.js at 2026-09-29T09:30:53Z
-->

# The screens of a use case

*The fixture of the skill use-case-screens: the screens of one goal, Renew a loan, of the loans module of the Eastbrook library system, a town that does not exist. It belongs to no engagement and specifies no system.*

*Written to SDD-07, The Screens of a Use Case, edition 1.3. Produced from the standard by `_working/2026-09-28_the_checklists/extract_checklist.py`, as the last step of its build; a copy of it is filled, and this file is never edited by hand. The quoted lines are the standard's own words.*

## 5 What a screen records — The record header

> Every screen carries a header, and every value in that header is stated once, in the header, and never again in the prose below it.

| The line | What is recorded | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference by which the set knows this screen. | not stated | `S1` |
| Name | What the person is doing here, in the words the business uses, from the actor's point of view. | not stated | Ask to renew a loan |
| Use cases | Every use case this screen serves, each with its version, and against each of them the numbered steps and variations of that use case which this screen serves. Usually there is one. | not stated | `UC-LN-02` Renew a loan, as it stood at SHA-256 73148b7c408f: step 1; variation *a |
| Primary actor | The actor of the use case. It is not a separate decision. Where a screen serves two use cases, both name the same actor, or the screen is really two screens, because a screen is what one person has in front of them. | not stated | The member. |
| Entities | The entities of the entity model this screen shows, and separately those it changes, by name only. | not stated | Shown: Copy. Changed: none. |
| Requirements realised | The identifiers of the requirements this screen serves, which are a subset of those the use case declares. | not stated | `F-1` |
| Business rules cited | The identifiers of the registered rules that govern this screen, which are a subset of those the use case cites. | not stated | None. |
| Quality requirements cited | The identifiers of the quality requirements that bind what a person sees here — or none, and none is an answer rather than an empty line. | not stated | None. |
| Status and version | Draft, reviewed or baselined, and the version. Those three words are the ones the standards beneath this one use, and no fourth word is used. | not stated | Draft, version 0.1 |

| The line | What is recorded | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference by which the set knows this screen. | not stated | `S2` |
| Name | What the person is doing here, in the words the business uses, from the actor's point of view. | not stated | Prove who you are |
| Use cases | Every use case this screen serves, each with its version, and against each of them the numbered steps and variations of that use case which this screen serves. Usually there is one. | not stated | `UC-LN-02` Renew a loan, as it stood at SHA-256 73148b7c408f: step 2; variations 3a, 4a and *a |
| Primary actor | The actor of the use case. It is not a separate decision. Where a screen serves two use cases, both name the same actor, or the screen is really two screens, because a screen is what one person has in front of them. | not stated | The member. |
| Entities | The entities of the entity model this screen shows, and separately those it changes, by name only. | not stated | Shown: Member. Changed: none. |
| Requirements realised | The identifiers of the requirements this screen serves, which are a subset of those the use case declares. | not stated | `F-1` |
| Business rules cited | The identifiers of the registered rules that govern this screen, which are a subset of those the use case cites. | not stated | `BR-1`, `BR-2` |
| Quality requirements cited | The identifiers of the quality requirements that bind what a person sees here — or none, and none is an answer rather than an empty line. | not stated | None. |
| Status and version | Draft, reviewed or baselined, and the version. Those three words are the ones the standards beneath this one use, and no fourth word is used. | not stated | Draft, version 0.1 |

| The line | What is recorded | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference by which the set knows this screen. | not stated | `S3` |
| Name | What the person is doing here, in the words the business uses, from the actor's point of view. | not stated | Confirm the renewal |
| Use cases | Every use case this screen serves, each with its version, and against each of them the numbered steps and variations of that use case which this screen serves. Usually there is one. | not stated | `UC-LN-02` Renew a loan, as it stood at SHA-256 73148b7c408f: steps 5 and 6; variations 6a and *a |
| Primary actor | The actor of the use case. It is not a separate decision. Where a screen serves two use cases, both name the same actor, or the screen is really two screens, because a screen is what one person has in front of them. | not stated | The member. |
| Entities | The entities of the entity model this screen shows, and separately those it changes, by name only. | not stated | Shown: Copy, Loan. Changed: Loan, Renewal. |
| Requirements realised | The identifiers of the requirements this screen serves, which are a subset of those the use case declares. | not stated | `F-1` |
| Business rules cited | The identifiers of the registered rules that govern this screen, which are a subset of those the use case cites. | not stated | `BR-5` |
| Quality requirements cited | The identifiers of the quality requirements that bind what a person sees here — or none, and none is an answer rather than an empty line. | not stated | None. |
| Status and version | Draft, reviewed or baselined, and the version. Those three words are the ones the standards beneath this one use, and no fourth word is used. | not stated | Draft, version 0.1 |

| The line | What is recorded | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference by which the set knows this screen. | not stated | `S4` |
| Name | What the person is doing here, in the words the business uses, from the actor's point of view. | not stated | Read the new due date |
| Use cases | Every use case this screen serves, each with its version, and against each of them the numbered steps and variations of that use case which this screen serves. Usually there is one. | not stated | `UC-LN-02` Renew a loan, as it stood at SHA-256 73148b7c408f: steps 7 and 8 |
| Primary actor | The actor of the use case. It is not a separate decision. Where a screen serves two use cases, both name the same actor, or the screen is really two screens, because a screen is what one person has in front of them. | not stated | The member. |
| Entities | The entities of the entity model this screen shows, and separately those it changes, by name only. | not stated | Shown: Loan, Renewal. Changed: none. |
| Requirements realised | The identifiers of the requirements this screen serves, which are a subset of those the use case declares. | not stated | `F-1` |
| Business rules cited | The identifiers of the registered rules that govern this screen, which are a subset of those the use case cites. | not stated | None. |
| Quality requirements cited | The identifiers of the quality requirements that bind what a person sees here — or none, and none is an answer rather than an empty line. | not stated | None. |
| Status and version | Draft, reviewed or baselined, and the version. Those three words are the ones the standards beneath this one use, and no fourth word is used. | not stated | Draft, version 0.1 |

| The line | What is recorded | Rule | Answer |
|---|---|---|---|
| Identifier | The stable reference by which the set knows this screen. | not stated | `S5` |
| Name | What the person is doing here, in the words the business uses, from the actor's point of view. | not stated | Learn that your identity could not be proved |
| Use cases | Every use case this screen serves, each with its version, and against each of them the numbered steps and variations of that use case which this screen serves. Usually there is one. | not stated | `UC-LN-02` Renew a loan, as it stood at SHA-256 73148b7c408f: variation 2a |
| Primary actor | The actor of the use case. It is not a separate decision. Where a screen serves two use cases, both name the same actor, or the screen is really two screens, because a screen is what one person has in front of them. | not stated | The member. |
| Entities | The entities of the entity model this screen shows, and separately those it changes, by name only. | not stated | Shown: none. Changed: none. |
| Requirements realised | The identifiers of the requirements this screen serves, which are a subset of those the use case declares. | not stated | `F-1` |
| Business rules cited | The identifiers of the registered rules that govern this screen, which are a subset of those the use case cites. | not stated | None. |
| Quality requirements cited | The identifiers of the quality requirements that bind what a person sees here — or none, and none is an answer rather than an empty line. | not stated | None. |
| Status and version | Draft, reviewed or baselined, and the version. Those three words are the ones the standards beneath this one use, and no fourth word is used. | not stated | Draft, version 0.1 |

## 11 What to write down

> This is the centre of the standard, and the promise it makes is that two specifiers answer the same questions. These are the questions. A screen set is finished when every line below has an answer or carries a written reason for having none.

### For each screen

| Line | Rule | Answer |
|---|---|---|
| The identifier, unique across the set, and the name — what the person is doing here, in the words the business uses. | not stated | `S1`; its name is in the record header. |
| The use cases this screen serves, each with its version, and against each of them the numbered steps and variations it serves. | not stated | Stated in the record header. |
| For a variation: whether it is a variation of a screen already in the set or a screen of its own, and why; and what it carries — what the actor may do about the condition, or what still holds despite the failure. | not stated | `*a` A variation of this screen, because the condition can arise at any step before step 7 and the member stays where they are, being told something different. It carries what still holds despite the failure: nothing is recorded, the loan keeps its due date, and the member is told that the request was interrupted. |
| The entities shown and, separately, the entities changed, by name only. | not stated | Stated in the record header. |
| The requirements realised, the business rules cited, and the quality requirements cited, by identifier — or none, and none is an answer rather than an empty line. | not stated | Stated in the record header. |
| For every value, where it came from, in one of the four ways; the authority, where it is consumed; the list, its owner, the strength of the binding and the clock that decides, where it is drawn from a governed list; that it is chosen and what tells the record apart, where it points at another record; and why it can be obtained no other way, where it enters the organisation here. | not stated | `S1.V1` The copy to be renewed — held here: this system is the authority for the copies of the library. It is a reference to a copy, chosen from the result of reading the copy's barcode and never typed, and what is stored is the copy's barcode number, which tells one copy apart from every other. |
| For every value, the least the screen demands and the most it admits, as two decisions — confirmed to be neither below the entity model's minimum nor mistaken for it. | not stated | `S1.V1` Must supply; admits one copy on loan to someone. The entity model requires it, and the screen demands no more. |
| For every rule cited, where it is cited and what its effect is at that place. No rule text. | not stated | None: no rule is cited on this screen. |
| Which act takes the person from this screen to which other screen, and which act raises which variation. | not stated | Ask to renew → `S2`<br>When the loans module becomes unavailable → raises `*a`<br>In `*a`: Leave → the use case ends in failure |
| The status and the version. | not stated | Stated in the record header. |

| Line | Rule | Answer |
|---|---|---|
| The identifier, unique across the set, and the name — what the person is doing here, in the words the business uses. | not stated | `S2`; its name is in the record header. |
| The use cases this screen serves, each with its version, and against each of them the numbered steps and variations it serves. | not stated | Stated in the record header. |
| For a variation: whether it is a variation of a screen already in the set or a screen of its own, and why; and what it carries — what the actor may do about the condition, or what still holds despite the failure. | not stated | `3a` A variation of this screen, because the use case ends in failure while the member is still looking at it, and the flow moves them nowhere else. It carries what the member may do about the condition: they are told that the loan is not on loan or that its due date has passed, so it cannot be renewed, and they may leave.<br>`4a` A variation of this screen, for the same reason. It carries what the member may do about the condition: they are told that the loan has been renewed as many times as the library allows, so it cannot be renewed again, and they may leave.<br>`*a` A variation of this screen, because the condition can arise at any step before step 7 and the member stays where they are, being told something different. It carries what still holds despite the failure: nothing is recorded, the loan keeps its due date, and the member is told that the request was interrupted. |
| The entities shown and, separately, the entities changed, by name only. | not stated | Stated in the record header. |
| The requirements realised, the business rules cited, and the quality requirements cited, by identifier — or none, and none is an answer rather than an empty line. | not stated | Stated in the record header. |
| For every value, where it came from, in one of the four ways; the authority, where it is consumed; the list, its owner, the strength of the binding and the clock that decides, where it is drawn from a governed list; that it is chosen and what tells the record apart, where it points at another record; and why it can be obtained no other way, where it enters the organisation here. | not stated | `S2.V1` The member — consumed from an authority elsewhere: the town's register of members. It is a reference to a member, chosen from the result of reading the member's library card and never typed, and what is stored is the member number, which tells one member apart from every other. |
| For every value, the least the screen demands and the most it admits, as two decisions — confirmed to be neither below the entity model's minimum nor mistaken for it. | not stated | `S2.V1` Must supply; admits one member in the register. The entity model requires it, and the screen demands no more. |
| For every rule cited, where it is cited and what its effect is at that place. No rule text. | not stated | `BR-1` at the act of proving who you are and continuing: when the loan is not on loan or its due date has passed, the renewal is refused and the member is told why, in variation `3a`.<br>`BR-2` at the same act: when the loan has reached the number of renewals the library allows, the renewal is refused and the member is told why, in variation `4a`. |
| Which act takes the person from this screen to which other screen, and which act raises which variation. | not stated | Prove who you are and continue → `S3`<br>Prove who you are, when the identity cannot be proved → `S5`<br>Prove who you are and continue, when the loan is not on loan or is past its due date → raises `3a`<br>Prove who you are and continue, when the loan has been renewed as often as the library allows → raises `4a`<br>When the loans module becomes unavailable → raises `*a`<br>In `3a`: Leave → the use case ends in failure<br>In `4a`: Leave → the use case ends in failure<br>In `*a`: Leave → the use case ends in failure |
| The status and the version. | not stated | Stated in the record header. |

| Line | Rule | Answer |
|---|---|---|
| The identifier, unique across the set, and the name — what the person is doing here, in the words the business uses. | not stated | `S3`; its name is in the record header. |
| The use cases this screen serves, each with its version, and against each of them the numbered steps and variations it serves. | not stated | Stated in the record header. |
| For a variation: whether it is a variation of a screen already in the set or a screen of its own, and why; and what it carries — what the actor may do about the condition, or what still holds despite the failure. | not stated | `6a` A variation of this screen, because the use case ends in failure while the member is still looking at it, and the flow moves them nowhere else. It carries what the member may do about the condition: they leave without confirming, nothing is recorded, and the loan keeps its due date.<br>`*a` A variation of this screen, because the condition can arise at any step before step 7 and the member stays where they are, being told something different. It carries what still holds despite the failure: nothing is recorded, the loan keeps its due date, and the member is told that the request was interrupted. |
| The entities shown and, separately, the entities changed, by name only. | not stated | Stated in the record header. |
| The requirements realised, the business rules cited, and the quality requirements cited, by identifier — or none, and none is an answer rather than an empty line. | not stated | Stated in the record header. |
| For every value, where it came from, in one of the four ways; the authority, where it is consumed; the list, its owner, the strength of the binding and the clock that decides, where it is drawn from a governed list; that it is chosen and what tells the record apart, where it points at another record; and why it can be obtained no other way, where it enters the organisation here. | not stated | `S3.V1` The copy's title — held here: this system is the authority for the copies of the library.<br>`S3.V2` The loan's due date — held here: this system is the authority for the loans.<br>`S3.V3` The due date the renewal would give — worked out: derived by the registered rule `BR-5` from the loan's due date and the library's loan policy. The screen carries a pointer to the rule and not the arithmetic. |
| For every value, the least the screen demands and the most it admits, as two decisions — confirmed to be neither below the entity model's minimum nor mistaken for it. | not stated | `S3.V1` May only read.<br>`S3.V2` May only read.<br>`S3.V3` May only read. |
| For every rule cited, where it is cited and what its effect is at that place. No rule text. | not stated | `BR-5` at `S3.V3`: the due date shown is the one the rule works out; the rule's text is in the register of business rules. |
| Which act takes the person from this screen to which other screen, and which act raises which variation. | not stated | Confirm the renewal → `S4`<br>Decide not to renew → raises `6a`<br>When the loans module becomes unavailable → raises `*a`<br>In `6a`: Leave → the use case ends in failure<br>In `*a`: Leave → the use case ends in failure |
| The status and the version. | not stated | Stated in the record header. |

| Line | Rule | Answer |
|---|---|---|
| The identifier, unique across the set, and the name — what the person is doing here, in the words the business uses. | not stated | `S4`; its name is in the record header. |
| The use cases this screen serves, each with its version, and against each of them the numbered steps and variations it serves. | not stated | Stated in the record header. |
| For a variation: whether it is a variation of a screen already in the set or a screen of its own, and why; and what it carries — what the actor may do about the condition, or what still holds despite the failure. | not stated | None: no variation of the use case leaves step 7 or step 8. |
| The entities shown and, separately, the entities changed, by name only. | not stated | Stated in the record header. |
| The requirements realised, the business rules cited, and the quality requirements cited, by identifier — or none, and none is an answer rather than an empty line. | not stated | Stated in the record header. |
| For every value, where it came from, in one of the four ways; the authority, where it is consumed; the list, its owner, the strength of the binding and the clock that decides, where it is drawn from a governed list; that it is chosen and what tells the record apart, where it points at another record; and why it can be obtained no other way, where it enters the organisation here. | not stated | `S4.V1` The loan's new due date — held here: the renewal recorded at step 7 gave it.<br>`S4.V2` The date the renewal was recorded — held here: this system records it when the renewal is made. |
| For every value, the least the screen demands and the most it admits, as two decisions — confirmed to be neither below the entity model's minimum nor mistaken for it. | not stated | `S4.V1` May only read.<br>`S4.V2` May only read. |
| For every rule cited, where it is cited and what its effect is at that place. No rule text. | not stated | None: no rule is cited on this screen. |
| Which act takes the person from this screen to which other screen, and which act raises which variation. | not stated | Finish → the use case ends in success |
| The status and the version. | not stated | Stated in the record header. |

| Line | Rule | Answer |
|---|---|---|
| The identifier, unique across the set, and the name — what the person is doing here, in the words the business uses. | not stated | `S5`; its name is in the record header. |
| The use cases this screen serves, each with its version, and against each of them the numbered steps and variations it serves. | not stated | Stated in the record header. |
| For a variation: whether it is a variation of a screen already in the set or a screen of its own, and why; and what it carries — what the actor may do about the condition, or what still holds despite the failure. | not stated | `2a` A screen of its own, because the use case ends in failure and the flow moves the member to be told so. It carries what the member may do about the condition: they are told that their identity could not be proved and that nothing was renewed, and they may leave. |
| The entities shown and, separately, the entities changed, by name only. | not stated | Stated in the record header. |
| The requirements realised, the business rules cited, and the quality requirements cited, by identifier — or none, and none is an answer rather than an empty line. | not stated | Stated in the record header. |
| For every value, where it came from, in one of the four ways; the authority, where it is consumed; the list, its owner, the strength of the binding and the clock that decides, where it is drawn from a governed list; that it is chosen and what tells the record apart, where it points at another record; and why it can be obtained no other way, where it enters the organisation here. | not stated | None: this screen shows no value. |
| For every value, the least the screen demands and the most it admits, as two decisions — confirmed to be neither below the entity model's minimum nor mistaken for it. | not stated | None: this screen shows no value. |
| For every rule cited, where it is cited and what its effect is at that place. No rule text. | not stated | None: no rule is cited on this screen. |
| Which act takes the person from this screen to which other screen, and which act raises which variation. | not stated | Leave → the use case ends in failure |
| The status and the version. | not stated | Stated in the record header. |

> A screen that answers only the name line has not been specified. It has been named.

### For the set as a whole

> This is the part filled in once, and it is the part most often not filled in at all.

| Line | Rule | Answer |
|---|---|---|
| How the set was worked out, and from what. | not stated | By walking the main success scenario and the extensions of `UC-LN-02` step by step, with the entity model of the loans module beside it, and not by walking the entity model. It is the fixture of the skill use-case-screens: the loans module of the Eastbrook library system, a town that does not exist, which belongs to no engagement and is not the specification of any system. |
| The use case and the version of it the set was worked out from; and which screens, if any, are shared with another use case. | not stated | `UC-LN-02` Renew a loan, as it stood at SHA-256 73148b7c408f: the use case's record header carries no line for a version, so the set names the file it was worked out from by its SHA-256, 73148b7c408f7fe1232498e37765501db024d7e3c014de82352b66c443a8fd4f. No screen is shared with another use case. The included use case Prove a member's identity, `UC-MB-01`, has no set of its own; its steps are served here, at step 2, on `S2`. |
| How many steps and variations there are, which of them are reached, and the written reason wherever one is not. | not stated | Eight steps and five variations. Steps 1 and 2 on `S1` and `S2`; steps 5 and 6 on `S3`; steps 7 and 8 on `S4`. Variation 2a on `S5`, a screen of its own; 3a and 4a on `S2`; 6a on `S3`; `*a` on `S1`, `S2` and `S3`.<br>No screen for step 3: the system confirms the loan's standing and presents nothing; when the loan does not qualify, what the member is told is variation `3a` on `S2`.<br>No screen for step 4: the system counts the loan's renewals and presents nothing; when the limit is reached, what the member is told is variation `4a` on `S2`. |
| The two lists of entities, and what reaches each of them. | not stated | Read: Member, shown on `S2`; Copy, shown on `S1` and `S3`; Loan, shown on `S3` and `S4`. Changed: Loan and Renewal, both on `S3`, where the member confirms the renewal. |
| The requirements, and what reaches each of them. | not stated | `F-1` reaches `S1` to `S5`. |
| The stakeholders' interests, with one sentence against each saying whether it is visible to the actor, together with who read them and when. | not stated | The member: to keep the copy longer and to be told the new due date — visible to the member on `S3` and `S4`. The head of circulation: that no loan is renewed against the library's loan policy — protected by the system at steps 3 and 4, and visible to the member only as the refusals `3a` and `4a` on `S2`; recorded as a sentence, not raised as a finding. The fines module: that the due date it counts overdue days from is the one the renewal gave — protected by the system and visible to nobody on these screens; recorded as a sentence. A member waiting for the copy: that a renewal keeps the copy from them no longer than the policy allows — protected by the system and visible to nobody on these screens; recorded as a sentence. Read by the author of this fixture on 29 September 2026. |
| How the walk-through is produced from the record, by whom, and when it was last produced. | not stated | By the kit's program `kit screens walk`, run by whoever changes this record, each time it changes; never written or corrected by hand. It was last produced on 29 September 2026, by the round that wrote this fixture, and the skill's fixture test produces it again on every run. |
| Which notation is used, and what that notation cannot say, with where each of those things is written instead. | not stated | One notation: an outline wireframe. Each screen is drawn as its name, its values in the order this record lists them, each value as its name beside an empty box, and its acts as buttons. It cannot say the size, weight, colour or position of anything, nor which control renders a choice: those belong to the enterprise standard for what a person sees and to the platform's pattern library. It cannot say what a value may hold, its type, length, format or permitted values: those are in the entity model. It cannot say the text of a rule: that is in the register of business rules. It cannot say how quickly or in which languages anything appears: those would be quality requirements, and none is cited here. |
| The statement of what agreeing to the walk-through commits the parties to, and what it does not. | not stated | Agreeing to this walk-through commits the parties to what is present on each screen, how it is grouped, in what order, and which screen follows which after what act. It does not commit them to any wording, layout, colour or size they happen to see, nor to any behaviour this record does not state. |
| What a later version may change and what it may not, written before there is a later version. | not stated | A later version may change a name, a hint or the order of values without a new identifier. A change to the use case a screen serves, or to the steps or variations it serves, produces a new screen with a new identifier and supersedes the old one; adding a use case to a screen does not, and removing one does. |
| Which screens are retired, and for each of them what replaced it or why nothing did. | not stated | None. |
| Who owns the set, who may propose a change, and who decides. | not stated | The owner of the skill use-case-screens owns this fixture. Anyone may propose a change, as a request to the owner, who decides. The use case changes first, then this record, and then the walk-through is produced again. |
| The level of detail the set was worked at, in the specifier's own words, applied consistently across every screen. | not stated | Every value the member reads or supplies, and no more; the same on all five screens. |
| The questions genuinely in dispute, each with a named owner and a date, and never closed by a silent default. | not stated | None. |
