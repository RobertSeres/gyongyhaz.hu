## 2025-05-14 - Mobile Menu Accessibility & State Feedback
**Learning:** Mobile navigation toggles in static sites often lack programmatic state (ARIA) and keyboard focus indicators. Simply hiding/showing a div is insufficient; synchronizing `aria-expanded`, dynamic `aria-label` updates, and swapping icons (hamburger to close) provides the necessary context for both sighted and screen-reader users.
**Action:** For every interactive toggle (menus, accordions, modals), ensure `aria-expanded` and `aria-label` are updated in the same JavaScript function that handles the visual transition.
