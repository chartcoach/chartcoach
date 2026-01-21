---
id: define-the-message-first
title: Define Your Message Before Designing the Chart
bibliography: references.bib
description: Start with a clear message and let it drive chart type, encodings, layout,
  and annotation choices.
labels:
- chart:any
- task:communicate
- visual:annotation
- impact:clarity
- data:any
- audience:novice
- process:design
---

## The Rule <!-- role: advice -->

Define the visualization’s message first, and use it as the guiding constraint for every design decision (chart type, color, emphasis, and text).

## The Logic <!-- role: reason -->

A clear message acts as an organizing constraint: it reduces arbitrary choices, improves coherence across encodings and annotations, and makes it easier for non-expert viewers to understand what the visualization is trying to say. Practitioners report that prioritizing message improves interpretability for lay audiences and helps teams coordinate concrete design decisions like chart selection, color, and text placement ([@schuster_who_2023; @gregory_data_2024]).

- **The Principle:** Message-first design as a coherence and decision-filtering constraint
- **The Evidence:** [@schuster_who_2023; @gregory_data_2024]

## Where to Apply <!-- role: context -->

Use this rule whenever you need the chart to communicate a specific takeaway rather than serve as open-ended exploration.

- **User Goal:** Grasp the main point quickly; understand “what this chart is saying”
- **Data Type:** Any (especially multi-variable data where many encodings are possible)
- **Audience:** General public, non-experts, cross-functional stakeholders, or mixed audiences

## When to Break It <!-- role: exceptions -->

Ignore or relax this rule when the primary purpose is unbiased exploration rather than persuasion or summarization.

- **Scenario:** Exploratory analysis dashboards meant to support many ad-hoc questions
- **Reason:** A single predefined message can over-constrain the design and hide alternative patterns or uncertainties

## The Price <!-- role: costs -->

Committing to a message early can limit breadth and require rework if the message changes.

- **The Sacrifice:** Less room to support multiple competing narratives or questions in one view
- **The Risk:** Anchoring on an early message that later turns out to be wrong or incomplete

## Common Mistakes <!-- role: mistakes -->

These anti-patterns often produce charts that look polished but don’t communicate.

- **The Wrong Fix:** Picking a chart type first (“we need a bar chart”) and trying to bolt on a message with a headline afterward
- **Why it fails:** The encodings, emphasis, and annotations were not chosen to support a specific takeaway, so the chart lacks a clear interpretive path

## How to Check <!-- role: check -->

- **Visual Sign:** The viewer’s eye has no obvious focal point; multiple elements compete for attention; the title is generic (“Sales by Region”)
- **The Test:** Write a one-sentence takeaway (“The one thing I want you to learn is…”) and verify that every major design element supports it; if you can’t do this, the message isn’t guiding the design

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add (or rewrite) a specific takeaway title and one annotation that highlights the key evidence in the chart
- **Best Fix:** Re-design from the message: choose the chart type and encodings that best support the takeaway, then adjust emphasis (color, ordering, labeling, and layout) to make the message the dominant reading
