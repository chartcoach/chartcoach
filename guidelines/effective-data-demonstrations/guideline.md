---
id: effective-data-demonstrations
title: Use Distinct Structures When Illustrating Statistical Fallibility
bibliography: references.bib
description: To show that stats are unreliable, use visually distinct shapes (stars
  vs. circles) rather than unstructured noise.
labels:
- chart:scatter
- task:educate
- impact:persuasion
- audience:novice
- source:methodology
---

## The Rule <!-- role: advice -->
When creating examples to demonstrate the importance of visualization (or the limitations of statistics), use datasets with clearly identifiable, structured shapes (e.g., lines, parabolas, stars) rather than unstructured noise.

## The Logic <!-- role: reason -->
The effectiveness of classic examples like Anscombe’s Quartet lies not just in the stats being the same, but in the graphs being "clearly different and identifiably distinct." Viewers perceive the contradiction more strongly when one graph shows a clear pattern (like a star or a dinosaur) and another shows a different clear pattern (like a circle), both sharing identical stats. Unstructured "blobs" with identical stats fail to convey the message as effectively.
*   **The Principle:** Perceptual Distinguishability
*   **The Evidence:** [@matejka_same_2017]

## Where to Apply <!-- role: context -->
*   **User Goal:** Teaching data literacy or persuading stakeholders to invest in visualization tools.
*   **Data Type:** Synthetic or pedagogical datasets.
*   **Audience:** Students, management, or non-technical stakeholders.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Testing data anonymization algorithms.
*   **Reason:** If the goal is to hide the image (steganography) or anonymize data while keeping stats, you might *want* the output to look like unstructured noise to obscure the original structure.

## The Price <!-- role: costs -->
*   **The Sacrifice:** It requires more effort to generate structured shapes (using techniques like simulated annealing) than random noise.
*   **The Risk:** Using "silly" shapes (like dinosaurs) might reduce the perceived seriousness of the analysis if the audience is very formal.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Generating two random clouds of points that look roughly the same but have the same stats.
*   **Why it fails:** The audience will look at them and say, "Well, they look pretty similar, so the stats *are* working." You need contrast to prove the point.

## How to Check <!-- role: check -->
*   **Visual Sign:** Your comparison charts look like slightly different versions of a fuzzy cloud.
*   **The Test:** Can you name the shape of the data in one word (e.g., "Star", "Line", "Circle")? If not, the structure isn't distinct enough.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use the pre-generated "Datasaurus Dozen" datasets.
*   **Best Fix:** Apply the simulated annealing method described in the paper to coerce data into recognizable geometric primitives.
