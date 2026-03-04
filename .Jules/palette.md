# Palette's Journal - Gyöngy Ház

## 2025-01-24 - Mobile Menu Accessibility Pattern
**Learning:** For mobile menu implementations, standardizing ARIA attributes and visual feedback (icons) in a single state management function ensures synchronization across multiple triggers (menu button and links).
**Action:** Always toggle `aria-expanded`, set `aria-controls`, update `aria-label`, and swap Font Awesome icon classes (e.g., `fa-bars` to `fa-xmark`) via JavaScript.

## 2025-01-24 - Focus Indicators and Accessibility
**Learning:** Using `focus:outline-none` without providing a visible alternative breaks keyboard navigation. Tailwind's `focus:ring` classes provide a consistent way to maintain accessibility while fitting the design.
**Action:** Replace `focus:outline-none` with `focus:ring-2 focus:ring-pastel-purple` or similar theme-aligned focus indicators.

## 2025-01-24 - Accessibility Tree Consistency
**Learning:** When a UI element is hidden/shown using CSS transforms or opacity instead of `display: none`, the accessibility tree remains unchanged unless `aria-hidden` is toggled.
**Action:** JavaScript must toggle the `aria-hidden` attribute alongside visual state changes to ensure screen readers ignore hidden content.

## 2025-01-24 - Playwright Testing with Timed Popups
**Learning:** Timed popups (newsletter ~1s, review ~5s) can interfere with Playwright tests. Elements with `opacity-0` can still intercept clicks.
**Action:** Verification scripts must wait for the `hidden` class or use `state='hidden'` to ensure elements are non-blocking before interacting with the main UI. Dismiss the newsletter by clicking 'Nem, lemaradok a kedvezményekről'.
