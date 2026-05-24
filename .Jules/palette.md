## 2025-05-14 - [Accessibility] Structural Landmarks and Keyboard Navigation
**Learning:** In legacy monolithic HTML projects, structural improvements like adding `<main>` landmarks and 'Skip to Content' links are the highest priority. They significantly reduce repetitive tabbing for keyboard users. Additionally, interactive elements implemented as `div` or `section` tags must have `role="button"`, `tabindex="0"`, and keyboard event handlers to be accessible.
**Action:** Always check for basic document structure (landmarks) first. When encountering non-semantic interactive elements, ensure they have proper ARIA roles and keyboard support.

## 2025-05-14 - [UX] Success Feedback and Form Accessibility
**Learning:** Providing clear feedback after form submission (like the newsletter) is crucial for UX. Using 'sr-only' labels for compact forms allows maintaining the visual design while providing context for screen readers.
**Action:** Implement hidden labels for visual-minimalist forms and ensure dynamic success messages are accessible.
