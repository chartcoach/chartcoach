---
id: label-axes-clearly-and-avoid-unmarked-truncation
title: Label axes clearly and do not truncate axes without an explicit label
bibliography: references.bib
description: Provide clear axis labels (including any truncation) so values can be
  interpreted unambiguously with minimal cognitive effort.
labels:
- chart:cartesian
- task:read-values
- visual:position
- impact:clarity
- data:quantitative
- audience:general
- accessibility:cognitive
---

## Axis labels must be present, clear, and non-ambiguous <!-- role: advice -->

Ensure axes are present and clearly labeled, and never truncate an axis unless the truncation is explicitly labeled. You may abbreviate axis labels only if you use a clear and consistent convention.

## Clear axis labeling reduces ambiguity and misreading <!-- role: reason -->

Axis labels establish what a positional encoding means and how to interpret magnitude, direction, and units; missing, unclear, or silently truncated axes force readers to infer the scale and can increase cognitive load and misinterpretation.

**Mechanism:** Clear labels and explicit truncation cues reduce inference work, prevent incorrect mental models of the scale, and support consistent decoding of position-based values.

**Evidence:** Clear axis titles and units help prevent misinterpretation, and truncating axes without clear labeling risks misleading readings of magnitude [@yellowfinbi_chart_axis]. Auditing heuristics for visualization accessibility treat unclear or missing axis labels as an understandable barrier that can increase ambiguity and cognitive load [@elavskyHowAccessibleMy2022].

**Notes:** Removing axes can be acceptable only when equivalent clarity is provided through visible text explanation or annotation.

## When to apply axis labeling checks <!-- role: context -->

- **User Goal:** Interpret what values mean on the chart and compare magnitudes accurately.
- **Task:** Read exact/approximate values, compare differences, or understand scale and units.
- **Data:** Quantitative measures mapped to axis position, including cases where units or baselines matter.
- **Chart Setting:** Any chart with axes, especially when space constraints encourage truncation or abbreviation.
- **Audience:** Mixed expertise, including readers with higher cognitive load sensitivity.
- **Success Criterion:** Readers can state what each axis represents (including units and any truncation) without guessing.

## When it can be acceptable to remove or reduce axes <!-- role: exceptions -->

**Break it when:** The chart intentionally omits axes because a visually available text explanation or annotation fully communicates what the axes would have conveyed, including units and any non-zero baseline or truncation. **Why:** In those rare cases, the axis is redundant and the alternative text/annotation carries the necessary interpretive information [@elavskyHowAccessibleMy2022; @yellowfinbi_chart_axis].

## Tradeoffs of strict axis labeling <!-- role: costs -->

**Sacrifice:** Additional space and visual clutter, especially in small multiples or dense layouts. **Risk:** Over-labeling can compete with the data marks and reduce scanning efficiency. **Mitigation:** Keep labels concise and use consistent abbreviations rather than removing interpretive information.

## Common axis labeling failures <!-- role: mistakes -->

- **Mistake:** Omitting axis titles or units when they are needed to interpret the scale. **Why it fails:** Readers cannot reliably map position to meaning, increasing ambiguity and cognitive load [@elavskyHowAccessibleMy2022; @yellowfinbi_chart_axis].
- **Mistake:** Truncating an axis without an explicit label indicating truncation or a changed baseline. **Why it fails:** It can create misleading impressions about differences or trends because the scale change is hidden [@yellowfinbi_chart_axis].
- **Mistake:** Using abbreviations inconsistently across related charts or panels. **Why it fails:** It forces readers to relearn conventions and increases interpretation effort [@elavskyHowAccessibleMy2022].

## Quick checks for unclear or missing axis labels <!-- role: check -->

**Failure Sign:** A reader cannot state what an axis measures (and in what units), or the axis appears shortened/trimmed without a clear indication. **Quick Check:** Ask “What does each axis represent, including units?” and “Is the axis baseline or range altered, and is that explicitly labeled?” **Stronger Test:** Have a reviewer unfamiliar with the chart restate both axes and the baseline/range without prompts; any confusion indicates the labels or truncation cues are insufficient [@elavskyHowAccessibleMy2022].

## Fix unclear or missing axis labels <!-- role: fix -->

- Add axis titles that clearly name the measured quantity and include units where applicable.
- If an axis is truncated, add an explicit label indicating truncation or the adjusted baseline so the scale change is unambiguous.
- Use abbreviations only with a clear, consistent convention applied across the full visualization (and across panels if present).
- If axes are removed, add a visually available text explanation or annotation that provides the same interpretive information the axes would have provided, including units and any truncation or baseline changes.
