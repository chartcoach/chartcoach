---
id: delay-visualization-titles
title: Delay or Toggle Title Display
bibliography: references.bib
description: Introduce titles after a delay or via toggle to allow users to form independent
  interpretations of the data.
labels:
- impact:bias-mitigation
- impact:comprehension
- task:interpretation
- visual:annotation
- audience:general-public
---

## The Rule <!-- role: advice -->
Design visualization interfaces that allow viewers to toggle titles off, or programmatically delay the display of the title by 5 to 10 seconds after the chart appears.

## The Logic <!-- role: reason -->
Titles frame the narrative and heavily influence the perceived main message of a visualization, often overriding the data itself. When a title is present immediately, it primes the viewer, triggering "selective perception" where they only look for evidence that supports the title.
*   **The Principle:** Bias Assimilation and Priming.
*   **The Evidence:** [@kong_frames_2018] found that slanted titles caused viewers to derive opposing messages from the exact same visualization. By delaying the title, you allow the viewer to process the visual information and form an "internal representation" before the author's framing takes effect.

## Where to Apply <!-- role: context -->
This interaction pattern is best suited for platforms where unbiased exploration is the primary goal.
*   **User Goal:** Critical thinking, data exploration, or unbiased fact-checking.
*   **Data Type:** Controversial topics (e.g., political policies, social issues) where pre-existing attitudes might trigger confirmation bias.
*   **Audience:** General audiences who may lack deep domain knowledge and are prone to trusting the "neutrality" of the visualization blindly.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Static Media (Print/PDF).
*   **Reason:** You cannot implement time-delays or toggles in static formats. In these cases, use an "Open-Ended" title frame (simply stating the topic) rather than a slanted declarative sentence.
*   **Scenario:** Rapid Dashboards.
*   **Reason:** In time-critical monitoring (e.g., stock tickers, server health), immediate identification via titles is necessary for efficiency.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Immediate context. Users might initially feel disoriented or unsure of what the specific variable measures without the text guide.
*   **The Risk:** Users might misinterpret the axes or variables if the visualization design itself (labels, legends) is not self-explanatory.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Writing a "neutral" title that actually uses a "statistics frame" (e.g., mentioning a specific trend like "Decrease in Budget").
*   **Why it fails:** [@kong_frames_2018] shows that even titles describing data trends can introduce slant. Total removal/delay is the only way to ensure the *initial* impression is based solely on the graphic.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the text appear at the exact same moment as the graphic?
*   **The Test:** Ask a user to interpret the graph without reading the title. If they can't do it, the graph needs better labeling, not just a title.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a "Show/Hide Title" button near the top of the visualization container.
*   **Best Fix:** Implement a CSS or JavaScript animation delay on the title element, or use a "reveal" interaction where the user must actively engage to see the author's conclusion.
