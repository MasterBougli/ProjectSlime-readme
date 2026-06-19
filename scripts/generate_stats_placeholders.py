#!/usr/bin/env python3
"""Placeholder SVGs when external stats APIs are unavailable."""

from pathlib import Path

DIST = Path("dist/02-stats")

TEMPLATES = {
    "stats-card.svg": ("GitHub Stats", "Repos · Commits · PRs · Issues"),
    "streak.svg": ("Contribution Streak", "Current · Longest · Total"),
    "top-langs.svg": ("Top Languages", "C++ · C# · Python · …"),
    "trophy.svg": ("GitHub Trophies", "Achievements preview"),
}


def placeholder(title: str, subtitle: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="420" height="120" viewBox="0 0 420 120" role="img">
  <rect width="420" height="120" rx="10" fill="#0d1117" stroke="#30363d"/>
  <text x="210" y="48" text-anchor="middle" fill="#7ee787" font-family="Segoe UI,sans-serif" font-size="16" font-weight="700">{title}</text>
  <text x="210" y="76" text-anchor="middle" fill="#8b949e" font-family="Segoe UI,sans-serif" font-size="12">{subtitle}</text>
  <text x="210" y="100" text-anchor="middle" fill="#58a6ff" font-family="Segoe UI,sans-serif" font-size="10">Live: github-readme-stats.vercel.app</text>
</svg>
"""


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    for filename, (title, subtitle) in TEMPLATES.items():
        path = DIST / filename
        if not path.exists() or path.stat().st_size < 100:
            path.write_text(placeholder(title, subtitle), encoding="utf-8")
            print(f"Placeholder {path}")


if __name__ == "__main__":
    main()
