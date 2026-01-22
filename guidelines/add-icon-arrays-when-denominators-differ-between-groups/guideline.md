---
id: add-icon-arrays-when-denominators-differ-between-groups
title: Add icon arrays when comparing risks across groups with different denominators
bibliography: references.bib
description: Use icon arrays to reduce denominator neglect when treated and untreated
  groups have different sample sizes.
labels:
- chart:icon-array
- task:compare
- visual:part-to-whole
- impact:accuracy
- data:risk
- audience:general-public
- domain:health-risk
---

## Use icon arrays to make unequal denominators visible in risk comparisons <!-- role: advice -->

Add icon arrays alongside the numeric counts whenever two groups being compared have different total sizes (different denominators). Keep each array’s total number of icons equal to that group’s sample size so the part-to-whole relationship is visually explicit.

## Why icon arrays reduce denominator neglect in unequal-denominator comparisons <!-- role: reason -->

When denominators differ across groups, many people overweight the absolute event counts (numerators) and underweight the total opportunities for the event (denominators), producing systematic over- or underestimation of relative risk reduction. Icon arrays make the denominator perceptually salient as a “whole,” so viewers are more likely to interpret numerators as parts of that whole rather than as standalone magnitudes.

**Mechanism:** Icon arrays externalize the group “whole” (denominator) and embed affected cases as a subset, which shifts attention from raw counts to proportions.

**Evidence:** Accuracy of estimated treatment relative risk reduction dropped when treated and untreated groups had different denominators, consistent with denominator neglect, and adding icon arrays largely eliminated this accuracy loss in both within-subject and between-subject designs [@garcia-retameroIconArraysHelp2010]. When denominators differed, correct estimates increased substantially with icon arrays (e.g., from about half correct to the mid–high 80% range in the lab study) and accuracy became more similar across denominator-size conditions [@garcia-retameroIconArraysHelp2010].

**Notes:** This guideline targets comparisons where the decision depends on proportions (risk per group), not raw event counts.

## When unequal-denominator risk comparisons occur <!-- role: context -->

- **User Goal:** Judge treatment effectiveness (e.g., relative risk reduction) from reported outcomes in treated vs untreated groups.
- **Task:** Compare two risks that are each expressed as “events out of total,” where totals differ across groups.
- **Data:** Two-group binary outcomes with unequal sample sizes (e.g., 100 treated vs 500 untreated), where event counts can mislead if read as absolute magnitudes.
- **Chart Setting:** Patient decision aids, web pages, pamphlets, consent discussions, or any static display where quick comprehension is needed.
- **Audience:** Mixed numeracy audiences, including older adults.
- **Success Criterion:** More accurate interpretation of risk reduction across denominator conditions.

## When not to rely on icon arrays <!-- role: exceptions -->

**Break it when:** The communication goal is explicitly about absolute burden (total number of events) rather than per-person risk. **Why:** Emphasizing part-to-whole can de-emphasize the absolute counts that are the intended message.

## Tradeoffs of adding icon arrays <!-- role: costs -->

**Sacrifice:** Visual space and layout simplicity, because arrays require enough area to show the whole population. **Risk:** Viewers may focus on the picture and ignore exact numeric values if precision is required. **Mitigation:** Ensure the numeric counts remain present alongside the arrays.

## Common ways this fails in practice <!-- role: mistakes -->

**Mistake:** Showing only the event counts (numerators) for treated vs untreated groups when denominators differ. **Why it fails:** Viewers systematically misestimate treatment effects by neglecting the different totals, leading to over- or underestimation of relative risk reduction [@garcia-retameroIconArraysHelp2010].

## Quick checks for denominator neglect risk <!-- role: check -->

**Failure Sign:** People’s judgments track which group has the larger event count, even when that group also has a much larger total. **Quick Check:** Remove the denominators from view mentally—if the “winner” flips based on numerators alone, the display is vulnerable. **Stronger Test:** Ask a small sample of users to estimate risk reduction; large systematic over/underestimates in unequal-denominator cases indicate denominator neglect.

## What to do instead if you cannot add icon arrays <!-- role: fix -->

- Present treated and untreated outcomes using equal denominators (same group sizes) so numerators can be compared proportionally.
- Re-express outcomes so the per-group denominator is unmistakable in the comparison task (e.g., keep each group’s “out of N” adjacent and visually grouped).
- Reduce reliance on raw event counts by emphasizing per-group rates in the main comparison message.
- Split the comparison into two clearly separated group summaries so each “part out of whole” is processed before comparing groups.
