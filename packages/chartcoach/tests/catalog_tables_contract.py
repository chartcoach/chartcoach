from __future__ import annotations

import json
from pathlib import Path

from chartcoach import Catalog, CatalogManifest, Guideline, open_catalog
from chartcoach.duckdb import register_catalog


def main() -> None:
    root = Path(__file__).parents[3]
    fixture = json.loads(
        (root / "fixtures/catalog-contract/tables.json").read_text(encoding="utf-8")
    )
    manifest = CatalogManifest.from_text(fixture["manifest"])
    guidelines = [Guideline.from_mapping(row) for row in fixture["guidelines"]]
    cases = {
        "release": open_catalog(root / "fixtures/catalog-release"),
        "empty": Catalog.from_guidelines([], manifest=manifest),
        "relational": Catalog.from_guidelines(guidelines, manifest=manifest),
        "reversed": Catalog.from_guidelines(reversed(guidelines), manifest=manifest),
    }
    output = {}
    for name, catalog in cases.items():
        description = catalog.describe()["tables"]
        entry_ids = catalog.table("guidelines").get_column("id").to_list()
        selected_ids = entry_ids[:1] * 2
        registrations = []
        with catalog.duckdb() as connection:
            for ids in [None, [], selected_ids]:
                register_catalog(connection, catalog, ids=ids)
                registrations.append(
                    {
                        "ids": ids,
                        "tables": {
                            table["name"]: {
                                "rows": connection.execute(
                                    f'SELECT * FROM "{table["name"]}" ORDER BY ALL'
                                ).fetchall(),
                                "schema": connection.execute(
                                    f'DESCRIBE "{table["name"]}"'
                                ).fetchall(),
                            }
                            for table in description
                        },
                    }
                )
        output[name] = {
            "description": description,
            "tables": {
                table["name"]: catalog.table(table["name"]).to_dicts()
                for table in description
            },
            "registrations": registrations,
        }
    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
