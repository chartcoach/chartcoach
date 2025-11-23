---
id: differentiate-baseline-incremental-risk
title: Visually Distinguish Baseline from Incremental Risk
bibliography: references.bib
description: Use distinct colors to separate pre-existing risks from new risks caused
  by treatment to prevent patients from attributing total risk to the intervention.
labels:
- visual:color
- task:comparison
- impact:bias-reduction
- data:risk
- chart:pictograph
---

## The Rule <!-- role: advice -->
When displaying side effects or complications, visually separate the baseline risk (risk without treatment) from the incremental risk (additional risk caused by treatment) using distinct colors.

## The Logic <!-- role: reason -->
Patients often mistakenly attribute the *total* risk of a complication to the treatment itself, ignoring the fact that they might face that risk even without treatment. Separating them visually reduces worry and lowers the perceived likelihood of side effects.
*   **The Principle:** Incremental Risk Framing.
*   **The Evidence:** In studies of women considering tamoxifen, those who saw distinct visual encodings for baseline vs. incremental risk had reduced worry and more accurate risk perceptions [@fagerlin_helping_2011].

## Where to Apply <!-- role: context -->
*   **User Goal:** evaluating the specific harm or benefit attributable to a medical intervention.
*   **Data Type:** Risk probabilities where a background rate exists (e.g., risk of menopausal symptoms in postmenopausal women vs. risk added by medication).
*   **Audience:** Patients considering treatments with known side effects.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When there is no known baseline risk for the specific outcome in the population (the risk is 0% without the intervention).
*   **Reason:** There is no baseline to visualize.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual simplicity. It requires explaining two concepts (baseline vs. additional) rather than one single number.
*   **The Risk:** If the colors are not clearly labeled, the user may be confused about which portion represents the drug's effect.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing only the total risk percentage in a treatment group.
*   **Why it fails:** This leads patients to believe the drug is solely responsible for the entire risk (e.g., believing a drug causes *all* hot flashes, rather than just the *extra* ones) [@fagerlin_helping_2011].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the graphic use a single color to represent the bad outcome?
*   **The Test:** Ask, "Can I see how many people would get this problem *without* taking the medicine?" If the answer is no, the rule is broken.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Split the bar or icon array into two colors: "Risk without pill" and "Extra risk with pill."
*   **Best Fix:** Use a pictograph where baseline cases are one color (e.g., light blue) and additional treatment-induced cases are a contrasting color (e.g., dark blue) [@fagerlin_helping_2011].
