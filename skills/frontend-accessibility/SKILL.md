---
name: frontend-accessibility
description: Use this skill for frontend accessibility implementation, remediation, or review when the task involves semantic HTML, accessible names, keyboard operation, focus management, ARIA boundaries, assistive technology behavior, or complex widgets such as dialogs, tabs, menus, listboxes, comboboxes, accordions, and disclosure controls. Do not use it for general form UX, responsive layout, performance profiling, or design-system governance unless the accessibility behavior is the primary concern.
---

# Frontend Accessibility Skill

## Core Workflow

1. Establish the current DOM, semantic structure, heading order, landmarks, names, roles, states, and interactive controls.
2. Walk the keyboard path before editing: Tab, Shift+Tab, Enter, Space, Escape, arrow keys, and typeahead where the pattern expects it.
3. Prefer native HTML. Add ARIA only when native semantics cannot express the required behavior, and keep every ARIA state synchronized with the UI.
4. Fix blocking issues first: unreachable controls, invisible focus, unnamed controls, keyboard traps, stale state, and focus loss.
5. Verify with the strongest available signal: real browser interaction, automated checks, accessibility snapshots, screen reader spot checks, and documented gaps.

## Read References By Task

Always read:

- `references/semantic-html.md`
- `references/focus-and-keyboard.md`

Read only when relevant:

- `references/aria-and-patterns.md` for dialogs, tabs, menus, listboxes, comboboxes, accordions, disclosure controls, and custom widgets.
- `references/assistive-tech-matrix.md` for screen reader, browser, zoom, high contrast, reduced motion, or mobile/touch verification.
- `references/audit-checklist.md` for PR, page, or flow reviews.
- `references/forward-tests.md` only when validating or iterating on this skill.

## Intake

- Identify the page, component, state, or user path under review.
- Identify the existing component library or accessibility primitives before inventing a new pattern.
- Identify available validation commands, browser automation, preview URLs, and manual test constraints.
- Record any unverified assistive technology, zoom, high contrast, touch, or reduced motion scenarios in the final response.

## Implementation Rules

- Use `button` for actions, `a` for navigation, and real form controls for form input.
- Do not add `role` to change an element into something it does not behave like.
- Do not use `aria-label` to hide unclear visible text; align visible text, accessible name, and control purpose.
- Manage focus only when the interaction changes context, opens/closes a layer, moves within a composite widget, or reports a blocking error.
- Keep disabled, expanded, selected, pressed, current, invalid, and busy states tied to real behavior.
- Treat APG examples as pattern guidance, not copy-paste guarantees; adapt only after confirming keyboard and assistive technology behavior.

## Delivery Requirements

- State which semantics, roles, names, states, focus paths, or keyboard behaviors changed.
- Report the validation performed and the exact gaps left untested.
- If only static review was possible, say so and do not claim full accessibility verification.
