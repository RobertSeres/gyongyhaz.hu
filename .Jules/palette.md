# Palette's Journal

## 2026-03-06 - Structural Landmark Pattern
**Learning:** Pairing a hidden-by-default 'Skip to Content' (Ugrás a tartalomra) link with a `<main>` landmark element that has `tabindex="-1"` and `class="focus:outline-none"` ensures keyboard users can successfully bypass repetitive header navigation links without causing persistent visual focus rings on subsequent mouse interactions.
**Action:** Always place the skip-to-content link as the very first interactive child inside the `<body>` element, preceding the sticky header/navigation layout blocks, and target a `<main>` sibling element wrapper of the core landing sections.
