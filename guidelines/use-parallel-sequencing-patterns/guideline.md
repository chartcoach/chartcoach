---
id: use-parallel-sequencing-patterns
title: Use Parallel Structure for Comparative Sequences
bibliography: references.bib
description: Repeat the same sequence of transition types across different data groups
  to improve memory and understandability.
labels:
- task:comparison
- task:storytelling
- impact:memory
- impact:comprehension
- visual:structure
---

## The Rule <!-- role: advice -->
When presenting comparisons between two high-level groups (e.g., "Eastern US" vs. "Western US"), use a parallel transition structure. If you show Group A using a sequence of [Map -> Chart -> Scatterplot], show Group B using that exact same sequence order.

## The Logic <!-- role: reason -->
Parallelism acts as a structural mnemonic device.
*   **The Principle:** Transition Parallelism.
*   **The Evidence:** [@hullman_deeper_2013] found that "perfect parallelism" (repeating the exact sequence of local transition types for different groups) resulted in significantly better memory of the presentation sequence compared to "reverse" parallelism (where the second group is shown in reverse order). Parallel structures help equate the importance of concepts and reduce the cognitive effort needed to track the narrative.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing multiple entities (e.g., regions, departments, products) across the same set of attributes.
*   **Data Type:** Grouped data where each group has similar available dimensions and measures.
*   **Audience:** Viewers who need to recall the information later.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Optimizing for "Global Cost" only.
*   **Reason:** Sometimes, reversing the order of the second group (e.g., A1->A2 then B2->B1) results in a lower transition cost at the "turning point" (A2 to B2 is closer than A2 to B1). However, the paper suggests the memory benefits of parallelism outweigh the local cost savings at that single turning point [@hullman_deeper_2013].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You might have one "expensive" transition when switching from the end of Group A to the beginning of Group B.
*   **The Risk:** The presentation might feel formulaic or repetitive.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** "Mirroring" the sequence (A-B-C then C-B-A) to make the middle transition smooth.
*   **Why it fails:** While the transition from C to C is smooth, the structural inconsistency harms the user's ability to recall the narrative sequence [@hullman_deeper_2013].

## How to Check <!-- role: check -->
*   **Visual Sign:** Write down the sequence of chart types or data views for the first section.
*   **The Test:** Does the second section follow the exact same pattern?
    *   Section 1: Overview -> Detail -> Time.
    *   Section 2: Overview -> Detail -> Time. (Pass)
    *   Section 2: Time -> Detail -> Overview. (Fail)

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reorder the slides in the second comparison block to match the first block exactly.
*   **Best Fix:** Identify the recurring "motif" (the pattern of transitions) and strictly enforce it as a global constraint across all groups being compared.
