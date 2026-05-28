---
name: site-reconstruction
description: Use this skill when you need to reverse engineer an existing website into a maintainable codebase with pixel-accurate 1:1 parity. Use it for internal site reconstruction, template reproduction for white-box or black-box testing, framework migration from live runtime pages, or any task that requires direct source extraction from DevTools, bundles, source maps, screenshots, or saved HTML, followed by exact restoration of routes, themes, hover states, active states, focus states, responsive layouts, and interactive behavior.
---

# Site Reconstruction

## Overview

This skill is a generic workflow for internal website reverse engineering and testing-oriented 1:1 reconstruction. It emphasizes direct source extraction, runtime truth, tool-capability detection, target-stack confirmation, and screenshot-verified parity. The default operating context is a company-owned site, internal template asset, or staging/production mirror used for white-box tests, black-box tests, visual regression, interaction validation, structure analysis, or source recovery.

## Mandatory Intake

Before reconstruction begins, do these checks in order.

### 1. Confirm Site Context And Testing Goal

Default to an internal/company-owned site workflow instead of treating permission checks as a blocker.

Confirm:

- whether the target is a company-owned production site, staging mirror, internal template asset, or other internal property
- whether the reconstruction is for white-box testing, black-box testing, visual regression, interaction validation, DOM/CSS structure analysis, or source recovery

Only add a permission-boundary confirmation if the target is clearly a third-party external site.

### 2. Confirm The Target Stack

If the target stack is not already explicit, pause and ask before doing reconstruction work.

Ask for one of:

- `React + Vite + Tailwind`
- `Vue + Vite + Tailwind`
- `Svelte / SvelteKit`
- `Astro`
- `HTML / CSS / JS`

If the repository already implies a stack, ask whether to:

- keep the existing stack
- migrate to another stack
- do a complete conversion with no compatibility layer

Do not assume the stack for a reusable reconstruction task.

### 3. Detect Tooling Capability

Before collecting truth sources, determine whether these tools are available.

#### Chrome DevTools MCP

Preferred for reverse engineering because it can expose:

- runtime DOM
- computed styles
- hover/focus/active/open states
- accessibility snapshots
- screenshots
- network assets
- source maps and bundle-linked assets

If DevTools MCP is available, use it first for runtime truth.

#### Playwright

Useful for:

- screenshot matrices
- multi-route capture
- visual regression
- repeatable parity checks

If Playwright is available, use it to automate screenshot and state capture after the runtime structure is understood.

#### Capability Order

1. `DevTools MCP + Playwright`
2. `DevTools MCP only`
3. `Playwright only`
4. neither available

If neither is available, explicitly warn that reconstruction confidence is lower and rely on HTML snapshots, bundles, static assets, and network resources.

### 4. Lock Scope

Lock:

- public routes
- page-type map
- target stack
- testing goals
- theme matrix
- viewport matrix
- required interaction states
- whether final output must be pure components with no template injection

## Core Rules

1. Runtime truth beats local guesses.
2. Direct source extraction beats approximate rewriting.
3. If copy, SVG, timing, assets, or structure can be recovered from bundles, source maps, or runtime markup, recover and reuse them directly.
4. Do not inject raw saved HTML into the final render path.
5. Rebuild extracted truth into maintainable route-specific components.
6. Separate “wrong frame” from “wrong implementation”.
7. Validate with screenshots and computed styles, not confidence.

## Workflow

### 1. Establish Source Priority

Use this priority unless the user says otherwise:

1. live runtime page
2. DevTools / Playwright DOM, computed styles, screenshots, network
3. source maps, bundles, compiled assets
4. saved HTML snapshots
5. current local implementation

### 2. Reverse Engineer The Source

Extract directly whenever possible:

- DOM structure
- link targets
- visible text
- SVG paths
- image, font, and icon URLs
- class/token patterns
- animation timing
- carousel intervals
- pricing/FAQ/blog/testimonial/content data
- source-mapped originals if present

If a detail cannot be extracted directly, make only the smallest necessary inference and label it internally as an inference.

Testing priority:

- for white-box testing, prioritize source maps, bundles, runtime state ownership, asset URLs, and component/data boundaries
- for black-box testing, prioritize screenshot matrices, state matrices, interaction parity, and layout/animation verification

### 3. Capture Runtime States

For each route, capture:

- title and headings
- CTA labels
- section order
- key DOM structure
- computed styles for default and interactive states
- hero/first viewport screenshot
- full-page screenshot
- screenshots for key states

### 4. Rebuild In The Confirmed Stack

Preserve these boundaries in any stack:

- page entry assembles sections
- route-specific sections own page pixels
- local components own local reuse
- shared primitives stay low-level
- content sources stay separate from UI

Avoid:

- template injection in the final render chain
- speculative pages
- invented content
- oversized shared abstractions that flatten route-specific layout

### 5. Restore Behavior

Recreate:

- hover, active, focus, selected, open states
- timed carousels and manual reset logic
- measured height transitions
- rolling numbers
- parallax/canvas/connector/orbit/marquee animations
- theme bootstrapping with no flash

### 6. Verify In Loops

After each meaningful change:

- run lint/build or equivalents
- refresh preview
- compare local vs source screenshots at the same route, theme, width, and state
- fix the largest visible mismatch first

## Decision Guardrails

If a mismatch may be caused by animation timing:

- reload both pages
- capture the initial frame
- trigger the same state on both sides
- compare active state ownership before editing

If an icon or logo looks missing:

- confirm the asset exists
- confirm `filter`, `opacity`, `visibility`, `mix-blend-mode`, and parent background
- confirm the local preview is using the latest build output

If the user requests exact parity, prefer extracted runtime/source truth over “clean room” rewriting.

## References

- For best practices: `references/best-practices.md`
- For intake and tool detection: `references/tooling-and-intake.md`
- For page-type priorities: `references/site-archetypes.md`
- For execution checklists: `references/workflow-checklists.md`
