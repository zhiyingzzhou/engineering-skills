# Tooling And Intake

Use this reference before capture or implementation.

## Intake Order

1. Authorization class and permission boundary.
2. Target URL or local artifact.
3. Testing or reconstruction goal.
4. Target stack.
5. Routes, page types, themes, viewport matrix, and required states.
6. Allowed direct extraction categories: source maps, copy, SVG, images, fonts, timing, CSS tokens, API data.
7. Output constraints: pure components, no raw template injection, framework migration, or parity tolerance.

## Target Stack

If not explicit, ask the user to choose:

- React + Vite + Tailwind
- Vue + Vite + Tailwind
- Svelte/SvelteKit
- Astro
- HTML/CSS/JS

If the repository already implies a stack, ask whether to keep it, migrate, or convert completely.

## Tool Detection

Use available tools in this order:

1. Chrome DevTools MCP or browser control plus Playwright.
2. Chrome DevTools MCP or browser control only.
3. Playwright only.
4. Static HTML, bundles, saved assets, and manual screenshots.

## DevTools / Browser Capture

Use when available for:

- Runtime DOM and accessibility snapshots.
- Computed styles and layout metrics.
- Hover, focus, active, open, selected, loading, and error states.
- Network assets, source maps, screenshots, and console/runtime observations.

## Playwright Capture

Use when available for:

- Repeatable route screenshots.
- Viewport, theme, and state matrices.
- Trace capture for interaction and animation timing.
- Visual comparisons and artifact naming.

## Degraded Mode

If neither runtime tooling nor Playwright is available, explicitly warn that confidence is lower and rely on permitted static artifacts, saved screenshots, and manual inspection.
