## 2025-05-14 - Mobile Menu & Modal Accessibility
**Learning:** Static websites often neglect the state of interactive elements like mobile menus and modals, leading to poor screen reader experiences. Specifically, the absence of `aria-expanded` and `role="dialog"` makes it difficult for users to understand the current UI state.
**Action:** Always include `aria-expanded` on toggle buttons and ensure JavaScript updates it. Use `role="dialog"` and `aria-modal="true"` for all popups to trap screen reader focus correctly.
