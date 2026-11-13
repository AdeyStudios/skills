# Production decisions from a multi-source fashion batch

Read when making variants, combining graphics with footage, reframing moving subjects or packaging several deliverables. These are transferable decisions, not a prescribed visual style or render stack.

## Different edits need different discoveries

Before polishing variants, describe each in one sentence using what the viewer sees. Compare their opening, selection, change of scale and payoff. If the only difference is a wipe or typeface, develop a different attention arc.

Useful questions include: can one garment carry a small story across settings? Does a detail recur in visibly different forms? Does the film offer a relationship between environment and material? Does a portrait become more interesting when construction details interrupt it? Choose based on the actual footage; none is a mandatory format.

In a six-edit batch, three films supported different pairs:

| Source | One approach | Another approach |
| --- | --- | --- |
| [LOEWE Spring/Summer 2025](https://www.youtube.com/watch?v=wqZby80VMq0) | Circular dress silhouettes revealed through an editorial image window | Flower shoes, a flower-print shirt and floral dresses linked through a visible motif |
| [Issey Miyake Fall 2021](https://www.vogue.com/video/watch/issey-miyake-fall-2021-ready-to-wear-video) | Sea movement connected to pleats and wind-blown fabric | One yellow coat followed from portrait to stairs and landscape |
| [Maison Margiela Artisanal 2024](https://www.youtube.com/watch?v=DgMJq67ZOwE) | Backlit entrances and theatrical whole-figure movement | Moving portraits interrupted by glove, lace and construction details |

The Issey source already connects nature and clothing. Re-editing an existing relationship is legitimate; do not claim to have invented the source film's direction. These examples illustrate variation, not a menu to repeat for every fashion house.

## Graphic treatments with live footage

A frame, page, title or image window can organise attention while footage keeps moving inside it. The graphic has an editorial job: reveal a silhouette, connect a detail, change scale or lead into the live scene. Once that discovery lands, let the subject take over. One purposeful transition can be enough; subsequent cuts need not repeat it.

For an overlap, use consecutive outgoing and incoming frames. Account for the consumed incoming frames when the transition finishes so the action does not restart. Inspect the encoded join for a repeated pose, tiny hold or jump. An actual still-to-live handoff instead needs the exact matching source frame and transform described in the fashion reference.

Do not let a graphic treatment reduce readable clothing to a small decorative panel for the entire piece. Check the subject at phone size, including during the opening and final reveal.

## Track the person, not the centre of the source

A centred portrait crop of a wide runway film often misses a walking model. Record the subject's position at the chosen interval's beginning and end, then inspect the intervening motion. Follow a stable body or garment anchor, with room for hats, hems, hands and walking direction. Use a wider image window when a tight crop cannot preserve the intended information.

Check each selected interval rather than reusing one crop across the source. In this batch, changing the crop path restored a figure moving across a wide stage. An unrelated black look was also removed from the yellow-coat sequence: continuity of the subject mattered more than having another attractive shot.

## Make timing explicit

Keep original source times and proxy-to-source mappings. Use edit-friendly proxies if needed, but inspect their actual frame counts; a nominal three-second clip may decode one frame short. Express timeline ranges in frames with an explicit frame rate, and check that every requested source range exists.

Choose cadence deliberately. This batch used 25 fps for 25/50 fps sources and 24 fps for approximately 24 fps footage instead of imposing 30 fps everywhere. Other briefs can need other rates. Decide whether conversion means resampling, a slight speed change or interpolation, and inspect the result around fabric, limbs and overlaps.

Detect candidate source cuts, then check near the real in/out frames. A transition already inside a source can slip past an overview sheet and appear as an unexplained fragment in the final edit. In the portrait variant, shortening a detail interval removed just such a fragment. Verify the compressed export as well as the selected source.

## Deliver a usable batch

Keep a portable project folder with relative media paths, canonical source links, source intervals, render settings and editable scripts or project files. A practical separation is `exports/` for final videos, `review/` for drafts and inspection sheets, `sources/` for originals, and a separate thumbnail location. A local comparison page can help with paired variants; it should use the actual final exports and working relative links.

Do not mix poster images with final videos in a way that makes six videos look like twelve deliverables. Give direct paths or links to the videos. When requested, reveal the existing folder in the file manager; create an archive only when wanted. Keep project media and private reference collections out of the public skill repository.

## Evidence and limits

The user liked all six delivered edits and requested preservation of this workflow on 13 November 2026. The exports passed complete decoding and frame count, dimension, cadence, colour-tag and silence checks; the author inspected timed frames and dense joins. That is qualitative creative acceptance and technical verification, not an independent comparison, full-speed phone playback by the author or measured audience retention. Keep that distinction when applying these lessons elsewhere.
