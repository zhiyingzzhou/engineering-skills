---
name: site-reconstruction
description: Use this skill for authorized reconstruction of owned or explicitly permitted websites into maintainable code with screenshot-verified parity. Use it for internal site reconstruction, staging or production mirrors, template recovery, framework migration, visual regression baselines, interaction validation, DOM/CSS structure analysis, source-map-assisted recovery, or route/theme/state parity work. Do not use it to copy third-party sites, private assets, proprietary source, brands, or copyrighted creative work without clear authorization; for third-party targets, default to non-copying analysis and ask for permission boundaries before direct extraction.
---

# Site Reconstruction

## Core Workflow

1. Confirm authorization, site ownership or permission, reconstruction goal, target stack, route scope, theme matrix, viewport matrix, and interaction states before extraction.
2. Detect available tooling: Chrome DevTools MCP or browser control for runtime truth, Playwright for repeatable screenshots and visual comparisons, and local build tooling for verification.
3. Capture runtime truth before implementation: DOM, accessible structure, computed styles, resources, screenshots, interaction states, animation timing, and source maps when permitted.
4. Rebuild into maintainable route-specific components; do not inject raw saved HTML into the final render path.
5. Verify in loops with same route, viewport, theme, browser, state, timing, and asset conditions.

## Read References By Task

Always read:

- `references/permissions-and-extraction.md`
- `references/tooling-and-intake.md`
- `references/best-practices.md`

Read only when relevant:

- `references/site-archetypes.md` for landing pages, docs, dashboards, ecommerce, auth, and form-heavy sites.
- `references/visual-parity.md` for screenshot matrices, diff thresholds, animation freezing, and artifact naming.
- `references/workflow-checklists.md` for execution and handoff reviews.
- `references/forward-tests.md` only when validating or iterating on this skill.

## Intake

- Confirm whether the target is company-owned, internally controlled, licensed, client-authorized, public third-party, or unknown.
- Confirm the testing goal: white-box recovery, black-box parity, visual regression, interaction validation, DOM/CSS analysis, or migration.
- Confirm the target stack or ask the user to choose: React + Vite + Tailwind, Vue + Vite + Tailwind, Svelte/SvelteKit, Astro, or HTML/CSS/JS.
- Confirm whether direct extraction of source maps, copy, SVG, images, fonts, and exact assets is permitted.
- Lock routes, page types, themes, viewports, breakpoints, required states, and whether the output must be pure components.

## Extraction Rules

- For owned or explicitly authorized targets, prefer runtime truth and direct source extraction when permitted.
- For third-party or unknown targets, do not copy source, source maps, copy, SVG paths, images, fonts, brand assets, or proprietary structure; produce analysis or an independently implemented approximation only after permission boundaries are clear.
- Treat source maps and bundles as debugging material, not automatic permission to reuse code.
- Label any inference internally and avoid inventing content, routes, pricing, testimonials, or claims.

## Rebuild Rules

- Keep page entries, route-specific sections, local components, shared primitives, and content data separated.
- Preserve hover, active, focus, selected, open, loading, empty, error, theme, responsive, and animation states.
- Compare computed styles for stateful UI: color, background, border, shadow, opacity, filter, transform, layout metrics, and visibility.
- Fix the largest visible mismatch first; separate wrong capture timing from wrong implementation.

## Delivery Requirements

- State authorization assumptions, extracted sources used, inferred details, and any assets intentionally not copied.
- Report screenshot/visual comparison coverage by route, theme, viewport, and state.
- Report lint/build/test results and any parity gaps left for follow-up.
