---
id: segment-icon-array-design-by-numeracy-and-graph-literacy-when-calibration-matters
title: Segment Icon-Array Icon Choices by Numeracy/Graph Literacy When Calibration
  Matters
bibliography: references.bib
description: "If you need perceived risk to track actual risk, icon type effects differ\
  \ by numeracy and graphical literacy\u2014so tailor or validate by subgroup."
labels:
- chart:icon-array
- task:calibrate-perception
- visual:iconography
- impact:accuracy
- data:probability
- audience:novice
- audience:expert
- domain:health-risk
---

## The Rule <!-- role: advice -->

When your success criterion is that perceived risk aligns with the communicated probability, validate icon type separately for lower vs higher numeracy and/or graphical literacy users.

## The Logic <!-- role: reason -->

- **The Principle:** Different users extract meaning from icon arrays differently, so the same iconography can yield different calibration.
- **The Evidence:** In the full sample, correlations between perceived and actual risk did not differ significantly by icon type; but among higher numeracy or higher graphical literacy participants, icon type significantly affected perceived–actual risk correlations (with restroom icons, photos, and ovals showing higher correlations than some other types) [@zikmund-fisherBlocksOvalsPeople2014]. Among lower numeracy/graph literacy participants, icon type did not show a clear advantage for calibration.

## Where to Apply <!-- role: context -->

- **User Goal:** Accurate “felt risk” that tracks the presented probability (calibration), not just recall or liking.
- **Data Type:** Personal or individualized risk estimates displayed in icon arrays.
- **Audience:** Mixed populations where you expect wide variance in numeracy and graph literacy.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your only goal is recall or preference (not perceived-risk calibration).
- **Reason:** The strongest, most consistent icon-type advantages were in recall and preference; calibration differences were subgroup-dependent and not robust across the whole sample [@zikmund-fisherBlocksOvalsPeople2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** More complex evaluation and potentially multiple UI variants.
- **The Risk:** Subgroup analyses can be unstable if your sample sizes per subgroup are small; you may overfit decisions without adequate validation [@zikmund-fisherBlocksOvalsPeople2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing a single icon type based only on overall-sample calibration results.
- **Why it fails:** Overall results can mask meaningful differences that appear within numeracy/graph-literacy strata [@zikmund-fisherBlocksOvalsPeople2014].

## How to Check <!-- role: check -->

- **Visual Sign:** One-size-fits-all icon choice justified by an average effect.
- **The Test:** Compute perceived–actual risk correlations (or interaction tests) separately for higher vs lower numeracy/graph literacy users and compare patterns across icon types [@zikmund-fisherBlocksOvalsPeople2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reanalyze your existing study data by numeracy/graph literacy (median split or pre-registered cut points) to see if icon choice behaves differently.
- **Best Fix:** If feasible, tailor icon type to audience segments (or choose the most robust icon across segments after subgroup validation), using outcomes aligned to your goal (calibration vs recall vs preference) [@zikmund-fisherBlocksOvalsPeople2014].
