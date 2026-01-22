---
id: use-vertically-stacked-bar-charts-for-range-comparison-between-two-sets
title: Use vertically stacked bar charts to compare which of two sets has the wider
  range
bibliography: references.bib
description: Vertically stacked bar charts support more precise judgments of which
  set has the wider min-to-max range than other arrangements.
labels:
- chart:bar
- task:compare
- visual:position
- impact:accuracy
- data:categorical
- audience:novice
- comparison:set-to-set
---

## Use vertical stacking for set-to-set range comparisons <!-- role: advice -->

Use two vertically stacked bar charts when the user must decide which dataset has the wider range (difference between minimum and maximum values). Avoid superposing the two bar sets in the same plotting area for this task.

## Why vertical stacking improves range comparison precision <!-- role: reason -->

Range judgments in bar charts can be supported by perceptual proxies that depend on perceiving within-set differences between items (e.g., comparing pairwise deltas across bars, including neighboring differences). Vertical stacking keeps the two sets perceptually separate, making it easier to extract within-set structure without confusion from overlapping marks.

**Mechanism:** Separating sets reduces cross-set visual interference, enabling viewers to apply within-set difference proxies that align with range judgments.

**Evidence:** In timed comparisons of “which set has the widest range” between two horizontal bar-chart sets, precision was best with vertically stacked charts and worst with superposed charts; stacked also yielded the highest accuracy among arrangements [@jardinePerceptualProxiesVisual2020a].

**Notes:** The staircase procedure showed stronger arrangement-driven accuracy differences for range than for mean, suggesting arrangement choice can be especially consequential for range judgments.

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Decide which of two groups has more spread (bigger min-to-max span).
- **Task:** Biggest range comparison between two sets.
- **Data:** Two series with multiple items each.
- **Chart Setting:** Brief exposure (about 1.5 seconds) with response after removal; viewers may be non-experts in statistical terminology.
- **Audience:** Non-expert viewers; some may need reinforcement of what “range” means.
- **Success Criterion:** High accuracy and precision for small differences in range width.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task is primarily item-to-item matching or detecting the largest between-set change for a specific item. **Why:** This paper contrasts range (set-level) performance with earlier item-focused tasks where overlap/animation can be more effective [@jardinePerceptualProxiesVisual2020a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Vertical stacking increases the required vertical space and may reduce the number of panels you can show at once. **Risk:** Users may need more scrolling in dashboards or reports. **Mitigation:** Use stacking selectively for comparisons where range judgments are central.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Superposing two bar sets to let users “see both at once” for range. **Why it fails:** Range comparison was least precise in the superposed arrangement in the study [@jardinePerceptualProxiesVisual2020a].
- **Mistake:** Assuming any arrangement will converge to similar performance once users practice. **Why it fails:** Accuracy differed across arrangements in the range task even with adaptive difficulty titration [@jardinePerceptualProxiesVisual2020a].

## Quick tests <!-- role: check -->

**Failure Sign:** Users can only answer correctly when one set’s range is dramatically larger. **Quick Check:** Show a stacked version and ask whether the wider-spread set is identifiable at a glance. **Stronger Test:** Run a short timed study varying the range difference and verify that stacked supports correct answers at smaller differences than your alternative layout.

## What to do instead if stacking is not possible <!-- role: fix -->

- Use an adjacent small-multiple layout rather than overlap.
- Increase separation cues between sets (distinct regions) if both must appear in one figure.
- Simplify the task by explicitly highlighting each set’s minimum and maximum bars.
- Change the representation so the comparison target is directly encoded (e.g., show only min and max per set) if the goal is strictly range.
