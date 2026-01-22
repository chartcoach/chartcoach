---
id: provide-a-human-readable-data-table-for-each-chart
title: "Provide a human-readable data table for the chart\u2019s underlying data (unless\
  \ the title and text fully convey the data)"
bibliography: references.bib
description: Include a human-readable data table for a chart, unless accompanying
  text already conveys all relevant information.
labels:
- chart:general
- task:access
- visual:multiple
- impact:accessibility
- data:tabular
- audience:general
- principle:compromising
- critical:true
---

## Provide a data table fallback for the chart <!-- role: advice -->

Provide a table that contains a human-readable version of the data the chart is based on. Omit the table only if the chart title, summary, context, or annotations already convey all relevant information contained in the chart.

## Data tables provide a tolerant alternative information path <!-- role: reason -->

A table provides a redundant, human-readable information flow that can be consumed differently than a graphical encoding, supporting transparency about the underlying values and tolerance for different ways people access information.

**Mechanism:** A table exposes the exact data values and labels in a format that can be read and navigated independently of chart perception and interaction, reducing the chance that essential information is available only through the visual or interactive form.

**Evidence:** Effective description practices for complex scientific visuals include providing data tables where appropriate to make the information understandable to blind readers. [@wgbh_effective_practices_2; @wgbh_effective_practices_3] A visualization accessibility heuristic evaluation framework treats “no table” as a critical failure unless accompanying text already conveys all relevant information. [@elavskyHowAccessibleMy2022]

**Notes:** A table is not an equivalent replacement for a visualization’s narrative or structure and does not, by itself, make the visualization accessible. [@elavskyHowAccessibleMy2022]

## When a table is needed as a fallback representation <!-- role: context -->

- **User Goal:** Access the underlying chart values and interpret what the chart shows even if the graphical form is hard to use.
- **Task:** Retrieve specific values, verify labels/units/metrics, and understand trends or relationships described in the chart.
- **Data:** Values that originate from a tabular dataset (categories, series, units, and measurements) that can be represented as rows and columns.
- **Chart Setting:** Static or interactive charts where some information may otherwise be available only through visual inspection or interactive exploration.
- **Audience:** People who may prefer or require non-visual or alternative representations, including people using assistive technologies. [@elavskyHowAccessibleMy2022]
- **Success Criterion:** All relevant information contained in the chart is available in a human-readable form without relying on the chart’s visual encodings alone.

## When you can omit the data table <!-- role: exceptions -->

**Break it when:** The chart title, summary, context, or annotations already convey all relevant information contained in the chart. **Why:** The table would not add additional necessary information beyond what is already available in text. [@elavskyHowAccessibleMy2022]

## Tradeoffs of adding a table <!-- role: costs -->

**Sacrifice:** Additional space and maintenance effort to keep the table consistent with the chart’s data. **Risk:** Readers may be directed to the table as a total substitute for the visualization’s narrative or structured relationships. **Mitigation:** Treat the table as a fallback representation of values rather than a replacement for the visualization experience. [@elavskyHowAccessibleMy2022]

## Common ways this guideline fails in practice <!-- role: mistakes -->

- **Mistake:** Provide only a table and treat it as equivalent access to the visualization. **Why it fails:** A table alone does not provide the visualization’s narrative or structured relationships and does not address other accessibility needs of the chart. [@elavskyHowAccessibleMy2022]
- **Mistake:** Provide a table that is not human-readable (e.g., missing labels, units, or clear organization). **Why it fails:** The fallback does not support understanding of the underlying variables, metrics, and values that the visualization communicates. [@wgbh_effective_practices_2; @wgbh_effective_practices_3]

## How to quickly verify a table fallback exists and is sufficient <!-- role: check -->

**Failure Sign:** The only way to obtain exact values is by reading the chart visually or by performing chart interactions, with no visible data table provided. **Quick Check:** Look for a table that lists the same variables and values the chart encodes, with human-readable labels. **Stronger Test:** Compare the chart’s communicated information to the table and accompanying text; confirm that the table (or the text exception) covers all relevant information contained in the chart. [@elavskyHowAccessibleMy2022]

## Practical ways to satisfy the requirement <!-- role: fix -->

- Provide a table that includes the chart’s underlying values with clear row/column labels, including variables, units, and metrics.
- Keep the table aligned with the chart’s data so that the values correspond to what the chart encodes.
- If you omit the table, provide a title, summary, context, or annotations that convey all relevant information contained in the chart.
- Use the table as a fallback for values while still addressing the chart’s other accessibility needs rather than treating the table as sufficient on its own. [@elavskyHowAccessibleMy2022]
