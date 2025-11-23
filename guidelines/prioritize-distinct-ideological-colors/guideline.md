---
id: prioritize-distinct-ideological-colors
title: Prioritize Distinct Ideological Colors Over Brand Colors
bibliography: references.bib
description: Use ideological color associations rather than official logos when party
  brand colors clash or overlap.
labels:
- visual:color
- impact:clarity
- data:categorical
- audience:general-public
- domain:politics
---

## The Rule <!-- role: advice -->
When assigning colors to political parties, do not strictly adhere to the parties' official corporate design or logo colors if they overlap. Instead, assign "political colors" associated with the party's ideology or historical convention to ensure distinctiveness.

## The Logic <!-- role: reason -->
Official branding is often insufficient for data visualization because multiple parties may use the same dominant color in their logos. For example, in Germany, both the SPD (Social Democrats) and CDU (Conservatives) use red in their logos. Using these brand colors makes it impossible to distinguish them in a chart. By switching to ideological colors—such as Black for the conservative CDU and Red for the socialist-rooted SPD—you create clear visual separation that aligns with established political associations [@muth_partycolors_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Differentiating between major parties in a multi-party system.
*   **Data Type:** Categorical data representing political groups.
*   **Audience:** Readers familiar with the general political landscape and ideological color conventions (e.g., Green for environmentalists, Yellow for liberals).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Single-party focus.
*   **Reason:** If the visualization is exclusively about one specific party and does not compare it to others, using their official brand identity is appropriate for recognition.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose strict adherence to the organization's corporate identity guidelines.
*   **The Risk:** Readers completely unfamiliar with political shorthand (e.g., "Black" for conservatives in Germany) might need a legend to make the connection, whereas a logo color might have been more intuitive initially.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using slight shade variations of the same hue (e.g., two different reds) for major opposing parties.
*   **Why it fails:** It is difficult to distinguish subtle shade differences in small chart elements or maps, leading to confusion between opposing political entities [@muth_partycolors_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Two major categories in your legend share the same basic hue (e.g., both look "Red").
*   **The Test:** Place the colors next to each other on a bar chart. If you cannot instantly tell which bar belongs to which party without reading the label, the colors are too similar.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Darken one color significantly (e.g., turn a red into a dark maroon/brown) if historical precedent exists.
*   **Best Fix:** Adopt the established "political color" convention for that ideology (e.g., switch the conservative party from their red logo color to their conventional black or blue representation).
