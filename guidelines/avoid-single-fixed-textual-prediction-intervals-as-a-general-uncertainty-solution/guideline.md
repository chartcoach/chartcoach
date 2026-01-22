---
id: avoid-single-fixed-textual-prediction-intervals-as-a-general-uncertainty-solution
title: Avoid relying on a single fixed textual prediction interval as the only uncertainty
  display
bibliography: references.bib
description: Single-threshold textual uncertainty can be highly sensitive to the chosen
  probability level and may not support consistent decisions across contexts.
labels:
- chart:text
- task:decide
- visual:text
- impact:robustness
- data:uncertainty
- audience:novice
- domain:transit
- complexity:basic
---

## Avoid relying on a single fixed textual prediction interval as the only uncertainty display <!-- role: advice -->

Do not use just one textual one-sided prediction interval (for example, “X% chance the bus arrives in Y minutes or later”) as the sole uncertainty communication when user priorities and costs vary. Prefer displays that let users adapt to different risk tolerances without changing the representation.

## Why fixed textual thresholds can be brittle <!-- role: reason -->

A single probability level compresses the distribution into one number, which limits flexibility when the optimal decision threshold changes across scenarios. If the displayed level does not match the decision’s implied risk tradeoff, users may learn an ineffective heuristic and fail to improve with experience.

**Mechanism:** Low expressiveness prevents users from selecting the probability cutoff appropriate to the cost of waiting versus missing; the interface bakes in a risk level that may be misaligned with the situation.

**Evidence:** In a repeated, incentivized bus-catching study, textual uncertainty performance depended strongly on the probability level shown: some text intervals approached dotplot performance while another (an 85% interval) showed poor decisions and little learning, comparable to no-uncertainty control behavior [@fernandesUncertaintyDisplaysUsing2018].

**Notes:** The sensitivity implies no single textual interval level is reliably best across contexts.

## When the “avoid fixed textual intervals” rule applies <!-- role: context -->

- **User Goal:** Make a timing decision under uncertainty with varying penalties for waiting or missing.
- **Task:** Adjust risk-taking based on context (important meeting vs casual plan) without changing UI settings.
- **Data:** Arrival-time uncertainty where different probability cutoffs could be rational in different scenarios.
- **Chart Setting:** Product UI intended to work across many users and situations, not a single standardized policy.
- **Audience:** General population with diverse risk tolerances.
- **Success Criterion:** Stable decision quality across scenarios without requiring per-scenario UI redesign.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** The organization mandates a single operational risk policy (a fixed “service guarantee” probability) and users are expected to follow that policy rather than optimize personal utility. **Why:** In that case, a single threshold is the intended decision rule.

## Tradeoffs and risks of avoiding fixed textual intervals <!-- role: costs -->

**Sacrifice:** More complex visual or interactive elements than a short sentence. **Risk:** Overcorrecting by adding too much detail can reduce glanceability in mobile contexts. **Mitigation:** Choose compact distribution displays that still support quick reading.

## Common mistakes with textual uncertainty intervals <!-- role: mistakes -->

- **Mistake:** Treating one probability level as universally appropriate for all riders and situations. **Why it fails:** Optimal risk thresholds vary with the costs of waiting and missing.
- **Mistake:** Swapping one interval level for another after negative feedback without adding flexibility. **Why it fails:** Another context will still be mismatched, recreating the brittleness.

## Quick tests for brittleness in textual intervals <!-- role: check -->

**Failure Sign:** Decision quality differs sharply when the same text pattern is used with different probability levels, or learning plateaus despite feedback. **Quick Check:** Test at least two cost scenarios and see whether the same textual threshold supports near-optimal choices in both. **Stronger Test:** Compare repeated-trial learning curves against a distribution display using expected/optimal payoff.

## What to do instead of a single textual interval <!-- role: fix -->

- Use a quantile dotplot (for example, ~50 dots) to let users infer different probability thresholds by counting.
- Use a CCDF plot to make the “still catch it if I arrive at time X” probability readable for any chosen time.
- If text is required, provide more than one probability reference point (so users can adapt), rather than only one.
- Provide outcome feedback over repeated use so users can calibrate how they act on uncertainty.
