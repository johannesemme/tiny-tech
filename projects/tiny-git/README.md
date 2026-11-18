# tiny-git

A tiny Git, written in Python to learn how Git works on the inside.
The command is `tg`.

## Goal

Use `tg` on a real folder of code, the way you'd use `git`:

```sh
tg init
tg add src/ README.md
tg commit -m "First commit"
tg branch experiment
tg checkout experiment
# ...edit, add, commit...
tg checkout main
tg merge experiment
tg log
```

`tg` stores its repository in a `.tg/` folder, using exactly the same format
real Git uses inside `.git/`. Only the folder name differs, so `tg` repos can
live inside the tiny-tech repo (in `playground/tiny-git/`) and be committed
like normal files.

Real `git` can still read a `tg` repo, which we use to check that `tg` is
correct:

```sh
git --git-dir=.tg --work-tree=. log
```

## Run

```sh
cd ../../playground && uv sync     # once
cd tiny-git
uv run tg init
```

## Test

```sh
uv run --group dev pytest          # from projects/tiny-git
```

## What's implemented

| Command | What it does |
| ------- | ------------ |
| `tg init` | Create an empty repository in the current folder |
| `tg add <paths...>` | Stage files for the next commit; a folder adds everything in it |
| `tg commit -m <msg>` | Save the staged files as a new commit on the current branch |
| `tg log` | Show the commits on the current branch, newest first |
| `tg branch` | List branches and mark the current one |
| `tg branch <name>` | Create a new branch at the current commit |
| `tg checkout <branch>` | Switch to a branch and update the files to match. Refuses if you have uncommitted changes |
| `tg merge <branch>` | Merge another branch into the current one (see below) |

### How `tg merge` behaves

- **Only the other branch has new commits:** the current branch just moves
  forward to it (a "fast-forward"). No merge commit is made.
- **Both branches have new commits:** changes are combined and a merge commit
  with two parents is created.
  - Changes to different files, or to different parts of the same file, are
    combined automatically.
  - If both branches changed the same lines, it's a **conflict**: `tg` writes
    both versions into the file between `<<<<<<<`, `=======` and `>>>>>>>`
    markers and stops. You fix the file, then `tg add` it and `tg commit`
    to finish the merge.
- Refuses to start if you have uncommitted changes.

The commit author is read from the environment variables `TG_AUTHOR_NAME` and
`TG_AUTHOR_EMAIL`, so there's no config file.

## Deliberately left out

- `status`, `diff`, `rm`, `rebase`, `stash`, `tag`, `merge --abort`
- Remotes: `clone`, `push`, `pull`, `fetch`
- Committing a file deletion (that needs `rm`)
- `.gitignore`: only `.git/` itself is skipped
- Checking out a commit hash directly (detached HEAD), and deleting branches
- Packfiles, config files, hooks
- The `.git/` folder name: `tg` uses `.tg/` (same contents, see above)

Any of these can be added later as a stretch goal.

## Learnings

See [`notes/`](notes/): one note per step, in order.
