---
id: include-attention-checks-to-filter-non-engaged-responses-in-persuasive-viz-studies
title: Include attention-check questions tied to each evidence block to filter non-engaged
  responses
bibliography: references.bib
description: Attention checks help ensure measured persuasion reflects exposure to
  the evidence rather than random responding.
labels:
- chart:agnostic
- task:evaluate
- visual:text
- impact:validity
- data:survey
- audience:researcher
- method:experiment
---

## Add attention checks per evidence block before measuring post-attitude <!-- role: advice -->

Ask brief attention-check questions that can be answered only by reading each evidence block, and exclude participants who fail them from the persuasion analysis. Place these checks after the message exposure and before the post-treatment attitude question.

## Why attention checks protect persuasion estimates <!-- role: reason -->

If participants do not attend to the evidence, measured “attitude change” may reflect noise rather than a response to the presented data format, weakening or distorting comparisons between charts and tables.

**Mechanism:** Filtering out inattentive responses increases internal validity by ensuring the treatment was actually processed at least at a minimal level.

**Evidence:** The experiments analyzed persuasion outcomes only for participants who answered all attention-check questions correctly, and substantial portions of the sample were excluded based on these checks (varying by topic) before computing persuasion likelihood and attitude change [@pandeyPersuasivePowerData2014].

**Notes:** Exclusion can create imbalanced group sizes across treatments, so it should be planned and monitored.

## When this applies: comparative tests of persuasive formats <!-- role: context -->

- **User Goal:** Evaluate whether charts vs tables change attitudes.
- **Task:** Ensure treatment exposure occurred before measuring outcomes.
- **Data:** Multi-part message with several discrete evidence items.
- **Chart Setting:** Online study or self-paced reading where disengagement is plausible.
- **Audience:** Crowd-sourced or general audiences with variable effort.
- **Success Criterion:** Outcome measures reflect engaged processing of the message.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Attention checks would reveal answers that materially change the persuasion content or act as an additional intervention. **Why:** The checks can become part of the persuasive treatment rather than a measurement gate.

## Tradeoffs of attention checks <!-- role: costs -->

**Sacrifice:** Longer study time and higher participant dropout/exclusion. **Risk:** Excluding participants can unbalance treatment groups and reduce representativeness. **Mitigation:** Track exclusion rates by condition and ensure adequate remaining sample sizes.

## Common failure modes with attention checks <!-- role: mistakes -->

- **Mistake:** Using generic attention checks unrelated to the evidence content. **Why it fails:** Passing does not guarantee the participant processed the treatment message [@pandeyPersuasivePowerData2014].
- **Mistake:** Running analysis on all participants regardless of attention. **Why it fails:** Noise can swamp format effects and undermine conclusions about persuasion [@pandeyPersuasivePowerData2014].

## Quick checks for this guideline <!-- role: check -->

**Failure Sign:** Many responses show implausible patterns (e.g., very fast completion, random text feedback) while still being included. **Quick Check:** Compute pass rates for each evidence-linked attention check and compare across conditions. **Stronger Test:** Re-run primary analyses with and without the exclusion filter to assess robustness.

## What to do instead if attention checks are not possible <!-- role: fix -->

- Use time-on-page thresholds as a weak proxy for exposure and report sensitivity analyses.
- Add a short open-ended prompt asking what evidence they recall and filter empty or nonsensical replies.
- Reduce message length so that full processing is more likely without checks.
- Conduct a smaller moderated study to confirm engagement with the evidence presentation.
