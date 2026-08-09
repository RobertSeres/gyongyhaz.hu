# Palette's Journal - Critical UX/Accessibility Learnings

## 2026-02-12 - Structural Landmark Pattern (Bypass Blocks)
**Learning:** The 'Structural Landmark Pattern' involves pairing a 'Skip to Content' link with a `<main>` landmark that has `tabindex="-1"` and `focus:outline-none`. This ensures that when a keyboard user jumps to the main content, the focus shifts correctly without a persistent focus ring, while still providing a clear landmark for screen reader users and satisfying WCAG 2.1 Success Criterion 2.4.1 (Bypass Blocks) for keyboard accessibility.
**Action:** Always implement a highly visible-on-focus, high-contrast, pill-shaped 'Skip to Content' link immediately inside the `<body>` element, and pair it with a uniquely identified `<main id="main-content" tabindex="-1" class="focus:outline-none">` landmark wrapping the primary unique content of the page.
