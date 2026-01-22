---
id: precompute-and-sum-risk-tradeoffs-instead-of-making-users-calculate
title: Precompute key totals and tradeoffs instead of requiring users to calculate
  them
bibliography: references.bib
description: Reduce cognitive effort and errors by doing the necessary arithmetic
  for users in risk and tradeoff communications.
labels:
- chart:general
- task:decide
- visual:annotation
- impact:accuracy
- data:probabilistic
- audience:novice
- domain:health
---

## Do the arithmetic for the user in quantitative tradeoff displays <!-- role: advice -->

When a decision requires combining multiple numeric components (such as summing risks or translating a multiplier into an end risk), provide the computed totals directly. Avoid requiring users to infer which operations to perform.

## Why offloading computation improves tradeoff accuracy <!-- role: reason -->

Users often struggle not only with arithmetic but also with selecting the correct algorithm and integrating multiple numbers under time pressure or stress. Providing computed totals reduces cognitive load and lowers the chance of procedure and interpretation errors.

**Mechanism:** Offloading calculation to the artifact reduces effortful processing requirements and helps users focus on meaning and choice.

**Evidence:** Completing calculations for consumers reduces cognitive effort and improves accuracy in making risk tradeoffs, such as providing baseline and end risks or summed risks across outcomes rather than expecting users to compute them [@anckerRethinkingHealthNumeracy2007].

**Notes:** This is especially relevant when document literacy demands are high or when multiple outcomes must be combined.

## Situations where users are likely to miscompute or miscombine risks <!-- role: context -->

- **User Goal:** Choose among treatments, screenings, or behavior changes using numeric tradeoffs.
- **Task:** Combine, sum, or translate numeric statements into comparable quantities.
- **Data:** Multiple outcome probabilities, multipliers, competing risks/benefits.
- **Chart Setting:** Decision aids, consent materials, portal summaries, brochures.
- **Audience:** Mixed numeracy; users under stress or time pressure.
- **Success Criterion:** Users reach decisions consistent with accurate understanding of totals and comparisons.

## When not to precompute totals <!-- role: exceptions -->

**Break it when:** The decision requires user-specified weights or value judgments that should not be collapsed into a single combined number. **Why:** A single precomputed total can conceal preference-sensitive tradeoffs.

## Tradeoffs of precomputing for users <!-- role: costs -->

**Sacrifice:** Less flexibility and less transparency about intermediate components. **Risk:** Users may distrust “black-box” totals or misapply them outside the stated conditions. **Mitigation:** Provide components alongside the total with clear labeling.

## Common failure modes in tradeoff displays <!-- role: mistakes -->

- **Mistake:** Listing multiple risks and expecting users to add or compare them mentally. **Why it fails:** Users may select the wrong operation or fail to integrate the numbers correctly.
- **Mistake:** Using multiplicative phrasing (e.g., “triples the risk”) without showing the end risk. **Why it fails:** Readers misjudge magnitude without translating it into an absolute level.

## Quick tests for computation offloading <!-- role: check -->

**Failure Sign:** Different users arrive at different totals from the same inputs, or cannot explain how to combine the listed numbers. **Quick Check:** Ask a user to compute the overall risk/benefit from the display without external aids and note whether they choose the right operation. **Stronger Test:** Compare decision accuracy between “components only” versus “components + computed totals.”

## What to do instead when a single total is inappropriate <!-- role: fix -->

- Show totals for each outcome separately and include an optional combined summary labeled as such.
- Provide a small interactive worksheet that performs arithmetic after the user enters values or selects options.
- Break the decision into steps that each require only one simple inference.
- Add explicit operation cues (e.g., “add these two risks”) where computation cannot be avoided.
