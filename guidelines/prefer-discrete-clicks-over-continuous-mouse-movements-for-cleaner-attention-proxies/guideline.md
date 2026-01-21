---
id: prefer-discrete-clicks-over-continuous-mouse-movements-for-cleaner-attention-proxies
title: Prefer Discrete Clicks Over Continuous Mouse Movements
bibliography: references.bib
description: Use BubbleView clicks instead of continuous mouse trajectories to reduce
  noise and converge faster to fixation-like maps.
labels:
- task:measure
- visual:attention
- impact:signal-quality
- audience:researcher
- method:BubbleView
- method:SALICON-comparison
- source:kimBubbleView2017
---

## The Rule <!-- role: advice -->

Collect discrete BubbleView clicks (not continuous cursor paths) when you want a cleaner proxy for attention with less post-processing.

## The Logic <!-- role: reason -->

Continuous mouse movements capture transitions and motion traces, which add noise and require thresholding/post-processing to infer “points of interest.” Clicks impose an effort barrier, making users more selective; BubbleView clicks matched or exceeded SALICON-style mouse movement performance at approximating fixations for feasible participant counts and required fewer participants to reach similar accuracy [@kimBubbleViewInterfaceCrowdsourcing2017].

- **The Principle:** Intentional action filters noise
- **The Evidence:** [@kimBubbleViewInterfaceCrowdsourcing2017]

## Where to Apply <!-- role: context -->

- **User Goal:** Build attention/importance maps efficiently; minimize cleaning.
- **Data Type:** Static images where you will aggregate across people.
- **Audience:** Researchers running online studies or building training data for models.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need denser sampling of exploration paths (including transitions), or interaction must be very fast/low-effort.
- **Reason:** Clicking is slower; movement-based capture is faster but noisier [@kimBubbleViewInterfaceCrowdsourcing2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Longer per-image viewing time to gather comparable coverage.
- **The Risk:** Important-but-subtle regions may be missed if participants avoid extra clicks [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to continuous movements to “get more data points.”
- **Why it fails:** More samples can mean more transition noise, not more meaningful attention points [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Heatmap shows streaks/paths rather than concentrated hotspots (typical of movement traces).
- **The Test:** Compare raw traces: if many samples occur during cursor travel between regions, your movement data is transition-heavy [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from movement capture to click capture.
- **Best Fix:** If movements are required, apply explicit discretization to remove transitions—then validate against fixation-like targets as in the paper’s evaluations [@kimBubbleViewInterfaceCrowdsourcing2017].
