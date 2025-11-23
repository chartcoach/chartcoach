---
id: use-3d-transitions-for-constancy
title: Use 3D Transitions to Maintain Object Constancy
bibliography: references.bib
description: Animate transitions between 2D views using 3D rotation to help users
  track data elements.
labels:
- chart:animation
- visual:motion
- task:navigate
- impact:usability
- audience:general
---

## The Rule <!-- role: advice -->
When switching between different 2D views of the same dataset (e.g., a bar chart vs. a line chart), use a smooth 3D rotation transition.

## The Logic <!-- role: reason -->
Motion reduces cognitive burden by allowing the eye to track objects, rather than re-identifying them after a sudden cut.
*   **The Principle:** **Object Constancy** and **Structure-from-Motion**. Preattentive processing of motion allows users to visually track data elements as they rearrange.
*   **The Evidence:** [@brath_3d_2014] notes that a 3D transition can reveal the relationship between attributes (e.g., rotating a grid of bars) and provide a "mental model" of the data structure. This avoids the occlusion issues sometimes found in 2D staggering animations.

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding how data aggregates or dimensions relate to one another.
*   **Data Type:** Multidimensional datasets represented in multiple 2D forms.
*   **Audience:** Users exploring complex data who might get lost during view changes.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The transition is purely decorative or too slow.
*   **Reason:** If the 3D movement does not physically connect the data points (e.g., flying text), it adds distraction rather than constancy.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Implementation complexity (requires a 3D environment even for 2D charts).
*   **The Risk:** If the rotation axis is confusing, users may lose orientation.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Hard cuts (instant switching) or fading between views.
*   **Why it fails:** Users must re-read labels and re-process the scene to understand where the data went [@brath_3d_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart disappear and reappear?
*   **The Test:** Ask a user to follow a specific data point (e.g., "Company X") during the view switch. If they lose it, the transition failed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add animation between states.
*   **Best Fix:** Implement a "stage" rotation where the 2D chart is treated as a slice of a 3D object, rotating to reveal the new perspective.
