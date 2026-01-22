---
id: define-metrics-variables-units-and-data-source-near-the-chart
title: Define every metric, variable, unit, and data source adjacent to the chart
bibliography: references.bib
description: Prevent ambiguity and cognitive overload by defining metrics, variables,
  calculations, units, and the data source close to the visualization.
labels:
- chart:all
- task:interpret
- visual:text
- impact:clarity
- data:any
- audience:all
- accessibility:cognitive
- chartability:understandable
---

## Define metrics, variables, units, and source beside the visualization <!-- role: advice -->

Define all metrics, variables, calculations, and units, and name the data source in text placed next to the chart or data interface. Do not require readers to search elsewhere in the surrounding content to learn what the chart’s measures mean.

## Why definitions reduce ambiguity and cognitive load <!-- role: reason -->

Undefined measures force readers to infer meaning, which increases ambiguity and makes it harder to build an accurate mental model of what the chart encodes and how values were computed.

**Mechanism:** Clear definitions externalize assumptions (variable meaning, units, computation rules, and provenance) so readers can interpret encodings without guessing or holding unresolved questions in working memory.

**Evidence:** Accessible descriptions of scientific charts and diagrams require explicit definitions of variables, units, and metrics, plus supporting context such as summaries and tables when needed, to make the information understandable to blind readers using audio access [@wgbh_effective_practices; @ncam_ncam_diagram]. A visualization-auditing heuristic framework for accessibility includes “Metrics and variables are undefined” as an Understandable failure and requires that data, calculations, and sources be defined near the chart [@elavskyHowAccessibleMy2022].

**Notes:** Definitions can appear in a caption, short glossary block, or nearby explanatory text, as long as they are immediately available at the point of interpretation.

## Where undefined metrics commonly occur <!-- role: context -->

- **User Goal:** Interpret what measures mean and use the visualization to draw a correct conclusion.
- **Task:** Understand encodings, compare values, and trust how numbers were computed.
- **Data:** Derived metrics, transformations, indices, rates, and composite scores with non-obvious units or denominators.
- **Chart Setting:** Any chart embedded in longer content where definitions might otherwise be placed elsewhere (e.g., body text, footnotes, appendix, separate tab).
- **Audience:** Readers with limited domain context, readers using audio access, and anyone scanning without reading surrounding prose.
- **Success Criterion:** Readers can explain what each metric represents, its unit, and how it was computed, and can identify the data source without leaving the chart context.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart contains no metrics or variables (for example, it is purely decorative and conveys no data). **Why:** There is nothing measurable to define, so adding definitions would not clarify interpretation [@elavskyHowAccessibleMy2022].

## Tradeoffs of adding definitions near the chart <!-- role: costs -->

**Sacrifice:** Space and visual simplicity may decrease because definitions and provenance text take room. **Risk:** Overly long or technical definitions can increase reading burden and distract from the chart’s main message. **Mitigation:** Keep definitions concise and focused on what is necessary to interpret the chart [@wgbh_effective_practices].

## Common ways this fails in practice <!-- role: mistakes -->

**Mistake:** Using abbreviations or internal metric names without stating what they mean or how they are calculated. **Why it fails:** Readers must guess the meaning and computation, making interpretation ambiguous and potentially misleading [@elavskyHowAccessibleMy2022].\
**Mistake:** Explaining metrics only in distant paragraphs or another page/section. **Why it fails:** The definition is not convenient at the moment of interpretation, increasing cognitive load and reducing usability for readers who rely on nearby text [@wgbh_effective_practices; @elavskyHowAccessibleMy2022].

## How to quickly verify definitions are present <!-- role: check -->

**Failure Sign:** A reader cannot tell what a measure represents, its unit, how it was computed, or where it came from without leaving the chart context. **Quick Check:** For each axis, legend, tooltip field, and headline number, ask “What is this, in what unit, computed how, from what source?” and confirm the answer is visible next to the chart. **Stronger Test:** Ask a reader unfamiliar with the dataset to restate each metric and its unit and source using only the chart area and its adjacent text, and note any missing or incorrect interpretations [@elavskyHowAccessibleMy2022].

## Practical fixes for undefined metrics and variables <!-- role: fix -->

- Add a short caption or nearby glossary that defines every variable name, metric, and unit used in the chart.
- Describe any calculation rules that produce derived measures (for example, rates, indices, or composites) in the same adjacent text block.
- Provide the data source in the same location as the definitions so provenance is available at the point of interpretation.
- Add a supporting representation (such as a table or structured summary) when definitions alone are insufficient to make complex measures understandable in non-visual access [@wgbh_effective_practices].
