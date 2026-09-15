# 06 · Rename the screenshots

**Goal:** watch Claude look at pictures, decide, and change your disk. **Time:** 15 minutes.

## Prepare (2 minutes)

1. Make a new folder on your Desktop called `claude-test`.
2. Copy 10 to 20 screenshots into it. On Windows they are usually in `Pictures\Screenshots`. **Copy, do not move.** Their names are probably things like `Screenshot 2026-08-14 101532.png`.

## Do this

1. Open the desktop app, click the **Code** tab.
2. Choose **Local**, click **Select folder**, pick `claude-test`.
3. Set the mode selector next to the send button to **Plan**.
4. Type this and send it:
   ```
   Look at each screenshot in this folder and propose a short descriptive name for it based on what is in the image. Show me a table: current name, proposed name. Do not rename anything yet.
   ```
5. Read the table. Change anything you dislike by replying, for example: *"Use Spanish for the names"* or *"Row 4 is a WhatsApp chat, not an email."*
6. When the table looks right, switch the mode to **Manual** and send:
   ```
   Go ahead and rename them exactly as in the table.
   ```
7. Claude will ask permission for each change. Click accept. Watch the counter change.
8. Open the folder in Windows Explorer. The files have new names.

## What just happened

A chat model can describe a picture. This one read twenty, made twenty decisions, asked you, and changed twenty real files. That is the whole difference, and you just saw it.

## If it goes wrong

- It renamed something badly: that is the next page.
- It did not ask permission and just did it: the mode was Auto. Switch to Manual. Nothing is lost, the files are a copy.

## You are done when

The files in `claude-test` have names you can read.

**Next:** [07 · Undo it](07-undo-it.md)
