## 2025-05-15 - Structural Landmark & Skip-Link Integration
**Learning:** In monolithic landing pages with fixed headers and high z-index overlays (like the newsletter modal), a "Skip to Content" link requires explicit `focus:fixed` and a higher `z-index` (e.g., `z-[150]`) to ensure it is visible and functional over all UI elements when keyboard-focused.
**Action:** Pair 'Skip to Content' with a `<main tabindex="-1">` landmark to ensure programmatic focus shift works reliably across all browsers without persistent visual focus rings.

## 2025-05-15 - Synchronized Mobile Menu Accessibility
**Learning:** Accessibility for mobile menus is more than just a toggle; it requires synchronized updates to `aria-expanded`, dynamic `aria-label` (Open vs Close), and Font Awesome icon swapping within the same interaction handler to prevent state desync in the accessibility tree.
**Action:** Always wrap state changes in a centralized JavaScript function and verify that navigation clicks also reset these attributes if the menu auto-closes.
