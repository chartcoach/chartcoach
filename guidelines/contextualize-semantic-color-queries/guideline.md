---
id: contextualize-semantic-color-queries
title: Contextualize Terms for Color Assignment
bibliography: references.bib
description: Refine color choices by considering the semantic context of the data
  label (e.g., distinguishing 'Apple' the brand from 'Apple' the fruit).
labels:
- visual:color
- data:semantics
- task:labeling
- impact:accuracy
---

## The Rule <!-- role: advice -->
Do not assign semantic colors based on isolated keywords; use the surrounding semantic context or category name to determine the correct color association.

## The Logic <!-- role: reason -->
Many terms are polysemous (have multiple meanings). The color association depends entirely on the specific definition being used in the dataset.
*   **The Principle:** **Semantic Disambiguation**. Language is highly contextual. A "correct" semantic color in one domain is an error in another.
*   **The Evidence:** The term "Apple" is strongly associated with red, green, and yellow in the context of fruit. However, in the context of "Brand" or "Company," "Apple" is associated with white, silver, or gray. The authors demonstrate that using the category (e.g., "Company") to refine the search (via WordNet synsets) shifts the color assignment from red to silver [@setlur_linguistic_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Accurate representation of specific entities (brands, sports teams, chemical elements).
*   **Data Type:** Text labels that might be ambiguous (e.g., "Jaguar" - animal vs. car, "Orange" - fruit vs. telecommunications brand).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The category is unambiguous.
*   **Reason:** If the dataset is explicitly "Fruits," disambiguation overhead is unnecessary.
*   **Scenario:** Abstract concepts.
*   **Reason:** Terms like "Happy" or "Anger" might have loose associations (Yellow/Red), but adding context like "Emotion" might not narrow down a specific brand identity color effectively.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Requires more metadata or manual input to define the "context" (e.g., telling the system this is a list of "Companies").
*   **The Risk:** Over-contextualization might miss common associations if the specific subset (e.g., "Tech Company") doesn't yield strong color results in a corpus search.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using the most popular global definition.
*   **Why it fails:** In a chart of "Tech Giants," coloring Apple red (because fruit is the most common global usage of the word) is confusing and incorrect.
*   **The Wrong Fix:** Ignoring modifiers.
*   **Why it fails:** "Amber" has a specific color, but "Burnt Amber" or "Light Amber" are distinct. Ignoring the modifier leads to inaccurate color representation [@setlur_linguistic_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the color seem nonsensical for the domain? (e.g., A silver bar for "Apple" in a fruit chart, or a red bar for "Apple" in a stock market chart).
*   **The Test:** Check the "Least Common Subsumer" or category header. Does the assigned color match the imagery of that specific category?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually override ambiguous terms.
*   **Best Fix:** Use query expansion. When searching for the color of a term, append the category name (e.g., search "Apple Brand Logo" instead of just "Apple") to retrieve the correct dominant colors [@setlur_linguistic_2016].
