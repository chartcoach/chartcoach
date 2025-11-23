---
id: prioritize-data-variation-over-design
title: Prioritize Data Variation Over Design Variation
bibliography: references.bib
description: When suggesting views for exploration, show different data combinations
  rather than multiple visual encodings of the same data.
labels:
- task:exploration
- task:discovery
- impact:coverage
- source:automated-recommendation
- visual:layout
---

## The Rule <!-- role: advice -->
When presenting a gallery of recommended visualizations for exploratory analysis, prioritize showing different combinations of variables and transformations (data variation) rather than showing many different chart types for the same specific data subset (design variation).

## The Logic <!-- role: reason -->
Exploratory visual analysis often suffers from "premature fixation," where users focus on specific questions or encodings too early. 
*   **The Principle:** Breadth-Oriented Exploration. By emphasizing data variation, the system encourages users to consider a wider range of variables and relationships they might otherwise overlook.
*   **The Evidence:** In a controlled study, users of a system that emphasized data variation (Voyager) significantly increased their variable coverage compared to users of a manual specification tool (PoleStar), increasing the number of unique variable sets examined by over 3 times [@wongsuphasawat_voyager_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Early-stage data exploration where the user's goal is vague or open-ended ("What is in this dataset?").
*   **System Type:** Recommendation-powered visualization browsers, faceted search interfaces, or dashboard generation tools.
*   **Audience:** Analysts who may lack deep prior knowledge of the dataset's structure or content.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Targeted Question Answering (Depth-First).
*   **Reason:** If the user has a specific hypothesis to test (e.g., "Is there a correlation between X and Y?"), they need to refine the visual design (e.g., switching from a bar chart to a line chart or adjusting scales) rather than seeing irrelevant variables [@wongsuphasawat_voyager_2016].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Users lose immediate fine-grained control over the specific visual encoding (e.g., changing colors, sorting) in the primary view.
*   **The Risk:** The "best" automated chart type selected by the system might obscure a specific pattern that an alternative design (hidden in a submenu) would reveal.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing a "carousel" of 10 different chart types (bar, pie, donut, treemap) all displaying the exact same single variable.
*   **Why it fails:** This consumes screen space with redundant information, preventing the user from spotting relationships between other unselected variables.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the initial dashboard or gallery view.
*   **The Test:** Count the number of unique data variables visible on the screen. If you see the same 2 variables plotted in 5 different ways, you are prioritizing design variation over data variation.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Cluster recommendations by the data columns they utilize. Display only the single highest-ranked chart type for that data cluster.
*   **Best Fix:** Implement an "Expand" or "Details" mode. Show the data variation in the main view, but allow users to click a specific chart to see "Design Alternatives" (alternative encodings of that specific data) in a side panel or modal.
