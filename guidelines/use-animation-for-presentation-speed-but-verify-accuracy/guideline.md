---
id: use-animation-for-presentation-speed-but-verify-accuracy
title: Use trend animation for fast presentation only when you can tolerate higher
  viewer error rates
bibliography: references.bib
description: Animated bubble charts can speed presentation viewing but can increase
  mistakes, especially without replay.
labels:
- chart:scatter
- task:present
- visual:motion
- impact:speed
- data:temporal
- audience:general
- usecase:presentation
---

## Use animation to convey trends quickly in presentations when errors are acceptable <!-- role: advice -->

Use animated bubble charts to communicate broad trend direction quickly in a presentation, but do not rely on them when correctness of detailed judgments is critical.

## Why animation is fast but error-prone in presentations <!-- role: reason -->

In a presentation, viewers cannot freely revisit earlier states; animation therefore compresses the time to consume the trend but forces viewers to decide based on fleeting motion that is easy to miss or mis-track.

**Mechanism:** Motion can create a strong global impression rapidly, but transient information and object tracking demands increase missed anomalies and misidentification.

**Evidence:** In presentation mode, animation produced faster completion times than both traces and small multiples [@robertsonEffectivenessAnimationTrend2008]. Across conditions, accuracy was low overall and small multiples was more accurate than animation, indicating animation carries an error risk for these tasks [@robertsonEffectivenessAnimationTrend2008].

**Notes:** Viewers commonly lose track of moving points, which undermines precise identification tasks.

## When this applies in communication settings <!-- role: context -->

- **User Goal:** Understand the general direction of change over time in multivariate data.
- **Task:** Follow overall movement patterns rather than identify many specific outliers.
- **Data:** Many entities moving through a scatterplot over time.
- **Chart Setting:** Talk or guided demonstration where viewers have limited control and limited time per question.
- **Audience:** Mixed expertise, passive viewers.
- **Success Criterion:** Faster comprehension of high-level story beats.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The audience must accurately identify specific entities or subtle anomalies from the display. **Why:** Small multiples produced higher accuracy than animation, and viewers frequently lose track of moving points [@robertsonEffectivenessAnimationTrend2008].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You trade some correctness for speed and excitement. **Risk:** Viewers may miss reversals/counter-trends or confuse entities during motion. **Mitigation:** Pair animation with a static follow-up view for verification.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using animation for tasks that require selecting the correct countries/continents precisely. **Why it fails:** Many viewers cannot reliably track points through motion, leading to errors [@robertsonEffectivenessAnimationTrend2008].
- **Mistake:** Ending the animation and expecting viewers to infer the full trend from the final frame. **Why it fails:** The final state does not preserve the path history needed for many trend questions [@robertsonEffectivenessAnimationTrend2008].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers ask “can you replay that?” or disagree on what moved where. **Quick Check:** After one run, ask for a specific anomaly; if answers scatter widely, add a static alternative. **Stronger Test:** Compare a short audience quiz using animation-only versus animation-plus-static on the same questions.

## What to do instead <!-- role: fix -->

- Add a static traces view immediately after the animation to preserve paths for reference.
- Use small multiples when the presentation requires accurate identification of anomalies across many entities.
- Reduce the number of entities shown if the animated scene becomes hard to track.
- Reframe questions toward high-level movement if the format must remain animation-only.
