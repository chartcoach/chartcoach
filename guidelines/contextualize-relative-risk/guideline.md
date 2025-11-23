---
id: contextualize-relative-risk
title: Contextualize Relative Risk Reductions
bibliography: references.bib
description: Never present relative risk reduction alone; pair it with baseline risk
  or absolute risk reduction to prevent misleading interpretations.
labels:
- task:compare
- visual:text
- impact:persuasion
- impact:ethics
- data:statistical
- audience:decision-makers
---

## The Rule <!-- role: advice -->

Do not present Relative Risk Reduction (RRR) in isolation. Always accompany it with the baseline risk or the Absolute Risk Reduction (ARR).

## The Logic <!-- role: reason -->

Relative values ignore the baseline risk, making small effects on rare events look massive. While RRR is perceived as larger and is more persuasive, using it alone prevents a fair comparison of benefits and harms.
*   **The Principle:** Framing Effect / Baseline Neglect
*   **The Evidence:** RRR is perceived as larger (SMD 0.41) and is more persuasive (SMD 0.66) than ARR, but without baseline information, it is likely to "misinform decisions" and lead to misinterpretation [@akl_using_2011].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.
*   **User Goal:** Making an informed decision about a medical intervention or policy.
*   **Data Type:** Efficacy data comparing a control group to an intervention group.
*   **Audience:** Patients, policy makers, and clinicians deciding on treatments.

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.
*   **Scenario:** Purely persuasive marketing where ethics are not a constraint.
*   **Reason:** If the sole goal is to persuade someone to adopt an intervention regardless of their values (e.g., "industry perspective"), RRR is statistically more effective at persuasion [@akl_using_2011]. *Note: This is ethically discouraged in evidence-based practice.*

## The Price <!-- role: costs -->

Be honest about the downsides.
*   **The Sacrifice:** Simplicity and Impact. The message becomes more complex and potentially less "exciting" (perceived effectiveness may drop).
*   **The Risk:** Information overload if too many statistical formats are presented simultaneously without hierarchy.

## Common Mistakes <!-- role: mistakes -->
Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.
*   **The Wrong Fix:** Reporting only "50% reduction."
*   **Why it fails:** It hides whether the risk dropped from 2% to 1% (negligible for many) or 50% to 25% (massive impact).

## How to Check <!-- role: check -->

*   **Visual Sign:** A big bold number with a "%" sign describing a change, with no reference to the original starting number.
*   **The Test:** Ask "50% of what?" If the visualization doesn't answer that immediately, it is incomplete.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Add a subtitle: "50% reduction (from 2 in 100 to 1 in 100)."
*   **Best Fix:** Visualize the absolute difference (e.g., grouped bar chart or slope graph) showing the Control Event Rate vs. the Intervention Event Rate, while using the relative percentage as a secondary annotation.
