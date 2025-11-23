---
id: write-context-plain-language
title: Write Context in Plain Language
bibliography: references.bib
description: Use simple, non-technical language in captions and annotations to ensure
  clarity for both lay audiences and experts.
labels:
- visual:text
- impact:clarity
- impact:accessibility
- audience:novice
- audience:expert
---

## The Rule <!-- role: advice -->

Write titles, captions, and annotations using plain, non-technical language. Avoid abstract terms, scientific jargon, and complex vocabulary.

## The Logic <!-- role: reason -->

Complex language acts as a barrier to understanding, increasing the cognitive load required to decode a visualization. When text is difficult to parse, users struggle to identify the overarching narrative. Research indicates that plain language improves communication efficiency for everyone, not just the general public.

*   **The Principle:** Cognitive Accessibility. Simplifying language reduces the mental effort required to process the context, allowing the user to focus on the data insights.
*   **The Evidence:** Studies show that both experts and lay viewers criticize the use of complex or abstract language in captions [@schuster_being_2024]. Furthermore, research analyzing captions over decades found that modern, plain-language captions were significantly easier to distill into clear messages than older, scientifically dense descriptions [@koesten_what_2023]. Practitioners identify learning to simplify language as the most essential skill for newcomers to the field [@schuster_who_2023].

## Where to Apply <!-- role: context -->

*   **User Goal:** When the viewer needs to understand the "so what" of the data (narrative) rather than the specific mechanics of the analysis.
*   **Data Type:** especially critical for complex simulations, such as climate data, where future scenarios can be difficult to grasp if described abstractly.
*   **Audience:** General audiences, interdisciplinary teams, and even domain experts (who still prefer clarity over unnecessary complexity).

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Highly technical peer-to-peer documentation or academic papers focused on methodology.
*   **Reason:** In these specific contexts, precise technical terminology (jargon) serves as a shorthand for complex concepts that the audience is expected to know. Replacing terms like "confidence interval" or "stochastic process" with plain English might reduce precision.

## The Price <!-- role: costs -->

*   **The Sacrifice:** You may lose a degree of technical precision or succinctness that specific jargon provides.
*   **The Risk:** Explaining complex concepts in plain language can sometimes require more words, potentially cluttering the visual space if not edited tightly.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Copying the methodology description directly into the chart caption.
*   **Why it fails:** Methodology text describes *how* the data was made, not *what* it implies, and often uses alienating vocabulary (e.g., "uncertainty quantification").
*   **The Wrong Fix:** Using acronyms assuming universal knowledge.
*   **Why it fails:** It creates an immediate mental block for any user outside the immediate project team.

## How to Check <!-- role: check -->

*   **The Test:** The "Read-Aloud" Test. Read the caption or annotation out loud. If you stumble or sound like a textbook, it is too complex.
*   **The Test:** The "Layperson" Test. Show the text to someone outside your field. If they have to ask "what does this word mean?", the language is not plain enough.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Identify technical nouns and verbs (e.g., "ameliorate," "aggregate," "stochastic") and replace them with common synonyms (e.g., "improve," "combine," "random").
*   **Best Fix:** Rewrite the text to focus on the *outcome* rather than the *process*. Instead of "Data reflects high variance in stochastic models," write "The possible outcomes vary widely."
