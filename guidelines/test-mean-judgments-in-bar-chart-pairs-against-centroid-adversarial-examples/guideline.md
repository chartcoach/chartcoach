---
id: test-mean-judgments-in-bar-chart-pairs-against-centroid-adversarial-examples
title: Stress-test bar-chart mean comparisons with centroid-shift adversarial examples
bibliography: references.bib
description: Validate bar-chart mean comparison designs by checking whether centroid
  manipulations systematically mislead viewers.
labels:
- chart:bar
- task:compare
- visual:position
- impact:robustness
- data:categorical
- audience:general
- method:adversarial-testing
---

## Centroid adversarial stress test for mean judgments <!-- role: advice -->

Before relying on a bar-chart pair for “which has the larger mean?”, test the design with stimuli where the lower-mean chart has a more right-shifted bar-area centroid than the higher-mean chart.

## Why centroid shifts can mislead mean comparisons <!-- role: reason -->

Mean comparisons in bar charts can be swayed by perceptual proxies—simple spatial heuristics that the visual system may use instead of computing an arithmetic mean. Shifting the centroid of the filled bar area can create an impression of “more” even when the arithmetic mean is smaller, so a design that is vulnerable to this manipulation can mislead viewers.

**Mechanism:** The visual system may substitute a spatial summary (center of mass/centroid of the bar area along the value axis) for the arithmetic mean, causing centroid-shifted charts to be chosen more often.

**Evidence:** In a crowdsourced staircase experiment that pitted correct answers against adversarial proxy-optimized datasets, centroid manipulation showed the strongest evidence of increasing the mean-discrimination threshold relative to control, consistent with centroid acting as a deceptive proxy for MaxMean judgments [@ondovRevealingPerceptualProxies2021].

**Notes:** The effect was reported at the population level with additional individual differences; some participants were much more affected than others.

## When centroid stress tests apply <!-- role: context -->

- **User Goal:** Choose which of two categories/groups has the higher average level.
- **Task:** Forced-choice comparison of means across two bar charts (side-by-side lineup).
- **Data:** Two series with the same number of bars (the paper used seven) and comparable scale.
- **Chart Setting:** Brief-glance or time-limited viewing where viewers cannot compute values exactly.
- **Audience:** Mixed literacy audiences; expect heterogeneous strategies across individuals.
- **Success Criterion:** Robust correctness (or stable preference) even under adversarial centroid shifts.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Users can inspect exact values (e.g., labels, tables, or long untimed viewing) and the task expectation is computation rather than perceptual judgment. **Why:** The centroid proxy is most relevant when viewers must rely on fast perceptual heuristics rather than calculation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Creating centroid-adversarial stimuli and running a small validation adds time and experimental overhead. **Risk:** If you only test centroid, you may miss other deceptive proxies that affect your specific setting. **Mitigation:** Use centroid as a minimum viable stress test, then expand to additional proxies relevant to your task.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming that matching arithmetic means is sufficient to guarantee perceived equality in bar-chart pairs. **Why it fails:** Viewers may rely on perceptual proxies like centroid and can be pulled toward the wrong choice even when means differ in the correct direction [@ondovRevealingPerceptualProxies2021].

## Quick tests <!-- role: check -->

**Failure Sign:** In pilot trials, participants disproportionately pick the chart whose “mass” seems shifted toward larger values even when its mean is smaller. **Quick Check:** Generate a small set of paired charts where only the centroid proxy is strengthened in the lower-mean chart and see if accuracy drops. **Stronger Test:** Use a staircase/titration design to estimate the titer threshold shift relative to a control condition without proxy manipulation.

## What to do instead <!-- role: fix -->

- Increase redundancy by adding explicit mean markers (e.g., a mean line) so the intended statistic is visually anchored.
- Reduce reliance on fast perception by allowing longer viewing or providing value labels when correctness is critical.
- Compare means using a representation that directly encodes the mean as a single mark per group rather than requiring aggregation across multiple bars.
- Run additional adversarial tests against other plausible proxies (e.g., max-bar) if your data distributions make them likely competitors.
