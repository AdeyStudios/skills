# Contributing

Improve a workflow based on an actual need, a useful source or an observed failure. Explain the changed behaviour and keep the change proportional to the problem. See [LEARNING.md](LEARNING.md) for incorporating new material.

Each skill must be usable on its own, follow the [Agent Skills specification](https://agentskills.io/specification), and avoid private paths or dependencies on a particular AI model. Required tools and data should be described by capability.

Check that `SKILL.md` has valid YAML frontmatter, that its lowercase hyphenated name matches the directory, and that relative links resolve. Keep descriptions specific enough to distinguish neighbouring skills. Test changed scripts if adding executable helpers.

## Behaviour checks

These are representative review prompts, not claims that cross-agent evaluation has already passed. Use a clean temporary project and synthetic or authorised data. Inspect the agent's reasoning and output, not exact wording.

| Skill | Example request | Useful behaviour |
| --- | --- | --- |
| seo-content-research | Recommend pages for a new invoicing app. No keyword tool or Search Console access is available. | Investigates available search results, distinguishes intent evidence from volume, and labels uncertainty without inventing demand. |
| seo-review | A useful article has a canonical pointing to the homepage. Is that an issue? | Verifies the rendered metadata and indexing intent before recommending a self-canonical; does not promise indexing. |
| design-review | Review a long mobile topic name and a hover card that pushes Save down. Preserve a light brand. | Checks wrapping and touch behaviour, avoids overlap and accidental action movement, and preserves the light theme. |
| improve-onboarding | Signup completion increased, but users still do not finish their first useful task. | Examines activation and downstream behaviour rather than treating signup as success. |
| growth-economics | Spend is £600; there are 100 signups, 10 new paid customers, £80 gross profit per customer so far, and no long-term retention data. | Distinguishes £6 per signup from £60 media CAC; computes £800 observed gross profit and £200 after media spend within the stated period, qualifies cost coverage, and does not invent lifetime value. |

For changes to boundaries, include an adjacent request that should not trigger the skill. A payments integration implementation, for example, is different from assessing acquisition economics.

Record the agent used, inputs, observed outcome and limitations when reporting a behavioural check. Structural validation alone does not prove the workflow is effective.
