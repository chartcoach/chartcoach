---
id: prefer-closed-shape-targets-when-users-must-selectively-attend-under-clutter
title: Prefer Closed Shapes for Targets in Cluttered Selective-Attention Situations
bibliography: references.bib
description: Closed shapes are processed faster and more accurately than open shapes
  when users must attend to a target among distractors.
labels:
- chart:scatter
- task:filter
- visual:shape
- impact:speed
- impact:accuracy
- data:categorical
- audience:general
- source:paper
---

## The Rule <!-- role: advice -->

If users must quickly pick out or respond to a “target” class amid distractors, encode that target with a **closed shape** rather than an open shape.

## The Logic <!-- role: reason -->

Closed shapes showed a processing advantage (faster RTs, fewer errors) in basic perceptual tasks, and closed targets were often more efficiently processed in the visualization setting when discrimination was required (notably for linear relationship judgments).

- **The Principle:** Differential processing efficiency by shape feature category.
- **The Evidence:** Experiments 1 and 2 found faster and more accurate responses for closed vs. open targets; Experiment 3 showed closed-target advantages in single-plot linear relationship judgments, with interactions depending on distractor family and difficulty [@burlinsonOpenVsClosed2018a].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly spotting, selecting, or focusing on one class while ignoring others (selective attention).
- **Data Type:** Dense or cluttered point displays; mixed-symbol single plots.
- **Audience:** General; especially when speed is prioritized.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The “target” class is not privileged; all classes must be equally salient or you want to avoid making one class feel dominant.
- **Reason:** Closed shapes can be processed more efficiently; privileging them could bias attention toward that class in attention-demanding contexts [@burlinsonOpenVsClosed2018a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Potential imbalance in perceived prominence between classes.
- **The Risk:** Viewers may attend more to the closed-symbol class than intended in mixed displays.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using open shapes (e.g., plus/asterisk) for the most important class in a cluttered plot because they “look lighter.”
- **Why it fails:** The paper’s perceptual tasks showed open targets produced slower RTs and higher error rates than closed targets [@burlinsonOpenVsClosed2018a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users consistently struggle more with one class (often the open-symbol class) when asked to identify it quickly among distractors.
- **The Test:** Swap the target class from open to closed while leaving everything else unchanged; if time/accuracy improves, the rule was violated.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reassign the focal/target class to a closed symbol (circle/square/triangle).
- **Best Fix:** Combine this with cross-family pairing (target closed, distractor open) in mixed-symbol plots to reduce same-family interference documented in the paper [@burlinsonOpenVsClosed2018a].
