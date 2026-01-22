---
id: avoid-stripeplot-like-discrete-gradients-for-static-mobile-uncertainty
title: Avoid stripeplot-style discrete gradients for static probability estimation
  on mobile
bibliography: references.bib
description: Stripe-based discrete gradients produce less precise probability estimates
  than low-count dotplots and density plots in transit prediction tasks.
labels:
- chart:distribution
- task:estimate
- visual:density
- impact:accuracy
- data:uncertainty
- audience:novice
- platform:mobile
---

## Do not use stripeplot encodings for threshold probability questions <!-- role: advice -->

If users must estimate the chance of arriving before a specified time from a static mobile visualization, avoid stripeplot-style encodings. Prefer a low-count quantile dotplot or a density plot instead.

## Stripe density is hard to read precisely in small static displays <!-- role: reason -->

Stripeplots behave like a discrete analog of gradients, and the visual system may not support precise estimation from stripe density in compact, static contexts.

**Mechanism:** When discrete marks are too numerous or visually blend into a continuous texture, users are more likely to rely on imprecise density/area heuristics rather than count-based reasoning.

**Evidence:** In the experiment comparing four encodings (density, stripeplot-50, dotplot-20, dotplot-100) for realtime transit prediction scenarios, stripeplot had the highest variance (least precise probability estimates) and was also rated lowest in ease of use [@kayWhenIshMy2016].

**Notes:** This guidance is specific to static, small-screen probability estimation tasks; it does not address other tasks (e.g., communicating “some uncertainty exists” without requiring numeric probability estimates).

## Static mobile displays requiring probability extraction <!-- role: context -->

- **User Goal:** Make a time-critical decision based on likelihood (e.g., coffee vs. catch the bus).
- **Task:** Estimate probability of arrival before a threshold or within an interval.
- **Data:** Predictive distributions for arrival time.
- **Chart Setting:** Small rows in a multi-item list; limited vertical resolution; static marks.
- **Audience:** Non-experts interpreting probability without training.
- **Success Criterion:** Lower variance in estimated probabilities and usable subjective workload.

## When not to do this <!-- role: exceptions -->

**Break it when:** The goal is a qualitative cue of “more/less uncertain” rather than estimating specific probabilities. **Why:** Stripe texture may still convey a rough sense of spread without supporting precise numeric extraction.

## Tradeoffs of avoiding stripeplots <!-- role: costs -->

**Sacrifice:** You give up an encoding that resembles gradient-style uncertainty and may feel visually lightweight. **Risk:** Replacing stripes with dots can increase visual busyness. **Mitigation:** Keep dot counts low and align the design to common list-row constraints.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using stripe density and expecting users to infer tail probabilities accurately. **Why it fails:** Users’ estimates become more variable, undermining decision consistency.

## Quick tests <!-- role: check -->

**Failure Sign:** Users’ threshold probability answers differ widely for the same underlying distribution. **Quick Check:** Ask multiple users for the chance of arriving before a time and look for large spread in responses. **Stronger Test:** Run an internal replication of the probability estimation task and compute response variance across encodings.

## What to do instead <!-- role: fix -->

- Use a low-count quantile dotplot to support counting-based interval estimation.
- Use a density plot when visual appeal is prioritized and slightly higher variance is acceptable.
- Add brief per-encoding tutorials if you introduce an unfamiliar representation.
