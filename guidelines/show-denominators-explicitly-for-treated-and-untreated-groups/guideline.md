---
id: show-denominators-explicitly-for-treated-and-untreated-groups
title: Make Denominators Salient for Treated and Untreated Groups
bibliography: references.bib
description: Prevent denominator neglect by ensuring viewers can see the total number
  of treated and untreated individuals, not just event counts.
labels:
- chart:icon-array
- task:compare
- visual:quantity
- impact:accuracy
- data:probabilistic
- audience:low-numeracy
- domain:health
- bias:denominator-neglect
---

## The Rule <!-- role: advice -->

When comparing treatment vs no treatment, visually emphasize the total group sizes (denominators) for both groups, not just the number of events (numerators).

## The Logic <!-- role: reason -->

When denominators differ across groups, many people—especially those with low numeracy—base judgments on raw event counts and misestimate risk reduction (overestimating when the treated denominator is smaller; underestimating when it is larger). This pattern indicates denominator neglect and was observed with numeric-only presentations in national samples; it disappeared when displays made denominators salient (via icon arrays) [@garcia-retameroCommunicatingTreatmentRisk2009].

- **The Principle:** Numerator salience drives ratio misinterpretation when denominators vary
- **The Evidence:** [@garcia-retameroCommunicatingTreatmentRisk2009]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare effectiveness of a treatment across groups with different sample sizes
- **Data Type:** Two-group risk data where denominators can differ (treated N ≠ untreated N)
- **Audience:** Broad populations, with special attention to low-numeracy users

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your communication goal is to report raw event burden (absolute counts) rather than risk or effectiveness.
- **Reason:** In that case, denominators are not the primary quantity for the decision, and emphasizing them may distract from the intended message [@garcia-retameroCommunicatingTreatmentRisk2009].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need larger graphics or more annotation to show totals clearly.
- **The Risk:** If totals are visually heavy, the display can feel “busy,” especially for large denominators.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reporting “5 died with treatment vs 80 died without” without equal emphasis on “out of 100 vs out of 800.”
- **Why it fails:** Viewers may infer a larger treatment benefit by focusing on 5 vs 80 rather than 5/100 vs 80/800 [@garcia-retameroCommunicatingTreatmentRisk2009].

## How to Check <!-- role: check -->

- **Visual Sign:** The event markers dominate the display while totals are implicit or hard to notice.
- **The Test:** Swap denominators (e.g., show 100 vs 800 vs 800 vs 100) while keeping the true relative risk reduction constant; if perceived effectiveness changes, denominators are not salient enough [@garcia-retameroCommunicatingTreatmentRisk2009].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add clear “out of N” totals adjacent to each group and/or show the whole population visually.
- **Best Fix:** Use full icon arrays sized to each denominator so users can see the part-to-whole relationship directly for treated and untreated groups [@garcia-retameroCommunicatingTreatmentRisk2009].
