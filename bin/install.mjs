#!/usr/bin/env node

import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';

const args = process.argv.slice(2);

if (args.length === 1 && ['--help', '-h'].includes(args[0])) {
  console.log(`Adey Studios Skills

Usage: adey-skills [install | update | --help | --version]

Installs all Adey Studios skills globally for Claude Code and Codex.
Install and update both fetch the current collection from GitHub.
Uses skills CLI 1.7.4; requires Node.js 22.20+ and network access.
No skill or agent selection menus. Restart your agent session afterwards.`);
  process.exit(0);
}

if (args.length === 1 && ['--version', '-v'].includes(args[0])) {
  const { version } = JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8'));
  console.log(version);
  process.exit(0);
}

if (args.length > 1 || (args.length === 1 && !['install', 'update'].includes(args[0]))) {
  console.error('Unknown argument. Run adey-skills --help for usage.');
  process.exit(1);
}

console.log('Installing the latest Adey Studios skills for Claude Code and Codex…');

// Arguments are fixed, not interpolated from user input. Windows needs a shell
// to launch npx.cmd; POSIX runs npx directly without shell expansion of '*'.
const result = spawnSync('npx', [
  '--yes', 'skills@1.7.4', 'add', 'AdeyStudios/skills',
  '--global', '--skill', '*', '--agent', 'claude-code', 'codex', '--yes',
], { stdio: 'inherit', shell: process.platform === 'win32' });

if (result.error) {
  console.error(`Could not start the skills installer: ${result.error.message}`);
  process.exit(1);
}

if (result.signal) {
  process.kill(process.pid, result.signal);
} else {
  process.exit(result.status ?? 1);
}
