## 2024-05-26 - Accessibility Foundations: Skip Link & Main Landmark

**Learning:** In legacy monolithic HTML projects with fixed navigation, structural improvements like adding `<main>` landmarks and 'Skip to Content' links are the highest priority and should be the first check in an accessibility audit; they significantly reduce repetitive tabbing for keyboard users and provide high immediate value with minimal code churn.

**Action:** When starting an audit for a static, single-page repository, prioritize adding a "Skip to Content" link and wrapping the primary content in a `<main>` tag to establish a solid accessibility foundation before implementing more granular micro-UX changes.
