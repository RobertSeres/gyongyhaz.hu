# Palette's Journal - Critical UX Learnings

## 2026-01-12 - Structural Landmark Pattern (WCAG 2.1 SC 2.4.1)
**Learning:** Pairing an accessible, high-contrast 'Skip to Content' link with a semantically defined `<main>` landmark with `tabindex="-1"` and `focus:outline-none` allows keyboard and assistive technology users to immediately bypass repetitive fixed navigation headers directly into the main interactive page content without retaining an awkward persistent focus outline.
**Action:** When working on single-page landing pages with fixed navbars, always ensure the skip link is the first focusable element in `<body>` with high `z-index` and sufficient color contrast against dark backgrounds.
