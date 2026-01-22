---
id: add-precise-description-legend-and-source-to-explain-what-the-chart-shows
title: Add a precise description, direct labels or legend, and a source so readers
  know what the chart shows
bibliography: references.bib
description: Finish charts with precise descriptive text, clear series identification,
  and a source for transparency and interpretation.
labels:
- chart:general
- task:interpret
- visual:text
- impact:trust
- data:general
- audience:general
- component:metadata
---

## Finish the chart with precise description, clear series identification, and a source <!-- role: advice -->

Add a description that precisely defines what is being measured (including scope and timeframe), label every data-encoding element via direct labels or a legend, and include a data source.

## Why finishing text prevents misreadings and builds trust <!-- role: reason -->

Readers did not participate in your analysis process; without explicit definitions, they may misinterpret units, time periods, categories, or what is included, and without a source they cannot assess or verify the data.

**Mechanism:** Descriptions and labels remove ambiguity about what the marks represent, and sources provide transparency that supports credibility and reuse.

**Evidence:** Precise descriptions and keys are essential for reader understanding of what is shown, and including a source improves transparency and credibility for the audience [@muth_better_charts_2017].

**Notes:** Labels should be as close as possible to what they label to reduce reader effort.

## When to add description, labels/legend, and source <!-- role: context -->

- **User Goal:** Correctly interpret measures, categories, and time scope without prior knowledge.
- **Task:** Decode the chart and understand inclusion/exclusion boundaries (e.g., “selected” categories, fiscal vs calendar periods).
- **Data:** Any dataset where scope, definitions, or timeframe could be misunderstood.
- **Chart Setting:** Published charts in articles, reports, or presentations where the chart must stand alone.
- **Audience:** First-time viewers; readers who may not know the domain conventions.
- **Success Criterion:** A reader can explain what the chart measures, over what time span, and where the data came from.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart is a private draft used only among collaborators who share definitions and sources elsewhere in the same artifact. **Why:** Redundant metadata can be unnecessary during rapid iteration.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Space and time to write careful text. **Risk:** Overly long descriptions can reduce scannability and compete with the chart. **Mitigation:** Keep descriptions precise and compact while preserving the critical qualifiers (scope, units, timeframe, selection).

## Common ways this fails in practice <!-- role: mistakes -->

- **Mistake:** Using a vague description that omits key qualifiers (scope, units, timeframe, selection). **Why it fails:** Readers fill gaps with assumptions and interpret the chart incorrectly.
- **Mistake:** Leaving series unlabeled or relying on distant legends. **Why it fails:** Readers spend effort matching colors/lines to labels and may make decoding errors.
- **Mistake:** Omitting the source. **Why it fails:** Readers cannot evaluate credibility or reproduce the analysis.

## Quick tests <!-- role: check -->

**Failure Sign:** A reader asks what the unit is, what time period is used, or what the categories represent. **Quick Check:** Cover the surrounding article text and see if the chart still answers “what, where, when, and in what units.” **Stronger Test:** Ask a reader to restate the chart description in their own words; if they omit key qualifiers, the description is not precise enough.

## What to do instead <!-- role: fix -->

- Rewrite the description to include metric, unit, population/scope, timeframe, and any selection qualifier that matters.
- Replace a legend with direct labels where possible, or move the legend closer to the data it explains.
- Add the source line even if it is “internal reporting,” and make it specific enough to be traceable.
- If space is constrained, shorten non-essential phrasing but keep the defining qualifiers intact.
