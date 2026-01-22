---
id: target-text-and-alt-text-to-ninth-grade-reading-level-or-lower
title: Write all text and alternative text at a ninth-grade reading level or lower
bibliography: references.bib
description: Keep all visible text and alternative text at a grade 9 reading level
  or below, defining any necessary jargon in simple language.
labels:
- chart:any
- task:read
- visual:text
- impact:accessibility
- data:any
- audience:general
- accessibility:cognitive
---

## Write all chart text at grade 9 or below <!-- role: advice -->

Write all visible text and alternative text for the visualization at a reading grade level of 9 or lower. If complex terminology is unavoidable, explain it using grade 9 language or below.

## Lower reading level reduces cognitive load and ambiguity <!-- role: reason -->

Lower reading levels make the meaning of chart instructions, captions, and alternative text easier to parse, reducing ambiguity and the working-memory effort needed to understand what the visualization is saying.

**Mechanism:** Shorter sentences and simpler word choices reduce cognitive load, helping people understand the visualization without spending extra effort decoding language.

**Evidence:** Reading level can be estimated with tools that assign a readability grade and highlight complex sentence structures to support writing at grade 9 or below [@hemingwayapp_hemingway_editor]. When complex or unfamiliar terms are necessary, providing definitions or supplementary explanations supports understanding for people with cognitive disabilities [@w3c_understanding_meaningful]. This requirement is treated as an Understandable, critical audit item for visualization accessibility [@elavskyHowAccessibleMy2022].

**Notes:** This applies to both on-screen text and non-visual text that assists access (such as alternative text).

## When to apply a ninth-grade reading level <!-- role: context -->

- **User Goal:** Understand what the visualization is about and what it implies.
- **Task:** Read titles, captions, instructions, annotations, legends, and alternative text to interpret the chart.
- **Data:** Any dataset, especially when interpretation depends on accompanying explanatory text.
- **Chart Setting:** Any visualization or data interface that contains textual content, including non-visual text for assistive technologies.
- **Audience:** Mixed audiences, including people with cognitive disabilities or limited familiarity with the topic language.
- **Success Criterion:** Users can understand the message and how to interpret the visualization without needing specialized reading skill.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The domain requires complex or unfamiliar terms to be accurate. **Why:** Replacing required terms can remove essential meaning, so the terms must remain but be defined or supplemented in simpler language [@w3c_understanding_meaningful].

## Tradeoffs of simplifying language <!-- role: costs -->

**Sacrifice:** Some precision or nuance may be harder to express concisely in plain language. **Risk:** Over-simplification can obscure important technical distinctions. **Mitigation:** Keep necessary terminology but add short, plain-language explanations alongside it [@w3c_understanding_meaningful].

## Common ways this fails in practice <!-- role: mistakes -->

- **Mistake:** Writing concise but jargon-heavy titles, captions, or alternative text without defining terms. **Why it fails:** Unfamiliar vocabulary increases ambiguity and comprehension effort, especially for people with cognitive disabilities [@w3c_understanding_meaningful].
- **Mistake:** Treating alternative text as a technical dump of terms and abbreviations. **Why it fails:** Alternative text is still read as language and can be inaccessible if it requires high reading proficiency [@elavskyHowAccessibleMy2022].

## How to quickly check reading level <!-- role: check -->

**Failure Sign:** Titles, captions, instructions, or alternative text contain dense sentences and unexplained terminology that is hard to read aloud smoothly. **Quick Check:** Run the text through a readability tool that returns an estimated grade level and flags complex sentences, then verify it is grade 9 or lower [@hemingwayapp_hemingway_editor]. **Stronger Test:** Identify any complex terms that must remain and confirm they have adjacent plain-language definitions or supplemental explanations [@w3c_understanding_meaningful].

## How to fix high reading level text <!-- role: fix -->

- Rewrite titles, captions, instructions, and alternative text until readability tools estimate grade 9 or lower [@hemingwayapp_hemingway_editor].
- Replace long sentences with shorter sentences and remove unnecessary modifiers and passive phrasing [@hemingwayapp_hemingway_editor].
- Keep required complex terms but add plain-language definitions or supplementary explanations near their first use [@w3c_understanding_meaningful].
- Apply the same reading-level constraint to both visible text and alternative text used for assistive access [@elavskyHowAccessibleMy2022].
