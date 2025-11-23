---
id: use-static-grouped-arrays
title: Use Static Grouped Arrays for Risk Comparison
bibliography: references.bib
description: When comparing medical risks, static grouped icon arrays outperform animated
  versions in accuracy and user preference.
labels:
- chart:icon-array
- task:compare
- visual:animation
- impact:accuracy
- audience:general
---

## The Rule <!-- role: advice -->
Use static icon arrays with risk events grouped together when presenting side-by-side risk comparisons. Do not use animation (such as building icons one-by-one or shuffling) to emphasize the data.

## The Logic <!-- role: reason -->
Research indicates that "less is more" in risk communication. Animated graphics, despite offering motion cues, often inhibit knowledge accuracy and decision quality compared to simple static displays.
*   **The Principle:** **Cognitive Load and Distraction.** Animated elements can distract users—particularly those with higher numeracy who might otherwise attempt to count icons—thereby degrading performance.
*   **The Evidence:** In a study comparing static graphics against eight different animation types (including building, settling, and shuffling), no animation significantly improved outcomes. The static grouped control condition consistently resulted in optimal treatment choices and high knowledge accuracy [@zikmund-fisher_animated_2012].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing two hypothetical medical treatments or risks side-by-side to determine which is safer.
*   **Data Type:** Binary risk data presented as part-to-whole relationships (e.g., 100-icon arrays).
*   **Audience:** General public, spanning both low and high numeracy levels.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Demonstrating the accumulation of risk over time.
*   **Reason:** The "building" animation (where icons appear one by one) showed slight, though not statistically significant, promise. If the specific instructional goal is to show *time* rather than static magnitude, this animation style is the least harmful [@zikmund-fisher_animated_2012].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "bells and whistles" or the perceived novelty of a high-tech interface.
*   **The Risk:** The interface may appear less "modern" to stakeholders who equate animation with sophistication, though users actually rated the complex animated graphs as less helpful [@zikmund-fisher_animated_2012].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding "shuffling" animations to represent the randomness of a disease.
*   **Why it fails:** This drastically lowers graph evaluation ratings and accuracy. It creates distraction rather than clarification.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the icons moving, blinking, or appearing sequentially?
*   **The Test:** If you take a screenshot of the final state, does it convey the exact same information as the video? If yes, use the screenshot.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove the animation code and render the final frame immediately.
*   **Best Fix:** Ensure the icons are arranged in a contiguous block (grouped) rather than scattered, and present them statically.
