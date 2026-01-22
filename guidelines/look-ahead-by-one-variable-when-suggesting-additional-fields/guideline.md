---
id: look-ahead-by-one-variable-when-suggesting-additional-fields
title: Suggest views that add exactly one non-selected variable to the current selection
bibliography: references.bib
description: "Generate multivariate suggestions by augmenting the user\u2019s selected\
  \ variables with one additional field at a time."
labels:
- chart:gallery
- task:explore
- visual:layout
- impact:coverage
- data:multivariate
- audience:novice
- system:recommendation
---

## Expand the selection by one variable per suggested view <!-- role: advice -->

For a selected variable set, recommend charts that include the user-selected variables plus exactly one additional variable, rather than jumping to larger combinations by default.

## One-step suggestions balance breadth with orientation <!-- role: reason -->

Adding one variable at a time provides a manageable exploration gradient: users can attribute changes in a view to a single new field and avoid combinatorial explosion. This also supports systematic coverage because each non-selected field can be introduced as a single-step extension.

**Mechanism:** Single-step expansions keep the recommendation space navigable and reduce confusion about which added variable caused a pattern.

**Evidence:** The recommendation strategy constructs suggested variable sets by taking the user’s selected set and forming new sets that add exactly one non-selected variable, explicitly to promote breadth while keeping users oriented and avoiding combinatorial overload [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

**Notes:** Users can still reach higher-order combinations by iterating selections.

## When the user has selected a set of variables and wants ideas <!-- role: context -->

- **User Goal:** Find additional variables that relate to the current selection.
- **Task:** Relationship discovery and hypothesis generation.
- **Data:** Many available fields, making full enumeration infeasible.
- **Chart Setting:** Recommendation-driven gallery with faceted steering controls.
- **Audience:** Users exploring without a complete mental model of the dataset.
- **Success Criterion:** Suggestions feel understandable and systematically cover the dataset.

## When to deviate from single-step look-ahead <!-- role: exceptions -->

**Break it when:** The user explicitly requests higher-dimensional views (for example, exploring three-way interactions) and is willing to trade simplicity for richer slices. **Why:** Single-step additions can slow access to complex relationships once the user is ready to go deeper [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Tradeoffs of one-variable-at-a-time suggestions <!-- role: costs -->

**Sacrifice:** It can take more interactions to reach complex multivariate views. **Risk:** Users may miss emergent patterns that only appear with multiple added variables simultaneously. **Mitigation:** Provide an easy way to select another variable and immediately refresh suggestions [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Common mistakes in variable suggestion design <!-- role: mistakes -->

**Mistake:** Recommending many-variable charts by default (adding several new fields at once). **Why it fails:** Users lose track of what changed and the recommendation set becomes hard to scan and interpret [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Checks for whether suggestions are digestible <!-- role: check -->

**Failure Sign:** Users ask “what is different between these charts?” or cannot name the newly introduced field. **Quick Check:** For each suggestion, verify there is exactly one capsule/field not present in the selected set. **Stronger Test:** In a think-aloud session, measure whether users can correctly describe what new variable each suggestion introduces [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## What to do if users need richer combinations <!-- role: fix -->

- Add an “include/exclude variable” control so users can iteratively build higher-order sets through repeated single-step additions.
- Provide bookmarking so users can save promising single-step findings before moving to more complex views.
- Offer an explicit mode (or filter) to request multi-variable look-ahead only when needed [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
