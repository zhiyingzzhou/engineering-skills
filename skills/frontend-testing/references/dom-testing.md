# DOM Testing

Use this reference for Testing Library, component tests, semantic queries, user-event, and async assertions.

## Query Priority

- Prefer role plus accessible name for controls, headings, landmarks, and status.
- Use label text for form fields.
- Use visible text for content when role/name is not appropriate.
- Use placeholder only when the placeholder is the actual user cue.
- Use `data-testid` only for stable elements that cannot be selected semantically.

## Query Types

- Use `getBy*` when the element should exist synchronously.
- Use `queryBy*` when asserting absence.
- Use `findBy*` when the element appears asynchronously.
- Use `within` to scope queries to a region, dialog, table, or list.

## Interaction And Assertions

- Use user-level interactions, such as click, type, tab, keyboard, select, upload, and pointer flows.
- Assert visible results, accessible state, form values, error messages, focus, URL changes, or emitted user outcomes.
- Use semantic assertions where available, such as focus, disabled, invalid, checked, visible, and text content.
- Avoid testing private state, private functions, CSS class implementation, or DOM nesting as the main assertion.

## Async Pitfalls

- Await user interactions when the library requires it.
- Wait for the UI state, not arbitrary time.
- Avoid broad snapshots as the only assertion.
