# Storybook Docs

Use this reference for Storybook, equivalent component docs, executable examples, accessibility checks, interaction tests, and visual review.

## Documentation Goals

- Show real rendered components, not screenshots of intended behavior.
- Keep stories aligned with the component contract and source types.
- Make design, engineering, QA, and product review the same state matrix.
- Treat docs as a regression surface for accessibility and visual states.

## Story Coverage

- Every primitive should show default, key variants, disabled, loading, error, long content, and focus-visible behavior where applicable.
- Form and input components should include labels, descriptions, errors, required/optional text, disabled/readonly, and autofill-relevant examples.
- Overlay and composite components should include open, keyboard focus, nested content, and close behavior.
- Components with async behavior should show loading, empty, success, and failure states.

## Tests In Docs

- Use interaction tests for state changes that users trigger.
- Use accessibility tests to catch missing names, roles, contrast issues detectable by tooling, and invalid ARIA.
- Use visual snapshots for states where spacing, theme, density, and layout regression matter.
- Keep test data deterministic and avoid stories that depend on production services.

## Review Checks

- Are docs generated from the same args/props contract consumers use?
- Do examples include edge cases, not only happy paths?
- Are do/don't notes tied to a visible example or failing pattern?
