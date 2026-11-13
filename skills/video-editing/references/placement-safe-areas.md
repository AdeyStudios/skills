# Placement, cropping and interface safe areas

Reviewed 13 November 2026. Read before composing text for TikTok or Instagram Reels, and when checking delivery. Platform layouts change; identify the actual surface rather than applying one permanent rectangle to every video.

## Two different losses of visibility

**Cropping** removes picture outside the displayed viewport: feed previews, profile tiles, cover crops and different device shapes may show less than the exported 9:16 frame. **Occlusion** leaves the picture present but covers it with app chrome: top navigation, account information, captions, subtitles, music labels, buttons and an ad CTA. Passing one check does not pass the other.

The same headline can be legible in a local player and lose its first line in a feed crop. A URL neatly aligned to the bottom of a composition can sit behind the caption or controls. Cover positioning is a separate decision from video playback framing.

## What the sources establish

- [TikTok Auction In-Feed Ads](https://ads.tiktok.com/resources/help/article/tiktok-auction-in-feed-ads?lang=en-GB), updated June 2026: safe areas depend on aspect ratio, caption length and additional formats. It provides different standard/anchor and LTR/RTL templates and warns that preview and live display can differ by device. Use the template matching the placement; an ordinary-feed template cannot establish safety for every add-on or organic layout.
- [TikTok interactive Download Card specifications](https://ads.tiktok.com/resources/help/article/tiktok-interactive-add-on-download-card-ad-specifications?lang=en-GB): longer captions reduce the available area; inspect the corresponding preview. Adopt the mechanism, without assuming an organic edit needs an ad card or other commercial elements.
- Meta's **Reels ads guide**, [publisher-authored PDF hosted by an event organiser](https://d3m889aznlr23d.cloudfront.net/img/events/458925814/assets/e042d2be.reels_ads_guide1.pdf), page 4: reserve the bottom 35% from important creative elements, text and logos, and check with its safe-zone templates. This is advertising guidance, not a measured map of every organic Reel. On a 1080×1920 canvas, 35% is 672 pixels; on 720×1280 it is 448 pixels. The remainder is not automatically all safe.

Meta's [live help article](https://www.facebook.com/business/help/980593475366490) and Ads Guide redirected to an access/temporary-block page during this research. Do not claim their current full numeric margins were verified here. Obtain an accessible current template or preview when available. No specific current Instagram feed/profile crop ratio was verified from a live first-party specification in this review.

These sources explain interface risk. They do not prove an engagement lift for moving a headline, or require paid-ad layouts for all organic content.

## Apply before polishing

1. Identify platform, organic/ad placement, intended feed/cover surfaces, caption length, subtitle plan and language direction. Use known brief/context; do not make a routine edit wait for optional details.
2. Obtain the current placement guide or inspect a relevant actual preview. Record its source/date, canvas dimensions and reserved regions. For a shared export, use the intersection of relevant usable areas. Treat the right-side button rail and lower caption area separately where needed.
3. Block out the headline, subject/payoff, subtitles and any essential branding against those regions. Make the opening clear inside the usable area from its first readable state. Avoid making the premise depend on a tiny label at the very top.
4. Check complete glyph bounds, not just a text anchor. Include multiline headings, descenders and any essential outline. Inspect animated bounds for the interval the viewer must read; decorative entrances can cross an edge if the complete readable state is safely held.
5. Check important source text too. A downloaded post with baked-in words may already be unsuitable for the new placement. Reframe, rebuild an authorised text layer, or choose a different interval; placing a second title over the problem does not fix it.

Do not reserve the whole picture for text. Footage and decoration can fill the canvas, with the essential information composed to survive the intended display. Move a title, change its line breaks, reduce unnecessary copy or make a separate layout before reducing its size below phone readability.

## When placement details are unavailable

For an initial 9:16 draft, use a **conservative house layout assumption** for essential text: x=10–80% of width, y=20–60% of height. At 1080×1920 this is x=108–864, y=384–1152; at 720×1280 it is x=72–576, y=256–768. This deliberately leaves room above, below and on the button side. It is our fallback, **not an official TikTok/Instagram safe zone**, and does not guarantee visibility with expanded UI, unusual devices, RTL layouts or every placement. Replace it with appropriate evidence when available.

Use centred 3:4, 4:5 and square crops as **stress tests** when actual feed/cover behaviour is unknown. These are candidate views, not claims that an app currently uses all three. If the posting preview positions the cover differently, use that crop. Do not certify a cover from a centred test alone.

The optional helper requires Python and Pillow, plus FFmpeg for video input:

```sh
python scripts/preview_placement.py final.mp4 --at 1.0 --output new-placement-review
python scripts/preview_placement.py frame.png --boxes text-boxes.json --output new-layout-review
```

An optional boxes JSON is a list such as `[{"label":"opening headline", "box":[0.10,0.25,0.75,0.40]}]`, with normalized left/top/right/bottom bounds. Supply actual rendered bounds; the helper performs no OCR. It writes a fallback overlay, candidate crops, a contact sheet and a report of supplied boxes outside each view. `--margins TOP RIGHT BOTTOM LEFT` can replace the fallback with a documented rectangular assumption. Irregular controls need their actual mask as an additional check.

## Verify the delivery

Review the actual encoded first frame, hook, every important text state, payoff and ending at phone size. Show both crop and UI risks, including the expected caption and controls; check subtitles against both. Review the cover separately and keep preview overlays out of the final export. Use an unpublished in-app/editor placement preview when accessible; this check does not authorise publishing or uploading to an external service.

State which surfaces and assumptions were checked. A mock overlay or contact sheet is a simulated check, not proof of a current Instagram/TikTok display. The reason for this update was real feedback that top-aligned copy in locally attractive compositions was vulnerable after posting; moving essential information into a placement-aware composition is the adopted change.
