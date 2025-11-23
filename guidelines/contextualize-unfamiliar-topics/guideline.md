---
id: contextualize-unfamiliar-topics
title: Contextualize Unfamiliar Topics
bibliography: references.bib
description: Provide clear definitions and orientation cues to support audiences who
  lack specific domain or geographic knowledge.
labels:
- impact:clarity
- impact:inclusivity
- audience:novice
- visual:text
- visual:annotation
- task:interpret
---

## The Rule <!-- role: advice -->

Explicitly define domain-specific terms and provide necessary orientation cues within the visualization. Do not assume the viewer shares your background knowledge of the topic, acronyms, or geography.

## The Logic <!-- role: reason -->

Visualizations do not exist in a vacuum; their interpretation relies heavily on the viewer's prior knowledge. When a design assumes familiarity with specific terms or locations, it risks excluding viewers or causing misinterpretation.

*   **The Barrier of Terminology:** Even commonly cited terms, such as "gender pay gap," can be barriers to entry. Research shows that providing simple definitions significantly improves comprehension, particularly among demographics like students or retirees who may be unfamiliar with the jargon [@knoll_gulf_2025].
*   **The Need for Orientation:** In geographic visualizations, such as crisis maps, a lack of orientation cues (like clear country or city labels) leads to uncertainty and self-doubt, even among digital natives. Without these anchors, viewers struggle to place the data in context [@koesten_encountering_2025].
*   **Engagement through Reframing:** Revisiting familiar topics with new insights or visual styles helps avoid overwhelming the audience and maintains engagement, a strategy employed to combat misinformation and reach new readers [@gregory_data_2024].

## Where to Apply <!-- role: context -->

*   **User Goal:** Public communication, journalism, or educational contexts where the audience has mixed levels of expertise.
*   **Data Type:** Geographic data (maps), specialized domain metrics, or socio-political statistics.
*   **Audience:** The general public, cross-functional teams, or any group outside the immediate subject matter experts.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Highly specialized dashboards designed exclusively for subject matter experts (e.g., a Bloomberg terminal for traders or an air traffic control display).
*   **Reason:** For experts, basic definitions create visual clutter and cognitive friction. They prioritize data density and rapid retrieval over introductory context.

## The Price <!-- role: costs -->

*   **The Sacrifice:** Screen real estate. Adding definitions, subtitles, or geographic context layers consumes space that could be used for more data points.
*   **The Risk:** If the tone is not managed carefully, defining basic concepts can feel patronizing to moderately knowledgeable viewers.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Using industry acronyms in titles or axes without expanding them (e.g., labeling an axis "YTD EBITDA" for a general audience).
*   **Why it fails:** It forces the user to leave the visualization to search for definitions, breaking their flow and reducing trust.
*   **The Wrong Fix:** Displaying a zoomed-in map of a specific region without an inset map or labels to show where it fits globally.
*   **Why it fails:** Users lacking specific geographic knowledge cannot mentally locate the data, leading to confusion [@koesten_encountering_2025].

## How to Check <!-- role: check -->

*   **Visual Sign:** Scan the text elements. Are there words, acronyms, or locations that a high school student would not immediately recognize?
*   **The Test:** The "Hallway Test." Show the visualization to someone outside your immediate department or field. Ask them to explain what the chart is showing without giving them a preamble. If they stumble on terms or location, you need more context.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Add a subtitle that defines the primary metric or variable in plain language. Add major city or country labels to maps.
*   **Best Fix:** Integrate "explainers" directly into the design. Use annotations to define terms where they appear, or use a "scrollytelling" approach to reframe the topic and build up the necessary context before showing the complex data [@gregory_data_2024].
