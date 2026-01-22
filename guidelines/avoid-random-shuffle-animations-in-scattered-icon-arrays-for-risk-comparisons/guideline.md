---
id: avoid-random-shuffle-animations-in-scattered-icon-arrays-for-risk-comparisons
title: Avoid random shuffling animations in scattered icon arrays for risk comparisons
bibliography: references.bib
description: Do not animate scattered icon arrays with repeated shuffling because
  it lowers comprehension and user ratings in two-risk comparisons.
labels:
- chart:icon-array
- task:compare
- visual:motion
- impact:comprehension
- data:risk
- audience:general
- animation:shuffle
---

## Avoid shuffling scattered risk icons during side-by-side comparisons <!-- role: advice -->

Avoid animations that repeatedly reshuffle scattered risk icons (whether automatic or user-triggered) when people must compare two risks on screen.

## Shuffling adds motion noise that competes with comparison <!-- role: reason -->

Repeated shuffling creates continual motion that can capture attention and introduce instability, making it harder to extract and compare risk magnitudes across options. It can also reduce trust and satisfaction with the graphic.

**Mechanism:** Ongoing motion and spatial re-randomization increases cognitive load and disrupts any counting or pattern-based estimation strategy, especially when two moving displays must be compared at once.

**Evidence:** In an experiment with 8 animated variants, conditions that included shuffling of scattered icons had substantially lower evaluation ratings than static grouped displays, and several shuffle conditions showed worse knowledge and/or choice accuracy than the static grouped control (notably without consistent benefits in any measured outcome) [@zikmund-fisherAnimatedGraphicsComparing2012].

**Notes:** User-controlled shuffling did not resolve the performance and preference problems observed with shuffling in this comparative context.

## Contexts where shuffling is especially harmful <!-- role: context -->

- **User Goal:** Decide which of two options has lower risk.
- **Task:** Side-by-side comparison under limited attention.
- **Data:** Small risk differences where precision matters.
- **Chart Setting:** Two simultaneous icon arrays (e.g., treatment A vs B).
- **Audience:** Mixed numeracy; some users rely on counting.
- **Success Criterion:** Maintain knowledge accuracy and avoid lowering user-rated helpfulness.

## Exceptions to consider <!-- role: exceptions -->

**Break it when:** You are deliberately measuring or eliciting subjective uncertainty rather than comprehension or choice accuracy. **Why:** Shuffling emphasizes variability/randomness cues that can conflict with magnitude extraction [@zikmund-fisherAnimatedGraphicsComparing2012].

## Costs of removing shuffling <!-- role: costs -->

**Sacrifice:** You lose a strong visual cue intended to communicate randomness. **Risk:** Viewers may underestimate uncertainty if no other uncertainty cue is provided. **Mitigation:** Treat uncertainty communication as a separate design element and test it explicitly.

## Common mistakes with shuffle animations <!-- role: mistakes -->

- **Mistake:** Keeping the shuffle running while asking users to compare two options. **Why it fails:** Continual motion competes with the comparison task and depresses ratings and accuracy [@zikmund-fisherAnimatedGraphicsComparing2012].
- **Mistake:** Adding a “shuffle” button to make users feel in control. **Why it fails:** User-triggered shuffling still produced poor outcomes relative to the static grouped control in this setting [@zikmund-fisherAnimatedGraphicsComparing2012].

## Quick checks for shuffle-driven degradation <!-- role: check -->

**Failure Sign:** Users describe the display as distracting or unhelpful, or accuracy drops among otherwise high-performing users. **Quick Check:** Turn off the shuffle and retest the same questions; if accuracy and ratings rise, the motion is harming performance. **Stronger Test:** Run an A/B where the only difference is shuffle vs no-shuffle and compare gist knowledge and graphic evaluation [@zikmund-fisherAnimatedGraphicsComparing2012].

## Fixes if you need to communicate randomness without shuffling <!-- role: fix -->

- Remove repeated shuffling during the comparison step and show a stable grouped view for reading magnitude.
- Use a non-moving scattered snapshot only as a brief, optional precursor to a stable grouped display.
- Separate the randomness explanation from the magnitude comparison (e.g., a short caption plus a stable graphic).
- Measure whether your intended uncertainty message improves without reducing choice and knowledge accuracy.
