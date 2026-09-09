from __future__ import annotations

import json
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import duckdb
import pytest
from chartcoach import Catalog, CatalogError, CatalogManifest, Guideline, open_catalog
from chartcoach._catalog import documents, model, references
from chartcoach.duckdb import register_catalog


def test_registration_preserves_caller_transaction(sample_catalog: Catalog) -> None:
    with duckdb.connect(":memory:") as connection:
        connection.execute("create table guidelines as select 'retained' as id")
        connection.execute("begin transaction")
        register_catalog(connection, sample_catalog)
        connection.execute("rollback")
        assert connection.sql("select * from guidelines").fetchall() == [("retained",)]
        assert connection.sql(
            "select table_name from information_schema.tables"
        ).fetchall() == [("guidelines",)]


def test_native_registration_error_preserves_connection(
    sample_catalog: Catalog,
) -> None:
    with duckdb.connect(":memory:") as connection:
        connection.execute("create view guidelines as select 'retained' as id")
        with pytest.raises(duckdb.CatalogException):
            register_catalog(connection, sample_catalog)
        assert connection.sql("select * from guidelines").fetchall() == [("retained",)]


def test_concurrent_catalog_operations_reuse_completed_derivations(
    sample_catalog: Catalog, monkeypatch: pytest.MonkeyPatch
) -> None:
    calls: Counter[str] = Counter()

    def instrument(module, name):
        original = getattr(module, name)

        def counted(*args, **kwargs):
            calls[name] += 1
            return original(*args, **kwargs)

        monkeypatch.setattr(module, name, counted)

    instrument(documents, "build_document_rows")
    instrument(references, "build_reference_tables")
    instrument(references, "build_guideline_sources_df")
    instrument(model, "_dataframe_digest")

    def inspect(_):
        rows = sample_catalog.documents()
        info = sample_catalog.describe()
        record = sample_catalog.read(ids=["direct-labels"])[0]
        citation = sample_catalog.cite(ids=["direct-labels"])[0]
        return rows.height, info["entries_digest"], record["title"], citation["id"]

    with ThreadPoolExecutor(max_workers=4) as workers:
        results = list(workers.map(inspect, range(12)))

    assert all(result == results[0] for result in results)
    assert results[0][0] == 6
    assert results[0][2:] == ("Use direct labels", "direct-labels")
    assert calls == {
        "build_document_rows": 1,
        "build_reference_tables": 1,
        "build_guideline_sources_df": 1,
        "_dataframe_digest": 1,
    }


def test_cached_catalog_frames_are_isolated_from_callers() -> None:
    catalog = open_catalog(Path(__file__).parents[3] / "fixtures/catalog-release")
    before = catalog.read(ids=["direct-labels"], source_detail="full")
    digest = catalog.entries_digest()
    names = [table["name"] for table in catalog.describe()["tables"]]
    for name in names:
        frame = catalog.table(name)
        columns = frame.columns
        frame.drop_in_place(columns[0])
        assert catalog.table(name).columns == columns

    first = catalog.documents()
    second = catalog.documents()
    first[0, "text"] = "Changed document"
    assert second.item(0, "text") != "Changed document"
    assert catalog.documents().equals(second)
    assert catalog.read(ids=["direct-labels"], source_detail="full") == before
    assert catalog.entries_digest() == digest


def test_failed_document_derivation_can_be_retried(
    sample_catalog: Catalog, monkeypatch: pytest.MonkeyPatch
) -> None:
    original = documents.build_document_rows

    def fail(*args, **kwargs):
        raise ValueError("document construction interrupted")

    monkeypatch.setattr(documents, "build_document_rows", fail)
    with pytest.raises(ValueError, match="construction interrupted"):
        sample_catalog.documents()
    monkeypatch.setattr(documents, "build_document_rows", original)

    assert sample_catalog.documents().height == 6


def test_duckdb_connections_own_independent_materialized_tables(
    sample_catalog: Catalog,
) -> None:
    first = sample_catalog.duckdb()
    second = sample_catalog.duckdb()
    try:
        first.execute("update guidelines set title = 'Changed title'")
        first.execute("drop table sections")
        first.close()
        assert second.sql(
            "select title from guidelines where id = 'direct-labels'"
        ).fetchone() == ("Use direct labels",)
        assert second.sql("select count(*) from sections").fetchone() == (2,)
        assert sample_catalog.read(ids=["direct-labels"])[0]["title"] == (
            "Use direct labels"
        )
    finally:
        first.close()
        second.close()


def test_register_catalog_replaces_tables_and_preserves_caller_objects(
    sample_catalog: Catalog,
) -> None:
    with duckdb.connect(":memory:") as connection:
        connection.execute("create table caller_data as select 42 as value")
        connection.execute("create view caller_view as select 7 as value")
        register_catalog(connection, sample_catalog)
        connection.execute("delete from guidelines")
        register_catalog(connection, sample_catalog)

        assert connection.sql("select count(*) from guidelines").fetchone() == (2,)
        assert connection.sql("select * from caller_data").fetchone() == (42,)
        assert connection.sql("select * from caller_view").fetchone() == (7,)
        assert connection.sql(
            "select view_name from duckdb_views() where not internal"
        ).fetchall() == [("caller_view",)]


def test_register_catalog_failure_releases_its_temporary_view(
    sample_catalog: Catalog,
) -> None:
    with duckdb.connect(":memory:") as connection:
        connection.execute("create view guidelines as select 7 as value")
        with pytest.raises(duckdb.CatalogException):
            register_catalog(connection, sample_catalog)

        assert connection.sql(
            "select view_name from duckdb_views() where not internal"
        ).fetchall() == [("guidelines",)]
        assert connection.sql("select * from guidelines").fetchone() == (7,)


@pytest.mark.parametrize(
    ("ids", "expected_ids", "expected_references"),
    [
        (["𐀀", "𐀀"], ["𐀀"], ["shared", "web"]),
        (["sourceless"], ["sourceless"], []),
        ([], [], []),
    ],
    ids=["linked-references", "sourceless", "empty"],
)
def test_register_catalog_selects_entries_and_their_reference_closure(
    ids: list[str], expected_ids: list[str], expected_references: list[str]
) -> None:
    fixture = json.loads(
        (Path(__file__).parents[3] / "fixtures/catalog-contract/tables.json").read_text(
            encoding="utf-8"
        )
    )
    catalog = Catalog.from_guidelines(
        [Guideline.from_mapping(row) for row in fixture["guidelines"]],
        manifest=CatalogManifest.from_text(fixture["manifest"]),
    )
    with catalog.duckdb() as connection:
        schemas = {
            table["name"]: connection.table(table["name"]).types
            for table in catalog.describe()["tables"]
        }
        assert register_catalog(connection, catalog, ids=ids) is connection
        assert connection.sql("select id from guidelines order by id").fetchall() == [
            (value,) for value in expected_ids
        ]
        assert connection.sql('select id from "references" order by id').fetchall() == [
            (value,) for value in expected_references
        ]
        for name, schema in schemas.items():
            assert connection.table(name).types == schema
            if name in {"guidelines", "references"}:
                continue
            assert all(
                row[0] in expected_ids
                for row in connection.sql(
                    f'select guideline_id from "{name}"'
                ).fetchall()
            )
        assert connection.sql(
            "select reference_id from guideline_sources order by reference_id"
        ).fetchall() == [(value,) for value in expected_references]
        assert connection.sql(
            "select reference_id from guideline_references order by reference_id"
        ).fetchall() == [(value,) for value in expected_references]
        if not ids:
            assert all(connection.table(name).fetchall() == [] for name in schemas)


def test_register_catalog_validates_selection_before_replacing_caller_tables(
    sample_catalog: Catalog,
) -> None:
    with duckdb.connect(":memory:") as connection:
        connection.execute("create table guidelines as select 42 as value")
        with pytest.raises(CatalogError, match="Unknown guideline entry ID"):
            register_catalog(connection, sample_catalog, ids=["missing"])
        with pytest.raises(CatalogError, match="ids must be a sequence"):
            register_catalog(connection, sample_catalog, ids="direct-labels")
        assert connection.sql("select * from guidelines").fetchall() == [(42,)]


def test_register_catalog_validates_references_before_replacing_caller_tables(
    sample_catalog: Catalog,
) -> None:
    rows = sample_catalog.to_frame().to_dicts()
    rows[0]["references"] = ["@article{broken, title={Unclosed}"]
    catalog = Catalog.from_guidelines(
        [Guideline.from_mapping(row) for row in rows],
        manifest=sample_catalog.manifest,
    )
    with duckdb.connect(":memory:") as connection:
        connection.execute("create table guidelines as select 42 as value")
        with pytest.raises(CatalogError, match="Invalid BibTeX"):
            register_catalog(connection, catalog)
        assert connection.sql("select * from guidelines").fetchall() == [(42,)]


@pytest.mark.parametrize("empty", [False, True], ids=["populated", "empty"])
def test_duckdb_preserves_catalog_table_values_and_empty_types(
    empty: bool,
    sample_manifest: CatalogManifest,
    capfd: pytest.CaptureFixture[str],
) -> None:
    catalog = (
        Catalog.from_guidelines([], manifest=sample_manifest)
        if empty
        else open_catalog(Path(__file__).parents[3] / "fixtures/catalog-release")
    )
    with catalog.duckdb(config={"enable_external_access": False}) as connection:
        for table in catalog.describe()["tables"]:
            name = table["name"]
            frame = catalog.table(name)
            relation = connection.table(name)
            assert relation.columns == frame.columns
            assert relation.fetchall() == frame.rows()
        assert connection.sql("describe guidelines").fetchall() == [
            ("id", "VARCHAR", "YES", None, None, None),
            ("title", "VARCHAR", "YES", None, None, None),
            ("description", "VARCHAR", "YES", None, None, None),
            ("labels", "VARCHAR[]", "YES", None, None, None),
            ("body", "VARCHAR", "YES", None, None, None),
            (
                "sections",
                'STRUCT("role" VARCHAR, title VARCHAR, "content" VARCHAR)[]',
                "YES",
                None,
                None,
                None,
            ),
        ]
    assert capfd.readouterr().err == ""
