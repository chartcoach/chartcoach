from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from release_registry import release_files

_VERSION = re.compile(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)\.dev([1-9]\d*)")


def command(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def gh(*args: str) -> str:
    return command("gh", *args)


def preview_version(commit: str) -> str:
    # Excluding the commit itself keeps its identity stable if it is tagged later.
    tags = command(
        "git", "tag", "--merged", f"{commit}^", "--sort=-v:refname"
    ).splitlines()
    finals = [
        tag
        for tag in tags
        if re.fullmatch(r"v?(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", tag)
    ]
    if not finals:
        raise ValueError(
            "No preceding stable release tag. Fetch full history and tags."
        )
    base = max(
        finals, key=lambda tag: tuple(map(int, tag.removeprefix("v").split(".")))
    )
    major, minor, patch = map(int, base.removeprefix("v").split("."))
    count = command("git", "rev-list", "--count", f"{base}..{commit}")
    return f"{major}.{minor}.{patch + 1}.dev{count}"


def stamp(root: Path, version: str) -> None:
    if _VERSION.fullmatch(version) is None:
        raise ValueError("Expected X.Y.Z.devN preview version")
    project = root / "packages/chartcoach/pyproject.toml"
    text, count = re.subn(
        r'^version = "[^"]+"$',
        f'version = "{version}"',
        project.read_text(),
        count=1,
        flags=re.MULTILINE,
    )
    if count != 1:
        raise ValueError("Missing Python package version")
    project.write_text(text)
    for relative in ("packages/catalog/package.json", "apps/chat/package.json"):
        path = root / relative
        manifest = json.loads(path.read_text())
        manifest["version"] = version.replace(".dev", "-dev.")
        path.write_text(json.dumps(manifest, indent=2) + "\n")


def package_names(version: str) -> list[str]:
    npm = version.replace(".dev", "-dev.")
    return [
        f"chartcoach-{version}-py3-none-any.whl",
        f"chartcoach-{version}.tar.gz",
        f"chartcoach-catalog-{npm}.tgz",
        f"chartcoach-{npm}.tgz",
    ]


def marker_name(version: str) -> str:
    return f"chartcoach-{version}-SHA256SUMS"


def provenance_name(version: str) -> str:
    return f"chartcoach-{version}-provenance.json"


def artifact_names(version: str) -> list[str]:
    return [*package_names(version), provenance_name(version)]


def checksum(directory: Path, version: str) -> Path:
    tarballs, wheel, sdist = release_files(directory, preview=True)
    if wheel.name != package_names(version)[0] or {p.name for p in tarballs} != set(
        package_names(version)[2:]
    ):
        raise ValueError("Preview artifact names do not match the requested version")
    path = directory / marker_name(version)
    path.write_text(
        "".join(
            f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n"
            for p in (
                wheel,
                sdist,
                *sorted(tarballs),
                directory / provenance_name(version),
            )
        )
    )
    return path


def provenance(commit: str, output: Path) -> None:
    env = os.environ
    repository = f"{env['GITHUB_SERVER_URL']}/{env['GITHUB_REPOSITORY']}"
    predicate = {
        "buildDefinition": {
            "buildType": "https://github.com/chartcoach/chartcoach/blob/main/development_docs/releasing.md#preview-provenance-v1",
            "externalParameters": {
                "checkoutCommit": commit,
                "workflow": {
                    "repository": repository,
                    "ref": env["GITHUB_REF"],
                    "path": ".github/workflows/publish.yml",
                },
            },
            "resolvedDependencies": [
                {
                    "uri": f"git+{repository}@{env['GITHUB_REF']}",
                    "digest": {"gitCommit": env["GITHUB_SHA"]},
                },
                {"uri": f"git+{repository}@{commit}", "digest": {"gitCommit": commit}},
            ],
        },
        "runDetails": {
            "builder": {
                "id": f"{env['GITHUB_SERVER_URL']}/{env['GITHUB_WORKFLOW_REF']}"
            },
            "metadata": {
                "invocationId": f"{repository}/actions/runs/{env['GITHUB_RUN_ID']}/attempts/{env['GITHUB_RUN_ATTEMPT']}"
            },
        },
    }
    output.write_text(json.dumps(predicate, indent=2) + "\n")


def assets() -> list[dict[str, Any]]:
    return json.loads(gh("release", "view", "preview", "--json", "assets"))["assets"]


def available(items: list[dict[str, Any]]) -> set[str]:
    return {
        item["name"]
        for item in items
        if item["state"] == "uploaded" and item["size"] > 0
    }


def resolve(commit: str) -> None:
    # Query the latest run rather than an older successful attempt.
    runs = json.loads(
        gh(
            "run",
            "list",
            "--workflow",
            "ci.yml",
            "--branch",
            "main",
            "--commit",
            commit,
            "--event",
            "push",
            "--limit",
            "1",
            "--json",
            "status,conclusion",
        )
    )
    if not runs or runs[0] != {"status": "completed", "conclusion": "success"}:
        raise ValueError("The latest main push CI must succeed for this exact commit")
    version = preview_version(commit)
    # A 404 is the only absent-release state; auth and API failures must surface.
    releases = json.loads(
        gh("api", "--paginate", "--slurp", f"repos/{os.environ['GH_REPO']}/releases")
    )
    release = next(
        (item for page in releases for item in page if item["tag_name"] == "preview"),
        None,
    )
    complete = release is not None and marker_name(version) in available(assets())
    with Path(os.environ["GITHUB_OUTPUT"]).open("a") as output:
        output.write(
            f"commit={commit}\nversion={version}\npublish={str(not complete).lower()}\n"
        )


def discovered_versions(items: list[dict[str, Any]]) -> list[str]:
    versions = set()
    for item in items:
        match = re.fullmatch(
            r"chartcoach(?:-catalog)?-(\d+\.\d+\.\d+)(?:\.dev|-dev\.)([1-9]\d*)(?:-py3-none-any\.whl|\.tar\.gz|\.tgz|-SHA256SUMS|-provenance\.json)",
            item["name"],
        )
        if match:
            versions.add(f"{match[1]}.dev{match[2]}")
    return sorted(
        versions,
        key=lambda version: tuple(map(int, version.replace(".dev", ".").split("."))),
        reverse=True,
    )


def publish(directory: Path, commit: str, version: str) -> None:
    repository = os.environ["GH_REPO"]
    downloads = f"https://github.com/{repository}/releases/download/preview"
    manifest = checksum(directory, version)
    paths = [
        directory / ("python" if name.endswith((".whl", ".tar.gz")) else "npm") / name
        for name in package_names(version)
    ]
    paths.append(directory / provenance_name(version))
    # Listing releases distinguishes an absent release from a failed API request.
    releases = json.loads(
        gh("api", "--paginate", "--slurp", f"repos/{repository}/releases")
    )
    if not any(item["tag_name"] == "preview" for page in releases for item in page):
        gh(
            "release",
            "create",
            "preview",
            "--prerelease",
            "--latest=false",
            "--target",
            commit,
            "--title",
            "Preview builds",
            "--notes",
            "Packages built from main.",
        )
    items = assets()
    uploaded = available(items)
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)

        def upload(path: Path) -> None:
            # Failed uploads leave starter assets, which contain no published bytes.
            if any(
                item["name"] == path.name and item["state"] == "starter"
                for item in items
            ):
                gh("release", "delete-asset", "preview", path.name, "--yes")
            if path.name in uploaded:
                gh(
                    "release",
                    "download",
                    "preview",
                    "--pattern",
                    path.name,
                    "--dir",
                    temporary,
                )
                if (root / path.name).read_bytes() != path.read_bytes():
                    raise ValueError(f"Published preview bytes differ: {path.name}")
            else:
                gh("release", "upload", "preview", str(path))

        for path in paths:
            upload(path)
        items = assets()
        uploaded = available(items)
        versions = discovered_versions(items)
        # An interrupted newer upload must not suppress notes or evict a
        # completed publication. This build joins completed builds provisionally;
        # its marker is committed only after all publication work succeeds.
        builds = [
            v
            for v in versions
            if set(artifact_names(v)) <= uploaded
            and (v == version or marker_name(v) in uploaded)
        ]
        cutoff = builds[29] if len(builds) >= 30 else None
        stale = versions[versions.index(cutoff) + 1 :] if cutoff else []
        wheel, _, catalog, chat = package_names(version)
        install = f'```console\nuv pip install "chartcoach @ {downloads}/{wheel}"\npnpm add "{downloads}/{catalog}"\nnpx --yes {downloads}/{chat}\n```'
        if os.environ.get("PRIVATE_REPOSITORY") == "true":
            install = (
                f"```console\nmkdir chartcoach-preview-{version}\ncd chartcoach-preview-{version}\n"
                f"gh release download preview -R {repository} --pattern '{wheel}' --pattern '{catalog}' --pattern '{chat}'\n"
                f"uv tool install --force ./{wheel}\nnpm init --yes\nnpm install --ignore-scripts ./{catalog}\n"
                "npm pkg set 'overrides.@chartcoach/catalog=$@chartcoach/catalog'\n"
                f"npm install --ignore-scripts ./{chat}\nnpx --no-install chartcoach\n```"
            )
        source_record = (
            f"Source provenance is recorded in `{provenance_name(version)}`; "
            "`buildDefinition.externalParameters.checkoutCommit` identifies the packaged source, "
            "and resolved dependencies record the workflow revision."
        )
        if os.environ.get("PREVIEW_ATTESTED") == "true":
            source_record += f" Verify signed provenance with `gh attestation verify {wheel} -R {repository}`."
        else:
            source_record += " This provenance record is unsigned; GitHub artifact attestations require a public repository or Enterprise Cloud."
        if builds[0] == version:
            notes = root / "notes.md"
            notes.write_text(
                f"Packages built from `main` after exact-commit CI passes. Latest: `{version}` from [{commit[:7]}](https://github.com/{repository}/commit/{commit}).\n\n{install}\n\nKeeps the newest 30 completed builds. Use PyPI and npm for stable releases. The preview tag stays on its original commit; versioned assets identify each build.\n\n{source_record}\n"
            )
            gh("release", "edit", "preview", "--notes-file", str(notes))
        if version not in stale:
            pulls = json.loads(gh("api", f"repos/{repository}/commits/{commit}/pulls"))
            pull = next(
                (
                    p["number"]
                    for p in pulls
                    if p["merged_at"] and p["base"]["ref"] == "main"
                ),
                None,
            )
            if pull is not None:
                pages = json.loads(
                    gh(
                        "api",
                        "--paginate",
                        "--slurp",
                        f"repos/{repository}/issues/{pull}/comments",
                    )
                )
                announcement_marker = f"<!-- chartcoach-preview:{version} -->"
                if not any(
                    announcement_marker in c["body"] for page in pages for c in page
                ):
                    body = root / "comment.md"
                    body.write_text(
                        f"{announcement_marker}\nchartcoach `{version}` from this PR is available as a [preview build](https://github.com/{repository}/releases/tag/preview):\n\n{install}\n"
                    )
                    gh("pr", "comment", str(pull), "--body-file", str(body))
        # Announce before pruning; commit the checksum marker only on completion.
        for old in stale:
            for name in [*artifact_names(old), marker_name(old)]:
                if any(item["name"] == name for item in items):
                    gh("release", "delete-asset", "preview", name, "--yes")
        if version not in stale:
            upload(manifest)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build and publish coordinated rolling previews."
    )
    parser.add_argument(
        "command",
        choices=("version", "stamp", "resolve", "checksum", "provenance", "publish"),
    )
    parser.add_argument("--commit")
    parser.add_argument("--version")
    parser.add_argument("--directory", type=Path, default=Path("dist/release"))
    parser.add_argument("--output", type=Path)
    options = parser.parse_args()
    if options.command in {
        "version",
        "resolve",
        "provenance",
        "publish",
    } and not re.fullmatch(r"[0-9a-f]{40}", options.commit or ""):
        parser.error("--commit must be a full lowercase commit SHA")
    if options.command in {"stamp", "checksum", "publish"} and not _VERSION.fullmatch(
        options.version or ""
    ):
        parser.error("--version must be X.Y.Z.devN")
    if options.command == "provenance" and options.output is None:
        parser.error("provenance requires --output")
    if options.command == "version":
        print(preview_version(options.commit))
    elif options.command == "resolve":
        resolve(options.commit)
    elif options.command == "stamp":
        stamp(Path.cwd(), options.version)
    elif options.command == "checksum":
        checksum(options.directory, options.version)
    elif options.command == "provenance":
        provenance(options.commit, options.output)
    else:
        publish(options.directory, options.commit, options.version)


if __name__ == "__main__":
    main()
