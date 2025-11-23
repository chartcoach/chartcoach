---
id: encode-multiple-facets-simultaneously
title: Encode Multiple Data Facets Simultaneously
bibliography: references.bib
description: Combine multiple data attributes into a single visual space to support
  complex sensemaking rather than relying on isolated simple charts.
labels:
- chart:multivariate
- task:sensemaking
- visual:density
- impact:insight
- data:big-data
- audience:expert
- complexity:high
---

## The Rule <!-- role: advice -->
Design visualizations that encode multiple facets and layers of data within the same visual space, rather than relying on separate simple charts (like bar or pie charts) or temporal animation.

## The Logic <!-- role: reason -->
Simple charts typically represent only one or two facets of data (e.g., attributes or relationships), which is insufficient for big data tasks where relationships are often non-explicit or unknown. According to [@ola_beyond_2016], users need to explore various data elements simultaneously to "quickly perceive patterns, develop insights, and create and discard hypotheses." Segregating data into isolated views or using animation forces the user to rely on short-term memory to synthesize information, which can lead to cognitive overload and inaccurate understanding.

## Where to Apply <!-- role: context -->
*   **User Goal:** Complex sensemaking tasks such as predicting outbreaks, discovering at-risk populations, or analyzing causation where variables are inter-related.
*   **Data Type:** Big health data characterized by high volume, variety, and velocity (e.g., 12 million records, 57 risk factors, 187 countries).
*   **Audience:** Professionals engaged in analytical tasks rather than simple narrative consumption.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Simple perceptual tasks.
*   **Reason:** If the user only needs to compare two explicit values (e.g., "Which disease has a higher mortality rate?"), a simple bar chart is more effective than a complex multi-faceted visualization [@ola_beyond_2016].
*   **Scenario:** Narrative presentations.
*   **Reason:** When telling a specific story to a lay audience, step-by-step animation (like Gapminder) may be preferable to a dense analytical display.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Immediate familiarity. Users accustomed to Microsoft Office-style charts may initially find dense visualizations "non-trivial" or difficult to interpret.
*   **The Risk:** Visual clutter. Without a systematic design approach (like a pattern language), encoding many facets can result in unintelligible "bad design" [@ola_beyond_2016].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using animation to show changes over time or across categories.
*   **Why it fails:** As one representation replaces another, users must recall previous states, overloading short-term memory and potentially causing inaccurate understanding of trends [@ola_beyond_2016].
*   **The Wrong Fix:** Distributed dashboards.
*   **Why it fails:** Spreading simple charts across a dashboard forces users to "mentally combine representations," which negatively impacts the internal mental process of sensemaking [@ola_beyond_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the user have to look at three different charts to answer a single "Why?" question?
*   **The Test:** Check if the visualization displays relationships (links), groupings (clusters), and attributes (values) in a single integrated view.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Overlay additional data dimensions onto existing charts using visual marks (e.g., size, color, texture) rather than creating new charts.
*   **Best Fix:** Use a framework-based approach (such as Sedig and Parsons' pattern language) to blend patterns—for example, combining `[Token•Link•Area•Group]` to show location, spread, and category in one unified structure [@ola_beyond_2016].
