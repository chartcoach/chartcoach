---
id: leverage-text-and-faces
title: Leverage Text and Faces to Capture Attention
bibliography: references.bib
description: Use text and human faces as strong attractors of attention, as they often
  override low-level visual features like color or contrast.
labels:
- visual:semantics
- impact:hierarchy
- audience:general
- content:text
- content:imagery
---

## The Rule <!-- role: advice -->
Use text labels and human faces (specifically gaze direction) to direct viewer attention, rather than relying solely on color, intensity, or orientation.

## The Logic <!-- role: reason -->
Visual attention is driven by both bottom-up factors (contrast, color) and top-down cognitive factors. @borji_quantitative_2013 highlights that standard saliency models fail because they miss "cognitive factors" such as the presence of text or human faces. These recognized concepts drive visual attention significantly, with text messages and the gaze direction of characters acting as powerful cues that exist independently of low-level visual saliency.

*   **The Principle:** Top-Down Attention Control (Cognitive Factors)
*   **The Evidence:** @borji_quantitative_2013

## Where to Apply <!-- role: context -->
*   **User Goal:** Directing the user to specific insights or explanations.
*   **Data Type:** Infographics, annotated charts, or dashboards containing mixed media.
*   **Audience:** Users looking for narrative or explanation within the data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Preattentive processing tasks (e.g., "find the red dot").
*   **Reason:** If the goal is rapid detection of a statistical outlier based on a simple feature (like color pop-out), adding text or faces will distract from the pure search task and increase cognitive load.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Speed of processing. "Reading" text or interpreting a face is slower than spotting a bright color.
*   **The Risk:** Text can clutter the visualization and distract from the data patterns if used excessively.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Increasing the color saturation or border thickness to make an element "pop" when it contains no semantic meaning.
*   **Why it fails:** @borji_quantitative_2013 suggests that "meaning" (semantics) is a stronger driver than simple visual contrast in complex scenes.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you relying entirely on heatmaps or color coding to guide the eye without explanatory labels?
*   **The Test:** If you remove the color, does the viewer still know where to look? (If no, you lack semantic anchors like text).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a direct text annotation to the most interesting data point.
*   **Best Fix:** Integrate the narrative elements (text/icons) into the visual flow so they guide the eye sequentially through the data.
