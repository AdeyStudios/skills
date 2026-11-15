---
name: marketing-automation
description: Design, review or implement explicitly authorised recurring marketing research and monitoring jobs with state, verification, budgets and recovery. Use for scheduled agent workflows, not as permission to schedule or publish every available marketing skill.
license: MIT
---

# Marketing automation

Working draft. Guidance has not yet demonstrated improved business outcomes.

Make recurring marketing work dependable. A skill describes a method; the runner, data connections, model and permissions are separate capabilities.

## Research

Identify the outcome, trigger, project, existing jobs and the action the user actually authorises. Read [the run contract](references/run-contract.md) before designing or changing a recurring job. Inspect available runner capabilities rather than assuming a specific scheduler or chat integration.

Verify access in the runner that will execute the job. An interactive agent's Search Console, analytics or GitHub connection does not automatically exist in a separate process. Distinguish missing data, missing credentials, expired model login, no fresh evidence and a genuine empty result. Never print tokens while checking access.

## Execute

- Choose one bounded recurring task and a cadence suited to the data. A job may inspect daily while only acting when a condition is met. Do not infer an obligation to generate content, PRs or alerts on every run.
- Describe inputs, retrieval limits, authorised costs, decisions, state, verification, output and stop conditions. Let the runner load only the methods needed for that job; this skill does not require a particular vendor or other skills to be installed.
- Preserve a source/evidence snapshot and prior decisions in the project's permitted records. Use stable job/period identifiers, a concurrency lock or equivalent, and a checkpoint for completed side effects. Retry temporary failures within a bounded limit; do not replay a completed publish or send.
- Define what happens when the machine sleeps, the model cannot authenticate or a provider quota is exhausted. Catch-up, skip and backfill are explicit policies, not assumptions about the scheduler. Avoid overlapping backfills or a burst of duplicate work.
- Stage drafts or recommendations by default unless the task already authorises publication. Send notifications only through an authorised destination, with enough context for an actionable reply. A chat message is not automatically a validated command to execute arbitrary code.
- If asked to implement, verify the concrete configuration and run a bounded dry run before enabling the schedule. If the user wants discussion only, deliver the run specification and leave the scheduler unchanged.

## Verify

Test success, no-change, missing access, malformed data, duplicate/restarted runs and the runner's real missed-run behaviour. Monitor evidence freshness, stage counts and completion markers as well as errors: a process can exit successfully after collecting nothing useful. Verify delivery and acknowledgement when required, without claiming a notification was received merely because an API accepted it.

Report the exact active jobs, verified access and unresolved dependencies. Separate configuration, dry-run success and measured marketing impact. See [source decisions](references/sources.md).
