---
id: avoid-random-icon-arrays-for-comparing-moderately-different-risks
title: Avoid random icon arrays when viewers must distinguish moderately different
  risks at a glance
bibliography: references.bib
description: Randomly scattered icon arrays can cause viewers to confuse proportions
  that differ by around a tenth under quick viewing.
labels:
- chart:icon-array
- task:compare
- visual:position
- impact:decision-quality
- data:proportion
- audience:general-public
- domain:risk-communication
---

## Avoid random-scatter icon arrays for side-by-side proportion comparison <!-- role: advice -->

Avoid randomly scattered icon arrays when the viewer needs to compare two risks or detect moderate differences quickly. Use a design that makes the part-to-whole relationship immediately visible.

## Random scatter can obscure moderate differences through bias and variance <!-- role: reason -->

When icons are dispersed, viewers’ estimates become both noisier and more biased, so two different underlying proportions can yield overlapping perceived values, undermining rank and difference judgments.

**Mechanism:** Increased estimation variance (and often overestimation) from dispersed marks expands the overlap between perceived distributions of two proportions, making them harder to discriminate.

**Evidence:** With random arrangements, more than one quarter of viewers incorrectly ranked two icon arrays that differed by 11 percentage points (29% vs 40%), indicating that moderate differences may not be visually discernible at first glance [@anckerEffectArrangementStick2011]. Sequential arrangements reduced this confusion substantially in the same task setup [@anckerEffectArrangementStick2011].

**Notes:** Correlations between random and sequential estimates suggest people retain some sense of magnitude, but not enough for dependable discrimination of moderate differences under time pressure.

## When moderate risk differences must be visible <!-- role: context -->

- **User Goal:** Decide which of two risks is larger, or whether a change is meaningful.
- **Task:** Compare proportions; rank-order two conditions.
- **Data:** Two (or more) proportions close enough that confusion is plausible.
- **Chart Setting:** Side-by-side “before vs after,” “treatment vs control,” or “option A vs option B” risk displays.
- **Audience:** Mixed numeracy and education levels.
- **Success Criterion:** High correct ranking rate and low confusion between nearby proportions.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** Exact discriminability between nearby proportions is not required (for example, the viewer only needs a rough sense of “some” versus “most”). **Why:** The added noise from random scatter may be acceptable if the decision does not depend on moderate differences [@anckerEffectArrangementStick2011].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Designs optimized for discriminability may appear less “natural” than random scatter. **Risk:** Over-emphasizing discriminability can invite overconfidence in tiny differences if the underlying numbers are uncertain. **Mitigation:** Pair comparisons with clear numeric values or explanatory text about magnitude.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Presenting two random-scatter icon arrays and expecting viewers to reliably see an ~10 percentage-point difference quickly. **Why it fails:** Random arrangement can produce enough estimation error that viewers invert the ordering [@anckerEffectArrangementStick2011].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** A substantial share of users reverses the ordering of two proportions that should be clearly different. **Quick Check:** Run a timed (about 10 seconds) ranking task with the two graphics and measure the reversal rate. **Stronger Test:** Compare reversal rates between random and sequential versions of the same pair to verify the design supports discrimination [@anckerEffectArrangementStick2011].

## Fix: What to do instead <!-- role: fix -->

- Replace random scatter with a sequential (blocked) arrangement for both graphics in the comparison.
- Add explicit percentage labels to each graphic so the comparison does not depend on visual estimation alone.
- Keep array size and layout constant across conditions so viewers can compare like-for-like.
- If randomness is conceptually important, separate the “randomness illustration” from the “proportion comparison” graphic into different views.
