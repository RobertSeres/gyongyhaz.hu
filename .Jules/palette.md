## 2025-05-14 - Modal Interference in Accessibility Verification
**Learning:** In projects with non-deterministic UI interruptions (like timed newsletter modals), automated accessibility tests for keyboard navigation (e.g., 'Skip to Content' links) can fail or produce misleading screenshots if the modal captures focus or obscures the target.
**Action:** Always include logic in Playwright/verification scripts to proactively identify and dismiss known modals before asserting focus states or taking screenshots of base-layer accessibility features.
