# 01 · `tg init`: an empty repository

## The idea

A repository is just a folder with a known layout. `init` creates that layout
and nothing else: no boxes, no branches, no commits.

```
.tg/
├── HEAD            "ref: refs/heads/main\n"
├── objects/        (empty) the warehouse for boxes
└── refs/
    └── heads/      (empty) one sticky note per branch goes here
```

- **`objects/`**: where every box (blob, tree, commit) will be stored. Boxes
  never change; new ones are only added.
- **`refs/heads/`**: one small file per branch. The file `refs/heads/main`
  holds the fingerprint of the newest commit on `main`. Moving a branch means
  overwriting that file. These are the "sticky notes".
- **`HEAD`**: says which branch you're on. It doesn't hold a fingerprint, it
  points to a branch: `ref: refs/heads/main`.

So there are two levels: HEAD → branch → commit. `commit` follows HEAD to find
which branch to move. `checkout` only rewrites HEAD.

## The unborn branch

Right after `init`, HEAD says we're on `main`, but `refs/heads/main` doesn't
exist yet, because there's no commit for it to point to. Git calls this an
*unborn branch*. The first commit creates the file.

## How real Git does it

`git init` creates the same three things, plus extras we skip: `config`,
`description`, `hooks/`, `info/`, `objects/info`, `objects/pack`, `refs/tags`.
Git only needs HEAD, `objects/` and `refs/` to recognise a folder as a
repository.

Running `git init` twice is safe in real Git ("Reinitialized existing Git
repository"). `tg init` refuses instead, to keep things simple.

## What we implemented

- `cli.py`: an argparse parser with one subcommand per command.
  `set_defaults(func=...)` connects a subcommand to the function that runs it,
  and `main()` calls `args.func(args)`. Passing `args` lets each command read
  its own options later (e.g. `tg commit -m`).
- `commands.py`: `init_repo` refuses if `.tg/` exists, otherwise creates
  `HEAD`, `refs/heads/` and `objects/`.

## Gotchas

- `mkdir(parents=True)` creates missing parent folders too, so creating
  `refs/heads` also creates `refs`.
- Check for an existing `.tg/` *before* creating anything, so a second `init`
  never damages the existing repository.
- HEAD must end with a newline, exactly like Git writes it.

## Verify with real Git

```sh
git --git-dir=.tg symbolic-ref HEAD
# refs/heads/main
```

If Git answers this, it accepted `.tg/` as a repository and read our HEAD
file. Tests: `tests/test_init.py`.
