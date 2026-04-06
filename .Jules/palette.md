## 2025-05-24 - Accessibility Overhaul & Feedback Loops

**Learning:** Static landing pages with many popups/modals often lack proper ARIA attributes and feedback mechanisms. Users need visual confirmation for actions like form submissions, and screen readers need descriptive labels and roles to navigate interactive elements correctly.

**Action:** Always wrap newsletter inputs in a `<form>` to allow "Enter" key submission, and provide a clear success/loading state. For popups, use `role="dialog"`, `aria-modal="true"`, and `aria-labelledby`. For popups that use CSS transitions (like `translate-y`), also toggle `aria-hidden` and `pointer-events-none` to manage the accessibility tree and prevent accidental interaction when "hidden".
