# 16 · Your first saved command

**Goal:** turn a request you keep typing into a command you type once. **Time:** 20 minutes.

## What a saved command is

A small text file. When it exists, you can type `/its-name` in the Code tab and Claude runs the whole request. Anthropic calls these *skills*. You can think of them as saved prompts.

## Do this

1. Pick the request you have repeated most. The inventory from page 08 is a good first one.
2. In the Code tab, mode Manual, send:
   ```
   Create a skill called inventory. When I run it, write or update a file called INVENTORY.md in the current folder with a table of every file: name, folder, size, date modified, and a one-line description. Ask me nothing; just do it and tell me how many files you listed.
   ```
   Claude creates a folder `.claude/skills/inventory/` with a file `SKILL.md` inside. Accept it.
3. Open `SKILL.md`. It looks like this, and you can edit the words:
   ```
   ---
   name: inventory
   description: Write INVENTORY.md listing every file in this folder
   ---
   Write or update INVENTORY.md ...
   ```
4. Type `/inventory` and send. Watch it run without any further typing from you.

## Where it lives

Inside this folder, in `.claude/skills/`, so it works here. If you want a command everywhere, ask Claude to *"make this a personal skill instead"* and it moves it to your user folder.

## Ideas for your next three

- `/resumen` : summarize every new note since the last summary, in Spanish.
- `/recibos` : the receipts task from page 12, with its check built in.
- `/revisa` : read the document I name and list every claim that has no source.

## You are done when

You typed `/inventory` and got the file.

**Next:** [17 · Put it on a schedule](17-put-it-on-a-schedule.md)

*En español: [Habilidades (skills), documentación oficial](https://code.claude.com/docs/es/skills)*
