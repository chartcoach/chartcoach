---
id: collect-about-10-to-15-bubbleview-participants-per-image-for-stable-importance-maps
title: "Collect about 10\u201315 BubbleView participants per image for stable aggregate\
  \ maps"
bibliography: references.bib
description: "Use roughly 10\u201315 participants per image to capture most of the\
  \ achievable click-to-fixation similarity while controlling cost."
labels:
- chart:other
- task:study-design
- visual:attention
- impact:efficiency
- data:experimental
- audience:researcher
- method:bubbleview
---

## Target ~10–15 participants per image for aggregation <!-- role: advice -->

Recruit roughly 10–15 BubbleView participants per image to obtain stable aggregate click maps for fixation approximation or importance estimation.

## Why modest sample sizes saturate performance quickly <!-- role: reason -->

Aggregating clicks across participants rapidly reduces individual noise and produces a stable density map; beyond a moderate number of participants, additional clicks provide diminishing returns in similarity to fixation distributions.

**Mechanism:** Averaging across independent observers suppresses idiosyncratic click choices and highlights consistently inspected regions; the marginal value of additional observers decreases as the aggregate map stabilizes.

**Evidence:** On information visualizations, 10–15 participants achieved about 97–98% of the extrapolated performance limit for predicting fixation locations, with little gain beyond that range [@kimBubbleViewInterfaceCrowdsourcing2017]. Similar results showed that even for natural images and webpages, small cohorts already accounted for a substantial fraction of fixations [@kimBubbleViewInterfaceCrowdsourcing2017].

**Notes:** “Enough” depends on image complexity and task constraints, but the paper’s experiments repeatedly used this range as a practical default.

## When this participant target applies <!-- role: context -->

- **User Goal:** Balance cost and data quality in a BubbleView study.
- **Task:** Build per-image aggregate click/importance maps for comparison, modeling, or ranking.
- **Data:** Static images where you will aggregate clicks across participants.
- **Chart Setting:** Crowdsourcing with per-image budgets and many images.
- **Audience:** Typical online participants; heterogeneous devices and environments.
- **Success Criterion:** Aggregate maps converge (small changes when adding more participants).

## When this target might be insufficient <!-- role: exceptions -->

**Break it when:** Your images produce highly variable viewing behavior across people (low inter-observer consistency) or you need fine-grained element estimates. **Why:** More participants may be required to average out variability and stabilize rankings [@kimBubbleViewInterfaceCrowdsourcing2017].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Increasing participants raises cost linearly. **Risk:** Using too few participants can yield unstable maps that reflect noise or individual strategies. **Mitigation:** Pilot on a subset and measure how similarity or stability changes as you add participants [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Fixing participant count without checking convergence on your stimulus type. **Why it fails:** Different image types and tasks can have different consistency and may saturate at different rates [@kimBubbleViewInterfaceCrowdsourcing2017].

## Quick tests <!-- role: check -->

**Failure Sign:** Adding a few more participants changes the hotspot structure or element ranking substantially. **Quick Check:** Recompute maps with random subsets (e.g., 5 vs. 10 vs. 15 participants) and visually compare hotspot stability. **Stronger Test:** Plot a fixation-prediction-style score (or another stability metric) as a function of participant count and look for saturation [@kimBubbleViewInterfaceCrowdsourcing2017].

## What to do instead <!-- role: fix -->

- Increase the participant count for image types with low consistency or when rankings are unstable.
- Use a more defined task (e.g., description) if you cannot recruit many participants but need cleaner clicks.
- Increase per-image viewing time on dense layouts to reduce sparsity in clicks.
- Reduce the number of images per participant session to maintain attention and data quality [@kimBubbleViewInterfaceCrowdsourcing2017].
