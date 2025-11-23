---
id: match-saturation-to-significance
title: Match Color Saturation to Political Significance
bibliography: references.bib
description: Increase the saturation and darkness of a party's color as their electoral
  success and importance grows.
labels:
- visual:color
- visual:hierarchy
- impact:emphasis
- data:temporal
- domain:politics
---

## The Rule <!-- role: advice -->
Adjust the saturation and lightness of a party's assigned color based on their importance in the current political landscape. Use desaturated, lighter colors for minor or new parties, and transition to fully saturated, darker hues if they gain significant vote share or parliamentary seats.

## The Logic <!-- role: reason -->
Color is an excellent tool to make elements stick out visually. A desaturated color suggests lower importance or a peripheral status. As a party becomes a major topic in the media or enters parliament, keeping a faint color feels inappropriate. For example, German media shifted the AfD party from a light, desaturated blue to a bold, dark blue as their vote share grew from 4.7% to 12.6%, reflecting that they had "fully arrived on the political landscape" [@muth_partycolors_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** accurately representing the visual weight of political actors over time.
*   **Data Type:** Election results comparing historical performance to current results.
*   **Audience:** General news readers tracking political shifts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Strict neutral reporting of candidate lists.
*   **Reason:** If the goal is to show a ballot list without implying hierarchy or influence, all colors should have equal visual weight to avoid bias.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Consistency over time.
*   **The Risk:** Changing a color (even just its saturation) between election cycles might confuse readers who remember the old palette.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Keeping a major disruptor party in a pastel or washed-out color.
*   **Why it fails:** It visually minimizes a group that has actually gained significant influence, potentially misleading the reader about the election's outcome [@muth_partycolors_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** A party with a double-digit vote share looks visually "weaker" or "fainter" than a party with a similar or smaller share.
*   **The Test:** Convert the chart to grayscale. Does the party with significant influence disappear or fade into the background?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the saturation (vibrancy) of the existing hue.
*   **Best Fix:** Select a darker, bolder shade of the same hue to give the party equal visual weight to established major parties.
