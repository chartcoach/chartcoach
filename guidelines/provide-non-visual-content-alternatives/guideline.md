---
id: provide-non-visual-content-alternatives
title: Provide Non-Visual Content Alternatives
bibliography: references.bib
description: Ensure all trends, annotations, and narratives in a visualization are
  accessible via screen readers and text alternatives.
labels:
- impact:accessibility
- impact:inclusion
- task:consume
- visual:non-visual
- audience:blind
- audience:low-vision
---

## The Rule <!-- role: advice -->
Ensure that all information presented visually—including data trends, annotations, and narrative elements—is available without sight through screen readers, Braille displays, or text alternatives.

## The Logic <!-- role: reason -->
Data visualizations often rely exclusively on visual perception, excluding users with blindness or low vision. The "Content is only visual" heuristic, part of the Perceivable category in the Chartability framework, mandates that users must be able to identify content using senses such as sound and touch [@elavsky_how_2022].
*   **The Principle:** Perceivability (POUR). Information must not be limited to a single sensory modality.
*   **The Evidence:** Standard accessibility guidelines state that non-text content must have text descriptions so information is presented in alternative modalities [@w3c_wcag_quick]. Chartability emphasizes that accessible experiences must be manually checked to ensure trends and major narrative elements are exposed to assistive technologies [@elavsky_how_2022].

## Where to Apply <!-- role: context -->
This applies to all data-driven interfaces, videos, presentations, and animations.
*   **User Goal:** Understanding the data's story, specific values, and key takeaways without relying on visual observation.
*   **Audience:** Users employing Assistive Technologies (AT) such as screen readers on desktop or mobile devices [@apple_voiceover_user] [@google_use_talkback].
*   **Data Type:** Any chart, graph, or map where "visually apparent" trends or features are necessary for understanding.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Strictly decorative elements.
*   **Reason:** If an element conveys no information, data, or narrative value (e.g., a decorative border), adding non-visual descriptions creates noise and redundancy. However, most data visualizations contain meaningful information and rarely fall into this category.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Testing rigor and time. You cannot rely solely on automated checkers; manual testing with specific browser/screen reader combinations is required [@elavsky_how_2022].
*   **The Risk:** Increased development complexity to ensure synchronization between visual states (like animations) and audio descriptions.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Providing a short, generic alt text like "Bar chart of sales."
*   **Why it fails:** This identifies the object but fails to expose the "visually apparent" trends, annotations, or narrative elements required for equivalence [@elavsky_how_2022].
*   **The Wrong Fix:** Relying only on colorblindness simulators.
*   **Why it fails:** This addresses color perception but does not solve the "Content is only visual" failure for users who cannot see the screen at all.

## How to Check <!-- role: check -->
*   **Visual Sign:** If you turn off your monitor, can you still access all the information?
*   **The Test:** Perform manual audits using the following specific combinations to ensure the device can access all chart info: JAWS with Chrome, NVDA with Firefox (on Windows) [@nvaccess_home_free] [@freedomscientific_jaws_screen], and VoiceOver with Safari (on macOS and iOS) [@apple_voiceover_user].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Provide a detailed text description or a data table adjacent to the visualization that explicitly describes the trends and values visually represented [@w3c_wcag_quick].
*   **Best Fix:** Implement full programmatic accessibility where the chart elements themselves are navigable and readable by screen readers, and ensure videos or animations include synchronized audio descriptions [@youtube_accessible_chart].
