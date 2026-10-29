import { test } from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, writeFileSync, readFileSync, existsSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, delimiter } from 'node:path';
import { fileURLToPath } from 'node:url';

const installer = fileURLToPath(new URL('../bin/install.mjs', import.meta.url));

function fixture(t) {
  const directory = mkdtempSync(join(tmpdir(), 'adey-skills-test-'));
  const capture = join(directory, 'arguments.json');
  t.after(() => rmSync(directory, { recursive: true, force: true }));
  const fake = join(directory, 'fake-npx.mjs');
  writeFileSync(fake, `import { writeFileSync } from 'node:fs';
writeFileSync(process.env.ADEY_SKILLS_TEST_CAPTURE, JSON.stringify(process.argv.slice(2)));
process.exit(Number(process.env.ADEY_SKILLS_TEST_STATUS || 0));
`);
  if (process.platform === 'win32') {
    writeFileSync(join(directory, 'npx.cmd'), `@"${process.execPath}" "${fake}" %*\r\n`);
  } else {
    writeFileSync(join(directory, 'npx'), `#!/bin/sh\nexec '${process.execPath.replaceAll("'", "'\\''")}' '${fake.replaceAll("'", "'\\''")}' "$@"\n`, { mode: 0o755 });
  }
  return {
    capture,
    run(args = [], extra = {}) {
      return spawnSync(process.execPath, [installer, ...args], {
        encoding: 'utf8',
        env: {
          ...process.env,
          PATH: directory + delimiter + process.env.PATH,
          ADEY_SKILLS_TEST_CAPTURE: capture,
          ...extra,
        },
      });
    },
  };
}

test('default install requests every skill globally for both agents without prompts', (t) => {
  const f = fixture(t);
  assert.equal(f.run().status, 0);
  const args = JSON.parse(readFileSync(f.capture, 'utf8'));
  assert.equal(args[0], '--yes');
  assert.equal(args[1], 'skills@1.7.4');
  assert.equal(args[2], 'add');
  assert.equal(args[3], 'AdeyStudios/skills');
  assert.ok(args.includes('--global'));
  assert.equal(args[args.indexOf('--skill') + 1], '*');
  assert.deepEqual(args.slice(args.indexOf('--agent') + 1, -1), ['claude-code', 'codex']);
  assert.equal(args.at(-1), '--yes');
});

test('help and version do not start an installation', (t) => {
  const f = fixture(t);
  assert.match(f.run(['--help']).stdout, /Usage:/);
  const version = f.run(['--version']);
  assert.equal(version.status, 0);
  assert.equal(version.stdout.trim(), '0.1.0');
  assert.equal(existsSync(f.capture), false);
});

test('unknown input cannot become installer arguments', (t) => {
  const f = fixture(t);
  assert.equal(f.run(['--all']).status, 1);
  assert.equal(existsSync(f.capture), false);
});

test('installation failure is returned rather than reported as success', (t) => {
  const f = fixture(t);
  assert.equal(f.run([], { ADEY_SKILLS_TEST_STATUS: '17' }).status, 17);
});

test('update requests the current GitHub collection through the same installer', (t) => {
  const f = fixture(t);
  assert.equal(f.run(['update']).status, 0);
  const args = JSON.parse(readFileSync(f.capture, 'utf8'));
  assert.ok(args.includes('AdeyStudios/skills'));
});

test('a missing npx produces a useful error', { skip: process.platform === 'win32' }, (t) => {
  const f = fixture(t);
  const result = f.run([], { PATH: '' });
  assert.equal(result.status, 1);
  assert.match(result.stderr, /Could not start the skills installer/);
});
