---
id: state-data-origins-processing
title: State Data Origins and Processing
bibliography: references.bib
description: Build trust by explicitly stating data sources, collection methods, and
  processing steps within the visualization context.
labels:
- impact:credibility
- impact:trust
- data:metadata
- task:interpret
- audience:general
---

## The Rule <!-- role: advice -->

Explicitly label where your data comes from, how it was collected, and how it was processed. If there are gaps or omissions in the data, explain them directly in the text or caption.

## The Logic <!-- role: reason -->

Transparency is the primary mechanism for establishing credibility in data visualization. When viewers understand the provenance of the data, they are more likely to trust the visual representation.

*   **The Principle:** Reputation Transfer and Transparency. Viewers who perceive a data source as reputable transfer that trust to the visualization [@knoll_gulf_2025]. Conversely, ambiguity creates suspicion; viewers interpret unexplained gaps or blank areas as a lack of credibility rather than a lack of data [@koesten_encountering_2025].
*   **The Evidence:** Providing methodological details allows users to generate more accurate interpretations of the message [@koesten_what_2023]. Professional standards, such as those at *Scientific American*, rely on distinguishing between peer-reviewed and raw datasets and crediting all contributors to maintain authority [@gregory_data_2024].

## Where to Apply <!-- role: context -->

This advice applies to any visualization intended to inform, persuade, or document reality.

*   **User Goal:** Evaluating the reliability of information or making decisions based on data.
*   **Data Type:** Any dataset, particularly those with potential gaps, extensive pre-processing, or multiple sources.
*   **Audience:** Both lay audiences (who need reassurance of legitimacy) and expert audiences (who need to verify methods).

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Abstract data art or decorative illustrations.
*   **Reason:** The goal is aesthetic experience rather than information transmission; rigorous citation may clutter the visual flow.
*   **Scenario:** Internal exploratory dashboards for a single user.
*   **Reason:** The user already knows the source and context intimately.

## The Price <!-- role: costs -->

*   **The Sacrifice:** Visual space and simplicity. Adding captions, footnotes, and annotations increases the text-to-ink ratio and reduces the space available for the chart itself.
*   **The Risk:** "Fine print fatigue." If the methodological notes are too dense or technical, viewers may ignore them entirely.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Writing "Source: Various" or "Source: Internet."
*   **Why it fails:** It provides no path for verification and suggests laziness.
*   **The Wrong Fix:** Leaving missing data points blank without annotation.
*   **Why it fails:** Viewers often mistake missing data for zero values or visualization errors.

## How to Check <!-- role: check -->

*   **Visual Sign:** Look for the footer or caption. Is it empty? Look for gaps in the chart (e.g., empty regions on a map). Are they labeled?
*   **The Test:** Ask a viewer, "Where did these numbers come from?" and "Why is this spot empty?" If they have to guess, the context is insufficient.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Add a footer text line stating the specific dataset name and year (e.g., "Source: World Bank Open Data, 2023").
*   **Best Fix:** Include a dedicated caption or sidebar that details the data source, credits contributors, and briefly explains processing steps (e.g., "Data excludes incomplete records from Q3"). Explicitly annotate missing data areas (e.g., "No data available for this region").
