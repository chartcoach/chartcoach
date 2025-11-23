---
id: eliminate-seizure-risks
title: Eliminate Seizure-Inducing Flashes and Patterns
bibliography: references.bib
description: Ensure visualizations do not contain flashing content or rapid red transitions
  that can trigger photosensitive epilepsy.
labels:
- impact:accessibility
- impact:safety
- visual:animation
- visual:color
- audience:neurological-disability
- complexity:critical
---

## The Rule <!-- role: advice -->
Do not include content that flashes more than three times in any one-second period, particularly if the flashes contain the color red. Ensure that neither automatic animations nor user-triggered interactions create rapid flickering effects.

## The Logic <!-- role: reason -->
Visualizations that flicker or flash rapidly can trigger seizures in individuals with photosensitive epilepsy. This is a critical safety issue categorized under the "Perceivable" principle of accessibility [@elavsky_how_2022].
*   **The Principle:** Photosensitive Epilepsy Triggers. Content that flashes at specific frequencies (typically above 3 Hz) or occupies a significant portion of the visual field with high-contrast transitions poses a severe health risk [@w3c_understanding_three].
*   **The Evidence:** Standards bodies like the W3C and tools like PEAT have established thresholds to minimize these risks. Furthermore, research indicates that interaction techniques in data visualization—not just passive video—can produce sequences capable of inducing seizures [@elavsky_how_2022].

## Where to Apply <!-- role: context -->
This advice applies to any visualization involving movement, state changes, or alerts.
*   **User Goal:** Monitoring real-time data with alerts, or exploring data through animated transitions.
*   **Data Type:** Live streaming data, animated time-series, or interactive dashboards.
*   **Audience:** All users, specifically protecting those with photosensitive epilepsy or cognitive sensitivities.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** None.
*   **Reason:** This is a safety-critical guideline. There is no design justification for including content that physically harms the user.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot use rapid blinking or high-frequency strobing to demand user attention for critical alerts.
*   **The Risk:** High-speed animation of large datasets might need to be slowed down to ensure transitions do not exceed safe flashing thresholds.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Only checking automatic animations (videos/GIFs) while ignoring user interaction.
*   **Why it fails:** Users can generate seizure-inducing sequences themselves through rapid interaction, such as quickly scrubbing through a timeline or toggling filters repeatedly [@elavsky_how_2022].
*   **The Wrong Fix:** Using a large, flashing red background to signal a critical system error.
*   **Why it fails:** Red flashes are particularly dangerous and increase the likelihood of triggering a seizure [@umd_photosensitive_epilepsy].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does any part of the chart blink, flash, or flicker more than three times per second? Is a significant portion of the screen turning red repeatedly?
*   **The Test:** Use the Photosensitive Epilepsy Analysis Tool (PEAT) to analyze video captures of the visualization in action [@umd_photosensitive_epilepsy].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove the animation or blinking effect entirely.
*   **Best Fix:** Slow down transitions so they are smooth rather than strobing. For alerts, use static, high-contrast icons or non-flashing color changes instead of blinking lights [@w3c_understanding_three].
