---
id: use-number-needed-to-treat
title: Use Number Needed to Treat for Realistic Impact
bibliography: references.bib
description: Use the Number Needed to Treat (NNT) metric to foster conservative, realistic
  assessments of intervention benefits.
labels:
- chart:kpi
- task:assess
- impact:neutrality
- data:statistical
- audience:expert
- metric:nnt
---

## The Rule <!-- role: advice -->
Express intervention results as the "Number Needed to Treat" (NNT) alongside percentage changes.

## The Logic <!-- role: reason -->
The Number Needed to Treat (the reciprocal of absolute risk reduction) helps decision-makers internalize the effort required to prevent a single adverse event. Research shows that when data is presented as NNT, decision-makers provide significantly more conservative ratings of effectiveness and are less inclined to treat compared to relative risk presentations [@bucher_influence_1994]. This metric provides concrete information about the "consequences of giving no treatment" versus the effort of treatment.

## Where to Apply <!-- role: context -->
*   **User Goal:** Determining whether a treatment is worth the effort, cost, or side effects.
*   **Data Type:** Primary prevention studies where a large number of healthy people must be treated to prevent one illness.
*   **Audience:** Physicians or healthcare providers managing individual patient risks.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Communicating with audiences who struggle with reciprocal math or complex probability concepts.
*   **Reason:** NNT can be cognitively difficult to process for lay audiences compared to simple frequencies (e.g., "1 in 100").

## The Price <!-- role: costs -->
*   **The Sacrifice:** It emphasizes the "waste" or "inefficiency" of a treatment (the people treated who did not benefit).
*   **The Risk:** It may discourage the use of drugs that are statistically significant and effective, simply because the preventative efficiency seems low visually.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Only showing the "Success Rate" of the drug.
*   **Why it fails:** It obscures the cost-benefit ratio of the intervention intervention.

## How to Check <!-- role: check -->
*   **The Test:** Look at the data. Does it tell you how many people need to undergo the intervention to see one success?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a text label: "Number Needed to Treat: 71 patients for 5 years to prevent 1 event."
*   **Best Fix:** Create a unit chart (isotype) showing 71 figures, with 1 highlighted to represent the prevented event, visualizing the NNT ratio directly.
