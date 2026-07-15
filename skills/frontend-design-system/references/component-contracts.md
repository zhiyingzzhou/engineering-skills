# Component Contracts

Use this reference when designing, changing, or reviewing reusable component APIs.

## Contract Contents

- Purpose: what problem the component solves and when not to use it.
- Inputs: variants, sizes, density, state, data shape, slots, render props, callbacks, and refs.
- State model: controlled, uncontrolled, default value, async loading, error, disabled, readonly, selected, expanded, pressed, and invalid.
- Accessibility ownership: built-in roles, names, focus behavior, keyboard behavior, labeling, descriptions, and required consumer-provided text.
- Styling surface: stable tokens, class hooks, CSS variables, or theme slots that are supported long term.

## API Rules

- Prefer semantic variants over temporary visual flags.
- Replace boolean clusters with a clear variant or state enum when combinations matter.
- Do not hard-code business copy, route logic, API response structures, analytics events, or product-specific permissions into primitives.
- Keep escape hatches narrow and documented.
- Do not break focus, keyboard, or name behavior through visual customization.

## State Matrix

Cover at least: default, hover, focus-visible, active, disabled, loading, error, success, selected/current, expanded/collapsed, empty, long text, dense content, and RTL/locale-sensitive content when relevant.

## Review Checks

- Can a consumer use the component correctly from the docs alone?
- Are invalid prop combinations prevented by types or runtime guards?
- Are accessibility obligations clear between component and consumer?
- Does the API remain stable across themes and product surfaces?
