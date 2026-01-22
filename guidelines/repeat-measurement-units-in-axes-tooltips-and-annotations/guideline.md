---
id: repeat-measurement-units-in-axes-tooltips-and-annotations
title: Repeat measurement units in axes, tooltips, and annotations
bibliography: references.bib
description: Make units unmistakable by showing them wherever values appear, not only
  in a title or caption.
labels:
- chart:general
- task:interpret
- visual:text
- impact:clarity
- data:quantitative
- audience:novice
- complexity:basic
---

## Repeat units everywhere values appear <!-- role: advice -->

Show the unit in axis labels, tooltips, and annotations, not just in the description. Prefer readable number formats that encode scale directly rather than forcing readers to apply multipliers.

## Units prevent interpretation errors and reduce mental math <!-- role: reason -->

When units appear only in one place, readers can miss them or forget them while inspecting values elsewhere. Repeating units and expressing scale in the number format keeps meaning attached to the numbers at the moment of reading.

**Mechanism:** Redundant unit cues reduce ambiguity and working-memory demands when readers move between chart elements.

**Evidence:** Units should be made obvious by repeating them across axis labels, tooltips, and annotations so readers don’t need to infer or remember them from distant text [@muth_text_in_data_visualizations_2022].

**Notes:** Avoid “in thousands/millions” when a compact numeric format can express the same scale directly.

## Apply when values are read in multiple places <!-- role: context -->

- **User Goal:** Understand what a number means without hunting for context.
- **Task:** Read exact or approximate values from axes, labels, annotations, or hover states.
- **Data:** Quantitative measures with units (currency, percent, people, tons, etc.) and/or scaled values.
- **Chart Setting:** Charts with tooltips, multiple annotations, or small multiples where context can be lost.
- **Audience:** Mixed literacy audiences; readers skimming quickly.
- **Success Criterion:** Readers can state both value and unit correctly without referencing the caption.

## When repetition can be reduced <!-- role: exceptions -->

**Break it when:** The unit is visually and unavoidably attached to every value already (for example, every label includes the unit and there are no other value readouts). **Why:** Repetition can become redundant and consume space without adding clarity.

## Extra text can crowd the display <!-- role: costs -->

**Sacrifice:** Slightly longer labels and tooltips. **Risk:** Overly verbose units can clutter tight layouts. **Mitigation:** Use standard abbreviations and concise formats while keeping the unit explicit.

## Typical failure modes <!-- role: mistakes -->

**Mistake:** Putting the unit only in a subtitle or note while axes and tooltips show bare numbers. **Why it fails:** Readers can misinterpret values or forget the unit while exploring the chart.

## Quick checks <!-- role: check -->

**Failure Sign:** A value shown in a tooltip or annotation could plausibly be mistaken for a different unit or scale. **Quick Check:** Scan the chart without reading the description; if units are unclear, they are not repeated enough. **Stronger Test:** Ask a reader what unit a specific data point uses; uncertainty indicates missing cues.

## What to do instead when space is tight <!-- role: fix -->

- Add the unit to axis titles and tooltip text, even if it also appears in the description.
- Use compact number formats that encode scale directly rather than “in thousands/millions.”
- Move less-important unit explanations into a note while keeping the unit visible where values are read.
- Remove low-priority labels and rely on tooltips to preserve unit context without clutter.
