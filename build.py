#!/usr/bin/env python3
"""Build index.html by splicing the sprite data into the game template.

The game is a single self-contained HTML file. `src/el-squad-2d.html` is the
template (all game code, no sprite data); `src/sprites.js` holds the character
frames as base64 data URIs. This script combines them into `index.html`.
"""
import pathlib

root = pathlib.Path(__file__).parent
template = (root / "src" / "el-squad-2d.html").read_text()
sprites = (root / "src" / "sprites.js").read_text()
out = template.replace("<script>", "<script>\n" + sprites + "</script>\n<script>", 1)
(root / "index.html").write_text(out)
print(f"built index.html ({len(out) // 1024} KB)")
