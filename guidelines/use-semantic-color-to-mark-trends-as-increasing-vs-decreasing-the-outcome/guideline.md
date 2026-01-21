---
id: use-semantic-color-to-mark-trends-as-increasing-vs-decreasing-the-outcome
title: Use Semantic Color to Mark Trends as Increasing vs Decreasing the Outcome
bibliography: references.bib
description: Assign colors by narrative role (e.g., increases vs decreases) so viewers
  immediately understand how each trend contributes to the overall story.
labels:
- chart:small-multiples
- task:explain
- visual:color
- impact:clarity
- data:temporal
- audience:general
- complexity:intermediate
- source:datawrapper-fix-my-chart
---

## The Rule <!-- role: advice -->

Color the series (or panels) by what they *do* in the story (e.g., one color for trends that reduce the outcome and another for trends that increase it), and keep that meaning consistent across the full set of panels. [@mintzer_sequential_storytelling_2024]

## The Logic <!-- role: reason -->

Semantic color reduces interpretation work: instead of decoding each panel from scratch, readers can use color as an immediate cue for “this factor pushes the result up” vs “this factor pushes it down.” That supports the post’s goal of making interrelated indicators feel connected and narratively legible. [@mintzer_sequential_storytelling_2024]

- **The Principle:** Color encodes narrative role
- **The Evidence:** [@mintzer_sequential_storytelling_2024]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly grasp how multiple trends contribute differently to one outcome (e.g., fertility decreases population growth pressure while mortality/life expectancy increase net population). [@mintzer_sequential_storytelling_2024]
- **Data Type:** Several related time series where each series can be interpreted as a contributor with a directional effect in the narrative. [@mintzer_sequential_storytelling_2024]
- **Audience:** Non-technical readers who benefit from immediate cues about “which side” a trend is on. [@mintzer_sequential_storytelling_2024]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The same metric has a mixed/ambiguous role in the story (not clearly “increasing” or “decreasing” the outcome), or the article is intentionally avoiding directional framing.
- **Reason:** Forcing semantic color can oversimplify the relationship and mislead viewers about the metric’s role. [@mintzer_sequential_storytelling_2024]

## The Price <!-- role: costs -->

- **The Sacrifice:** Flexibility—color is no longer “just aesthetics”; it’s committed to a specific interpretation. [@mintzer_sequential_storytelling_2024]
- **The Risk:** If your narrative framing changes (or is disputed), the color scheme may need to change too, since it encodes meaning. [@mintzer_sequential_storytelling_2024]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assigning unrelated colors per panel/series (or using default palettes) that don’t communicate why the trends belong together.
- **Why it fails:** Viewers don’t get a consistent signal about each trend’s contribution, so the chart still reads as disconnected facts. [@mintzer_sequential_storytelling_2024]

## How to Check <!-- role: check -->

- **Visual Sign:** Colors feel decorative; a viewer can’t explain what a color “means” in one sentence. [@mintzer_sequential_storytelling_2024]
- **The Test:** Ask: “If I point to the orange (or green) panels, can someone tell me the shared role they play in the story?” If not, the colors aren’t semantic. [@mintzer_sequential_storytelling_2024]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Pick two role-based colors (e.g., “reduces” vs “increases”) and recolor all panels/lines to match those roles consistently. [@mintzer_sequential_storytelling_2024]
- **Best Fix:** Combine role-based color with short annotations that explicitly state the role (“reduces…”, “increases…”) so color and text reinforce the same interpretation. [@mintzer_sequential_storytelling_2024]
