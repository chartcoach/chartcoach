---
id: avoid-stereotypical-gender-colors
title: Avoid Using Pink and Blue for Gender Data
bibliography: references.bib
description: Use neutral or alternative color palettes for gender data to avoid reinforcing
  cultural stereotypes.
labels:
- visual:color
- data:categorical
- impact:inclusivity
- audience:general
- task:comparison
---

## The Rule <!-- role: advice -->
Do not assign pink to women and blue to men when visualizing gender data. Instead, choose alternative, distinct color combinations (such as purple/green or teal/orange).

## The Logic <!-- role: reason -->
In western culture, these colors carry significant "stereotype baggage." Pink is often associated with "weak, shy girls who play with dolls," while blue implies "strong & rough" boys [@muth_gendercolor_2018]. Using this combination in data visualization effectively endorses these stereotypes, which is often counter-productive to the message of the chart, especially when visualizing topics like gender pay gaps.

## Where to Apply <!-- role: context -->
*   **User Goal:** Communicating data about men and women without bias.
*   **Data Type:** Categorical comparisons between sexes or genders.
*   **Audience:** General audiences, particularly in news media and corporate reporting.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When immediate decipherability is the absolute highest priority and the audience is broad and non-technical.
*   **Reason:** As noted by Alan Smith (Financial Times), readers decipher charts with stereotypical colors faster because they do not need to consult a legend [@muth_gendercolor_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Immediate cognitive recognition.
*   **The Risk:** Readers must spend a brief moment consulting the legend or annotations to understand which color represents which gender, rather than relying on cultural intuition.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Keeping the colors but swapping them (Pink for Men, Blue for Women) to "challenge" the stereotype.
*   **Why it fails:** This leads to misinterpretation because readers intuitively assume the standard cultural coding [@muth_gendercolor_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart look like a baby shower announcement?
*   **The Test:** If you removed the legend, would a user assume stereotypes (Pink=Women)? If yes, and you are trying to avoid bias, change the palette.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Desaturate the colors or shift the hues (e.g., to Purple and Green).
*   **Best Fix:** Adopt a completely new, historically or thematically relevant palette, such as the "Suffragette colors" (Purple/Green/White) used by *The Telegraph* [@muth_gendercolor_2018].
