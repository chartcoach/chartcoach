---
id: prefer-pictograph-data-marks-when-working-memory-is-loaded
title: Prefer Pictograph Data Marks When Working Memory Is Loaded
bibliography: references.bib
description: Under memory load (intervening charts), pictograph-based charts improve
  recall compared to simple shapes.
labels:
- chart:bar
- task:recall
- visual:glyph
- impact:memorability
- data:categorical
- audience:general
- context:multi-view
- source:haroz-chi2015
---

## The Rule <!-- role: advice -->

When viewers must remember values across multiple successive charts (memory under load), use pictographs as the data marks rather than simple geometric shapes.

## The Logic <!-- role: reason -->

Under load, similar numeric encodings can interfere in memory; pictographs provide additional identity/shape cues that help keep datasets distinct and improve recall accuracy.

- **The Principle:** Richer, more differentiated encoding reduces interference
- **The Evidence:** In a 1-back working-memory task (remember the previous chart while viewing the next), pictograph charts produced lower error than shape-based charts (Exp. 3) [@harozISOTYPEVisualizationWorking2015a].

## Where to Apply <!-- role: context -->

- **User Goal:** Remember chart values while also processing other charts or information
- **Data Type:** Sequences of small categorical charts (e.g., repeated 3-bar charts) with distinct categories
- **Audience:** Readers comparing successive graphics; viewers multitasking or switching context

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is rapid value lookup where memory load is minimal and labels must be maximally efficient
- **Reason:** The paper’s strongest pictograph memory advantage appears under load; in simpler immediate recall (Exp. 1) pictographs did not improve accuracy, and pictograph axis labels hurt [@harozISOTYPEVisualizationWorking2015a].

## The Price <!-- role: costs -->

- **The Sacrifice:** More complex marks and potential styling overhead (icon selection/consistency)
- **The Risk:** Poorly chosen or ambiguous pictographs could reduce distinctiveness (the benefit depends on clear, discriminable symbols) [@harozISOTYPEVisualizationWorking2015a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding pictographs as decoration while leaving the data marks as plain bars
- **Why it fails:** Superfluous imagery harmed performance; the observed benefit requires pictographs to encode the data marks [@harozISOTYPEVisualizationWorking2015a].

## How to Check <!-- role: check -->

- **Visual Sign:** Each category/value is represented by a distinct pictographic mark (not just a shared background)
- **The Test:** Run a simple 1-back recall check: show chart A, then chart B, then ask for chart A’s values; compare pictograph vs shape marks [@harozISOTYPEVisualizationWorking2015a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap geometric marks for clearly distinguishable pictograph marks while preserving the same scale and layout.
- **Best Fix:** Use pictographs consistently as the primary encoding for category identity across a sequence of related charts to reduce cross-chart interference [@harozISOTYPEVisualizationWorking2015a].
