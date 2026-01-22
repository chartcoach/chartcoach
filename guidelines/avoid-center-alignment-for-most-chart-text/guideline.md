---
id: avoid-center-alignment-for-most-chart-text
title: Avoid center-aligning chart text longer than a few words
bibliography: references.bib
description: Use left or right alignment to create clean edges and improve multi-line
  readability.
labels:
- chart:general
- task:read
- visual:text
- impact:clarity
- data:general
- audience:novice
- complexity:basic
---

## Left- or right-align chart text instead of centering it <!-- role: advice -->

Avoid center alignment for titles, descriptions, and multi-line annotations; use left or right alignment to create a clean edge. Reserve center alignment for very short text where line breaks are unlikely.

## Centered multi-line text is harder to scan and align visually <!-- role: reason -->

When lines are centered, each line starts in a different place, making it slower to find the next line and creating uneven edges that don’t align neatly with chart elements. Aligned text creates consistent vertical edges that can line up with other components in the layout.

**Mechanism:** Consistent line starts (or ends) improve reading flow and visual alignment with chart structures.

**Evidence:** Left- or right-aligned text looks tidier and is easier to read than center-aligned text, especially for longer passages [@muth_text_in_data_visualizations_2022].

**Notes:** Alignment also supports clean layout relationships between text blocks and chart boundaries.

## Apply to titles, subtitles, descriptions, and annotations <!-- role: context -->

- **User Goal:** Read explanatory text quickly and comfortably.
- **Task:** Read multi-line text and relate it to chart elements.
- **Data:** Any.
- **Chart Setting:** Any chart with text blocks that can wrap onto multiple lines.
- **Audience:** Broad audiences; especially skimmers.
- **Success Criterion:** Text blocks look tidy and are easy to scan line by line.

## When centering can work <!-- role: exceptions -->

**Break it when:** The text is very short and intentionally treated as a centered display element (for example, a single-word label). **Why:** With no wrapping, the readability penalty is minimal.

## Trade symmetry for readability <!-- role: costs -->

**Sacrifice:** Perfect visual symmetry in some layouts. **Risk:** Right alignment can feel odd for long passages in left-to-right reading contexts. **Mitigation:** Default to left alignment for longer text blocks and use right alignment selectively for edge alignment.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Center-aligning long annotations to “balance” the chart. **Why it fails:** Readers spend extra effort finding the start of each line, and the ragged edges look messy.

## Quick checks <!-- role: check -->

**Failure Sign:** Multi-line text has uneven left edges and looks jittery. **Quick Check:** If the text wraps to more than one line, it should almost never be centered. **Stronger Test:** Ask someone to read the annotation aloud; stumbling at line breaks indicates poor alignment.

## Better alternatives <!-- role: fix -->

- Left-align descriptive text blocks and align them with a chart edge.
- Use right alignment only when it creates a clean edge with nearby chart elements.
- Shorten text so it doesn’t wrap, if a centered display treatment is necessary.
- Move long explanations into a note below the chart where left alignment is natural.
