---
id: prefer-static-grouped-icon-arrays-for-comparing-two-risks
title: Prefer static grouped icon arrays when comparing two risks side-by-side
bibliography: references.bib
description: Use static grouped icon arrays for two-risk comparisons because they
  yield the best understanding, choices, and ratings versus tested animations and
  scattered layouts.
labels:
- chart:icon-array
- task:compare
- visual:position
- impact:clarity
- data:risk
- audience:general
- medium:screen
---

## Use static grouped icon arrays for side-by-side risk comparison <!-- role: advice -->

Use static icon arrays with event icons grouped into a contiguous block when you need people to compare two risks side-by-side.

## Static grouped arrays reduce distraction and support accurate comparisons <!-- role: reason -->

Static grouped icon arrays keep the display stable and make it easy to judge magnitude, which supports both gist knowledge (which option is riskier) and choice accuracy (selecting the lower-risk option). Adding motion and randomness cues can draw attention away from magnitude comparison, lowering comprehension and preference.

**Mechanism:** A stable, grouped arrangement makes the part-to-whole relationship visually countable and comparable, while minimizing attention capture from motion that competes with the comparison task.

**Evidence:** In a randomized online experiment comparing 10 icon-array formats for two treatments and two side-effect risks, the static grouped condition performed best overall on choice accuracy, gist knowledge accuracy, and evaluation ratings; no animation improved these outcomes versus static grouped displays, and many animations performed worse [@zikmund-fisherAnimatedGraphicsComparing2012].

**Notes:** The tested setting used two simultaneous side-by-side risk displays; the observed disadvantages are tied to that comparative viewing context.

## Contexts that call for static grouped icon arrays <!-- role: context -->

- **User Goal:** Choose the option with the lower overall risk profile when options differ slightly.
- **Task:** Compare two risks (or two options’ risks) presented at the same time.
- **Data:** Two proportions representing adverse event risks (part-to-whole), including small differences.
- **Chart Setting:** Screen-based decision aid or web content showing two icon arrays side-by-side.
- **Audience:** General audiences with varying numeracy and willingness to think carefully.
- **Success Criterion:** Higher choice accuracy, higher gist knowledge accuracy, and higher user ratings of the graphic.

## Exceptions where this rule may not fit the goal <!-- role: exceptions -->

**Break it when:** Your primary goal is to emphasize the randomness/uncertainty of who experiences an outcome rather than to maximize accurate magnitude comparison. **Why:** Grouped static arrays prioritize magnitude readability over randomness cues [@zikmund-fisherAnimatedGraphicsComparing2012].

## Costs of using static grouped arrays <!-- role: costs -->

**Sacrifice:** You give up an immediate visual cue that outcomes are randomly distributed across individuals. **Risk:** Viewers may infer outcomes occur in “blocks” or are less random than they are. **Mitigation:** Treat randomness emphasis as a separate communication goal from magnitude comparison and validate the display against your outcome metrics.

## Common mistakes when applying this guideline <!-- role: mistakes -->

**Mistake:** Adding animation “for engagement” to side-by-side icon arrays that are already understandable. **Why it fails:** The added motion can reduce knowledge accuracy and lower user evaluations without improving choices [@zikmund-fisherAnimatedGraphicsComparing2012].

## Quick checks to confirm the design is working <!-- role: check -->

**Failure Sign:** Users misidentify which option has the higher risk or report low helpfulness despite simple data. **Quick Check:** Ask a small set of users to point to the lower-risk option and explain why, using only the graphic. **Stronger Test:** A/B test static grouped arrays against any enhanced/animated variant using choice accuracy and gist knowledge as primary metrics [@zikmund-fisherAnimatedGraphicsComparing2012].

## Fixes if your current design is not performing well <!-- role: fix -->

- Replace animated or scattered icon arrays with static grouped icon arrays.
- Remove motion cues that compete with side-by-side comparison (especially concurrent animations).
- Present the same risk information in a stable grouped layout for both options to support direct magnitude comparison.
- Validate comprehension with a dominance-choice question and a gist question before shipping.
