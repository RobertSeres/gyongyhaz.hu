## 2025-05-14 - Multi-Trigger UI State Synchronization
**Learning:** When a UI component like a mobile menu has multiple trigger points (e.g., a toggle button and internal navigation links), using a centralized state management function is crucial to keep ARIA attributes (`aria-expanded`), visual states (icons), and interaction states in sync.
**Action:** Always create a unified `toggle[Component]` function that accepts an optional force-state parameter to ensure consistent accessibility and visual feedback across all interaction points.

## 2025-05-14 - Modal Accessibility Management
**Learning:** For non-modal popups that use CSS transforms/opacity for visibility (like sticky reviews), managing `aria-hidden` and `pointer-events-none` manually via JavaScript is necessary to ensure they don't remain in the accessibility tree or intercept clicks while "hidden".
**Action:** Implement an `updateAccessibility` helper for all dynamic UI elements to toggle both screen reader visibility and interaction capability.
