---
id: avoid-non-data-vis-palettes-that-imply-hierarchy-for-categorical-data
title: Avoid Palettes That Imply Hierarchy When Categories Are Equal
bibliography: references.bib
description: "Don\u2019t use palettes built around background and accent roles when\
  \ all categories should carry equal visual weight."
labels:
- chart:all
- task:categorize
- visual:color
- impact:clarity
- data:categorical
- audience:general
- complexity:intermediate
- source:datawrapper
---

## The Rule <!-- role: advice -->

When categories are meant to be equally important, use a palette where colors have roughly equal visual importance; avoid “background + accent” palettes designed for UI/interior design.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Perceived salience creates unintended ranking and attention bias
- **The Evidence:** Muth explains that many popular palettes (especially from general design collections or books) are built for scenes with primary and secondary elements—desaturated background-like colors plus a few strong accents—which is often the opposite of what you want for categorical palettes where all groups should read as peers [@muth_good_color_palettes_2024].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Compare multiple categories without one being unintentionally highlighted
- **Data Type:** Categorical data with peer categories (no “focus” group)
- **Audience:** Any audience where unintended emphasis could mislead interpretation

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You are deliberately designing a hierarchy (e.g., one highlighted series and several contextual series)
- **Reason:** Accent + muted colors can support the narrative by guiding attention [@muth_good_color_palettes_2024].
- **Scenario:** Your categories naturally form pairs (e.g., same industry across two years)
- **Reason:** A palette with paired salience (like ColorBrewer’s “Paired”) can be appropriate for pair comparisons [@muth_good_color_palettes_2024].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Some aesthetically pleasing “designer palettes” become unusable as-is
- **The Risk:** Forcing equal importance may reduce your ability to guide attention when a story truly needs a focal point [@muth_good_color_palettes_2024].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Taking a five-color palette from a palette gallery and assigning every color to a category without checking salience balance
- **Why it fails:** One or two accent colors dominate, creating implied hierarchy [@muth_good_color_palettes_2024].
- **The Wrong Fix:** Keeping a very bright yellow/pastel color on a white background because it “matches the palette”
- **Why it fails:** It disappears and functions like a background color rather than a category color [@muth_good_color_palettes_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers’ eyes snap to one category even when the data doesn’t warrant it; some categories look “muted” or “disabled”
- **The Test:** Squint or blur the chart: if one color consistently pops as an accent, the palette is not balanced for equal categories [@muth_good_color_palettes_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce saturation/brightness of the dominant accent color(s) or strengthen the muted ones until they feel similarly salient [@muth_good_color_palettes_2024].
- **Best Fix:** Choose or generate a categorical palette specifically intended for data visualization and equal category importance, then validate it with contrast and colorblind checks [@muth_good_color_palettes_2024].
