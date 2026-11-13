"""Simulate placement risks. Masks/crops are assumptions, never live UI guarantees."""
import argparse
import io
import json
import math
from pathlib import Path
import subprocess
import sys

from PIL import Image, ImageDraw, ImageOps, UnidentifiedImageError


def rect_for_crop(width, height, ratio):
    if width / height <= ratio:
        h = min(height, round(width / ratio))
        top = (height - h) // 2
        return (0, top, width, top + h)
    w = min(width, round(height * ratio))
    left = (width - w) // 2
    return (left, 0, left + w, height)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--at', type=float, default=0)
    parser.add_argument('--boxes', type=Path)
    parser.add_argument('--margins', type=float, nargs=4, metavar=('TOP', 'RIGHT', 'BOTTOM', 'LEFT'),
                        default=(.20, .20, .40, .10))
    args = parser.parse_args()
    if not math.isfinite(args.at) or args.at < 0:
        parser.error('--at must be finite and nonnegative')
    top, right, bottom, left = args.margins
    if (not all(math.isfinite(v) and 0 <= v < 1 for v in args.margins)
            or top + bottom >= 1 or left + right >= 1):
        parser.error('margins must leave a positive interior')
    if args.output.exists() and (not args.output.is_dir() or any(args.output.iterdir())):
        parser.error('output must be new or empty; refusing to overwrite review files')
    try:
        with Image.open(args.source) as opened:
            frame = ImageOps.exif_transpose(opened).convert('RGB')
    except UnidentifiedImageError:
        result = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(args.at), '-i', str(args.source),
                                 '-frames:v', '1', '-f', 'image2pipe', '-c:v', 'png', '-'],
                                capture_output=True, check=True)
        if not result.stdout:
            parser.error('no video frame available at the requested time')
        frame = Image.open(io.BytesIO(result.stdout)).convert('RGB')
    w, h = frame.size
    boxes = json.loads(args.boxes.read_text()) if args.boxes else []
    if not isinstance(boxes, list):
        parser.error('boxes JSON must be a list')
    for item in boxes:
        b = item.get('box', []) if isinstance(item, dict) else []
        if (len(b) != 4 or not all(isinstance(v, (float, int)) and math.isfinite(v) and 0 <= v <= 1 for v in b)
                or b[0] >= b[2] or b[1] >= b[3]):
            parser.error('each box must contain normalized ordered left/top/right/bottom bounds')
    safe = (math.ceil(w * left), math.ceil(h * top), math.floor(w * (1-right)), math.floor(h * (1-bottom)))
    views = {'layout-assumption': safe}
    views.update({name: rect_for_crop(w, h, ratio) for name, ratio in [('crop-3x4', .75), ('crop-4x5', .8), ('crop-square', 1)]})
    args.output.mkdir(parents=True, exist_ok=True)
    overlay = Image.new('RGBA', (w, h), (210, 32, 58, 100))
    draw = ImageDraw.Draw(overlay)
    draw.rectangle((safe[0], safe[1], safe[2]-1, safe[3]-1), fill=(0, 0, 0, 0), outline=(54, 234, 149, 255), width=max(1, round(w/250)))
    Image.alpha_composite(frame.convert('RGBA'), overlay).convert('RGB').save(args.output/'layout-assumption.png')
    for name, rect in views.items():
        if name != 'layout-assumption':
            frame.crop(rect).save(args.output/f'{name}.png')
    checks = []
    for i, item in enumerate(boxes):
        x0, y0, x1, y1 = item['box']
        pixel = (x0*w, y0*h, x1*w, y1*h)
        outside = [name for name, r in views.items()
                   if pixel[0] < r[0] or pixel[1] < r[1] or pixel[2] > r[2] or pixel[3] > r[3]]
        checks.append({'label': item.get('label', f'box-{i+1}'), 'box': item['box'], 'outside_views': outside})
    report = {'status': 'simulation', 'source': str(args.source), 'sample_seconds': args.at,
              'width': w, 'height': h, 'margins_top_right_bottom_left': args.margins,
              'basis': 'Custom rectangular assumption' if '--margins' in sys.argv else 'Conservative house assumption; not official platform UI',
              'views': {k: list(v) for k, v in views.items()}, 'boxes': checks,
              'limits': 'No OCR, animation tracking, actual app UI, caption expansion or off-centre cover positioning checked.'}
    (args.output/'placement-report.json').write_text(json.dumps(report, indent=2))
    sheet = Image.new('RGB', (1000, 520), '#202028')
    d = ImageDraw.Draw(sheet)
    for i, name in enumerate(views):
        with Image.open(args.output/f'{name}.png') as im:
            thumb = im.copy()
        thumb.thumbnail((230, 430), Image.Resampling.LANCZOS)
        x = 250*i + (250-thumb.width)//2
        sheet.paste(thumb, (x, 60+(430-thumb.height)//2))
        d.text((250*i+12, 12), name, fill='white')
        d.text((250*i+12, 30), 'ASSUMPTION' if i == 0 else 'CROP STRESS TEST', fill='#c7b5ec')
    sheet.save(args.output/'placement-sheet.jpg', quality=92)
    print(json.dumps({'output': str(args.output), 'supplied_boxes': len(checks),
                      'boxes_with_warnings': sum(bool(x['outside_views']) for x in checks),
                      'status': 'simulation'}))


if __name__ == '__main__':
    main()
