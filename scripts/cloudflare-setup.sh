#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

UV_VERSION="${UV_VERSION:-0.11.23}"
UV_INSTALL_DIR="${UV_INSTALL_DIR:-$ROOT/.cache/cloudflare/bin}"
UV="$UV_INSTALL_DIR/uv"

if (($# == 0)); then
  APP_FILTERS=("@chartcoach/site" "@chartcoach/docs")
else
  APP_FILTERS=("$@")
fi

DEPENDENCY_FILTERS=()
for app_filter in "${APP_FILTERS[@]}"; do
  DEPENDENCY_FILTERS+=(--filter "$app_filter^...")
done

if [[ -x "$UV" ]] && "$UV" --version | grep -q "uv $UV_VERSION "; then
  "$UV" --version
else
  curl -LsSf "https://astral.sh/uv/$UV_VERSION/install.sh" | env UV_UNMANAGED_INSTALL="$UV_INSTALL_DIR" sh
fi

corepack enable
pnpm install --frozen-lockfile
"$UV" sync --locked --package chartcoach --no-dev
pnpm "${DEPENDENCY_FILTERS[@]}" --if-present build
