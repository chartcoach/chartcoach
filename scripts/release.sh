#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

usage() {
  cat <<'EOF'
Usage: ./scripts/release.sh check-version <release-tag>

Checks package identities and matching stable X.Y.Z versions. Tags may
include a leading "v". Does not change files or publish packages.
EOF
}

check_version() {
  local release_tag="${1:-}"
  if [[ "$#" != 1 || ! "$release_tag" =~ ^v?(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$ ]]; then
    usage
    exit 1
  fi

  uv version --package chartcoach --output-format json | node -e '
    const python = JSON.parse(require("node:fs").readFileSync(0, "utf8"));
    const npm = require("./packages/catalog/package.json");
    const tag = process.argv[1];
    if (python.package_name !== "chartcoach" || npm.name !== "@chartcoach/catalog") {
      console.error("Expected chartcoach and @chartcoach/catalog package identities");
      process.exitCode = 1;
    } else if (python.version !== npm.version) {
      console.error(`Python package version ${python.version} does not match npm package version ${npm.version}`);
      process.exitCode = 1;
    } else if (tag.replace(/^v/, "") !== python.version) {
      console.error(`Package version ${python.version} does not match release tag ${tag}`);
      process.exitCode = 1;
    }' "$release_tag"
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
