#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if (($# == 0)); then
  APP_FILTERS=("@chartcoach/site" "@chartcoach/docs")
else
  APP_FILTERS=("$@")
fi

DEPENDENCY_FILTERS=()
for app_filter in "${APP_FILTERS[@]}"; do
  DEPENDENCY_FILTERS+=(--filter "$app_filter^...")
done

corepack enable
pnpm install --frozen-lockfile
pnpm "${DEPENDENCY_FILTERS[@]}" --if-present build
