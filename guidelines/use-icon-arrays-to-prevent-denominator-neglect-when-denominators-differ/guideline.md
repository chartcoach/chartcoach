---
id: use-icon-arrays-to-prevent-denominator-neglect-when-denominators-differ
title: Add icon arrays when comparing treated vs untreated risks with different denominator
  sizes
bibliography: references.bib
description: Icon arrays alongside numbers reduce denominator neglect and improve
  accuracy when group sizes differ.
labels:
- chart:icon-array
- task:compare
- visual:position
- impact:clarity
- data:proportional
- audience:novice
- domain:health-risk
---

## Use icon arrays to prevent denominator neglect when denominators differ <!-- role: advice -->

Add icon arrays next to numerical risk information when treatment and control groups have different total sizes. Use one array per group so the total group size is visually explicit.

## Icon arrays make denominators perceptually salient <!-- role: reason -->

Icon arrays make the denominator (the total number of people at risk in each group) perceptually available, reducing the tendency to focus on the numerator (the number of events) alone.

**Mechanism:** By showing the full set of individuals in each group and highlighting the subset with the event, icon arrays support reasoning with proportions rather than absolute counts.

**Evidence:** When risks were shown only numerically and treated/untreated denominators differed, many participants—especially low-numeracy—misestimated relative risk reduction in ways consistent with denominator neglect; adding icon arrays eliminated the denominator-size effect on accuracy and reduced errors, particularly for low-numeracy participants [@garcia-retameroCommunicatingTreatmentRisk2009].

**Notes:** The benefit held in probabilistic national samples from both the United States and Germany.

## When treatment and control group sizes are unequal <!-- role: context -->

- **User Goal:** Judge how effective a treatment is compared with no treatment.
- **Task:** Estimate or compare relative risk reduction (Relative Risk Reduction, RRR) from outcome counts.
- **Data:** Two groups with unequal denominators (e.g., treated n=100 vs untreated n=800) and event counts.
- **Chart Setting:** Static or interactive patient-facing or clinician-facing materials where both groups are shown together.
- **Audience:** Mixed numeracy, including low numeracy.
- **Success Criterion:** Reduced denominator neglect; accuracy should not vary with denominator size.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Both groups have equal denominators and the only goal is to compare event counts. **Why:** Denominator neglect is less likely to be triggered by unequal group sizes in this specific setup.

## Tradeoffs of adding icon arrays <!-- role: costs -->

**Sacrifice:** Space and visual complexity increase because you must display two arrays (treated and untreated). **Risk:** Large denominators can produce dense displays that are harder to scan. **Mitigation:** Keep the display focused on the two groups and the event subset.

## Common ways this fails <!-- role: mistakes -->

- **Mistake:** Showing only the number of deaths/events for each group without making the total group size visually salient. **Why it fails:** Viewers may rely on absolute event counts and ignore denominators, producing denominator neglect.
- **Mistake:** Using a single combined icon array for both groups without clear separation. **Why it fails:** The viewer cannot easily map each numerator to its correct denominator.

## Quick checks for denominator neglect risk <!-- role: check -->

**Failure Sign:** Accuracy changes substantially when you keep the relative risk reduction constant but change the group sizes. **Quick Check:** Swap from (100 treated vs 800 untreated) to (800 treated vs 100 untreated) while holding the relative risk reduction constant; if interpretation flips, denominators are being neglected. **Stronger Test:** Run a brief comprehension check asking for expected deaths out of 1000 with and without treatment and compare error rates across denominator-size variants.

## What to do instead if you cannot add icon arrays <!-- role: fix -->

- Show treated and untreated denominators prominently and repeatedly wherever the event counts appear.
- Separate treated and untreated information into clearly labeled blocks so each numerator is paired with its denominator.
- Ask users to report expected outcomes out of a fixed base (e.g., “out of 1000”) for each group before asking about risk reduction.
- Redesign the communication so proportional information is the focal element rather than raw event counts.
