---
name: seo-review
description: Review a site's organic discoverability, indexing signals, metadata, internal links and page usefulness. Use for evidence-based SEO audits and prioritised fixes to existing pages; use a content research workflow when the main task is choosing new articles.
license: MIT
---

# SEO review

Identify concrete obstacles between useful public content and the people searching for it. Distinguish verified defects, useful improvements and untested hypotheses.

## Understand the site

Identify intended public pages, private or authenticated routes, important user journeys and the business goal. Inspect available code and live pages, plus authorised search analytics if available. Do not assume every URL should be indexed.

Choose representative pages from relevant templates rather than checking only the homepage. When possible, verify the deployed response as well as source code; a local change is not evidence that production is fixed.

## Check the evidence

- Verify response codes, redirect chains and accidental access restrictions. Inspect robots directives, `noindex`, canonical targets and XML sitemap coverage for pages intended to be indexed.
- Check meaningful, distinct titles and descriptions. A practice page can have a concise descriptive search title while retaining its full question in the content.
- Inspect crawlable internal links, useful anchor text, orphaned pages and hierarchy. Avoid self-links or navigation that adds steps without helping a visitor. Educational discovery links should support the product's intended primary journey.
- Review whether the page satisfies its apparent search intent. Check duplicate or thin material, misleading promises, actual explanations and useful examples. More words or more structured data are not automatically better.
- Check relevant rendered content, mobile usability and loading problems. Use field performance data when available and identify lab measurements as lab measurements.
- Review structured data only when it represents visible, supported content and an appropriate type. Check applicable official guidance before recommending search features.

Separate crawlability, indexing eligibility and actual indexing. A valid sitemap submission does not prove its URLs are indexed. Missing analytics access should be disclosed rather than replaced by guessed traffic or rankings.

## Report what matters

Lead with the most consequential verified problem. For each material finding, give the affected URL or code location, observed behaviour, implication, concrete fix and a way to verify it. Prioritise by likely impact, reach, confidence and effort without manufacturing numerical precision.

Use current official search-engine guidance for claims about indexing and supported features. Do not promise that a canonical, sitemap, title change or performance improvement will produce rankings.

When asked to fix issues, follow the repository's conventions, preserve private-route intent and run checks appropriate to the change. Verify the affected behaviour after editing. Report local, deployed and unverified results separately; do not claim production success from a clean build.
