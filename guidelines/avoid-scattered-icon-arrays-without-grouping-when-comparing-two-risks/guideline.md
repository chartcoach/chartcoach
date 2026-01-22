---
id: avoid-scattered-icon-arrays-without-grouping-when-comparing-two-risks
title: Avoid scattered icon arrays without a grouping view when comparing two risks
bibliography: references.bib
description: Do not rely on scattered icon arrays alone for two-risk comparisons because
  they reduce knowledge, choices, and perceived quality versus grouped displays.
labels:
- chart:icon-array
- task:compare
- visual:position
- impact:comprehension
- data:risk
- audience:general
- layout:side-by-side
---

## Avoid scattered-only icon arrays for side-by-side risk comparisons <!-- role: advice -->

Avoid presenting risks using icon arrays with event icons scattered across the matrix if viewers must compare two risks side-by-side and no grouped end-state is shown.

## Scattered layouts make magnitude harder to assess in comparisons <!-- role: reason -->

Scattered event icons can convey randomness but make it harder to perceive and compare exact magnitudes, which undermines gist knowledge and downstream choices in a comparative task. This difficulty becomes especially consequential when the difference between risks is small.

**Mechanism:** Random spatial dispersion weakens perceptual grouping, making it harder to rapidly estimate “how many” and compare two arrays, particularly under divided attention.

**Evidence:** In a large randomized experiment, the static scattered condition and several scattered animated conditions (without a clear grouped view) produced lower knowledge accuracy and, for higher-numeracy participants, lower choice accuracy than the static grouped icon-array control; these scattered conditions also received substantially lower graph evaluation ratings [@zikmund-fisherAnimatedGraphicsComparing2012].

**Notes:** The harms were most consistent for scattered displays that did not provide an easy-to-read grouped arrangement.

## Contexts where scattered-only arrays are risky <!-- role: context -->

- **User Goal:** Identify which option is less risky based on side-by-side visuals.
- **Task:** Compare two proportions, including close values (e.g., 14% vs 16%).
- **Data:** Binary outcome risk displayed as part-to-whole.
- **Chart Setting:** Two icon arrays on one screen, viewed quickly (survey/decision aid).
- **Audience:** Mixed numeracy; users may adopt counting strategies.
- **Success Criterion:** Accurate gist judgments and correct selection of the lower-risk option.

## Exceptions where scattered display may be justified <!-- role: exceptions -->

**Break it when:** The communication goal is to foreground perceived randomness or subjective uncertainty rather than accuracy of magnitude comparison. **Why:** Scattered layouts support randomness cues but can impair magnitude reading in comparisons [@zikmund-fisherAnimatedGraphicsComparing2012].

## Costs of avoiding scattered-only arrays <!-- role: costs -->

**Sacrifice:** You may lose a direct visual metaphor for randomness. **Risk:** Users may interpret grouped displays as implying clustering rather than chance distribution. **Mitigation:** Separate the “randomness” message from the “which is larger” comparison task and test both outcomes explicitly.

## Common mistakes with scattered arrays <!-- role: mistakes -->

**Mistake:** Using scattered icons to “look more realistic” while still expecting precise comparison. **Why it fails:** Realism cues can come at the cost of magnitude and comparison accuracy [@zikmund-fisherAnimatedGraphicsComparing2012].

## Quick checks to spot scattered-layout failures <!-- role: check -->

**Failure Sign:** Users say the risks “look similar” even when one is larger, or they cannot answer which option is higher without recounting repeatedly. **Quick Check:** Time-box a comparison question (e.g., 10 seconds) and see if accuracy drops. **Stronger Test:** Compare scattered-only vs grouped displays in an A/B with gist accuracy as the primary outcome [@zikmund-fisherAnimatedGraphicsComparing2012].

## Fixes if you already have a scattered display <!-- role: fix -->

- Add a grouped view as the primary end-state for magnitude reading.
- Replace scattered arrays with grouped arrays for the comparison step.
- Reduce the number of competing visual elements shown simultaneously during comparison.
- Validate with both “which is higher” and “which option should you pick” questions.
