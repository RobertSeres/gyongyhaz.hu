# Palette's Journal - Critical UX/Accessibility Learnings

This journal records critical UX and accessibility insights discovered during the development of Gyöngy Ház.

## 2026-07-02 - Structural Landmark Pattern
**Learning:** In legacy monolithic projects with fixed navigation, structural improvements like adding <main> landmarks and 'Skip to Content' links are the highest priority. They significantly reduce repetitive tabbing for keyboard users and provide high immediate value with minimal code churn.
**Action:** Always check for these foundational landmarks first in any accessibility audit of a single-page site.
