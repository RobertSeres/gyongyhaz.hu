# Palette's Journal - Critical UX/Accessibility Learnings

This journal records critical UX and accessibility insights discovered during the development of Gyöngy Ház.


## 2025-05-22 - Structural Landmark Pattern for Monolithic Sites
**Learning:** Pairing a 'Skip to Content' link with a <main> landmark that has tabindex="-1" and focus:outline-none is the most effective way to improve keyboard navigation in legacy monolithic HTML projects. It bypasses repetitive navigation and ensures focus shifts correctly without persistent visual rings.
**Action:** Implement this pattern as the first step in any accessibility audit for single-page applications to provide immediate high-impact value.
