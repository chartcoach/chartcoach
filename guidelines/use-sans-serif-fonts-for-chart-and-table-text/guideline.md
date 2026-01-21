---
id: use-sans-serif-fonts-for-chart-and-table-text
title: Use Sans-Serif Typefaces for Chart and Table Text
bibliography: references.bib
description: Default to a readable sans-serif typeface for chart labels and numbers;
  use serif sparingly and deliberately.
labels:
- chart:general
- task:read
- visual:typography
- impact:clarity
- data:general
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use a sans-serif typeface for the text in charts and tables; only use serif typefaces intentionally (often just for headlines).

## The Logic <!-- role: reason -->

Sans-serif typefaces tend to look cleaner and are easier to skim in visualization contexts, especially for numeric labels and ticks, which supports faster scanning and reduces reading friction in dense chart UI text [@muth_fonts_2022].

- **The Principle:** Skimmability for interface-like text
- **The Evidence:** [@muth_fonts_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly scanning labels, values, axis ticks, and annotations
- **Data Type:** Any chart/table with frequent short labels and numbers
- **Audience:** General audiences reading on screens (web-first)

## When to Break It <!-- role: exceptions -->

- **Scenario:** You want a more traditional/classy editorial tone or brand differentiation.
- **Reason:** Serif typefaces can communicate “classy, traditional, serious/professional” and can help a visualization stand out—most commonly when limited to titles/headlines [@muth_fonts_2022].
- **Scenario:** Your organization’s house style is strongly serif-led.
- **Reason:** Using the organization’s serif for visualization titles can increase recognizability and consistency with surrounding editorial design [@muth_fonts_2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less distinctive “personality” (common sans-serifs won’t make the chart stand out).
- **The Risk:** Over-reliance on default sans-serif choices can make a visualization feel generic [@muth_fonts_2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using decorative categories (script/handwritten/slab/monospace) as a default for chart text.
- **Why it fails:** These font categories are rarely used in data visualization and can introduce unnecessary style signals that compete with the data [@muth_fonts_2022].
- **The Wrong Fix:** Using serif fonts everywhere (including ticks and table values) without a deliberate reason.
- **Why it fails:** It can reduce skimmability for numbers and dense UI text compared to a clean sans-serif default [@muth_fonts_2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Labels and numeric ticks feel “busy” or slow to scan, or the typography draws more attention than the data.
- **The Test:** Do a fast scan for key values (ticks, table columns) and see if you can read them effortlessly without slowing down; if not, try a neutral sans-serif and compare [@muth_fonts_2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch labels/numbers to a standard, normal-width sans-serif (e.g., the kind commonly used on the web) [@muth_fonts_2022].
- **Best Fix:** Use a sans-serif for all functional chart text, and (only if needed) apply a serif selectively to headlines/titles for tone or branding [@muth_fonts_2022].
