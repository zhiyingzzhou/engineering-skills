# Semantic HTML

Use this reference when the task involves page structure, landmarks, headings, links, buttons, images, form controls, names, or replacing clickable `div`/`span` elements.

## Baseline

- Prefer native HTML before ARIA. Native elements bring roles, states, keyboard behavior, form behavior, and platform mappings that ARIA cannot fully recreate.
- Use `button` for in-page actions and `a[href]` for navigation. Do not use `role="button"` or click handlers on static elements when a real control works.
- Use one primary `main` landmark, meaningful headings, and sectioning elements only when they describe real page regions.
- Use lists, tables, captions, `fieldset`, `legend`, `label`, `output`, and `details` only when they express real relationships.

## Names And Text Alternatives

- Align visible text, accessible name, and control purpose. If they differ, document why.
- Decorative icons and images should be hidden from assistive technology. Informative images need useful alt text.
- Icon-only controls need a stable accessible name and visible affordance.
- Avoid naming controls with implementation details such as file names, icon names, or internal action IDs.

## Common Repairs

- Replace clickable containers with native controls.
- Replace heading-like styling with real headings when it marks a content boundary.
- Add or repair labels instead of relying on placeholders.
- Restore semantic relationships that styling wrappers obscured.
- Remove redundant roles that duplicate native semantics unless they are required by a tested pattern.

## Verification

- Inspect the accessibility tree or browser snapshot where available.
- Confirm heading and landmark navigation is meaningful.
- Confirm names are useful without visual context.
- Record when only static DOM review was performed.
