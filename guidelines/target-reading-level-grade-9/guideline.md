---
id: target-reading-level-grade-9
title: Target Reading Level Grade 9 or Lower
bibliography: references.bib
description: Ensure all text and alternative text is written at a 9th-grade reading
  level or lower to maximize understandability.
labels:
- impact:accessibility
- impact:clarity
- visual:text
- audience:general
- task:understand
---

## The Rule <!-- role: advice -->

Write all text, including titles, annotations, and alternative text, at a reading grade level of 9 or lower.

## The Logic <!-- role: reason -->

This guideline is derived from the "Understandable" principle within the Chartability framework, which aims to present data without ambiguity and in a way that minimizes cognitive load [@elavsky_how_2022]. Adhering to lower reading levels ensures that content is accessible to people with cognitive disabilities, lower literacy, or those reading in a second language. As noted in WCAG understanding documents, simplifying language and defining jargon helps a broad range of users effectively process meaningful content [@w3c_understanding_meaningful].

## Where to Apply <!-- role: context -->

This rule applies to all textual elements associated with a data visualization.
*   **User Goal:** Reading titles, captions, tooltips, and alternative text descriptions to understand the data narrative.
*   **Data Type:** Any visualization containing text or requiring alternative text descriptions.
*   **Audience:** General audiences and users with cognitive or neurological disabilities.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Highly technical or specialized scientific visualizations where specific terminology is unavoidable.
*   **Reason:** Precision is required for the subject matter. However, even in these cases, the complex terminology should be explained or defined using a reading grade level of 9 or lower [@elavsky_how_2022].

## The Price <!-- role: costs -->

*   **The Sacrifice:** You may lose some degree of academic nuance or brevity often associated with complex sentence structures.
*   **The Risk:** Oversimplifying technical concepts without proper care may lead to a loss of precision or perceived authority among expert-only audiences.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Assuming that because the data is complex, the language describing it must also be complex.
*   **Why it fails:** This compounds the difficulty of the task; users must struggle to parse both the visual pattern and the linguistic explanation simultaneously.

## How to Check <!-- role: check -->

*   **Visual Sign:** Sentences are long, use passive voice, or contain frequent multisyllabic academic words.
*   **The Test:** Use an automated tool to estimate the reading level. The Hemingway Editor is a recommended tool that analyzes text, highlights complex sentences, and assigns a readability grade level to help authors adjust content [@hemingwayapp_hemingway_editor].

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Shorten sentences and replace complex adverbs or passive voice with direct, active language.
*   **Best Fix:** Rewrite the content to define any necessary jargon and provide supplementary material for unfamiliar terms, ensuring the explanation itself stays below a 9th-grade reading level [@w3c_understanding_meaningful].
