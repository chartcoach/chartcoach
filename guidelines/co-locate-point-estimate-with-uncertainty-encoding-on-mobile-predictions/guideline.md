---
id: co-locate-point-estimate-with-uncertainty-encoding-on-mobile-predictions
title: Co-locate the point estimate with the uncertainty visualization for mobile
  predictions
bibliography: references.bib
description: Prevent false precision by placing the point prediction inside the same
  visual mark as the uncertainty display.
labels:
- chart:distribution
- task:estimate
- visual:position
- impact:trust
- data:uncertainty
- audience:novice
- platform:mobile
---

## Co-locate point and uncertainty marks <!-- role: advice -->

Place the predicted time (point estimate) directly on top of the uncertainty visualization rather than in a separate column or separate region. Ensure that reading the point estimate necessarily involves looking at the uncertainty depiction in the same area.

## Point-without-uncertainty encourages false precision <!-- role: reason -->

Separating a prominent point estimate from an uncertainty encoding makes it easy for viewers to attend to the single number and ignore the probabilistic information, reinforcing an unjustified sense of precision.

**Mechanism:** Spatial integration increases the chance that users perceive “a prediction with uncertainty” rather than “a precise fact plus optional extra,” reducing the likelihood of discounting uncertainty during quick decisions.

**Evidence:** A key design tension identified was the “glanceability/false precision tradeoff,” and a layout with point predictions placed outside the uncertainty context was rejected because it facilitated ignoring uncertainty; placing the point estimate on the distribution was used to resolve this tension [@kayWhenIshMy2016].

**Notes:** This guideline is about layout and attention, independent of the specific uncertainty encoding (density, dotplot, etc.).

## Mobile realtime prediction lists <!-- role: context -->

- **User Goal:** Decide quickly under time pressure (e.g., whether to leave now, wait, or do a short errand).
- **Task:** Interpret a point prediction while also accounting for early/late risk.
- **Data:** Predictive distributions for arrival times (continuous outcomes with uncertainty).
- **Chart Setting:** Small-screen, list-based interfaces showing multiple upcoming events (e.g., multiple buses).
- **Audience:** Everyday users with limited statistical training.
- **Success Criterion:** Users incorporate uncertainty without losing the ability to skim.

## When not to do this <!-- role: exceptions -->

**Break it when:** The point estimate must be accessible without any graphics (e.g., extreme low-bandwidth or text-only mode). **Why:** The uncertainty visualization may be unavailable, so co-location cannot be guaranteed.

## Tradeoffs of co-location <!-- role: costs -->

**Sacrifice:** Some layout simplicity and potential whitespace; the combined mark may be denser. **Risk:** If the uncertainty encoding is visually complex, the point estimate can become harder to read at a glance. **Mitigation:** Keep the uncertainty mark compact and the point label legible.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Putting the point estimate in a right-aligned number column while showing uncertainty elsewhere. **Why it fails:** Users can make decisions based on the number alone and overlook uncertainty, recreating false precision.

## Quick tests <!-- role: check -->

**Failure Sign:** Users can accurately report the point time but cannot describe whether early arrival is plausible. **Quick Check:** Squint test: if only the big number remains readable, the uncertainty is likely separable and ignorable. **Stronger Test:** Run a short think-aloud with time-pressured scenarios and note whether users reference uncertainty spontaneously.

## What to do instead <!-- role: fix -->

- Overlay the point estimate marker/label directly on the distribution mark.
- Replace a separate “minutes” column with an on-mark label positioned at the distribution’s central tendency.
- If space is tight, reduce the number of other competing numeric elements so the integrated mark remains glanceable.
