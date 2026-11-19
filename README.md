# tiny-tech

A monorepo of small, from-scratch reimplementations of real technology,
built to understand how things work.

Website: https://johannesemme.github.io/tiny-tech/

## Projects

| Project | What it is | Notes | Status |
| ------- | ---------- | ----- | ------ |
| [tiny-git](projects/tiny-git) | A minimal Git: commits, branches, checkout, merge | [notes](projects/tiny-git/notes/) | 🚧 |

## Layout

```
tiny-tech/
├── projects/            # one directory per tiny-* project
│   └── tiny-<name>/
│       ├── README.md    # what it does, how to run it, what's left out
│       └── notes/       # what we learned, one note per step
├── playground/          # where the projects get used and tried out
│   ├── pyproject.toml   # one Python env with every project installed (editable)
│   └── tiny-<name>/     # experiments for each project
└── scripts/
    └── new-project.sh   # scaffold a new project
```

Each project is self-contained: its own language, dependencies, and tooling.
Nothing is shared between projects unless it is clearly worth it.

## Playground

`projects/` is where each tiny-* project is **built**. `playground/` is where
they are **used**: it's the place to try a project out by hand, the way a real
user would, and to experiment with what it can do.

- **One folder per project.** For example, `playground/tiny-git/` is a folder
  of sample files where you run `tg init`, `tg add`, `tg commit` and so on.
- **Committed and public.** The playground is part of the repo, so others can
  see what each project was tried on and what it produced.
- **One shared Python environment.** `playground/pyproject.toml` installs every
  Python project into `playground/.venv`. Projects are installed in *editable*
  mode, which means the playground always runs the latest code in `projects/`
  without reinstalling. It also means projects can be imported and combined,
  e.g. `import tiny_git` in a script here.

### Using it

Set up the environment once (and again whenever a project is added):

```sh
cd playground
uv sync
```

Then go into a project's folder and use it. For tiny-git:

```sh
cd tiny-git
uv run tg init           # or activate the environment once with
                         # `source ../.venv/bin/activate` and then just run `tg init`
```

### Adding a project to the playground

1. In `playground/pyproject.toml`, add the project to `dependencies` and point
   to its folder under `[tool.uv.sources]`, the same way `tiny-git` is set up.
2. Create a folder for it: `playground/tiny-<name>/`.
3. Run `uv sync`.


## Starting a new project

```sh
./scripts/new-project.sh git    # can be used to creste e.g. projects/tiny-git
```

## Conventions

- **Educational first.** The point is to learn how the real thing works.
  Each project keeps its learnings in `projects/tiny-<name>/notes/`.
- **Small on purpose.** Implement the core idea; skip the long tail. Each
  project's README says what was deliberately left out.
- **Self-contained.** A project builds and runs from its own directory.
- **Readable over clever.** The code is the documentation.
