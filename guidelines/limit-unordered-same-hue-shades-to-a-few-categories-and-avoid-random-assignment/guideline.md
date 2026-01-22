---
id: limit-unordered-same-hue-shades-to-a-few-categories-and-avoid-random-assignment
title: Use only a few unordered shades of one hue for categories, and never assign
  them randomly
bibliography: references.bib
description: If you encode categories with shades of one hue, keep the count small
  and avoid arbitrary shade assignments that invite false interpretation.
labels:
- chart:general
- task:categorize
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- complexity:intermediate
---

## Use only a few unordered shades of one hue for categories, and never assign them randomly <!-- role: advice -->

If you use shades of one hue to encode categories, keep it to a small number of clearly distinguishable shades and avoid arbitrary shade assignment. Ensure any darker/lighter choice has a defensible meaning, especially for binary categories.

## Why “same-hue shades as categories” is fragile <!-- role: reason -->

Readers often interpret light-to-dark differences as encoding magnitude, rank, or importance, even when the designer intended “just different categories.” Distinguishing multiple similar shades is also cognitively and perceptually demanding, and it becomes worse when categories are unordered and not directly labeled.

**Mechanism:** Lightness is naturally read as quantitative; when it is used for nominal categories, viewers rationalize meaning and may infer hierarchy, and discrimination drops as shade steps become subtle.

**Evidence:** Using a single-hue scheme can support accessibility and reduce “too colorful” appearance, but it increases the chance that viewers infer unintended meaning from shade differences and becomes hard to read once more than a few shades are used; binary schemes should assign the darker shade to the more significant category when significance exists [@muth_quantitative_vs_qualitative_2021].

**Notes:** The problem is not the hue itself but the combination of unordered categories plus multiple lightness steps without clear rationale.

## When this applies: considering shades for nominal categories <!-- role: context -->

- **User Goal:** Reduce colorfulness and/or improve robustness in grayscale while still separating categories.
- **Task:** Identify categories without implying an order.
- **Data:** Nominal categories, often with small cardinality (two to three).
- **Chart Setting:** Static charts where labels/legends may be skimmed.
- **Audience:** Mixed audiences, including color-vision-impaired readers and quick skimmers.
- **Success Criterion:** Categories remain distinguishable without suggesting a false ranking.

## When not to follow it <!-- role: exceptions -->

- **Break it when:** You need readers to reliably distinguish many categories quickly. **Why:** Multiple shades of one hue are difficult to discriminate and do not scale well [@muth_quantitative_vs_qualitative_2021].
- **Break it when:** The shade differences have no meaningful rationale and the chart is not directly labeled. **Why:** Readers will invent explanations for the shading, reducing trust and accuracy [@muth_quantitative_vs_qualitative_2021].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You lose categorical distinctness compared with a qualitative palette of different hues. **Risk:** Viewers infer importance or higher values from darker shades even when you didn’t intend that mapping. **Mitigation:** Keep the number of shades small and use labeling/separation to reduce reliance on subtle lightness differences [@muth_quantitative_vs_qualitative_2021].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using four or more unordered shades of the same hue to represent categories. **Why it fails:** Readers struggle to tell them apart and may abandon decoding [@muth_quantitative_vs_qualitative_2021].
- **Mistake:** Introducing multiple hues as “extra shades” to avoid running out of one-hue steps. **Why it fails:** It can look like those hues represent different top-level groups rather than more categories of the same kind [@muth_quantitative_vs_qualitative_2021].
- **Mistake:** Making shade assignments arbitrary (for example, random dark/light by category). **Why it fails:** Readers rationalize the lightness as meaningful and infer false structure [@muth_quantitative_vs_qualitative_2021].

## Quick tests <!-- role: check -->

**Failure Sign:** People disagree about which category is “more” or “more important” just from the colors, or they can’t reliably name categories from the legend. **Quick Check:** Convert the palette to grayscale; if two categories collapse to similar gray, they are not separable by lightness. **Stronger Test:** Ask a colleague to explain why one category is darker; if they invent a story you didn’t intend, the scheme is too suggestive [@muth_quantitative_vs_qualitative_2021].

## What to do instead <!-- role: fix -->

- Switch to distinct hues when the primary need is to differentiate categories clearly [@muth_quantitative_vs_qualitative_2021].
- If you keep a one-hue scheme, reduce the number of categories shown or aggregate them into fewer groups [@muth_quantitative_vs_qualitative_2021].
- Use direct labels so category identification does not depend on distinguishing subtle shades [@muth_quantitative_vs_qualitative_2021].
- If you introduce a second hue, make it represent an explicit higher-level grouping rather than “extra shades” [@muth_quantitative_vs_qualitative_2021].
