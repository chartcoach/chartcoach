"""Open one catalog, select guideline entries, then read and cite evidence.

    import chartcoach.agent as cc

    catalog = cc.open_catalog()
    candidates = catalog.query(contains="labels", limit=5)
    selected_ids = candidates.get_column("id").head(3).to_list()
    records = catalog.read(ids=selected_ids, source_detail="minimal")
    citations = catalog.cite(ids=selected_ids)
    description = catalog.describe()

Compose database queries through the native connection and index table:

    with catalog.duckdb() as connection:
        rows = connection.sql("select id, title from guidelines limit 5").fetchall()

    # Select a profile from description["profiles"] for a release with an index.
    table = catalog.index(profile)
    hits = table.search(
        "direct labels", query_type="fts", fts_columns="text"
    ).select(["id", "parent_id", "role", "_score"]).limit(5).to_list()
    records = catalog.read(ids=list(dict.fromkeys(hit["parent_id"] for hit in hits)))

`contains` matches a contiguous phrase in the ID, title, or description.
For an empty result, shorten the phrase or search section text with SQL.
Explicit full-text search uses an available index without embedding the query.
Native hits include scores and may share a parent guideline. Read the selected
entries' context and exceptions before applying their advice.

Use catalog.artifact(path) for a verified local release file and catalog.cache()
for a complete release directory that open_catalog can reopen offline.

Inspect the packaged agent resources through the installed plugin:

    plugin = cc.agent_plugin()
    core = plugin.skill("core")
    print(core.source)
"""

from ._catalog import Catalog, CatalogError, open_catalog
from ._skills import agent_plugin

__all__ = ["Catalog", "CatalogError", "agent_plugin", "open_catalog"]
