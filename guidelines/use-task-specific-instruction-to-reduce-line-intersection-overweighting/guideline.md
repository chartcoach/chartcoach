---
id: use-task-specific-instruction-to-reduce-line-intersection-overweighting
title: "Use task-specific instruction that warns against line\u2013location intersection\
  \ overweighting in ensemble tracks"
bibliography: references.bib
description: Reduce the collocation effect by directly instructing viewers not to
  base judgments on a single line overlapping the point of interest.
labels:
- chart:ensemble-track
- task:assess-risk
- visual:annotation
- impact:accuracy
- data:uncertainty
- audience:novice
- domain:hurricane
---

## Use task-specific instruction that warns against line–location intersection overweighting in ensemble tracks <!-- role: advice -->

If viewers must judge risk at a specific point on an ensemble track map, give task-specific instruction that explicitly tells them not to increase risk solely because one line overlaps the point.

## Targeted debiasing reduces collocation effects more than general explanations <!-- role: reason -->

Viewers can be consciously aware of using “a line hits the point” as a strategy, so instructions that directly name and correct this strategy reduce its influence more than general explanations of how ensembles are generated. However, the visual impact of an intersecting mark remains influential, so the bias may not fully disappear.

**Mechanism:** Task-specific instruction interrupts a deliberate but misguided heuristic (“touching means more likely”) and refocuses attention toward the distribution’s center as the highest-likelihood region.

**Evidence:** Task-specific instructions that explained the collocation effect and included practice reduced the collocation effect more than visualization-only instructions, and both reduced it relative to no instruction [@padillaPowerfulInfluenceMarks2020]. Even with task-specific instruction, the collocation effect was not fully eliminated, showing persistent bottom-up influence of intersecting marks [@padillaPowerfulInfluenceMarks2020].

**Notes:** Participants reported higher confidence after receiving either form of instruction, so confidence gains should not be treated as evidence that the bias is gone [@padillaPowerfulInfluenceMarks2020].

## Context: Decisions that hinge on whether a point is “hit” by any track <!-- role: context -->

- **User Goal:** Decide which of multiple specific locations is at higher risk.
- **Task:** Compare point-specific risk/damage using an ensemble track visualization.
- **Data:** Uncertain paths presented as multiple discrete lines.
- **Chart Setting:** Static, where exact line intersections are perceptually salient.
- **Audience:** Non-experts or mixed audiences, especially those likely to use simple heuristics.
- **Success Criterion:** Risk judgments reflect proximity to the distribution center more than exact intersection with a single line.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The communication setting cannot support instruction (e.g., no captions, no onboarding, extremely limited time). **Why:** The task-specific method depends on the viewer receiving and processing the corrective message [@padillaPowerfulInfluenceMarks2020].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Task-specific instruction takes more time and may feel directive. **Risk:** Increased confidence after instruction can mask remaining bias and encourage overreliance on the visualization. **Mitigation:** Evaluate behavior (e.g., reduced collocation effect) rather than relying on self-reported understanding or confidence [@padillaPowerfulInfluenceMarks2020].

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Providing only generic background about forecast uncertainty without addressing the “line overlaps my location” heuristic. **Why it fails:** General instruction reduces bias less than targeted instruction that directly corrects intersection overweighting [@padillaPowerfulInfluenceMarks2020].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Viewers still strongly prefer the location touched by a line over an equally plausible location not touched. **Quick Check:** Use a small set of paired examples where only the line–point intersection changes and see if responses still shift sharply. **Stronger Test:** Compute the on-line minus off-line judgment difference before and after instruction and confirm a substantial reduction [@padillaPowerfulInfluenceMarks2020].

## Fix: What to do instead <!-- role: fix -->

- Add a short task-focused callout stating that any single line overlap is not meaningful because many unshown paths exist.
- Include one or two practice questions with feedback that reinforce using the center of the track cluster rather than individual intersections.
- Combine task-specific instruction with a moderate increase in the number of plotted tracks to reduce single-line salience.
- If residual bias is unacceptable for the decision, redesign the visualization so point-specific judgments do not hinge on crisp line intersections.
