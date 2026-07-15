# Workflow Checklists

Use this reference for execution and handoff reviews.

## Before Capture

- Authorization class is recorded.
- Target stack is confirmed.
- Routes, themes, viewport matrix, and required states are locked.
- Direct extraction permissions are clear.
- Tooling availability is known.

## Capture

- Title, headings, copy, CTA labels, links, and section order.
- Runtime DOM and accessibility structure.
- Computed styles for default and interactive states.
- Network resources and permitted assets.
- First viewport, full page, section, mobile, and interaction screenshots.
- Animation timing and state ownership.

## Implementation

- Page entry assembles route-specific sections.
- Local components own local reuse.
- Shared primitives stay low-level.
- Content data is separate from UI.
- Raw saved HTML is not injected into the final render path.
- Third-party or unauthorized assets are not copied.

## Regression

- Run lint/build or equivalents.
- Compare same route, theme, viewport, state, and timing.
- Freeze animation, time, random content, and network where possible.
- Fix the largest visible mismatch first.
- Record remaining parity gaps.
