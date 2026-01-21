---
id: keep-color-key-within-view-or-repeat-it
title: Keep the Color Key Within View or Repeat It
bibliography: references.bib
description: Ensure readers can always look up color-to-category mappings by keeping
  the key nearby or repeating it as they move through the visualization.
labels:
- chart:multi
- task:interpret
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- format:scroll
- component:legend
---

## The Rule <!-- role: advice -->

Keep your color key close to the data at all times: place it on the same page (print) or within roughly one screen of scrolling (digital), and repeat it as needed.

## The Logic <!-- role: reason -->

This reduces the effort of remembering and re-checking color-category associations while reading, and prevents long “eye-travel” between marks and legend that interrupts comprehension. The blog post notes that even attentive readers repeatedly look back to the key and benefit from seeing it multiple times rather than hunting for it.

- **The Principle:** Minimize lookup distance and memory load for categorical color mappings
- **The Evidence:** [@muth_remind_colors_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Decode what colors mean while scanning and interpreting the chart
- **Data Type:** Categorical encodings using multiple distinct colors
- **Audience:** General readers, especially first-time viewers of the graphic
- **Format Fit:** Long/tall charts, multi-panel graphics, and articles where the visualization is scrolled

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization directly labels categories on the marks (so a separate key is unnecessary).
- **Reason:** If color meaning is already explicit at the point of reading, a repeated key adds redundancy without improving understanding (the post frames proximity/repetition as solutions when readers need to check mappings). [@muth_remind_colors_2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** More space used for repeated legend elements.
- **The Risk:** Visual clutter or reduced room for the data if repetition is overdone. [@muth_remind_colors_2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing the legend only once at the top or bottom of a long visualization.
- **Why it fails:** Readers still need to re-check mappings while reading; making them scroll/search increases friction and confusion in the moment they need the key. [@muth_remind_colors_2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Large stretches of chart where no legend is visible.
- **The Test:** Scroll through the piece: at any point, can you confirm a color’s meaning without scrolling more than about one screen? If not, you’ve broken the rule. [@muth_remind_colors_2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Repeat the same color key above/beside each major section or panel.
- **Best Fix:** Make the color key sticky so it stays visible as readers scroll (top, bottom, or side). [@muth_remind_colors_2023]
