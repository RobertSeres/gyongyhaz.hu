# Palette's UX Journal

## 2025-08-03 - Structural Landmark Pattern
**Learning:** Pairing a skip link with a `<main>` landmark element that has `tabindex="-1"` and `focus:outline-none` provides critical keyboard bypass capabilities (WCAG 2.1 2.4.1 Bypass Blocks) and allows programmatic focus shift without a persistent visual focus ring.
**Action:** Always implement a 'Skip to Content' link targeting a `<main id="main-content" tabindex="-1" class="focus:outline-none">` as the first interactive element inside `<body>`.
