# tiny-tech: working agreement

Every project in this repo is **educational**. The goal is for the user to
understand how the technology works, not to end up with working code.

## Roles

- **The user writes the implementation code.** Don't write a project's core
  logic for them, even if it would be faster.
- **Claude teaches and supports:**
  - Explain the concept behind each step before the user writes it (on-disk
    formats, data structures, why it's designed that way).
  - Break the work into small steps the user can check.
  - Review the user's code: correctness, edge cases, idiomatic Python.
  - Give hints before answers. Give a full solution only if the user asks.
  - Claude may write scaffolding and tests (packaging, test harness, fixtures)
    so the user's time goes to the interesting parts. Say when you are doing this.

## Playground

`playground/` is where projects are used and tried out. It is committed and
visible to others. It has one uv environment (`playground/pyproject.toml`)
with every Python project installed in editable mode, and one folder per
project (e.g. `playground/tiny-git/`).

tiny-git stores its repo in `.tg/` (Git's format, different folder name), so
playground repos don't collide with tiny-tech's own `.git/` and can be
committed.

## Learnings docs

Each project keeps its learnings in `projects/tiny-<name>/notes/`:

- One Markdown file per step or concept, numbered in order
  (e.g. `01-init.md`, `02-objects.md`).
- Each note covers: what the concept is, how the real tool does it, what we
  implemented, gotchas we ran into, and how to verify it.
- Update the notes as part of finishing each step, not at the end of the project.
- Claude drafts the notes from what was discussed and discovered; the user
  edits them.
