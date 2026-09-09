from __future__ import annotations

import base64
import hashlib
import io
import json
import runpy
import subprocess
import sys
import tarfile
import time
import urllib.error
import urllib.request
from email.message import Message
from pathlib import Path

import pytest

_ROOT = Path(__file__).parents[3]
_REGISTRY = _ROOT / "scripts" / "release_registry.py"
_NPM = "https://registry.npmjs.org/@chartcoach%2Fcatalog/0.2.0"
_PYPI = "https://pypi.org/pypi/chartcoach/0.2.0/json"


@pytest.fixture
def release_files(tmp_path: Path) -> Path:
    (tmp_path / "npm").mkdir()
    (tmp_path / "python").mkdir()
    data = json.dumps({"name": "@chartcoach/catalog", "version": "0.2.0"}).encode()
    with tarfile.open(tmp_path / "npm" / "catalog.tgz", "w:gz") as archive:
        entry = tarfile.TarInfo("package/package.json")
        entry.size = len(data)
        archive.addfile(entry, io.BytesIO(data))
    (tmp_path / "python" / "chartcoach-0.2.0-py3-none-any.whl").write_bytes(b"wheel")
    (tmp_path / "python" / "chartcoach-0.2.0.tar.gz").write_bytes(b"sdist")
    return tmp_path


@pytest.fixture
def registry(monkeypatch: pytest.MonkeyPatch) -> dict[str, bytes | int]:
    responses: dict[str, bytes | int] = {}

    def open_url(url: str, *, timeout: int) -> io.BytesIO:
        assert timeout > 0
        response = responses.get(url, 404)
        if isinstance(response, int):
            raise urllib.error.HTTPError(
                url, response, "registry error", Message(), None
            )
        return io.BytesIO(response)

    monkeypatch.setattr(urllib.request, "urlopen", open_url)
    monkeypatch.setattr(time, "sleep", lambda _: None)
    return responses


def _run(monkeypatch: pytest.MonkeyPatch, *arguments: str | Path) -> None:
    monkeypatch.setattr(sys, "argv", [str(_REGISTRY), *(str(arg) for arg in arguments)])
    runpy.run_path(str(_REGISTRY), run_name="__main__")


def _publish(registry: dict[str, bytes | int], release: Path) -> None:
    tarball = (release / "npm" / "catalog.tgz").read_bytes()
    registry["https://registry.npmjs.org/catalog.tgz"] = tarball
    registry[_NPM] = json.dumps(
        {
            "name": "@chartcoach/catalog",
            "version": "0.2.0",
            "dist": {
                "integrity": "sha512-"
                + base64.b64encode(hashlib.sha512(tarball).digest()).decode(),
                "tarball": "https://registry.npmjs.org/catalog.tgz",
            },
        }
    ).encode()
    python_files = []
    for path in (release / "python").iterdir():
        data = path.read_bytes()
        url = f"https://files.pythonhosted.org/{path.name}"
        registry[url] = data
        python_files.append(
            {
                "filename": path.name,
                "digests": {"sha256": hashlib.sha256(data).hexdigest()},
                "url": url,
            }
        )
    registry[_PYPI] = json.dumps({"urls": python_files}).encode()


def test_npm_retry_publishes_missing_version_and_skips_matching_bytes(
    release_files: Path,
    registry: dict[str, bytes | int],
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    tarball = release_files / "npm" / "catalog.tgz"
    _run(monkeypatch, "npm-state", tarball)
    assert capsys.readouterr().out == "publish\n"
    _publish(registry, release_files)
    _run(monkeypatch, "npm-state", tarball)
    assert capsys.readouterr().out == "published\n"


def test_registry_auth_failure_cannot_be_treated_as_an_available_version(
    release_files: Path,
    registry: dict[str, bytes | int],
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    registry[_NPM] = 403
    with pytest.raises(SystemExit, match="1"):
        _run(monkeypatch, "npm-state", release_files / "npm" / "catalog.tgz")
    assert "403" in capsys.readouterr().err


@pytest.mark.parametrize("registry_name", ["npm", "python"])
def test_release_preflight_rejects_conflicting_published_bytes(
    release_files: Path,
    registry: dict[str, bytes | int],
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    registry_name: str,
) -> None:
    _publish(registry, release_files)
    key = _NPM if registry_name == "npm" else _PYPI
    payload = registry[key]
    assert isinstance(payload, bytes)
    metadata = json.loads(payload)
    if registry_name == "npm":
        metadata["dist"]["integrity"] = "sha512-different"
    else:
        metadata["urls"][0]["digests"]["sha256"] = "different"
    registry[key] = json.dumps(metadata).encode()
    with pytest.raises(SystemExit, match="1"):
        _run(monkeypatch, "check", release_files, "--allow-missing")
    assert "differs from the verified" in capsys.readouterr().err


def test_partial_publication_is_recoverable_but_cannot_pass_final_verification(
    release_files: Path,
    registry: dict[str, bytes | int],
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    _publish(registry, release_files)
    del registry[_PYPI]
    _run(monkeypatch, "check", release_files, "--allow-missing")
    with pytest.raises(SystemExit, match="1"):
        _run(monkeypatch, "check", release_files)
    assert "PyPI has not published" in capsys.readouterr().err


def test_final_verification_checks_downloaded_bytes(
    release_files: Path,
    registry: dict[str, bytes | int],
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    _publish(registry, release_files)
    _run(monkeypatch, "check", release_files)
    registry["https://registry.npmjs.org/catalog.tgz"] = b"corrupted"
    with pytest.raises(SystemExit, match="1"):
        _run(monkeypatch, "check", release_files)
    assert "Published artifact bytes differ" in capsys.readouterr().err


def test_release_rejects_distribution_files_outside_the_verified_set(
    release_files: Path,
    registry: dict[str, bytes | int],
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    (release_files / "python" / "other-package.whl").write_bytes(b"unexpected")
    with pytest.raises(SystemExit, match="1"):
        _run(monkeypatch, "check", release_files, "--allow-missing")
    assert (
        "exactly one npm tarball, wheel, and source distribution"
        in capsys.readouterr().err
    )


def test_final_verification_retries_transient_registry_errors(
    release_files: Path,
    registry: dict[str, bytes | int],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _publish(registry, release_files)
    open_url = urllib.request.urlopen
    requests = 0

    def transient(url: str, *, timeout: int) -> object:
        nonlocal requests
        if url == _NPM:
            requests += 1
            if requests == 1:
                raise urllib.error.HTTPError(url, 503, "unavailable", Message(), None)
        return open_url(url, timeout=timeout)

    monkeypatch.setattr(urllib.request, "urlopen", transient)
    _run(monkeypatch, "check", release_files)
    assert requests == 2


def test_distribution_verifier_rejects_additional_wheels(release_files: Path) -> None:
    directory = release_files / "python"
    (directory / "other-package.whl").write_bytes(b"unchecked")
    result = subprocess.run(
        [
            sys.executable,
            _ROOT / "packages/chartcoach/tests/verify_built_package.py",
            "--dist-dir",
            directory,
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 2
    assert (
        "exactly one ChartCoach wheel and matching source distribution" in result.stderr
    )


def test_release_tag_rejects_shell_input_before_invoking_tools(tmp_path: Path) -> None:
    sentinel = tmp_path / "executed"
    result = subprocess.run(
        [_ROOT / "scripts" / "release.sh", "check-version", f"$(touch {sentinel})"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert not sentinel.exists()
