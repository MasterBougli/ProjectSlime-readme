#!/usr/bin/env python3
"""Generate roadmap-progress SVG for ProjectSlime README."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "roadmap.json"
OUT = Path("dist/roadmap.svg")


def load_config() -> dict:
    with CONFIG.open(encoding="utf-8") as handle:
        return json.load(handle)


def status_color(colors: dict, status: str) -> str:
    return colors.get(status, colors["todo"])


def build_svg(config: dict) -> str:
    milestones = config["milestones"]
    colors = config["colors"]
    title = config.get("title", "Roadmap")

    width = 820
    height = 120
    node_w = 88
    gap = 8
    start_x = 20
    y_node = 52

    parts: list[str] = []
    for index, milestone in enumerate(milestones):
        x = start_x + index * (node_w + gap)
        fill = status_color(colors, milestone["status"])
        stroke = colors["accent"] if milestone["status"] == "active" else fill
        stroke_width = "2" if milestone["status"] == "active" else "1"

        if index > 0:
            prev_x = start_x + (index - 1) * (node_w + gap) + node_w
            line_y = y_node + 18
            parts.append(
                f'<line x1="{prev_x}" y1="{line_y}" x2="{x}" y2="{line_y}" '
                f'stroke="{colors["accent"]}" stroke-width="2" opacity="0.45"/>'
            )

        parts.append(
            f'<rect x="{x}" y="{y_node}" width="{node_w}" height="36" rx="8" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
        )
        parts.append(
            f'<text x="{x + node_w / 2}" y="{y_node + 22}" text-anchor="middle" '
            f'fill="{colors["text"]}" font-family="Segoe UI, sans-serif" '
            f'font-size="11" font-weight="600">{milestone["id"]}</text>'
        )

    body = "\n  ".join(parts)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{title}">
  <rect width="100%" height="100%" fill="{colors['bg']}" rx="12"/>
  <text x="{width / 2}" y="28" text-anchor="middle" fill="{colors['text']}" font-family="Segoe UI, sans-serif" font-size="14" font-weight="700">{title}</text>
  {body}
</svg>
"""


def main() -> None:
    config = load_config()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_svg(config), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
