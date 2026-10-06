# The screens of Receive a returned item (UC-LD-02)

*A fixture of the method's interaction-design skill. The application is the lending desk of the
library of a town called Eastbrook, which does not exist; it belongs to no engagement. The
screen record is written in the fixture application's own form, which
`../screen_record_form.yaml` declares for the listing program.*

| Line | Entry |
|---|---|
| Use case | Receive a returned item (`UC-LD-02`), its description at version 1 |
| Primary actor | The desk librarian |
| Status and version | version 1 · baselined · accepted by Mara Lind on 22 September 2026 |

## UC-LD-02-S01 · Find the loan

| Id | Value | Record · attribute | Reference | List | Least it demands |
|---|---|---|---|---|---|
| V01 | Item barcode | item · barcode | — | — | must supply |
| V02 | Loan | return · loan | chosen from a result, told apart by loan · due date | — | must supply |
| V03 | Loan state | loan · state | — | — | may only read |

| Id | Act | Stands on | Leads to |
|---|---|---|---|
| A01 | Search | the screen | UC-LD-02-S01, the result |
| A02 | Choose this loan | a row of the result | UC-LD-02-S02 |

## UC-LD-02-S02 · Confirm the return

| Id | Value | Record · attribute | Reference | List | Least it demands |
|---|---|---|---|---|---|
| V01 | Condition on return | return · condition | — | L03 item condition | must supply |
| V02 | Loan | return · loan | carried from UC-LD-02-S01 | — | may only read |
| V03 | Fine due | return · fine | — | — | may only read |

| Id | Act | Stands on | Leads to |
|---|---|---|---|
| A01 | Confirm the return | the screen | ends the goal; the loan stands returned |
| A02 | Back | the screen | UC-LD-02-S01 |
