---
id: contextualize-effect-sizes
title: Contextualize Findings by Field Size and Effect
bibliography: references.bib
description: Evaluate research credibility by comparing sample size against the magnitude
  of the claimed effect.
labels:
- task:evaluate
- impact:validity
- visual:scale
- data:quantitative
---

## The Rule <!-- role: advice -->
Be skeptical of isolated findings in two specific scenarios: small studies claiming large effects, and large studies claiming tiny effects.

## The Logic <!-- role: reason -->
The probability of a finding being true relates to power and effect size.
1.  **Small Studies:** Small sample sizes mean lower power. As power decreases, the Positive Predictive Value (PPV) drops. Therefore, findings from small studies (e.g., molecular predictors) are less likely to be true than large studies (e.g., large cardiology RCTs) [@ioannidis_why_2005].
2.  **Tiny Effects in Large Studies:** In fields where true effects are likely small (e.g., genetic risk factors), large studies are necessary. However, claimed research findings may simply be accurate measures of the prevailing bias rather than true relationships (Corollary 2).

## Where to Apply <!-- role: context -->
*   **User Goal:** Assessing the weight of evidence in a specific scientific field.
*   **Data Type:** Comparative literature reviews or meta-analyses.
*   **Audience:** Researchers evaluating the reproducibility of a field.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The "Gold Standard" Large RCT.
*   **Reason:** A well-powered, randomized, low-bias study is the exception; findings here (with moderate pre-study odds) have a high probability (approx 85%) of being true [@ioannidis_why_2005].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Rejection of "exciting" early discoveries from small teams.
*   **The Risk:** Assuming a "hot" field with many teams finding effects is accurate; Ioannidis argues the opposite—the "hotter" the field, the *less* likely findings are true due to competition and time pressure (Corollary 6).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Celebrating a "p < 0.05" finding in an underpowered study as a breakthrough.
*   **Why it fails:** In a study with low power, a "significant" finding is statistically more likely to be a false positive or a gross overestimate of the effect size.

## How to Check <!-- role: check -->
*   **Visual Sign:** A plot showing massive relative risks (e.g., RR > 3.0) in a study with very few participants.
*   **The Test:** Compare the result to the typical effect size in that specific field. If genetic markers usually have RR 1.1–1.5, a finding of RR 4.0 is likely false.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Down-weight the credibility of underpowered studies.
*   **Best Fix:** Demand or conduct large-scale evidence (e.g., meta-analysis of good-quality trials) to converge on the "gold standard" [@ioannidis_why_2005].
