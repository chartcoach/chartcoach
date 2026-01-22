---
id: prefer-scatter-like-dot-encodings-over-text-or-two-group-summaries-to-reduce-causal-interpretations
title: Prefer scatter-style dot displays over text or coarse two-group summaries when
  you want to avoid causal interpretations
bibliography: references.bib
description: Scatter-like displays reduce causal interpretations relative to text
  and coarse summary presentations of the same relationship.
labels:
- chart:scatter
- chart:bar
- chart:text
- task:interpret
- visual:mark
- impact:trust
- data:correlational
- audience:novice
- custom:causality
---

## Use scatter-style presentations to dampen causal readings <!-- role: advice -->

Use a scatter-style dot display rather than a text description or a coarse two-group summary when presenting correlational evidence without causal support. Keep the presentation focused on observed association rather than “high versus low” grouped comparisons.

## Why scatter-style views reduce causal interpretation <!-- role: reason -->

Scatter-style displays can make the relationship feel like a set of observations rather than a comparison of conditions, which can reduce the tendency to treat one variable as an intervention producing the other. Coarse summaries and textual restatements can encourage viewers to form a simple narrative that more directly maps to causal language.

**Mechanism:** Showing many individual points makes variability and non-determinism salient, reducing the plausibility of a single causal story.

**Evidence:** In a context-rich setting, participants gave higher causation agreement ratings for text and bar-chart summaries than for scatter plots, even though the underlying relationship was the same. [@xiongIllusionCausalityVisualized2020]

**Notes:** The same study found that viewers still correctly recognized the presence of correlation across formats, so reducing causal interpretation did not require hiding the association entirely.

## When to apply scatter-style dot displays <!-- role: context -->

- **User Goal:** Communicate “these variables move together” while discouraging “X causes Y.”
- **Task:** Judge/interpret claims about what the data support.
- **Data:** Two-variable observational relationship with moderate correlation.
- **Chart Setting:** Explanatory graphics in media, education, or stakeholder updates where causal claims are tempting.
- **Audience:** Viewers likely to default to causal storytelling from patterns.
- **Success Criterion:** Maintain recognition of correlation while lowering agreement with causal statements.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The purpose is to communicate an explicitly grouped comparison as the primary message. **Why:** Scatter-style displays can make group differences less immediate than a grouped summary.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Scatter-style displays can be harder to read precisely and may feel less “summary-like.” **Risk:** Some audiences may find point clouds visually busy and disengage. **Mitigation:** Keep axes and labels simple and avoid unnecessary clutter.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Presenting the same coarse summary as prose (“when X is high, Y is high”) and assuming it is neutral. **Why it fails:** Textual summaries were associated with higher causal agreement than scatter plots for the same relationship.
- **Mistake:** Using a scatter plot but then describing it with counterfactual/intervention language in accompanying copy. **Why it fails:** Viewers’ judgments were collected directly against causal statements, showing that language can steer interpretation even when data are correlational.

## Quick tests <!-- role: check -->

**Failure Sign:** Readers paraphrase the graphic as a policy lever (“increase X to increase Y”). **Quick Check:** Replace the summary with a scatter-style view and see if paraphrases become more associative (“tends to,” “is related”). **Stronger Test:** Compare causal agreement ratings for a scatter-style version versus a grouped-summary version in a small pilot.

## What to do instead <!-- role: fix -->

- Switch from a coarse grouped summary to a scatter-style dot display showing individual observations.
- Remove or reduce explicit “high vs low” grouping language in captions when causality is not supported.
- Add a second view that reveals variability if a summary view must be shown for space reasons.
- Reframe the accompanying statement to describe association rather than an intervention claim.
