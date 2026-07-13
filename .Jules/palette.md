## 2025-05-14 - Structural Landmark Pattern
**Learning:** Pairing a 'Skip to Content' link with a `<main>` landmark that has `tabindex="-1"` and `focus:outline-none` ensures that keyboard users can bypass repetitive navigation and that focus is programmatically shifted to the correct starting point without persistent visual artifacts.
**Action:** Always implement this pattern as the first child of `<body>` and wrap the primary content area to satisfy WCAG 2.4.1 (Bypass Blocks).
