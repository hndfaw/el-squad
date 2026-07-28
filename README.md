# El Squad — Retro Rescue 🎀

A retro synthwave platformer starring **Elara**, **Helia**, and **Ellen** — three
pixel-art heroes with fully frame-based animation (idle, 3-frame run cycle, jump,
fall, land, hurt, and victory poses).

## Play

- **Pick your hero** — each has her own feel (Elara is speedy, Helia balanced,
  Ellen has the floatiest super jump).
- **Round 1: Sunset Meadow** — run right, jump platforms, collect 32 stars,
  bounce off slimes, reach the GOAL castle.
- **Round 2: Midnight Ice** — a frozen night world with red spikes: touch one
  and you're knocked back and lose a star.
- **Power-ups** — eat a glowing orb for an 8-second boost:
  pink **Moon Jumps**, yellow **Super Speed**, cyan **Bubble Shield**
  (spike immunity).
- No fail state: falling just respawns you at the last checkpoint.

### Controls

| Input    | Action |
|----------|--------|
| ← → / A D | Run (manual mode) |
| Space / ↑ / W | Jump — **hold for a high jump, tap for a hop** |
| Phone    | **Auto-run** is on by default: tap anywhere to jump |
| AUTO/MANUAL button | Switch modes any time |
| ♪ button | Mute |

On phones the world fills the whole screen and characters render larger.
Sound starts on your first tap (on iPhone, make sure the ring/silent switch
isn't on silent).

## Deploy on Vercel

This is a fully static site — `index.html` is the entire game, no build step
and no dependencies.

1. Go to [vercel.com/new](https://vercel.com/new) and import this repository.
2. Framework preset: **Other**. Leave build command and output directory empty.
3. Deploy — your game is live at `https://<project>.vercel.app`.

(Or from the CLI: `npx vercel --prod` in this folder.)

## Development

- `src/el-squad-2d.html` — the game template: all logic, rendering, audio.
- `src/sprites.js` — character animation frames as base64 PNG data URIs,
  extracted from the original green-screen sprite sheets.
- `python3 build.py` — rebuilds `index.html` from the two sources.

Everything renders on a single `<canvas>`: pixel-font text, parallax synthwave
background, chiptune music via WebAudio — no external assets or libraries.
