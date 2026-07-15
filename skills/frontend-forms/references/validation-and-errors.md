# Validation And Errors

Use this reference when designing validation timing, field errors, server errors, summaries, and recovery behavior.

## Timing

- Show static requirements before input.
- Avoid blocking errors before the user has interacted with the field.
- Validate after blur, after a meaningful pause, or on submit depending on cost and severity.
- Treat server validation as authoritative when client and server disagree.

## Field Errors

- Place field-level errors near the field and explain how to fix the issue.
- Set `aria-invalid` only while the current value is invalid.
- Link the active error message to the field description relationship.
- Do not rely on color alone.
- Preserve valid user-entered values after failure unless a security rule requires clearing them.

## Error Summary

- Use an error summary for multi-field or submit-blocking failures.
- Focus the summary or the first invalid field after submit; choose the pattern that best supports the existing UI.
- Summary links should move focus to the relevant field.
- Keep server, network, permission, and field-format errors distinguishable.

## Recovery

- Prevent duplicate submit with disabled or pending state that remains understandable.
- Announce successful submission and next step.
- Allow retry after network failure without losing entered data.
- Avoid live-region spam; focus blocking failures and use concise status for non-blocking updates.
