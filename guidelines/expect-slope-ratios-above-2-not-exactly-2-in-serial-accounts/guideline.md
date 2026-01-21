---
id: expect-slope-ratios-above-2-not-exactly-2-in-serial-accounts
title: Do Not Treat a 2:1 Slope Ratio as the Default Benchmark
bibliography: references.bib
description: Do not assume the target-absent slope is exactly twice the target-present
  slope; observed ratios are typically greater than 2 and vary with task and efficiency.
labels:
- chart:scatter
- task:validate
- visual:position
- impact:validity
- data:experimental
- audience:expert
- domain:visual-search
---

## The Rule <!-- role: advice -->

Do not use an exact 2:1 target-absent:target-present slope ratio as the default “serial self-terminating” benchmark when interpreting RT×set-size data.

## The Logic <!-- role: reason -->

Across a very large dataset, mean slope ratios are significantly greater than 2.0, and the absent-vs-present relationship includes a positive intercept. This indicates that a simple serial self-terminating account (implying a clean 2:1 through-origin relation) is not generally adequate as a benchmark.

- **The Principle:** Use empirically supported benchmarks; theoretical simplifications can systematically bias interpretation.
- **The Evidence:** The paper reports mean ratios > 2.0, a regression slope ~2.0 with positive intercept, and systematic ratio variation with task and efficiency [@wolfeWhatCan11998].

## Where to Apply <!-- role: context -->

- **User Goal:** Interpreting whether data are consistent with a simple serial self-terminating search story.
- **Data Type:** Present/absent slopes derived from multiple set sizes.
- **Audience:** Researchers comparing observed patterns to canonical “serial” predictions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are teaching the classic heuristic as a historical approximation and explicitly note it is not an empirical law.
- **Reason:** The paper challenges its general validity, not its pedagogical existence [@wolfeWhatCan11998].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less tidy model-to-data matching and fewer “textbook” interpretations.
- **The Risk:** Without careful benchmarks, readers may find interpretation less intuitive.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Declaring “serial self-terminating” whenever ratio ≈ 2.
- **Why it fails:** Ratios can exceed 2 systematically and differ by task; matching 2 does not uniquely identify a mechanism [@wolfeWhatCan11998].

## How to Check <!-- role: check -->

- **Visual Sign:** A plot or write-up that treats deviation from 2.0 as “noise” rather than a systematic pattern.
- **The Test:** Examine whether the absent-vs-present regression includes a non-zero intercept and whether ratios vary with efficiency/task in your data.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Report observed ratio distributions and confidence intervals instead of comparing only to 2.0.
- **Best Fix:** Compare your data to empirical benchmarks by task type/efficiency and model the absent/present relationship with an intercept, consistent with the paper’s findings [@wolfeWhatCan11998].
