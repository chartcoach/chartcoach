---
id: assign-distinct-hues-primary-candidates
title: Assign Distinct Hues to Intra-Party Candidates
bibliography: references.bib
description: Use a varied 'confetti' palette of distinct hues to separate candidates
  within the same party primary.
labels:
- visual:color
- task:distinguish
- data:categorical
- domain:politics
- chart:map
---

## The Rule <!-- role: advice -->
When visualizing primary elections or contests involving multiple candidates from a single party, abandon the single party color. Instead, assign distinct, varied hues (a "confetti box" approach) to each candidate to ensure they can be distinguished.

## The Logic <!-- role: reason -->
In a general election, "Red" might equal "Republicans." However, in a primary, every candidate is a Republican. Using shades of red for all candidates creates a chart that is impossible to read. You must break the party-color rule and use a full spectrum of colors (greens, blues, purples, yellows) to separate the individuals, as seen in visualizations by *The New York Times* or *Bloomberg* for the 2016 primaries [@muth_partycolors_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** distinguishing between multiple individuals belonging to the same group.
*   **Data Type:** Primary election results or single-party demographic maps.
*   **Audience:** Readers looking for winner-take-all details in specific regions.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Visualizing the party as a unified whole against others.
*   **Reason:** If the chart is about the party's total turnout vs. another party, revert to the single party color.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Ideological semantic association.
*   **The Risk:** A Republican candidate might be represented by "Blue" (traditionally Democratic) or "Green" (traditionally Environmentalist) in the primary context, which creates temporary cognitive dissonance.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using 10 different shades of the main party color (e.g., 10 shades of Blue for Democrats).
*   **Why it fails:** The human eye cannot reliably distinguish between that many shades of a single hue, especially on a complex map [@muth_partycolors_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** The map or chart looks monochromatic, and users have to constantly refer to the legend to see which shade belongs to whom.
*   **The Test:** Can you name the candidate winning a specific county without looking at the legend? If not, the contrast is too low.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Vary the lightness significantly (light blue vs dark blue).
*   **Best Fix:** Assign completely different hues to top candidates (Purple vs. Orange vs. Teal) to maximize contrast.
