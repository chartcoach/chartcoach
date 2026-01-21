---
id: iterate-with-user-centered-testing-to-avoid-curse-of-knowledge
title: Test with Representative Users and Iterate
bibliography: references.bib
description: Use quick user-centered design tests to catch misreadings caused by designer
  expertise.
labels:
- chart:any
- task:validate
- visual:process
- impact:decision-making
- data:any
- audience:novice
- complexity:advanced
---

## The Rule <!-- role: advice -->

Run quick tests with people like your target audience, gather feedback, and iterate the visualization until they can answer the intended questions reliably.

## The Logic <!-- role: reason -->

- **The Principle:** Designers suffer from the curse of knowledge and cannot accurately simulate novice interpretation; iteration exposes misreadings early.
- **The Evidence:** The paper argues that principles interact and that user-centered design—showing variants, asking viewers to answer key questions, iterating—efficiently improves effectiveness [@zacksDesigningGraphsDecisionMakers2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Ensuring the chart supports the real decisions/questions it’s meant to support.
- **Data Type:** Any, especially high-stakes policy/finance/health communication.
- **Audience:** Any non-identical-to-you audience (especially non-experts).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Trivial, low-stakes internal sketches where correctness is not required.
- **Reason:** The cost of testing may outweigh the benefit for throwaway drafts; the paper’s emphasis is on decision/communication effectiveness [@zacksDesigningGraphsDecisionMakers2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Time and coordination to recruit and run feedback sessions.
- **The Risk:** Feedback can conflict; you must decide which audience goals matter.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Relying on the designer’s own “it seems clear to me.”
- **Why it fails:** Your expertise makes intended interpretations feel obvious even when they aren’t [@zacksDesigningGraphsDecisionMakers2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Stakeholders interpret the chart differently or focus on irrelevant parts.
- **The Test:** Give the chart to a few representative viewers and ask them to answer the key decision questions without guidance; measure accuracy and time.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Show 2–3 alternative designs to a handful of users and choose the one that yields faster, more accurate answers.
- **Best Fix:** Establish a lightweight iteration loop (prototype → test → revise) as a standard step for decision-critical graphics [@zacksDesigningGraphsDecisionMakers2020].
