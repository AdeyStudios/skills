# Site audit procedure

Use this reference for a broad technical and on-page audit, optionally grounded in search analytics. Adapt depth to the site and access; unavailable checks are limitations, not passes or failures.

## Collect a reproducible baseline

1. Confirm the exact domain, resolving response, product, intended audience, market and language. Record dates and available history. Scope public page templates separately from login, account, app and utility routes.
2. Fetch representative responses: homepage, navigation destinations, a hub, a content page, an interactive landing page where present, and a genuine missing URL. Record status, redirect chain, final URL, relevant headers and document-head metadata. Keep raw-response evidence separate from rendered-browser evidence.
3. Fetch robots and sitemap documents, including sitemap indexes. Count unique eligible URLs by section, observe redirects and compare crawlable links. Sitemap inclusion or an apparently recent lastmod is not proof of publication date or indexation. Do not prescribe sitemap priorities as a ranking lever.
4. Check important homepage and navigation actions end to end, including destination status and whether the intended task can begin. A source-string match alone does not verify a dynamically generated link. Distinguish an unlinked obsolete URL from a currently broken CTA.
5. Inspect raw HTML versus the rendered page where rendering may affect content or links. Extract the document head title, not SVG titles, image captions or embedded application strings. Check actual H1 structure, canonicals, robots, descriptions and meaningful content.

Record tools, sample coverage and failed fetches. A proxy or environment error is not evidence that the public site fails. Avoid repeated requests to private or disallowed routes; inspect authorised source or metadata when appropriate.

## Check discovery, indexing and page quality

- Trace useful paths from entry pages to content hubs and articles. Sitemap presence without incoming links in a limited sample means an orphan candidate, not a proven site-wide orphan.
- Establish intended indexing before changing canonicals, robots or noindex. Blocking crawl and preventing indexing are different mechanisms; do not blanket-noindex an interactive section solely because it has fewer words.
- Check titles for distinct, accurate intent and useful branding. Treat length as a preview/readability consideration, not a universal character-count rule. Google can generate a title from multiple sources; a different displayed title does not establish its cause.
- Check descriptions and heading structure in context, language declaration, and alternates where genuinely different language/region versions exist. UK pricing or spelling alone does not make a missing hreflang set a defect.
- Check social previews as sharing behaviour, separate from direct ranking claims.
- Inspect structured data for validity, visible supporting content, the appropriate type and current feature eligibility. Missing a schema type is not automatically an issue; do not add FAQ or rating markup just to increase a score or promise a rich result.
- Assess content by whether it answers the visitor's task with a useful explanation, example or interaction. Word counts can flag candidates but cannot establish thinness by themselves.

## Performance and mobile

Check representative mobile journeys, viewport, readability, tap targets and visible failures. Use field data when available. For lab measurements, record URL, device strategy, tool/version, conditions and date; one Lighthouse run is a diagnostic sample, not a ranking or conversion forecast.

Inspect LCP, INP and CLS where measurable; do not substitute a retired or differently defined lab metric for a field metric. Investigate actual transfer and execution costs, images, fonts, third-party scripts, caching headers and render-blocking resources before prescribing changes. Preserve needed consent, authentication and analytics behaviour. A private response's caching policy may be intentional; do not globally cache personalised content as an SEO fix.

## Search Console, when available

Prefer an authorised read-only connector/API. Otherwise use user-provided exports or a user-controlled signed-in browser. Never request their password. Confirm property, search type, filters, date range, final versus preliminary data, export limits and reporting dates.

Collect relevant performance dimensions, property totals, index coverage reasons and affected URL lists, plus sitemap submission/read status. URL-level inspection is needed for specific indexation conclusions. A performance export with no row for a new page does not prove it is unindexed.

Compare like-for-like date windows and page cohorts. Note new pages, releases and changes in query, country or device mix. Prefer query-by-page rows for opportunity attribution. Pages at positions roughly 8 to 30 may be investigation candidates, not automatically easy wins. Check relevance, actual result pages and the existing answer before recommending work.

Compute aggregates reproducibly with explicit grouping membership and deduplication. Query-row sums can omit anonymised data; page-level impressions can differ from property totals. Do not infer competition, conversion or title failure merely to explain those differences. CTR comparisons should account for position and search context, without imposing a universal target.

## Opportunity and delivery decisions

For each issue capture: URL/template, observation/date, source, diagnosis versus hypothesis, affected visitor journey, proposed fix or cheapest next check, effort/risk, verification and business outcome to observe. Use a practical order:

1. Verified breakages preventing important discovery, access or the next useful action.
2. Existing relevant pages with a confirmed intent/content/linking mismatch and meaningful opportunity evidence.
3. New content with a distinct unmet need and product fit.
4. Cosmetic or speculative improvements only where their return justifies the work.

The order is conditional on impact and scope. If another team is already addressing an item, record that dependency rather than duplicating the work. Keywords and ideas belong in the report only when they support a decision; do not invent volume or pad a fixed list.

Deliver a short executive summary, prioritised issue table, relevant search-data tables, preserved strengths, and next actions with owners/status where known. Recheck any recommendation against current deployment before implementation. A review is not permission to spend, publish, contact others or schedule an agent.

## Basis and limits

This working draft incorporates the structure of a user-supplied Grok audit and procedure, qualified against official documentation on 13 November 2026. It retains evidence reconciliation, broad template coverage and explicit priorities; it does not adopt the source's site-specific findings or causal conclusions as general rules.

- [Search Console performance metrics and dimensions](https://support.google.com/webmasters/answer/7576553).
- [Search Analytics API query and aggregation behaviour](https://developers.google.com/webmaster-tools/v1/searchanalytics/query).
- [Google title-link guidance](https://developers.google.com/search/docs/appearance/title-link): descriptive titles, multiple title sources and device-dependent truncation, not a fixed character limit.
- [Search documentation updates](https://developers.google.com/search/updates): verify feature support before prescribing structured data. FAQ rich results were retired in May 2026; adding that type is not a current rich-result opportunity.

Packaging and author scenario checks do not establish ranking, traffic or conversion improvement. Those need later observed outcomes.
