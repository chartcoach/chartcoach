---
id: avoid-stacked-bars-near-parity
title: Avoid Stacked Bars for Values Near 50 Percent
bibliography: references.bib
description: Use stand-alone bars instead of stacked bars for values near 50% to prevent
  category repulsion bias.
labels:
- chart:stacked-bar
- chart:bar
- task:compare
- visual:position
- impact:accuracy
- data:proportion
---

## The Rule <!-- role: advice -->
Do not use stacked bar graphs or visual contexts that emphasize the full 0-100% range when the values being displayed are close to 50%. Instead, use stand-alone bars without a framing context.

## The Logic <!-- role: reason -->
When a value is integrated into a context (like a stacked bar), viewers unconsciously categorize it relative to implicit landmarks, such as the halfway point.
*   **The Principle:** Category Repulsion. Values near the middle (50%) are visually "repulsed" away from that boundary. Values just below 50% are underestimated, and values just above 50% are overestimated [@mccoleman_no_2021].
*   **The Evidence:** Experiments showed that while stacked bars generally reduce absolute error, they introduce systematic signed error. Specifically, values between 25-49% were underestimated and values between 51-75% were overestimated due to repulsion from the implicit 50% mark [@mccoleman_no_2021].

## Where to Apply <!-- role: context -->
This advice is critical when the data sits near the middle of the range.
*   **User Goal:** When unbiased perception of magnitude is critical (e.g., accurately seeing that a value is 48%, not 40%).
*   **Data Type:** Proportions or percentages, specifically those falling in the 25%–75% range.
*   **Audience:** General audiences who rely on visual estimation rather than reading exact labels.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the data values are very small (e.g., 5%) or very large (e.g., 95%).
*   **Reason:** In these cases, the endpoint (100% mark) acts as a useful anchor that improves precision, making stacked bars superior to stand-alone bars [@mccoleman_no_2021].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the explicit part-to-whole relationship that a stacked bar conveys immediately.
*   **The Risk:** Viewers might lose track of the total capacity or the fact that the values are complementary percentages.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a stacked bar to compare close election results (e.g., 48% vs 52%).
*   **Why it fails:** The repulsion bias will exaggerate the difference, making the 52% look significantly larger and the 48% significantly smaller than they really are [@mccoleman_no_2021].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are your bars touching the top axis or stacked to fill a container? Are the values visually close to the middle?
*   **The Test:** Check if the data range includes values between 40% and 60%. If so, the container creates a "repulsion" zone.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Break the stack. Place the bars side-by-side on a common baseline.
*   **Best Fix:** Use a standard bar chart where the bars do not physically touch a "ceiling" or 100% line, removing the "container" cue.
