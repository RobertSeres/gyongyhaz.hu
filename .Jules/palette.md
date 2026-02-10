# Palette's Journal - Gyöngy Ház

## 2025-05-14 - Static Site Accessibility Gaps
**Learning:** Static marketing sites often suppress focus outlines (`focus:outline-none`) for visual reasons without providing alternatives, breaking keyboard navigation. They also frequently rely on placeholders instead of labels for forms. These patterns can be addressed cleanly using Tailwind's `focus:ring` and `sr-only` classes without impacting the visual design for most users.
**Action:** Systematically check for and replace `focus:outline-none` with accessible rings and ensure all inputs have linked `<label>` elements (visually hidden if necessary).
