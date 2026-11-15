---
name: conversion-retention
description: Diagnose and improve the journey from discovery or store listing through signup, activation, payment and useful repeat use. Use for conversion and retention decisions, with store optimisation as a mode rather than a substitute for product value.
license: MIT
---

# Conversion and retention

Working draft. Guidance has not yet demonstrated improved business outcomes.

Find the next obstacle between a relevant visitor and repeated customer value. Conversion is a meaningful next action; retention is returning to receive value, not opening notifications.

## Research

Select the actual surface and decision: listing-to-install, landing-to-trial, signup-to-value, trial-to-payment or useful repeated use. Establish the intended outcome, product rhythm, traffic source, platform, current deployment and relevant segments. Read existing journey and measurement definitions.

Check instrumentation before interpreting a drop. Consent changes, event renaming, identity joins, missing server events, delayed ingestion and self-deleted accounts can change measured counts. Keep visitors, sessions, people, events and transactions distinct. Inspect actual current screens and representative error states where possible.

## Execute

- Trace the relevant journey through its first useful result. Locate mismatches between the source promise, page, effort requested and delivered value. Distinguish a usability bug, weak explanation, unsuitable audience, pricing objection and insufficient product value before proposing a redesign.
- Prioritise a small, observable improvement. Support the customer's desired outcome with truthful proof and clear choices. Do not invent urgency, social proof, hidden fees or obstructive cancellation. A signup increase that worsens activation or refunds is not an unqualified win.
- For store listings, use [the store review mode](references/store-listings.md). Treat screenshot/title work as acquisition work and check downstream activation separately.
- For retention, define the value-bearing action and the expected return opportunity. Use cohorts old enough to have reached the checkpoint; distinguish paid renewal, cancellation, voluntary inactivity and payment failure. Do not call a cohort that has not reached day seven churned.
- Describe each experiment as a mechanism, eligible audience, proposed change, outcome, counter-metric and decision condition. Use randomised comparisons when feasible. With sparse data, combine observed task failures and qualitative evidence with explicitly uncertain outcomes rather than declaring significance.
- Implement only within the requested scope. A specialist design, onboarding or copywriting skill may help when available, but none is required to understand this workflow.

## Verify

Test the actual changed route and relevant narrow/wide layouts, keyboard, long content, loading, error/retry and recovery states. For measurement, check event definitions, denominators, deployment date and observation window. Compare like cohorts; a before/after difference alone is not causation. Give the current result, uncertainty and next review condition.

Do not launch store experiments, change prices, send lifecycle messages or alter tracking merely because a review recommends them. Maintain the task's existing authorisation. See [source decisions](references/sources.md).
