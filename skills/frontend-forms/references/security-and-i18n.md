# Security And Internationalization

Use this reference for authentication, checkout, addresses, names, phone numbers, dates, privacy-sensitive fields, and localized validation.

## Security And Privacy

- Do not expose passwords, tokens, OTP codes, payment details, or personal data in URLs, logs, analytics, or client error traces.
- Avoid clearing user input after ordinary validation failures; clear sensitive fields only when required by security policy.
- Use generic account-recovery and sign-in errors when revealing account existence would be risky.
- Preserve paste and password-manager behavior unless a documented security requirement forbids it.
- Confirm loading and disabled states do not hide security-critical next steps.

## Internationalization

- Names, addresses, phone numbers, postal codes, and dates vary by locale. Avoid patterns that only fit one country unless the product is scoped that way.
- Do not require first/last name splits unless the backend contract requires it.
- Address order, required fields, state/province labels, and postal-code formats must be locale-aware where the product supports multiple countries.
- Date input should avoid ambiguous formats and use localized display with unambiguous stored values.

## Review Checks

- Is the validation stricter than the backend or locale allows?
- Is any sensitive value persisted longer than needed?
- Does translated copy still fit labels, errors, buttons, and summaries?
