# Assistive Technology Matrix

Use this reference when a task asks for confidence beyond static semantics or when the UI includes complex widgets, overlays, critical forms, or keyboard-only workflows.

## Minimum Matrix

- Keyboard-only in at least one desktop browser.
- Browser accessibility tree or snapshot when available.
- Screen reader spot check for the changed path when available: VoiceOver on macOS/iOS, NVDA on Windows, or the product's supported stack.
- 200% zoom or equivalent browser zoom for layout and operability.
- High contrast or forced colors when the UI depends on custom focus, borders, icons, or color-coded state.
- Reduced motion when the UI includes animation, parallax, auto-scrolling, or timed effects.
- Touch exploration when custom controls or overlays must work on mobile assistive technology.

## What To Verify

- The user can identify where they are, what changed, and what the next action is.
- Focus order, screen reader reading order, and visual order are compatible.
- Names, roles, states, and values are meaningful in context.
- Dynamic changes are either focused, announced, or intentionally silent.
- Modal/layered UI prevents background confusion and restores focus.

## Reporting Gaps

Name the exact unverified combinations. Example: "Keyboard and Chrome accessibility snapshot checked; VoiceOver, NVDA, forced colors, and mobile touch assistive technology were not checked."
