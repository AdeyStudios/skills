# Recurring marketing run contract

Use when designing, reviewing or implementing an actual recurring job. The contract may be a concise project document or structured configuration; no scheduler is assumed.

## Job and access

Define the project, one outcome, responsible owner, cadence/trigger and timezone. Identify the exact runner and where its model credentials, data connections and repository permissions come from. Verify a harmless read of each essential input from that runner when authorised. Do not assume an installed interactive connector is inherited by a scheduled process.

Distinguish read/recommend, local draft, PR creation, publication, spending and external messaging. Carry existing task authorisation forward, but do not let a broad job description grant new permissions. Keep keys and private customer data outside public skill files and logs.

## Inputs and decisions

Record source/property, query scope, market, time window, freshness requirement, exclusions and expected stage counts. Decide what missing access, partial responses and genuine empty results mean. Cache or retain source responses only within authorised storage and retention limits.

State when the job should act, skip, investigate or stop. Define what the job remembers: source snapshot, prior decision, completed items, cooldown and pending work. Match cadence to the evidence rather than a desired output quota. Lack of a new finding is a valid successful outcome.

## Reliability and missed runs

Choose and verify a policy for a missed period: skip, run once after wake/recovery, or bounded backfill. Specify how stale queued work expires. A laptop runner requires the machine and its dependencies to be available; naming a daily time does not prove catch-up exists.

Use an execution key such as project + job + scheduled period, and a lock/lease appropriate to the runner. Check completed side effects before retrying a resumed task. Distinguish an accepted API request from a completed publish or delivered notification; keep enough state to reconcile an uncertain acknowledgement instead of blindly sending again.

Set bounded retries/backoff for transient failures. Expired login, invalid schema, quota exhaustion, unexpected scope or excessive cost should produce an actionable blocked result through an authorised channel, not an infinite model loop. Set model/CPU/concurrency and retrieval limits proportionate to the workload. Do not download or run local models merely because a workflow needs an LLM.

## Outputs and review

Define the output location and format, evidence links, what changed, costs, unresolved gaps and next decision. Define notification conditions and authorised destination. Avoid repeating a notification for the same unresolved failure; record acknowledgement and escalation separately. If replies can trigger work, validate sender, intended job and permitted action rather than executing arbitrary text.

Before enabling a job, check a dry run, no-change case, dependency failure, partial data and interrupted/repeated execution. Verify the scheduler's actual configuration and timezone. Report configured, enabled, successfully run and externally verified outcomes separately.

A request to prepare this contract is not permission to install or enable a schedule.
