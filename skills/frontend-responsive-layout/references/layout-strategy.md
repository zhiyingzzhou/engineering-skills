# Layout Strategy

Use this reference for viewport breakpoints, container behavior, grid/flex layout, reading width, and content hierarchy.

## Principles

- Start from the narrowest credible space and expand upward.
- Create breakpoints where content breaks, not where a device name appears.
- Prefer flexible constraints over fixed dimensions: `minmax()`, `clamp()`, `auto-fit`, `auto-fill`, wrapping, and intrinsic sizing.
- Use container queries when a component's layout depends on its parent size rather than the viewport.

## Container Queries

- Define a containment context with `container-type` before relying on `@container`.
- Use named containers when multiple ancestors could match.
- Use container query units only when the component should scale with the container.
- Provide reasonable fallback behavior when container queries are unavailable or not used by the current stack.

## Layout Review

- Identify the element that causes overflow, compression, clipping, or excessive whitespace.
- Check whether the layout assumes a fixed column count, fixed width, fixed height, or one-line text.
- Keep readable line lengths on wide screens.
- Preserve visual hierarchy when content wraps or collapses.

## Repair Patterns

- Replace magic margins with `gap` and grid/flex tracks.
- Let toolbars, tabs, and button groups wrap or collapse deliberately.
- Move secondary content below, into disclosure, or into a horizontal overflow region only when that matches the task.
