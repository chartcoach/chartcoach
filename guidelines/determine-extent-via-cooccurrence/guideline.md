---
id: determine-extent-via-cooccurrence
title: Set map extent using semantic co-occurrence
bibliography: references.bib
description: Determine the zoom level of a map by including the primary location and
  other locations that frequently appear with it in similar contexts.
labels:
- chart:map
- visual:zoom
- task:contextualize
- data:geospatial
- impact:relevance
---

## The Rule <!-- role: advice -->
Do not simply zoom to the bounds of the primary location mentioned. Set the map extent to include the primary location *plus* related locations determined by spatial distance, hierarchy, and corpus co-occurrence.

## The Logic <!-- role: reason -->
A map is most useful when it shows the primary location in relation to other relevant entities. NewsViews identifies a "primary location" but determines the view frame by calculating a similarity score with other mentioned locations. This score combines Euclidean distance, hierarchy (e.g., sibling counties), and textual co-occurrence (how often locations are mentioned together in news archives). This ensures the map captures the "critical area" relevant to the story [@gao_newsviews_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding the regional influence or context of a story.
*   **Data Type:** News articles or narratives containing multiple toponyms (place names).
*   **Audience:** Readers who need to see the "stage" on which the story plays out.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The story is hyper-local and strictly about the internal geography of a single city or enclosure.
*   **Reason:** Including distant co-occurring locations might zoom the map out too far, obscuring local details.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may display a larger geographic area than strictly necessary for the single primary subject.
*   **The Risk:** If co-occurrence data is noisy, the map might zoom out to include an irrelevant city just because it was mentioned in a different context.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Zooming exclusively to the bounding box of the single mentioned city or county.
*   **Why it fails:** It removes the neighborly context that allows users to compare the primary location to its surroundings [@gao_newsviews_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** The map is so tight around the subject that the user cannot see neighboring towns or state lines.
*   **The Test:** Check if locations mentioned in the text as comparisons (e.g., "unlike neighboring [Town]") are visible in the default view.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Set a minimum zoom level that ensures context is visible.
*   **Best Fix:** Calculate a weighted similarity score between the main location and other locations mentioned in the text, and expand the bounding box to include high-scoring "sibling" locations.
