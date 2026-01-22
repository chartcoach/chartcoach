---
id: avoid-too-many-ensemble-tracks-that-imply-completeness
title: Avoid plotting so many ensemble tracks that viewers infer the display shows
  all possible paths
bibliography: references.bib
description: Do not increase ensemble track count beyond the point where viewers start
  believing the display is exhaustive.
labels:
- chart:ensemble-track
- task:assess-risk
- visual:mark-density
- impact:trust
- data:uncertainty
- audience:novice
- domain:hurricane
---

## Avoid plotting so many ensemble tracks that viewers infer the display shows all possible paths <!-- role: advice -->

Do not densify an ensemble track visualization to the point where viewers interpret the plotted lines as an exhaustive set of outcomes.

## Dense marks can trigger an “all outcomes are shown” misconception <!-- role: reason -->

When many tracks are plotted, the ensemble can look complete rather than sampled, encouraging a mistaken belief that the figure contains all possible paths. In this state, viewers may treat absence of a line through a location as meaningful evidence of safety, and they may still overweight line-location intersections.

**Mechanism:** High mark density can shift the mental model from “sample of many possible paths” to “the set of possible paths,” changing how presence/absence of a line is interpreted.

**Evidence:** Participants viewing the 65-track visualization were more likely to report that the forecast “shows all possible paths the hurricane could take” compared to those viewing 9 tracks [@padillaPowerfulInfluenceMarks2020]. Within the 65-track condition, believing the display showed all possible paths was associated with a larger collocation effect than not holding that belief [@padillaPowerfulInfluenceMarks2020].

**Notes:** In this study, the 65-track display reduced collocation bias relative to 9 tracks but increased it relative to 17 and 33 tracks, suggesting a non-monotonic relationship between track count and bias [@padillaPowerfulInfluenceMarks2020].

## Contexts where viewers may interpret ensembles as exhaustive <!-- role: context -->

- **User Goal:** Infer whether a particular location is “in danger” based on shown paths.
- **Task:** Use presence/absence of lines over a point as evidence.
- **Data:** Ensemble paths where only a subset can be displayed.
- **Chart Setting:** Static display without animation showing the full ensemble.
- **Audience:** Non-experts without training on how ensembles are sampled.
- **Success Criterion:** Viewers understand plotted tracks as a subset and do not infer safety from missing intersections.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The communication explicitly intends to show an exhaustive set of modeled outcomes and this is true for the underlying data. **Why:** The “completeness” inference matches the semantics in that special case [@padillaPowerfulInfluenceMarks2020].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Showing fewer tracks can make the ensemble look overly sparse and can increase the influence of any single line. **Risk:** Reducing tracks too far can reintroduce strong collocation bias. **Mitigation:** Balance density to avoid both “single line dominance” and “exhaustive set” misconceptions [@padillaPowerfulInfluenceMarks2020].

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Increasing tracks until the plot looks “fully filled in” without checking what viewers think the lines represent. **Why it fails:** Viewers may infer the set is complete and reason incorrectly from missing or present intersections [@padillaPowerfulInfluenceMarks2020].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** In debriefs or comprehension checks, many viewers answer “yes” to the idea that the display shows all possible paths. **Quick Check:** Add a single comprehension question about whether the plotted tracks are “all possible paths” versus “a subset.” **Stronger Test:** Compare collocation-effect metrics across multiple densities and confirm the densest condition does not worsen the bias relative to a moderate density [@padillaPowerfulInfluenceMarks2020].

## Fix: What to do instead <!-- role: fix -->

- Reduce the number of plotted tracks if viewers infer the display is exhaustive.
- Use a moderate track count that preserves distribution shape without creating an appearance of completeness.
- Add brief explanatory text stating that the shown lines are only a subset of many modeled paths.
- Evaluate multiple track densities with users and select the density that minimizes collocation bias and completeness misconceptions.
