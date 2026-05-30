## 2025-05-14 - Structural Landmark Pattern

**Learning:** In legacy monolithic HTML projects with fixed navigation, structural improvements like adding `<main>` landmarks and 'Skip to Content' links are the highest priority and should be the first check in an accessibility audit; they significantly reduce repetitive tabbing for keyboard users and provide high immediate value with minimal code churn.

**Action:** Pair a 'Skip to Content' link with a `<main>` landmark that has `tabindex="-1"` and `focus:outline-none`; this ensures that when a keyboard user jumps to the main content, the focus shifts correctly without a persistent focus ring, while still providing a clear landmark for screen reader users.
