## 2025-05-14 - [Mobile Menu Accessibility]
**Learning:** Toggling `aria-expanded` is necessary but not sufficient for the best screen reader experience on stateful buttons. Explicitly toggling the `aria-label` (e.g., from "Open menu" to "Close menu") provides immediate and clear context to the user about what the button will do next.
**Action:** Always synchronize `aria-expanded`, `aria-label`, and visual icon states for toggle buttons.
