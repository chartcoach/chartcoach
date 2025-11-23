---
id: prioritize-blue-orange-palettes
title: Prioritize Blue and Orange Palettes
bibliography: references.bib
description: Use blue and orange combinations rather than red/green to ensure distinctness
  for colorblind readers.
labels:
- visual:color
- impact:accessibility
- audience:general
- task:compare
---

## The Rule <!-- role: advice -->
When selecting colors for categorical differences, prioritize blue and orange (or red) combinations. Avoid combining green with orange, red, or blue of the same lightness.

## The Logic <!-- role: reason -->
Blue is the safest hue because it looks distinctive to people with normal vision as well as those with the most common types of colorblindness (red-/green-blindness) [@muth_colorblindness_2020].
*   **The Principle:** Color Perception Consistency.
*   **The Evidence:** According to [@muth_colorblindness_2020], red-blind readers perceive a blue/orange mix as blue/olive, while green-blind readers see it as blue/orange. Conversely, combining nearby colors like blue and purple "will completely torpedo" a colorblind user's ability to understand the chart.

## Where to Apply <!-- role: context -->
*   **User Goal:** Distinguishing between two or more distinct categories.
*   **Data Type:** Categorical or divergent data.
*   **Audience:** General audiences where color vision deficiency prevalence is unknown.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** You are required to use specific brand colors that clash with this rule.
*   **Reason:** Corporate identity constraints may override aesthetic choice, though secondary indicators (icons/labels) become mandatory here.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the semantic meaning often associated with "Green" (good) and "Red" (bad).
*   **The Risk:** To colorblind users, red and green do not look like indicators for "good" and "bad," but rather like dark olive/orange and lighter versions of the same, losing the intended semantic metaphor [@muth_colorblindness_2020].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using "Traffic Light" colors (Red, Yellow, Green) assuming they are universally understood.
*   **Why it fails:** In a chart, green can look identical to red or orange for colorblind users unless the lightness is dramatically different.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using Green and Red to signify opposites?
*   **The Test:** Use a colorblind simulator like Coblis or Color Oracle to see if the hues merge into a similar muddy yellow or brown [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Swap green for blue.
*   **Best Fix:** Use a verified colorblind-safe palette (like Okabe & Ito) that balances blue, orange, and yellow while avoiding problematic green/red clashes.
