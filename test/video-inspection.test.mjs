import { test } from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, readFileSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';

const python = process.env.VIDEO_EDITING_PYTHON || 'python3';
const script = fileURLToPath(new URL('../skills/video-editing/scripts/inspect_video.py', import.meta.url));
const available = spawnSync(python, ['-c', 'from PIL import Image']).status === 0
  && ['ffmpeg', 'ffprobe'].every(bin => spawnSync(bin, ['-version']).status === 0);
function run(bin, args) {
  const result = spawnSync(bin, args, { encoding: 'utf8', maxBuffer: 4 * 1024 * 1024 });
  assert.equal(result.status, 0, result.stderr);
  return result.stdout;
}

test('video inspection preserves source, locates real cuts, samples exact frames and refuses overwrites',
  { skip: !available && 'Requires Python with Pillow, ffmpeg and ffprobe' }, () => {
    const folder = mkdtempSync(join(tmpdir(), 'video-skill-test-'));
    try {
      const source = join(folder, 'colours.mp4');
      const output = join(folder, 'inspection');
      run('ffmpeg', ['-v', 'error', '-f', 'lavfi', '-i', 'color=red:s=160x284:r=30:d=2',
        '-f', 'lavfi', '-i', 'color=blue:s=160x284:r=30:d=2',
        '-f', 'lavfi', '-i', 'color=green:s=160x284:r=30:d=2',
        '-filter_complex', '[0:v][1:v][2:v]concat=n=3:v=1:a=0[v]', '-map', '[v]',
        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', source]);
      const hash = () => createHash('sha256').update(readFileSync(source)).digest('hex');
      const original = hash();
      run(python, [script, source, '--output', output, '--max-frames', '8', '--save-full-frames']);
      assert.equal(hash(), original);
      const meta = JSON.parse(readFileSync(join(output, 'metadata.json')));
      assert.equal(meta.status, 'complete');
      assert.equal(meta.decoded_frames, 180);
      assert.equal(meta.samples.length, 8);
      assert.equal(meta.samples.at(-1).source_frame_index, 179);
      assert.equal(meta.scene_candidates_are_exhaustive, false);
      const cuts = readFileSync(join(output, 'candidate_cuts.csv'), 'utf8').trim().split('\n').slice(1)
        .map(row => Number(row.split(',')[0]));
      assert.deepEqual(cuts, [60, 120]);
      const sample = meta.samples.find(item => item.relative_seconds > 2 && item.relative_seconds < 4);
      const pixel = JSON.parse(run(python, ['-c',
        'from PIL import Image; import sys,json; im=Image.open(sys.argv[1]); print(json.dumps([list(im.size),list(im.getpixel((80,142)))]))',
        join(output, sample.full_resolution_frame)]));
      assert.deepEqual(pixel[0], [160, 284]);
      assert.ok(pixel[1][2] > 240 && pixel[1][0] < 15, 'Exact sampled frame should be blue');
      const marker = join(output, 'keep.txt');
      writeFileSync(marker, 'keep');
      const refusal = spawnSync(python, [script, source, '--output', output], { encoding: 'utf8' });
      assert.notEqual(refusal.status, 0);
      assert.equal(readFileSync(marker, 'utf8'), 'keep');
      const audio = join(folder, 'audio.wav');
      run('ffmpeg', ['-v', 'error', '-f', 'lavfi', '-i', 'sine=frequency=440:duration=0.1', audio]);
      const noVideo = spawnSync(python, [script, audio, '--output', join(folder, 'audio-inspection')], { encoding: 'utf8' });
      assert.notEqual(noVideo.status, 0);
      assert.match(noVideo.stderr, /No video stream/);
    } finally {
      rmSync(folder, { recursive: true, force: true });
    }
  });
