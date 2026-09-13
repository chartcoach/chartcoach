from __future__ import annotations

import json
from pathlib import Path

import pytest
from chartcoach import CatalogError
from chartcoach._catalog.profiles import (
    ProfileMetadata,
    validate_embedding_model,
)

_FIXTURE = Path(__file__).parents[3] / "fixtures" / "catalog-contract" / "profile.json"


def test_python_parses_the_shared_profile_contract() -> None:
    metadata = ProfileMetadata.from_bytes(_FIXTURE.read_bytes())

    assert metadata.dimensions == 4
    assert metadata.embedding_functions[0].source_column == "text"
    assert metadata.lancedb_version == "0.38.0"
    assert ProfileMetadata.from_bytes(metadata.to_bytes()) == metadata


@pytest.mark.parametrize(
    ("patch", "message"),
    [
        ({"dimensions": True}, "positive safe integer"),
        (
            {"distance_metric": "manhattan"},
            "Unsupported profile distance metric",
        ),
        ({"extra": True}, "unsupported fields"),
    ],
)
def test_profile_contract_rejects_invalid_fields(
    patch: dict[str, object], message: str
) -> None:
    value = json.loads(_FIXTURE.read_text()) | patch

    with pytest.raises(CatalogError, match=message):
        ProfileMetadata.from_mapping(value)


def test_profile_contract_rejects_unsafe_embedding_model_values() -> None:
    value = json.loads(_FIXTURE.read_text())
    binding = value["embedding_functions"][0]

    with pytest.raises(CatalogError, match="registry variable"):
        ProfileMetadata.from_mapping(
            value
            | {"embedding_functions": [binding | {"model": {"api_key": "secret"}}]}
        )

    with pytest.raises(CatalogError, match="invalid registry variable"):
        ProfileMetadata.from_mapping(
            value
            | {
                "embedding_functions": [
                    binding | {"model": {"options": {"key": "$var:key"}}}
                ]
            }
        )

    with pytest.raises(CatalogError, match="finite JSON numbers"):
        ProfileMetadata.from_mapping(
            value
            | {
                "embedding_functions": [
                    binding | {"model": {"temperature": float("inf")}}
                ]
            }
        )


@pytest.mark.parametrize(
    "model",
    [
        {"endpoint_url": "https://user:password@example.test/v1"},
        {"endpoint_url": "https://example.test/v1?token="},
        {"options": {"endpoint_url": "https://example.test/v1?access_key=secret"}},
        {"options": [{"headers": {"access_key": "secret"}}]},
        {"default_headers": {"X-Custom": "value"}},
    ],
)
def test_profile_contract_rejects_persisted_authentication_data(
    model: dict[str, object],
) -> None:
    value = json.loads(_FIXTURE.read_text())
    binding = value["embedding_functions"][0]

    with pytest.raises(CatalogError, match="credentials|authentication|empty"):
        ProfileMetadata.from_mapping(
            value | {"embedding_functions": [binding | {"model": model}]}
        )


def test_profile_contract_bounds_encoded_metadata() -> None:
    with pytest.raises(CatalogError, match="64 KiB"):
        ProfileMetadata.from_bytes(b" " * 65_537)


def test_provider_validation_keeps_model_identity_concrete() -> None:
    with pytest.raises(CatalogError, match="name.*cannot use a registry variable"):
        validate_embedding_model(
            {"name": "$var:model-name", "device": "$var:device"},
            allowed_fields=frozenset({"name", "device"}),
        )

    validate_embedding_model(
        {"tokenizer_name": "concrete-tokenizer"},
        allowed_fields=frozenset({"tokenizer_name"}),
    )
