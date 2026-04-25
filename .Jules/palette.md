# Palette's UX Journal 🎨

Critical UX and accessibility learnings for the Gyöngy Ház repository.

## 2025-01-24 - Mobile Menu & Modal Accessibility
**Learning:** For mobile-first interfaces with Font Awesome icons, visual state changes (like 'bars' to 'times') must be synchronized with ARIA attributes (`aria-expanded`, dynamic `aria-label`) through a centralized state manager to ensure consistency for all users.
**Action:** Use a unified `toggleMenu` function for all menu triggers (button and links) and apply similar logic to modals.
