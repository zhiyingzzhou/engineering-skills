# ARIA And Patterns

Use this reference only when native HTML cannot express the needed behavior or when reviewing an existing ARIA/custom widget.

## ARIA Boundary

- Follow the APG principle: no ARIA is better than bad ARIA.
- ARIA changes semantics only; it does not add keyboard behavior, pointer behavior, focus management, form submission, or validation.
- Do not create role/state contradictions, such as a `div role="button"` that lacks button keyboard behavior.
- Keep `aria-expanded`, `aria-selected`, `aria-pressed`, `aria-current`, `aria-invalid`, `aria-busy`, and `aria-disabled` synchronized with real UI behavior.
- Use `aria-label`, `aria-labelledby`, and `aria-describedby` for names and descriptions, not to compensate for unclear UX.

## Pattern Checks

- `dialog`: name the dialog, move focus inside, contain focus for modal dialogs, provide a close path, restore focus after close, and avoid background interaction.
- `tabs`: expose `tablist`, `tab`, `tabpanel`, selected state, panel association, and arrow-key movement. Use automatic activation only when panels display without noticeable latency.
- `menu`: use only for application-style command menus, not ordinary site navigation. Support arrow keys, Escape, disabled items, and focus return.
- `listbox`: expose active option, selected option, multi-select rules, typeahead expectations, and scroll visibility.
- `combobox`: keep input value, expanded state, popup ownership, active descendant or roving focus, filtering, Escape, and commit behavior consistent.
- `accordion` / disclosure: use buttons, expose expanded state, associate the controlled region when useful, and keep collapsed content out of the tab path.

## Live Regions And Dynamic State

- Use live regions for important asynchronous feedback that does not receive focus.
- Do not broadcast every minor state change.
- Prefer a concise status region for background save, loading completion, or non-blocking errors.
- For blocking validation, focus an error summary or first invalid field instead of relying only on live regions.

## Verification

- Confirm role, name, state, and keyboard behavior together.
- Compare default, hover, focus, active, selected, expanded, disabled, loading, and error states.
- If mobile/touch assistive technology was not checked, record the gap.
