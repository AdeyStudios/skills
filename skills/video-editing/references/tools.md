# Tools and finishing

Use whichever authorised tools can realise and inspect the edit. These adapters are optional. The editorial skill does not require a particular editor, model, operating system or private connector.

## Source inspection helper

`scripts/inspect_video.py` needs Python 3, Pillow, FFmpeg and ffprobe. It reads the source and writes a new inspection directory; it refuses to overwrite an occupied directory.

```sh
python /path/to/video-editing/scripts/inspect_video.py source.mp4 --output new-inspection
python /path/to/video-editing/scripts/inspect_video.py source.mp4 --output new-inspection --interval 0.25 --max-frames 60 --save-full-frames
```

Outputs include metadata, exact decoded-frame timestamps, a sample manifest, timed contact sheets and candidate source cuts. `--max-frames` limits overview size by widening the sample interval when needed. Candidate cuts can miss edits or respond to motion; manually inspect around intended in/out points.

Saved thumbnails are for analysis. The optional full-resolution PNGs preserve the sampled source frames for creative work. A still-to-live transition needs the recorded source frame and matching transform, not an approximate time inferred from a small JPEG. Verify footage between samples.

HDR-tagged sources are flagged; the helper does not claim to tone-map their thumbnails. Use a colour-managed reference for colour decisions. A filename, manifest rendition label or export size is not evidence of source detail: inspect decoded dimensions and orientation.

## Source discovery and download

Use connected media tools or a suitable downloader when available and authorised. Keep the original, canonical source URL, publisher and relevant date together. Verify that media matches the requested show or subject. Temporary signed media URLs are retrieval details, not durable source citations. Never bundle another creator's downloaded videos into this public skill.

A failed page viewer or direct CDN request does not establish that the public video is unavailable. Try an available maintained downloader before asking the user to supply a file. For example, when installed, `yt-dlp --no-playlist --no-overwrites -o 'sources/%(id)s.%(ext)s' 'PUBLIC_VIDEO_URL'` can resolve public playback formats that a copied page URL cannot. Verify the resulting file with ffprobe and decoding; a successful HTTP response can contain HTML rather than video. Keep retries bounded; respect rate limits and disclose an actual login or access requirement instead of silently using browser credentials or bypassing protected access.

Prefer the highest useful real source quality, not a nominal format label. Inspect colour metadata, variable frame rate and existing audio before conforming. Preserve useful audio or deliver silent according to the brief; do not add music merely because a platform recommends sound.

## Editor automation

Check an existing integration's health and current project before starting another process or listener. A busy local port can mean the intended connection is already running. Do not repeatedly launch a bridge, stop an unrelated process or modify security settings to get past that symptom.

Use a separate project or version for an experimental edit. Preserve the user's active work and original media. Keep within the integration's media/output permissions. Follow the installed editor's actual API/version documentation rather than assuming a generic SDK or a licensed edition is available.

If a requested editor is unavailable, report that specific gap and continue independent work. Prepare a reviewable input or proof while requesting the minimum missing access. Clearly distinguish a proposed grade, a look calculated outside an editor, and an actual editor-applied and rendered grade.

## Colour and delivery

- Match source colour space, transfer, range and orientation deliberately. A display-referred clip is not log footage. Preserve intended garment colour unless the brief explicitly authorises a creative change.
- A high-quality intermediate can bridge a graphics renderer and a colour editor. Check that its tags and decoded appearance agree, then inspect the actual graded render before compressing delivery.
- Keep typography, garment edges and gradients readable at phone size. Repeated temporal samples that leave separated duplicate edges are not convincing motion blur.
- Verify the final container's streams as well as the image. Native renders can carry timecode/data tracks; a requested silent video should not accidentally acquire an audio stream during packaging.
- Check the compressed delivery against the graded master for colour, crop, duration and motion. Re-encoding, a larger resolution or a successful decode does not establish better source quality or stronger editing.
- Retain the project, source mapping and actual render settings needed to revise the work. Do not claim to have used a named application merely because it is installed or supplied an intermediate format.
