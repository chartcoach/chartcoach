---
id: support-lightweight-in-place-refinements-instead-of-enumerating-parameter-variants
title: Support lightweight in-place refinements instead of enumerating parameter variants
bibliography: references.bib
description: Avoid consuming gallery space with minor variants by offering simple
  interactive adjustments on demand.
labels:
- chart:interactive
- task:refine
- visual:scale
- visual:sort
- impact:scannability
- data:categorical
- audience:novice
- system:gallery
---

## Replace minor chart variants with direct refinement controls <!-- role: advice -->

Do not enumerate small parameter variations (such as sort order, axis transposition, or linear vs. log scale) as separate recommended charts; provide simple interactions that let users adjust these parameters on demand.

## Fine-tuning preserves gallery capacity for meaningful differences <!-- role: reason -->

Minor variants are important but can flood a gallery if shown as separate recommendations. Moving these into interactive controls keeps the default gallery focused on substantive differences (variables and transformations) while still enabling users to reach the variants they need.

**Mechanism:** Interaction-based parameter changes reduce redundant thumbnails and keep exploration moving without forcing users to choose among near-identical charts.

**Evidence:** The design collapses the space of small but important parameter variations to a single default chart while providing interactions for fine-tuning (for example, transpose, sorting, and scale toggles) [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

**Notes:** These refinements are especially useful in an expanded view where the chart is larger.

## When parameter variants are common and space is limited <!-- role: context -->

- **User Goal:** Adjust a view to better read it without losing momentum.
- **Task:** Quick chart refinement during exploration.
- **Data:** Variables where sorting and scale choice affect readability (for example, categorical axes, skewed quantitative fields).
- **Chart Setting:** Recommendation gallery with many charts competing for limited space.
- **Audience:** Users who benefit from defaults but occasionally need adjustments.
- **Success Criterion:** Users can reach useful variants quickly without wading through redundant recommendations.

## When explicit variant enumeration can be acceptable <!-- role: exceptions -->

**Break it when:** The goal is to explicitly compare parameter variants side-by-side as part of the analysis. **Why:** Interactive toggles hide the comparison and may impede evaluating differences across variants [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Tradeoffs of interaction-based refinements <!-- role: costs -->

**Sacrifice:** Users may not discover that a better parameterization exists unless they try the controls. **Risk:** Defaults can bias interpretation if users never adjust them. **Mitigation:** Place refinement controls in a visible location in expanded mode and keep them simple [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Common mistakes with parameter variation <!-- role: mistakes -->

**Mistake:** Generating separate gallery entries for each sort and scale option. **Why it fails:** It reduces scannability and crowds out views that would increase dataset coverage [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Quick checks for parameter-variant overload <!-- role: check -->

**Failure Sign:** Many gallery items have identical variable sets and mark types and differ only by ordering or scale. **Quick Check:** For a given variable set, verify only one default chart appears in the main gallery. **Stronger Test:** Track whether users can achieve common refinements (sort, transpose, log) without leaving the current view [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## What to do if users still request more variants <!-- role: fix -->

- Add explicit controls for transpose, sorting, and scale transforms in the expanded view.
- Provide sensible defaults for these parameters so the first view is generally readable.
- Keep alternative encodings in a drill-down list, but keep parameter tweaks as interactions rather than additional thumbnails [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
