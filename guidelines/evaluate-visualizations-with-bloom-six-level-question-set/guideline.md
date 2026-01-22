---
id: evaluate-visualizations-with-bloom-six-level-question-set
title: Evaluate a visualization with one question per Bloom level (knowledge through
  evaluation)
bibliography: references.bib
description: "Use a six-question set mapped to Bloom\u2019s taxonomy to measure multiple\
  \ levels of understanding from a visualization."
labels:
- chart:general
- task:evaluate
- visual:general
- impact:clarity
- data:general
- audience:general
- method:user-study
---

## Use six Bloom-mapped questions to evaluate understanding outcomes <!-- role: advice -->

Evaluate each visualization using a fixed set of six questions, each targeting a different Bloom level: knowledge, comprehension, application, analysis, synthesis, and evaluation. Ask the questions in that order to cover both fact extraction and higher-level reasoning.

## Why Bloom-level coverage reveals different understanding gaps <!-- role: reason -->

A visualization can support some kinds of understanding (like reading a value) while failing at others (like describing a trend, making a prediction, or justifying a decision). Mapping questions to Bloom’s levels creates systematic coverage of distinct cognitive objectives so you can detect where a design changes what viewers can do and conclude.

**Mechanism:** Separating evaluation into multiple learning objectives reduces the chance that a study only measures low-level perceptual decoding, and increases the chance of detecting design effects that only appear in higher-level tasks (e.g., trend characterization, prediction, policy justification).

**Evidence:** A six-level Bloom-based question set detected design differences that would have been missed by accuracy/speed-style evaluation alone, including cases where redesigns changed what patterns people noticed or how they described trends [@burnsHowEvaluateData2020]. Across three real-world case studies, different chart versions produced differences at some Bloom levels but not others, motivating multi-level evaluation rather than relying on a single task type [@burnsHowEvaluateData2020].

**Notes:** The levels functioned more like complementary skills than a strict hierarchy in these case studies.

## When a Bloom-level evaluation is the right fit <!-- role: context -->

- **User Goal:** Compare visualization designs by what viewers understand and can do with the information.
- **Task:** Measure understanding beyond point reading (e.g., trend description, prediction, justification, decision argument).
- **Data:** Any, especially when misinterpretation risk is high (temporal patterns, multi-variable relationships, distributions).
- **Chart Setting:** Static or interactive; remote studies are feasible with text responses.
- **Audience:** General audiences or mixed literacy; suitable for crowdsourced participants.
- **Success Criterion:** Differences in comprehension, reasoning, and decision support—not just perceptual accuracy.

## When not to use all six levels <!-- role: exceptions -->

**Break it when:** Your evaluation goal is strictly perceptual decoding (e.g., low-level channel discrimination only). **Why:** Higher-level questions test broader reasoning and transfer, not just encoding legibility, and may add noise relative to a narrowly scoped perceptual question.

## Tradeoffs and risks of six-level evaluation <!-- role: costs -->

**Sacrifice:** More participant time and more qualitative analysis effort than a single-task study. **Risk:** Open-ended responses require coding decisions that can introduce subjectivity. **Mitigation:** Use a pre-defined coding scheme or blind coding to chart condition to reduce bias.

## Common ways Bloom-level evaluations fail in practice <!-- role: mistakes -->

- **Mistake:** Evaluating only value-retrieval accuracy and calling it “understanding.” **Why it fails:** It can miss differences in conclusions, trend interpretation, prediction, or justification that vary by design.
- **Mistake:** Using only open-ended prompts without structure. **Why it fails:** It can create overwhelming qualitative volume and make comparisons less systematic across designs.

## Quick tests to see if your evaluation covers understanding <!-- role: check -->

**Failure Sign:** Two designs look “equivalent” on accuracy but clearly lead to different takeaways or decisions in practice.\
**Quick Check:** Verify you have at least one question each for: value retrieval, summary/takeaway, trend/relationship, prediction, and justification.\
**Stronger Test:** Pilot both designs and check whether differences appear at any Bloom level even when low-level accuracy is similar.

## What to do instead when six questions are too heavy <!-- role: fix -->

- Use only the Bloom levels that match your communication goal (e.g., comprehension + analysis + evaluation) and drop others.
- Keep one closed-ended question for knowledge/application and pair it with one open-ended question for analysis or evaluation.
- Replace free-form prompts with constrained prompts that still target the same Bloom level (e.g., “describe the trend in one sentence”).
- If you cannot code qualitative data, redesign the Bloom questions into multiple-choice variants that preserve the targeted level.
