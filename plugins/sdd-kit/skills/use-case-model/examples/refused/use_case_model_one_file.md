# The allotment registry — use case model

*A fixture for the refusal side of the check. The same fictitious subject as the fixture beside
it, held in the one-file shape of the retired plugin for use case models: the survey written by hand inside
the model, no record header, no linked requirements, no format on any row and no glossary.
The gate of that plugin passed a model of this shape; the check of this skill refuses it.*

Document control: version 1.0.

## 1. Purpose, scope and how to read this model

### 1.1 Purpose

The allotment registry lets the residents of a town apply for a garden plot for the season,
lets the garden officer allocate the plots fairly and keep a waiting list, and keeps the record
of every allocation so that any one of them can be explained afterwards.

## 2. Conformance to the standard

The model is checked by the gate of the plugin it was written with.

## 3. The system under discussion

### 3.1 System boundary

The registry takes applications while the application window is open, confirms who is applying
and that they live in the town, allocates plots, keeps the waiting list, takes the plot rent
through the payment service, and records every allocation decision with its reason.

### 3.2 Design scope and altitude

The boundary is the software, treated black-box.

### 3.3 What is deliberately outside the boundary

The registry does not maintain the town's address data and does not handle money itself.

### 3.4 Governed switches on the boundary

None.

### 3.5 The governed-parameter register

| # | Parameter | Owner | Read by | Standing |
|---|---|---|---|---|
| P-1 | The length of the application window | The garden committee | AP-01 | Configuration |

### 3.6 Context diagram

Drawn by the document build.

### 3.7 The population this model acts on

Every resident of the town.

## 4. Actor catalogue

### 4.1 Primary actors — human roles

| ID | Actor | Goal | Note |
|---|---|---|---|
| AC-01 | **Resident** | To apply for a plot, pay for it and hold it for the season | May not allocate a plot |
| AC-02 | **Garden officer** | To allocate the plots fairly and keep the waiting list | May not apply for a plot |

### 4.3 Primary actor — time

| ID | Actor | Goal | Note |
|---|---|---|---|
| AC-03 | **Season calendar** | To open and close the application window each season | |

### 4.4 Supporting actors — external systems

| ID | Actor | Goal | Note |
|---|---|---|---|
| AC-04 | **Identity service** | Confirms who is applying | |
| AC-05 | **Address register** | Holds the residence data the registry reads | |
| AC-06 | **Payment service** | Settles the plot rent the registry requests | |

### 4.5 Offstage actors

| Actor | Interest |
|---|---|
| **Council auditor** | Requires that every allocation can be explained |

## 5. Package structure

| Package | Code | What it is about | Use cases | Maps to |
|---|---|---|---|---|
| **Applications** | AP | Taking an application from a resident during the window | 4 | |
| **Allocation** | AL | Giving plots out, taking the rent, keeping the waiting list | 5 | |
| | | **Total, derived by adding the column above** | **9** | |

## 6. Use case survey

### 6.1 Package AP — Applications

Taking an application from a resident during the application window.

| ID | Use case | Primary actor | Lv · Pri · St | Brief | Provenance |
|---|---|---|---|---|---|
| AP-01 | **Run the allotment season** | Season calendar | S · 1 · D | The application window opens and closes, and the season runs from the first application to the last allocation | — |
| AP-02 | **Apply for a plot** | Resident | U · 1 · B | The resident applies for a plot for the season and learns whether the application is accepted through the identity service and the address register | — |
| AP-03 | **Confirm the applicant's identity** | Resident | F · 2 · D | Who is applying is confirmed | — |
| AP-04 | **Check the applicant's residence** | Resident | F · 2 · D | That the applicant lives in the town is confirmed | — |

### 6.2 Package AL — Allocation

Giving plots out, taking the rent and keeping the waiting list.

| ID | Use case | Primary actor | Lv · Pri · St | Brief | Provenance |
|---|---|---|---|---|---|
| AL-01 | **Allocate a plot** | Garden officer | U · 1 · R | A free plot is given to the next accepted application | — |
| AL-02 | **Pay the plot rent** | Resident | U · 2 · D | The season's rent is paid through the payment service so that the plot can be handed over | — |
| AL-03 | **Place an applicant on the waiting list** | Garden officer | U · 2 · D | An accepted application that no free plot can serve is kept for later | — |
| AL-04 | **Record the allocation decision** | Garden officer | F · 2 · D | Each allocation decision is recorded with the reason for it | — |
| AL-05 | **Give up a plot** | Resident | U · 3 · D | A plot is given back during the season so that it can be allocated again | — |

## 7. Relationships

### 7.1 «include» register

| Included | Kind | Base use cases | Why it is factored out rather than written into each base |
|---|---|---|---|
| **AP-03 Confirm the applicant's identity** | subfunction | AP-02 | The same step whichever way the application arrives |
| **AP-04 Check the applicant's residence** | subfunction | AP-02 | The same step for every application |
| **AL-04 Record the allocation decision** | subfunction | AL-01 | Recorded the same way for every allocation |

### 7.2 «extend» register

| Extension | Base | Kind | Condition |
|---|---|---|---|
| **AL-02 Pay the plot rent** | AP-02 | optional | rent is due before the plot is handed over |
| **AL-03 Place an applicant on the waiting list** | AL-01 | optional | no plot is free |

### 7.3 Generalisation

None.

### 7.4 The relationships the model deliberately does not draw

Giving up a plot does not extend allocation.

## 8. Use case diagrams

Drawn by the document build.

## 15. The entity model

| Entity | One-line definition | Reconciliation |
|---|---|---|
| **Resident** | A person living in the town who may apply for a plot | named here |
| **Plot** | One garden plot the registry can allocate for a season | named here |
| **Application** | A resident's request for a plot in one season | named here |
| **Allocation** | The decision giving one plot to one application, with its reason | named here |
| **Waiting list entry** | An accepted application that no free plot could serve | named here |
| **Rent payment** | The payment of one plot's rent for one season | named here |
| **Season** | One growing season, with its application window | named here |

## 16. The business rules register

| ID | Statement | Kind | Authority | Cited by |
|---|---|---|---|---|
| BR-01 | A resident holds at most one application in a season | BEHAVIOUR | the garden committee | AP-02 |
| BR-02 | Only a resident of the town may apply | PROHIBITION | the garden committee | AP-04 |
| BR-03 | Plots are allocated in the order the applications were accepted | BEHAVIOUR | the garden committee | AL-01 |

## 17. Annexes

None.
