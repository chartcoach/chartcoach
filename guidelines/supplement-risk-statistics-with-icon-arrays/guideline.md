---
id: supplement-risk-statistics-with-icon-arrays
title: Supplement Risk Statistics with Icon Arrays
bibliography: references.bib
description: Use icon arrays alongside numerical data to prevent denominator neglect
  in health risk communication.
labels:
- chart:icon-array
- task:compare
- impact:clarity
- data:risk
- audience:patient
- audience:low-numeracy
---

## The Rule <!-- role: advice -->
When communicating health risks or treatment efficacy—especially with inconsistent sample sizes—always accompany numerical statistics with **icon arrays** (pictographs representing individuals).

## The Logic <!-- role: reason -->
People suffer from "denominator neglect," a cognitive bias where they focus on the absolute number of events (the numerator) while ignoring the total sample size (the denominator). For example, people often perceive 80 deaths out of 800 as riskier than 5 deaths out of 100, simply because 80 is larger than 5.

*   **The Principle:** **Part-to-Whole Salience**. Icon arrays visually disentangle overlapping classes, making the relationship between the affected group and the total population concrete and visible.
*   **The Evidence:** In studies involving medical scenarios, denominator neglect led to inaccurate risk assessments in 74% of low-numeracy participants. Adding icon arrays reduced this error rate to 42% [@garcia-retamero_using_2012].

## Where to Apply <!-- role: context -->
*   **User Goal:** Helping patients or the public understand the true reduction in risk provided by a medical treatment.
*   **Data Type:** Probabilistic information, relative risks, or ratios with unequal denominators (e.g., comparing a treated group of 800 vs. a control group of 100).
*   **Audience:** Populations with **low numeracy** (math skills) or those communicating in a **non-native language**, as these groups are most susceptible to denominator neglect [@garcia-retamero_using_2012].

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The goal is persuasion rather than informed consent.
*   **Reason:** If the intent is to artificially inflate perception of risk (e.g., an aggressive anti-smoking campaign), relying on ratios with different denominators without visuals can be more "effective" at inducing fear, though this is ethically questionable and subject to bioethics review [@garcia-retamero_using_2012].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Space. Icon arrays require significant screen or page real estate compared to a simple text percentage.
*   **The Risk:** Individuals with **low graph literacy** may still struggle to associate the visual patterns with meaningful interpretations, benefiting less from the aid than high-literacy users [@garcia-retamero_using_2012].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Providing only the relative risk reduction percentage (e.g., "Reduces risk by 50%").
*   **Why it fails:** This masks the absolute risk. A 50% reduction could mean saving 1 life in 1,000 or 500 lives in 1,000. Without the absolute numbers visualized, the impact is ambiguous [@garcia-retamero_using_2012].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you presenting risk ratios (e.g., "1 in X") using only text or numbers?
*   **The Test:** Ask a user to identify which of two treatments is more effective when the group sizes differ. If they pick the one with the higher absolute number of successes despite a lower percentage, the design has failed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Ensure all numerical ratios use the same denominator (e.g., convert "1 in 5" and "20 in 100" to "20 in 100" and "20 in 100").
*   **Best Fix:** Generate an icon array showing the total population as a grid of circles/icons, with the "event" (e.g., deaths) colored differently (e.g., black) at the end of the array [@garcia-retamero_using_2012].
