## 2025-05-14 - Mobile Menu Accessibility and Feedback
**Learning:** For mobile menus, adding `aria-expanded` and `aria-controls` is crucial for screen readers, but synchronizing these with visual icon changes (e.g., hamburger to 'X') and dynamic `aria-label` updates provides a much more intuitive experience for all users.
**Action:** Always use a centralized state management function for UI components with multiple triggers (like menu buttons and links) to ensure accessibility attributes and visual states remain perfectly synchronized.

## 2025-05-14 - Playwright Visibility Verification
**Learning:** When verifying Tailwind's `hidden` class in Playwright for elements that also use responsive variants like `md:hidden`, standard `.to_have_class(re.compile(r"hidden"))` can produce false positives.
**Action:** Use regex word boundaries or explicit class list checking to ensure you are targeting the exact visibility utility.
