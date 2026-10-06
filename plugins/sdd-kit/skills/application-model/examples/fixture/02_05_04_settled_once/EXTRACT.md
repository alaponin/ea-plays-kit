# What the model of the lending desk reads from the documents settled once — an extract

*A fixture of the method's application-model skill: the lending desk of the library of a town
called Eastbrook, which does not exist; it belongs to no engagement. This file stands in for the
entity model, the shared registers and the architecture specification of the application, which
the fixture does not carry. It is an extract of the entries the model reads from them, and it
claims conformance to no standard. Each part names the document it stands in for.*

## 1. From the entity model

| Record | Attribute | Type | Relationship or list |
|---|---|---|---|
| member | card number | text, twelve characters | — |
| member | name | text | — |
| member | category | coded value | the governed list member category |
| item | barcode | text, fourteen characters | — |
| item | title | text | — |
| loan | member | reference | to member, told apart by the card number |
| loan | item | reference | to item, told apart by the barcode |
| loan | loan period | coded value | the governed list loan period |
| loan | due date | date | — |
| return | loan | reference | to loan, told apart by the due date |
| return | condition on return | coded value | the governed list item condition |
| return | fine due | amount of money | — |

| Governed list | Kept where | Values |
|---|---|---|
| member category | the library's own | adult, child, student, staff |
| loan period | fixed by the application | one week, two weeks, three weeks |
| item condition | the library's own | as new, good, worn, damaged, lost |

| Term | What it means |
|---|---|
| loan | one item lent to one member until its due date |

## 2. From the shared registers

| Kind | Entry |
|---|---|
| identity rule | a member is the same member when the card number is the same |
| state and move | a loan stands new, on loan, overdue or returned; it moves new to on loan when lent, on loan to overdue when its due date passes, and on loan or overdue to returned when returned |
| event | a loan becoming overdue is published to the library's notice service |
| setting | the most items a member may hold at once, set by the head librarian |

## 3. From the architecture specification

| Part | Entry |
|---|---|
| the application binding | the platform's version 9.0, enterprise edition, on a PostgreSQL database |
| a component switched on | the status framework, for the loan's states |
| an architecture decision | the fine is computed by the application, not by the finance system |
