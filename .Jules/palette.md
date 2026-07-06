# Palette's Journal - Critical UX/Accessibility Learnings

This journal records critical UX and accessibility insights discovered during the development of Gyöngy Ház.

## 2025-05-15 - Structural Landmark Pattern
**Learning:** In monolithic single-page sites with fixed navigation, a 'Skip to Content' link is essential for keyboard navigation, but it must be paired with a `<main>` landmark that has `tabindex="-1"` and `focus:outline-none`. This ensures that focus shifts correctly to the start of the content area across all browsers without leaving a permanent visual focus ring on the entire section container.
**Action:** Always wrap primary content in `<main id="main-content" tabindex="-1" class="focus:outline-none">` and provide a corresponding skip link as the first focusable element in the `<body>`.
