# 12 · Prove it worked

**Goal:** never trust "done". Name the check before you start. **Time:** 30 minutes.

Anthropic's own advice to engineers, in one line: *if you cannot verify it, do not ship it.* The same is true for you. The good news is that Claude can run the check for you, if you ask for it up front.

## Prepare

Copy `exercises/receipts` to your Desktop. It is twelve fake receipts as PDFs with useless names. Or use a copy of a real folder of receipts.

## Do this

1. Open the copy in the Code tab. Mode: **Plan**.
2. Send this. Notice the last sentence. That is the check, named before anything happens.
   ```
   Read every PDF in this folder. For each one, extract the date, the vendor, and the total. Put them in a file called expenses.csv with those three columns. Then propose renaming each PDF to the pattern YYYY-MM-DD_vendor_total.pdf. Show me the table before renaming anything. After renaming, open three PDFs at random, read them again, and confirm that their rows in expenses.csv match. Report any mismatch.
   ```
3. Read the table. Approve. Switch to **Manual** and say go.
4. Read the verification report at the end. Then do your own: open one PDF yourself and compare it to its row.

## The habit

Every time you give Claude a job, add one sentence at the end that says how you will both know it worked:

- *"Then re-open three at random and confirm."*
- *"Then count the files and tell me if the number changed."*
- *"Then show me the three rows you are least sure about."*

If you cannot think of a check, that is a sign the task is not clear yet. Go back to the interview.

## You are done when

`expenses.csv` exists, the PDFs have readable names, and you personally confirmed one row.

**Next:** [13 · How big is this?](13-how-big-is-this.md)
