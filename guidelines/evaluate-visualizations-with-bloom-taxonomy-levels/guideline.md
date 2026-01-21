---
id: evaluate-visualizations-with-bloom-taxonomy-levels
title: "Evaluate Visualizations Across Bloom\u2019s Six Levels"
bibliography: references.bib
description: Assess a visualization with a structured set of tasks spanning recall,
  interpretation, transfer, reasoning, prediction, and evidence-based judgment.
labels:
- task:evaluate
- impact:clarity
- audience:general-public
- custom:methodology
- custom:blooms-taxonomy
---

## The Rule <!-- role: advice -->

Evaluate a visualization by designing tasks for all six Bloom-derived levels: **Knowledge, Comprehension, Application, Analysis, Synthesis, and Evaluation**, rather than relying only on speed/accuracy value-retrieval tasks.

## The Logic <!-- role: reason -->

Different designs can change what viewers extract, infer, predict, and justify; focusing only on low-level tasks misses these differences. The paper proposes that Bloom’s taxonomy provides a systematic coverage of “levels of understanding” and demonstrates that design differences can appear at some levels but not others (e.g., COVID chart differences emerged at Analysis and Knowledge, but not consistently at Synthesis/Evaluation).

- **The Principle:** Multi-level understanding requires multi-level measurement
- **The Evidence:** [@burnsHowEvaluateData2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Validate whether design choices support not just reading values, but also summarizing, applying, reasoning about trends, predicting, and arguing from data
- **Data Type:** Any (paper demonstrates with economic, demographic, and temporal public-health charts)
- **Audience:** Especially useful for non-expert/public-facing communication and “in the wild” charts [@burnsHowEvaluateData2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only need to test perceptual decoding speed/accuracy of a specific encoding
- **Reason:** A full six-level battery may be unnecessary overhead if the communication goal is strictly perceptual performance [@burnsHowEvaluateData2020]

## The Price <!-- role: costs -->

- **The Sacrifice:** More study design effort than standard retrieval/comparison tasks
- **The Risk:** Open-ended levels (Comprehension/Analysis/Evaluation) require qualitative coding effort and careful operationalization [@burnsHowEvaluateData2020]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating “understanding” as only value lookup or mean comparison
- **Why it fails:** The study shows redesigns can change higher-level interpretations (e.g., trend characterization) even when some lower-level outcomes look similar [@burnsHowEvaluateData2020]

## How to Check <!-- role: check -->

- **Visual Sign:** Your evaluation has only closed-form questions like “What is the value of X?” or “Which is bigger?”
- **The Test:** List your tasks and map each to Bloom levels; if most cluster in Knowledge/Application only, you are not measuring higher-level understanding [@burnsHowEvaluateData2020]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add at least one open-ended prompt for Comprehension (“describe the data”) and one for Analysis (“describe the trend/relationship”)
- **Best Fix:** Add exactly one task per level (six tasks total) as the paper’s minimal, systematic battery [@burnsHowEvaluateData2020]
