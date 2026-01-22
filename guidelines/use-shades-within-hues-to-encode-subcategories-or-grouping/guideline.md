---
id: use-shades-within-hues-to-encode-subcategories-or-grouping
title: Use hues for main categories and shades for subcategories (even if subcategories
  are unordered)
bibliography: references.bib
description: 'Combine hue and shade to show hierarchy: hue separates top-level categories
  while shades differentiate their subcategories.'
labels:
- chart:general
- task:group
- visual:color
- impact:structure
- data:hierarchical
- audience:general
- complexity:intermediate
---

## Use hues for main categories and shades for subcategories (even if subcategories are unordered) <!-- role: advice -->

Use distinct hues to separate main categories, and use lighter/darker shades of each hue to differentiate subcategories within them. Don’t assume shades must imply an order when they are clearly used as “within-category differentiators.”

## Why hue-plus-shade communicates hierarchy <!-- role: reason -->

A stable hue communicates “belongs to this group,” while variation in lightness within that hue communicates “different item inside the group.” Readers accept lightness variation as a secondary differentiator when the primary grouping is already established.

**Mechanism:** Hue establishes categorical membership at a higher level; shade variation acts as a subordinate cue that helps disambiguate related items without adding more unrelated colors.

**Evidence:** Using hues for categories and shades for subcategories is illustrated as an effective pattern (for example, two main groups with shades for territories/variants), and shades can work even when the subcategories are not ordered because readers infer the intent is differentiation within a group [@muth_quantitative_vs_qualitative_2021].

**Notes:** If everything is directly labeled, color becomes optional; labels can “free” color from acting as a legend key.

## When this applies: hierarchical categories in one view <!-- role: context -->

- **User Goal:** Help readers see both grouping (which major category) and identity within groups (which subcategory).
- **Task:** Group and differentiate items within each group.
- **Data:** Categorical hierarchy (category → subcategory), possibly with many subcategories.
- **Chart Setting:** Area-based charts, stacked compositions, treemaps, and similar displays.
- **Audience:** Readers who need quick grouping recognition without reading a legend repeatedly.
- **Success Criterion:** Readers can immediately see group membership and still pick out distinct sub-items.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The number of subcategories per main category is large enough that shades become indistinguishable. **Why:** Many similar lightness steps are hard to tell apart, especially without ordering or labels [@muth_quantitative_vs_qualitative_2021].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You reduce the palette’s capacity for many clearly distinct categories because shades are closer than separate hues. **Risk:** Viewers may still try to interpret a light-to-dark progression as ordered if the design suggests ranking. **Mitigation:** Make the grouping visually explicit through labeling, layout, or separators so shade reads as “within-group variation” [@muth_quantitative_vs_qualitative_2021].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using too many shades within one hue to represent many subcategories. **Why it fails:** Readers give up distinguishing multiple similar shades, especially when not ordered or directly labeled [@muth_quantitative_vs_qualitative_2021].
- **Mistake:** Mixing shades across multiple hues in a way that makes some groups look like different top-level categories. **Why it fails:** Additional hues can accidentally imply additional group levels or different category types [@muth_quantitative_vs_qualitative_2021].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers confuse subcategories within a group or can’t reliably match legend entries to marks. **Quick Check:** Convert the chart to grayscale; if subcategories blur together within each group, you have too many shades. **Stronger Test:** Ask someone to identify three randomly chosen subcategories inside the same main category; if they hesitate, simplify the hierarchy or labeling [@muth_quantitative_vs_qualitative_2021].

## What to do instead <!-- role: fix -->

- Reduce the number of subcategories shown at once by filtering, aggregating, or splitting into small multiples [@muth_quantitative_vs_qualitative_2021].
- Add direct labels or clear separators so subcategory identification doesn’t depend entirely on subtle shade differences [@muth_quantitative_vs_qualitative_2021].
- If subcategories have a meaningful order, align shade intensity with that order to make the ramp interpretable [@muth_quantitative_vs_qualitative_2021].
- If the hierarchy is not essential, remove the subcategory level and show only the main categories with hues [@muth_quantitative_vs_qualitative_2021].
