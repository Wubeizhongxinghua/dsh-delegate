#!/usr/bin/env python3
"""Compose a headless profile from the user's existing plugin profile."""
import json, os, pathlib, shutil, sys
home = pathlib.Path(os.environ.get('DSH_HOME', pathlib.Path.home() / '.dsh')).expanduser()
source_name = os.environ.get('DSH_DELEGATE_SOURCE_PROFILE', 'desktop')
if not source_name or '/' in source_name or source_name in ('.', '..', 'codex-delegate'):
    sys.exit('Invalid DSH_DELEGATE_SOURCE_PROFILE.')
src = home / 'profiles' / source_name
dst = home / 'profiles' / 'codex-delegate'
if not (src / 'package.json').is_file():
    sys.exit('Source dsh profile not found. Set DSH_DELEGATE_SOURCE_PROFILE to an installed profile.')
if dst.exists() and not (dst / '.dsh-delegate-managed').is_file():
    sys.exit('Refusing to overwrite an existing codex-delegate profile.')
dst.mkdir(parents=True, exist_ok=True)
(dst / '.dsh-delegate-managed').touch()
manifest = json.loads((src / 'package.json').read_text())
bundles = manifest['dsh']['profile']['bundles']
bundles = [b for b in bundles if b not in ('@deepseek-ai/dsh-web-app', '@deepseek-ai/dsh-headless', '@deepseek-harness-tui/dsh-tui', '@deepseek-ai/dsh-acp-app', '@deepseek-ai/dsh-sdk-app', '@deepseek-ai/dsh-sdk-minimal')]
bundles.append('@deepseek-ai/dsh-headless')
manifest['dsh']['profile']['bundles'] = bundles
manifest['name'] = 'dsh-profile-codex-delegate'
(dst / 'package.json').write_text(json.dumps(manifest, indent=2) + '\n')
(dst / 'cordis.yml').write_text('[]\n')
if (src / 'cordis.patch.yml').is_file():
    shutil.copyfile(src / 'cordis.patch.yml', dst / 'cordis.patch.yml')
else:
    (dst / 'cordis.patch.yml').write_text('[]\n')
link = dst / 'node_modules'
if link.is_symlink():
    link.unlink()
elif link.exists():
    sys.exit('Refusing to replace non-symlink node_modules in managed profile.')
if (src / 'node_modules').exists():
    link.symlink_to((src / 'node_modules').resolve(), target_is_directory=True)
