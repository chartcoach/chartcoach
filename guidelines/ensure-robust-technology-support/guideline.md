---
id: ensure-robust-technology-support
title: Ensure Robust Technology Support
bibliography: references.bib
description: Ensure visualizations function across various browsers, devices, operating
  systems, and input mechanisms.
labels:
- impact:robustness
- impact:accessibility
- task:interact
- audience:general
- visual:interface
---

## The Rule <!-- role: advice -->
Do not isolate chart access to a single browser, device, software, or operating system. Ensure the visualization functions through a diversity of technological means.

## The Logic <!-- role: reason -->
This rule is based on the **Robust** principle of the Chartability framework, which requires designs to be compliant with existing standards and compatible with the user's assistive technologies of choice [@elavsky_how_2022].
*   **The Principle:** Technological Diversity.
*   **The Evidence:** Restricting access to specific environments makes the technology "fragile." Users must be able to switch between input modes (such as keyboard, mouse, or touch screen) interchangeably; prohibiting specific inputs or requiring specific gestures excludes users who rely on alternative mechanisms [@w3c_understanding_concurrent].

## Where to Apply <!-- role: context -->
This applies to all data-driven visualizations and interfaces intended for broad consumption.
*   **User Goal:** Accessing information regardless of their hardware or software setup.
*   **Data Type:** Any interactive or static visualization rendered digitally.
*   **Audience:** Users with diverse setups, including those using assistive technologies or specific input devices.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Highly controlled, proprietary hardware environments.
*   **Reason:** In specific industrial or closed-loop systems where the hardware and software stack is immutable and standardized for all operators, cross-platform compatibility may be unnecessary, though this makes the system fragile to future updates.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Ensuring robustness requires additional testing time across multiple browsers and devices.
*   **The Risk:** Failing to do this results in "fragile technology support," where a simple browser update or a user switching devices renders the visualization unusable [@elavsky_how_2022].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** optimizing only for the developer's current browser (e.g., "Works best in Chrome").
*   **Why it fails:** This isolates users who cannot or do not use that specific browser or operating system.
*   **The Wrong Fix:** Locking interaction to a single input type, such as mouse-only hovering.
*   **Why it fails:** This prohibits users who rely on keyboards, touch screens, or other concurrent input mechanisms from accessing the data [@w3c_understanding_concurrent].

## How to Check <!-- role: check -->
*   **Visual Sign:** The chart fails to load or function when switched to a different browser or device.
*   **The Test:** Attempt to use the visualization using different input mechanisms (e.g., switch from mouse to keyboard navigation) and view it on different browsers or operating systems.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove code that restricts input methods or detects and blocks specific browsers.
*   **Best Fix:** Develop using standard, open web technologies and validate functionality across a matrix of common browsers, operating systems, and input devices (mouse, keyboard, touch).
