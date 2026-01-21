---
id: compose-designs-by-merging-encodings-of-the-same-information
title: Compose Charts by Merging Encodings of Shared Information
bibliography: references.bib
description: When combining multiple relations, merge axes or marks that encode the
  same domain to reduce redundancy and improve integration.
labels:
- chart:any
- task:combine
- visual:composition
- impact:clarity
- data:relational
- audience:expert
- composition:algebra
- source:mackinlay-1986
---

## The Rule <!-- role: advice -->

When combining multiple views, compose them by merging the parts that encode the same domain information (shared axes or shared marks) instead of duplicating them.

## The Logic <!-- role: reason -->

A broad variety of designs can be generated systematically by composing primitive graphical languages; composition is guided by merging identical encodings (same information) to reduce redundancy and create unified presentations.

- **The Principle:** Principle of Composition (merge parts that encode the same information)
- **The Evidence:** The paper defines composition operators (double-axes, single-axis, mark composition) around this principle [@mackinlayAutomatingDesignGraphical1986b].

## Where to Apply <!-- role: context -->

- **User Goal:** See multiple relations together without redundant structure
- **Data Type:** Multiple relations sharing domain sets (e.g., same items, same axes ranges)
- **Audience:** Analysts/designers building multiview displays

## When to Break It <!-- role: exceptions -->

- **Scenario:** The merged parts would conflict (e.g., same retinal property encoding different variables) or create illegibility.
- **Reason:** Mark composition requires compatibility of constraints; conflicting encodings cannot be safely merged [@mackinlayAutomatingDesignGraphical1986b].

## The Price <!-- role: costs -->

- **The Sacrifice:** More constraints on what combinations are possible; may force alternate encodings.
- **The Risk:** Poorly chosen merges can cause clutter or interference among encodings [@mackinlayAutomatingDesignGraphical1986b].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Simply placing charts side-by-side without merging shared structure.
- **Why it fails:** It increases redundancy and makes it harder to perceive all information as one integrated presentation [@mackinlayAutomatingDesignGraphical1986b].

## How to Check <!-- role: check -->

- **Visual Sign:** Repeated axes or repeated item lists appear multiple times even though they represent the same domain.
- **The Test:** Identify whether two subviews encode the same domain set on an axis or mark set; if yes and they remain duplicated, composition is not being used [@mackinlayAutomatingDesignGraphical1986b].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Share axes when domains match (double-axes for identical x/y; single-axis for one shared axis).
- **Best Fix:** Use mark composition to merge mark sets when they encode the same domain value with compatible positional/retinal constraints [@mackinlayAutomatingDesignGraphical1986b].
