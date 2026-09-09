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
    with urllib.request.urlopen(url, timeout=30) as response:
        for chunk in iter(lambda: response.read(1024 * 1024), b""):
            digest.update(chunk)
    if digest.hexdigest() != expected:
        raise ValueError(
            f"Published artifact bytes differ from the verified build: {url}"
        )


def npm_state(
    tarball: Path, *, download: bool = False, expected_version: str | None = None
) -> bool:
    with tarfile.open(tarball, "r:gz") as archive:
        manifest_file = archive.extractfile("package/package.json")
        if manifest_file is None:
            raise ValueError("npm tarball is missing package/package.json")
        manifest = json.load(manifest_file)
    version = manifest["version"]
    if manifest["name"] != "@chartcoach/catalog" or not re.fullmatch(
        r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", version
    ):
        raise ValueError("Expected @chartcoach/catalog with a stable X.Y.Z version")
    if expected_version is not None and version != expected_version:
        raise ValueError("Python and npm artifact versions differ")
    published = _read_json(
        f"https://registry.npmjs.org/@chartcoach%2Fcatalog/{version}"
    )
    if published is None:
        return False
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
    if download:
        _verify_download(published["dist"]["tarball"], expected, "sha512")
    return True


def check_release(directory: Path, *, allow_missing: bool = False) -> None:
    tarballs = list((directory / "npm").glob("*.tgz"))
    wheels = list((directory / "python").glob("chartcoach-*-py3-none-any.whl"))
    if len(tarballs) != 1 or len(wheels) != 1:
        raise ValueError("Expected exactly one npm tarball and one ChartCoach wheel")
    version = (
        wheels[0].name.removeprefix("chartcoach-").removesuffix("-py3-none-any.whl")
    )
    sdist = wheels[0].with_name(f"chartcoach-{version}.tar.gz")
    if not sdist.is_file():
        raise ValueError(f"Missing source distribution: {sdist}")
    if set((directory / "npm").iterdir()) != {tarballs[0]} or set(
        (directory / "python").iterdir()
    ) != {wheels[0], sdist}:
        raise ValueError(
            "Release must contain exactly one npm tarball, wheel, and source distribution"
        )
    npm_present = npm_state(
        tarballs[0], download=not allow_missing, expected_version=version
    )
    published = _read_json(f"https://pypi.org/pypi/chartcoach/{version}/json")
    files = {item["filename"]: item for item in published["urls"]} if published else {}
    for path in (wheels[0], sdist):
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
        if not allow_missing:
            _verify_download(artifact["url"], expected, "sha256")
    if not npm_present and not allow_missing:
        raise PendingPublication("npm has not published the verified tarball")


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
    check.add_argument(
        "--allow-missing",
        action="store_true",
        help="Permit versions and files awaiting publication.",
    )
    options = parser.parse_args()
    try:
        if options.command == "npm-state":
            print("published" if npm_state(options.tarball) else "publish")
        else:
            attempts = 1 if options.allow_missing else 6
            for attempt in range(attempts):
                try:
                    check_release(
                        options.directory, allow_missing=options.allow_missing
                    )
                    break
                except (OSError, ValueError) as error:
                    if not _retryable(error) or attempt == attempts - 1:
                        raise
                    print(f"Waiting for registry publication: {error}", file=sys.stderr)
                    time.sleep(5)
    except (OSError, ValueError, KeyError, tarfile.TarError) as error:
        parser.exit(1, f"Release registry check failed: {error}\n")


if __name__ == "__main__":
    main()
