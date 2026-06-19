#!/usr/bin/env python3
"""100% custom SVG animations for ProjectSlime — no external APIs."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
DIST = Path("dist/07-custom")
C = CONFIG["colors"]


def write(name: str, svg: str) -> None:
    path = DIST / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(svg.strip() + "\n", encoding="utf-8")
    print(f"Wrote {path}")


def slime_blob() -> None:
    write(
        "slime-blob.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200" role="img" aria-label="Slime blob">
  <defs>
    <radialGradient id="g" cx="40%" cy="35%" r="65%">
      <stop offset="0%" stop-color="{C['slime']}" stop-opacity="0.95"/>
      <stop offset="70%" stop-color="{C['forest']}" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="{C['bg']}"/>
    </radialGradient>
  </defs>
  <ellipse cx="100" cy="108" rx="72" ry="64" fill="url(#g)">
    <animate attributeName="rx" values="72;78;70;72" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="ry" values="64;58;66;64" dur="3s" repeatCount="indefinite"/>
  </ellipse>
  <ellipse cx="78" cy="88" rx="14" ry="18" fill="{C['bg']}" opacity="0.35"/>
  <circle cx="118" cy="92" r="8" fill="{C['bg']}" opacity="0.5">
    <animate attributeName="cy" values="92;90;92" dur="2s" repeatCount="indefinite"/>
  </circle>
</svg>""",
    )


def mana_bar() -> None:
    write(
        "mana-bar.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="360" height="56" viewBox="0 0 360 56" role="img" aria-label="Mana bar">
  <rect width="360" height="56" rx="10" fill="{C['bg']}" stroke="{C['border']}"/>
  <text x="16" y="22" fill="{C['text']}" font-family="Segoe UI,sans-serif" font-size="12" font-weight="600">Mana</text>
  <rect x="16" y="30" width="328" height="14" rx="7" fill="{C['panel']}"/>
  <rect x="16" y="30" width="328" height="14" rx="7" fill="{C['sky']}">
    <animate attributeName="width" values="328;260;328;200;328" dur="6s" repeatCount="indefinite"/>
  </rect>
  <circle cx="300" cy="37" r="5" fill="{C['slime']}" opacity="0.8">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="1.2s" repeatCount="indefinite"/>
  </circle>
</svg>""",
    )


def forest_silhouette() -> None:
    write(
        "forest-silhouette.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="120" viewBox="0 0 900 120" role="img" aria-label="Silvanterra forest">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0a1628"/>
      <stop offset="100%" stop-color="{C['bg']}"/>
    </linearGradient>
  </defs>
  <rect width="900" height="120" fill="url(#sky)"/>
  <g fill="{C['forest']}" opacity="0.85">
    <polygon points="40,120 70,45 100,120"><animateTransform attributeName="transform" type="rotate" values="0 70 120;-1 70 120;0 70 120" dur="4s" repeatCount="indefinite"/></polygon>
    <polygon points="120,120 155,30 190,120"/>
    <polygon points="220,120 250,50 280,120"><animateTransform attributeName="transform" type="rotate" values="0 250 120;1.5 250 120;0 250 120" dur="5s" repeatCount="indefinite"/></polygon>
    <polygon points="320,120 360,35 400,120"/>
    <polygon points="450,120 480,55 510,120"/>
    <polygon points="560,120 600,25 640,120"><animateTransform attributeName="transform" type="rotate" values="0 600 120;-1 600 120;0 600 120" dur="4.5s" repeatCount="indefinite"/></polygon>
    <polygon points="680,120 715,40 750,120"/>
    <polygon points="780,120 815,50 850,120"/>
  </g>
  <rect y="100" width="900" height="20" fill="{C['bg']}"/>
  <text x="450" y="18" text-anchor="middle" fill="{C['slime']}" font-family="Segoe UI,sans-serif" font-size="13" font-weight="600">Silvanterra</text>
</svg>""",
    )


def predator_wisp() -> None:
    write(
        "predator-wisp.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="420" height="100" viewBox="0 0 420 100" role="img" aria-label="Predator wisp">
  <rect width="420" height="100" rx="12" fill="{C['bg']}" stroke="{C['border']}"/>
  <text x="210" y="24" text-anchor="middle" fill="{C['text']}" font-size="12" font-weight="600">Predator — Feu follet</text>
  <g>
    <circle r="10" fill="{C['sky']}" opacity="0.9">
      <animateMotion dur="4s" repeatCount="indefinite" path="M60,60 C120,20 180,90 240,55 S360,30 360,60"/>
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle r="7" fill="{C['slime']}" opacity="0.8">
      <animateMotion dur="3.2s" repeatCount="indefinite" path="M80,70 C140,40 200,80 260,50 S340,65 340,45"/>
    </circle>
    <circle r="5" fill="#a371f7" opacity="0.7">
      <animateMotion dur="2.8s" repeatCount="indefinite" path="M100,50 C160,70 220,35 280,65 S360,55 360,40"/>
    </circle>
  </g>
</svg>""",
    )


def contrib_grid_custom() -> None:
    cells = []
    colors = [C["panel"], C["forest"], C["slime"], C["sky"], "#1a3a2a"]
    for row in range(7):
        for col in range(52):
            shade = colors[(row + col) % len(colors)]
            opacity = 0.35 + ((row * col) % 5) * 0.12
            cells.append(
                f'<rect x="{col * 15}" y="{row * 15}" width="13" height="13" rx="2" fill="{shade}" opacity="{opacity:.2f}"/>'
            )
    body = "\n  ".join(cells)
    write(
        "contrib-grid-custom.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="800" height="120" viewBox="0 0 800 120" role="img" aria-label="Contributions stylisées">
  <rect width="800" height="120" rx="10" fill="{C['bg']}"/>
  <text x="16" y="18" fill="{C['text']}" font-size="11" font-weight="600">Activité dev — style slime</text>
  <g transform="translate(16,28) scale(0.85)">
  {body}
  </g>
</svg>""",
    )


def trophy_custom() -> None:
    trophies = [
        ("Commits", C["slime"]),
        ("UE", C["sky"]),
        ("MVP", C["forest"]),
        ("F0", "#a371f7"),
    ]
    parts = []
    for i, (label, color) in enumerate(trophies):
        x = 24 + i * 100
        parts.append(f'<rect x="{x}" y="28" width="88" height="64" rx="10" fill="{C["panel"]}" stroke="{color}" stroke-width="2"/>')
        parts.append(f'<text x="{x + 44}" y="58" text-anchor="middle" fill="{color}" font-size="20">🏆</text>')
        parts.append(f'<text x="{x + 44}" y="78" text-anchor="middle" fill="{C["text"]}" font-size="10" font-weight="600">{label}</text>')
    write(
        "trophy-custom.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="440" height="110" viewBox="0 0 440 110" role="img" aria-label="Achievements slime">
  <rect width="440" height="110" rx="12" fill="{C['bg']}"/>
  <text x="220" y="20" text-anchor="middle" fill="{C['text']}" font-size="12" font-weight="600">Achievements ProjectSlime</text>
  {" ".join(parts)}
</svg>""",
    )


def typing_custom() -> None:
    lines = ["Predator Slime", "Unreal Engine 5.7", "Silvanterra · MVP"]
    texts = []
    for i, line in enumerate(lines):
        texts.append(
            f'<text x="24" y="{40 + i * 26}" fill="{C["slime"]}" font-family="Consolas,monospace" font-size="16" font-weight="600" opacity="0">'
            f'{line}'
            f'<animate attributeName="opacity" values="0;1;1;0" dur="9s" begin="{i * 3}s" repeatCount="indefinite"/>'
            f"</text>"
        )
    write(
        "typing-custom.svg",
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="400" height="110" viewBox="0 0 400 110" role="img" aria-label="Typing custom">
  <rect width="400" height="110" rx="10" fill="{C['bg']}" stroke="{C['border']}"/>
  {"".join(texts)}
  <rect x="370" y="24" width="3" height="62" fill="{C['slime']}">
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
  </rect>
</svg>""",
    )


def main() -> None:
    slime_blob()
    mana_bar()
    forest_silhouette()
    predator_wisp()
    contrib_grid_custom()
    trophy_custom()
    typing_custom()


if __name__ == "__main__":
    main()
