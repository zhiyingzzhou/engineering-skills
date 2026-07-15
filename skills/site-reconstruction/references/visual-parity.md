# Visual Parity

Use this reference for screenshot matrices, diff thresholds, artifact naming, and repeatable comparison.

## Matrix

- Capture first viewport and full page for each route.
- Capture at least narrow mobile, common desktop, and one intermediate width unless scope says otherwise.
- Capture each required theme.
- Capture key states: hover, focus, active, open, selected, loading, empty, error, sticky, and animated frame.

## Stabilization

- Use the same browser, viewport, device scale factor, locale, timezone, fonts, reduced-motion setting, and color scheme.
- Freeze time, random data, animation, carousel position, and network responses where possible.
- Wait for fonts, images, and app idle state before capture.
- Compare the same animation frame or disable animation for static parity.

## Diff Policy

- Define acceptable pixel threshold before claiming parity.
- Treat text wrapping, icon shape, asset crop, spacing, and state mismatch as higher priority than tiny anti-aliasing differences.
- Keep artifact names deterministic: route, theme, viewport, state, source/local, timestamp or revision.

## Delivery

- State which screenshots were compared.
- State threshold or manual review standard.
- Attach or reference remaining mismatch categories.
