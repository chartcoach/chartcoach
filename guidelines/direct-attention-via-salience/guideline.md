---
id: direct-attention-via-salience
title: Direct Attention to Task-Relevant Data via Saliency
bibliography: references.bib
description: Use visual salience (color, contrast, motion) to guide bottom-up attention
  specifically to the information required for the decision.
labels:
- visual:color
- visual:contrast
- impact:efficiency
- task:search
- audience:novice
- psychology:attention
---

## The Rule <!-- role: advice -->
Identify the critical information needed for a user's specific task and use visual encoding techniques (like high-contrast colors or distinct borders) to direct the user's bottom-up attention immediately to that information.

## The Logic <!-- role: reason -->
Visualizations automatically trigger "bottom-up attention," a fast, involuntary Type 1 process where the eye is drawn to salient features (like bright colors or moving targets). According to [@padilla_decision_2018], if the most salient features are irrelevant to the task, decision-making slows down or fails because the user must actively suppress this automatic response using working memory (Type 2 processing). Conversely, when salient features align with the task, performance improves significantly.

*   **The Principle:** Bottom-up Attention / Type 1 Processing
*   **The Evidence:** Studies cited in [@padilla_decision_2018] (e.g., Hegarty et al., 2010; Stone et al., 1997) show that viewers often focus on salient foreground information (like the number of icons) while ignoring non-salient background data (like base rates), unless design interventions realign salience with relevance.

## Where to Apply <!-- role: context -->
This advice applies to complex displays where specific data points are critical for decision-making.
*   **User Goal:** Rapid identification of specific threats, targets, or values (e.g., identifying a storm path or a tumor).
*   **Data Type:** Complex spatial data (maps, medical imaging) or dense statistical displays.
*   **Audience:** Particularly critical for novices who lack the "top-down" knowledge to know where to look without guidance.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Exploratory Data Analysis (EDA).
*   **Reason:** In EDA, the "relevant" information is unknown. artificially highlighting one area might bias the user against discovering patterns in non-salient regions.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose neutrality. By choosing what is salient, you are choosing what the user sees first.
*   **The Risk:** If you misidentify the user's goal, you will actively distract them and degrade their performance by forcing them to fight against your design.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Making everything "pop" or using high-contrast colors for decorative elements (e.g., borders, backgrounds).
*   **Why it fails:** This creates "visual clutter" or directs bottom-up attention to non-data ink, requiring the user to expend cognitive effort to ignore it.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do your eyes jump to the data, or to the frame/grid/legend?
*   **The Test:** Use a saliency algorithm (as suggested by [@padilla_decision_2018], such as the Itti et al. model) or a simple "squint test" to see what features remain visible when details are blurred.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Mute the colors of gridlines, axes, and background elements; increase saturation only for the data points relevant to the primary task.
*   **Best Fix:** Redesign the encoding so that the variable of interest maps to the most potent pre-attentive attribute (e.g., color hue or intensity) available.
