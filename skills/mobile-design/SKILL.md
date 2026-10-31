---
name: mobile-design
description: Design, review or restructure native iOS and Android app screens and journeys, including platform components, navigation, touch, keyboard, device capabilities, motion and accessible states. Use for native mobile experiences; mobile websites and PWAs belong to web design.
license: MIT
---

# Mobile design

Working draft. Build a product that belongs on the device, with its own identity and clear content. Simplicity is not a ban on colour, surfaces, animation or native components. A native app should offer more than a website compressed into a phone.

## Research

- Establish the main task, audience, target OS/framework, supported versions and device sizes. Inspect the implementation and actual screens if available. A screenshot can show hierarchy; it cannot establish keyboard, gesture, audio or lifecycle behaviour.
- Determine the authorised depth: review, focused correction or structural redesign. Preserve working behaviour and the brand. When the user explicitly wants a rethink, question navigation, screen responsibilities and interaction patterns before polishing existing rows. Do not mistake preserving functionality for preserving every layout.
- Trace a complete task: arrival, input, processing, useful result and return. Identify what belongs on the main screen, in a detail view, in a contextual sheet or in account settings. Separate concerns when it improves the task; do not automatically add tabs, cards or screens.
- Inspect relevant native apps or a supplied reference in use. Record what helps, such as direct manipulation or a recognisable central task, and what does not transfer. Translate its principle into this product rather than copying its colour scheme or unrelated features.
- Check current official platform guidance and actual SDK availability for consequential choices. iOS and Android can share an identity while using different controls, back behaviour and presentation. Third-party skill recipes are references, not platform requirements. See [sources and adoption](references/sources.md) for the basis of this workflow.

## Execute

### Give the task a native structure

- Prefer suitable platform navigation, lists, pickers, sheets, menus and share controls. Choose them by function, not by a component quota. A custom alternative should solve a concrete need and retain accessibility, expected back behaviour and state restoration.
- Make top-level destinations, task detail and contextual actions distinguishable. Keep back/edge gestures and Android system back working. Preserve the user's place and unfinished input across relevant tab, sheet and detail transitions.
- Establish a recognisable main object or action: a question, transaction, document or other product-specific task. Use hierarchy, meaningful icons, colour and surfaces to show relationships and state. Avoid both an undifferentiated text wall and a grid of decorative cards.
- Keep typography and spacing coherent. Respect system text scaling, localisation, light/dark behaviour and accessible contrast. Let essential content wrap and rearrange; decorative symbols must not outgrow their containers at large text sizes. Colour must not carry meaning alone.

### Design input and navigation together

- Treat the keyboard as part of the layout. Keep input, relevant context and the action reachable without trapping the user. Use expected submission/dismissal behaviour for the field: a multiline editor must still allow newlines. Consider drag or background-tap dismissal where natural, without intercepting links, text selection or scrolling. Do not force an extra Done step when the task does not need it.
- Reserve actual layout space for navigation, composers, safe areas and device insets. Avoid stacking duplicate system/custom bars or hiding usable content behind floating chrome. Decide which region scrolls; nested independent scrolling is a deliberate choice, not an accidental result of fixed heights.
- Choose pagination for the task. A chronological feed can load more as it approaches the end; a record browser may need explicit pages, search or filters. Preserve position, deduplicate results and retain loaded content on failure. A loading sentinel disappearing must not cancel its own request. Provide recovery and an honest end state.
- Consider voice, camera, sharing or other device capabilities when they materially improve the task. They are options, not requirements for every app. Ask permission at the relevant action, explain the benefit and provide a useful denied/unavailable path. Do not start recording simply because a screen appeared.
- For voice input, make listening and stop states explicit, preserve editable words and typed prefixes, and avoid duplicate partial transcripts. Bind late callbacks to the initiating user/task/session; stop on navigation, interruption and backgrounding as appropriate. Handle permission dialogs without accidentally cancelling setup. Keep input recoverable on errors; speech recognition does not imply automatic submission. Distinguish local processing from a service receiving audio.

### Make the experience responsive and expressive

- Give actions immediate, legible feedback. Use system motion first; add brief transitions for a real selection, insertion, expansion or completion when helpful. State what changes and why it moves. Do not add entrance effects to every row or delay an available result to imply work.
- Keep motion interruptible and respect reduced-motion settings. Use haptics or sound selectively, with platform/user preferences and a visible equivalent. Simulator success cannot prove the physical feedback feels right.
- Design loading, empty, offline, denied-permission, error and completion states relevant to the task. Keep drafts and prior results through recoverable failure. Completion should reveal the actual useful result and next action; progress must represent real work.
- Implement only the authorised scope. Preserve access rules, saved data and request/retry semantics while changing presentation. A more attractive UI must not introduce duplicate submissions or silently save unfinished settings.

## Verify

- Exercise the affected task in a running app or simulator when available, including keyboard open/closed, back/sheet/tab transitions, long content and failure/retry. Inspect rendered screens as well as layout bounds; a control can be technically tappable while its background or icon is visibly broken.
- Check compact and large layouts relevant to the supported devices, large system text, reduced motion, supported themes and accessibility labels/order. Use VoiceOver or TalkBack where available and report when that check was not performed. Check API availability against the supported SDK/OS range.
- Use synthetic fixtures for destructive, paid or personal-data scenarios. Separate fixture UI results from real service integration. Physical microphone quality, haptics, audio interruptions and device performance need device evidence; list what remains untested.
- Report the structural decisions, relevant before/after states, what was actually exercised and remaining limits. Build success and user preference are useful evidence, but do not establish retention or conversion gains. Keep project screenshots and acceptance results with the project.
