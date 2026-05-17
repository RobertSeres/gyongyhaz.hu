## 2025-05-14 - Keyboard accessibility for custom interactive elements
**Learning:** Interactive elements implemented as `<div>`s instead of `<button>`s or `<a>`s are invisible to keyboard users and screen readers unless explicitly given a `role="button"`, `tabindex="0"`, and event handlers for 'Enter' and 'Space'.
**Action:** Always verify if clickable containers need ARIA roles and keyboard listeners to ensure the interface is accessible to all users.
