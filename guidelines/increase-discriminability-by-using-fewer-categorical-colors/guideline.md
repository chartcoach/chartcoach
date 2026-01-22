---
id: increase-discriminability-by-using-fewer-categorical-colors
title: Reduce the number of categorical colors when discrimination accuracy matters
bibliography: references.bib
description: Use fewer categories per view because discrimination errors rise as palette
  size increases.
labels:
- chart:categorical
- task:discriminate
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
---

## Reduce palette size when accurate color identification is required <!-- role: advice -->

When accurate identification of categories is important, reduce the number of distinct colors used at once rather than forcing a larger categorical palette.

## Why fewer colors improve discrimination <!-- role: reason -->

As the number of colors increases, the chance that at least one pair becomes confusable rises and attention demands increase, which increases errors in category identification tasks.

**Mechanism:** More categories create more pairwise comparisons and more opportunities for a weak pair; this degrades identification accuracy even if many pairs remain distinct.

**Evidence:** In the discrimination task, average error increased as palette size increased (3-color < 5-color < 8-color), and palette size had a significant effect on error rates [@gramazioColorgoricalCreatingDiscriminable2017a]. The paper notes that higher palette sizes can also change how well pair-based discriminability and preference scores predict behavior, indicating additional difficulty at larger sizes [@gramazioColorgoricalCreatingDiscriminable2017a].

**Notes:** Preference ratings were more stable across sizes than error in the reported benchmark experiment, so the main risk at larger sizes is discrimination failure.

## When this applies <!-- role: context -->

- **User Goal:** Correctly identify categories from color-coded marks.
- **Task:** Discriminate and count/compare colored regions or marks.
- **Data:** Categorical with many classes, but not all need simultaneous display.
- **Chart Setting:** Dense marks or repeated lookup tasks (e.g., choropleths with many regions).
- **Audience:** General users, including those under time pressure.
- **Success Criterion:** Lower misclassification or miscounting due to color confusions.

## When not to follow it <!-- role: exceptions -->

**Break it when:** All categories must be visible simultaneously and cannot be grouped or filtered. **Why:** Reducing palette size would remove required information.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may need interaction, grouping, or multiple views to show all categories. **Risk:** Users might lose global context if categories are split across views. **Mitigation:** Preserve consistent mapping within each view and provide navigational structure to access all categories.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Expanding to 8+ colors to “fit everything” in one legend. **Why it fails:** Errors increase with palette size, so fitting everything at once can reduce correctness.
- **Mistake:** Assuming better palette optimization fully cancels the size effect. **Why it fails:** The experiments show size still impacts error even under structured palette generation.

## Quick tests <!-- role: check -->

**Failure Sign:** Users misidentify categories more often when the legend grows. **Quick Check:** Try the same chart with fewer categories shown (or grouped) and see whether confusions drop immediately. **Stronger Test:** Run a small discrimination test comparing error rates between the full palette and a reduced palette.

## What to do instead <!-- role: fix -->

- Group low-importance categories into an “Other” class to reduce palette size.
- Use interaction (filtering, highlighting) so users only compare a subset of categories at a time.
- Use multiple coordinated views, each with a smaller palette, instead of one view with a large palette.
- Redesign the task so that color is not the only channel carrying category identity.
