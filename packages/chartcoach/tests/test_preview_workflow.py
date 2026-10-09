from __future__ import annotations

import hashlib
import importlib.util
import io
import json
import os
import subprocess
import tarfile
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest
import yaml

_ROOT = Path(__file__).parents[3]
_VERSION = "0.3.4.dev7"
_COMMIT = "a" * 40
_PREDICATE_TYPE = "https://github.com/chartcoach/chartcoach/blob/main/development_docs/releasing.md#preview-provenance-v1"


@pytest.fixture
def preview(monkeypatch: pytest.MonkeyPatch) -> ModuleType:
    monkeypatch.syspath_prepend(str(_ROOT / "scripts"))
    spec = importlib.util.spec_from_file_location(
        "preview_release", _ROOT / "scripts/preview_release.py"
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setenv("GH_REPO", "chartcoach/chartcoach")
    monkeypatch.setenv("PRIVATE_REPOSITORY", "false")
    monkeypatch.setenv("PREVIEW_ATTESTED", "false")
    return module


def build(directory: Path, version: str, *, sdk: str | None = None) -> Path:
    (directory / "python").mkdir(parents=True)
    (directory / "npm").mkdir()
    npm_version = version.replace(".dev", "-dev.")
    for name, filename in [
        ("@chartcoach/catalog", f"chartcoach-catalog-{npm_version}.tgz"),
        ("chartcoach", f"chartcoach-{npm_version}.tgz"),
    ]:
        manifest: dict[str, Any] = {"name": name, "version": npm_version}
        if name == "chartcoach":
            manifest["dependencies"] = {
                "@chartcoach/catalog": sdk
                or f"https://github.com/chartcoach/chartcoach/releases/download/previews/chartcoach-catalog-{npm_version}.tgz"
            }
        content = json.dumps(manifest).encode()
        with tarfile.open(directory / "npm" / filename, "w:gz") as archive:
            item = tarfile.TarInfo("package/package.json")
            item.size = len(content)
            archive.addfile(item, io.BytesIO(content))
    (directory / "python" / f"chartcoach-{version}-py3-none-any.whl").write_bytes(
        version.encode()
    )
    (directory / "python" / f"chartcoach-{version}.tar.gz").write_bytes(b"source")
    (directory / f"chartcoach-{version}-provenance.json").write_text(
        '{"buildDefinition": {}}'
    )
    return directory


@pytest.fixture
def distribution(tmp_path: Path) -> Path:
    return build(tmp_path / "release", _VERSION)


class GitHub:
    def __init__(self) -> None:
        self.exists = True
        self.immutable = False
        self.draft = False
        self.files: dict[str, bytes] = {}
        self.starters: set[str] = set()
        self.notes = ""
        self.comments: list[dict[str, str]] = []
        self.deleted: list[str] = []
        self.uploads: list[str] = []
        self.fail: str | None = None

    def __call__(self, *args: str) -> str:
        if self.fail and self.fail in args:
            raise subprocess.CalledProcessError(1, args)
        if args[0] == "api":
            endpoint = args[-1]
            if endpoint.endswith("/releases"):
                return json.dumps(
                    [
                        [
                            {
                                "tag_name": "previews",
                                "immutable": self.immutable,
                                "draft": self.draft,
                            }
                        ]
                        if self.exists
                        else []
                    ]
                )
            if endpoint.endswith("/pulls"):
                return json.dumps(
                    [{"number": 42, "merged_at": "date", "base": {"ref": "main"}}]
                )
            if endpoint.endswith("/comments"):
                return json.dumps([[], self.comments])
        if args[0] == "release":
            assert args[2] == "previews"
        if args[:2] == ("release", "view"):
            return json.dumps(
                {
                    "assets": [
                        *[
                            {"name": name, "state": "uploaded", "size": len(data)}
                            for name, data in self.files.items()
                        ],
                        *[
                            {"name": name, "state": "starter", "size": 0}
                            for name in self.starters
                        ],
                    ]
                }
            )
        elif args[:2] == ("release", "upload"):
            if self.immutable:
                raise subprocess.CalledProcessError(1, args)
            path = Path(args[3])
            assert path.name not in self.files
            self.files[path.name] = path.read_bytes()
            self.uploads.append(path.name)
        elif args[:2] == ("release", "download"):
            (Path(args[-1]) / args[4]).write_bytes(self.files[args[4]])
        elif args[:2] == ("release", "edit"):
            # Live GitHub seals a mutable published release on a metadata edit
            # when repository immutability has been enabled again.
            self.immutable = True
            self.notes = Path(args[-1]).read_text()
        elif args[:2] == ("release", "delete-asset"):
            name = args[3]
            self.files.pop(name, None)
            self.starters.discard(name)
            self.deleted.append(name)
        elif args[:2] == ("pr", "comment"):
            self.comments.append({"body": Path(args[-1]).read_text()})
        else:
            raise AssertionError(args)
        return ""


@pytest.fixture
def github(preview: ModuleType, monkeypatch: pytest.MonkeyPatch) -> GitHub:
    fake = GitHub()
    monkeypatch.setattr(preview, "gh", fake)
    return fake


def test_version_ignores_suffixed_tags_and_later_tagging(
    preview: ModuleType, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)

    def git(*args: str) -> str:
        return subprocess.check_output(["git", *args], text=True).strip()

    git("init", "-q")
    git("config", "user.email", "test@example.com")
    git("config", "user.name", "Test")
    git("commit", "--allow-empty", "-qm", "base")
    git("tag", "0.3.2")
    git("tag", "v0.3.3")
    git("commit", "--allow-empty", "-qm", "second")
    git("tag", "v9.9.9-rc1")
    git("tag", "v0.3.4.dev5")
    git("commit", "--allow-empty", "-qm", "source")
    commit = git("rev-parse", "HEAD")
    assert preview.preview_version(commit) == "0.3.4.dev2"
    git("tag", "v0.3.4")
    assert preview.preview_version(commit) == "0.3.4.dev2"


def test_stamp_changes_only_software_versions(
    preview: ModuleType, tmp_path: Path
) -> None:
    for relative in (
        "packages/chartcoach/pyproject.toml",
        "packages/catalog/package.json",
        "apps/chat/package.json",
        "pnpm-lock.yaml",
    ):
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((_ROOT / relative).read_bytes())
    before = (tmp_path / "pnpm-lock.yaml").read_bytes()
    preview.stamp(tmp_path, _VERSION)
    assert (
        f'version = "{_VERSION}"'
        in (tmp_path / "packages/chartcoach/pyproject.toml").read_text()
    )
    for relative in ("packages/catalog/package.json", "apps/chat/package.json"):
        assert json.loads((tmp_path / relative).read_text())["version"] == "0.3.4-dev.7"
    assert (tmp_path / "pnpm-lock.yaml").read_bytes() == before
    with pytest.raises(ValueError):
        preview.stamp(tmp_path, "0.3.4.dev7+local")


def test_checksum_covers_all_distributions_and_provenance(
    preview: ModuleType, distribution: Path
) -> None:
    marker = preview.checksum(distribution, _VERSION)
    paths = [
        path
        for folder in ("python", "npm")
        for path in (distribution / folder).iterdir()
    ]
    paths.append(distribution / preview.provenance_name(_VERSION))
    assert set(marker.read_text().splitlines()) == {
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}"
        for path in paths
    }
    with pytest.raises(ValueError):
        preview.checksum(distribution, "0.3.4.dev8")


def test_preview_chat_requires_installable_matching_sdk(
    preview: ModuleType, tmp_path: Path
) -> None:
    release = build(tmp_path / "bad", _VERSION, sdk="0.3.4-dev.7")
    with pytest.raises(ValueError, match="matching SDK asset URL"):
        preview.checksum(release, _VERSION)


def test_publication_is_immutable_and_idempotent(
    preview: ModuleType, distribution: Path, github: GitHub
) -> None:
    preview.publish(distribution, _COMMIT, _VERSION)
    assert github.uploads == [
        *preview.artifact_names(_VERSION),
        preview.marker_name(_VERSION),
    ]
    assert len(github.comments) == 1
    assert _COMMIT in github.comments[0]["body"]
    assert github.notes == ""
    assert github.immutable is False
    assert (
        "npx --yes https://github.com/chartcoach/chartcoach/releases/download/previews/chartcoach-0.3.4-dev.7.tgz"
        in github.comments[0]["body"]
    )
    preview.publish(distribution, _COMMIT, _VERSION)
    assert len(github.uploads) == 6
    assert len(github.comments) == 1
    github.files[preview.package_names(_VERSION)[0]] = b"conflicting bytes"
    with pytest.raises(ValueError, match="Published preview bytes differ"):
        preview.publish(distribution, _COMMIT, _VERSION)


@pytest.mark.parametrize("failure", ["upload", "comment", "delete-asset"])
def test_partial_publication_resumes_before_completion_marker(
    preview: ModuleType, distribution: Path, github: GitHub, failure: str
) -> None:
    for n in range(1, 33):
        for name in [
            *preview.artifact_names(f"0.3.3.dev{n}"),
            preview.marker_name(f"0.3.3.dev{n}"),
        ]:
            github.files[name] = b"old bytes"
    github.fail = failure
    with pytest.raises(subprocess.CalledProcessError):
        preview.publish(distribution, _COMMIT, _VERSION)
    assert preview.marker_name(_VERSION) not in github.files
    github.fail = None
    preview.publish(distribution, _COMMIT, _VERSION)
    assert preview.marker_name(_VERSION) in github.files
    assert len(github.comments) == 1
    assert len(github.files) == 30 * 6


def test_starter_upload_is_removed_before_retry(
    preview: ModuleType, distribution: Path, github: GitHub
) -> None:
    name = preview.package_names(_VERSION)[0]
    github.starters.add(name)
    preview.publish(distribution, _COMMIT, _VERSION)
    assert name in github.deleted
    assert name in github.files
    assert not github.starters


def test_old_completion_preserves_static_notes_and_prunes_unavailable_urls(
    preview: ModuleType, distribution: Path, github: GitHub
) -> None:
    github.notes = "newer build notes"
    for n in range(8, 38):
        for name in [
            *preview.artifact_names(f"0.3.4.dev{n}"),
            preview.marker_name(f"0.3.4.dev{n}"),
        ]:
            github.files[name] = b"newer bytes"
    orphan = preview.package_names("0.3.4.dev1")[2]
    github.files[orphan] = b"interrupted upload"
    preview.publish(distribution, _COMMIT, _VERSION)
    assert github.notes == "newer build notes"
    assert not github.comments
    assert not set(preview.package_names(_VERSION)) & github.files.keys()
    assert orphan not in github.files
    assert len(github.files) == 30 * 6


@pytest.mark.parametrize(
    "state",
    [
        None,
        {"status": "in_progress", "conclusion": ""},
        {"status": "completed", "conclusion": "failure"},
        {"status": "completed", "conclusion": "cancelled"},
        {"status": "completed", "conclusion": "skipped"},
    ],
)
def test_resolution_rejects_every_non_success_state(
    preview: ModuleType, monkeypatch: pytest.MonkeyPatch, state: object
) -> None:
    def fake(*args: str) -> str:
        assert args[:2] == ("run", "list")
        assert args[args.index("--commit") + 1] == _COMMIT
        assert args[args.index("--event") + 1] == "push"
        return json.dumps([] if state is None else [state])

    monkeypatch.setattr(preview, "gh", fake)
    with pytest.raises(ValueError, match="latest main push CI"):
        preview.resolve(_COMMIT)


@pytest.mark.parametrize("complete", [False, True])
def test_resolution_skips_only_completed_builds(
    preview: ModuleType,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    github: GitHub,
    complete: bool,
) -> None:
    github.exists = True
    github.files[preview.package_names(_VERSION)[0]] = b"partial"
    if complete:
        github.files[preview.marker_name(_VERSION)] = b"complete"
    real = preview.gh
    monkeypatch.setattr(
        preview,
        "gh",
        lambda *args: (
            json.dumps([{"status": "completed", "conclusion": "success"}])
            if args[:2] == ("run", "list")
            else real(*args)
        ),
    )
    monkeypatch.setattr(preview, "preview_version", lambda commit: _VERSION)
    output = tmp_path / "output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    preview.resolve(_COMMIT)
    assert f"publish={str(not complete).lower()}" in output.read_text()


def test_api_failure_never_creates_a_release(
    preview: ModuleType, distribution: Path, github: GitHub
) -> None:
    github.exists = False
    github.fail = "api"
    with pytest.raises(subprocess.CalledProcessError):
        preview.publish(distribution, _COMMIT, _VERSION)
    assert not github.exists
    assert not github.uploads


@pytest.mark.parametrize("operation", ["resolve", "publish"])
@pytest.mark.parametrize("state", ["missing", "immutable", "draft", "unknown"])
def test_unusable_channel_fails_before_build_or_publication(
    preview: ModuleType,
    distribution: Path,
    github: GitHub,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    operation: str,
    state: str,
) -> None:
    github.exists = state != "missing"
    github.immutable = state == "immutable"
    github.draft = state == "draft"
    real = preview.gh

    def fake(*args: str) -> str:
        if args[:2] == ("run", "list"):
            return json.dumps([{"status": "completed", "conclusion": "success"}])
        if state == "unknown" and args[-1].endswith("/releases"):
            return json.dumps([[{"tag_name": "previews", "draft": False}]])
        return real(*args)

    monkeypatch.setattr(preview, "gh", fake)
    monkeypatch.setattr(preview, "preview_version", lambda commit: _VERSION)
    output = tmp_path / "output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    with pytest.raises(ValueError, match="published, mutable release"):
        if operation == "resolve":
            preview.resolve(_COMMIT)
        else:
            preview.publish(distribution, _COMMIT, _VERSION)
    assert not output.exists()
    assert not github.uploads
    assert not github.deleted
    assert not github.notes
    assert not github.comments


def test_provenance_distinguishes_signing_and_source_commits(
    preview: ModuleType, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    env = {
        "GITHUB_SERVER_URL": "https://github.com",
        "GITHUB_REPOSITORY": "chartcoach/chartcoach",
        "GITHUB_REF": "refs/heads/main",
        "GITHUB_SHA": "b" * 40,
        "GITHUB_WORKFLOW_REF": "chartcoach/chartcoach/.github/workflows/publish.yml@refs/heads/main",
        "GITHUB_RUN_ID": "123",
        "GITHUB_RUN_ATTEMPT": "2",
    }
    for key, value in env.items():
        monkeypatch.setenv(key, value)
    output = tmp_path / "provenance.json"
    preview.provenance(_COMMIT, output)
    data = json.loads(output.read_text())
    definition = data["buildDefinition"]
    assert definition["buildType"] == _PREDICATE_TYPE
    assert definition["externalParameters"]["checkoutCommit"] == _COMMIT
    assert {
        item["digest"]["gitCommit"] for item in definition["resolvedDependencies"]
    } == {_COMMIT, "b" * 40}
    assert data["runDetails"]["metadata"]["invocationId"].endswith("/123/attempts/2")


def test_workflow_gates_source_and_attests_the_exact_artifact_set(
    tmp_path: Path,
) -> None:
    # BaseLoader preserves GitHub's `on` key rather than YAML 1.1's boolean.
    workflow = yaml.load(
        (_ROOT / ".github/workflows/publish.yml").read_text(), Loader=yaml.BaseLoader
    )
    assert workflow["on"]["workflow_run"]["workflows"] == ["CI"]
    guard = workflow["jobs"]["resolve-preview"]["if"]
    for condition in (
        "event == 'push'",
        "head_branch == 'main'",
        "conclusion == 'success'",
        "head_repository.full_name == github.repository",
    ):
        assert condition in guard
    assert workflow["jobs"]["prepare"]["if"] == "github.event_name != 'workflow_run'"
    jobs = workflow["jobs"]
    assert jobs["verify-preview"]["needs"] == "build-preview"
    assert jobs["publish-preview"]["needs"] == ["resolve-preview", "verify-preview"]
    attest = next(
        step
        for step in jobs["publish-preview"]["steps"]
        if step["name"] == "Attest verified preview artifacts"
    )
    assert attest["if"] == (
        "github.event.repository.private == false || vars.PREVIEW_ATTESTATIONS == 'true'"
    )
    assert "environment" not in jobs["publish-preview"]
    assert attest["with"]["predicate-type"] == _PREDICATE_TYPE
    assert attest["with"]["predicate-path"].endswith("-provenance.json")
    assert jobs["publish-preview"]["concurrency"] == {
        "group": "publish-preview-release",
        "cancel-in-progress": "false",
        "queue": "max",
    }
    steps = jobs["publish-preview"]["steps"]
    read_back = next(
        s for s in steps if s["name"] == "Verify stored preview attestation"
    )
    assert read_back["if"] == attest["if"]
    assert steps.index(attest) < steps.index(read_back) < len(steps) - 1
    files = [
        f"dist/release/python/chartcoach-{_VERSION}-py3-none-any.whl",
        f"dist/release/python/chartcoach-{_VERSION}.tar.gz",
        "dist/release/npm/chartcoach-catalog-0.3.4-dev.7.tgz",
        "dist/release/npm/chartcoach-0.3.4-dev.7.tgz",
        f"dist/release/chartcoach-{_VERSION}-SHA256SUMS",
        f"dist/release/chartcoach-{_VERSION}-provenance.json",
    ]
    for filename in files:
        path = tmp_path / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()
    for job, name, key in [
        ("build-preview", "Retain verified preview inputs", "path"),
        ("publish-preview", "Attest verified preview artifacts", "subject-path"),
    ]:
        step = next(step for step in jobs[job]["steps"] if step["name"] == name)
        matched = {
            path.relative_to(tmp_path).as_posix()
            for pattern in step["with"][key].splitlines()
            for path in tmp_path.glob(pattern)
        }
        assert matched == set(files)


def test_interrupted_newer_upload_does_not_suppress_announcements_or_evict_completed_builds(
    preview: ModuleType, distribution: Path, github: GitHub
) -> None:
    for n in range(1, 31):
        for name in [
            *preview.artifact_names(f"0.3.3.dev{n}"),
            preview.marker_name(f"0.3.3.dev{n}"),
        ]:
            github.files[name] = b"completed"
    for name in preview.artifact_names("0.3.4.dev8"):
        github.files[name] = b"interrupted before completion"
    github.notes = "old release notes"
    preview.publish(distribution, _COMMIT, _VERSION)
    assert _VERSION in github.comments[0]["body"]
    assert github.notes == "old release notes"
    assert github.immutable is False
    assert preview.marker_name(_VERSION) in github.files
    assert len([name for name in github.files if name.endswith("-SHA256SUMS")]) == 30
    assert preview.marker_name("0.3.3.dev2") in github.files
    assert preview.marker_name("0.3.3.dev1") not in github.files


def test_consecutive_builds_keep_release_metadata_static_and_assets_writable(
    preview: ModuleType, distribution: Path, github: GitHub, tmp_path: Path
) -> None:
    github.notes = "Static rolling preview instructions"
    preview.publish(distribution, _COMMIT, _VERSION)
    preview.publish(build(tmp_path / "next", "0.3.4.dev8"), "b" * 40, "0.3.4.dev8")
    assert github.notes == "Static rolling preview instructions"
    assert github.immutable is False
    assert len(github.uploads) == 12
    assert len(github.comments) == 2
    assert preview.marker_name(_VERSION) in github.files
    assert preview.marker_name("0.3.4.dev8") in github.files


def test_private_publication_uses_authenticated_downloads_and_unsigned_provenance(
    preview: ModuleType,
    distribution: Path,
    github: GitHub,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("PRIVATE_REPOSITORY", "true")
    monkeypatch.setenv("PREVIEW_ATTESTED", "false")
    preview.publish(distribution, _COMMIT, _VERSION)
    assert (
        "gh release download previews -R chartcoach/chartcoach"
        in github.comments[0]["body"]
    )
    assert (
        "npm pkg set 'overrides.@chartcoach/catalog=$@chartcoach/catalog'"
        in github.comments[0]["body"]
    )
    assert "npx --no-install chartcoach" in github.comments[0]["body"]
    assert "This provenance record is unsigned" in github.comments[0]["body"]
    assert "gh attestation verify" not in github.comments[0]["body"]
    assert preview.provenance_name(_VERSION) in github.files
    assert "gh release download" in github.comments[0]["body"]
    preview.publish(distribution, _COMMIT, _VERSION)
    assert len(github.comments) == 1


def test_provenance_bytes_are_reused_across_publication_attempts(
    preview: ModuleType,
    distribution: Path,
    github: GitHub,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("PREVIEW_ATTESTED", "true")
    github.fail = "comment"
    with pytest.raises(subprocess.CalledProcessError):
        preview.publish(distribution, _COMMIT, _VERSION)
    original = github.files[preview.provenance_name(_VERSION)]
    monkeypatch.setenv("GITHUB_RUN_ATTEMPT", "2")
    github.fail = None
    preview.publish(distribution, _COMMIT, _VERSION)
    assert github.files[preview.provenance_name(_VERSION)] == original
    assert "gh attestation verify" in github.comments[0]["body"]
    assert "gh attestation download" in github.comments[0]["body"]
    assert "--bundle BUNDLE_FILE" in github.comments[0]["body"]
    assert f'--predicate-type "{_PREDICATE_TYPE}"' in github.comments[0]["body"]
    assert (
        '--signer-workflow "chartcoach/chartcoach/.github/workflows/publish.yml"'
        in github.comments[0]["body"]
    )


@pytest.mark.parametrize(
    ("failures", "download_state", "source", "valid_signature", "attempts", "success"),
    [
        (0, "error", _COMMIT, True, 1, True),
        (2, "error", _COMMIT, True, 3, True),
        (5, "error", _COMMIT, True, 5, False),
        (2, "missing", _COMMIT, True, 3, True),
        (5, "missing", _COMMIT, True, 5, False),
        (2, "empty", _COMMIT, True, 3, True),
        (5, "empty", _COMMIT, True, 5, False),
        (0, "error", "b" * 40, True, 1, False),
        (0, "error", _COMMIT, False, 1, False),
    ],
)
def test_stored_attestation_checks_source_and_bounds_visibility_retries(
    tmp_path: Path,
    failures: int,
    download_state: str,
    source: str,
    valid_signature: bool,
    attempts: int,
    success: bool,
) -> None:
    workflow = yaml.load(
        (_ROOT / ".github/workflows/publish.yml").read_text(), Loader=yaml.BaseLoader
    )
    step = next(
        s
        for s in workflow["jobs"]["publish-preview"]["steps"]
        if s["name"] == "Verify stored preview attestation"
    )
    wheel_dir = tmp_path / "dist/release/python"
    wheel_dir.mkdir(parents=True)
    wheel = f"chartcoach-{_VERSION}-py3-none-any.whl"
    (wheel_dir / wheel).write_bytes(b"wheel")
    bundle = f"sha256:{hashlib.sha256(b'wheel').hexdigest()}.jsonl"
    (wheel_dir / bundle).write_bytes(b"stale bundle must be replaced")
    verified = json.dumps(
        [
            {
                "verificationResult": {
                    "statement": {
                        "predicate": {
                            "buildDefinition": {
                                "externalParameters": {"checkoutCommit": source}
                            }
                        }
                    }
                }
            }
        ]
    )
    # Stub only GitHub's network/cryptographic boundary; execute the actual shell
    # step, digest naming, retry control flow, and source check.
    stub = f'''
downloads=0
sleep() {{ :; }}
gh() {{
    printf '%s\\n' "$*" >> "$RUNNER_TEMP/calls"
    if [ "$2" = download ]; then
        downloads=$((downloads + 1))
        if [ "$downloads" -le {failures} ]; then
            if [ "{download_state}" = empty ]; then
                : > '{bundle}'
            fi
            [ "{download_state}" != error ]
        else
            printf 'fresh bundle\\n' > '{bundle}'
        fi
    else
        [ "{str(valid_signature).lower()}" = true ] || return 1
        printf '%s\\n' '{verified}'
    fi
}}
'''
    result = subprocess.run(
        ["bash", "-eu", "-o", "pipefail", "-c", stub + step["run"]],
        cwd=tmp_path,
        env={
            "PATH": os.environ["PATH"],
            "RUNNER_TEMP": str(tmp_path),
            "GITHUB_REPOSITORY": "chartcoach/chartcoach",
            "COMMIT": _COMMIT,
            "VERSION": _VERSION,
        },
        capture_output=True,
        text=True,
        check=False,
    )
    assert (result.returncode == 0) is success, result.stderr
    calls = (tmp_path / "calls").read_text().splitlines()
    downloads = [c for c in calls if c.startswith("attestation download")]
    verifications = [c for c in calls if c.startswith("attestation verify")]
    assert len(downloads) == attempts
    assert all("--predicate-type" not in c for c in downloads)
    assert len(verifications) == (0 if failures == 5 else 1)
    if verifications:
        assert (
            f"--bundle sha256:{hashlib.sha256(b'wheel').hexdigest()}.jsonl"
            in verifications[0]
        )
        assert f"--predicate-type {_PREDICATE_TYPE}" in verifications[0]
        assert (
            "--signer-workflow chartcoach/chartcoach/.github/workflows/publish.yml"
            in verifications[0]
        )
