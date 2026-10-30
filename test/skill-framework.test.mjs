import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, readdirSync, statSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const skillRoot = join(root, 'skills');

test('skill directories have valid basic metadata and match their names', () => {
  const folders = readdirSync(skillRoot).filter(name => statSync(join(skillRoot, name)).isDirectory());
  assert.ok(folders.length >= 9, 'Expected all existing skills plus the three founder skills');
  for (const folder of folders) {
    assert.match(folder, /^[a-z]+(?:-[a-z]+)*$/);
    const body = readFileSync(join(skillRoot, folder, 'SKILL.md'), 'utf8');
    assert.match(body, /^---\n[\s\S]*?\n---\n/, folder + ' needs YAML frontmatter');
    const metadata = body.slice(4, body.indexOf('\n---', 4));
    assert.ok(metadata.split('\n').includes('name: ' + folder), folder + ' name must match its directory');
    assert.match(metadata, /^description:\s*.+/m, folder + ' needs a meaningful description');
  }
});

test('new founder skills follow the documented Research / Execute / Verify workflow', () => {
  const framework = readFileSync(join(root, 'SKILL-FRAMEWORK.md'), 'utf8');
  assert.match(framework, /## When creating or improving a skill/);
  assert.match(framework, /## When executing a skill/);
  for (const skill of ['founder-os', 'customer-discovery', 'idea-validation']) {
    const body = readFileSync(join(skillRoot, skill, 'SKILL.md'), 'utf8');
    for (const phase of ['Research', 'Execute', 'Verify']) {
      assert.match(body, new RegExp('^## ' + phase + '$', 'm'), skill + ' missing ' + phase);
    }
    assert.match(body, /working draft/i, skill + ' should not claim to be proven');
  }
});
