## 2025-05-14 - Footer Newsletter Accessibility and Feedback
**Learning:** Standard loose input/button combinations for newsletters lack keyboard accessibility and clear feedback for screen reader users. Wrapping them in a semantic form with an sr-only label and aria-live status message significantly improves the UX for all users.
**Action:** Always wrap newsletter inputs in a <form> and provide aria-live feedback messages for async-like operations.
