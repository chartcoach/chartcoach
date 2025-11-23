---
id: remove-redundant-map-labels
title: Remove Redundant Geographic Labels
bibliography: references.bib
description: Reduce map clutter by removing base labels (like cities) when custom
  annotations provide sufficient context.
labels:
- chart:map
- task:clean
- visual:text
- impact:clarity
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->
Remove standard base layer labels (such as city or state names) if your custom annotations already mention specific locations.

## The Logic <!-- role: reason -->
Extra text competes for the viewer's attention. According to Rose Mintzer-Sweeney, "extra text steals attention from your annotations" [@mintzer_map_annotations_2024]. If your narrative annotations already mention specific states or regions, they serve a dual purpose: telling the data story and helping the reader get oriented, making the standard labels unnecessary noise.

## Where to Apply <!-- role: context -->
*   **User Goal:** Telling a specific story about regional data patterns.
*   **Data Type:** High-density geographic maps (e.g., point maps of power plants).
*   **Audience:** Readers who need narrative guidance rather than a reference atlas.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The annotations discuss data behavior but do not mention location names.
*   **Reason:** The reader will lose their geographical bearing without reference points.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "atlas" utility of the map; users cannot look up specific cities irrelevant to the story.
*   **The Risk:** If annotations are sparse, users unfamiliar with the geography may feel lost.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Keeping all base labels and making annotations larger to compete.
*   **Why it fails:** This creates a "cluttered" appearance where the actual data points are overshadowed by text [@mintzer_map_annotations_2024].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the map look "busy" or "messy" even before adding data points?
*   **The Test:** Read your annotations. If you deleted all city labels, would the annotation text still tell you roughly where you are looking?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Turn off the "city labels" layer in your mapping tool.
*   **Best Fix:** Audit the map elements and explicitly "delete its least important elements" to prioritize the data narrative [@mintzer_map_annotations_2024].
