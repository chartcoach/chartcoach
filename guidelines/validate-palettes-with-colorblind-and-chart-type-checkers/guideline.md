---
id: validate-palettes-with-colorblind-and-chart-type-checkers
title: Validate Your Palette With Dedicated Checking Tools
bibliography: references.bib
description: "Use palette-checking tools (and your chart tool\u2019s built-in checks)\
  \ to detect colorblindness issues and insufficient distinction across chart types."
labels:
- chart:all
- task:validate
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Before publishing, run your palette through a dedicated palette-checker (and any built-in colorblind checks in your visualization tool) to confirm categories remain distinct in the chart types you’re using.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** External validation catches failures your eye misses in context
- **The Evidence:** Muth recommends checking colors with tools and calls out Viz Palette for testing distinguishability across chart types and colorblindness modes, and notes Datawrapper’s built-in colorblind check as an option for quick validation [@muth_good_color_palettes_2024].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Prevent misreading due to indistinguishable colors in real chart contexts
- **Data Type:** Any multi-category palette used in marks, lines, areas, or legends
- **Audience:** Broad audiences, including viewers with color vision deficiencies

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You’re doing very early exploration and speed matters more than polish
- **Reason:** The cost of checking may not be justified until you approach publication [@muth_good_color_palettes_2024].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Extra time and tool-switching (unless your tool has built-ins)
- **The Risk:** You may need to revise a palette you already like, delaying delivery [@muth_good_color_palettes_2024].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Only checking swatches in isolation (not in the actual chart marks/legend sizes)
- **Why it fails:** Distinctions that look fine as big swatches can fail at small sizes or in specific chart types [@muth_good_color_palettes_2024].
- **The Wrong Fix:** Assuming a “data vis palette” label guarantees accessibility
- **Why it fails:** Muth emphasizes that even palettes made for data visualization may not fit your case [@muth_good_color_palettes_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Confusing categories in the legend or overlapping marks; errors appear only in certain chart types (lines vs. areas)
- **The Test:** Run the palette through a tool like Viz Palette and a colorblind simulator; also inspect the palette directly in your intended chart types [@muth_good_color_palettes_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap out the most confusable color(s) and re-test until the checker shows clear separability [@muth_good_color_palettes_2024].
- **Best Fix:** Rebuild the palette with distinct lightness steps and balanced salience, then validate again across chart types and colorblind modes [@muth_good_color_palettes_2024].
