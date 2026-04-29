## 2025-05-01 - [Modal & Form Accessibility]
**Learning:** Modals and sticky popups require explicit ARIA roles (dialog), modal states (aria-modal), and title associations (aria-labelledby) to be truly accessible. Additionally, converting interactive divs to forms improves semantics but requires explicit prevention of default submission behavior to avoid page reloads on static sites.
**Action:** Always wrap input groups in `<form onsubmit="event.preventDefault();">` and ensure all modals have `role="dialog"` and are labeled by their primary heading.
