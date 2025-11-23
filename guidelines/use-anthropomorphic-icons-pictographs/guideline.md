---
id: use-anthropomorphic-icons-pictographs
title: Use Stylized Person Icons in Risk Arrays
bibliography: references.bib
description: Use anthropomorphic icons (like restroom signs) in icon arrays to improve
  recall and user preference compared to abstract shapes.
labels:
- chart:icon-array
- chart:pictograph
- task:recall
- impact:engagement
- impact:memorability
- audience:patient
- data:probability
---

## The Rule <!-- role: advice -->
Use stylized, anthropomorphic icons (specifically "restroom-style" male/female figures) when designing icon arrays to communicate risk. Do not use abstract geometric shapes like blocks, ovals, or smile faces.

## The Logic <!-- role: reason -->
Icons that resemble the subject matter (people) create a stronger mental connection than abstract symbols, leading to better memory retention and higher user preference.
*   **The Principle:** **Anthropomorphic Resonance.** Human-like icons appear to be easier to recall and are rated as more helpful and preferable by users than abstract shapes. For highly numerate users, the distinct "white space" around these irregular shapes also facilitates the strategy of counting specific events [@zikmund-fisher_blocks_2014].
*   **The Evidence:** In a study of 1,504 adults, participants who viewed risk data using restroom icons had significantly higher recall accuracy (~81%) compared to those viewing rectangular blocks (~70.5%) or smile faces (~70.5%). Users also rated restroom icons as significantly more preferred than abstract options [@zikmund-fisher_blocks_2014].

## Where to Apply <!-- role: context -->
Apply this whenever communicating health risks or probability statistics to a general audience where memory retention is a key goal.
*   **User Goal:** Remembering their specific risk percentage after the interaction.
*   **Data Type:** Binary risk data (event vs. non-event) presented in an icon array (e.g., 100 icons).
*   **Audience:** General public, specifically those with adequate numeracy or graphical literacy skills who benefit from counting distinct shapes.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The audience has known **Low Numeracy** skills and the goal is purely **magnitude estimation** (gist) rather than precise recall.
*   **Reason:** Research suggests that solid rectangular blocks may help low-numeracy users estimate "gist" (area-based probability) better than person icons. In the study, low-numeracy participants showed a higher correlation between actual and perceived risk when viewing blocks (r=0.42) compared to restroom icons (r=0.20), likely because blocks fuse into a single visual area that is easier to process than distinct countable items [@zikmund-fisher_blocks_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** It requires gender-matching or creating neutral anthropomorphic figures, which is more production work than generating standard squares.
*   **The Risk:** If the icons are too complex (e.g., actual photographs), they perform similarly to restroom icons but are significantly harder to scale and produce dynamically [@zikmund-fisher_blocks_2014].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using standard geometric shapes (blocks or ovals) because they look "cleaner."
*   **Why it fails:** Abstract shapes result in lower data recall and lower user preference scores. They fail to leverage the user's emotional or cognitive connection to the "person" being represented [@zikmund-fisher_blocks_2014].
*   **The Wrong Fix:** Using actual photographs of people.
*   **Why it fails:** While photographs performed similarly to restroom icons in recall and preference, they conferred no additional performance advantage and introduce significant practical difficulties in matching race/gender/appearance to the user [@zikmund-fisher_blocks_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart look like a grid of bricks or eggs?
*   **The Test:** Ask a user, "Who does this chart represent?" If they say "blocks" or "shapes" rather than "people," the icon type is too abstract.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace rectangles or circles with a standard SVG "user" or "restroom" icon.
*   **Best Fix:** Implement a dynamic icon array that uses stylized person outlines, ensuring distinct gaps (white space) between figures to allow for counting.
