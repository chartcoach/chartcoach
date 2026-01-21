from __future__ import annotations

import hashlib
import re


def fence(text: str, lang: str = "json") -> str:
    return f"```{lang}\n{text}\n```"


def unfence(text: str) -> list[str]:
    pattern = r"```(?:\w+)?\n(.*?)\n```"
    return [match.strip() for match in re.findall(pattern, text, re.DOTALL)]


def string_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
