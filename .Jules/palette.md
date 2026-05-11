# Palette's Journal - Gyöngy Ház

## 2025-01-24 - Structural Accessibility Implementation
**Learning:** In legacy monolithic HTML projects, structural navigation improvements (specifically adding `<main>` landmarks and 'Skip to Content' links) are prioritized over fine-grained component accessibility fixes as they provide the highest immediate value for keyboard and screen reader users with minimal code churn.
**Action:** Always verify landmark hierarchy (e.g., `<main>` and `<footer>` as siblings) and ensure skip links target a focusable container with `tabindex="-1"`.
