## 2025-01-24 - Footer Newsletter Accessibility and Feedback
**Learning:** In simple single-page sites, form elements are often replaced by generic divs. Converting these to semantic <form> elements with proper <label> (even if sr-only) and providing clear async feedback (loading state + success message) significantly improves accessibility and UX without changing the visual design.
**Action:** Always check if interactive inputs are wrapped in semantic <form> tags and provide immediate feedback for all simulated or real async actions.
