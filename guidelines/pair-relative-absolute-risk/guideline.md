---
id: pair-relative-absolute-risk
title: Pair Relative Changes with Absolute Baselines
bibliography: references.bib
description: Display absolute risk reduction alongside relative percentages to prevent
  the overestimation of treatment efficacy.
labels:
- chart:table
- chart:text
- task:compare
- impact:clarity
- data:statistical
- audience:expert
- bias:magnification
---

## The Rule <!-- role: advice -->
Never present relative risk reduction (percentages) in isolation. Always display it alongside the absolute risk reduction or the baseline event rates.

## The Logic <!-- role: reason -->
Reporting relative risk reduction alone creates a "magnification" effect. While technically accurate, it subliminally inflates the perceived efficacy of an intervention by ignoring the underlying event frequency. In a study of physicians, those shown only relative risks rated drug effectiveness significantly higher (mean difference of 0.45 to 1.39 scale points) than those shown absolute risks [@bucher_influence_1994]. Providing absolute risk forces the audience to account for the "large denominator" of people who do not benefit.

## Where to Apply <!-- role: context -->
This advice is critical when reporting the results of interventions where the target event is rare (low incidence).
*   **User Goal:** Making clinical or policy decisions based on trial data.
*   **Data Type:** Clinical trial results, efficacy studies, or primary prevention statistics.
*   **Audience:** Decision-makers (e.g., physicians, policy-makers) who need to weigh benefits against costs/side effects.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Investigating biological mechanisms rather than clinical utility.
*   **Reason:** If the goal is to assess the pure potency of a chemical agent regardless of clinical relevance, relative risk might be the primary metric of interest (though context is still usually helpful).

## The Price <!-- role: costs -->
*   **The Sacrifice:** The perceived "wow factor" of the intervention will likely decrease.
*   **The Risk:** The audience may adopt a more conservative attitude toward the intervention, potentially under-prescribing if they focus too heavily on the high number of non-beneficiaries [@bucher_influence_1994].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Reporting "34% reduction" without mentioning that the rate dropped from 2% to 1.5%.
*   **Why it fails:** It hides the fact that the absolute benefit is only 0.5%, leading to overstated enthusiasm for the treatment.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do you see a large percentage change (e.g., "50% drop") but cannot find the original count or rate (e.g., "10 in 1000")?
*   **The Test:** Ask "50% of what?" If the graphic doesn't answer that immediately, it fails.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add the absolute risk reduction (e.g., "Absolute reduction: 1.4%") next to the relative percentage.
*   **Best Fix:** Visualize the full denominator, showing the small fraction of people who benefited relative to the total treated population.
