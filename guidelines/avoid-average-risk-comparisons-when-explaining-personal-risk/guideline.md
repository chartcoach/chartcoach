---
id: avoid-average-risk-comparisons-when-explaining-personal-risk
title: Avoid Comparative Average-Risk Benchmarks When They Could Bias Decisions
bibliography: references.bib
description: Treat comparisons to 'average risk' as persuasive, not neutral, because
  they can bias beliefs about treatment effectiveness.
labels:
- task:explain
- task:persuasion
- impact:fairness
- impact:trust
- audience:novice
- data:risk
- domain:health
- source:fagerlinHelpingPatientsDecide2011
---

## The Rule <!-- role: advice -->

Do not assume that “average person” comparative risk information is neutral; avoid including it when it could bias treatment judgments.

## The Logic <!-- role: reason -->

Comparative risk information can shift attention from absolute risk to “better/worse than average,” which can change worry, behavior, and perceived treatment effectiveness in non-normative ways even when absolute benefit is identical.

- **The Principle:** Prevent evaluative anchoring on social comparison
- **The Evidence:** The paper describes comparative risk as persuasive and reports evidence that it can bias beliefs about effectiveness and endorsement [@fagerlinHelpingPatientsDecide2011].

## Where to Apply <!-- role: context -->

- **User Goal:** Evaluate whether benefits outweigh risks for themselves.
- **Data Type:** Tailored/personal risk estimates where an “average risk” comparator is tempting to add.
- **Audience:** Patients making screening or prevention decisions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** None explicitly endorsed; the paper notes potential usefulness for interpretability but expresses wariness.
- **Reason:** Evidence suggests comparative info can also bias decisions [@fagerlinHelpingPatientsDecide2011].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less contextual “is this high or low?” framing for users.
- **The Risk:** Some users may find absolute risks harder to interpret without a reference point.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding “average risk is 13%” as a default embellishment to every personalized risk output.
- **Why it fails:** It can become persuasive and distort judgments about intervention value [@fagerlinHelpingPatientsDecide2011].

## How to Check <!-- role: check -->

- **Visual Sign:** Statements or visuals that emphasize “above/below average” as a headline or primary takeaway.
- **The Test:** Ask, “Would the user’s view of treatment effectiveness change solely because the comparator changed?” If yes, the comparator is acting persuasively.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove average-risk comparisons and present only the user’s absolute risk and absolute changes with treatment.
- **Best Fix:** If you keep any comparison, ensure the decision framing stays anchored on absolute benefit vs harm for the individual, not on relative standing [@fagerlinHelpingPatientsDecide2011].
