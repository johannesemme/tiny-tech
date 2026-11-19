# 00 · Background: what Git is and how it works

General notes on Git. For a concrete example with real boxes, see
[00-example-walkthrough](00-example-walkthrough.md).

## Why Git exists

- Version control answers "what did this look like before?", "who changed
  what?" and "how do several people work on the same files?".
- Older tools were either per-file (SCCS, RCS) or centralized (CVS,
  Subversion): one server held the history, and branching was painful.
- The Linux kernel used BitKeeper, a commercial *distributed* tool, until its
  free license was withdrawn in April 2005.
- Linus Torvalds wrote Git in a few days to replace it. His requirements:
  distributed, fast, and able to detect any corruption. Git managed its own
  code by 7 April 2005.
- The first version was about 1,000 lines of C. Most of today's Git is
  performance, networking and user experience; the core data model has
  never changed. That's why a tiny version is possible.

## The core idea

Git is a **save-game system for a folder**. A save is a *commit*.

It's built on three ideas:

1. **Fingerprints (hashes).** A hash function mixes every byte of some
   content into a fixed-size number. Same content → same fingerprint; change
   one byte → completely different fingerprint. Git uses SHA-1: 40 hex
   characters. Python has it in `hashlib`.
2. **A warehouse of boxes (objects).** Every piece of content is stored in a
   box named after its fingerprint. Boxes are never changed, only added.
3. **Sticky notes (refs).** Small files with a name that point to a save:
   branches like `main`, and `HEAD`, which says which branch you're on.

## How a box is made

Every box has the same shape:

```
<kind> <size>\0<content>
```

- `kind` says how to read the content: `blob`, `tree` or `commit`.
- `size` is the content's length in bytes (used to check the box is complete).
- `\0` is a zero byte that marks where the label ends.

The whole thing is fingerprinted with SHA-1, which gives the box its name.
Then it's compressed with zlib and stored. The fingerprint is calculated
*before* compressing.

## The three kinds of box

### File box (blob)

Only the file's *content*: no name, no folder.

```
blob <size>\0<file content>
```

- Made by `git add`.
- Two files with the same content share one blob.

### Folder box (tree)

A list of entries, one per file or subfolder, **sorted by name**:

```
tree <size>\0
<type> <name> <fingerprint>
<type> <name> <fingerprint>
...
```

| Type | Meaning | Fingerprint points to |
| ---- | ------- | --------------------- |
| `100644` | Normal file (any kind: .txt, .py, .png) | a blob |
| `100755` | Executable file | a blob |
| `040000` | Folder | another tree |

- Made by `git commit`, from the index.
- This is where file **names** are attached to content.
- Sorting means the same folder contents always give the same bytes, and so
  the same fingerprint.

### Save box (commit)

Plain text:

```
commit <size>\0
tree <fingerprint of the root folder box>
parent <fingerprint of the previous save>
author <name> <email> <seconds since 1970> <time zone>
committer <name> <email> <seconds since 1970> <time zone>

<message>
```

- Made by `git commit`.
- `tree`: points to the root folder box. Not the files themselves, but from
  it you can reach the whole snapshot.
- `parent`: the save before this one. The first save has none. These links
  are the history.
- `author` wrote the change; `committer` saved it. Usually the same person.
- An empty line, then the message.

## add vs commit

- `git add <file>`: makes the **file box** and records `path → fingerprint`
  in the **index** (staging area). The index is a flat list with full paths
  (like `src/app.py`) of everything the next save will contain. It isn't
  emptied after a commit.
- `git commit`: turns the index into **folder boxes** (bottom up, since a
  folder needs its children's fingerprints), then a **save box**, then moves
  the current branch's sticky note to the new save.

## Key properties

- **Every save is a full snapshot**, but only new content creates new boxes.
  Unchanged files and folders are reused by fingerprint.
- **Editing never changes an old box.** It creates a new one; old saves keep
  pointing to the old content, which is how you can go back.
- **A change ripples upwards**: file → its folder → parent folders → new save.
  Folders that don't contain the change are reused whole.
- **Deleting a file creates no box.** It's just missing from the next folder
  box. Older saves still have it.
- **Git doesn't track empty folders**, only files.
- **Git doesn't record changes or moves.** It stores snapshots, and works out
  what changed by comparing fingerprints between two saves.
