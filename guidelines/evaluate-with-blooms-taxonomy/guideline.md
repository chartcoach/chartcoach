---
id: evaluate-with-blooms-taxonomy
title: Evaluate Beyond Perceptual Accuracy
bibliography: references.bib
description: Use Bloom's Taxonomy to validate visualizations against higher-level
  tasks like prediction and synthesis, not just value retrieval.
labels:
- impact:evaluation
- task:analyze
- task:synthesize
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->
Do not validate visualizations solely based on how fast or accurately users can retrieve specific values. You must also test higher-level understanding by asking users to predict future values (Synthesis), identify trends (Analysis), and make decisions based on the data (Evaluation).

## The Logic <!-- role: reason -->
A visualization can support perfect value retrieval (Knowledge level) while failing to support the identification of trends or logical predictions. "Understanding is far more than extraction of individual values." Different designs afford different conclusions at different levels of cognitive processing; a design that succeeds at one level may fail at another.
*   **The Principle:** Bloom’s Taxonomy of Educational Objectives.
*   **The Evidence:** Evaluation of chart redesigns revealed that while some designs improved value retrieval, they did not necessarily change the users' ability to apply that data or make different policy arguments, suggesting these levels are independent skills [@burns_how_2020].

## Where to Apply <!-- role: context -->
*   **User Goal:** Verifying if a design choice (e.g., a redesign) actually improves user understanding.
*   **Data Type:** Any complex real-world data.
*   **Audience:** Visualization designers and researchers conducting A/B testing or usability studies.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Dashboards for lookup tasks.
*   **Reason:** If the tool is strictly a "lookup table" meant only for precise value retrieval (e.g., checking a specific stock price), higher-level synthesis testing may be unnecessary.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Conducting this type of evaluation requires qualitative analysis (coding open-ended responses) which is more time-consuming than measuring click-accuracy or response time.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assuming a chart is "better" because users can read the numbers 10% faster.
*   **Why it fails:** Speed does not equal comprehension. Users might read numbers quickly but fail to notice a bi-modal distribution or a correlation [@burns_how_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** N/A (Process check).
*   **The Test:** Review your user testing script. If all questions have a single correct numeric answer, you are missing the higher levels of understanding.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add one "prediction" question: "Based on this chart, what do you expect the value to be next week?"
*   **Best Fix:** Adopt the 6-level framework from the paper: Ask questions targeting Knowledge, Comprehension, Application, Analysis, Synthesis, and Evaluation [@burns_how_2020].
