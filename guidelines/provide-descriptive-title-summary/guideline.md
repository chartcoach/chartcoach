---
id: provide-descriptive-title-summary
title: Provide a Title, Summary, or Caption
bibliography: references.bib
description: Ensure every visualization includes text that describes the content to
  aid understanding, recall, and accessibility.
labels:
- impact:accessibility
- impact:cognition
- visual:text
- task:identify
- chart:all
---

## The Rule <!-- role: advice -->
Always accompany data visualizations with a clear title, summary, or caption.

## The Logic <!-- role: reason -->
Visualizations must limit ambiguity and minimize cognitive load to be considered understandable. While general standards like WCAG require headings to be descriptive *if* they are present, they do not explicitly mandate that a heading must exist in the first place—a gap identified as a serious flaw for data interfaces [@elavsky_how_2022]. 

*   **The Principle:** Visualization Recall and Context.
*   **The Evidence:** Research demonstrates that memorable graphics frequently rely on clear titles, labels, and narratives. Providing these text elements is essential to help viewers understand the context and recall what the chart conveys [@borkin_beyond_memorability_2016].

## Where to Apply <!-- role: context -->
This is a critical heuristic applicable to all data experiences.
*   **User Goal:** To immediately identify the subject and key takeaway of a chart without extensive analysis.
*   **Data Type:** Any quantitative or qualitative data representation.
*   **Audience:** Essential for all users, but critical for those with cognitive disabilities or those using assistive technologies who need text to anchor the visual experience [@elavsky_how_2022].

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Strictly decorative graphics.
*   **Reason:** If an image provides no information and is marked as decorative (hidden from screen readers), a visible title may confuse the user about the image's importance.
*   **Scenario:** Inline visualizations (Sparklines).
*   **Reason:** If a graphic is embedded directly within a sentence or paragraph that explicitly functions as its description and context.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate. Descriptive titles and summaries occupy vertical space that might otherwise be used for the chart area.
*   **The Risk:** If the summary is poorly written or inaccurate, it may bias the user's interpretation of the data before they analyze the visual itself.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on axis labels to define the chart.
*   **Why it fails:** Axis labels define dimensions, not the overall message or subject of the dataset.
*   **The Wrong Fix:** Omitting titles to achieve a "cleaner" or "minimalist" aesthetic.
*   **Why it fails:** This prioritizes style over usability and recall, forcing the user to expend cognitive effort to deduce the chart's purpose [@borkin_beyond_memorability_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart stand alone without a headline or explanatory text block?
*   **The Test:** Remove the chart visualization itself. Is there enough text remaining (title or caption) to tell the user what data subject was being looked at?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a text header directly above the chart stating what the data represents (e.g., "Sales by Region").
*   **Best Fix:** Add a descriptive title *and* a caption or summary that explains the key insight or trend visible in the data (e.g., "Sales increased in the North: A breakdown of regional revenue").
