# Palette's UX Journal

## 2025-02-14 - Skip-to-Content & Structural Landmark Pattern in Static Landing Pages
**Learning:** In monolithic single-page marketing sites with fixed navigation bars and high-z-index overlays, keyboard and screen reader accessibility is severely hindered if landmark navigation is missing. Pairing a high-contrast 'Skip to Content' link (`z-[150]`) with a `<main tabindex="-1">` landmark satisfies WCAG 2.4.1 (Bypass Blocks) and ensures focus moves smoothly to main content without visual outlines persisting after click.
**Action:** Always provide a first-child skip link targeting a `<main id="main-content" tabindex="-1">` wrapper with Hungarian localized copy (`Ugrás a tartalomra`) and pair `bg-pastel-purple` with `text-dark-bg` for WCAG AA contrast.
