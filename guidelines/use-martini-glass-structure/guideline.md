---
id: use-martini-glass-structure
title: Structure Narratives like a Martini Glass
bibliography: references.bib
description: Begin with a tight, author-driven narrative path before opening the visualization
  for free, reader-driven exploration.
labels:
- chart:interactive
- task:explore
- impact:engagement
- visual:structure
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->
Start your interactive visualization with a strictly guided, author-driven narrative sequence (the stem), then open the interface to allow free, reader-driven exploration (the glass).

## The Logic <!-- role: reason -->
Purely open-ended tools (like spreadsheets) are great for analysis but poor for storytelling; purely linear films tell stories but lack verification. The "Martini Glass" structure balances both.
*   **The Principle:** Narrative Balance. By providing context first, you ensure the user understands the dataset's key themes before being overwhelmed by controls.
*   **The Evidence:** [@segel_narrative_2010] identify this as one of the most common and effective hybrid structures (Section 4.4.1), observing that it functions as a "jumping off point" where the initial authoring suggests themes the reader might explore on their own.

## Where to Apply <!-- role: context -->
This advice applies to interactive data journalism and educational visualizations.
*   **User Goal:** Understanding a complex topic and then verifying it personally.
*   **Data Type:** Complex, multi-dimensional datasets where users might get lost without an introduction.
*   **Audience:** General audiences who need an "establishing shot" before diving into details.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Drill-Down Stories.
*   **Reason:** As noted in [@segel_narrative_2010] (Section 4.4.3), some stories work better by letting users immediately choose a theme to reveal details (user-directed path) rather than forcing a linear intro.
*   **Scenario:** Pure Analysis Tools.
*   **Reason:** If the tool is strictly for professional analysts (e.g., Tableau workspace), the narrative "stem" is an obstruction.

## The Price <!-- role: costs -->
*   **The Sacrifice:** First-time interaction speed. The user must "sit through" the intro before they can freely query the data.
*   **The Risk:** If the "stem" is too long or boring, users may abandon the visualization before reaching the interactive "glass."

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** The "Interactive Slideshow" (in specific contexts).
*   **Why it fails:** While effective, the slideshow structure (Section 4.4.2) constrains interaction throughout the entire experience. The Martini Glass is distinct because it eventually removes constraints entirely.
*   **The Wrong Fix:** Dumping users into the data with a text intro on the side.
*   **Why it fails:** As seen in the Minnesota Employment Explorer critique (Section 3.5), providing text without enforcing a narrative path often results in users failing to find the story.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does your visualization have a distinct "Next" or "Play" phase followed by a "Reset/Explore" phase?
*   **The Test:** Can a user explore a variable *not* discussed in your intro text? If yes, but only *after* the intro is done, you have a Martini Glass.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a "Skip Intro" button that unlocks all filters immediately.
*   **Best Fix:** Design a linear slideshow of 3-5 key insights that manipulates the visualization automatically, then leave the visualization in its final state with all controls enabled for the user.
