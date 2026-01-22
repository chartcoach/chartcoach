---
id: account-for-low-numeracy-when-designing-icon-arrays-for-proportion-estimation
title: Design icon-array proportion displays to be robust for low-numeracy audiences
bibliography: references.bib
description: Lower numeracy and education are associated with less accurate proportion
  estimates from icon arrays, especially with random arrangements.
labels:
- chart:icon-array
- task:estimate
- visual:layout
- impact:accessibility
- data:proportion
- audience:low-numeracy
- domain:risk-communication
---

## Make icon-array proportion reading resilient to low numeracy <!-- role: advice -->

Assume that some viewers will have difficulty translating an icon array into an accurate percentage, and choose formats that minimize estimation error without counting. Prefer designs that reduce cognitive burden when communicating to mixed-ability audiences.

## Numeracy and education predict estimation accuracy under quick viewing <!-- role: reason -->

People with lower numeracy and lower educational attainment are more likely to misestimate proportions in icon arrays, and design choices that increase perceptual workload can widen these gaps.

**Mechanism:** Lower facility with percentages and proportional reasoning (and/or reporting a numeric answer) increases error; layouts that require more visual aggregation amplify this effect.

**Evidence:** Lower numeracy was associated with greater inaccuracy for some proportions (notably 6% and 29%) and low-numeracy respondents gave higher mean estimates across graphics, with significant differences in several conditions [@anckerEffectArrangementStick2011]. In a mixed model, relative inaccuracy decreased with higher numeracy scores and (marginally) with higher education, while random arrangement increased relative inaccuracy [@anckerEffectArrangementStick2011].

**Notes:** The numeracy association was strongest for lower proportions tested and was not uniformly significant for all proportions.

## When audience numeracy is mixed or unknown <!-- role: context -->

- **User Goal:** Understand a probability from a picture and use it in a judgment.
- **Task:** Estimate or interpret a proportion quickly.
- **Data:** Small-to-moderate probabilities where errors have large relative impact.
- **Chart Setting:** Public-facing health materials, clinic handouts, or web decision aids.
- **Audience:** Heterogeneous audiences that include low-numeracy and lower-education users.
- **Success Criterion:** Comparable understanding across numeracy levels, not just good average performance.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The display is intended for a highly numerate specialist audience and will be used with time to verify exact numbers. **Why:** The primary constraint (first-glance estimation under time pressure) is less relevant [@anckerEffectArrangementStick2011].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Robust designs may prioritize readability over stylistic realism. **Risk:** Over-optimizing for quick estimation can reduce perceived “randomness” or naturalness. **Mitigation:** Validate with brief comprehension checks in the intended audience.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Treating icon arrays as inherently “easy for everyone” and ignoring numeracy differences. **Why it fails:** Numeracy and education meaningfully predict estimation error in quick visual proportion tasks [@anckerEffectArrangementStick2011].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Low-numeracy participants systematically give higher estimates than others for the same icon arrays. **Quick Check:** Segment pilot responses by a short numeracy screener and compare bias/variance. **Stronger Test:** Use a repeated-measures pilot where the same proportion is shown in different arrangements and measure whether disparities widen under random layouts [@anckerEffectArrangementStick2011].

## Fix: What to do instead <!-- role: fix -->

- Prefer sequential (blocked) arrangements rather than random scatter to reduce aggregation demands.
- Include numeric percentage labels so users do not need to translate visual density into a number unaided.
- Test with participants of varied numeracy and education levels and revise formats that show large between-group gaps.
- Avoid relying on small unlabeled differences between risks when communicating to mixed-numeracy audiences.
