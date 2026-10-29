---
name: design-review
description: Review an existing screen, component or product journey for visual hierarchy, information density, consistency, interaction quality and responsive usability. Use when improving layout, styling or behaviour while preserving the product's purpose and established brand.
license: MIT
---

# Design review

Default philosophy: simple design, intense content, with Edward Tufte as an influence on information clarity. Make useful information easy to understand and actions easy to complete. This is a preference for clarity and substance, not a requirement to make every product look identical.

## Start with the actual experience

Identify the user's task, audience, primary action and constraints. Inspect the screenshot or implementation before prescribing a style. For interactive or responsive problems, inspect the relevant states in a browser when available; say when the review is limited to screenshots.

Preserve established typography, colour, components and working interactions unless they cause a demonstrated problem or the user requests a change. Do not force dark mode, light mode, a new font or a new design system. Treat instructions specific to the project as stronger than this skill's defaults.

## Apply the design judgment

- Give content a clear reading order. Use typography, alignment and proximity before adding containers, badges or decoration. An explanation should be understandable without its surrounding marketing copy.
- Use available space deliberately. Avoid unnecessarily narrow desktop layouts, oversized empty regions and padding that creates avoidable scrolling. Do not sacrifice legibility, touch targets or natural scrolling on small screens to force everything into one viewport.
- Prefer meaningful information density over visual noise. Charts need readable labels, units, time ranges and an honest representation of the data. Images and illustrations should explain something rather than fill space.
- Make navigation consistent across related pages: placement, active state, widths and predictable destinations. Keep the primary task clear; remove redundant links and nested paths that make people lose their place.
- Check long titles, names, topic labels and realistic content. Let text wrap or reorganise before it overlaps controls or overflows. Do not truncate essential meaning just to preserve a tidy mockup.
- Treat hover as an enhancement. Essential information and controls must also work with touch and keyboard. In-card summaries or an explicit disclosure may be more appropriate than tooltips on mobile.
- Keep action placement predictable. Expanding help should not cover neighbouring content or unexpectedly move a primary action while someone is trying to use it. Reserve sensible space or choose another disclosure pattern; do not pin every element simply to eliminate all layout movement.
- Check contrast, focus visibility, labels, target sizes and content at zoom. Include loading, empty, error and success states when relevant to the problem.

For exports or share images, inspect the generated artifact, not only its HTML preview. Ensure the content fits, labels remain readable at the intended display size, and theme and selected content match the user's choice. Buttons should accurately describe what the destination or clipboard can actually receive.

## Make the review actionable

Explain what to keep, the few highest-impact problems and concrete changes tied to the task. Refer to the relevant screen region, state or component. Avoid a catalogue of subjective complaints or a generic redesign presentation.

For implementation requests, make the authorised changes and check realistic desktop and mobile states, long content, keyboard access and any behaviour affected by the change. Do not turn a focused correction into a brand overhaul. State which screens and interactions were inspected and what remains unverified.
