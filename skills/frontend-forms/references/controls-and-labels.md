# Controls And Labels

Use this reference when selecting controls, labeling fields, grouping inputs, or reviewing form semantics.

## Control Choice

- Use native `input`, `select`, `textarea`, and `button` before custom controls.
- Choose `type`, `inputmode`, `autocomplete`, `min`, `max`, `step`, `pattern`, and `required` according to the data contract and user input reality.
- Use a real submit button and form submission path unless the application has a documented reason not to.
- Use `fieldset` and `legend` for grouped radio buttons, checkboxes, address segments, or multi-field concepts.

## Labels And Descriptions

- Every field needs a programmatic label. Visible labels are preferred.
- Placeholders can provide examples, not field identity.
- Associate help text, format requirements, counters, and errors with the field through `aria-describedby` or native relationships.
- Mark required and optional fields consistently before the user submits.

## Field Contract Matrix

For every field, record:

- Name and user-facing label.
- Data type, allowed format, required/optional status, default value, and dependencies.
- Client validation, server validation, normalization, and persisted value.
- Autofill token, privacy sensitivity, and whether the field can be safely retained after failure.

## Review Checks

- Can the user understand what to enter before typing?
- Can the field be completed with keyboard, screen reader, autofill, and mobile input?
- Do grouped controls expose a real group name?
