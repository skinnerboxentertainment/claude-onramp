# 09 · The note Claude reads

**Goal:** give Claude standing instructions for a folder, in five lines. **Time:** 20 minutes.

Every time Claude Code opens a folder, it looks for a file called `CLAUDE.md` and reads it first. It is the Project instructions from stage 1, but for a folder. Whatever you write there, it will follow in every session.

## Prepare

Copy `exercises/notes` to your Desktop. It is nine short notes about a small website project. Or use a folder of your own notes.

## Do this

1. Code tab, **Select folder**, pick the notes copy. Mode: **Manual**.
2. Type `/init` and send. Claude reads the folder and writes a first draft of `CLAUDE.md`. Accept it.
3. Open `CLAUDE.md`. It will be too long. Delete everything Claude could work out by itself from the files. Keep only what a human would have to tell a new colleague. Aim for five lines. For example:
   ```
   These are working notes for the Saturday market website.
   Dates in file names are the date the note was written.
   When notes disagree, the newer note wins.
   Answer in Spanish.
   Never edit a note. Add a new one instead.
   ```
4. Save it. Now ask questions of the folder:
   ```
   What are the main themes across these notes?
   ```
   ```
   Which notes contradict each other? Quote both sides.
   ```
   In the sample notes, the deadline moves and the rule about showing prices changes. See whether it finds both.
5. Ask it to write a new note, `summary.md`, with the current state of the project in ten lines. Read it. Is it right?

## The rule for this file

Short beats long. A `CLAUDE.md` of five true lines works better than fifty. Anthropic's own advice: if the file gets long, it stops being followed.

## You are done when

`CLAUDE.md` exists, is short, and Claude answered two questions from the notes. **Stage 2 is complete.** You have watched Claude act on your files, safely, and you know how to stop it.

**Optional:** in the Code tab type `/powerup` for Anthropic's own short animated lessons. Print the [cheatsheet](../cheatsheet.md).

**Next:** [10 · The loop](../stage-3-structure/10-the-loop.md)

*En español: [Cómo Claude recuerda tu proyecto (oficial)](https://code.claude.com/docs/es/memory) · [¿Qué es Claude Code? Guía sin programar (C. Tala)](https://cristiantala.com/que-es-claude-code/)*
