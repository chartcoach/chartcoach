---
id: describe-visually-apparent-relationships-in-text
title: Describe visually apparent patterns and relationships in text
bibliography: references.bib
description: Provide a text description of trends, clusters, outliers, and other visually
  apparent relationships so key insights are available without vision.
labels:
- chart:general
- task:interpret
- visual:relationship
- impact:accessibility
- data:multivariate
- audience:assistive-technology
- accessibility:assistive
---

## Describe chart-level patterns and relationships in text <!-- role: advice -->

Describe trends, clusters, patterns, outliers, and other significant statistical semantics in text, not only through visual cues. Ensure the description communicates the relationships that a sighted viewer would likely notice quickly.

## Why relationship descriptions reduce user labor <!-- role: reason -->

When meaning is carried primarily by visual pattern recognition, users who cannot access those visual cues must reconstruct the same insights through higher-effort exploration or may miss them entirely. Making visually apparent relationships available in text shifts key interpretation work from painstaking element-by-element inspection toward a direct, comparable summary.

**Mechanism:** Textual descriptions make key “info and relationships” determinable without relying on sensory characteristics, enabling access to higher-level structure (e.g., “overall increase,” “one clear outlier,” “two clusters”) rather than forcing navigation through individual marks.

**Evidence:** Structural meaning and relationships conveyed visually should also be available in a form that does not depend on visual perception, so users can determine relationships without relying on sensory characteristics alone [@w3c_understanding_info; @elavskyHowAccessibleMy2022]. Chart sonification can expose data patterns through audio mappings and keyboard control as an additional non-visual channel for perceiving trends and outliers [@highcharts_highcharts_accessibility; @elavskyHowAccessibleMy2022].

**Notes:** This guideline targets relationship-level semantics (patterns and findings), not only mark-level values.

## When “visually apparent” semantics must be described <!-- role: context -->

- **User Goal:** Understand the main findings and relationships in a visualization without relying on vision.
- **Task:** Identify trends, compare groups, notice outliers, recognize clusters, or extract the “takeaway.”
- **Data:** Any dataset where meaning is expressed as relationships among marks (e.g., correlation patterns, temporal trends, group separation, exceptional points).
- **Chart Setting:** Static or interactive charts where insights are primarily communicated through spatial arrangement, clustering, shape, or other emergent visual patterns.
- **Audience:** People using assistive technologies or who cannot reliably perceive visual relationships, including screen reader users.
- **Success Criterion:** A user can access the key patterns and findings via text at a minimum, without having to infer them solely from visual structure.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization does not communicate any higher-level relationships beyond what is already fully and explicitly presented in text. **Why:** There are no additional visually apparent semantics to translate into a separate relationship description [@elavskyHowAccessibleMy2022].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional authoring time to write and maintain relationship-level descriptions as the chart or data changes. **Risk:** Overstating findings or implying statistical significance that is not warranted by the data. **Mitigation:** Keep relationship descriptions tightly aligned to what the visualization presents as the intended, significant semantics [@elavskyHowAccessibleMy2022].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Providing only mark-level text (e.g., listing data points) with no chart-level patterns or findings. **Why it fails:** It forces high labor navigation to reconstruct trends, clusters, or outliers that were meant to be quickly perceived visually [@elavskyHowAccessibleMy2022].
- **Mistake:** Describing patterns using sensory-only language (e.g., “the red line,” “the points on the left”). **Why it fails:** It depends on sensory characteristics rather than conveying relationships in a non-visual form [@w3c_understanding_info; @elavskyHowAccessibleMy2022].

## Quick tests <!-- role: check -->

**Failure Sign:** A non-visual user can access values or labels but cannot access statements about overall trends, clusters, or outliers. **Quick Check:** Remove reliance on visual inspection and verify that the chart’s key findings (trends/outliers/clusters) exist in text somewhere associated with the chart. **Stronger Test:** Confirm the relationship description communicates “info and relationships” without requiring sensory characteristics to interpret it [@w3c_understanding_info; @elavskyHowAccessibleMy2022].

## What to do instead <!-- role: fix -->

- Write a concise text description that explicitly states the key trends, clusters, outliers, and comparisons the visualization is meant to make apparent [@elavskyHowAccessibleMy2022].
- Ensure the relationship description does not rely on sensory characteristics to identify elements, and instead names the relevant variables, groups, or conditions [@w3c_understanding_info; @elavskyHowAccessibleMy2022].
- Provide an additional non-visual channel, such as chart sonification with keyboard controls, when it helps convey patterns like trend shape, peaks, or anomalies [@highcharts_highcharts_accessibility; @elavskyHowAccessibleMy2022].
- If relationship-level meaning cannot be expressed with available semantics in the current interface, add or revise the supporting text so the intended higher-level findings remain accessible at a minimum [@elavskyHowAccessibleMy2022].
