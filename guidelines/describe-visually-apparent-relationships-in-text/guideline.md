---
id: describe-visually-apparent-relationships-in-text
title: Describe Visually Apparent Patterns and Relationships in Text
bibliography: references.bib
description: Describe trends, outliers, and other visually apparent relationships
  in text so key insights are available without vision.
labels:
- chart:any
- task:interpret
- visual:relationship
- impact:accessibility
- data:any
- audience:all
- category:assistive
- source:chartability
---

## The Rule <!-- role: advice -->

Describe visually apparent features and relationships—such as trends, clusters, patterns, outliers, and significant statistical findings—in text at a minimum, and optionally expose them through additional modalities like sonification.

## The Logic <!-- role: reason -->

- **The Principle:** Visual relationships must not be exclusive to vision; they should be expressed in a form that preserves structure and meaning beyond the visual channel.
- **The Evidence:** Chartability frames this as an Assistive, labor-reducing requirement because it lowers the cognitive and functional effort needed to access “visually apparent” semantics when they are otherwise unavailable or tedious to extract non-visually [@elavskyHowAccessibleMy2022]. WCAG’s “Info and Relationships” emphasizes that relationships conveyed visually should also be available in a way that can be determined from the content structure (not just appearance) [@w3c_understanding_info]. Highcharts documents a sonification approach as an optional multi-sensory method to convey chart structure and patterns through audio controls [@highcharts_highcharts_accessibility].

## Where to Apply <!-- role: context -->

- **User Goal:** Detecting and understanding higher-level insights that are obvious visually (e.g., “there is an upward trend,” “there is an outlier cluster,” “two groups separate”).
- **Data Type:** Any dataset where meaningful interpretation depends on relationships among marks (e.g., time series trends, scatterplot clusters/outliers, ranked patterns).
- **Audience:** People who may not access or interpret the visual layer reliably, including users of assistive technologies and users who benefit from reduced interpretive labor [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization does not present any visually apparent higher-level features (e.g., a purely decorative graphic or a chart whose intent is only to show raw values without interpretive claims).
- **Reason:** If there are no claimed or salient visual relationships to communicate, there may be nothing meaningful to summarize beyond basic data access.

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional authoring effort to write and maintain textual descriptions of insights and to keep them aligned with updates to the data or chart.
- **The Risk:** Overstating, mischaracterizing, or selectively describing relationships can mislead users if the text does not accurately match what the visualization shows [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Providing only a generic label (e.g., “This chart shows sales over time”) without describing the actual relationships (trend direction, turning points, outliers).
- **Why it fails:** It does not convey the visually apparent semantics (patterns/outliers/relationships) that the chart communicates by sight [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Relying on a 1:1 alternative modality (e.g., only mapping each point to a tone) without describing higher-level relationships.
- **Why it fails:** The notes in Chartability highlight that semantic tools for communicating relationships (like trends or comparisons) are limited, and 1:1 mappings can leave users doing the same (or more) interpretive labor [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart’s main takeaway is “obvious by looking,” but the surrounding text does not mention it (no trend/outlier/cluster/pattern summary).
- **The Test:** Identify one or two visually apparent findings (e.g., the dominant trend or a clear outlier). If you cannot find those findings stated in text near the chart, the rule is broken [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a short textual description that explicitly states the key visually apparent relationships (e.g., the main trend and any major outliers) [@elavskyHowAccessibleMy2022].
- **Best Fix:** Provide a structured text summary that communicates the important relationships and, when appropriate, add an optional multi-sensory representation such as sonification following an established approach (e.g., a controllable sonification module) [@highcharts_highcharts_accessibility] while maintaining relationship clarity consistent with accessibility principles for information and relationships [@w3c_understanding_info].
