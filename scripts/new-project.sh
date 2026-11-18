#!/usr/bin/env bash
# Scaffold a new tiny-* project: ./scripts/new-project.sh <name>
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $0 <name>   (e.g. $0 git -> projects/tiny-git)" >&2
  exit 1
fi

name="${1#tiny-}"
root="$(cd "$(dirname "$0")/.." && pwd)"
dir="$root/projects/tiny-$name"

if [[ -e "$dir" ]]; then
  echo "error: $dir already exists" >&2
  exit 1
fi

mkdir -p "$dir"
cat > "$dir/README.md" <<README
# tiny-$name

A tiny implementation of $name.

## Run

\`\`\`sh
# TODO
\`\`\`

## What's implemented

- TODO

## Deliberately left out

- TODO
README

echo "Created projects/tiny-$name"
echo "Remember to add it to the Projects table in README.md."
