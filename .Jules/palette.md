# Palette's UX Journal

## 2025-05-15 - Structural Landmark Pattern
**Learning:** Pairing a 'Skip to Content' link with a `<main>` landmark that has `tabindex="-1"` and `focus:outline-none` ensures that when a keyboard user jumps to the main content, the focus shifts correctly without a persistent focus ring, while still providing a clear landmark for screen reader users.
**Action:** Always implement this pattern in single-page applications to improve keyboard and screen reader accessibility.
