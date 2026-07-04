# Palette's Journal - Critical UX/Accessibility Learnings

This journal records critical UX and accessibility insights discovered during the development of Gyöngy Ház.

## 2026-07-04 - Structural Landmark Pattern in Monolithic HTML
**Learning:** In legacy monolithic HTML projects with fixed navigation, structural improvements like adding `<main>` landmarks and 'Skip to Content' links are the highest priority. They significantly reduce repetitive tabbing for keyboard users and provide high immediate value with minimal code churn.
**Action:** Always check for `<main>` landmarks and skip-links as the first step in an accessibility audit for single-page applications.
