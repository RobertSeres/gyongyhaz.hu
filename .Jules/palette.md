# Palette's Journal - Critical UX/Accessibility Learnings

This journal records critical UX and accessibility insights discovered during the development of Gyöngy Ház.

## 2025-05-15 - High Z-Index Skip Links
**Learning:** In projects with fixed navigation bars and high-z-index components (like the newsletter modal at `z-[100]`), a 'Skip to Content' link requires explicit `focus:fixed` positioning and a higher `z-index` (e.g., `z-[150]`) to ensure it remains visible and accessible above all other overlays when focused.
**Action:** Always verify focus visibility of skip links against all fixed-position UI elements.
