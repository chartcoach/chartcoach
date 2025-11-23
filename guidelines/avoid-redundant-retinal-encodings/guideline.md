---
id: avoid-redundant-retinal-encodings
title: Avoid Multiple Retinal Encodings
bibliography: references.bib
description: Do not use multiple retinal channels (color, shape, size) simultaneously
  unless strictly necessary, to prevent cognitive overload.
labels:
- visual:color
- visual:shape
- visual:size
- impact:cognitive-load
- impact:clarity
---

## The Rule <!-- role: advice -->
Avoid using multiple retinal encodings (e.g., mapping data to both color AND shape, or color AND size) within the same chart, especially during automated chart generation.

## The Logic <!-- role: reason -->
Using too many visual channels simultaneously increases cognitive load and makes the chart harder to interpret.
*   **The Principle:** Interference and Over-encoding.
*   **The Evidence:** The ranking algorithm in Voyager explicitly "penalizes encodings that use multiple retinal encodings" because "over-encoding can impede interpretation." It also considers the interactions among visual variables (perceptual separability) to avoid ineffective charts [@wongsuphasawat_voyager_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapid scanning and interpretation of data patterns.
*   **Chart Type:** Scatter plots and other multidimensional views.
*   **System:** Automated visualization recommenders.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Redundant coding for accessibility.
*   **Reason:** Mapping the *same* variable to both Color and Shape can help users with color vision deficiencies. (Note: The rule specifically warns against mapping *different* variables to these channels or arbitrarily combining them for the sake of showing more dimensions).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Data density. You display fewer dimensions of data in a single static view.
*   **The Risk:** Users may need to view two separate charts to understand the relationship between variable A, B, and C, rather than one complex chart.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Creating a "confetti" scatter plot where X=Price, Y=Sales, Color=Region, Shape=Product, Size=Profit.
*   **Why it fails:** It becomes nearly impossible to isolate the effect of a single variable visually.

## How to Check <!-- role: check -->
*   **Visual Sign:** The chart looks cluttered and requires frequent reference to multiple different legends to understand a single data point.
*   **The Test:** List the retinal channels used: Color, Shape, Size. If the count is > 1, verify if the additional complexity is strictly required for the task.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove the least important variable from the visual encoding.
*   **Best Fix:** Use small multiples (faceting). Instead of mapping the third variable to Shape, split the chart into separate panels (rows/columns) based on that variable.
