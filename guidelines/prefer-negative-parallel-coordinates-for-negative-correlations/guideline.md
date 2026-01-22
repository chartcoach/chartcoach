---
id: prefer-negative-parallel-coordinates-for-negative-correlations
title: Prefer parallel coordinates plots when your correlations are predominantly
  negative
bibliography: references.bib
description: Parallel coordinates can match scatterplot-level precision for negative
  correlations but perform worse for positive correlations.
labels:
- chart:parallel-coordinates
- task:compare
- visual:orientation
- impact:accuracy
- data:multivariate
- audience:practitioner
- direction:negative-correlation
---

## Use parallel coordinates preferentially for negative correlations, not positive ones <!-- role: advice -->

Use a parallel coordinates plot when you expect predominantly negative correlations and viewers must discriminate correlation strength; avoid relying on it for positive correlations without validation.

## Why parallel coordinates are sign-asymmetric for correlation discrimination <!-- role: reason -->

Parallel coordinates change their line intersection structure dramatically with correlation sign, which can amplify cues for negative correlation while weakening cues for positive correlation. This can lead to substantially different discrimination thresholds (JNDs) between signs for the same visualization.

**Mechanism:** Strong intersection patterns can create a salient perceptual cue for “more negatively correlated,” reducing JND, while more parallel structures for positive correlation can reduce distinctiveness and increase JND.

**Evidence:** Parallel coordinates plots showed a significant asymmetry: negative correlations were discriminated more precisely than positive correlations, and negative parallel coordinates were not significantly different from scatterplots in JND performance [@harrisonRankingVisualizationsCorrelation2014a]. Positive parallel coordinates were significantly worse than scatterplots in the tested discrimination task [@harrisonRankingVisualizationsCorrelation2014a].

**Notes:** This advice targets correlation discrimination precision and assumes the parallel coordinates plot is used specifically to judge correlation between two dimensions.

## When this parallel-coordinates choice applies <!-- role: context -->

- **User Goal:** Compare or rank correlation strength when relationships are mostly negative.
- **Task:** Decide which of two relationships is more correlated (more negative).
- **Data:** At least two quantitative dimensions; focus on a pairwise correlation impression.
- **Chart Setting:** Static or lightly interactive parallel coordinates in a limited pixel area.
- **Audience:** Mixed expertise; needs strong perceptual cues.
- **Success Criterion:** Low JND for negative correlations; avoid chance-boundary behavior.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** Your relationships are primarily positive or mixed-sign and you cannot separate sign-specific encodings. **Why:** The paper shows positive parallel coordinates can be much less precise for correlation discrimination.

## Tradeoffs of using parallel coordinates for negative correlations <!-- role: costs -->

**Sacrifice:** You may need additional handling when the sign flips (for example, different layouts or a different chart choice). **Risk:** Users may misinterpret the visual cue if they are not expecting sign-dependent structure. **Mitigation:** Keep sign cues consistent within the product and avoid mixing sign conditions without clear context.

## Common mistakes with parallel coordinates for correlation <!-- role: mistakes -->

- **Mistake:** Treating parallel coordinates as interchangeable with scatterplots for positive correlations. **Why it fails:** The paper shows significantly worse JND performance for positive correlations.
- **Mistake:** Using a single evaluation/model for parallel coordinates across both signs. **Why it fails:** Sign asymmetry is strong enough to require separate assessment.

## Quick checks for this decision <!-- role: check -->

**Failure Sign:** Users struggle to tell “more correlated” for positive relationships in parallel coordinates but do better for negative ones. **Quick Check:** Compare predicted JND from the positive vs negative Weber models for parallel coordinates at your r range. **Stronger Test:** Run a small forced-choice discrimination test for both signs using your styling and data characteristics.

## What to do instead if you must show positive correlations in parallel coordinates <!-- role: fix -->

- Switch to a scatterplot for the positive-correlation comparison tasks.
- Separate positive and negative relationships into different views and use the more precise chart per sign.
- If you cannot switch chart types, limit claims to coarse distinctions where the predicted JND is acceptably small.
- Avoid using the chart for fine ranking tasks when predicted JND is high.
