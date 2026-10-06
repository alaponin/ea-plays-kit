# F-LD-01 — the return is confirmed on one screen, and moved on a form of another record

**What was missing.** The interaction design decides, in its Moves table, that the loan is moved to
returned by the button Confirm the return, which stands on the screen Confirm the return
(UC-LD-02-S02). That screen records a return: its values are the return's loan, condition and
fine. The model offers a move's button only on a form of the record that moves, so no one form can
both record the return and move the loan.

**Where the model needed it.** The act A01 of UC-LD-02-S02, and the form `frmReturn`.

**What was done.** The return is recorded on `frmReturn`, a form of the return, and the move is
offered as Confirm the return on `frmLoanReturned`, a form of the loan; the ledger records the
landing as an assumption. The kit's gate admits the model.

**Who is to answer.** The analyst who wrote the interaction design, to decide whether the return
screen is one act or two; and, if one, the delivery kit, for an act that moves the record a value
of the form names.

*A fixture of the method's application-model skill; the lending desk of Eastbrook does not exist.*
