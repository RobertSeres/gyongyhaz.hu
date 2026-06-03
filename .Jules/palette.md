## 2025-05-14 - Structural Landmark and Skip Link Pattern

**Learning:** In legacy monolithic HTML projects with fixed navigation, structural improvements like adding `<main>` landmarks and 'Skip to Content' links are the highest priority. They significantly reduce repetitive tabbing for keyboard users and provide high immediate value with minimal code churn. Pairing a 'Skip to Content' link with a `<main>` landmark that has `tabindex="-1"` and `focus:outline-none` ensures that when a keyboard user jumps to the main content, the focus shifts correctly without a persistent focus ring.

**Action:** Always check for `<main>` landmarks and skip links first in single-page static sites. Ensure the skip link is the first interactive element in the `<body>` and use Tailwind's `sr-only focus:not-sr-only` classes for high-contrast accessibility.
