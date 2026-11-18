#!/usr/bin/env bash
# Scaffold a new tiny-* project: ./scripts/new-project.sh <name>
set -euo pipefail # enable strict mode for safer scripting

# Check for correct # of arguments, shows usage if incorrect
if [[ $# -ne 1 ]]; then
  echo "usage: $0 <name>   (e.g. $0 git -> projects/tiny-git)" >&2
  exit 1
fi

# Extract project name and set up directory paths
name="${1#tiny-}"
root="$(cd "$(dirname "$0")/.." && pwd)"
dir="$root/projects/tiny-$name"

# Check if project directory already exists, exit with error if it does
if [[ -e "$dir" ]]; then
  echo "error: $dir already exists" >&2
  exit 1
fi

# Create project directory structure and initial files
mkdir -p "$dir/notes" && touch "$dir/notes/.gitkeep"
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
