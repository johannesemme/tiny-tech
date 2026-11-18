# tiny-tech

A monorepo of small, from-scratch reimplementations of real technology —
built to understand how things work, not to replace them.

## Projects

| Project | What it is | Status |
| ------- | ---------- | ------ |
| _none yet_ | | |

<!-- Add a row per project, e.g.
| [tiny-git](projects/tiny-git) | A minimal Git: objects, index, commits, branches | 🚧 |
-->

## Layout

```
tiny-tech/
├── projects/          # one directory per tiny-* project
│   └── tiny-<name>/
│       └── README.md  # what it does, how to run it, what's left out
└── scripts/
    └── new-project.sh # scaffold a new project
```

Each project is self-contained: its own language, dependencies, and tooling.
Nothing is shared between projects unless it is clearly worth it.

## Starting a new project

```sh
./scripts/new-project.sh git    # creates projects/tiny-git
```

## Conventions

- **Small on purpose.** Implement the core idea; skip the long tail. Each
  project's README says what was deliberately left out.
- **Self-contained.** A project builds and runs from its own directory.
- **Readable over clever.** The code is the documentation.
