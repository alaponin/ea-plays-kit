# The screens of Lend an item to a member (UC-LD-01)

*A fixture of the method's interaction-design skill. The application is the lending desk of the
library of a town called Eastbrook, which does not exist; it belongs to no engagement. The
screen record is written in the fixture application's own form, which
`../screen_record_form.yaml` declares for the listing program.*

| Line | Entry |
|---|---|
| Use case | Lend an item to a member (`UC-LD-01`), its description at version 1 |
| Primary actor | The desk librarian |
| Status and version | version 1 · baselined · accepted by Mara Lind on 22 September 2026 |

## UC-LD-01-S01 · Find the member

| Id | Value | Record · attribute | Reference | List | Least it demands |
|---|---|---|---|---|---|
| V01 | Member card number | member · card number | — | — | must supply |
| V02 | Member | loan · member | chosen from a result, told apart by member · card number | — | must supply |
| V03 | Member category | member · category | — | L01 member category | may only read |

| Id | Act | Stands on | Leads to |
|---|---|---|---|
| A01 | Search | the screen | UC-LD-01-S01, the result |
| A02 | Choose this member | a row of the result | UC-LD-01-S02 |

## UC-LD-01-S02 · Record the loan

| Id | Value | Record · attribute | Reference | List | Least it demands |
|---|---|---|---|---|---|
| V01 | Item | loan · item | chosen from a result, told apart by item · barcode | — | must supply |
| V02 | Loan period | loan · period | — | L02 loan period | must supply |
| V03 | Due date | loan · due date | — | — | may only read |
| V04 | Loan state | loan · state | — | — | may only read |
| V05 | Member | loan · member | carried from UC-LD-01-S01 | — | may only read |

| Id | Act | Stands on | Leads to |
|---|---|---|---|
| A01 | Lend the item | the screen | ends the goal; the loan stands on loan |
| A02 | Cancel | the screen | ends the goal; nothing is saved |
