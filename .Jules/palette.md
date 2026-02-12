# Palette's Journal - Gyöngy Ház

## 2025-05-14 - Initial Audit
**Learning:** Found several accessibility and micro-UX issues in a static landing page:
1. Icon-only links (star ratings) lack ARIA labels.
2. Gallery images lack descriptive alt text.
3. Interactive content (service descriptions) depends entirely on hover, making it inaccessible to touch and keyboard users.
4. Promotional popups lack frequency capping (localStorage logic is disabled), leading to poor user experience on repeated visits.

**Action:** Prioritize fixing the hover-dependent content and missing ARIA labels to ensure the site is usable for everyone.

## 2025-05-15 - Accessible Hover-Content Pattern
**Learning:** For static brochure sites using CSS transitions for "hover reveal" content, keyboard accessibility can be achieved without JavaScript by using `tabindex="0"` on the container and the `:focus-within` CSS pseudo-class. This ensures the content is visible to keyboard users while they navigate. Combining this with `focus-visible` styles prevents visual clutter for mouse users.
**Action:** Apply the `tabindex="0"` + `:focus-within` pattern when encountering hover-only informational elements.
