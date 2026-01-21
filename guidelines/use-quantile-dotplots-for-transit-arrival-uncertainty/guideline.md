---
id: use-quantile-dotplots-for-transit-arrival-uncertainty
title: Use Quantile Dotplots to Show Transit Arrival Uncertainty
bibliography: references.bib
description: Prefer quantile dotplots (especially ~50 dots) over point-only or other
  common uncertainty displays to support better bus-catching decisions.
labels:
- chart:dotplot
- task:decide
- visual:position
- impact:decision-quality
- data:temporal
- audience:novice
- domain:transit
---

## The Rule <!-- role: advice -->

Show bus-arrival uncertainty with a low-density quantile dotplot (prefer ~50 dots) instead of only a point estimate or other common uncertainty encodings.

## The Logic <!-- role: reason -->

Quantile dotplots frame probability as countable outcomes, which supports more accurate and consistent choices in a bus-catching decision task compared to no-uncertainty (point-only) and several alternative uncertainty displays. In a controlled, incentivized experiment, dotplots with 50 outcomes achieved near-optimal expected payoff and reduced variability across decisions [@fernandesUncertaintyDisplaysUsing2018].

- **The Principle:** Frequency-based probability framing (counting outcomes supports reasoning).
- **The Evidence:** Dot50 decisions reached ~97% of optimal expected payoff and had lower within-subject variability than control [@fernandesUncertaintyDisplaysUsing2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide when to leave/arrive to catch a bus while balancing waiting time vs. risk of missing.
- **Data Type:** Predictive distribution over arrival time (uncertain time-to-event).
- **Audience:** General public / non-expert transit riders on mobile.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot allocate enough screen space to render discrete dots legibly (e.g., extreme mini-sparkline constraints).
- **Reason:** The display may become unreadable and undermine the counting-based advantage described in the paper’s framing [@fernandesUncertaintyDisplaysUsing2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** More visual complexity than a single time label.
- **The Risk:** If dots are too dense or too small, users may stop interpreting them as discrete outcomes and the benefit may erode [@fernandesUncertaintyDisplaysUsing2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Replacing dotplots with a PDF curve because it “looks statistical.”
- **Why it fails:** In the experiment, PDFs underperformed dotplots and CDF-style displays on decision quality and/or consistency [@fernandesUncertaintyDisplaysUsing2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Dots visually merge into a solid mass, or users can’t plausibly count/approximate proportions at a glance.
- **The Test:** Shrink to intended mobile size and verify individual dots remain visually distinct (not forming a continuous blob).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce dot count or increase dot spacing so outcomes remain discrete.
- **Best Fix:** Use a quantile dotplot tuned for glanceability (the paper’s best-performing example used ~50 dots) [@fernandesUncertaintyDisplaysUsing2018].
