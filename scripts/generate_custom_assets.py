#!/usr/bin/env python3
"""Generate custom SVG assets for ProjectSlime README gallery."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config.json"
ROADMAP_PATH = ROOT / "roadmap.json"
DIST = Path("dist")


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def ensure_dirs() -> None:
    for folder in (
        "01-contributions",
        "02-stats",
        "03-headers",
        "04-text",
        "05-project",
        "06-badges",
    ):
        (DIST / folder).mkdir(parents=True, exist_ok=True)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path}")


def generate_banner(config: dict) -> None:
    c = config["colors"]
    title = config["project_name"]
    tagline = config["tagline"]
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="140" viewBox="0 0 900 140" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{c['bg']}"/>
      <stop offset="50%" stop-color="{c['panel']}"/>
      <stop offset="100%" stop-color="#0a2f14"/>
    </linearGradient>
    <linearGradient id="glow" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{c['slime']}" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="{c['sky']}" stop-opacity="0.05"/>
    </linearGradient>
  </defs>
  <rect width="900" height="140" rx="16" fill="url(#bg)"/>
  <rect width="900" height="140" rx="16" fill="url(#glow)"/>
  <circle cx="72" cy="70" r="34" fill="{c['slime']}" opacity="0.25"/>
  <circle cx="72" cy="70" r="22" fill="{c['slime']}" opacity="0.55"/>
  <text x="130" y="62" fill="{c['text']}" font-family="Segoe UI, sans-serif" font-size="30" font-weight="700">{title}</text>
  <text x="130" y="96" fill="{c['muted']}" font-family="Segoe UI, sans-serif" font-size="16">{tagline}</text>
  <rect x="20" y="118" width="860" height="4" rx="2" fill="{c['border']}"/>
  <rect x="20" y="118" width="280" height="4" rx="2" fill="{c['slime']}"/>
</svg>
"""
    write(DIST / "03-headers" / "banner-slime.svg", svg)


def generate_capsule_static(config: dict) -> None:
    c = config["colors"]
    title = config["project_name"]
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="100" viewBox="0 0 900 100" role="img">
  <defs>
    <linearGradient id="cap" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{c['slime']}"/>
      <stop offset="100%" stop-color="{c['bg']}"/>
    </linearGradient>
  </defs>
  <rect width="900" height="100" rx="50" fill="url(#cap)"/>
  <text x="450" y="58" text-anchor="middle" fill="{c['text']}" font-family="Segoe UI, sans-serif" font-size="28" font-weight="700">{title}</text>
</svg>
"""
    write(DIST / "03-headers" / "capsule-gradient.svg", svg)


def generate_wave_separator(config: dict) -> None:
    c = config["colors"]
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="60" viewBox="0 0 900 60" preserveAspectRatio="none" role="img">
  <path d="M0,30 C150,60 300,0 450,30 C600,60 750,0 900,30 L900,60 L0,60 Z" fill="{c['slime']}" opacity="0.35"/>
  <path d="M0,40 C200,10 400,50 600,35 C750,25 850,45 900,38 L900,60 L0,60 Z" fill="{c['sky']}" opacity="0.2"/>
</svg>
"""
    write(DIST / "03-headers" / "wave-separator.svg", svg)


def generate_roadmap(config_path: Path = ROADMAP_PATH) -> None:
    from generate_roadmap_svg import build_svg, load_config as load_roadmap

    config = load_roadmap()
    write(DIST / "05-project" / "roadmap.svg", build_svg(config))


def generate_milestones_progress() -> None:
    roadmap = load_json(ROADMAP_PATH)
    colors = roadmap["colors"]
    milestones = roadmap["milestones"]
    done = sum(1 for m in milestones if m["status"] == "done")
    active = sum(1 for m in milestones if m["status"] == "active")
    total = len(milestones)
    pct = int((done + active * 0.5) / total * 100)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="80" viewBox="0 0 900 80" role="img">
  <rect width="900" height="80" rx="12" fill="{colors['bg']}"/>
  <text x="24" y="28" fill="{colors['text']}" font-family="Segoe UI, sans-serif" font-size="14" font-weight="600">MVP Progress</text>
  <text x="876" y="28" text-anchor="end" fill="{colors['accent']}" font-family="Segoe UI, sans-serif" font-size="14" font-weight="700">{pct}%</text>
  <rect x="24" y="42" width="852" height="18" rx="9" fill="{colors['todo']}"/>
  <rect x="24" y="42" width="{int(852 * pct / 100)}" height="18" rx="9" fill="{colors['done']}"/>
  <text x="450" y="72" text-anchor="middle" fill="{colors['text']}" font-family="Segoe UI, sans-serif" font-size="11">{done} done · {active} active · {total - done - active} todo</text>
</svg>
"""
    write(DIST / "05-project" / "milestones-progress.svg", svg)


def generate_tech_stack(config: dict) -> None:
    c = config["colors"]
    items = config["tech_stack"]
    width = 900
    chip_w = 150
    gap = 12
    start_x = (width - (len(items) * chip_w + (len(items) - 1) * gap)) / 2
    chips = []
    for index, label in enumerate(items):
        x = start_x + index * (chip_w + gap)
        chips.append(
            f'<rect x="{x}" y="24" width="{chip_w}" height="36" rx="18" fill="{c["panel"]}" stroke="{c["slime"]}" stroke-width="1.5"/>'
        )
        chips.append(
            f'<text x="{x + chip_w / 2}" y="47" text-anchor="middle" fill="{c["text"]}" font-family="Segoe UI, sans-serif" font-size="12" font-weight="600">{label}</text>'
        )
    body = "\n  ".join(chips)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="84" viewBox="0 0 {width} 84" role="img">
  <rect width="{width}" height="84" rx="12" fill="{c['bg']}"/>
  {body}
</svg>
"""
    write(DIST / "05-project" / "tech-stack.svg", svg)


def generate_shields_row(config: dict) -> None:
    c = config["colors"]
    badges = [
        ("UE 5.7", c["slime"]),
        ("C++", c["sky"]),
        ("Steam EA", "#1b2838"),
        ("Private", "#da3633"),
        ("Silvanterra", c["forest"]),
    ]
    x = 20
    parts = []
    for label, color in badges:
        w = 24 + len(label) * 8
        parts.append(f'<rect x="{x}" y="20" width="{w}" height="28" rx="14" fill="{color}"/>')
        parts.append(
            f'<text x="{x + w / 2}" y="39" text-anchor="middle" fill="{c["text"]}" font-family="Segoe UI, sans-serif" font-size="11" font-weight="700">{label}</text>'
        )
        x += w + 10
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="68" viewBox="0 0 900 68" role="img">
  <rect width="900" height="68" rx="12" fill="{c['bg']}"/>
  {" ".join(parts)}
</svg>
"""
    write(DIST / "06-badges" / "shields-row.svg", svg)


def generate_typing_static(config: dict) -> None:
    c = config["colors"]
    lines = ["Predator Slime", "Unreal Engine 5.7", "Silvanterra · MVP Forêt"]
    y = 34
    text_nodes = []
    for line in lines:
        text_nodes.append(
            f'<text x="24" y="{y}" fill="{c["slime"]}" font-family="Consolas, monospace" font-size="18" font-weight="600">{line}</text>'
        )
        y += 28
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="420" height="110" viewBox="0 0 420 110" role="img">
  <rect width="420" height="110" rx="10" fill="{c['bg']}" stroke="{c['border']}" stroke-width="1"/>
  {" ".join(text_nodes)}
  <rect x="390" y="18" width="3" height="74" fill="{c['slime']}">
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
  </rect>
</svg>
"""
    write(DIST / "04-text" / "typing-static.svg", svg)


def generate_feature_cards() -> None:
    roadmap = load_json(ROADMAP_PATH)
    c = roadmap["colors"]
    features = [
        ("Corps = inventaire", "Absorption ressources"),
        ("Predator", "Feux follets 30s"),
        ("Mimétisme", "5 espèces EA"),
        ("Sophia", "Guide sarcastique"),
    ]
    cards = []
    for index, (title, subtitle) in enumerate(features):
        x = 20 + index * 215
        cards.append(f'<rect x="{x}" y="16" width="200" height="72" rx="10" fill="{c["panel"]}" stroke="{c["accent"]}" stroke-width="1"/>')
        cards.append(
            f'<text x="{x + 16}" y="44" fill="{c["text"]}" font-family="Segoe UI, sans-serif" font-size="13" font-weight="700">{title}</text>'
        )
        cards.append(
            f'<text x="{x + 16}" y="66" fill="#8b949e" font-family="Segoe UI, sans-serif" font-size="11">{subtitle}</text>'
        )
    # fix muted color - roadmap colors don't have muted, use text with opacity via separate fill
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="104" viewBox="0 0 900 104" role="img">
  <rect width="900" height="104" rx="12" fill="{c['bg']}"/>
  {" ".join(cards)}
</svg>
"""
    write(DIST / "05-project" / "feature-cards.svg", svg)


def main() -> None:
    config = load_json(CONFIG_PATH)
    ensure_dirs()
    generate_banner(config)
    generate_capsule_static(config)
    generate_wave_separator(config)
    generate_roadmap()
    generate_milestones_progress()
    generate_tech_stack(config)
    generate_shields_row(config)
    generate_typing_static(config)
    generate_feature_cards()


if __name__ == "__main__":
    main()
