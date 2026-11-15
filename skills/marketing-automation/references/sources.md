# Source decisions

Reviewed 15 November 2026.

- [Treg GTM playbook, operations chapters](https://treg.to/gtm-engineering): bounded costs, evidence lineage, staged rollout and noticing silently incomplete retrieval.
- [Marketing loops](https://github.com/coreyhaines31/marketingskills/tree/main/skills/marketing-loops): recurring work should distinguish checking a condition from taking an action and carry state between runs.
- [Swan GTM Skills](https://github.com/swan-gtm/gtm-skills): reference for portable decision guidance with an optional execution layer. We have not run or validated every skill in that collection.

We developed the run contract around runner-specific access, missed schedules, idempotency, evidence freshness and outcome verification. No fixed upstream spend threshold, vendor integration, cron setting or messaging channel is required. Daily output quotas and perpetual model retries were not adopted.

Skill creation installs a method only. It does not start a runner, register a job or grant access to another agent's tools.
