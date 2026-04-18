## 2025-05-22 - Footer Newsletter Accessibility and Feedback
**Learning:** The footer newsletter was missing semantic form structure, accessible labels, and feedback for asynchronous operations. Implementing a hidden label for screen readers and a loading state with `aria-live` significantly improves the UX for all users.
**Action:** Always ensure form inputs have associated labels (visible or `sr-only`) and provide immediate visual/audible feedback for asynchronous submissions using spinners and `aria-live`.
