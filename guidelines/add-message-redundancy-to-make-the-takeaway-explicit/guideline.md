---
id: add-message-redundancy-to-make-the-takeaway-explicit
title: Repeat the Main Message Using Annotations or Explanatory Elements
bibliography: references.bib
description: Message redundancy is associated with higher-quality recall of what a
  visualization means.
labels:
- chart:any
- task:understand
- visual:annotation
- visual:text
- impact:comprehension
- impact:recall
- audience:general
- source:borkin-2016
---

## The Rule <!-- role: advice -->

Add message redundancy: explicitly restate the main conclusion using annotations, labels, explanatory text, or images that reinforce the takeaway.

## The Logic <!-- role: reason -->

Repeating the message provides multiple cues for encoding and later retrieval, increasing the chance that the viewer remembers the intended takeaway rather than just the visual form.

- **The Principle:** Multiple retrieval cues for the same message
- **The Evidence:** Visualizations with message redundancy had higher average description quality than those without (overall 1.99 vs 1.59), and top-quality descriptions were much more likely to come from message-redundant visualizations (57% vs 22% in bottom third) [@borkinMemorabilityVisualizationRecognition2016].

## Where to Apply <!-- role: context -->

- **User Goal:** Remember the chart’s conclusion later (not just recognize it)
- **Data Type:** Any, especially when a single trend is the key point
- **Audience:** Communication-focused venues (news/infographics)

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization is intended as a neutral reference where highlighting a single message could be inappropriate.
- **Reason:** The rule pushes the viewer toward a particular takeaway; the paper evaluates recall quality as remembering “message,” which may not match all intents [@borkinMemorabilityVisualizationRecognition2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional elements increase layout complexity and consume space.
- **The Risk:** Too many cues may crowd the figure; viewers may spend more time reading than inspecting data encodings [@borkinMemorabilityVisualizationRecognition2016].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more text that adds context but doesn’t restate the actual conclusion.
- **Why it fails:** Redundancy only helps if it reinforces the message; otherwise it just adds reading load [@borkinMemorabilityVisualizationRecognition2016].

## How to Check <!-- role: check -->

- **Visual Sign:** The viewer can describe what’s plotted but not what it implies.
- **The Test:** Ask a viewer for a one-sentence takeaway after viewing; if they only list encodings (“it’s a bar chart of X”), message redundancy is missing [@borkinMemorabilityVisualizationRecognition2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add one annotation pointing at the key trend with a short statement.
- **Best Fix:** Combine a message-bearing title with supporting annotations/labels so the conclusion is expressed in more than one way [@borkinMemorabilityVisualizationRecognition2016].
