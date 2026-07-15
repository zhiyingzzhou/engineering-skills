# Best Practices

Use this reference for reconstruction approach after permission and scope are clear.

## Source Priority

For owned or explicitly authorized targets:

1. Live runtime page.
2. DevTools or browser runtime truth: DOM, computed styles, screenshots, accessibility tree, network, and state.
3. Playwright captures and repeatable screenshot matrices.
4. Source maps, bundles, compiled assets, API responses, and static resources when reuse is permitted.
5. Saved HTML snapshots.
6. Current local approximation.

For public third-party or unknown targets, use only non-copying analysis unless permission is clarified.

## Runtime Truth

- Runtime DOM beats saved HTML when hydration, theme branches, media queries, feature flags, or animation initialization are involved.
- Computed styles beat class names for visual parity.
- State captures beat memory: hover, active, focus, selected, expanded, open, loading, empty, and error states.
- Screenshots should include first viewport, full page, section-level, mobile, and key interaction states.

## Reconstruction Boundaries

- Rebuild into maintainable route-specific sections and local components.
- Keep shared primitives low-level.
- Keep content sources separate from UI.
- Do not inject raw saved HTML into the final render path.
- Do not invent routes, claims, testimonials, pricing, logos, or product details.

## Computed Style Checks

Capture or compare:

- Color, background, border, shadow, opacity, filter, transform.
- Font family, size, weight, line height, spacing, and text wrapping.
- Width, height, padding, margin, gap, grid/flex tracks, position, z-index, and overflow.
- Transition duration, easing, delay, transform origin, and animation state.

## Guardrails

- If a mismatch may be animation timing, reload both pages and compare the same frame/state.
- If an asset looks missing, check existence, path, filter, opacity, visibility, blend mode, and parent background.
- If exact parity is requested, fix the largest visible mismatch first and keep a visible gap log.
