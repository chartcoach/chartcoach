---
id: match-data-scales-to-permissible-operations-before-choosing-analyses-or-encodings
title: Match data scales to permissible operations before choosing analyses or encodings
bibliography: references.bib
description: Use nominal, ordinal, interval, and ratio scales to determine valid operations
  and suitable encodings.
labels:
- chart:general
- task:encode
- visual:general
- impact:accuracy
- data:categorical
- audience:general
- workflow:analyze
---

## Match data scales to permissible operations before choosing analyses or encodings <!-- role: advice -->

Identify whether each variable is nominal, ordinal, interval, or ratio, and only use analyses and encodings that are valid for that scale.

## Why scale-aware design avoids invalid comparisons and misleading summaries <!-- role: reason -->

Different scales permit different operations; treating nominal or ordinal values as if they were interval/ratio invites invalid arithmetic and misinterpretation. Scale-aware choices prevent the visualization from implying operations (like differences or averages) that the data do not support.

**Mechanism:** Data scale constrains which transformations (such as ranking or averaging) are meaningful and which visual channels communicate ordered magnitude versus categorical identity.

**Evidence:** The framework distinguishes nominal, ordinal, interval, and ratio scales based on permissible logical and mathematical operations, and notes that scale influences which analyses and visual encodings can be used [@bornerDataVisualizationLiteracy2019].

**Notes:** Conversions between scales are possible but should be treated as transformations with implications for interpretation.

## When data-scale checks are required <!-- role: context -->

- **User Goal:** Ensure the visualization’s implied comparisons match the data’s meaning.
- **Task:** Choose analyses, summaries, and encodings for variables.
- **Data:** Mixed-type tables with categorical and numeric columns; variables that may be binned or recoded.
- **Chart Setting:** Any; especially when aggregating or computing summaries.
- **Audience:** General audiences who may assume numeric-looking axes imply numeric operations.
- **Success Criterion:** No arithmetic or ordering is implied where it is not valid.

## When not to keep the original scale unchanged <!-- role: exceptions -->

**Break it when:** You intentionally transform quantitative variables into categories (for example, thresholding into bins) to support a categorical task. **Why:** The transformed variable is no longer interpreted as interval/ratio after binning, so the design should reflect the new scale.

## Tradeoffs of strict scale matching <!-- role: costs -->

**Sacrifice:** Flexibility to compute convenient summaries on variables that do not support them. **Risk:** Overemphasis on scale labels can slow iteration when the correct next step is to transform the variable. **Mitigation:** Document any scale-changing transformation and ensure the visualization reflects the transformed meaning.

## Common scale-related failure modes <!-- role: mistakes -->

**Mistake:** Computing averages or differences on ordinal ranks. **Why it fails:** Ordinal scales encode order without meaningful intervals, so arithmetic implies unsupported distances.

## Quick tests for scale-encoding alignment <!-- role: check -->

**Failure Sign:** The chart invites arithmetic comparisons (differences, means) on variables that are categories or ranks. **Quick Check:** For each axis/legend, ask “Is order meaningful?” and “Are equal steps meaningful?” **Stronger Test:** Have a reader explain what operations they believe the chart supports and compare that to the variable’s scale.

## What to do when the needed operation is not valid for the scale <!-- role: fix -->

- Transform the variable to a scale that supports the required operation and describe the transformation.
- Reframe the stakeholder question to an insight need that fits the available scales.
- Choose an analysis that is valid for the scale, such as ranking for ordinal rather than averaging.
- Redesign the encoding to emphasize identity channels for nominal variables instead of magnitude channels.
