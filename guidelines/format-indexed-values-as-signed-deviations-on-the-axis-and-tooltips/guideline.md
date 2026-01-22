---
id: format-indexed-values-as-signed-deviations-on-the-axis-and-tooltips
title: "Format indexed values as signed deviations everywhere (axis and tooltips)\
  \ to reinforce \u201Cchange from baseline\u201D"
bibliography: references.bib
description: Prevent index misreads by consistently displaying deviations as negative/positive
  changes rather than raw magnitudes.
labels:
- chart:line
- task:interpret-change
- visual:text
- impact:clarity
- data:temporal
- audience:novice
- custom:tooltip
---

## Show deviations with their sign in every numeric readout <!-- role: advice -->

When a chart encodes values as differences from a reference period, format the y-axis and tooltip numbers as signed deviations (for example, show “−11%” rather than “11”). Keep the same “from the baseline” framing in the axis labeling so viewers repeatedly see that values are deltas, not levels.

## Why consistent signed formatting prevents level-vs-change confusion <!-- role: reason -->

If numeric readouts drop the sign or otherwise present deltas as plain magnitudes, readers can revert to interpreting them as absolute quantities. Repeating “this is a deviation” through consistent signed numbers and baseline framing reduces the chance that viewers switch mental models between axis, tooltip, and narrative.

**Mechanism:** Signed values provide an immediate directional cue (above/below the baseline) and keep the viewer anchored on “difference from reference,” especially when multiple series meet at the baseline.

**Evidence:** A recommended fix for an indexed employment chart is to “keep repeating these concepts in symbolic terms” by putting the whole y-axis and every tooltip value in negative-percentage terms (e.g., “−11% instead of just plain 11”) so mainstream readers interpret the chart as change from the reference period [@mintzer_y_axis_2024].

**Notes:** This is most important when many lines converge at the baseline, which visually resembles “same value” unless the surrounding numeric cues emphasize “same reference point.”

## Use this when tooltips or axis labels are the main decoder <!-- role: context -->

- **User Goal:** Understand direction and size of change relative to a specific reference time point.
- **Task:** Read precise values from the axis and tooltips while comparing many series.
- **Data:** Indexed differences (percent or percentage-point differences) where the sign carries meaning.
- **Chart Setting:** Interactive or annotated chart with tooltips that users rely on for exact values.
- **Audience:** Readers unfamiliar with index charts or likely to assume absolute levels.
- **Success Criterion:** Readers consistently describe values as “above/below the reference period” when quoting numbers.

## When not to do this <!-- role: exceptions -->

**Break it when:** The values are intentionally displayed as absolute distances (magnitudes) where direction is irrelevant to the message. **Why:** Forcing signs can add cognitive noise and imply directional meaning that the analysis does not use.

## Tradeoffs of always-signed deltas <!-- role: costs -->

**Sacrifice:** Some viewers may find repeated minus signs visually heavy, and labels can become longer. **Risk:** If the underlying measure is not actually a delta (or mixes deltas and levels), signed formatting will mislead. **Mitigation:** Audit that every displayed value truly shares the same baseline definition.

## Common ways this goes wrong <!-- role: mistakes -->

- **Mistake:** Showing signed values on the axis but unsigned values in tooltips (or vice versa). **Why it fails:** Inconsistency invites viewers to switch interpretations between interaction states.
- **Mistake:** Using an index but labeling values like a normal rate (e.g., “employment rate: 11”). **Why it fails:** Readers interpret the number as a level, not a deviation from the reference period.

## Quick tests for consistent “delta” interpretation <!-- role: check -->

**Failure Sign:** People report the chart is showing current employment rates rather than changes from the reference period. **Quick Check:** Hover any series and read the tooltip aloud; if it doesn’t sound like a deviation (signed and baseline-framed), the formatting is too level-like. **Stronger Test:** Ask a reader what “11” means; if they answer with an absolute rate instead of “11 below/above the reference,” the signs or framing are missing.

## What to do instead if signed labels overwhelm the display <!-- role: fix -->

- Reduce the number of tick labels so the remaining signed labels have room to be legible.
- Put the baseline meaning directly into the baseline label so even sparse signed ticks remain interpretable.
- Use a short unit suffix that matches the delta framing (e.g., “% from 2023”) on key ticks rather than repeating long text everywhere.
- If interaction is limited, bake the delta framing into static annotations near the axis so readers do not need tooltips to learn the interpretation.
