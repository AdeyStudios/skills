---
name: growth-economics
description: Assess whether product growth can be profitable using advertising spend, acquisition costs, funnel conversion, pricing, margins, retention and payback. Use for CAC, ROAS, LTV and growth sustainability analysis or experiment planning; not for implementing payment integrations or changing live ad campaigns.
license: MIT
---

# Growth economics

Connect acquisition to retained customers and contribution profit. Cheap clicks, more signups and revenue growth do not establish a sustainable business.

## Establish the decision and data

Clarify whether the user is choosing a channel, diagnosing a funnel, evaluating pricing or deciding whether to scale. Use supplied exports and authorised analytics or advertising tools; do not assume any particular connector is available.

Record the period, currency, market, channel, customer definition, attribution method and cohort. Distinguish new customers from renewals and reactivations. Check whether spend includes production, agency and sales costs, whether revenue is gross or net, and how refunds, tax and discounts are treated. Do not expose raw customer records in a public report.

Missing retention, margin or conversion information is a limit to the conclusion, not permission to invent it. Continue with a useful partial model and identify the next piece of evidence that could change the decision.

## Join the funnel to the economics

Follow the actual business journey, for example impressions, visits, signups, activation, first payment and retained payment. Use meaningful denominators and consistent populations. A product may not have every one of these steps.

Use the applicable calculations, stating the units and cost scope:

- **Stage conversion:** people completing the next stage divided by eligible people entering the stage, within a defined conversion window.
- **Media CAC:** attributable advertising spend divided by new paying customers attributed to that spend. Cost per signup is not paying-customer CAC.
- **Fully loaded CAC:** defined acquisition costs divided by new paying customers acquired. Document included costs rather than presenting it as interchangeable with media CAC.
- **Observed contribution per customer:** revenue net of discounts, refunds and applicable sales taxes, less consistently defined variable delivery costs, divided by the cohort's customers. Include relevant payment fees, AI or infrastructure usage, fulfilment and variable support. Avoid subtracting the same cost twice.
- **Cohort contribution after acquisition:** total observed cohort contribution less the acquisition costs assigned to it. This is not company net profit; fixed costs and other excluded costs remain to be covered.
- **ROAS:** attributed revenue divided by ad spend. State gross or net revenue and the attribution window. ROAS is not a profit measure and attribution is not proof of causation.
- **CAC payback:** the earliest point where cumulative cohort contribution before acquisition cost covers that cohort's CAC. Use observed timing when possible. CAC divided by stable monthly contribution is only a rough approximation.

Distinguish revenue LTV from contribution LTV. For subscriptions, contribution LTV based on average revenue times margin divided by churn is only a rough steady-state model: it assumes consistent definitions, time units and relatively stable retention and economics. Do not apply it blindly to young cohorts, annual billing, changing churn or non-subscription purchases. Prefer observed cohort cash flows plus an explicit, bounded forecast. Report the observation window and unobserved tail.

Use consistent gross-profit or contribution definitions when comparing models. Label uncollected projected revenue, recognised revenue and cash receipts separately where the difference matters.

## Interpret before recommending scale

- Compare acquisition cohorts and retained value by channel, device, market or offer only when samples and tracking support the comparison. Keep attribution uncertainty and overlapping conversion windows visible.
- Look for the binding constraint: acquisition price, message mismatch, activation, payment conversion, retention, delivery cost or insufficient demand. Improving the wrong step can inflate activity without improving profit.
- Distinguish marginal from average CAC. A profitable small test does not prove a larger budget will retain the same audience quality or acquisition cost.
- Assess cash timing, refunds and the ability to fund payback. A positive lifetime forecast may still require unaffordable working capital.
- For uncertain inputs, show transparent downside, central and upside scenarios. State where assumptions come from and which one controls the conclusion. Do not present generic CAC:LTV or payback benchmarks as universal pass/fail rules.
- Treat experiments, holdouts or other credible causal evidence as stronger evidence of incremental acquisition than platform-reported attribution alone. Do not infer incremental conversions simply by summing platforms.

## Deliver a usable decision

Lead with what the evidence supports: profitable so far within the measured period, unprofitable at current economics, promising but immature, or insufficiently measured. Give the key calculations, included costs and missing evidence so the conclusion can be checked.

Recommend a small number of changes or tests with a hypothesis, primary outcome, relevant guardrails and a decision rule. Define a test budget or ceiling only as a proposal unless already authorised. Avoid declaring a winner from a tiny sample or choosing a duration that cannot capture the conversion and retention window.

Use supplied data for arithmetic. Verify current platform rules, prices or market claims with authoritative sources if they affect the recommendation. Keep assumptions distinct from facts. This skill supplies analysis; it does not authorise spending money, changing prices, publishing ads or modifying payment systems.
