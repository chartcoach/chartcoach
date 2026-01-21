---
id: avoid-using-standard-mturk-timings-for-fine-grained-response-time-claims
title: Do Not Rely on Standard MTurk Page Timing for Fine-Grained Response Time Analysis
bibliography: references.bib
description: Standard HIT timing is too noisy for seconds-level reaction-time conclusions
  in perception studies.
labels:
- chart:multiple
- task:measure
- visual:multiple
- impact:validity
- data:quantitative
- audience:researcher
- method:crowdsourcing
---

## The Rule <!-- role: advice -->

Do not interpret response times collected from the standard Mechanical Turk HIT interface as precise measures of perceptual speed.

## The Logic <!-- role: reason -->

Heer & Bostock observed median per-trial times (~42s) far above the “few seconds” expected in lab settings, with large variance due to uncontrolled factors such as page loading, scrolling, inattention, and submission delays [@heerCrowdsourcingGraphicalPerception2010a]. This noise can swamp true perceptual timing effects.

- **The Principle:** Measurement contamination from uncontrolled interaction overhead
- **The Evidence:** Inflated and highly variable MTurk times; authors avoided timing-based recommendations [@heerCrowdsourcingGraphicalPerception2010a]

## Where to Apply <!-- role: context -->

- **User Goal:** Quantify speed-accuracy tradeoffs or compare conditions by reaction time
- **Data Type:** Short perceptual judgments (a few seconds in lab)
- **Audience:** Researchers using MTurk’s default task wrapper

## When to Break It <!-- role: exceptions -->

- **Scenario:** Effects are very large and robust even under noisy timing, and timing is a secondary outcome.
- **Reason:** Some coarse timing differences may still emerge, but precision is not defensible [@heerCrowdsourcingGraphicalPerception2010a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose a useful dependent measure (time) unless you build custom instrumentation.
- **The Risk:** Overengineering timing can reduce participation if the task feels unusual.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reporting MTurk “time to submit” as if it were reaction time.
- **Why it fails:** Submission time includes non-perceptual delays unrelated to the visualization condition [@heerCrowdsourcingGraphicalPerception2010a].

## How to Check <!-- role: check -->

- **Visual Sign:** Many trials take tens of seconds or minutes for tasks that should take ~2–5 seconds.
- **The Test:** Inspect the distribution of times; if medians and variance resemble those reported by Heer & Bostock, treat timing as contaminated [@heerCrowdsourcingGraphicalPerception2010a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Drop timing as a primary outcome; focus on accuracy/error.
- **Best Fix:** Implement your own embedded task UI and instrument timing internally (e.g., “ready-set-go” + JS timers) as suggested in [@heerCrowdsourcingGraphicalPerception2010a].
