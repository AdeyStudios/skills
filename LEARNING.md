# Learning into better skills

The collection should improve as we learn. A video, article, named concept, experiment or product observation is input for a discussion, not an automatic new rule.

Follow the shared [Research → Execute → Verify standard](SKILL-FRAMEWORK.md) when turning a useful lesson into a workflow. A skill update that passes a format check is not automatically verified as improving real work.

## Working together

1. Bring the source or data and identify what caught your attention. A link, timestamp, excerpt or named concept is useful; a full transcript is not required.
2. Read or watch the available material. If only an excerpt or transcript is accessible, say so rather than claiming to have watched the video.
3. Explain the idea together in plain language. Separate the source's claim, the evidence provided, our interpretation and the preference we want to adopt.
4. Decide where it applies and where it would fail. A style preference is valid as a preference; a causal or numerical claim needs supporting evidence. One successful project does not establish a universal rule.
5. Propose the smallest concrete change to the relevant skill. Explain what the agent would do differently. We can keep, qualify, test, defer or reject it.
6. Once agreed, update the skill and check a realistic request. Record the source and decision when they explain the instruction; avoid accumulating a transcript archive in the skill.

If the user explicitly requests a particular update, implement that scope without asking for the same approval again. Do not silently incorporate unrelated ideas from the same source.

## Keeping instructions useful

- Put broadly useful judgment in `SKILL.md`.
- Use a skill's `references/` folder for substantial supporting material needed only in some tasks, with a clear link explaining when to read it.
- Keep project-specific preferences and raw private data in their own projects.
- Include links, short attributed notes and original synthesis rather than copying entire videos or articles.
- Revise or remove weak instructions when experience contradicts them.

## A useful proposal

```text
Source: URL, title, date accessed, relevant timestamp or supplied excerpt
Idea: What we think is useful
Basis: Evidence, hypothesis or preference
Applies when: The tasks or conditions this helps
Proposed change: The exact instruction to add, replace or remove
Check: A realistic request and the behaviour we expect
Decision: Adopt, qualify, test, defer or reject, with a brief reason
```

This format is optional. The purpose is to make the reasoning reviewable, not to add process to every small edit.

## Design skill split, 31 October 2026

**Decision:** the user requested separate web and mobile guidance after preferring a native redesign that went beyond a document-like presentation. Added independently usable `web-design` and `mobile-design`; updated `design-review` as the shared review for mixed or unspecified platforms. Mobile websites/PWAs remain browser work. All three are working drafts.

**Adopted lesson:** choose the depth of the intervention explicitly. An authorised restructure can revisit navigation, screen responsibilities and input patterns; a wrapping correction should remain local. Clarity can include visual identity, useful surfaces, native components and purposeful feedback. Preserve functionality and access/retry semantics without freezing a layout the user asked to replace.

**Conditional, not universal:** the mobile workflow considers keyboard, gestures, state restoration, motion and relevant device capabilities. It does not require voice, cards, infinite scrolling or a particular tab arrangement in every app. Web guidance keeps browser semantics, focus, history, responsive reflow and keyboard/pointer/touch use. Source prescriptions about fonts, colours, CSS or animation timings were not imported as universal rules. The source-specific rationale is in each new skill's `references/sources.md`.

**Initial checks performed by the authoring agent:**

- Applied `web-design` to a temporary synthetic long-label/Save fixture in Chrome. Reproduced horizontal overflow at 320 CSS pixels, then made a local grid/wrapping correction without changing its font, colours or content. Checked 320, 640 and 1280 pixel widths at 100% and 200% root text size: no horizontal overflow, full label, no overlap and a visible Save action. Tab reached Save with a visible focus outline; inspected the resulting narrow large-text render. This was text enlargement, not a claim of full browser-zoom or WCAG conformance testing.
- Applied the mobile review to existing native Topics light/large-text renders and Topics/voice source. Confirmed that topic discovery, selected settings and saving have distinct responsibilities; large text uses a single column and a full-width footer; permission denial retains a typed fallback; recognition callbacks have session guards. This was a screenshot/source review, not a fresh native end-to-end or physical-device test. Earlier app acceptance checks motivated the skill but do not retrospectively validate it.
- Walked through the boundary prompts in CONTRIBUTING.md: a PWA uses web guidance, a narrow layout correction keeps its scope, a native restructure can change screen architecture, a feed's task determines pagination, and Android tab history requires checking implementation/current multiple-stack support rather than a blanket prohibition. These are author self-checks, not independent agent evaluations.
- Validated all three changed skills' YAML/frontmatter and local references. The repository's eight existing metadata/installer tests pass. They check packaging and structure, not the quality of design decisions.

**Limit:** there has been no independent cross-agent or with/without-skill comparison. The founder's approval concerns the preceding combined redesign, not a measured retention or conversion effect of these new skills. Next evaluation should use unseen native and browser tasks in another agent, compare the resulting decisions and inspect the actual task completion; revise the smallest rule that demonstrably fails.
