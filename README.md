# Adey Studios Skills

Reusable workflows for researching, designing and growing products. Built in public by Adey Studios and refined through real work and learning.

These are initial working drafts, not proven methodologies. They use the open [Agent Skills format](https://agentskills.io/specification). The same skill files can be used by compatible agents, including Claude Code and Codex. Each host supplies its own tools, permissions and invocation syntax.

## Skills

| Skill | Use it to |
| --- | --- |
| [seo-content-research](skills/seo-content-research/SKILL.md) | Choose useful content opportunities using search intent, existing answers and product fit. |
| [seo-review](skills/seo-review/SKILL.md) | Diagnose discoverability and indexing problems with evidence and prioritised fixes. |
| [design-review](skills/design-review/SKILL.md) | Review a screen or journey for clear hierarchy, useful content, consistent interactions and responsive behaviour. |
| [improve-onboarding](skills/improve-onboarding/SKILL.md) | Help new users reach the product's first useful outcome with less friction. |
| [growth-economics](skills/growth-economics/SKILL.md) | Assess acquisition, advertising, conversion, retention, CAC and contribution profit together. |

## Install

With the optional [skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add AdeyStudios/skills
```

Choose an individual skill:

```sh
npx skills add AdeyStudios/skills --skill design-review
```

You can also copy an individual skill folder into the skills directory supported by your agent. Cloning this repository alone does not install its skills. No custom installer, paid service or particular model is required by these instruction files; research and analytics tasks need the appropriate data or tools.

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

## Licence

MIT. See [LICENSE](LICENSE). External sources retain their own licences; linking to a source does not relicense its content.
