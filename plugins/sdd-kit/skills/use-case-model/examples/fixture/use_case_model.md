---
system: The allotment registry
standard: SDD-05
written_to: {edition: "2.1", sha256: "5fc156de61994b9d6255ee3e478cc582d7e271f68a0417eea1107190c038bdc7"}
version: "1.0"
owner: the registry's architect (a fictitious role of this fixture)
boundary: software
treatment: black-box
use_cases: use_cases
survey: survey.md
named:
  requirements: named_sets/requirements.md
  entity_model: named_sets/entity_model.md
  glossary: named_sets/glossary.md
  business_rules: named_sets/business_rules.md
  settings: {none: "No use case of this model reads a setting, so the model names no catalogue of settings."}
claim: _conformance/use_case_model.md_conformance.md
---

# The use case model — the allotment registry

*A fixture. The subject is fictitious and belongs to no engagement: a town's register of
allotment garden plots, invented so that the skill's check and render steps can be run against
a model whose every value is known.*

## 1. Purpose

The allotment registry lets the residents of a town apply for a garden plot for the growing
season, lets the garden officer allocate the plots fairly and keep a waiting list, and keeps
the record of every allocation so that any one of them can be explained afterwards.

## 2. The system under discussion

The system is the registry software. The treatment is black-box: the model states what the
registry does for the people and systems outside it, and nothing about how it does it.

### Inside the boundary

The registry takes applications while the application window is open, confirms who is
applying and that they live in the town, allocates plots, keeps the waiting list, takes the
plot rent through the payment service, and records every allocation decision with its reason.

### Deliberately outside the boundary

The registry does not maintain the town's address data, which it reads from the address
register, and it does not handle money itself, which the payment service settles. It does not
decide the rent, and it does not look after the gardens themselves.

## 3. The actors

| Actor | Kind | Is it a person? | The goal it brings, or the service it gives |
|---|---|---|---|
| Resident | primary | yes | To apply for a plot, pay for it and hold it for the season |
| Garden officer | primary | yes | To allocate the plots fairly and keep the waiting list |
| Season calendar | primary | no | To open and close the application window each season |
| Identity service | supporting | no | Confirms who is applying |
| Address register | supporting | no | Holds the residence data the registry reads |
| Payment service | supporting | no | Settles the plot rent the registry requests |
| Council auditor | offstage | yes | Never interacts; requires that every allocation can be explained |

## 4. The packages

| Package | Code | What it is about | Its use cases |
|---|---|---|---|
| Applications | AP | Taking an application from a resident during the window | UC-01, UC-02, UC-06, UC-07 |
| Allocation | AL | Giving plots out, taking the rent, keeping the waiting list | UC-03, UC-04, UC-05, UC-08, UC-09 |

### How the packages depend on one another

Allocation reads only applications that the Applications package has accepted; Applications
never reads an allocation. The season's summary goal sits in Applications because the window
it opens is where every season starts.

## 5. The survey

The survey is `survey.md`, generated from the record headers of the use case files by the
skill's `extract.py --write-survey`, and never written by hand.

## 6. Which supporting actor each use case calls on

| Use case | Supporting actors it calls on |
|---|---|
| UC-03 | Address register |
| UC-04 | Payment service |
| UC-06 | Identity service |
| UC-07 | Address register |

## 7. The relationships

### Included steps

| Included | Base use cases | Why it is written once |
|---|---|---|
| UC-06 | UC-02 | Confirming the applicant's identity is the same step whichever way the application arrives |
| UC-07 | UC-02 | The residence check is the same step for every application |
| UC-08 | UC-03 | The allocation decision and its reason are recorded the same way for every allocation |

### Optional steps

| Extension | Base | At the point | When |
|---|---|---|---|
| UC-04 | UC-02 | the application is accepted | rent is due before the plot is handed over |
| UC-05 | UC-03 | no plot is free | the applicant is placed on the waiting list |

### Generalisations

None.

### The relationships the model deliberately does not draw

Giving up a plot does not extend allocation: a resident gives a plot up at any moment of the
season, not at a point of another use case.

## 8. The diagrams

The diagrams are drawn from the record headers by the render step of the skill; the model
keeps no picture.

## 9. Which use cases are written out, and in what order

Applying for a plot is written out in full first: every resident passes through it, and it is
where the rules of the registry meet the residents. Allocating a plot is outlined next,
because the fairness of the allocation is the second risk. The rest stay brief until their
value is known.
