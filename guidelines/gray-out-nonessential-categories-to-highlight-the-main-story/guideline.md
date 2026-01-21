---
id: gray-out-nonessential-categories-to-highlight-the-main-story
title: Gray Out Nonessential Categories to Make Highlights Pop
bibliography: references.bib
description: Use gray for background categories so a small set of colored marks becomes
  the immediate focal point.
labels:
- chart:general
- task:highlight
- visual:color
- impact:focus
- data:categorical
- audience:general
- complexity:beginner
- source:datawrapper
---

## The Rule <!-- role: advice -->

Make the majority of nonessential categories gray, and use one (or a few) saturated colors only for the categories/values you want readers to notice first.

## The Logic <!-- role: reason -->

Gray acts as a deliberate “background” treatment: against gray marks, saturated colored marks gain contrast and become the first thing readers see, even if they occupy less space. This establishes a strong figure–ground separation that supports storytelling.

- **The Principle:** Figure–ground separation via reduced chroma/contrast
- **The Evidence:** [@muth_emphasize_color_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Notice the key category/range/value immediately while keeping the rest as context.
- **Data Type:** Many-category charts (lines, bars, scatter points, tables) where only a few series/items matter most to the message.
- **Audience:** Readers who will scan quickly and need guidance on what matters. [@muth_emphasize_color_2023]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Readers must compare many categories equally and without direct labels.\
  **Reason:** Graying out most series removes the ability to differentiate them and can hinder comparison. [@muth_emphasize_color_2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced legibility and prominence for the gray categories (often fewer labels or less emphasis).
- **The Risk:** If the “gray” items are still important for interpretation, readers may ignore them too much and misunderstand context. [@muth_emphasize_color_2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Highlighting too many items with saturated colors.\
  **Why it fails:** If everything is emphasized, nothing is; attention fragments and the main takeaway gets lost. [@muth_emphasize_color_2023]
- **The Wrong Fix:** Using gray for a category that is equally important as the colored ones.\
  **Why it fails:** Gray is widely interpreted as “less important,” so it unintentionally demotes that category. [@muth_emphasize_color_2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers’ attention doesn’t land on your intended highlight first, or multiple colored items compete.
- **The Test:** Convert the design mentally into “colored vs gray”: if more than a small set remains colored, you likely diluted the highlight. [@muth_emphasize_color_2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Recolor all categories to a single gray, then add color back only to the few categories that carry your message. [@muth_emphasize_color_2023]
- **Best Fix:** Combine gray-out with selective labeling: label only the colored highlights (and optionally a few essential gray reference items) so the hierarchy is both visual and textual. [@muth_emphasize_color_2023]
