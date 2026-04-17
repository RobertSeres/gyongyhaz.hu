## 2025-01-24 - Accessibility labels and interactive feedback
**Learning:** Placeholders are not a substitute for labels. Screen readers need explicit labels (even if hidden via `sr-only`) to provide context for form inputs. Additionally, asynchronous actions (like newsletter signups) need immediate visual feedback (loading states) and accessible confirmation (aria-live) to feel responsive and intuitive.
**Action:** Always add `sr-only` labels to inputs and implement loading/success states for all form submissions.
