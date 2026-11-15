---
name: seo-review
description: Review a site's organic discoverability, indexing signals, metadata, internal links and page usefulness. Use for evidence-based SEO audits and prioritised fixes to existing pages; use a content research workflow when the main task is choosing new articles.
license: MIT
---

# SEO review

Produce a prioritised, evidence-backed account of what prevents useful public content from reaching relevant visitors. Distinguish verified defects, useful improvements and hypotheses. This is a working draft, not a proven traffic-growth system.

For a comprehensive audit, read [the audit procedure](references/site-audit.md). For a narrow issue, inspect only the relevant surfaces. Do not inflate a focused request into a full audit.

## Understand the site

Identify intended public pages, private or authenticated routes, important user journeys and the business goal. Inspect available code and live pages, plus authorised search analytics if available. Do not assume every URL should be indexed.

Verify the requested domain resolves and matches the intended product and analytics property. Record the market, language, observation date, deployment and data window. Resolve meaningful target mismatches before auditing a different business.

Choose representative pages from relevant templates rather than checking only the homepage. When possible, verify the deployed response as well as source code; a local change is not evidence that production is fixed.

Read prior audits and change history before making a backlog. Treat supplied reports as dated evidence, not fresh crawl results. Separate open, resolved, in-progress and superseded findings; do not reopen work merely because an old PDF mentions it.

## Check the evidence

- Verify response codes, redirect chains and accidental access restrictions. Inspect robots directives, `noindex`, canonical targets and XML sitemap coverage for pages intended to be indexed.
- Check meaningful, distinct titles and descriptions. A practice page can have a concise descriptive search title while retaining its full question in the content.
- Inspect crawlable internal links, useful anchor text, orphaned pages and hierarchy. Avoid self-links or navigation that adds steps without helping a visitor. Educational discovery links should support the product's intended primary journey.
- Review whether the page satisfies its apparent search intent. Check duplicate or thin material, misleading promises, actual explanations and useful examples. More words or more structured data are not automatically better.
- Check relevant rendered content, mobile usability and loading problems. Use field performance data when available and identify lab measurements as lab measurements.
- Review structured data only when it represents visible, supported content and an appropriate type. Check applicable official guidance before recommending search features.

Separate crawlability, indexing eligibility and actual indexing. A valid sitemap submission does not prove its URLs are indexed. Missing analytics access should be disclosed rather than replaced by guessed traffic or rankings.

### Use search data correctly

Prefer authorised Search Console evidence for the selected property and search type. Use the available history to understand the site's age, then compare equivalent windows with compatible data freshness, filters and dimensions. Record incomplete dates and recently published pages before interpreting changes.

Keep property totals, query rows, page rows, index coverage and sitemap reports distinct. Anonymised queries and grouping rules mean their totals need not reconcile. Do not sum or average CTR or average-position rows to recreate property totals. Do not call clicks conversions.

Inspect brand/non-brand, page templates, country and device segments where useful. Join query and page dimensions before attributing a query's performance to a particular URL. Multiple exposed URLs alone do not prove harmful cannibalisation. Sparse impressions, zero clicks or a single average position justify investigation, not a causal diagnosis or automatic rewrite.

Reconcile conflicting evidence explicitly. A `site:` search is an incomplete hint; it does not override authoritative property or URL-level evidence. Aggregate coverage reasons cannot identify the affected URLs without a URL list or inspection.

### Connect the audit to useful discovery

Check the live pages supporting important audience questions, not only global metadata. Identify whether a problem is an access/indexing defect, an inadequate answer or an unverified demand assumption. Hand off new-topic selection to content research when available; a technical audit should not create articles merely because a competitor has them.

AI citation-readiness suggestions must be labelled separately from observed AI visibility. Check current official search guidance before recommending special files, schema or crawler changes. A heuristic score is not evidence of search inclusion or a traffic forecast.

The [source decisions](references/marketing-sources.md) distinguish the playbook's linked SEO collection from the existing audit procedure.

## Report what matters

Lead with the most consequential verified problem. For each material finding, give the affected URL or code location, evidence and date, observed behaviour, implication, confidence, concrete fix or next check, effort and verification. Prioritise user-journey failures and verified eligibility problems before speculative copy changes or cosmetic scores. Consider reach, likely value and implementation risk; do not manufacture numerical precision.

Produce a persistent report in the user's requested format when available, with a short executive summary, prioritised findings, relevant data and a small actionable next-step list. An audit does not require a particular canvas product, a long checklist, a keyword subscription or a quota of content ideas. Include what already works so later agents preserve it. Keep the chat response short and link the report.

Use current official search-engine guidance for claims about indexing and supported features. Do not promise that a canonical, sitemap, title change or performance improvement will produce rankings.

When asked to fix issues, follow the repository's conventions, preserve private-route intent and run checks appropriate to the change. Verify the affected behaviour after editing. Report local, deployed and unverified results separately; do not claim production success from a clean build.

For repeat runs, inspect changes since the last audit and refresh the relevant evidence before repeating a full crawl. Record the change date, expected effect and next observation window. Recheck implementation promptly; assess traffic only after sufficient comparable observations. If evidence is too weak or the likely return is low, retain or close the investigation rather than generating work.
