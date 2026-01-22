---
id: compare-generated-palettes-against-industry-benchmarks-on-error-and-preference
title: Validate categorical palettes against benchmark sets using both discrimination
  error and preference ratings
bibliography: references.bib
description: Evaluate palette quality by comparing discrimination accuracy and subjective
  preference against established benchmark palettes.
labels:
- chart:categorical
- task:evaluate
- visual:color
- impact:trust
- data:categorical
- audience:expert
- complexity:intermediate
---

## Benchmark palettes using both error and preference outcomes <!-- role: advice -->

Validate categorical palettes by comparing them to benchmark palette sets using both discrimination error and preference ratings, not only computed color metrics.

## Why benchmarking on human outcomes improves confidence <!-- role: reason -->

Computed palette scores can predict behavior, but benchmarking against common standards on measurable outcomes shows whether a method produces palettes that are competitive in real tasks and acceptable to viewers.

**Mechanism:** Discrimination tasks capture confusability under realistic chart conditions, while preference ratings capture acceptance; together they cover the main objectives the paper targets.

**Evidence:** In benchmark comparisons across ColorBrewer, Microsoft, Tableau, Random, and two generated settings, generated palettes were generally as discriminable and often more preferable than industry-standard palette sets, based on human error and preference ratings [@gramazioColorgoricalCreatingDiscriminable2017a]. The paper’s experiments show that palette scores correlate with behavioral measures but can vary by palette size and setting, supporting outcome-based validation [@gramazioColorgoricalCreatingDiscriminable2017a].

**Notes:** Use representative chart stimuli (e.g., maps) because discriminability depends on mark type and size.

## When this applies <!-- role: context -->

- **User Goal:** Decide whether a palette (or palette generator) is “good enough” for deployment.
- **Task:** Compare alternative palettes or methods under realistic usage.
- **Data:** Categorical color encodings.
- **Chart Setting:** Product or publication workflows where palette choice is reused.
- **Audience:** Teams accountable for both usability and appearance.
- **Success Criterion:** Comparable or improved discrimination error without worse preference than established benchmarks.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot run any user evaluation and must rely only on computed constraints. **Why:** Benchmarking requires collecting human responses.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Time to design stimuli and collect responses. **Risk:** Results may depend on the chosen chart context and participant sample. **Mitigation:** Use the same stimuli across palette sets and include multiple palette sizes if relevant.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Comparing only by a single numeric metric (e.g., distance) and declaring victory. **Why it fails:** The experiments show preference and discriminability can move in opposite directions.
- **Mistake:** Benchmarking only with swatches. **Why it fails:** Task context (map/mark size) affects discriminability outcomes.

## Quick tests <!-- role: check -->

**Failure Sign:** A palette “scores well” but performs poorly or is disliked when used in charts. **Quick Check:** Run a small side-by-side comparison against a known benchmark palette in the same chart. **Stronger Test:** Collect error rates on a discrimination task and preference ratings for multiple palettes per set.

## What to do instead <!-- role: fix -->

- Use a simple discrimination task that forces comparison of the most confusable pair in each palette.
- Collect preference ratings on the same chart stimuli without task-induced bias.
- Compare results across multiple palette sizes you expect to use.
- If a palette underperforms benchmarks, retune the discriminability–preference balance and re-test.
