from __future__ import annotations

from dataclasses import dataclass
from io import StringIO

import dspy
import polars as pl

from chartcoach.catalog import Catalog

from .adapters import guideline_browser_inputs_from_request
from ..strategy import RetrievalStrategy
from ..types import RetrievalRequest, RetrievalResponse


class GuidelineBrowserSignature(dspy.Signature):
    """
    An expert visualization critic that validates design choices against a rigorous knowledge catalog.

    INSTRUCTIONS:
    1. Do not rely on internal training data for design rules.
    2. You are an investigatory agent. Map vague requirements (e.g., "make it pop", "old audience") to specific catalog labels (e.g., "color:salience", "accessibility").
    3. You must "show your work" by citing specific Guideline IDs found in the catalog.
    4. Explore the catalog thoroughly: If the user mentions multiple constraints, perform multiple searches to find guidelines for each aspect.
    5. Read the full details of multiple retrieved guidelines to assess relevance and prioritize the best ones; avoid irrelevant or redundant rules.
    6. Always reference the retrieved guideline IDs in the feedback. Ensure every suggestion cites at least one relevant guideline ID. Do not cite labels.
    """

    chart: dspy.Image = dspy.InputField(desc="Image of the chart to evaluate.")
    situation: str = dspy.InputField(
        desc="Description of the analytical and rhetorical goals of the chart creator, including the target audience and context."
    )
    chart_spec: str = dspy.InputField(
        desc="JSON string representing the chart specification and/or schema context."
    )
    existing_chart_feedback: str = dspy.InputField(
        desc="Existing feedback on the chart from other sources, if any, to build upon."
    )

    used_guideline_ids: list[str] = dspy.OutputField(
        desc="List of guideline IDs from the catalog that were definitively used to generate the rationale."
    )
    feedback: str = dspy.OutputField(
        desc="\n".join(
            [
                "Feedback strictly grounded in the catalog guidelines.",
                "Always add citations to the specific guideline IDs you used. Ensure every suggestion references at least one retrieved ID. Never cite the labels you searched for.",
                "Ensure that you query the catalog deeply to find relevant rules before giving feedback.",
                "Your feedback should be actionable, completely distinct top 5 suggestions, each with brief rationale.",
                "Output in markdown format without fences.",
            ]
        )
    )


@dataclass(frozen=True, slots=True)
class GuidelineBrowserTools:
    """DSPy tool functions over a `Catalog` instance."""

    catalog: Catalog

    def _query_guidelines(
        self,
        df: pl.DataFrame,
        *,
        where_labels: list[str] | None = None,
        where_reftypes: list[str] | None = None,
    ) -> pl.DataFrame:
        matches_df = df

        if where_labels is not None:
            matches_df = matches_df.filter(
                pl.col("guideline")
                .struct.field("labels")
                .list.set_intersection(where_labels)
                .list.len()
                > 0
            )

        if where_reftypes is not None:
            matches_df = matches_df.filter(
                pl.col("references")
                .list.join("\n\n")
                .str.contains_any([f"@{rt}{{" for rt in where_reftypes])
            )

        return matches_df

    def list_guideline_labels(self) -> list[str]:
        """
        [TAXONOMY DISCOVERY] Discover all available topic labels in the catalog.

        Returns a sorted list of searchable labels covering visual design, tasks, accessibility, and other topics.

        OUTPUT: List of label strings you can use in `list_guideline_abstracts(where_labels=[...])`
        """
        return (
            self.catalog.df()
            .select("guideline")
            .unnest("guideline")
            .select("labels")
            .explode("labels")
            .unique("labels")
            .sort("labels")["labels"]
            .to_list()
        )

    def list_reftypes(self) -> list[str]:
        """
        [REFERENCE TYPE DISCOVERY] Discover available source types for filtering by authority.

        OUTPUT: List of reference type strings for filtering.
        """
        return (
            self.catalog.df()
            .select("references")
            .explode("references")
            .select(
                reftype=pl.col("references").str.split("{").list.get(0).str.slice(1)
            )
            .drop_nulls()
            .unique()
        )["reftype"].to_list()

    def list_guideline_abstracts(
        self,
        where_labels: list[str] | None = None,
        where_reftypes: list[str] | None = None,
    ) -> str:
        """
        [GUIDELINE SEARCH] Search for relevant guidelines by topic and optionally filter by source authority.

        Returns CSV with columns: id, title, description, labels.

        NEXT STEP: Note promising 'id' values, then call `read_guidelines_by_id([...])`.
        """
        matches_df = self._query_guidelines(
            self.catalog.df(),
            where_labels=where_labels,
            where_reftypes=where_reftypes,
        )

        abstract_df = matches_df.select(
            pl.col("id"),
            pl.col("guideline").struct.field("title"),
            pl.col("guideline").struct.field("description"),
            pl.col("guideline").struct.field("labels").list.join(";"),
        )
        stringio = StringIO()
        abstract_df.write_csv(stringio)

        return stringio.getvalue()

    def read_guidelines_by_id(self, ids: list[str]) -> list[dict]:
        """
        [DETAILED RETRIEVAL] Get full content and citations for specific guidelines.

        Returns list of dicts with: id, body (full rationale + details), references.
        """
        id_df = pl.DataFrame({"id": ids})
        matched_df = id_df.join(self.catalog.df(), on="id", how="inner")
        return matched_df.select(
            "id",
            pl.col("guideline").struct.field("body"),
            "references",
        ).to_dicts()


class GuidelineBrowserStrategy(RetrievalStrategy):
    """ReAct strategy for browsing a guideline catalog to retrieve relevant guidelines."""

    id = "guideline-browser@v0"

    def __init__(
        self,
        *,
        catalog: Catalog,
        lm: dspy.LM,
    ) -> None:
        super().__init__(catalog)
        self._tools = GuidelineBrowserTools(catalog=catalog)
        self._lm = lm
        self._program = dspy.ReAct(
            GuidelineBrowserSignature,
            tools=[
                self._tools.list_guideline_labels,
                self._tools.list_reftypes,
                self._tools.list_guideline_abstracts,
                self._tools.read_guidelines_by_id,
            ],
        )

    @property
    def tools(self) -> GuidelineBrowserTools:
        return self._tools

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        inputs = guideline_browser_inputs_from_request(request)
        with dspy.context(lm=self._lm):
            prediction = self._program(
                chart=inputs.chart,
                situation=inputs.situation,
                chart_spec=inputs.chart_spec,
                existing_chart_feedback=inputs.existing_chart_feedback,
            )

        used_ids = list(getattr(prediction, "used_guideline_ids", []))
        id_to_entry = {entry.id: entry for entry in self.catalog.entries}
        retrieved_entries = [id_to_entry[gid] for gid in used_ids if gid in id_to_entry]

        return RetrievalResponse(
            catalog=Catalog(entries=retrieved_entries),
            meta={"used_guideline_ids": used_ids},
        )
