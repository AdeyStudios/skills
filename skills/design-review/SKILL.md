---
name: design-review
description: Review an interface when platform scope is mixed or unspecified, diagnosing hierarchy, information density, screen responsibilities and interaction quality. Use web-design for a known browser task and mobile-design for a known native app; this review also works independently.
license: MIT
---

# Design review

Working draft. Default philosophy: simple design, intense content, with Edward Tufte as an influence on information clarity. Make useful information easy to understand and actions easy to complete. Clarity does not require a flat, document-like interface: meaningful surfaces, visual identity and responsive interaction can improve it. This is not a requirement to make every product look identical.

## Research

Identify the user's task, audience, primary action, platform and constraints. Inspect the screenshot or implementation before prescribing a style. Trace the actual task in the browser or app when available; say when the review is limited to screenshots.

Establish the requested depth: review, focused correction or structural redesign. For a rethink, inspect screen responsibilities, navigation and the complete interaction before styling existing components. For a local problem, keep the correction local. Preserving functionality does not mean freezing a structure the user asked to replace.

If a specialist is available, use `web-design` for browser experiences (including mobile websites/PWAs) or `mobile-design` for native apps. Do not require another skill to complete this review: the principles below stand alone. For mixed work, apply each platform's conventions rather than enforcing one interaction model everywhere.

Preserve established typography, colour, components and working interactions unless they cause a demonstrated problem or the user requests a change. Do not force dark mode, light mode, a new font or a new design system. Treat instructions specific to the project as stronger than this skill's defaults.

## Execute

- Give content a clear reading order. Use typography, alignment and proximity before adding containers, badges or decoration. An explanation should be understandable without its surrounding marketing copy.
- Use available space deliberately. Avoid unnecessarily narrow desktop layouts, oversized empty regions and padding that creates avoidable scrolling. Do not sacrifice legibility, touch targets or natural scrolling on small screens to force everything into one viewport.
- Prefer meaningful information density over visual noise. Charts need readable labels, units, time ranges and an honest representation of the data. Images and illustrations should explain something rather than fill space.
- Make navigation consistent across related pages: placement, active state, widths and predictable destinations. Keep the primary task clear; remove redundant links and nested paths that make people lose their place.
- Check long titles, names, topic labels and realistic content. Let text wrap or reorganise before it overlaps controls or overflows. Do not truncate essential meaning just to preserve a tidy mockup.
- Treat hover as an enhancement. Essential information and controls must also work with touch and keyboard. In-card summaries or an explicit disclosure may be more appropriate than tooltips on mobile.
- Keep action placement predictable. Expanding help should not cover neighbouring content or unexpectedly move a primary action while someone is trying to use it. Reserve sensible space or choose another disclosure pattern; do not pin every element simply to eliminate all layout movement.
- Check contrast, focus visibility, labels, target sizes and content at zoom. Include loading, empty, error and success states when relevant to the problem.
- Group the main task, detail, configuration and account concerns deliberately. Use appropriate platform components and consider its interaction opportunities; a native app need not behave like a small web document, and a website need not imitate native chrome.
- Give actions clear feedback and use purposeful, interruptible motion where it helps. Respect reduced motion. Consider capabilities such as voice only when they improve the task; permission denial and fallback are part of the design. Do not add effects or features merely to make the screen appear busy.

When reviewing progress, success moments, perceived waiting or competing choices, read [references/behavioural-design.md](references/behavioural-design.md). Apply these principles to the user's task; do not add gamification, decoration or delays merely to invoke a psychological effect.

For exports or share images, inspect the generated artifact, not only its HTML preview. Ensure the content fits, labels remain readable at the intended display size, and theme and selected content match the user's choice. Buttons should accurately describe what the destination or clipboard can actually receive.

## Verify

Explain what to keep, the few highest-impact problems and concrete changes tied to the task. Refer to the relevant screen region, state or component. Avoid a catalogue of subjective complaints or a generic redesign presentation.

For implementation requests, make the authorised changes and exercise the affected task, including long content, keyboard open/closed, navigation, relevant failure/retry and completion states. Inspect rendered accessibility-size layouts as well as bounds; a technically reachable control can still look broken. Use browser/device checks appropriate to the platform, and distinguish simulation from physical audio, haptics and gestures. State which screens and interactions were inspected and what remains unverified. Do not turn a focused correction into a brand overhaul or claim product impact from build success.
