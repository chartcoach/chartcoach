---
id: evaluate-decision-justification-with-evaluation-level-policy-argument
title: Evaluate decision support by asking for a policy recommendation and a data-based
  justification
bibliography: references.bib
description: Test whether a visualization supports evidence-based decisions by eliciting
  an argument grounded in the displayed data.
labels:
- chart:general
- task:justify
- visual:general
- impact:trust
- data:general
- audience:general
- method:user-study
---

## Ask for a recommendation and require evidence from the chart <!-- role: advice -->

Use an evaluation-level prompt that asks participants to propose a decision (such as a policy change) and to justify it using evidence from the visualization.

## Why justification tasks test evidence selection, not just reading <!-- role: reason -->

A visualization may permit accurate reading yet still encourage weak or biased arguments if viewers select misleading evidence or ignore critical structure. A justification prompt reveals what evidence viewers treat as decisive and whether different designs change the arguments people feel licensed to make.

**Mechanism:** Evaluation prompts force a judgment plus a rationale, exposing the mapping from visual impressions to real-world claims and the evidence features chosen to support those claims.

**Evidence:** Participants often produced the same policy conclusion and cited similar evidence across original and redesigned charts even when the designs differed in the patterns they made salient at other levels, showing that high-level decisions can diverge from low-level decoding differences [@burnsHowEvaluateData2020]. The method operationalized evaluation as evidence-backed argumentation rather than as rating the visualization itself, aligning measurement with understanding of the underlying data [@burnsHowEvaluateData2020].

**Notes:** This level can be scored by coding which conclusions and evidence types appear in responses.

## When to use evidence-backed recommendation prompts <!-- role: context -->

- **User Goal:** Determine what decisions a visualization supports or encourages.
- **Task:** Recommend an action and cite supporting evidence from the displayed data.
- **Data:** Real-world topics where viewers could form arguments (public health, economics, demographics).
- **Chart Setting:** Communication-focused visualizations used in reports, news, or policy contexts.
- **Audience:** Non-expert readers who may form decisions quickly from visual impressions.
- **Success Criterion:** Appropriateness and diversity of evidence cited; differences in arguments across designs.

## When not to use this evaluation approach <!-- role: exceptions -->

**Break it when:** Your study goal is to assess the visualization’s encoding quality directly (e.g., legibility, aesthetics) rather than data-driven reasoning. **Why:** A recommendation task measures downstream decision behavior, not perceived design quality.

## Tradeoffs of policy-argument evaluation <!-- role: costs -->

**Sacrifice:** Responses can be influenced by participant beliefs and biases independent of the chart. **Risk:** Conclusions may converge across designs even if other understanding measures differ, reducing sensitivity. **Mitigation:** Treat this as a complement to lower-level tasks rather than a replacement.

## Common mistakes in evaluation-level prompts <!-- role: mistakes -->

**Mistake:** Asking for a recommendation without requiring evidence from the chart. **Why it fails:** It measures opinion more than chart-supported reasoning.

## Quick checks for evidence-based argument quality <!-- role: check -->

**Failure Sign:** Participants make strong recommendations but cite no concrete feature of the data (no referenced trend, comparison, or magnitude).\
**Quick Check:** Verify the prompt explicitly asks “what evidence would you provide.”\
**Stronger Test:** Code both the conclusion type and the evidence type, then compare their frequencies across designs.

## What to do instead if arguments are dominated by prior beliefs <!-- role: fix -->

- Ask participants to justify a provided conclusion rather than generating their own conclusion.
- Constrain the decision context (e.g., “based only on this chart”) to focus attention on chart evidence.
- Pair the evaluation prompt with an analysis prompt about a specific trend to anchor responses.
- Compare evidence-citation patterns across designs rather than trying to judge “correctness” of the recommendation.
