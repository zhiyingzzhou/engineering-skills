# Accessibility Audit Checklist

Use this reference for PR reviews, page audits, and risk summaries.

## Minimum Review

- Identify critical user paths, entry points, and blocking states.
- Check headings, landmarks, labels, names, roles, states, and descriptions.
- Check keyboard reachability, operation, focus order, visible focus, and focus recovery.
- Check complex widgets against APG-style behavior, not just role names.
- Check form errors, async feedback, loading, disabled, selected, expanded, and invalid states.
- Check zoom to 200%, narrow viewport, long text, high contrast or forced colors where possible.

## Severity

- High: unreachable task, keyboard trap, unnamed critical control, stale ARIA state, lost focus after context change, inaccessible blocking error.
- Medium: confusing heading/landmark structure, weak focus indication, incomplete descriptions, inconsistent widget keys, unannounced important async feedback.
- Low: redundant ARIA, minor ordering issues, verbose names, non-critical decorative noise.

## Delivery

- Report what was verified manually and automatically.
- Report which assistive technology, browser, zoom, contrast, reduced motion, touch, or mobile checks were not performed.
- Avoid claiming WCAG or full accessibility compliance from static review alone.
