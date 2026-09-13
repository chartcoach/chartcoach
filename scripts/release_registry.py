from __future__ import annotations

import argparse
import base64
import hashlib
import json
import re
import sys
import tarfile
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


class PendingPublication(ValueError):
    pass


def _read_json(url: str) -> dict[str, Any] | None:
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        error.close()
        if error.code == 404:
            return None
        raise


def _digest(path: Path, algorithm: str) -> str:
    digest = hashlib.new(algorithm)
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _verify_download(url: str, expected: str, algorithm: str) -> None:
    if not url.startswith("https://"):
        raise ValueError(f"Registry returned a non-HTTPS artifact URL: {url}")
    digest = hashlib.new(algorithm)
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            for chunk in iter(lambda: response.read(1024 * 1024), b""):
                digest.update(chunk)
    except urllib.error.HTTPError as error:
        error.close()
        if error.code == 404:
            raise PendingPublication(
                f"Registry artifact is not available yet: {url}"
            ) from error
        raise
    if digest.hexdigest() != expected:
        raise ValueError(
            f"Published artifact bytes differ from the verified build: {url}"
        )


def npm_manifest(tarball: Path) -> dict[str, Any]:
    with tarfile.open(tarball, "r:gz") as archive:
        manifest_file = archive.extractfile("package/package.json")
        if manifest_file is None:
            raise ValueError("npm tarball is missing package/package.json")
        return json.load(manifest_file)


def npm_artifact(
    tarball: Path, *, expected_version: str | None = None
) -> tuple[str, str] | None:
    manifest = npm_manifest(tarball)
    version = manifest["version"]
    if manifest["name"] not in {
        "@chartcoach/catalog",
        "chartcoach",
    } or not re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", version):
        raise ValueError(
            "Expected a ChartCoach npm package with a stable X.Y.Z version"
        )
    if expected_version is not None and version != expected_version:
        raise ValueError("Python and npm artifact versions differ")
    published = _read_json(
        f"https://registry.npmjs.org/{manifest['name'].replace('/', '%2F')}/{version}"
    )
    if published is None:
        return None
    expected = _digest(tarball, "sha512")
    integrity = "sha512-" + base64.b64encode(bytes.fromhex(expected)).decode("ascii")
    if (
        published.get("name") != manifest["name"]
        or published.get("version") != version
        or published["dist"].get("integrity") != integrity
    ):
        raise ValueError(
            f"npm {version} differs from the verified tarball. Stop publication."
        )
    return published["dist"]["tarball"], expected


def release_files(
    directory: Path, *, tag: str | None = None
) -> tuple[list[Path], Path, Path]:
    tarballs = list((directory / "npm").glob("*.tgz"))
    wheels = list((directory / "python").glob("chartcoach-*-py3-none-any.whl"))
    if len(tarballs) != 2 or len(wheels) != 1:
        raise ValueError("Expected two npm tarballs and one ChartCoach wheel")
    version = (
        wheels[0].name.removeprefix("chartcoach-").removesuffix("-py3-none-any.whl")
    )
    manifests = [npm_manifest(path) for path in tarballs]
    if {item["name"] for item in manifests} != {"@chartcoach/catalog", "chartcoach"}:
        raise ValueError("Expected chartcoach and @chartcoach/catalog npm packages")
    if any(item["version"] != version for item in manifests):
        raise ValueError("Python and npm artifact versions differ")
    sdist = wheels[0].with_name(f"chartcoach-{version}.tar.gz")
    if not sdist.is_file():
        raise ValueError(f"Missing source distribution: {sdist}")
    distributions = {
        path
        for folder in ("npm", "python")
        for path in (directory / folder).iterdir()
        if path.name.endswith((".whl", ".tar.gz", ".tgz"))
    }
    if distributions != {*tarballs, wheels[0], sdist}:
        raise ValueError(
            "Release must contain two npm tarballs, one wheel, and one source distribution"
        )
    if tag is not None and tag.removeprefix("v") != version:
        raise ValueError(
            f"Release tag {tag!r} does not match artifact version {version}"
        )
    return tarballs, wheels[0], sdist


def check_release(
    directory: Path, *, allow_missing: bool = False, tag: str | None = None
) -> None:
    tarballs, wheel, sdist = release_files(directory, tag=tag)
    version = wheel.name.removeprefix("chartcoach-").removesuffix("-py3-none-any.whl")
    npm = [npm_artifact(path, expected_version=version) for path in tarballs]
    published = _read_json(f"https://pypi.org/pypi/chartcoach/{version}/json")
    files = {item["filename"]: item for item in published["urls"]} if published else {}
    for path in (wheel, sdist):
        artifact = files.get(path.name)
        if artifact is None:
            if allow_missing:
                continue
            raise PendingPublication(f"PyPI has not published {path.name}")
        expected = _digest(path, "sha256")
        if artifact["digests"].get("sha256") != expected:
            raise ValueError(
                f"PyPI {path.name} differs from the verified build. Stop publication."
            )
    if any(item is None for item in npm) and not allow_missing:
        raise PendingPublication("npm has not published the verified tarball")
    if not allow_missing:
        for artifact in npm:
            assert artifact is not None
            _verify_download(artifact[0], artifact[1], "sha512")
        for path in (wheel, sdist):
            _verify_download(files[path.name]["url"], _digest(path, "sha256"), "sha256")


def _retryable(error: BaseException) -> bool:
    if isinstance(error, urllib.error.HTTPError):
        return error.code in {408, 425, 429, 500, 502, 503, 504}
    return isinstance(
        error,
        (PendingPublication, urllib.error.URLError, TimeoutError, ConnectionError),
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check release bytes against package registries."
    )
    commands = parser.add_subparsers(dest="command", required=True)
    npm = commands.add_parser(
        "npm-state", help="Print publish or published after checking npm integrity."
    )
    npm.add_argument("tarball", type=Path)
    check = commands.add_parser(
        "check", help="Verify both registry artifacts against a release build."
    )
    check.add_argument("directory", type=Path)
    check.add_argument("--tag", help="Require the artifacts to match this release tag.")
    check.add_argument(
        "--wait-seconds",
        type=int,
        default=120,
        help="Retry pending registry files and transient errors for this many seconds (default: 120).",
    )
    check.add_argument(
        "--allow-missing",
        action="store_true",
        help="Permit versions and files awaiting publication.",
    )
    options = parser.parse_args()
    if options.command == "check" and options.wait_seconds < 0:
        parser.error("--wait-seconds must be nonnegative")
    try:
        if options.command == "npm-state":
            print("published" if npm_artifact(options.tarball) else "publish")
        else:
            deadline = time.monotonic() + (
                0 if options.allow_missing else options.wait_seconds
            )
            while True:
                try:
                    check_release(
                        options.directory,
                        allow_missing=options.allow_missing,
                        tag=options.tag,
                    )
                    break
                except (OSError, ValueError) as error:
                    remaining = deadline - time.monotonic()
                    if not _retryable(error) or remaining <= 0:
                        raise
                    print(f"Waiting for registry publication: {error}", file=sys.stderr)
                    time.sleep(min(5, remaining))
    except (OSError, ValueError, KeyError, tarfile.TarError) as error:
        parser.exit(1, f"Release registry check failed: {error}\n")


if __name__ == "__main__":
    main()
