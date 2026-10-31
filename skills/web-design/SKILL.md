---
name: web-design
description: Design, review or restructure websites and browser-based apps for responsive layout, visual identity, semantic components and keyboard, pointer and touch interaction. Includes mobile websites and PWAs; native iOS and Android app design is a separate workflow.
license: MIT
---

# Web design

Working draft. Make the page or app useful, distinctive and fluent in the browser. Clear design can be expressive; it does not require a bare document or a generic hero-and-cards template.

## Research

- Establish the audience, primary task, route/page type, current stack/design system and requested depth: review, focused correction or structural redesign. A marketing page, long explanation and working dashboard have different content and navigation needs. Preserve product behaviour and established identity unless there is a reason or authorisation to change them.
- Inspect the actual page and relevant states in a browser when available, alongside the code. Trace arrival, main action, feedback and return. Distinguish observed problems from stylistic preference; disclose screenshot-only or source-only limits.
- Study supplied references in use where possible. Extract the relevant hierarchy, interaction or visual principle, then adapt it to the task. Do not copy an unrelated page structure, enforce a fixed font palette or add sections simply because an external skill lists them. See [sources and adoption](references/sources.md).
- For a structural redesign, decide information order, navigation and component responsibilities before CSS polish. For a local issue, identify the smallest change that addresses it. A request to fix one wrapping label does not authorise a brand overhaul.

## Execute

### Compose around the actual content

- Give the main task and important information a clear visual order using type, contrast, alignment, spacing and useful surfaces. Use the existing design tokens or establish a coherent small set when authorised. Choose components by their purpose; do not make every section an identical card, nor remove all grouping in the name of minimalism.
- Use realistic titles, labels, paragraphs, numbers and empty/error content. Let important text wrap or reorganise before it overlaps controls. Charts need honest scales, labels, units and time ranges. Images should demonstrate or explain something, not fill an empty section.
- Match page structure to intent. A focused landing page needs a coherent promise, primary action and support for its claims; a multi-purpose homepage need not behave like a campaign landing page. An in-app task should not inherit marketing-page furniture. Do not invent social proof, savings or scarcity.
- Use space deliberately across widths: readable measures for prose, room for dense data and stable action placement. Mobile-first means a usable touch/browser layout, not blindly shrinking a desktop sidebar. Wide layouts should use space when it benefits the task.

### Use browser interaction well

- Use links for destinations and buttons for actions, with meaningful headings, landmarks, labels and native form behaviour. Preserve expected back/forward navigation, deep links, reloads and opening links in another tab. Do not use clickable containers as a substitute for accessible controls.
- Support keyboard, touch and pointer input. Keep focus visible and in a logical order, including after dialogs, validation and route transitions. Hover may enhance, but must not be the only way to discover essential content or controls. Gestures need an accessible alternative.
- Design menus and dialogs for focus management, escape/dismissal and return to the triggering control. Make validation understandable beside the affected field. Preserve entered text through recoverable errors, rather than resetting the form.
- Handle sticky headers/footers, safe areas, browser chrome and virtual keyboards without obscuring the active control or primary action. Choose a deliberate document/region scroll model; do not pile on fixed heights and nested scrollbars to make a screenshot fit.
- Pick list navigation by the task: automatic loading, explicit pages, search or filters. Keep location/shareability and footer access in mind. Loading and retry must preserve results and position; successful network responses alone do not prove a usable feed.
- Make clipboard, downloads, sharing and permission-based browser features accurately labelled and capability-aware. Inspect the actual exported artifact. An unsupported image-copy operation should not silently become a text copy with the same success message.

### Add coherent feedback and motion

- Define pressed, focus, selected, loading, empty, error and success states relevant to the task. Use motion for a real change or continuity, not to animate every paragraph on scroll. Keep content/actions available, respect reduced motion and avoid shifting targets during interaction.
- Keep processing feedback honest. No artificial waits, invented checks, fabricated percentages or celebratory claims beyond what the user accomplished. Use colour and visual accents consistently without making colour the sole signal.
- Implement the authorised change in the current stack. Preserve business rules, data, access and submission/retry behaviour. Do not deploy or publish merely because a design is complete; use the task's existing authorisation.

## Verify

- Exercise the affected journey at a narrow mobile width, a relevant desktop width and important intermediate layouts. Check long/localised content, text enlargement/reflow, supported themes and reduced motion. A single viewport screenshot is insufficient for a responsive claim.
- Use the keyboard through the changed controls and inspect focus when headers, dialogs or footers are present. Check touch behaviour in a real mobile browser when available: desktop emulation does not prove virtual-keyboard, viewport or permission behaviour.
- Inspect loading, empty, validation, failure/retry and completion where affected. Verify relevant links/routes and the final download/share output. Check semantics, labels, contrast and accessibility tooling as available; do not equate an automated scan with a complete accessibility review.
- Report the changes, actual browser/device/state evidence and limits. Use screenshots to demonstrate meaningful states. Distinguish verified implementation from hoped-for engagement, activation or conversion; those outcomes require separate data.
