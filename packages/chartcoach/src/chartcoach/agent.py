"""Open one catalog, select guideline entries, then read and cite evidence.

    import chartcoach.agent as cc

    catalog = cc.open_catalog()
    candidates = catalog.query(contains="direct labels", limit=5)
    selected_ids = candidates.get_column("id").head(3).to_list()
    records = catalog.read(ids=selected_ids, source_detail="minimal")
    citations = catalog.cite(ids=selected_ids)
    description = catalog.describe()

Inspect the packaged agent resources through the installed plugin:

    plugin = cc.agent_plugin()
    core = plugin.skill("core")
    print(core.source)
"""

from .catalog import Catalog, CatalogError, open_catalog
from .skills import agent_plugin

__all__ = ["Catalog", "CatalogError", "agent_plugin", "open_catalog"]
