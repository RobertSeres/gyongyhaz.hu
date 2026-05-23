# Palette's Journal - Critical Learnings

## 2025-05-14 - [Accessibility & Navigation]
**Learning:** In legacy monolithic HTML projects with fixed navigation, structural improvements like adding `<main>` landmarks and 'Skip to Content' links are the highest priority. They significantly reduce repetitive tabbing for keyboard users and provide high immediate value with minimal code churn.
**Action:** Always implement `<main>` and a skip link as the first step in an accessibility audit for single-page layouts.

## 2025-05-14 - [Mobile Menu Accessibility]
**Learning:** Mobile navigation implementations often fail to communicate state to screen readers. Synchronizing `aria-expanded`, dynamic `aria-label`, and visual icon classes (e.g., swapping `fa-bars` to `fa-times`) through a centralized JavaScript function ensures a consistent experience for all users.
**Action:** Use a unified `toggleMenu` function to handle all state changes (ARIA, icons, and visibility) rather than fragmented event listeners.
