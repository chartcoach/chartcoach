---
id: start-with-tool-default-palettes-before-inventing-new-ones
title: "Start With Your Tool\u2019s Default Palette Before Creating a New One"
bibliography: references.bib
description: Use the default palette in your visualization tool as a fast, often-accessible
  baseline, then customize only if needed.
labels:
- chart:all
- task:style
- visual:color
- impact:efficiency
- data:categorical
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use your charting tool’s default categorical colors as the first option, and only replace them when they fail your requirements (contrast, distinctness, meaning, or brand fit).

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Default palettes are pre-tested baselines for common use cases
- **The Evidence:** Muth explains that default palettes are the easiest way to get a “workable” palette; she highlights that many tools start with medium/dark blue because it tends to be broadly acceptable and contrast-friendly, and notes some tools even prioritize contrast strongly (e.g., darker Excel/PowerPoint colors) [@muth_good_color_palettes_2024].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Get to a readable chart quickly without palette design overhead
- **Data Type:** Any categorical encoding where you need 1–10+ distinct colors
- **Audience:** General/public-facing charts where accessibility and clarity matter

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** Your tool’s defaults don’t meet your constraints (e.g., too low contrast on your background, not colorblind-safe enough for your combination, or wrong associations for the topic)
- **Reason:** Muth cautions that even “data vis” palettes (including defaults) can still be a poor fit for your specific case [@muth_good_color_palettes_2024].
- **Scenario:** You need a palette aligned with an organizational style guide
- **Reason:** Defaults may conflict with established brand colors and design standards [@muth_good_color_palettes_2024].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Less uniqueness and brand differentiation
- **The Risk:** Relying on defaults can produce generic-looking visuals or mismatched tone if your topic needs specific associations [@muth_good_color_palettes_2024].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Replacing defaults immediately with a trendy palette from a palette website without checking suitability
- **Why it fails:** Many non–data-vis palettes are built for background + accent roles and can create unequal importance or low contrast in charts [@muth_good_color_palettes_2024].
- **The Wrong Fix:** Assuming a tool’s dynamic palette will always work for any number of categories
- **Why it fails:** Muth notes some tools change palettes with category count; colors that worked at 2 categories may not behave the same at 4+ [@muth_good_color_palettes_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** Defaults produce barely visible marks (especially light colors on white) or categories that are hard to tell apart
- **The Test:** Run a colorblind check and a contrast check against your background; inspect small marks/lines and the legend key at reduced size [@muth_good_color_palettes_2024].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Keep the default palette but swap or tweak only the failing colors (e.g., darken the lightest color, replace near-duplicate hues) [@muth_good_color_palettes_2024].
- **Best Fix:** Use defaults as a baseline, then design a custom palette that preserves their accessibility intent (contrast + distinctness) while matching your topic/brand [@muth_good_color_palettes_2024].
