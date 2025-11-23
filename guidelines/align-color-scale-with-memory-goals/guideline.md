---
id: align-color-scale-with-memory-goals
title: Match Color Scale to Memory Goals
bibliography: references.bib
description: Choose rainbow scales for hue recall and sequential scales for value
  recall.
labels:
- chart:map
- visual:color
- task:recall
- impact:memorability
- data:quantitative
---

## The Rule <!-- role: advice -->
Select your color scale based on what the user needs to remember: use rainbow scales if they must recall *which color* was present (hue recall), and sequential scales if they must recall *what magnitude* was present (value recall).

## The Logic <!-- role: reason -->
Research by Gołębiowska and Çöltekin indicates a trade-off in memorability. Rainbow colors facilitate better recall of hues (users remember seeing "red" or "green" regions) likely because nameable colors are easier to encode in memory [@golbiowska_rainbow_2022]. However, sequential scales lead to significantly better recall of the actual *values* represented, as summarized in the review by Zeng et al. [@zeng_review_2023].

*   **The Principle:** Nameable Colors vs. Magnitude Association
*   **The Evidence:** [@golbiowska_rainbow_2022], [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Recall tasks. (e.g., presenting a slide and asking the audience to remember key areas later).
*   **Data Type:** Spatial data on maps.
*   **Audience:** Presentations or educational settings where short-term memory of the visual is required.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Accuracy is paramount over memory.
*   **Reason:** Even if a user remembers "Red" better, if they cannot intuitively map "Red" to "High Value," the memory is not useful for quantitative reasoning.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Optimizing for hue recall (Rainbow) sacrifices intuitive ordering. Optimizing for value recall (Sequential) sacrifices distinct hue memorability.
*   **The Risk:** Using rainbow colors for memory might lead users to remember the *wrong* information (the color) without the context of what that color means (the value).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assuming that because a map is "memorable" (colorful), it is also "informative."
*   **Why it fails:** Users may remember the visual pattern of colors but fail to recall the quantitative data those colors represented [@golbiowska_rainbow_2022].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using named colors (Red, Green, Blue) or shades (Light, Medium, Dark)?
*   **The Test:** Show the chart for 15 seconds, hide it, and ask the user to sketch the high-value areas.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If value recall is the priority, switch to a sequential scale.
*   **Best Fix:** Determine if the data is truly quantitative (use sequential) or categorical (use qualitative/rainbow hues) and style accordingly.
