---
id: pretrain-component-characteristics
title: Define Components Before Explaining the System
bibliography: references.bib
description: Provide training on the names and behaviors of individual elements before
  presenting the full interactive or animated system.
labels:
- structure:sequence
- impact:comprehension
- audience:novice
- task:learning
---

## The Rule <!-- role: advice -->
Ensure users know the names and specific behaviors of key components *before* showing them how those components interact in a complex system.

## The Logic <!-- role: reason -->
Building a mental model involves two steps: constructing "component models" (what things are) and a "causal model" (how they interact). Doing both simultaneously can cause Type 2 Cognitive Overload.
*   **The Mechanism:** Pretraining off-loads the work of learning the components. When the full system is presented, the user can devote their limited cognitive capacity solely to understanding the causal links between the already-known parts [@mayer_nine_2003].
*   **The Evidence:** This is the *Pretraining Effect*. Students who received pre-instruction on component names performed better on transfer tests (Effect Size 1.00) [@mayer_nine_2003].

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding complex machinery, biological systems, or dense data dashboards.
*   **Data Type:** Systems with multiple interacting variables or moving parts.
*   **Audience:** Users with low prior knowledge of the specific domain.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Expert audiences.
*   **Reason:** Experts already possess the component models in long-term memory; pretraining would be redundant and annoying.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Requires an extra step in the user flow (a "pre-boarding" or glossary phase).
*   **The Risk:** Users may become impatient if the pretraining is too disconnected from the "real" content.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** A tooltip that appears only on hover during a fast-paced animation.
*   **Why it fails:** This forces the user to hunt for information while trying to watch the system operate, increasing split attention.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the visualization jump straight into a complex interaction (e.g., "Here is how the car brake works") without defining what a "piston" or "brake shoe" is?
*   **The Test:** Ask a user to pause the start of the visualization and name the parts. If they can't, they are likely to suffer cognitive overload during the animation.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a static slide or overlay before the animation labeled "Key Terms."
*   **Best Fix:** Create a short, interactive module where users click parts to see their names and a brief animation of their isolated behavior before entering the main visualization.
