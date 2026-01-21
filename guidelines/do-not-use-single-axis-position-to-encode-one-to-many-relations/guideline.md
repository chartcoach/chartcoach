---
id: do-not-use-single-axis-position-to-encode-one-to-many-relations
title: Avoid Single-Axis Position Encodings for One-to-Many Relations
bibliography: references.bib
description: Do not use a single mark per key positioned on one axis when the key
  maps to multiple values.
labels:
- chart:dot
- task:show-relationships
- visual:position
- impact:correctness
- data:relational
- audience:any
- relation:one-to-many
- source:mackinlay-1986
---

## The Rule <!-- role: advice -->

Do not encode a one-to-many relation using a design where each key is represented by a single mark with a single position on an axis.

## The Logic <!-- role: reason -->

In a single-position language (e.g., marks positioned along one axis with each mark uniquely paired to a domain value), a mark cannot occupy two positions simultaneously; therefore one-to-many tuples cannot all be encoded without loss.

- **The Principle:** Single mark ↔ single position implies functional dependency
- **The Evidence:** The paper proves that one-to-many relations are not expressible in such a language (Theorem 1) [@mackinlayAutomatingDesignGraphical1986b].

## Where to Apply <!-- role: context -->

- **User Goal:** Show all associations from a key to multiple values (e.g., a category linked to multiple measurements/events)
- **Data Type:** One-to-many relations (same key appears with multiple distinct values)
- **Audience:** Any

## When to Break It <!-- role: exceptions -->

- **Scenario:** You change the semantic convention so marks represent tuples (not unique keys).
- **Reason:** The theorem depends on the convention that marks are uniquely paired with domain values; if marks represent tuples, multiple marks per key can exist [@mackinlayAutomatingDesignGraphical1986b].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need more marks (multiple per key) or a different chart type.
- **The Risk:** If you keep one mark per key, you will necessarily drop facts or overwrite values [@mackinlayAutomatingDesignGraphical1986b].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Aggregating multiple values into one without stating it (e.g., picking an arbitrary value).
- **Why it fails:** It changes the relation being presented and violates “encode all facts” [@mackinlayAutomatingDesignGraphical1986b].

## How to Check <!-- role: check -->

- **Visual Sign:** Multiple tuples share the same key, but the chart shows only one mark for that key.
- **The Test:** For any key with multiple values, ask: “Where are the other values drawn?” If there is no separate graphical element for them, the encoding is invalid [@mackinlayAutomatingDesignGraphical1986b].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use multiple marks per key (tuple-based marks) if your interpretation conventions support it.
- **Best Fix:** Choose a graphical language that can encode nonfunctional relations (e.g., use two positional dimensions or a connection-based representation, as appropriate) [@mackinlayAutomatingDesignGraphical1986b].
