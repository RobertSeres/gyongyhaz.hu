## 2026-03-14 - Unified Mobile Menu State Management
**Learning:** In Tailwind-based static sites with multiple menu trigger points (the main toggle button and internal nav links), state synchronization for ARIA attributes and Font Awesome icon classes frequently becomes inconsistent if managed by separate event listeners.
**Action:** Use a single, unified `toggleMenu(forceClose)` function to centralize the toggling of visibility classes, `aria-expanded` attributes, and Font Awesome icon swaps (e.g., `fa-bars` to `fa-xmark`). This ensures the screen reader state and visual indicators are always in lockstep.

## 2026-03-14 - Modal and Popup Semantic Separation
**Learning:** Full-screen modals (Newsletter, Coupons) and sticky non-modal popups (Review prompt) require different ARIA configurations. Using `aria-modal="true"` on non-modal sticky popups can unintentionally trap focus or confuse users navigating the background content.
**Action:** Apply `role="dialog"` and `aria-labelledby` to all popups, but restrict `aria-modal="true"` to true overlay modals that require focus trapping. For sticky popups, manage accessibility tree visibility via `aria-hidden` or simple visibility logic while keeping the rest of the page interactable.
