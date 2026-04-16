## 2025-05-14 - [A11y & Feedback Improvements]
**Learning:** The project lacked basic accessibility features like ARIA labels for icon-only buttons and proper labels for form inputs. Additionally, the footer newsletter provided no feedback to the user upon submission.
**Action:** Always verify that icon-only buttons have `aria-label`, inputs have associated `<label>` (can be `sr-only`), and interactive forms provide immediate visual confirmation of success.
