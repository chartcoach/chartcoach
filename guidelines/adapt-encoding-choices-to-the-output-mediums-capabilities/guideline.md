---
id: adapt-encoding-choices-to-the-output-mediums-capabilities
title: Adapt Encodings to the Output Medium (Color vs Monochrome)
bibliography: references.bib
description: Choose encodings that the target medium can render distinctly; change
  chart designs when channels like color are unavailable.
labels:
- chart:any
- task:adapt
- visual:color
- impact:accessibility
- data:ordinal
- audience:any
- medium:capabilities
- source:mackinlay-1986
---

## The Rule <!-- role: advice -->

Select encodings (and even chart types) based on what the output medium can reliably differentiate—especially whether color is available.

## The Logic <!-- role: reason -->

Effectiveness depends on both human perception and the medium’s capabilities; removing a channel (like color) can invalidate a previously effective composite design and force a different composition strategy. The paper’s APT examples show color enables ordinal encoding via hue, while monochrome can force a switch to aligned bar charts when grayscale discrimination is insufficient or encodings conflict.

- **The Principle:** Media-sensitive effectiveness: match encodings to available channels
- **The Evidence:** The paper’s media sensitivity section contrasts color scatter plot vs monochrome aligned bars due to channel availability and conflicts [@mackinlayAutomatingDesignGraphical1986b].

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly distinguish ordinal/nominal classes and read values on the target device
- **Data Type:** Multivariate relations requiring retinal encodings (e.g., ordinal categories like “Great…Terrible”)
- **Audience:** Any, especially when outputs vary (print, screen)

## When to Break It <!-- role: exceptions -->

- **Scenario:** The application can guarantee interaction for details (so some encodings can be deferred) rather than requiring all information in static form.
- **Reason:** The paper notes static labeling/detail has tradeoffs; interactive retrieval can change what must be encoded directly [@mackinlayAutomatingDesignGraphical1986b].

## The Price <!-- role: costs -->

- **The Sacrifice:** Different media may require different designs; consistency across outputs may be reduced.
- **The Risk:** Reusing a color-dependent design in monochrome can collapse distinctions (e.g., ordinal levels blending) or force conflicting encodings [@mackinlayAutomatingDesignGraphical1986b].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Converting color to multiple gray levels for many ordinal categories without checking discriminability.
- **Why it fails:** The paper notes multiple grays can blend, making ordinal values hard to distinguish [@mackinlayAutomatingDesignGraphical1986b].

## How to Check <!-- role: check -->

- **Visual Sign:** Categories that should be distinct look the same on the target medium (e.g., grayscale levels indistinguishable).
- **The Test:** Render using the actual medium constraints (e.g., monochrome) and verify that all encoded levels remain clearly differentiable [@mackinlayAutomatingDesignGraphical1986b].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace color encodings with an alternative available channel that remains distinguishable under constraints.
- **Best Fix:** Switch composition strategy (e.g., from mark composition using color to single-axis composition with aligned bars) when channel constraints or conflicts prevent an effective merged design [@mackinlayAutomatingDesignGraphical1986b].
