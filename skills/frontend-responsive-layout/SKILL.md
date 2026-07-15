---
name: frontend-responsive-layout
description: Use this skill for frontend responsive layout design, remediation, or review when the task involves viewport or container breakpoints, Flex/Grid sizing, overflow, wrapping, content-driven layout, responsive media, container queries, dynamic viewport units, safe areas, touch targets, virtual keyboards, orientation changes, zoom, or cross-device visual layout. Do not use it for Core Web Vitals profiling, form validation, component API governance, or accessibility semantics unless layout behavior is the primary concern.
---

# Frontend Responsive Layout Skill

## Core Workflow

1. Reproduce the layout issue at the smallest, largest, and one intermediate relevant size before editing.
2. Identify whether the failure is caused by viewport assumptions, container assumptions, fixed dimensions, intrinsic content, media, positioning, or input modality.
3. Fix constraints close to the source: grid/flex tracks, `min-width`, wrapping, aspect ratio, media sizing, safe area, or container query.
4. Prefer content-driven breakpoints and container behavior over device-name breakpoints.
5. Verify no horizontal overflow, content clipping, touch-target regression, image distortion, or layout shift across the agreed viewport matrix.

## Read References By Task

Always read:

- `references/layout-strategy.md`
- `references/overflow-and-sizing.md`

Read only when relevant:

- `references/responsive-media.md` for images, video, iframes, art direction, aspect ratio, and layout stability.
- `references/device-checklist.md` for touch, orientation, virtual keyboard, safe area, zoom, reduced motion, and interaction modality.
- `references/forward-tests.md` only when validating or iterating on this skill.

## Intake

- Identify the affected viewport widths, heights, containers, orientation, zoom level, and input modality.
- Identify whether the layout depends on viewport media queries, container queries, fixed pixels, or design tokens.
- Identify available preview, screenshot, visual regression, build, and device simulation commands.
- Identify whether the change can affect content hierarchy, accessibility, LCP media, CLS, or form usability.

## Implementation Rules

- Use `minmax()`, `clamp()`, flexible tracks, wrapping, and stable aspect ratios before adding more hard breakpoints.
- Use `min-width: 0` or equivalent constraints when flex/grid children cause overflow.
- Use container queries only after defining the containment context deliberately.
- Use `srcset`, `sizes`, `picture`, stable dimensions, and non-lazy loading for critical media when appropriate.
- Account for `svh`/`dvh`/`lvh`, safe areas, virtual keyboards, pointer/hover capabilities, and 200% zoom when relevant.

## Delivery Requirements

- State which constraints, containers, breakpoints, overflow paths, or media strategies changed.
- Report viewport/device checks performed and whether they were simulated or real-device checks.
- Call out unverified orientation, zoom, touch, keyboard, safe-area, or media loading scenarios.
