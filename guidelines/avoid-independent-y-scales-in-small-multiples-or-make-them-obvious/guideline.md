---
id: avoid-independent-y-scales-in-small-multiples-or-make-them-obvious
title: Avoid independent y-axis scales in small multiples, or make the different scales
  unmistakable
bibliography: references.bib
description: Because readers may assume shared axes, either keep a common scale or
  clearly signal when scales differ.
labels:
- chart:line
- task:interpret
- visual:scale
- impact:trust
- data:temporal
- audience:novice
- complexity:advanced
---

## Avoid independent y-axis scales in small multiples, or make the different scales unmistakable <!-- role: advice -->

Avoid using different y-axis scales across small-multiple panels when possible. If you use independent y-axes, explicitly signal that scales differ so readers do not assume a shared scale.

## Hidden scale changes create false comparisons <!-- role: reason -->

Readers often generalize design rules across panels and may assume consistent axes in a grid of similar charts. If scales differ but look similar, viewers can incorrectly compare heights across panels and derive false insights, undermining both accuracy and trust.

**Mechanism:** Unnoticed scale changes change the meaning of vertical position, causing systematic misinterpretation when viewers compare across panels.

**Evidence:** Independent y-axes in small multiples are useful but dangerous because readers may not check axes and assume a shared scale; it is recommended to avoid them when possible or add clear cues such as explicit notes in the description and unusual-looking gridlines that draw attention to scale differences [@muth_small_multiple_line_charts_2024].

**Notes:** The goal is not to forbid independent scales, but to prevent silent scale drift across panels.

## When your design risks being read as “same axes everywhere” <!-- role: context -->

- **User Goal:** Interpret trends correctly without being misled by scale artifacts.
- **Task:** Compare patterns across panels while avoiding false magnitude comparisons.
- **Data:** Multiple time series where you are considering per-panel scaling.
- **Chart Setting:** Small multiples with similar-looking panels where axis assumptions are likely.
- **Audience:** General readers who may not inspect each axis carefully.
- **Success Criterion:** Readers correctly understand what is comparable and what is not.

## When it’s acceptable to use independent scales without extra signaling <!-- role: exceptions -->

**Break it when:** All panels truly share the same y-axis scale. **Why:** In that case, the concern about unnoticed scale differences does not apply [@muth_small_multiple_line_charts_2024].

## Tradeoffs of making scale differences obvious <!-- role: costs -->

**Sacrifice:** Some elegance and space; additional text or visual cues may be needed. **Risk:** If signaling is subtle, it may still be missed; if signaling is heavy, it may distract from the trends. **Mitigation:** Choose cues that are hard to ignore but do not dominate the display [@muth_small_multiple_line_charts_2024].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using independent y-axes and assuming readers will notice by checking every axis. **Why it fails:** Many readers won’t, leading to false insights [@muth_small_multiple_line_charts_2024].
- **Mistake:** Using independent y-axes while writing conclusions that depend on cross-panel magnitude comparisons. **Why it fails:** The design encourages invalid comparisons [@muth_small_multiple_line_charts_2024].

## Quick tests <!-- role: check -->

**Failure Sign:** Two panels show similarly tall rises, but the underlying numeric changes are very different and nothing in the design flags this. **Quick Check:** Ask “Could a reader compare heights across panels and be wrong?” If yes, the scale difference is not obvious enough. **Stronger Test:** Show the chart briefly and ask what’s comparable across panels; if readers mention absolute magnitude, add stronger signaling or use a shared scale [@muth_small_multiple_line_charts_2024].

## What to do instead <!-- role: fix -->

- Use a shared y-axis scale across all panels when cross-panel magnitude comparison matters.
- Add a clear sentence in the chart description that y-axis scalings differ among panels when independent scales are used.
- Add visual cues that make axes differences noticeable, such as gridlines that do not appear uniform across panels.
- Provide a separate view that uses shared scales if readers also need magnitude comparisons [@muth_small_multiple_line_charts_2024].
