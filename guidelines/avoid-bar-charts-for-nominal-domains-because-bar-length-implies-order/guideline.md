---
id: avoid-bar-charts-for-nominal-domains-because-bar-length-implies-order
title: Avoid bar charts for nominal domains because bar length implies ordering
bibliography: references.bib
description: Do not encode nominal categories with bar lengths when no meaningful
  order or magnitude exists for those categories.
labels:
- chart:bar
- task:categorize
- visual:length
- impact:accuracy
- data:categorical
- audience:general
- concept:unintended-encoding
---

## Bar length should not encode nominal categories <!-- role: advice -->

Avoid using bar charts when the encoded domain is nominal (unordered), because bar length communicates ordered or quantitative meaning.

## Why bars add unintended facts for nominal data <!-- role: reason -->

Bar charts carry a strong convention that longer bars mean “more,” creating an ordering relationship among encoded values. If the underlying domain is nominal, that ordering is an extra fact introduced by the graphic rather than by the data.

**Mechanism:** Length comparisons are a salient perceptual task; viewers interpret differences in bar extent as meaningful magnitude or rank, even if the data provides no such structure.

**Evidence:** A bar chart applied to a nominal attribute (such as country of origin) encodes additional incorrect ordering facts via bar-length comparisons, violating expressiveness (“only the facts”) [@mackinlayAutomatingDesignGraphical1986b]. A plot-chart alternative avoids this unintended ordering by not using length as an encoding for the nominal domain [@mackinlayAutomatingDesignGraphical1986b].

**Notes:** This is an expressiveness failure first (wrong meaning), not merely an effectiveness issue.

## When this applies <!-- role: context -->

- **User Goal:** Show category membership for a nominal attribute.
- **Task:** Identify which items belong to which category without implying rank.
- **Data:** Nominal domain (unordered set) such as labels, names, or categories without magnitude.
- **Chart Setting:** Static view where bar length would be visually compared across categories.
- **Audience:** General readers relying on conventional chart semantics.
- **Success Criterion:** The chart does not imply that categories have greater/lesser values.

## When to break it <!-- role: exceptions -->

**Break it when:** The categories actually have an ordered or quantitative meaning that you want the reader to compare by magnitude. **Why:** In that case, the ordering implied by bar length matches real facts in the data [@mackinlayAutomatingDesignGraphical1986b].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** You may lose an immediately familiar chart form that many audiences recognize. **Risk:** Alternative encodings can reduce immediate “at-a-glance” magnitude comparison because magnitude is not meaningful for nominal data anyway. **Mitigation:** Use position or grouping encodings that communicate membership clearly.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Assigning arbitrary numeric codes to nominal categories and plotting them as bars. **Why it fails:** It fabricates magnitude and rank that do not exist in the schema of the data [@mackinlayAutomatingDesignGraphical1986b].

## Quick tests <!-- role: check -->

**Failure Sign:** A reader could sensibly ask “Which category is bigger/better?” based only on bar length, even though the data has no such concept. **Quick Check:** Ask whether “greater than” is defined for the category values; if not, bar length is the wrong encoding. **Stronger Test:** List every visual comparison the chart enables (longer/shorter) and confirm each corresponds to a valid relation in the data.

## What to do instead <!-- role: fix -->

- Use a plot-chart-like encoding where categories are labels and marks indicate membership without using length.
- Encode category with a mark property intended for nominal distinctions (for example, distinct mark shapes or hues when available).
- Use grouping or faceting so categories are separated spatially without implying magnitude.
- Present the nominal attribute as text labels when the primary task is identification rather than comparison.
