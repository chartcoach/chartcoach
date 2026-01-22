---
id: include-baseline-risk-when-reporting-risk-reductions
title: Include baseline risk when reporting absolute or relative risk reduction
bibliography: references.bib
description: Provide baseline risk alongside risk reductions so users can accurately
  judge effect size.
labels:
- chart:general
- task:compare
- visual:annotation
- impact:accuracy
- data:probabilistic
- audience:novice
- domain:health
---

## Always pair risk reductions with baseline risk <!-- role: advice -->

When presenting a risk reduction, include the baseline risk so readers can interpret the magnitude in context. Show both the starting risk and the resulting risk whenever feasible.

## Why baseline risk prevents magnitude misinterpretation <!-- role: reason -->

Relative changes can inflate perceived effect size when the absolute level is small, and readers need a reference point to judge practical significance. Baseline risk supplies the denominator context that supports correct comparison and more accurate judgments.

**Mechanism:** Providing context anchors interpretation and reduces reliance on heuristic impressions from relative percentages.

**Evidence:** Relative differences without absolute context inflate perceived magnitude, and adding baseline risk improves accuracy in interpreting risk reduction information [@anckerRethinkingHealthNumeracy2007].

**Notes:** This applies to both patient-facing and clinician-facing summaries because both groups are susceptible to representation effects.

## Where baseline risk is required for comprehension <!-- role: context -->

- **User Goal:** Decide whether an intervention is worth it or understand benefit magnitude.
- **Task:** Judge effect size and compare options.
- **Data:** Treatment effects, screening benefits, side-effect risks.
- **Chart Setting:** Decision aids, patient brochures, portal summaries, clinical summaries shared with patients.
- **Audience:** Mixed numeracy; readers prone to framing and format effects.
- **Success Criterion:** Readers can correctly state the before-and-after risk and compare interventions fairly.

## When not to emphasize baseline risk <!-- role: exceptions -->

**Break it when:** No credible baseline estimate exists for the user’s relevant population or subgroup. **Why:** A misleading baseline can distort decisions more than an omitted one.

## Tradeoffs of including baseline risk <!-- role: costs -->

**Sacrifice:** More explanatory space and possibly more complex wording. **Risk:** Users may confuse baseline population risk with personal risk if personalization is unclear. **Mitigation:** Clearly label what population the baseline refers to.

## Common failure modes in effect-size reporting <!-- role: mistakes -->

- **Mistake:** Reporting only a relative risk reduction (e.g., “cuts risk by 50%”). **Why it fails:** Readers overestimate the practical impact without knowing the starting risk.
- **Mistake:** Reporting only an absolute reduction without the starting level. **Why it fails:** Users cannot gauge whether the change is large or small relative to the baseline.

## Quick tests for baseline comprehension <!-- role: check -->

**Failure Sign:** Users can repeat the relative change but cannot answer “out of 100 people like me, how many are affected before and after?” **Quick Check:** Ask readers to paraphrase the baseline and resulting risk in their own words. **Stronger Test:** Compare accuracy of effect-size interpretation with and without baseline risk in a small comprehension test.

## What to do instead if baseline is uncertain or variable <!-- role: fix -->

- Provide a plausible baseline range and show corresponding resulting risks across that range.
- Tailor baseline risk to the user’s characteristics when supported by data and clearly labeled.
- Use a display that makes the denominator explicit so baseline context is visually present.
- Add a brief interpretive statement that restates the baseline and the resulting risk in plain language.
