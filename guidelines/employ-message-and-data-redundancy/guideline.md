---
id: employ-message-and-data-redundancy
title: Employ Message and Data Redundancy
bibliography: references.bib
description: Repeat the main trends visually and textually to improve understanding
  and recall.
labels:
- visual:text
- visual:labels
- impact:comprehension
- impact:clarity
- chart:all
---

## The Rule <!-- role: advice -->
Encode your data and message in multiple ways: explicitly state trends in text (message redundancy) and label data points directly (data redundancy).

## The Logic <!-- role: reason -->
Redundancy helps people grasp main trends and improves recognition. [@borkin_beyond_2016] distinguishes between *data redundancy* (e.g., labeling bar values while also having an axis) and *message redundancy* (e.g., a caption explaining the trend shown in the line chart). Visualizations containing these redundancies resulted in better-quality text descriptions from users. Redundancy helps "restore messages damaged by noise" and ensures the audience pays attention to the right details.

## Where to Apply <!-- role: context -->
*   **User Goal:** ensuring the takeaway is unambiguous.
*   **Data Type:** Quantitative data where specific values or specific trends are the point of focus.
*   **Audience:** Audiences who need to recall the specific narrative or values later.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-density dashboards with limited space.
*   **Reason:** Excessive labeling on every data point can cause occlusion and clutter in dense displays.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Minimalism and white space.
*   **The Risk:** Creating a "busy" visual appearance if text labeling is not handled with good typography and layout.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Removing axis labels because you added direct labels (or vice versa).
*   **Why it fails:** Redundancy is the goal. Removing one channel to "clean up" the chart removes the reinforcement mechanism that aids memory.
*   **The Wrong Fix:** Relying solely on the visual encoding (e.g., bar height) to convey the value.
*   **Why it fails:** Users may misinterpret visual magnitude; text confirms the precise value.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the conclusion written out in a sentence on the chart? are the key values written as numbers on the chart?
*   **The Test:** If you remove the graphic, can you still read the main trend in the text? If you remove the axis, do you know the specific values of key points?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add data labels to the most important data points (e.g., the max and min).
*   **Best Fix:** Add an annotation or subtitle that explicitly describes the visual trend (e.g., "Revenue doubled in Q4").
