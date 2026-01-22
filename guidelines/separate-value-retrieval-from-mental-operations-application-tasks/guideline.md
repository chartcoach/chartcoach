---
id: separate-value-retrieval-from-mental-operations-application-tasks
title: Separate value retrieval tasks from application tasks that require computation
bibliography: references.bib
description: Measure point reading and computation separately because design effects
  can differ across these skills.
labels:
- chart:general
- task:retrieve
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- method:user-study
---

## Test value lookup and computed answers as different outcomes <!-- role: advice -->

Use one question that only requires locating a single value (knowledge), and a separate question that requires operating on two values (application), such as computing a difference.

## Why computation can mask design effects that appear in lookup <!-- role: reason -->

Reading a value and transforming values are different skills; a design can improve lookup accuracy without improving performance on multi-step operations. Separating them avoids concluding “no effect” just because an application task is difficult.

**Mechanism:** Application tasks add steps (multiple lookups plus arithmetic), increasing opportunities for error unrelated to the chart’s basic legibility and potentially reducing sensitivity to design differences.

**Evidence:** Redesigns improved accuracy on knowledge (single-value retrieval) questions across chart topics, but did not produce a significant improvement on application questions requiring differences between values [@burnsHowEvaluateData2020]. Performance on knowledge predicted performance on application, consistent with overlap in required subskills, but this dependency did not extend to higher-level tasks like trend description [@burnsHowEvaluateData2020].

**Notes:** Treat application outcomes as transfer/operation performance, not a proxy for basic readability.

## When to split retrieval from application <!-- role: context -->

- **User Goal:** Understand whether a design improves legibility, reasoning, or both.
- **Task:** Read exact/extreme values; compute differences or other derived quantities.
- **Data:** Quantitative values where arithmetic operations are plausible user tasks.
- **Chart Setting:** Static charts in surveys or experiments.
- **Audience:** Mixed numeracy; crowdsourced samples.
- **Success Criterion:** Detect design effects on lookup separately from effects on computation.

## When not to separate them <!-- role: exceptions -->

**Break it when:** Your real-world use case never requires numeric operations (only gist-level interpretation). **Why:** Application questions may test skills irrelevant to the intended decision-making context.

## Tradeoffs of splitting task types <!-- role: costs -->

**Sacrifice:** More questions and time per chart. **Risk:** Participants may fatigue and reduce response quality in later questions. **Mitigation:** Keep prompts short and ensure each question targets a distinct skill.

## Common mistakes when mixing retrieval and application <!-- role: mistakes -->

**Mistake:** Using only a computation question to infer readability. **Why it fails:** Errors can come from arithmetic or multiple lookups even if single-value reading is improved.

## Quick checks to validate task separation <!-- role: check -->

**Failure Sign:** Participants often get the computed answer wrong but can correctly name the component values when asked directly.\
**Quick Check:** Ensure the retrieval question can be answered without any arithmetic or comparison.\
**Stronger Test:** Analyze whether retrieval correctness predicts computation correctness; if so, treat them as related but distinct measures.

## What to do instead when you must use only one task <!-- role: fix -->

- Use a single-value retrieval task if basic decoding is the primary goal.
- Use a computation task only if the real-world task explicitly requires derived values.
- Provide a calculator or reduce arithmetic complexity if you specifically want to test chart-based value access rather than numeracy.
- Add a follow-up asking for the two component values to separate lookup errors from arithmetic errors.
