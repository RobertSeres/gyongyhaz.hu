## 2026-03-06 - Structural Landmark Pattern
**Learning:** Pairing a 'Skip to Content' link with a `<main>` landmark that has `tabindex="-1"` and `focus:outline-none` ensures keyboard users can bypass repetitive navigation modules easily, and that browser focus shifts correctly without generating a persistent, distracting focus ring on the main content block itself.
**Action:** When working on monolithic or single-page applications, always place a high-contrast 'Skip to Content' link as the first child of the `<body>`, and target a sibling `<main>` landmark wrapping the primary content.
