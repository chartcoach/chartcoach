---
id: validate-with-colorblind-people-when-accessibility-matters
title: Ask Colorblind Readers to Review Your Chart
bibliography: references.bib
description: Get feedback from colorblind people to confirm your visualization is
  decipherable beyond what simulators can guarantee.
labels:
- chart:multi
- task:review
- impact:accessibility
- visual:process
- data:any
- audience:general
- source:datawrapper
---

## The Rule <!-- role: advice -->

Before publishing, ask at least one colorblind person to try reading your chart and report where they get confused.

## The Logic <!-- role: reason -->

Tools and simulations are imperfect and individuals vary; direct feedback from the intended audience is the most reliable way to catch ambiguity and confirm that your encodings work in practice [@muth_colorblindness_2020].

- **The Principle:** User validation beats theoretical compliance for perception-dependent design
- **The Evidence:** The post explicitly recommends asking colorblind people, noting variability and offering ways to find reviewers; it also cautions not to rely too much on simulators [@muth_colorblindness_2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Avoid misinterpretation and ensure inclusive readability
- **Data Type:** Any visualization where color encodes meaning
- **Audience:** Public or diverse audiences; high-stakes communication [@muth_colorblindness_2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You’re doing rapid internal exploration where accessibility isn’t a requirement yet
- **Reason:** Review time may not be justified until nearing publication [@muth_colorblindness_2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Time and coordination to recruit reviewers and iterate
- **The Risk:** Conflicting feedback across individuals may require prioritization and additional redesign [@muth_colorblindness_2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating simulation screenshots as “proof” and skipping human review
- **Why it fails:** Simulations are approximations and don’t represent all individual experiences [@muth_colorblindness_2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Reviewers hesitate, mislabel categories, or need repeated explanation
- **The Test:** Give the chart without guidance and ask the reviewer to describe the main takeaway and how they identified categories [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase lightness contrast and add direct labels for the most important elements based on feedback
- **Best Fix:** Add a redundant non-color encoding (symbols, patterns, dashes) and simplify the color scheme until reviewers report effortless decoding [@muth_colorblindness_2020].
