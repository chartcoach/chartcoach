#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

usage() {
  cat <<'EOF'
Usage: ./scripts/release.sh check-version <release-tag>

Checks that a GitHub release tag matches the package versions. Tags may
include a leading "v".
EOF
}

python_package_version() {
  uv version --short --package chartcoach
}

npm_package_version() {
  node -p "require('./packages/catalog/package.json').version"
}

check_version() {
  local release_tag="${1:-}"
  if [[ -z "$release_tag" ]]; then
    usage
    exit 1
  fi

  local python_version
  python_version="$(python_package_version)"
  local npm_version
  npm_version="$(npm_package_version)"

  local actual="${release_tag#v}"
  if [[ "$python_version" != "$npm_version" ]]; then
    printf 'Python package version %s does not match npm package version %s\n' "$python_version" "$npm_version" >&2
    exit 1
  fi

  if [[ "$actual" != "$python_version" ]]; then
    printf 'Package version %s does not match release tag %s\n' "$python_version" "$release_tag" >&2
    exit 1
  fi
}

case "${1:-}" in
  check-version)
    shift
    check_version "$@"
    ;;
  -h | --help)
    usage
    ;;
  *)
    usage
    exit 1
    ;;
esac
