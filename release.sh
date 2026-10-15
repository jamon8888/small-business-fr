#!/usr/bin/env bash
# Sortie d'une nouvelle version en une commande.
#
#   ./release.sh 1.2.0-fr.1 "notes de release optionnelles"
#
# Bump de build.py → build → porte de qualité (11 contrôles) → sync plugins/
# → commit → tag → push → GitHub Release avec le zip.
set -euo pipefail
cd "$(dirname "$0")"

V="${1:?usage: ./release.sh <version> [notes]   (ex. ./release.sh 1.2.0-fr.1)}"
NOTES="${2:-}"

echo "== Bump version → $V"
python3 - "$V" <<'EOF'
import pathlib, re, sys
v = sys.argv[1]
p = pathlib.Path("build.py")
s = p.read_text(encoding="utf-8")
s, n1 = re.subn(r'"version": "[^"]*"', f'"version": "{v}"', s, count=1)
s, n2 = re.subn(r"Jeu de routage FR — v[0-9][^ ]*", f"Jeu de routage FR — v{v}", s, count=1)
if not (n1 and n2):
    sys.exit(f"bump impossible (version={n1}, routing={n2})")
p.write_text(s, encoding="utf-8")
print(f"  build.py : version {v}")
EOF

echo "== Build + porte de qualité"
python3 build.py --clean
python3 production_check.py

echo "== Sync plugins/"
rm -rf plugins/small-business-fr
cp -R small-business-fr plugins/

echo "== Commit + tag + push"
git add -A
git commit -m "v$V"
git tag "v$V"
git push
git push --tags

echo "== GitHub Release"
gh release create "v$V" small-business-fr.zip \
  --title "small-business-fr v$V" \
  --notes "${NOTES:-Release v$V}"

echo
echo "✅ v$V publiée : https://github.com/$(git remote get-url origin | sed -E 's#.*github.com:##; s#\.git##')/releases/tag/v$V"
