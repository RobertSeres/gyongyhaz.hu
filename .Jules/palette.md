# Palette's UX & Accessibility Journal

## 2026-02-12 - The Structural Landmark & Skip to Content Link Pattern
**Learning:** Pairing a 'Skip to Content' bypass link with a `<main>` landmark that has `tabindex="-1"` and `focus:outline-none` is a highly effective, low-impact accessibility win. Placing the bypass link as the absolute first child of `<body>` ensures it is immediately discoverable by screen reader and keyboard-only users, while maintaining site-wide landmarks as siblings prevents semantic errors.
**Action:** When working on monolithic or single-page static sites, always evaluate if bypass blocks are supported. Implement a high-contrast 'Skip to Content' link paired with a `<main id="main-content" tabindex="-1" class="focus:outline-none">` wrapper as the primary accessibility foundation.
