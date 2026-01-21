---
id: repeatedly-state-the-risk-time-interval
title: Repeatedly State the Risk Time Interval
bibliography: references.bib
description: Continuously reinforce the time horizon (e.g., 5-year vs lifetime) because
  people often ignore time and misjudge magnitude.
labels:
- task:explain
- impact:clarity
- impact:fairness
- audience:novice
- data:temporal
- data:risk
- domain:health
- source:fagerlinHelpingPatientsDecide2011
---

## The Rule <!-- role: advice -->

Repeat the time interval every time you state a risk (e.g., “5-year risk,” “10-year risk,” “lifetime risk”) and do not rely on a single legend.

## The Logic <!-- role: reason -->

People often ignore the time element and focus only on the ratio magnitude; changing the displayed time horizon can bias perceived effectiveness, and visuals frequently fail to foreground time.

- **The Principle:** Prevent temporal neglect in probability judgments
- **The Evidence:** The paper reports robust inattention to time, including biased perceptions when survival graphs show longer vs shorter intervals; pictographs and other visuals often relegate time to easy-to-miss legends [@fagerlinHelpingPatientsDecide2011].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare risks/benefits fairly across treatments and horizons.
- **Data Type:** Any risk statistic tied to a period (5-year, 10-year, 15-year, lifetime) including survival/mortality outcomes.
- **Audience:** Patients interpreting cancer risk, screening benefit, or treatment outcomes.

## When to Break It <!-- role: exceptions -->

- **Scenario:** None stated in the paper.
- **Reason:** Not specified.

## The Price <!-- role: costs -->

- **The Sacrifice:** Repetition increases text density and can feel redundant.
- **The Risk:** If different parts of the material use different horizons without clear signaling, confusion increases.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Mentioning the time horizon once in a footnote/legend and then listing multiple risks without time labels.
- **Why it fails:** Users may ignore time and compare ratios as if they share the same interval [@fagerlinHelpingPatientsDecide2011].
- **The Wrong Fix:** Showing survival curves with different time spans across options without emphasizing the span.
- **Why it fails:** Perceived effectiveness can be biased by the length of time displayed [@fagerlinHelpingPatientsDecide2011].

## How to Check <!-- role: check -->

- **Visual Sign:** Risk numbers appear without an adjacent “over X years” phrase; time is only in a caption.
- **The Test:** Remove captions/legends mentally—if time disappears, users will likely miss it too.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Append “over X years” directly to every risk statement and axis label.
- **Best Fix:** Present the same risk at multiple time intervals when appropriate (e.g., 5-, 10-, 20-year) to force attention to accumulation over time [@fagerlinHelpingPatientsDecide2011].
