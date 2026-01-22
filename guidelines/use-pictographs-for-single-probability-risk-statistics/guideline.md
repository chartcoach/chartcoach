---
id: use-pictographs-for-single-probability-risk-statistics
title: Use pictographs (icon arrays) to show single risk or benefit probabilities
bibliography: references.bib
description: Prefer pictographs over bar, pie, or other graphs when communicating
  individual risk statistics for patient decisions.
labels:
- chart:pictograph
- task:compare
- visual:position
- impact:clarity
- data:probabilistic
- audience:novice
- domain:healthcare
---

## Use pictographs when graphing an individual probability <!-- role: advice -->

When you include a graph to communicate a single risk or benefit probability, use a pictograph (icon array) that shows both the people affected and not affected.

## Pictographs improve comprehension of probabilities <!-- role: reason -->

Icon arrays make the numerator and denominator concrete and visible at the same time, helping viewers grasp both exact values and the overall takeaway.

**Mechanism:** By representing probabilities as frequencies over a fixed set of icons, pictographs reduce abstraction and support accurate interpretation.

**Evidence:** Pictographs are understood more quickly and accurately than other common risk graphics for individual statistics, and they support both verbatim and gist understanding in patient decision contexts [@fagerlinHelpingPatientsDecide2011].

**Notes:** Pictographs are particularly suited to single-timepoint probabilities rather than showing complex time trends.

## When pictographs are the right choice <!-- role: context -->

- **User Goal:** Understand the likelihood of an outcome or side effect and compare options.
- **Task:** Read a probability and interpret its magnitude.
- **Data:** One or a small number of probabilities (often per option), commonly per 100 people.
- **Chart Setting:** Static handouts, web decision aids, or slide-based explanations.
- **Audience:** Patients with low numeracy; readers who benefit from concrete denominators.
- **Success Criterion:** Users can correctly answer “how many out of 100” and distinguish affected vs unaffected.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary goal is to show how risk changes over time with many time points. **Why:** Pictographs are not well suited to representing trajectories across time.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Pictographs can take more space than compact charts. **Risk:** If icons are too small or the denominator changes across panels, users can misread comparisons. **Mitigation:** Keep a consistent denominator and ensure legibility.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a pie chart or bar chart for a single probability without showing the denominator clearly. **Why it fails:** Viewers can lose the sense of “out of how many” and misjudge magnitude.
- **Mistake:** Showing only affected icons without showing unaffected icons. **Why it fails:** Users cannot easily infer the denominator and may overfocus on the highlighted portion.

## Quick tests <!-- role: check -->

**Failure Sign:** People can repeat a percent but cannot say “how many out of 100.” **Quick Check:** Hide the numeric label and see if the icon count still supports the intended reading. **Stronger Test:** Ask users to compare two icon arrays and explain the difference in plain language.

## What to do instead <!-- role: fix -->

- Use a consistent 100-icon grid and label it as “out of 100 people.”
- Show both affected and unaffected icons to preserve the full denominator.
- If time trends are required, switch to a time-based graphic and explicitly label the time horizon.
- Pair the pictograph with a short frequency statement that matches the icons.
