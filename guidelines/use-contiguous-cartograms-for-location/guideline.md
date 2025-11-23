---
id: use-contiguous-cartograms-for-location
title: Use Contiguous Cartograms for Location Recognition
bibliography: references.bib
description: Contiguous cartograms offer the best performance for locating and recognizing
  specific regions.
labels:
- chart:cartogram
- chart:contiguous-cartogram
- task:locate
- task:filter
- visual:shape
- impact:recognition
---

## The Rule <!-- role: advice -->
Prioritize contiguous (deformed) cartograms when users need to locate specific regions or filter data by location.

## The Logic <!-- role: reason -->
Contiguous cartograms distort the map to size regions by value but attempt to maintain the original shape and relative position as much as possible. This familiarity aids in recognition.
*   **The Principle:** Shape Constancy and Relative Position.
*   **The Evidence:** Experimental results in [@zeng_review_2023], derived from [@nusrat_evaluating_2018], rank contiguous cartograms (E-1) as the most accurate design for `filter` (locate/recognize) tasks, outperforming rectangular and Dorling variants.

## Where to Apply <!-- role: context -->
*   **User Goal:** Finding a specific state or country on the map.
*   **Data Type:** Global or national datasets where users rely on mental maps for navigation.
*   **Audience:** General users who rely on geographic familiarity.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The statistical values are highly disproportionate (e.g., one tiny region has a massive value).
*   **Reason:** Extreme distortion can make the contiguous map unrecognizable. In these cases, a Dorling cartogram (circles) might be necessary to accommodate the data range.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Simplicity. The shapes can be complex and irregular compared to the clean lines of rectangular or circular maps.
*   **The Risk:** "Ghost" shapes where extreme distortion makes a region look like a blob, reducing recognition.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using rectangular cartograms to make the map look "cleaner."
*   **Why it fails:** Rectangular abstraction removes the shape cues users rely on to identify regions, significantly increasing error rates in location tasks [@nusrat_evaluating_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you identify a region solely by its outline?
*   **The Test:** Remove the labels. Can a user still point to "Germany" or "Texas"?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add clear labels if the distortion is too high.
*   **Best Fix:** Switch to a contiguous algorithm (like Gastner-Newman) that balances shape preservation with statistical accuracy.
