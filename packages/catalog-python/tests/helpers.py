from __future__ import annotations

import csv
import io
import json
from typing import Any

from click.testing import Result


def jsonl_rows(result: Result) -> list[dict[str, Any]]:
    assert result.exit_code == 0, result.output
    return [json.loads(line) for line in result.output.splitlines() if line.strip()]


def json_value(result: Result) -> Any:
    assert result.exit_code == 0, result.output
    return json.loads(result.output)


def csv_rows(result: Result) -> list[dict[str, str]]:
    assert result.exit_code == 0, result.output
    return list(csv.DictReader(io.StringIO(result.output)))
