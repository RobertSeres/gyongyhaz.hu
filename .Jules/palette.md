# Palette's Journal - Gyöngy Ház

## 2025-05-14 - Structural Landmark Pattern
**Learning:** Pairing a 'Skip to Content' link with a <main> landmark that has tabindex="-1" and focus:outline-none ensures that when a keyboard user jumps to the main content, the focus shifts correctly without a persistent focus ring, while still providing a clear landmark for screen reader users.
**Action:** Use this pattern in legacy monolithic HTML projects to improve navigation efficiency for keyboard and screen reader users.

## 2025-05-14 - Interactive Element Accessibility in Non-Semantic Markup
**Learning:** In projects using 'div' elements as buttons with 'onclick' handlers, adding 'role="button"', 'tabindex="0"', and keyboard event listeners (Enter/Space) is crucial for restoring accessibility without disrupting the existing CSS layout.
**Action:** Always audit for non-semantic interactive elements and apply appropriate ARIA roles and keyboard support.
