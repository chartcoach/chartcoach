---
id: avoid-encoding-nominal-categories-with-area
title: Avoid Encoding Nominal Categories with Area
bibliography: references.bib
description: Do not use area as the primary encoding for nominal categories because
  it is low-ranked for nominal effectiveness.
labels:
- task:identify
- visual:area
- impact:clarity
- data:nominal
- audience:general
- complexity:foundational
---

## The Rule <!-- role: advice -->

Do not use area as the primary channel to encode nominal categories when other options (position, color hue, texture, saturation, shape) are available.

## The Logic <!-- role: reason -->

In the theoretical effectiveness ordering for nominal data, area is ranked lowest among the listed channels. This ordering is from [@mackinlayAutomatingDesignGraphical1986a] and is captured as structured guidance for recommendation systems in [@zengReviewCollationGraphical2023].

- **The Principle:** Effectiveness ordering for nominal perceptual tasks
- **The Evidence:** [@mackinlayAutomatingDesignGraphical1986a], collated in [@zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Identifying category membership without confusion
- **Data Type:** Nominal categories
- **Audience:** General audiences

## When to Break It <!-- role: exceptions -->

- **Scenario:** Area is the only available differentiator because position and all retinal channels are already committed.
- **Reason:** The guideline is about preference in channel choice, not absolute feasibility.

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to redesign the chart to free up hue/position/shape for categories.
- **The Risk:** Reassigning encodings can reduce the number of simultaneous variables you can show.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using different bubble sizes to represent different categories.
- **Why it fails:** Size/area differences can be misread as magnitude or order rather than pure identity and are low-ranked for nominal effectiveness here.

## How to Check <!-- role: check -->

- **Visual Sign:** Categories are distinguishable mainly by “bigger vs smaller” marks.
- **The Test:** Remove labels/legend; if the viewer would likely interpret larger marks as “more” of something, the encoding is risky for nominal categories.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap the nominal field from area to color hue (or to position-based separation).
- **Best Fix:** Reserve area for quantitative magnitude (if needed) and encode categories with position or hue as primary channels.
