---
id: use-clear-axis-labels
title: Provide Clear, Untruncated Axis Labels
bibliography: references.bib
description: Ensure every axis is clearly labeled (including units), and never truncate
  an axis without an explicit label or an equivalent textual explanation.
labels:
- chart:generic
- task:read
- visual:position
- impact:clarity
- impact:accessibility
- data:quantitative
- audience:general
- category:understandable
- source:community-practices
---

## The Rule <!-- role: advice -->

Provide clear axis labels (including units where applicable), and do not truncate an axis unless the truncation is explicitly and clearly labeled; only remove axes in rare cases where an adequate text explanation or annotation is provided.

## The Logic <!-- role: reason -->

Unclear, missing, or ambiguously truncated axes increase ambiguity and interpretation effort, raising cognitive load and making it easier for readers to misinterpret the data; clear axis titling and explicit truncation labelling prevents misreading and supports understandability in accessibility auditing practice [@elavskyHowAccessibleMy2022; @yellowfinbi_chart_axis].

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly interpreting what values mean and how the scale should be read (e.g., understanding magnitude and units).
- **Data Type:** Quantitative values encoded by position along one or more axes (any chart with an x- and/or y-axis).
- **Audience:** Anyone who may not infer scale and units implicitly, including readers under time pressure or with higher cognitive load [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Removing an axis entirely.
- **Reason:** This is acceptable only in rare cases when an adequate text explanation or annotation is provided that replaces the axis information (i.e., the chart remains unambiguous without the axis) [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** More visual space used for axis titles/labels and explanatory text.
- **The Risk:** If you add labels without a consistent convention (e.g., inconsistent abbreviations), you can introduce new ambiguity rather than reducing it [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Truncating the axis without clearly indicating truncation.
- **Why it fails:** Readers may interpret the scale as continuous from the baseline, which can change the perceived meaning of the plotted values and increase misinterpretation risk [@yellowfinbi_chart_axis; @elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Using abbreviations inconsistently across axes or charts.
- **Why it fails:** Abbreviations are allowed only with a clear and consistent convention; inconsistency adds cognitive work and ambiguity [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Omitting axis titles/units and assuming context will carry the meaning.
- **Why it fails:** Missing titles/units forces inference and increases cognitive load, undermining clarity [@yellowfinbi_chart_axis; @elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** An axis has no label/title, units are missing, labels are unclear/ambiguous, or the axis appears cut off/does not start where a reader would expect without any explicit cue.
- **The Test:** Ask, “Can I identify what this axis represents and its unit without guessing?” and “If the axis is truncated, is that truncation explicitly and clearly labeled (or replaced by adequate annotation/text)?” [@elavskyHowAccessibleMy2022; @yellowfinbi_chart_axis].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an axis title and clarify labels (including units); if truncation is used, add a clear truncation label.
- **Best Fix:** Provide axis titles and units plus a clear, consistent labeling convention (including consistent abbreviations), and if axes are removed, replace them with adequate explanatory text or annotation that preserves unambiguous interpretation [@elavskyHowAccessibleMy2022; @yellowfinbi_chart_axis].
