---
id: problem-specific-filtering
title: Filter Data to be Problem-Specific
bibliography: references.bib
description: Combat data overwhelm by filtering information to the specific topic
  or problem at hand.
labels:
- task:filter
- impact:focus
- data:high-volume
- visual:layout
---

## The Rule <!-- role: advice -->
Present information strictly in a topic-related, problem-specific way. Do not provide open access to heterogeneous data sources without pre-structuring or filtering the view.

## The Logic <!-- role: reason -->
Data in policy modeling (opinions, open data, statistics) is usually "complex and overwhelming because too much data is available."
*   **The Principle:** Relevance Filtering.
*   **The Evidence:** [@kohlhammer_toward_2012] states that "The key is to provide information in a topic-related, problem-specific way that lets policy makers better understand the problem and alternative solutions."

## Where to Apply <!-- role: context -->
*   **User Goal:** Information foraging (finding relevant facts) or policy definition.
*   **Data Type:** Heterogeneous sources (e.g., mixed text, stats, and logs).
*   **Audience:** Policy makers or analysts facing "ubiquitous computing" and "big data."

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Open-ended exploratory data analysis (EDA) by data scientists.
*   **Reason:** If the goal is to find completely unknown unknowns across unconnected datasets, strict pre-filtering might hide serendipitous connections.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The user cannot see the "full picture" of all available data simultaneously.
*   **The Risk:** If the "topic" definitions are too narrow, relevant context from adjacent topics might be excluded.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** A "mega-dashboard" that includes every available metric on a single screen.
*   **Why it fails:** It ignores the limitations of human attention and the complexity of the underlying data.

## How to Check <!-- role: check -->
*   **Visual Sign:** The screen is crowded with widgets unrelated to the immediate user query.
*   **The Test:** If the user is investigating "energy policy," does the interface still show data regarding "judicial decisions" unless explicitly linked?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use tabs or search-based navigation to hide unrelated data categories.
*   **Best Fix:** Use semantic technologies to dynamically generate views that only include entities dependent on or related to the current focus topic (as suggested in the Fupol and ePolicy descriptions in [@kohlhammer_toward_2012]).
