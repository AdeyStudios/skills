# Adey Studios Skills

A reusable system for discovering worthwhile problems, building useful products, acquiring customers and turning them into sustainable businesses. Built in public by Adey Studios and refined through real work and learning.

These are initial working drafts, not proven methodologies. They use the open [Agent Skills format](https://agentskills.io/specification). The same skill files can be used by compatible agents, including Claude Code and Codex. Each host supplies its own tools, permissions and invocation syntax.

## The skill hub

`founder-os` is the small decision hub: identify a venture's current constraint and choose the right work to do next. Specialist skills stay independently usable. Do not interpret the hub as a requirement to install or run every other skill.

## Skills

These are **working drafts**, not proven methodologies. "Placeholder" means there is no substantive workflow to rely on yet.

| Skill | Use it to | Maturity |
| --- | --- | --- |
| [founder-os](skills/founder-os/SKILL.md) | Decide what to focus on across one or more ventures and route the next task to the right specialist. | Working draft |
| [customer-discovery](skills/customer-discovery/SKILL.md) | Learn about real customers' problems, alternatives and behaviours from interviews, surveys, reviews and observation. | Working draft |
| [idea-validation](skills/idea-validation/SKILL.md) | Pressure-test a new venture or product idea with the smallest decision-changing experiment. | Working draft |
| [go-to-market](skills/go-to-market/SKILL.md) | Future work on positioning, channels and reaching the right customers. | Placeholder |
| [seo-content-research](skills/seo-content-research/SKILL.md) | Choose useful content opportunities using search intent, existing answers and product fit. | Working draft |
| [seo-review](skills/seo-review/SKILL.md) | Diagnose discoverability and indexing problems with evidence and prioritised fixes. | Working draft |
| [design-review](skills/design-review/SKILL.md) | Review a screen or journey for clear hierarchy, useful content, consistent interactions and responsive behaviour. | Working draft |
| [improve-onboarding](skills/improve-onboarding/SKILL.md) | Help new users reach the product's first useful outcome with less friction. | Working draft |
| [growth-economics](skills/growth-economics/SKILL.md) | Assess acquisition, advertising, conversion, retention, CAC and contribution profit together. | Working draft |

## The shared method: Research → Execute → Verify

**When creating a skill:** research real problems, trustworthy sources and counterexamples; turn that knowledge into one focused agent workflow; verify the skill on realistic tasks and revise it based on failures.

**When using a skill:** inspect context and available evidence; complete the *authorised* work (which may be an analysis rather than a code change); verify the actual output and, separately, check real-world results when they become measurable.

See [SKILL-FRAMEWORK.md](SKILL-FRAMEWORK.md) for the creation and execution standard and [CONTRIBUTING.md](CONTRIBUTING.md) for behaviour checks. New skills should follow this pattern; existing drafts can be updated incrementally rather than rewritten for formatting.

## Install

Install all nine globally for Claude Code and Codex, without selection menus:

```sh
npx -y github:AdeyStudios/skills
```

Requires Node.js 22.20+ and network access. Start a new agent session afterwards. Repeat this command to refresh the installed skills from the current GitHub collection.

The proposed npm name `@adeystudios/skills` is **not published yet**. Until it is published and verified, use the GitHub command above.

The installer delegates to the existing [skills CLI](https://github.com/vercel-labs/skills), pinned to 1.7.4. You can also use that CLI directly to choose different agents or an installation scope:

```sh
npx skills add AdeyStudios/skills
```

Choose an individual skill:

```sh
npx skills add AdeyStudios/skills --skill design-review
```

You can also copy an individual skill folder into the skills directory supported by your agent. Cloning this repository alone does not install its skills. The shortcut is optional; the skill files require no paid service or particular model. Research and analytics tasks need the appropriate data or tools.

## Use

After installation, invoke a skill using your agent's supported syntax. For example, in Codex:

```text
$design-review Review this checkout on mobile. Preserve the existing brand.
$seo-content-research Find content opportunities for this product using the attached Search Console export.
$growth-economics Assess whether this paid acquisition cohort is profitable. Here are spend, conversion and retention data.
```

Skills are generic. Supply project context in the request or keep it in that project's own documentation: audience, useful outcome, positioning, constraints and available evidence. They should not assume any particular Adey Studios product or private account.

## Improve them as we learn

Videos, articles, observations and product data can inform revisions. We discuss the useful idea, its evidence and where it applies before turning it into an instruction. See [LEARNING.md](LEARNING.md).

For contributions and practical review examples, see [CONTRIBUTING.md](CONTRIBUTING.md). Contributions should preserve cross-agent portability and contain no private customer data or credentials.

## Public skill collections for inspiration

Research these on your own terms; they are references, not automatically adopted instructions or endorsements. Check provenance, licensing and whether a practice holds up for your use case before importing it.

| Collection | Worth studying for |
| --- | --- |
| [Appllama / appllama-skills](https://github.com/Appllama/appllama-skills) | Research real product flows → implement → verify in a simulator, with a clear quality bar. |
| [Startup Skills / samuelcastro](https://github.com/samuelcastro/startup-skills) | Founder playbook, stage-dependent decisions and routing to specialist skills. |
| [Startup Founder Skills / shawnpang](https://github.com/shawnpang/startup-founder-skills) | Broad founder responsibilities and shared startup context. |
| [Growth Skills / JaredYin](https://github.com/JaredYin/growth-skills) | Deep specialist workflows for discovery, experiments, retention, monetisation and operating reviews. |
| [Marketing Skills / coreyhaines31](https://github.com/coreyhaines31/marketingskills) | Practical marketing, conversion and distribution playbooks. |

## Possible future skills (not yet added)

These are ideas to revisit as actual ventures create a need, **not** an implementation commitment: `founder-sales`, `product-strategy`, `business-finance`, `legal-and-risk`, `hiring-and-delegation` and `portfolio-capital-allocation`. Avoid expanding the library merely to increase the skill count.

## Licence

MIT. See [LICENSE](LICENSE). External sources retain their own licences; linking to a source does not relicense its content.
