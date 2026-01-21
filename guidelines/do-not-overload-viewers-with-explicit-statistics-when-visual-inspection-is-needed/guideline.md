---
id: do-not-overload-viewers-with-explicit-statistics-when-visual-inspection-is-needed
title: Avoid Showing Many Explicit Statistics at Once
bibliography: references.bib
description: Too many explicit statistical annotations can overwhelm viewers; rely
  on the visualization to support flexible visual estimation instead.
labels:
- chart:general
- task:summarize
- task:identify
- impact:clarity
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Do not display many statistics simultaneously (e.g., min, max, mean, variance, and outliers for every time slice) if the user’s goal is exploratory pattern finding.

## The Logic <!-- role: reason -->

- **The Principle:** Over-annotation increases clutter and cognitive load, while visual estimation preserves flexibility.
- **The Evidence:** The paper illustrates that providing explicit statistics even in visual form can quickly become overwhelming, and argues that visual estimation supports flexible subset selection and pattern discovery [@szafirFourTypesEnsemble2016a].

## Where to Apply <!-- role: context -->

- **User Goal:** Explore data, notice patterns, and choose subsets to inspect (rather than confirm a single pre-defined statistic).
- **Data Type:** Multivariate or time-series displays where many statistics could be attached to each segment.
- **Audience:** Analysts doing exploratory analysis; general readers scanning for main patterns.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When the task is compliance/reporting where a fixed small set of statistics must be read precisely.
- **Reason:** The paper’s critique targets exploratory contexts where too many statistics crowd out pattern perception [@szafirFourTypesEnsemble2016a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Users may not see exact numeric summaries immediately.
- **The Risk:** Without any explicit statistics, some audiences may over-trust rough visual estimates [@szafirFourTypesEnsemble2016a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding every available descriptive statistic as labels, error bars, and callouts across the whole chart.
- **Why it fails:** The display becomes cluttered, undermining rapid ensemble-based judgments and obscuring patterns [@szafirFourTypesEnsemble2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart reads like a wall of annotations; users can’t quickly say what changed or where variability is highest.
- **The Test:** Time-box a viewer to 5 seconds and ask for a high-level takeaway; if they can’t answer, you likely overloaded the display [@szafirFourTypesEnsemble2016a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove all but the one or two most decision-relevant statistics.
- **Best Fix:** Keep the visualization clean for ensemble perception and reveal precise statistics on demand (e.g., only for selected subsets), preserving flexibility [@szafirFourTypesEnsemble2016a].
