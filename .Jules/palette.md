# Palette's Journal - Gyöngy Ház

## 2025-05-22 - Structural Landmark Pattern
**Learning:** In legacy monolithic HTML projects with fixed navigation, structural improvements like adding <main> landmarks and 'Skip to Content' links are the highest priority. They significantly reduce repetitive tabbing for keyboard users.
**Action:** Always implement a 'Skip to Content' link paired with a <main> landmark (with tabindex="-1" and focus:outline-none) to ensure focus shifts correctly.
