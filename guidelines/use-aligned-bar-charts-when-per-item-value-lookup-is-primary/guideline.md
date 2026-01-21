---
id: use-aligned-bar-charts-when-per-item-value-lookup-is-primary
title: Use Aligned Bar Charts for Per-Item Value Lookup Across Measures
bibliography: references.bib
description: When users must find values for specific items across multiple relations,
  align bar charts on the shared item axis.
labels:
- chart:bar
- task:lookup
- visual:position
- impact:clarity
- data:multivariate
- audience:any
- composition:single-axis
- source:mackinlay-1986
---

## The Rule <!-- role: advice -->

When item identity and per-item values are primary, present multiple measures as aligned bar charts sharing the same item axis.

## The Logic <!-- role: reason -->

Compared with labeled scatter plots, aligned bar charts make it easy to find the values associated with a particular item because item labels are directly aligned with each measure; this is a design variation chosen for effectiveness when item details must be present.

- **The Principle:** Choose a design variation that matches the user’s lookup task and preserves legible item detail
- **The Evidence:** The paper contrasts scatter plots vs aligned bar charts for the “car details required” case [@mackinlayAutomatingDesignGraphical1986b].

## Where to Apply <!-- role: context -->

- **User Goal:** Locate a specific item and read several of its values (lookup/inspection)
- **Data Type:** Multiple functional relations sharing the same item set (e.g., Cars → Price, Cars → Mileage, etc.)
- **Audience:** Any

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary goal is seeing overall correlations between measures (pattern detection).
- **Reason:** The paper notes aligned bars make general relationships harder to see than scatter plots [@mackinlayAutomatingDesignGraphical1986b].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced visibility of global relationships (e.g., correlation shape).
- **The Risk:** With many items, aligned bars can become long and harder to scan as a whole [@mackinlayAutomatingDesignGraphical1986b].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a scatter plot with heavy labeling to “support lookup.”
- **Why it fails:** Labels obscure marks and make finding individuals difficult; the design becomes less effective [@mackinlayAutomatingDesignGraphical1986b].

## How to Check <!-- role: check -->

- **Visual Sign:** Users repeatedly ask “where is item X?” or struggle to compare item X across multiple measures.
- **The Test:** Try to read 3–4 measures for a named item quickly; if it’s slow or error-prone in the current chart, aligned bars are indicated [@mackinlayAutomatingDesignGraphical1986b].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reformat into small multiples of bar charts aligned on the item axis.
- **Best Fix:** Use single-axis composition: keep a shared item axis and place each measure in its own aligned bar chart panel [@mackinlayAutomatingDesignGraphical1986b].
