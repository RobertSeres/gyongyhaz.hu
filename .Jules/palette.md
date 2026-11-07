# Palette's UX Journal

## 2025-05-18 - Structural Landmark Pattern: Skip to Content & Main Landmark
**Learning:** In a single-page landing layout with a fixed navigation bar and heavy interactive content, keyboard and screen reader users must navigate through redundant header links on every reload unless a bypass mechanism is provided. Implementing a 'Skip to Content' link paired with `<main id="main-content" tabindex="-1" class="focus:outline-none">` fulfills WCAG 2.1 SC 2.4.1 (Bypass Blocks) and reliably transfers keyboard focus directly to the main content area without displaying an undesirable persistent focus ring.
**Action:** When working on static single-page landing sites, pair a visually-hidden, high-contrast focusable skip link (`sr-only focus:not-sr-only focus:fixed`) placed at the top of `<body>` with a programmatic `<main tabindex="-1">` landmark to enable effortless keyboard bypass.
