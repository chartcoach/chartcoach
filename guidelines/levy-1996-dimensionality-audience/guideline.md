---
id: levy-1996-dimensionality-audience
title: Use 2D for Analysis and 3D for Memorability
bibliography: references.bib
description: Users prefer 2D graphs for immediate self-use but 3D graphs for memorable
  presentations to others.
labels:
- visual:3d
- visual:2d
- task:presentation
- task:analysis
- impact:memorability
- audience:self-vs-others
---

## The Rule <!-- role: advice -->
Use standard 2-dimensional graphs when analyzing data for yourself or for immediate decision-making. Consider 3-dimensional graphs when the goal is to present to others or when the data needs to be memorable later.

## The Logic <!-- role: reason -->
There is a distinct split in user preference based on the "social" context of the graph. Users prefer simple 2D representations for their own immediate understanding ("self" and "now" scenarios). However, they shift preference toward 3D graphs when the goal is to show the data to an audience ("others") or ensure the audience remembers the content ("memory").
*   **The Principle:** Salience and Engagement.
*   **The Evidence:** @levy_gratuitous_1996 found that while 2D graphs were generally preferred, preferences significantly shifted toward 3D volume graphs for "memory" scenarios (p < 0.01). The authors suggest 3D objects may better engage visual systems evolved for a 3D world.

## Where to Apply <!-- role: context -->
This applies when deciding whether to apply 3D rendering effects (depth) to 2D data.
*   **User Goal:** Immediate analysis vs. Persuasive/Memorable presentation.
*   **Audience:** Self (analyst) vs. Others (Board of Directors/Clients).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The visualization requires precise data extraction or complex comparisons.
*   **Reason:** The paper notes that while preferred for memory, extraneous 3D depth can obscure data or create perceptual distortions (citing Tufte and others in the intro), though the authors' own focus was on *preference*.

## The Price <!-- role: costs -->
*   **The Sacrifice:** 3D graphs often contain "chart junk" or redundant cues that do not add data information.
*   **The Risk:** While the audience may prefer the 3D graph for presentation, they might struggle to read exact values compared to a 2D equivalent.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** "Flat design" for everything, even high-stakes presentations where impact is needed.
*   **Why it fails:** You may lose the engagement or memorability factor that subjects in the study associated with 3D volume graphs @levy_gratuitous_1996.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the graph flat (2D) or does it pop out (3D)?
*   **The Test:** Ask: "Who is looking at this? Is it for me to find an answer now, or for an audience to remember next week?"

## How to Fix <!-- role: fix -->
*   **Quick Fix:** For working papers, keep it 2D. For the final "hero slide" in a deck, consider a 3D treatment if memorability is the priority.
*   **Best Fix:** Align the rendering style with the communicative intent: simple/area graphs for "self" and "now"; 3D volume graphs for "others" and "memory."
