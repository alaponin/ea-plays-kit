# The interaction design of the lending desk application — its first increment

## 1. The header

| Line | Entry |
|---|---|
| Identifier | IXD-LD-W1 — the interaction design of the lending desk application of the library of a town called Eastbrook, which does not exist, its first increment; a fixture of the method's interaction-design skill, belonging to no engagement |
| Version and status | version 1.0 · baselined · accepted by Mara Lind on 23 September 2026 |
| The goals it covers | the goals below, each by its description and its screen record, with their versions |
| The program of its listings | `../../scripts/listings.py`, SHA-256 `2fad6c0963159ddd8c78342b1082488ea312600672d7ccef40c6d6aa69b48878`; the form it reads, `screen_record_form.yaml`, SHA-256 `b112cd575ce36e12a8d5285ca9d31e8f95e02fc555beee527793874095374e39` |
| What it claims | "This interaction design claims conformance to the rules of this standard, IXD-1 to IXD-29." The claim rule by rule stands beside this document, in `_conformance/` |
| What the owner reads | the answer (section 2), the five tables (section 3) and the pages (section 4) |

| Goal | Its description | Its screen record |
|---|---|---|
| Lend an item to a member (`UC-LD-01`) | version 1 · baselined · accepted by Mara Lind on 22 September 2026 | version 1 · baselined · accepted by Mara Lind on 22 September 2026 |
| Receive a returned item (`UC-LD-02`) | version 1 · baselined · accepted by Mara Lind on 22 September 2026 | version 1 · baselined · accepted by Mara Lind on 22 September 2026 |

## 2. The answer

The two goals draw on three lists, all the library's own and none longer than nine; at three places
a person picks one record among many — a member, an item and a loan; one record, the loan, carries
a state the screens show, and the goals move it by two acts; and of the eight acts on the screens,
two open a form that carries a record. The owner is asked to accept the five tables below and the
two recommendations where the goals are silent. The goals are silent on how many members and items
the library holds, and on the words shown when a member may not borrow more.

## 3. The decisions

### 3.1 Lists — one row for each list the goals draw on

| List | Kept where | Members in force | Maintained or fixed | Maintained by | First values from | Code shown as label | Depends on | Categories | Pattern |
|---|---|---|---|---|---|---|---|---|---|
| Member category (`member_category`) | the library's own | 4 | maintained | the administrator (`role_admin`) | the entity model's members | no | nothing | none | L2 |
| Loan period (`loan_period`) | the library's own | 3 | fixed | nobody: fixed by the model | the entity model's members | no | nothing | none | L1 |
| Item condition (`item_condition`) | the library's own | 5 | maintained | the head librarian (`role_head_librarian`) | the entity model's members | no | nothing | none | L2 |

### 3.2 References — one row for each place a person picks a record

| Place | Record set | How many | Found by | Searched by | Result shows | Fills | Locks | When nothing is found | Pattern |
|---|---|---|---|---|---|---|---|---|---|
| Find the member to lend to (`frmLoan.member`) | the library's members | grows with operations; about 12,000 today — the goals are silent, and the figure is the library's annual report | a search | the card number first; a fragment of the name | card number, name, category | the member's name (`member_name`), the category (`member_category`) | everything it fills | "No member holds this card number. Check the card, or register the reader first." | S1, S2 |
| Find the item to lend (`frmLoan.item`) | the library's items | grows with operations; about 60,000 today — the same source | a search | the barcode first; a fragment of the title | barcode, title, whether it is on loan | the title (`item_title`) | everything it fills | "No item carries this barcode. Check the label." | S1, S2 |
| Find the loan of a returned item (`frmReturn.loan`) | the loans on loan or overdue | grows with operations; a few hundred at a time | a search | the item's barcode | barcode, title, member, due date | the due date (`due_date`) | everything it fills | "No open loan holds this item. Put it aside for the head librarian." | S1, S2 |

### 3.3 Moves — one row for each move a person makes

| Record | From | To | Made by (goal, act) | Role | Button | Guard, in the words shown |
|---|---|---|---|---|---|---|
| Loan (`loan`) | new (`new`) | on loan (`on_loan`) | UC-LD-01, Lend the item — the move `lend` | the desk librarian (`role_desk`) | Lend the item | "This member already holds the most items a member may hold." |
| Loan (`loan`) | on loan (`on_loan`) | returned (`returned`) | UC-LD-02, Confirm the return — the move `return_on_time` | the desk librarian (`role_desk`) | Confirm the return | none: a loan on loan may always be returned |
| Loan (`loan`) | overdue (`overdue`) | returned (`returned`) | UC-LD-02, Confirm the return — the move `return_late` | the desk librarian (`role_desk`) | Confirm the return | none: an overdue loan may always be returned, and the fine is shown |

### 3.4 Read-only — one row for each record with a state

| Record | State | Values read-only in it |
|---|---|---|
| Loan | on loan | the member, the item and the due date |
| Loan | returned | everything |

### 3.5 Acts — one row for each act that opens a form

| Act | Stands on | Carries | Opens | Filled and locked | Returns to | On a menu |
|---|---|---|---|---|---|---|
| Choose this member (UC-LD-01-S01, A02) | a row of the result of the member search (`frmFindMember`) | the member (`member`) | Record the loan (`frmLoan`) | the member's name and category | the desk's start page | no |
| Choose this loan (UC-LD-02-S01, A02) | a row of the result of the loan search (`frmFindLoan`) | the loan (`loan`) | Confirm the return (`frmReturn`) | the item, the member and the due date | the desk's start page | no |

## 4. The pages

No page is produced for this fixture. It tests the skill's steps and not the pages, and says so
here rather than leaving the part empty.

## 5. Where the goals were silent

| # | The goals are silent on | The recommended answer | The row that carries it |
|---|---|---|---|
| 1 | how many members and items the library holds | about 12,000 members and 60,000 items, from the library's annual report | References, rows 1 and 2 |
| 2 | the words shown when a member may not borrow more | "This member already holds the most items a member may hold." | Moves, row 1 |

## 6. The findings raised

| # | Against | The finding | Its owner |
|---|---|---|---|
| 1 | the shared groundwork | the register does not say what becomes of a loan still overdue at the end of the library's year | the groundwork's analyst |

## 7. Appendix: the listings, and their comparison with the screen records

The four listings below were produced by `../../scripts/listings.py`, SHA-256 `2fad6c0963159ddd8c78342b1082488ea312600672d7ccef40c6d6aa69b48878`, from the screen records named here, read in the form the application declares in `screen_record_form.yaml`, SHA-256 `b112cd575ce36e12a8d5285ca9d31e8f95e02fc555beee527793874095374e39`. Each listing is made by a first reading of the records and compared, as a set of whole entries, with the same listing made by a second reading, which calls none of the program's functions that the first calls and matches the form's patterns against the records' words without regard to case, to backticks and asterisks, or to runs of white space; the last table gives the comparison. The two readings have the form in common, so a value whose cell is written in other words than the form's is left out of a listing by both, and the comparison does not see it; each run of the program names every value it placed in no listing, to be read against the four listings.

| Screen record | SHA-256 | Its status, as it reads |
|---|---|---|
| `screens/UC-LD-01.md` | `04394c2e622437231bfeda5970d891451aee7aab35452fe3bb516c489ae7b46b` | version 1 · baselined · accepted by Mara Lind on 22 September 2026 |
| `screens/UC-LD-02.md` | `2a94df8cf3ea1549c3a9e3c91ba2ff558f2abeaa1f4a663b3477bf80a1569c20` | version 1 · baselined · accepted by Mara Lind on 22 September 2026 |

### 7.1 Every coded value, with the list it draws on

| Screen | Value | Name | List |
|---|---|---|---|
| UC-LD-01-S01 | V03 | Member category | L01 member category |
| UC-LD-01-S02 | V02 | Loan period | L02 loan period |
| UC-LD-02-S02 | V01 | Condition on return | L03 item condition |

### 7.2 Every value that points at another record, with whether the person picks it

| Screen | Value | Name | Record · attribute | Picked by the person |
|---|---|---|---|---|
| UC-LD-01-S01 | V02 | Member | loan · member | yes |
| UC-LD-01-S02 | V01 | Item | loan · item | yes |
| UC-LD-01-S02 | V05 | Member | loan · member | no |
| UC-LD-02-S01 | V02 | Loan | return · loan | yes |
| UC-LD-02-S02 | V02 | Loan | return · loan | no |

### 7.3 Every record whose state a screen shows

| Record | Screen | Value |
|---|---|---|
| loan | UC-LD-01-S02 | V04 |
| loan | UC-LD-02-S01 | V03 |

### 7.4 Every act, with where it stands and where it leads

| Screen | Act | Words | Stands on | Leads to |
|---|---|---|---|---|
| UC-LD-01-S01 | A01 | Search | the screen | UC-LD-01-S01, the result |
| UC-LD-01-S01 | A02 | Choose this member | a row of the result | UC-LD-01-S02 |
| UC-LD-01-S02 | A01 | Lend the item | the screen | ends the goal; the loan stands on loan |
| UC-LD-01-S02 | A02 | Cancel | the screen | ends the goal; nothing is saved |
| UC-LD-02-S01 | A01 | Search | the screen | UC-LD-02-S01, the result |
| UC-LD-02-S01 | A02 | Choose this loan | a row of the result | UC-LD-02-S02 |
| UC-LD-02-S02 | A01 | Confirm the return | the screen | ends the goal; the loan stands returned |
| UC-LD-02-S02 | A02 | Back | the screen | UC-LD-02-S01 |

### 7.5 The comparison with a second reading of the screen records, as sets

| Listing | First reading | Second reading | In both | Only in the first | Only in the second | Equal as sets |
|---|---|---|---|---|---|---|
| Every coded value, with the list it draws on | 3 | 3 | 3 | none | none | yes |
| Every value that points at another record, with whether the person picks it | 5 | 5 | 5 | none | none | yes |
| Every record whose state a screen shows | 2 | 2 | 2 | none | none | yes |
| Every act, with where it stands and where it leads | 8 | 8 | 8 | none | none | yes |
