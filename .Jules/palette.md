## 2026-05-31 - Structural Landmark Pattern
**Learning:** Pairing a 'Skip to Content' link with a `<main>` landmark that has `tabindex="-1"` and `focus:outline-none` ensures that when a keyboard user jumps to the main content, the focus shifts correctly without a persistent focus ring, while still providing a clear landmark for screen reader users. This is essential in single-page layouts with fixed navigation.
**Action:** Always implement `tabindex="-1"` on the target of skip links to ensure programmatic focus works across all browsers while avoiding visual artifacts for mouse users.
