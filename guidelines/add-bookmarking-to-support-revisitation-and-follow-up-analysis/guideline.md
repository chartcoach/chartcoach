---
id: add-bookmarking-to-support-revisitation-and-follow-up-analysis
title: Add bookmarking to support revisitation and follow-up analysis
bibliography: references.bib
description: Let users save promising views during exploration so they can return
  for targeted analysis later.
labels:
- chart:gallery
- task:explore
- task:communicate
- visual:interaction
- impact:workflow
- data:tabular
- audience:novice
- system:analysis-workflow
---

## Provide a bookmark mechanism to save and revisit interesting views <!-- role: advice -->

Allow users to bookmark recommended charts during exploration and review them later in a dedicated bookmark gallery.

## Bookmarks bridge breadth-first exploration to later depth-first work <!-- role: reason -->

Exploration produces many fleeting findings; without a capture mechanism, users must rely on memory or repeat steps to reconstruct a view. Bookmarking preserves discoveries and supports follow-up analysis and sharing.

**Mechanism:** Externalizing intermediate findings reduces memory load and enables users to switch between broad scanning and focused investigation without losing progress.

**Evidence:** The system includes bookmarking to enable revisitation and follow-up, and user study results show participants bookmarked views at similar rates across recommendation browsing and manual specification, with many bookmarked views in the recommendation system including automatically added variables [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

**Notes:** Bookmarks can also support later transitions to more manual, targeted tooling.

## When exploration is iterative and users expect to follow up later <!-- role: context -->

- **User Goal:** Collect interesting patterns to report, share, or analyze further.
- **Task:** Exploratory analysis with later synthesis or question answering.
- **Data:** Any dataset where exploration yields multiple candidate insights.
- **Chart Setting:** A browsing-oriented interface where users may quickly move on from a view.
- **Audience:** Analysts working under time constraints who need to retain findings.
- **Success Criterion:** Users can return to specific views without reconstructing them.

## When bookmarking is less critical <!-- role: exceptions -->

**Break it when:** The workflow is strictly scripted or the analysis path is already captured elsewhere (for example, in a saved specification history). **Why:** Bookmarking may duplicate an existing revisitation mechanism [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Tradeoffs of bookmarking features <!-- role: costs -->

**Sacrifice:** UI space and implementation complexity for managing saved views. **Risk:** Users may over-bookmark and create an unmanageable collection. **Mitigation:** Provide a dedicated bookmark gallery that supports quick review and clearing [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Common failures in exploration workflows without bookmarks <!-- role: mistakes -->

**Mistake:** Expecting users to remember how to return to an interesting view discovered during browsing. **Why it fails:** Users lose insights when they switch attention to other variables or sections of the gallery [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Checks that bookmarking is doing useful work <!-- role: check -->

**Failure Sign:** Users take external notes or screenshots to preserve a chart they might want later. **Quick Check:** Confirm every chart in the gallery has an obvious “save” action. **Stronger Test:** In a timed exploration, see whether users can quickly retrieve a previously found view using bookmarks rather than reconstruction [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## What to do if users need more than static bookmarks <!-- role: fix -->

- Add a dedicated bookmark gallery that displays saved views together for review.
- Allow exporting of bookmarked view specifications so users can continue in other tools or modes.
- Provide undo/reset controls so users can explore freely while trusting they can return to saved states [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
