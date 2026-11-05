# Palette's UX Journal

## 2025-05-18 - Structural Landmark Pattern & Skip Link
**Learning:** Single-page landing pages with fixed/sticky headers often lack semantic structure and skip links, forcing keyboard and screen reader users to repeatedly navigate through top-level navigation items. Adding a skip link (`sr-only` until focused) combined with a semantic `<main id="main-content" tabindex="-1">` landmark satisfies WCAG 2.4.1 (Bypass Blocks) and allows programmatic focus shift upon activation without leaving an unwanted persistent visual outline (`focus:outline-none`).
**Action:** When working on monolithic or single-page static sites, check for semantic landmarks (`<main>`, `<header>`, `<footer>`) and always implement a high-contrast 'Skip to Content' link as the very first focusable element inside `<body>`.
