---
id: measure-persuasion-with-pre-post-attitude-and-initial-attitude-segmentation
title: Measure persuasion with pre/post attitude change and segment results by initial
  attitude
bibliography: references.bib
description: Pre/post attitude measures plus initial-attitude segmentation reveal
  when charts versus tables persuade.
labels:
- chart:agnostic
- task:evaluate
- visual:annotation
- impact:persuasion
- data:survey
- audience:researcher
- method:experiment
---

## Use pre/post attitude change and initial-attitude buckets to evaluate persuasive visuals <!-- role: advice -->

Measure persuasion as the difference between post-treatment and pre-treatment attitude, and analyze results separately for negatively polarized, neutral/weakly polarized, and positively polarized participants. Use the same attitude question wording pre and post.

## Why segmentation is necessary to understand persuasive impact <!-- role: reason -->

The effectiveness of a presentation format depends strongly on what the viewer already believes; without measuring initial attitude and change, you can miss or misinterpret format effects.

**Mechanism:** Initial attitudes constrain possible movement (ceiling/floor effects) and can change how viewers process the same evidence, producing different (even reversed) effects by subgroup.

**Evidence:** Format effects differed by initial attitude: charts increased persuasion likelihood for neutral/weakly polarized participants, while tables increased persuasion likelihood for negatively polarized participants, with consistent trends across three topics [@pandeyPersuasivePowerData2014]. The study operationalized persuasion as pre/post attitude change on a 7-point Likert scale and used initial-attitude buckets (negative, neutral/weak, positive) to detect these interactions [@pandeyPersuasivePowerData2014].

**Notes:** Segmenting also improves interpretability because strongly positive participants may show limited additional positive change.

## When this applies: evaluating persuasive message formats <!-- role: context -->

- **User Goal:** Assess whether a message format (e.g., charts vs tables) shifts attitudes.
- **Task:** Quantify attitude change attributable to a treatment.
- **Data:** Survey responses on a Likert attitude item collected before and after exposure.
- **Chart Setting:** Controlled comparison where only the data presentation format changes.
- **Audience:** Study participants or campaign audiences with varied prior beliefs.
- **Success Criterion:** Reliable detection of differences in persuasion likelihood and mean attitude change by segment.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot collect a valid pre-treatment attitude (e.g., exposure cannot be separated from measurement). **Why:** You cannot compute within-person attitude change or segment by initial attitude as defined here.

## Tradeoffs of pre/post + segmentation <!-- role: costs -->

**Sacrifice:** Extra survey time and analysis complexity. **Risk:** Small segment sizes can inflate uncertainty and reduce statistical power, especially for extreme initial-attitude groups. **Mitigation:** Ensure sufficient sample sizes per segment or aggregate across multiple comparable topics.

## Common failure modes in persuasion measurement <!-- role: mistakes -->

- **Mistake:** Reporting only overall average attitude change without subgroup analysis. **Why it fails:** Opposing subgroup effects can cancel out, obscuring actionable conclusions [@pandeyPersuasivePowerData2014].
- **Mistake:** Changing the attitude question wording between pre and post. **Why it fails:** You no longer measure the same construct, reducing reliability of the change score [@pandeyPersuasivePowerData2014].

## Quick checks for this guideline <!-- role: check -->

**Failure Sign:** Results look inconsistent or “no effect” overall but vary widely by participant comments or topic. **Quick Check:** Plot (+) change / no change / (-) change separately for each initial-attitude bucket. **Stronger Test:** Pre-register segment-level analyses and ensure minimum N per bucket before concluding there is no format effect.

## What to do instead if pre/post isn’t feasible <!-- role: fix -->

- Use a single post-exposure attitude measure but still collect a pre-exposure proxy for initial attitude (e.g., screening question before assignment).
- Run separate studies for different audience segments using screening to balance initial attitudes.
- Replicate across multiple topics to increase robustness of segment-level estimates.
- Add qualitative questions to detect whether changes are due to evidence acceptance, skepticism, or perceived manipulation.
