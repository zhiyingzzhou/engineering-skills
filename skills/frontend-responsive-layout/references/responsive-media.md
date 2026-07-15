# Responsive Media

Use this reference for images, video, iframes, charts, embeds, art direction, and layout stability.

## Images

- Provide stable dimensions with `width`/`height`, aspect-ratio, or equivalent layout constraints.
- Use `srcset` and `sizes` for responsive raster images.
- Use `picture` when the crop or art direction must change by layout context.
- Do not lazy-load likely LCP media.
- Keep downloaded image dimensions close to displayed dimensions and density.

## Media Containers

- Wrap videos, iframes, maps, and charts in stable ratio or height containers.
- Provide an overflow strategy for wide charts, tables, or diagrams.
- Preserve the subject of cropped images at every breakpoint.
- Separate decorative background media from content images that need alt text and intrinsic sizing.

## Layout Stability

- Reserve space for media before it loads.
- Avoid late insertion above existing content unless the space is preallocated.
- Coordinate with performance work when media changes could affect LCP or CLS.

## Verification

- Check narrow, medium, and wide sizes.
- Check high-density displays when image sharpness matters.
- Record whether media loading and LCP impact were verified.
