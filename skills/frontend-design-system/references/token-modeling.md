# Token Modeling

Use this reference for token source-of-truth, naming, theming, aliasing, export pipelines, and reviews of hard-coded values.

## DTCG-Oriented Shape

- Represent token values with explicit value and type concepts, such as `$value` and `$type`, in the source model or in the transform layer.
- Use groups for shared metadata, but do not hide token meaning inside deeply nested paths.
- Use aliases for semantic mapping, such as `color.text.default -> color.gray.900`, instead of duplicating raw values.
- Detect circular aliases before export.
- Mark deprecated tokens explicitly and provide replacements and migration expectations.

## Layers

- Base tokens: raw palette, spacing scale, type scale, radii, shadows, motion, z-index, and breakpoints.
- Semantic tokens: product meaning, such as text default, surface raised, border danger, action primary.
- Component tokens: local mappings used only when a reusable component needs stable customization points.

## Naming

- Name by purpose at semantic and component layers, not by hex value, pixel value, or one-off page usage.
- Keep theme names out of consumer-facing component APIs where alias mapping can solve the problem.
- Avoid defining the same semantic meaning at multiple layers.

## Review Checks

- Can every exported token trace back to a source token and theme mapping?
- Are deprecated tokens still used by consumers?
- Are token names stable enough for design, code, and documentation?
- Do transforms preserve units, color spaces, composite values, and references correctly?
