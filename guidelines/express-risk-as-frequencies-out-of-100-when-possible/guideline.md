---
id: express-risk-as-frequencies-out-of-100-when-possible
title: "Express risk as frequencies (for example, \u201CX out of 100\u201D) when possible"
bibliography: references.bib
description: Use frequency formats to make risk feel concrete and to align with common
  patient preferences.
labels:
- chart:none
- task:estimate
- visual:text
- impact:clarity
- data:probabilistic
- audience:novice
- domain:healthcare
---

## Prefer “X out of 100” risk statements over percentages when feasible <!-- role: advice -->

When presenting probabilities, use frequency formats such as “X out of 100 people” instead of only percentages.

## Frequencies can be easier to interpret and feel less abstract <!-- role: reason -->

Frequencies anchor probabilities to a concrete reference class, which can change perceived risk and may improve comprehension for some audiences.

**Mechanism:** A reference class (“out of 100”) supports mental simulation of how many people are affected and reduces abstraction compared with percentages.

**Evidence:** Studies show mixed results on whether frequencies improve understanding over percentages, but lower numeracy audiences may perceive risks differently depending on whether information is presented as frequencies or percentages, and patients often prefer frequencies [@fagerlinHelpingPatientsDecide2011].

**Notes:** Keep denominators consistent across options to avoid confusing comparisons.

## When frequency formats apply <!-- role: context -->

- **User Goal:** Understand likelihood of benefit or harm.
- **Task:** Interpret and compare probabilities.
- **Data:** Probabilities that can be normalized to a common denominator (often 100).
- **Chart Setting:** Verbal counseling, handouts, or decision aids with limited space for explanation.
- **Audience:** Patients with limited numeracy or discomfort with percentages.
- **Success Criterion:** Users can correctly restate “how many people are affected” and compare magnitudes.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The event is extremely rare and a “per 100” denominator would round to zero. **Why:** Rounding can erase meaningful differences and create false reassurance.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Frequencies can require choosing a denominator and may take more words. **Risk:** Inconsistent denominators across statements can mislead. **Mitigation:** Standardize the denominator across all options shown together.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Mixing “out of 100,” “out of 1000,” and percentages in the same comparison. **Why it fails:** Users may compare numerators directly and misjudge the relative size of risks.

## Quick tests <!-- role: check -->

**Failure Sign:** Users ask “out of how many?” **Quick Check:** Scan the page/script and confirm every probability includes an explicit denominator. **Stronger Test:** Ask users to compare two options and listen for denominator confusion.

## What to do instead <!-- role: fix -->

- Convert all compared probabilities to the same denominator before presenting them.
- If you must use percentages, add a matched frequency in parentheses.
- For very rare events, increase the denominator so the expected count is visible.
- Keep the frequency phrasing identical across options to support scanning.
