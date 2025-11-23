---
id: test-palettes-for-colorblindness-and-naming
title: Test Palettes for Colorblindness and Naming
bibliography: references.bib
description: Verify that chosen colors are distinguishable by colorblind users and
  have distinct linguistic names.
labels:
- visual:color
- impact:accessibility
- impact:communication
- task:design
---

## The Rule <!-- role: advice -->
Check that your colors can be distinguished by colorblind readers and do not share the same linguistic name.

## The Logic <!-- role: reason -->
Colors must be functional, not just aesthetic. If colors look the same to a segment of the audience, or if they are described by the same word (e.g., two shades both called "blue"), communication fails.
*   **The Principle:** Inclusive Design and Semantic Clarity.
*   **The Evidence:** [@muth_colorguide_2018] highlights *Viz Palette* for two specific checks: warning if colors have "the same name... which makes it harder to talk about your designs," and checking if they can be distinguished by colorblind people.

## Where to Apply <!-- role: context -->
*   **User Goal:** Finalizing a color palette for publication.
*   **Audience:** General public (which includes colorblind individuals) and collaborators (who need to discuss the design).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** None.
*   **Reason:** Accessibility and clear communication are fundamental requirements.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may have to abandon aesthetically pleasing palettes that lack sufficient contrast or distinct hue differences.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assuming that because two colors look different to you, they look different to everyone.
*   **Why it fails:** It ignores the reality of CVD (Color Vision Deficiency).

## How to Check <!-- role: check -->
*   **The Test:** Use a simulator like *Coblis*, *Sim Daltonism*, or the built-in simulator in Datawrapper [@muth_colorguide_2018].
*   **Visual Sign:** Does a "dark red" and "blue" look identical in simulation?

## How to Fix <!-- role: fix -->
*   **Best Fix:** Use tools like *Viz Palette* to identify conflicts and adjust hues or lightness until the warning signs disappear [@muth_colorguide_2018].
