---
id: do-not-assume-bloom-levels-are-dependent
title: Do Not Assume Performance Transfers Across Bloom Levels
bibliography: references.bib
description: Measure each level directly instead of inferring higher-level understanding
  from low-level accuracy.
labels:
- task:evaluate
- impact:validity
- audience:general-public
- custom:blooms-taxonomy
---

## The Rule <!-- role: advice -->

Do not infer higher-level understanding (Analysis/Synthesis/Evaluation) from lower-level accuracy (Knowledge/Application); measure each level explicitly.

## The Logic <!-- role: reason -->

Although Bloom’s taxonomy is often treated as hierarchical, the paper’s case studies found limited dependencies: Knowledge accuracy predicted Application accuracy (both require value estimation), but performance on lower levels did not reliably predict whether higher-level trend descriptions were reasonable. This supports treating levels as complementary rather than strictly dependent in visualization evaluation [@burnsHowEvaluateData2020].

- **The Principle:** Level-independence (partial) in visualization understanding
- **The Evidence:** [@burnsHowEvaluateData2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Evaluate whether a redesign changes conclusions, trend reasoning, predictions, or arguments
- **Data Type:** Any chart where “getting the point” is not guaranteed by accurate point-reading
- **Audience:** Mixed-literacy audiences where different skills may diverge [@burnsHowEvaluateData2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your tasks are intentionally nested (e.g., Application task literally reuses the same values as Knowledge)
- **Reason:** Then some dependency is expected by construction (as the paper observed) [@burnsHowEvaluateData2020]

## The Price <!-- role: costs -->

- **The Sacrifice:** More tasks and more analysis than a single accuracy metric
- **The Risk:** You may find “messy” results (differences at some levels but not others), requiring more nuanced interpretation [@burnsHowEvaluateData2020]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Declaring a visualization “effective” because users can retrieve values correctly
- **Why it fails:** Users may still mischaracterize trends or form unsupported conclusions that only appear at higher levels [@burnsHowEvaluateData2020]

## How to Check <!-- role: check -->

- **Visual Sign:** Your study reports only retrieval accuracy/time and makes claims about “insight” or “reasoning”
- **The Test:** Verify you have at least one direct measure of trend/relationship reasoning and one of evidence-backed judgment [@burnsHowEvaluateData2020]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an Analysis prompt (“how has X changed over time?”) and code for correctness/reasonableness
- **Best Fix:** Implement the full Bloom-level battery and analyze level-by-level differences rather than collapsing into a single score [@burnsHowEvaluateData2020]
