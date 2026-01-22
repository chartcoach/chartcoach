---
id: derive-arrival-status-probability-from-annotated-timeline-plus-distribution
title: Encode arrival-status probability by annotating a timeline that the predictive
  distribution spans
bibliography: references.bib
description: Let users infer 'departed/now/on-the-way' probabilities directly from
  the distribution by labeling timeline regions.
labels:
- chart:distribution
- task:infer
- visual:annotation
- impact:clarity
- data:uncertainty
- audience:novice
- platform:mobile
---

## Annotate time regions so status probabilities are readable from the distribution <!-- role: advice -->

Label timeline regions corresponding to meaningful statuses (such as “already departed,” “now,” and “on the way”) so that the probability mass in each region answers status questions. Use the same predictive distribution mark so users can read status probability without a separate widget.

## Status probability can be read as area/count within labeled regions <!-- role: reason -->

If a predictive distribution is plotted against time, status questions become interval-probability questions; labeling the relevant time regions turns this into a direct read-off of probability mass.

**Mechanism:** Annotations create semantic bins on the time axis, allowing users to map probability in those bins to categorical status likelihoods without adding another encoding that competes for space.

**Evidence:** A design goal was supporting “probabilistic estimate of arrival status,” and annotated timelines were used because they communicate “departed/now/on the way” probabilities implicitly “for free” from the same probabilistic prediction display [@kayWhenIshMy2016].

**Notes:** This is compatible with multiple uncertainty encodings (density, low-count dotplots).

## Mobile transit predictions where users doubt whether the bus already arrived <!-- role: context -->

- **User Goal:** Decide whether to keep waiting or switch plans based on the chance a bus has already arrived or is imminent.
- **Task:** Infer categorical status likelihood from a continuous time prediction.
- **Data:** Predictive arrival-time distribution anchored to “now.”
- **Chart Setting:** Timeline-based row layouts in a realtime list.
- **Audience:** Riders who may not trust categorical status labels.
- **Success Criterion:** Users can interpret status probability without extra interaction or separate probability widgets.

## When not to do this <!-- role: exceptions -->

**Break it when:** Your visualization does not include a time axis anchored to the present moment. **Why:** The mapping from distribution mass to status categories depends on those labeled time regions.

## Tradeoffs of timeline status annotations <!-- role: costs -->

**Sacrifice:** Some horizontal space and visual simplicity for labels/markers. **Risk:** Over-annotation can clutter small rows and reduce glanceability. **Mitigation:** Keep region labels minimal and consistent across the entire view.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Showing categorical statuses (e.g., “arriving,” “departed”) without expressing uncertainty. **Why it fails:** Users cannot judge how reliable the status is and may experience confusing failures when categories are wrong.

## Quick tests <!-- role: check -->

**Failure Sign:** Users ask “is it actually coming?” even when the distribution is shown. **Quick Check:** Ask a user for the chance the bus already departed; if they cannot point to a region on the timeline, the annotation is not doing its job. **Stronger Test:** Give scenarios about “already arrived vs. still coming” and measure consistency of answers.

## What to do instead <!-- role: fix -->

- Add a “now” marker and label time regions that correspond to key status categories.
- Replace separate status badges with probability-derived status cues tied to the timeline.
- If labels are too crowded, provide a lightweight legend that explains the regions once per screen.
