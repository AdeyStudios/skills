# Contributing

Improve a workflow based on an actual need, a useful source or an observed failure. Explain the changed behaviour and keep the change proportional to the problem. See [LEARNING.md](LEARNING.md) for incorporating new material and [SKILL-FRAMEWORK.md](SKILL-FRAMEWORK.md) for the shared **Research → Execute → Verify** standard.

Each skill must be usable on its own, follow the [Agent Skills specification](https://agentskills.io/specification), and avoid private paths or dependencies on a particular AI model. Required tools and data should be described by capability.

Check that `SKILL.md` has valid YAML frontmatter, that its lowercase hyphenated name matches the directory, and that relative links resolve. Keep descriptions specific enough to distinguish neighbouring skills. Test changed scripts if adding executable helpers.

## Skill creation and use

New or substantially revised skills should make three phases clear:

1. **Research:** define the narrow job and exclusion cases; examine original evidence, real examples, failure modes and limitations before adopting a framework.
2. **Execute:** state how the agent moves from inputs to a useful authorised deliverable or decision. An execute phase does not imply a write action: a research result can be the deliverable.
3. **Verify:** inspect correctness, edge cases and the user's real task; compare with and without the skill when practical. Separate proposed changes, performed actions, tested behaviour and measured business outcomes.

For skill **creation**, also check frontmatter, cross-agent portability, references and maturity claims. For skill **execution**, check tool permissions, data freshness, cohort definitions and real-world impact. Record failed cases as well as successful examples. See [SKILL-FRAMEWORK.md](SKILL-FRAMEWORK.md) for the full standard.

## Behaviour checks

These are representative review prompts, not claims that cross-agent evaluation has already passed. Use a clean temporary project and synthetic or authorised data. Inspect the agent's reasoning and output, not exact wording.

| Skill | Example request | Useful behaviour |
| --- | --- | --- |
| seo-content-research | Recommend pages for a new invoicing app. No keyword tool or Search Console access is available. | Investigates available search results, distinguishes intent evidence from volume, and labels uncertainty without inventing demand. |
| seo-review | A useful article has a canonical pointing to the homepage. Is that an issue? | Verifies the rendered metadata and indexing intent before recommending a self-canonical; does not promise indexing. |
| design-review | Review a long mobile topic name and a hover card that pushes Save down. Preserve a light brand. | Checks wrapping and touch behaviour, avoids overlap and accidental action movement, and preserves the light theme. |
| design-review | Our account check returns instantly. Should we add a three-second security animation, make every action colourful and hide most options to improve trust? | Keeps instant results, rejects invented checks, establishes a clear primary action and evaluates whether grouping would help before removing useful choices. |
| improve-onboarding | Signup completion increased, but users still do not finish their first useful task. | Examines activation and downstream behaviour rather than treating signup as success. |
| improve-onboarding | Setup has four known steps, an optional import of unpredictable duration and a final "You're an expert!" screen before the first lesson. How should progress and success work? | Uses honest step progress, treats import duration as uncertain, acknowledges saved setup and leads into the lesson without claiming mastery or activation. |
| improve-onboarding | A language app has a useful first lesson before signup. Should we replace it with a three-screen feature tour to shorten the flow? | Evaluates the lesson's contribution to value and continuity into account creation; does not optimise screen count alone. |
| improve-onboarding | A paywall test increased purchases, but paid users return less and refunds increased. Did onboarding improve? | Weighs activation, retention, refunds and paid conversion together; does not call the purchase increase a complete success. |
| growth-economics | Spend is £600; there are 100 signups, 10 new paid customers, £80 gross profit per customer so far, and no long-term retention data. | Distinguishes £6 per signup from £60 media CAC; computes £800 observed gross profit and £200 after media spend within the stated period, qualifies cost coverage, and does not invent lifetime value. |
| founder-os | I have two products, one with cheap signups but no repeat use, the other with an interested customer but no launch. What deserves next week? | Distinguishes stage and evidence, identifies the binding constraint, recommends one focus and names the opportunity cost without inventing metrics. |
| customer-discovery | Two existing free-access users say they would only pay £0. Should we cut pricing? | Segments entitlements, excludes internal/test accounts, does not interpret already-free customers as representative prospective buyers, and proposes an eligible sampling plan. |
| idea-validation | I can build this idea in a weekend; is that enough reason to start? | Identifies the riskiest demand assumption and a falsifiable low-cost test; separates building ability, clicks, repeated use and willingness to pay. |
| founder-os (boundary) | Please implement a Stripe webhook handler. | Defers to engineering work instead of turning an implementation request into a company-wide strategy review. |

For changes to boundaries, include an adjacent request that should not trigger the skill. A payments integration implementation, for example, is different from assessing acquisition economics.

Record the agent used, inputs, observed outcome and limitations when reporting a behavioural check. Structural validation alone does not prove the workflow is effective.
