#!/usr/bin/env python3
"""Read-only source inspection: timed overviews, frame provenance and cut candidates.

Requires Python 3, Pillow, ffprobe and ffmpeg. Does not edit the source, download
media, infer retention, tone-map HDR, or claim that detected cuts are exhaustive.
"""
import argparse
import bisect
import csv
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run(arguments):
    result = subprocess.run(arguments, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(f"{Path(arguments[0]).name} failed: {result.stderr.strip()[-900:]}")
    return result.stdout


def write_csv(path, rows, fields):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def inspect(source, output, interval=0.5, max_frames=60, threshold=0.18,
            save_full=False, skip_scenes=False, thumb_width=160):
    from PIL import Image, ImageDraw

    source = Path(source).expanduser().resolve()
    output = Path(output).expanduser().resolve()
    if not source.is_file():
        raise ValueError("Input must be an existing local media file.")
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise ValueError("Output must be a new or empty directory; existing files will not be overwritten.")
    for binary in ("ffprobe", "ffmpeg"):
        if not shutil.which(binary):
            raise RuntimeError(f"{binary} is required but is not available on PATH.")

    probe = json.loads(run(["ffprobe", "-v", "error", "-show_streams", "-show_format",
                            "-of", "json", str(source)]))
    videos = [s for s in probe.get("streams", []) if s.get("codec_type") == "video"
              and not s.get("disposition", {}).get("attached_pic")]
    if not videos:
        raise ValueError("No video stream was found; audio-only files and cover art are not video footage.")
    stream = videos[0]
    stream_index = stream["index"]
    decoded = json.loads(run(["ffprobe", "-v", "error", "-select_streams", str(stream_index),
                              "-show_frames", "-show_entries", "frame=best_effort_timestamp_time",
                              "-of", "json", str(source)]))
    raw_frames = decoded.get("frames", [])
    if not raw_frames or any("best_effort_timestamp_time" not in f for f in raw_frames):
        raise ValueError("Exact decoded-frame timestamps are unavailable; inspect this source in an editor.")
    pts = [float(f["best_effort_timestamp_time"]) for f in raw_frames]
    if any(b < a for a, b in zip(pts, pts[1:])):
        raise ValueError("Decoded presentation timestamps are not ordered; inspect the source before sampling.")
    start = pts[0]
    span = pts[-1] - start
    count = min(max_frames, max(1, math.ceil(span / interval) + 1), len(pts))
    targets = [start] if count == 1 else [start + span * i / (count - 1) for i in range(count)]
    indices = sorted({min(len(pts) - 1, bisect.bisect_left(pts, t)) for t in targets})
    warnings = []
    if stream.get("color_transfer") in ("smpte2084", "arib-std-b67"):
        warnings.append("HDR source: overview frames are not tone-mapped. Use a colour-managed viewer for colour decisions.")
    if len(videos) > 1:
        warnings.append("Multiple video streams: this inspection uses the first non-cover-art video stream.")
    output.mkdir(parents=True, exist_ok=True)
    metadata = {
        "status": "incomplete", "source": str(source), "video_stream_index": stream_index,
        "duration_seconds": float(probe.get("format", {}).get("duration", span)),
        "decoded_frames": len(pts), "source_start_pts_seconds": start,
        "encoded_width": stream.get("width"), "encoded_height": stream.get("height"),
        "codec": stream.get("codec_name"), "average_frame_rate": stream.get("avg_frame_rate"),
        "colour_space": stream.get("color_space"), "colour_transfer": stream.get("color_transfer"),
        "colour_primaries": stream.get("color_primaries"), "colour_range": stream.get("color_range"),
        "stream_side_data": stream.get("side_data_list", []),
        "audio_streams": [{k: s.get(k) for k in ("index", "codec_name", "sample_rate", "channels")}
                          for s in probe.get("streams", []) if s.get("codec_type") == "audio"],
        "requested_interval_seconds": interval, "max_overview_frames": max_frames,
        "overview_frames": len(indices), "warnings": warnings,
        "scene_detection": "skipped" if skip_scenes else "candidate detection; not an exhaustive shot list",
        "scene_threshold": threshold if not skip_scenes else None,
    }
    metadata_file = output / "metadata.json"
    metadata_file.write_text(json.dumps(metadata, indent=2) + "\n")
    write_csv(output / "decoded_frames.csv",
              ({"source_frame_index": i, "source_pts_seconds": t, "relative_seconds": t - start}
               for i, t in enumerate(pts)),
              ["source_frame_index", "source_pts_seconds", "relative_seconds"])

    samples = []
    thumbnails = []
    (output / "thumbnails").mkdir()
    if save_full:
        (output / "full-frames").mkdir()
    with tempfile.TemporaryDirectory(prefix="video-overview-") as temporary:
        select = "+".join(f"eq(n\\,{i})" for i in indices)
        run(["ffmpeg", "-v", "error", "-copyts", "-i", str(source), "-map", f"0:{stream_index}",
             "-vf", f"select={select}", "-an", "-fps_mode", "vfr", "-frames:v", str(len(indices)),
             "-pix_fmt", "rgb24", "-start_number", "0", str(Path(temporary) / "frame_%04d.png")])
        for j, index in enumerate(indices):
            frame = Path(temporary) / f"frame_{j:04d}.png"
            with Image.open(frame) as opened:
                image = opened.convert("RGB")
            if j == 0:
                metadata["displayed_frame_width"], metadata["displayed_frame_height"] = image.size
            thumb = image.resize((thumb_width, max(1, round(image.height * thumb_width / image.width))),
                                 Image.Resampling.LANCZOS)
            thumb_path = f"thumbnails/frame_{j:04d}.jpg"
            thumb.save(output / thumb_path, quality=90)
            full_path = f"full-frames/frame_{j:04d}.png" if save_full else ""
            if save_full:
                shutil.copy2(frame, output / full_path)
            samples.append({"source_frame_index": index, "source_pts_seconds": pts[index],
                            "relative_seconds": pts[index] - start,
                            "thumbnail": thumb_path, "full_resolution_frame": full_path})
            thumbnails.append(thumb)

    for page, offset in enumerate(range(0, len(samples), 36), 1):
        chunk = thumbnails[offset:offset + 36]
        cols = min(6, len(chunk))
        cell_w = thumb_width + 12
        cell_h = chunk[0].height + 30
        rows = math.ceil(len(chunk) / cols)
        sheet = Image.new("RGB", (cols * cell_w, rows * cell_h + 24), "#202020")
        draw = ImageDraw.Draw(sheet)
        draw.text((6, 5), source.name[:90], fill="white")
        for j, thumb in enumerate(chunk):
            x, y = (j % cols) * cell_w + 6, (j // cols) * cell_h + 46
            sample = samples[offset + j]
            draw.text((x, y - 18), f"{sample['relative_seconds']:.3f}s | f{sample['source_frame_index']}", fill="white")
            sheet.paste(thumb, (x, y))
        sheet.save(output / f"contact-sheet-{page:02d}.jpg", quality=93)

    candidates = []
    if not skip_scenes:
        stdout = run(["ffmpeg", "-v", "error", "-copyts", "-i", str(source), "-map", f"0:{stream_index}",
                      "-vf", f"select=gt(scene\\,{threshold}),metadata=mode=print:key=lavfi.scene_score:file=-",
                      "-an", "-fps_mode", "vfr", "-f", "null", "-"])
        timestamp = None
        for line in stdout.splitlines():
            match = re.search(r"pts_time:([-+0-9.eE]+)", line)
            if match:
                timestamp = float(match.group(1))
            if line.startswith("lavfi.scene_score=") and timestamp is not None:
                insertion = bisect.bisect_left(pts, timestamp)
                near = min(range(max(0, insertion - 1), min(len(pts), insertion + 1)),
                           key=lambda i: abs(pts[i] - timestamp))
                candidates.append({"source_frame_index": near, "source_pts_seconds": pts[near],
                                   "relative_seconds": pts[near] - start,
                                   "scene_score": float(line.split("=", 1)[1])})
    write_csv(output / "candidate_cuts.csv", candidates,
              ["source_frame_index", "source_pts_seconds", "relative_seconds", "scene_score"])
    write_csv(output / "frame_manifest.csv", samples,
              ["source_frame_index", "source_pts_seconds", "relative_seconds", "thumbnail", "full_resolution_frame"])
    metadata.update(status="complete", samples=samples, candidate_cut_count=len(candidates),
                    scene_candidates_are_exhaustive=False)
    metadata_file.write_text(json.dumps(metadata, indent=2) + "\n")
    return metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("--output", required=True)
    parser.add_argument("--interval", type=float, default=0.5)
    parser.add_argument("--max-frames", type=int, default=60)
    parser.add_argument("--scene-threshold", type=float, default=0.18)
    parser.add_argument("--thumb-width", type=int, default=160)
    parser.add_argument("--save-full-frames", action="store_true")
    parser.add_argument("--skip-scene-detection", action="store_true")
    args = parser.parse_args()
    if args.interval <= 0 or not 2 <= args.max_frames <= 600 or not 64 <= args.thumb_width <= 640:
        parser.error("Use a positive interval, 2–600 maximum frames, and a thumbnail width of 64–640.")
    if not 0 < args.scene_threshold <= 1:
        parser.error("Scene threshold must be greater than zero and at most one.")
    try:
        metadata = inspect(args.source, args.output, args.interval, args.max_frames,
                           args.scene_threshold, args.save_full_frames,
                           args.skip_scene_detection, args.thumb_width)
    except (ValueError, RuntimeError, ImportError) as error:
        parser.exit(1, f"Inspection failed: {error}\n")
    print(json.dumps({"output": str(Path(args.output).resolve()), "status": metadata["status"],
                      "overview_frames": metadata["overview_frames"],
                      "candidate_cuts": metadata["candidate_cut_count"],
                      "warnings": metadata["warnings"]}, indent=2))


if __name__ == "__main__":
    main()
