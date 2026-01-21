---
id: use-open-ended-prompts-for-comprehension-analysis-evaluation
title: Use Open-Ended Prompts for Comprehension, Analysis, and Evaluation
bibliography: references.bib
description: Elicit summaries, trend reasoning, and data-backed judgments with open-ended
  questions rather than only closed-form items.
labels:
- task:evaluate
- impact:insight
- audience:general-public
- custom:qualitative
---

## The Rule <!-- role: advice -->

Use **open-ended questions** to assess **Comprehension** (summaries), **Analysis** (trend/relationship descriptions), and **Evaluation** (arguments with evidence).

## The Logic <!-- role: reason -->

The paper argues that purely quantitative measures (speed/accuracy) are insufficient for understanding and uses open-ended prompts to capture conclusions and reasoning. Their case studies show that open-ended Analysis prompts surfaced a major difference between chart versions (e.g., noticing bimodality and trend characterization in the redesigned COVID chart) that earlier levels did not capture [@burnsHowEvaluateData2020].

- **The Principle:** Some understanding is only observable through explanation and justification
- **The Evidence:** [@burnsHowEvaluateData2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Detect how design changes what viewers *take away* and how they *justify* conclusions
- **Data Type:** Charts where salience, framing, and trend interpretation matter
- **Audience:** Broad audiences whose interpretations may vary and need to be characterized [@burnsHowEvaluateData2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot code qualitative responses (no staff/time)
- **Reason:** Open-ended prompts require post-hoc analysis to compare patterns across designs [@burnsHowEvaluateData2020]

## The Price <!-- role: costs -->

- **The Sacrifice:** More complex analysis pipeline (coding categories, comparing distributions)
- **The Risk:** Responses can be verbose or ambiguous; coding scheme choices can influence findings [@burnsHowEvaluateData2020]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Asking for “overall message” but treating it as a single correct answer
- **Why it fails:** The method is meant to compare distributions of conclusions, not force one “right” summary [@burnsHowEvaluateData2020]

## How to Check <!-- role: check -->

- **Visual Sign:** You only measure correctness rates and have no record of what people *thought was going on*
- **The Test:** Verify you have prompts that produce text explaining the data (summary, trend description, policy/argument + evidence) [@burnsHowEvaluateData2020]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add one Comprehension prompt (“describe the data to a friend”) and one Evaluation prompt (“argue for a decision and cite evidence”)
- **Best Fix:** Code responses blind to condition into categories of conclusions/evidence and compare frequencies across designs, as demonstrated in the paper [@burnsHowEvaluateData2020]
