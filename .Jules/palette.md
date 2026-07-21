## 2026-02-12 - Structural Landmark Pattern
**Learning:** Pairing a highly visible 'Skip to Content' link with a `<main id="main-content" tabindex="-1" class="focus:outline-none">` landmark drastically improves accessibility for keyboard and screen reader users without introducing visual clutter during normal browsing.
**Action:** Always place the skip-to-content link as the very first child of `<body>` and target a focused `<main>` sibling of the website header and footer.
