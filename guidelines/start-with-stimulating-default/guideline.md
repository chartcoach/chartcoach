---
id: start-with-stimulating-default
title: Start with a Stimulating Default View
bibliography: references.bib
description: Initialize the visualization with an engaging, pre-populated view rather
  than a blank slate.
labels:
- chart:interactive
- impact:engagement
- task:browse
- visual:state
- audience:general
---

## The Rule <!-- role: advice -->
Never load a visualization in a "blank" or "zeroed out" state. Launch with an interesting, complex, or provocative configuration of data already visible.

## The Logic <!-- role: reason -->
Users need a "hook" or a "hard lead" to engage with the content. A blank search box or empty chart puts the burden of discovery entirely on the user before they care about the data.
*   **The Principle:** The "Hard Lead." In journalism, stories begin with a summary or hook. Visualizations should do the same.
*   **The Evidence:** [@segel_narrative_2010] identify "Stimulating Default Views" as a key interactive design strategy (Section 4.2), serving as "jumping off points for further exploration" and capturing reader attention (Section 5 discussion on engagement).

## Where to Apply <!-- role: context -->
*   **User Goal:** Casual browsing or discovering interesting facts without a specific query in mind.
*   **Data Type:** Large, explorable databases (e.g., "Health Stats for all Countries").
*   **Audience:** Online readers who skim and need a reason to stop.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Search-Specific Tools.
*   **Reason:** If the user is coming to the tool specifically to look up their own house price or local school (Task: Known Item Search), a pre-loaded view of somewhere else might be annoying.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Neutrality. By choosing a default view, you are framing the story and potentially biasing the user's first impression.
*   **The Risk:** Relevance. The stimulating default might not be relevant to that specific user's interests.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** "Select a value to begin."
*   **Why it fails:** It creates a barrier to entry. The user doesn't know what values are available or interesting yet.
*   **The Wrong Fix:** Showing the "average" or "total" view.
*   **Why it fails:** Aggregates are often boring. Specific, dramatic outliers (like "Babe Ruth" in the Steroids example) are more engaging.

## How to Check <!-- role: check -->
*   **Visual Sign:** When the page loads, is the main chart area empty?
*   **The Test:** Does the user have to click or type something to see the first datapoint? If yes, you have failed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Pre-select the first item in your dropdown list so *something* shows up.
*   **Best Fix:** Curate a specific, dramatic case study (e.g., the year with the highest inflation, the outlier country) and load that state by default.
