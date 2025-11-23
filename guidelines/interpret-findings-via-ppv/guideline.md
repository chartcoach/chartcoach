---
id: interpret-findings-via-ppv
title: Interpret Findings Using Positive Predictive Value
bibliography: references.bib
description: Avoid relying solely on p-values to claim research truths; instead, estimate
  the post-study probability that a relationship is true.
labels:
- task:interpret
- impact:accuracy
- data:statistical
- audience:researchers
- complexity:advanced
---

## The Rule <!-- role: advice -->
Do not claim conclusive research findings based solely on formal statistical significance (typically $p < 0.05$). Instead, interpret results by estimating the Positive Predictive Value (PPV).

## The Logic <!-- role: reason -->
Reliance on $p$-values alone is an "ill-founded strategy" because the probability that a finding is true depends on more than just the significance level ($\alpha$). It depends heavily on the pre-study odds of a relationship being true ($R$), the statistical power ($1 - \beta$), and the presence of bias ($u$). As shown in the modeling by [@ioannidis_why_2005], even with a significant $p$-value, a research finding is often more likely to be false than true if the pre-study odds are low.

## Where to Apply <!-- role: context -->
This rule applies to the interpretation and presentation of all research claims, particularly in fields involving hypothesis testing.
*   **User Goal:** Determining the veracity of a claimed relationship.
*   **Data Type:** Statistical outputs from experimental or observational studies (e.g., 2x2 tables, regression results).
*   **Audience:** Scientific peers, policy makers, and general medical audiences.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Purely descriptive studies.
*   **Reason:** If no hypothesis is being tested and no claim of a "relationship" is being made, PPV calculation is not applicable.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to make definitive "black and white" claims based on a simple threshold.
*   **The Risk:** The pre-study odds ($R$) are often subjective and difficult to estimate, requiring the reader to make assumptions about the field's "yield" of true relationships.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Reporting smaller $p$-values (e.g., $p < 0.001$) as proof of truth.
*   **Why it fails:** Even with low $\alpha$, if bias is high or pre-study odds are extremely low (as in massive discovery-oriented testing), the finding may still be false [@ioannidis_why_2005].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the report conclude a relationship exists strictly because the null hypothesis was rejected?
*   **The Test:** Ask, "If I account for the ratio of true-to-no relationships in this specific field, does this result still hold up?"

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Acknowledge that "statistical significance" is not equivalent to "truth."
*   **Best Fix:** explicitly calculate and present the PPV using the formula $PPV = (1 - \beta)R / (R - \beta R + \alpha)$ (or the bias-adjusted version) provided in Table 1 and Table 2 of [@ioannidis_why_2005].
