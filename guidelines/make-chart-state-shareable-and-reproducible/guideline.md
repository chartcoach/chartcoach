---
id: make-chart-state-shareable-and-reproducible
title: Make interactive chart state shareable and reproducible
bibliography: references.bib
description: Ensure any customized interactive view can be shared and reopened to
  reproduce the same chart state with minimal effort.
labels:
- chart:interactive
- task:collaborate
- visual:interaction
- impact:accessibility
- data:multivariate
- audience:expert
- complexity:advanced
- a11y:compromising
---

## Share state as a single artifact that reproduces the same view <!-- role: advice -->

Make any user-defined chart state easy to share and reproduce as a single artifact such as a link, file, or saved state. Opening the shared artifact must restore the same parameters and view.

## Why reproducible state reduces access barriers in exploratory analysis <!-- role: reason -->

When an interactive visualization allows filtering, drilling down, or navigating a branching narrative, people depend on stable references to communicate findings and continue work later. If state cannot be reproduced, users must reconstruct it manually, shifting cognitive labor onto collaborators and often forcing inaccessible substitutes (such as screenshots) that lose interactivity and require separate accessibility work.

**Mechanism:** Reproducible state preserves context (filters, selections, viewpoint, and other parameters) so collaborators can return to the same evidence without re-deriving steps.

**Evidence:** Sharing a parameterized link that recreates an exact view reduces the effort needed to communicate a specific interactive state and enables others to see the same state without manual reconstruction [@moz_everything_you]. Providing built-in report sharing workflows supports collaborators viewing and revisiting interactive dashboards in the intended state rather than relying on static exports [@key2consulting_how_share]. A visualization accessibility audit framework includes “state is not easy to share and reproduce” as an accessibility barrier in complex interactive data experiences [@elavskyHowAccessibleMy2022].

**Notes:** The accessibility barrier is the extra work imposed on others when the original explorer cannot transmit the “proof in the system” of their current view.

## When state sharing is required in data experiences <!-- role: context -->

- **User Goal:** Share an insight found through exploration so another person can review, verify, or continue from the same view.
- **Task:** Collaborative analysis, review, handoff, or asynchronous discussion of findings.
- **Data:** Multivariate datasets where filters, drilldowns, or narrative branches change what is visible.
- **Chart Setting:** Interactive dashboards or applications with multiple controls and many possible states.
- **Audience:** Teams with mixed abilities and mixed tool expertise, including users of assistive technologies.
- **Success Criterion:** A recipient can open the shared artifact and see the same view and parameters without manual reconfiguration.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart has no meaningful interaction or configurable state beyond a fixed default view. **Why:** There is no state to capture or reproduce.

## Tradeoffs of state capture and sharing <!-- role: costs -->

**Sacrifice:** Implementing shareable state adds engineering and product complexity for storing or encoding parameters. **Risk:** Sharing may expose sensitive parameters or data access context if links/files are forwarded. **Mitigation:** Treat shared state as a controlled artifact within the system’s existing sharing model.

## Common ways state sharing fails in practice <!-- role: mistakes -->

- **Mistake:** Recommending screenshots as the primary sharing method for interactive findings. **Why it fails:** It removes interactive proof of the analysis and creates additional accessibility work to make the image accessible.
- **Mistake:** Allowing “share” to open only a generic landing view rather than the current configured state. **Why it fails:** The recipient must reconstruct steps, transferring cognitive labor and increasing the chance of mismatch.

## Quick tests for reproducible state <!-- role: check -->

**Failure Sign:** A user cannot produce a single shareable artifact that restores their current filters/selections/view. **Quick Check:** Create a non-default state, share it, open it in a fresh session, and verify whether the same view is restored without manual steps. **Stronger Test:** Ask a collaborator to reproduce the shared view from the artifact alone and note any required reconstruction steps or missing context.

## Practical ways to provide shareable, reproducible state <!-- role: fix -->

- Provide a single-link “Share this view” action that encodes or references all parameters needed to recreate the current state.
- Provide an exportable saved-state file (or internal saved view) that can be reopened to restore the same configuration.
- Provide a “Saved views” mechanism so users can name, revisit, and share specific states without re-performing interactions.
- If interactive state cannot be preserved, provide an accessible alternative that preserves the reasoning trail (for example, a saved report view intended for sharing rather than an ad-hoc screenshot).
