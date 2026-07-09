# Palette's Journal - Critical UX & Accessibility Learnings

This journal records critical UX and accessibility insights discovered during the development of this project.

## 2026-07-09 - Structural Landmark Pattern
**Learning:** Pairing a 'Skip to Content' link with a <main> landmark that has tabindex="-1" and focus:outline-none ensures that when a keyboard user jumps to the main content, the focus shifts correctly without a persistent focus ring, while still providing a clear landmark for screen reader users.
**Action:** Always implement this pattern in monolithic HTML projects to significantly reduce repetitive tabbing for keyboard users.
