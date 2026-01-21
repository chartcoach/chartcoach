---
id: expect-slope-based-cues-to-influence-range-judgments
title: Expect Slope-Based Cues to Influence Range Judgments
bibliography: references.bib
description: Design range comparisons knowing that viewers may rely on slope-like
  patterns across adjacent bars.
labels:
- chart:bar
- task:compare
- visual:shape
- visual:position
- impact:clarity
- data:categorical
- audience:general
- concept:perceptual-proxies
---

## The Rule <!-- role: advice -->

When the goal is to compare ranges, do not assume viewers will read range as max–min; check whether slope-like patterns across bars are biasing judgments.

## The Logic <!-- role: reason -->

For the MaxRange task, the paper reports slope-related proxies as influential in their modeling: participants showed patterns consistent with relying on slope-like cues, including cases where manipulating a slope proxy produced “selecting against” effects (interpreted as proxy conflicts with negatively correlated alternatives) [@ondovRevealingPerceptualProxies2021]. This indicates viewers may use trends/adjacent differences (slopes) instead of explicitly comparing the extremes.

- **The Principle:** Trend/gradient heuristic (slope as a proxy competing with true range)
- **The Evidence:** Slope proxies were central in MaxRange results and interpretation of proxy conflicts [@ondovRevealingPerceptualProxies2021].

## Where to Apply <!-- role: context -->

- **User Goal:** Choosing which series has a larger range from bar charts
- **Data Type:** Ordered bars (where adjacency creates perceived slopes), shown side-by-side
- **Audience:** General audiences; especially under quick viewing (1500ms impressions) [@ondovRevealingPerceptualProxies2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is explicitly about trend/shape (e.g., “which series rises fastest?”).
- **Reason:** Then slope cues are the intended signal.

## The Price <!-- role: costs -->

- **The Sacrifice:** Reducing slope salience may make charts less readable for trend-related questions.
- **The Risk:** If you dampen slope cues, you may hide meaningful local variation patterns.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating slope effects as “noise” without considering proxy conflicts.
- **Why it fails:** The paper shows that a manipulated proxy can appear to have the opposite effect when viewers use a different, negatively correlated proxy [@ondovRevealingPerceptualProxies2021].

## How to Check <!-- role: check -->

- **Visual Sign:** A chart with a smaller true range nevertheless looks more “dramatic” due to steep adjacent changes or strong min-to-max slope motifs.
- **The Test:** Compare two charts with matched ranges (or known ranges) and see whether perceived range tracks steepness rather than extremes, using a brief glance test [@ondovRevealingPerceptualProxies2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Make extrema more directly comparable (visually emphasize max and min together) so slope patterns are less likely to substitute for range.
- **Best Fix:** Run an adversarial check: generate or search for cases where slope cues disagree with true range and verify your design still supports correct range judgments across viewers [@ondovRevealingPerceptualProxies2021].
