---
id: use-gray-to-deemphasize-and-highlight-with-color
title: Deemphasize most elements in gray and use color only for highlights
bibliography: references.bib
description: Reserve saturated color for what should attract attention and keep the
  rest visually quiet.
labels:
- chart:multi
- task:focus
- visual:color
- impact:clarity
- data:multi
- audience:general
- custom:highlighting
---

## Reserve color for emphasis and keep the rest gray <!-- role: advice -->

Render most marks in gray and apply strong color to only the elements you want readers to notice first.

## Why selective color directs attention <!-- role: reason -->

Using too many attention-grabbing colors makes everything compete; gray creates a low-salience baseline so color can function as a cue for what matters.

**Mechanism:** Visual attention is pulled toward higher-contrast, more saturated elements; neutral grays reduce competition and make highlighted marks pop.

**Evidence:** Color can guide the viewer’s eye by setting highlights, and gray can be used as a key baseline color so emphasis colors carry meaning rather than decoration [@muth_colorguide_2018].

**Notes:** This works best when the highlight has a clear message (a key series, an outlier, a focus region).

## When this applies in practice <!-- role: context -->

- **User Goal:** Quickly identify what is important in the chart without reading everything.
- **Task:** Locate a focus series/group/region and compare it against the rest.
- **Data:** Multiple series or many marks where only a subset matters.
- **Chart Setting:** Static charts and maps, especially in editorial/storytelling contexts.
- **Audience:** Time-constrained readers scanning for the main point.
- **Success Criterion:** Viewers’ first glance lands on the intended element, and supporting context remains readable.

## When not to follow it <!-- role: exceptions -->

**Break it when:** All categories are equally important and need equal visual weight. **Why:** Highlighting would introduce an unintended hierarchy.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You give up the ability to encode many categories with strong, separate colors. **Risk:** Overuse of gray can make the chart feel dull or hide important secondary patterns. **Mitigation:** Use restrained secondary accents or annotations when multiple points deserve attention.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Assigning vivid colors to every series. **Why it fails:** Nothing stands out, so color stops guiding attention.
- **Mistake:** Highlighting multiple unrelated elements at once. **Why it fails:** Competing highlights dilute the focus cue.

## Quick tests <!-- role: check -->

**Failure Sign:** A viewer cannot tell what to look at first. **Quick Check:** Squint at the chart; the intended highlight should remain the most salient element. **Stronger Test:** Show the chart for five seconds and ask what the main point is; check whether the answer matches your intended highlight.

## What to do instead <!-- role: fix -->

- Convert non-essential series or regions to neutral grays and keep their labels readable.
- Use one strong accent color for the primary focus and keep any secondary accents muted.
- Add direct annotations to clarify why the highlighted element matters.
- If multiple elements must be emphasized, split into small multiples so each panel can have a clear highlight.
