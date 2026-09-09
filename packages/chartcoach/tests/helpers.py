from __future__ import annotations

import json
from typing import cast

from click.testing import Result

JsonObject = dict[str, object]


def assert_cli_error(
    result: Result,
    expected: str,
    *,
    exit_code: int = 1,
) -> None:
    assert result.exit_code == exit_code, result.output
    assert isinstance(result.exception, SystemExit)
    assert expected in result.stderr


def json_value(result: Result) -> JsonObject:
    assert result.exit_code == 0, result.output
    return cast(JsonObject, json.loads(result.stdout))
