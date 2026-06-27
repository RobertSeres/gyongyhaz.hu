# Palette's Journal - Critical UX/Accessibility Learnings

This journal records critical UX and accessibility insights discovered during the development of Gyöngy Ház.

## 2025-01-24 - Structural Landmark Pattern
**Learning:** In legacy monolithic HTML projects with fixed navigation, structural improvements like adding `<main>` landmarks and 'Skip to Content' links are the highest priority. They significantly reduce repetitive tabbing for keyboard users and provide high immediate value with minimal code churn. Pairing a 'Skip to Content' link with a `<main>` landmark that has `tabindex="-1"` and `focus:outline-none` ensures that when a keyboard user jumps to the main content, the focus shifts correctly without a persistent focus ring.
**Action:** Always check for basic navigation landmarks and skip links first in single-page applications.
