---
id: place-labels-proximally
title: Place Explanations Directly Next to Data Elements
bibliography: references.bib
description: Reduce cognitive load by placing labels and explanations immediately
  adjacent to the visual elements they describe rather than using legends.
labels:
- chart:line
- visual:position
- visual:text
- impact:clarity
- task:identify
- audience:general
---

## The Rule <!-- role: advice -->
Eliminate separate legends or color keys located in the corners of your visualization. Instead, bring elements and their explanations as close together as possible, placing labels directly on or next to the lines or bars they identify. Use the same color for the label as the element itself.

## The Logic <!-- role: reason -->
Separating data from its explanation forces the reader's eyes to flicker back and forth between the visual element and the key (e.g., "Wait, what did red represent?").
*   **The Principle:** Reduction of Eye-Travel
*   **The Evidence:** As noted in [@muth_readers_time_2017], separating these elements causes unnecessary "eye-travel long distances." Direct labeling creates a sense of orientation where the reader understands what each element represents immediately without "searching for grip and clarity."

## Where to Apply <!-- role: context -->
This advice applies to most charts with multiple categories, particularly static visualizations where interaction (hovering) is not the primary mode of consumption.
*   **User Goal:** Rapid understanding of categorical data.
*   **Data Type:** Multiline charts, bar charts with multiple categories.
*   **Audience:** General readers who need to feel "oriented" quickly.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-density interactive environments or small mobile screens where space is nonexistent.
*   **Reason:** As mentioned in the post-script regarding the 2017 NYT update, annotations and direct labels sometimes disappear in mobile-first or responsive designs due to space pressures [@muth_readers_time_2017].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Cleanliness and white space.
*   **The Risk:** The chart may look more cluttered than one with a hidden legend. It requires manual placement effort (e.g., turning off auto-legends and placing text by hand).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a separate color key in the corner.
*   **Why it fails:** It forces the reader to look back and forth to decode the chart, wasting their time.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do you have a box in the corner listing colors and names?
*   **The Test:** Track your eye movement. If you have to look away from the data curve to find out what it is, the label is too far away.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Move the legend closer to the data.
*   **Best Fix:** Remove the legend entirely. Place a text label at the end (or peak) of the line or bar, colored to match the data element.
