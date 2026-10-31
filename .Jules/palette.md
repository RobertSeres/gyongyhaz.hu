# Palette's UX Journal

## 2025-05-18 - Structural Landmark Pattern (Skip to Content & Main Landmark)
**Learning:** Monolithic landing pages often have heavy fixed navigation and animated hero banners, forcing keyboard-only and screen reader users to tab through dozens of links before reaching primary content. Implementing a 'Skip to Content' link paired with `<main id="main-content" tabindex="-1" class="focus:outline-none">` enables seamless bypass (WCAG 2.4.1) while preventing visual outline artifacts upon programmatic focus.
**Action:** Always place the skip-to-content anchor as the first child of `<body>`, style it with high contrast against the theme (`bg-pastel-purple text-dark-bg`), ensure high z-index (`z-[150]`) above fixed navigations/modals, and pair it with a semantic `<main>` landmark with `tabindex="-1"`.
