---
id: prefer-rainbow-or-sequential-over-other-conditions-for-filter-like-target-value-identification-in-quantitative-maps
title: Use rainbow hue or sequential saturation (not isarithmic sequential saturation)
  for filter-like target value identification in quantitative maps
bibliography: references.bib
description: For filter-style identification tasks on quantitative maps, some rainbow
  and sequential conditions outperform isarithmic sequential saturation in accuracy.
labels:
- chart:map
- task:filter
- visual:color
- impact:accuracy
- data:quantitative
- audience:novice
- domain:cartography
---

## Use RC-Choro or SC-Choro over SC-Isa for filter-like identification <!-- role: advice -->

When users must identify data points that match a specific target value (a filter-like task) in quantitative map-like visuals, prefer either a rainbow choropleth or a sequential choropleth over a sequential isarithmic condition.

## Why some map+palette pairings help filtering <!-- role: reason -->

Different palette–map-type pairings can change how easily users can pick out target values among many regions.

**Mechanism:** Some combinations create stronger separations between classes, which can make target matching easier than when colors are harder to discriminate in the spatial configuration.

**Evidence:** For a filter task, the reported accuracy ranking placed rainbow-choropleth and sequential-choropleth above rainbow-isarithmic and sequential-isarithmic, with significant differences reported between the top group and the lower-ranked conditions [@golbiowskaRainbowDashIntuitiveness2022]. This task-linked result is included in a broader collation intended to make such findings actionable in visualization recommendation settings [@zengReviewCollationGraphical2023].

**Notes:** This guideline is specific to the studied conditions and should not be generalized beyond similar map/palette setups without further testing.

## When filter-like target matching applies <!-- role: context -->

- **User Goal:** Locate regions meeting a specified condition (e.g., “find places with value X”).
- **Task:** Filter.
- **Data:** Quantitative values shown as discrete classes with a legend.
- **Chart Setting:** Static map-like display where users visually search and match colors to a legend.
- **Audience:** General audiences or learners.
- **Success Criterion:** Higher accuracy in selecting the correct regions.

## When not to follow this filtering rule <!-- role: exceptions -->

**Break it when:** The primary goal is consistent ordered interpretation across tasks like finding extrema. **Why:** Sequential schemes outperform rainbow schemes for ordered judgments like extrema-finding in the same study context.

## Tradeoffs of these palette–map choices <!-- role: costs -->

**Sacrifice:** You may need to constrain design choices to a specific map type/palette pairing rather than freely mixing them.\
**Risk:** A rainbow palette can still be hard to interpret as ordered magnitude even if it supports target matching.\
**Mitigation:** Keep the legend prominent and ensure class boundaries are visually clear.

## Common mistakes in target value map tasks <!-- role: mistakes -->

**Mistake:** Assuming that any sequential palette performs equally across map types for target matching. **Why it fails:** Performance differed across the tested choropleth vs isarithmic settings.

## Quick tests for target matching performance <!-- role: check -->

**Failure Sign:** Users repeatedly select adjacent classes instead of the target class.\
**Quick Check:** Give a target value and ask a few users to find matching regions; count mismatches.\
**Stronger Test:** Time a small pilot across candidate palette–map combinations and choose the best-performing one.

## What to do instead when target matching is failing <!-- role: fix -->

- Try a choropleth representation instead of an isarithmic one for the same classified data if the task is legend-based target matching.
- If staying with isarithmic, test alternate palettes and adjust class boundaries to increase separability.
- Increase the salience of the target class in the legend (e.g., stronger label emphasis) without changing the underlying mapping.
- Provide an auxiliary list or table of matching regions if the map alone yields frequent selection errors.
