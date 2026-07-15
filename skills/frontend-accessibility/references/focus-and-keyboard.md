# Focus And Keyboard

Use this reference when the task involves keyboard access, focus order, focus visibility, dialogs, overlays, composite widgets, dynamic content, or focus recovery.

## Keyboard Baseline

- Tab order should follow DOM order and the visual reading path unless a composite widget owns arrow-key navigation.
- Every interactive element must be reachable, operable, and understandable with a keyboard.
- Focus must remain visible in every theme, high contrast mode, and state.
- Avoid positive `tabindex`. Use `tabindex="0"` sparingly and `tabindex="-1"` for managed focus targets.
- Never create a keyboard trap. If focus is intentionally contained, provide a predictable close path.

## Focus Movement

- Move focus after opening modals, drawers, menus, popovers, route-like panels, or blocking error summaries.
- Return focus to the trigger or the next logical control after closing a layer.
- Do not steal focus for passive updates, toast messages, non-blocking loading states, or decorative changes.
- If content is removed, move focus to a stable nearby element instead of leaving focus lost on `body`.

## Composite Widgets

- Use roving `tabindex` when DOM focus should move among items.
- Use `aria-activedescendant` only when focus stays on a container/input and the active item is exposed through state.
- Arrow keys must be consistent with the pattern and orientation.
- Selection and focus are different. Auto-select on focus only when the pattern and latency make it safe.

## Verification

- Walk Tab, Shift+Tab, Enter, Space, Escape, arrow keys, Home/End, and typeahead where relevant.
- Check focus visibility against light/dark themes and high contrast where available.
- Check that animations, loading, route changes, and error states do not drop focus.
