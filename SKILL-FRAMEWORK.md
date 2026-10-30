# Research → Execute → Verify

This is the common design and execution standard for **new or substantially revised** Adey Studios skills. Existing skills are working drafts and can be brought into this structure when useful; do not rewrite them just to satisfy a heading convention.

The collection exists to help people discover worthwhile problems, build useful products, acquire customers and develop sustainable businesses. The framework is a method for making each skill useful, not a claim that a skill has already been tested successfully.

## When creating or improving a skill

1. **Define one job.** Name the decision or deliverable, the conditions that trigger the skill and adjacent tasks it must *not* take over. Prefer the smallest independent workflow; a hub may route tasks but should not duplicate specialist instructions.
2. **Research.** Inspect credible sources, real-world examples, counterexamples, relevant standards and available task evidence. Record provenance, access limits, market/version/date and what is observed versus claimed. Useful inspiration is not proof.
3. **Execute.** Translate learning into explicit agent behaviour: inputs, decisions, steps, outputs, failure handling and permissions. Use the skill's `SKILL.md` for core principles and `references/` for optional depth. Design for multiple agents without requiring a particular provider's tools.
4. **Verify.** Check syntax/paths, run realistic positive and boundary examples, and when possible compare results **with versus without** the skill. Verify the *output* against task requirements and measure *real-world outcomes* after use; do not conflate these. Capture failures and revise the method.
5. **Label maturity.** A `placeholder` only reserves a topic, a `working draft` describes a proposed workflow, and a `tested workflow` requires recorded tests. Even a good test is not universal proof. Make maturity clear in the skill, README or release notes.

## When executing a skill

### Research

Establish the user's actual objective, audience, constraints, available permissions and evidence. Inspect the relevant environment if accessible. Identify what is known, inferred or missing. Seek disconfirming evidence, not just supporting examples. Use the user's existing context without requiring them to repeat known information.

### Execute

Complete the authorised task at the appropriate depth: prepare an experiment, write the draft, implement the change, run the analysis or recommend a decision. Keep scope narrow, favour reversible steps and state assumptions. A research-only request may result in a research deliverable; **execute does not imply modifying systems**. Never treat a plan or a skill as permission to spend, message people, publish, delete or deploy.

### Verify

Inspect the output and affected path, including important errors and edge cases, with appropriate tests or authorised evidence. Then specify how the user will know whether the work improved customer or business outcomes. Separate **proposed**, **implemented**, **tested** and **measured**. When outcomes need time or data not yet available, say so and define the next check.

## What every skill should preserve

- **One clear job:** narrow triggers, exclusions and boundaries; general skills are not automatically superior to focused ones.
- **Evidence before frameworks:** use evidence to decide whether a principle applies; a sourced percentage, anecdote or benchmark is not a universal target.
- **Test against actual work:** examples should include a realistic success case and a neighbouring case where the skill should defer.
- **Compounding learning:** keep a short trace of lessons, failures, conditions and decisions, following [LEARNING.md](LEARNING.md); prune obsolete guidance.
- **Safety and portability:** use only authorised data, protect privacy, keep public skills generic, and disclose when tools or sources are missing.

For contribution checks and representative prompts, see [CONTRIBUTING.md](CONTRIBUTING.md).
