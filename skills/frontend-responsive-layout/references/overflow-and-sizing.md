# Overflow And Sizing

Use this reference when content spills, clips, squashes, overlaps, or creates horizontal scrolling.

## Common Causes

- Flex/grid children keep their intrinsic minimum size and need `min-width: 0` or equivalent.
- Long words, URLs, filenames, code, or table cells lack a wrapping or scrolling policy.
- Fixed heights cannot contain translated text, zoomed text, validation errors, or dynamic content.
- Absolute, sticky, transformed, or animated elements escape their intended containing block.
- Viewport-height assumptions fail with mobile browser chrome or virtual keyboards.

## Repair Rules

- Fix the constraint chain near the source before applying global `overflow: hidden`.
- Prefer flexible min/max constraints to fixed dimensions.
- Give tables, code blocks, charts, and data grids a deliberate narrow-screen strategy.
- Avoid hiding focus outlines or controls through clipping.
- Consider `svh`, `dvh`, and `lvh` for mobile viewport-height problems.

## Text

- Allow wrapping for user-generated content.
- Use truncation only when the full value is available through an accessible affordance.
- Test long labels, translated text, and large text zoom.

## Verification

- Check no unexpected horizontal scrolling at narrow, medium, and wide sizes.
- Check 200% zoom when text, controls, or fixed panels changed.
- Check focus and hover states do not resize or shift the layout.
