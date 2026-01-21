---
id: define-all-metrics-variables-and-data-sources
title: Define All Metrics, Variables, and Data Sources
bibliography: references.bib
description: Define every metric, variable, calculation, unit, and data source directly
  next to the chart to prevent ambiguity and reduce cognitive load.
labels:
- chart:any
- task:interpret
- visual:text
- impact:clarity
- data:any
- audience:novice
- accessibility:understandable
---

## The Rule <!-- role: advice -->

Define every metric, variable, calculation, and data source used in the chart, and place those definitions as close to the chart or data interface as possible.

## The Logic <!-- role: reason -->

Undefined or misleading variables force users to guess meaning, increasing ambiguity and cognitive load and making the visualization harder to understand, especially when information must be consumed through description rather than direct visual inspection.

- **The Principle:** Reduce ambiguity by making variable meaning explicit at the point of use.
- **The Evidence:** Guidance on accessible description of scientific charts emphasizes defining variables, metrics, and related information so the content is understandable in non-visual consumption contexts [@wgbh_effective_practices], and Chartability formalizes this as an Understandable heuristic for auditing charts [@elavskyHowAccessibleMy2022].

## Where to Apply <!-- role: context -->

This advice is designed for any chart or data interface that uses metrics, variables, or computed values.

- **User Goal:** Understand what each encoded value represents without guessing.
- **Data Type:** Any dataset where values depend on definitions (variables/metrics/calculations/source).
- **Audience:** People who are new to the topic or encountering the chart outside the surrounding article context.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization contains no metrics/variables/calculations beyond self-evident labels already presented adjacent to the chart.
- **Reason:** If nothing is undefined, adding redundant definitions does not address an actual ambiguity flagged by this heuristic [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** More space near the chart for definitions and source/metadata.
- **The Risk:** If the added text is long or poorly organized, users may have more to read before reaching the visual content [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Defining variables only in distant body text or elsewhere on the page.
- **Why it fails:** Users may not have the definitions “ready and convenient” when interpreting the chart, reintroducing ambiguity and extra effort [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Providing a metric name without explaining what it means (or what it is calculated from).
- **Why it fails:** The variable remains effectively undefined, which can mislead interpretation [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Axis labels, legend items, or annotations use terms (metrics/variables) that a reader cannot interpret precisely from the chart area alone.
- **The Test:** Hide or ignore nearby paragraphs of body text and check whether the chart area itself still defines the metrics/variables/calculations/source unambiguously [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a short definitions block (or caption note) immediately adjacent to the chart listing each metric/variable and its meaning, plus the data source [@elavskyHowAccessibleMy2022].
- **Best Fix:** Provide chart-adjacent, structured metadata that defines metrics, variables, and calculations in a way that supports clear description and interpretation for non-visual access contexts [@wgbh_effective_practices], aligning with Chartability’s Understandable auditing intent [@elavskyHowAccessibleMy2022].
