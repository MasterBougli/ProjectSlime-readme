# ProjectSlime — README animations

Repo **public** dédié aux assets SVG animés / générés pour le README de [ProjectSlime](https://github.com/MasterBougli/ProjectSlime) *(privé)*.

Les workflows GitHub Actions poussent les fichiers sur la branche **`output`**. Le README ProjectSlime les embarque via `raw.githubusercontent.com`.

## Assets générés

| Fichier | Source | Description |
|---------|--------|-------------|
| `snake.svg` | [Platane/snk](https://github.com/Platane/snk) | Grille de contributions « serpent » *(palette slime verte)* |
| `roadmap.svg` | `scripts/generate_roadmap_svg.py` | Progression milestones F0–F7 |
| `activity-graph.svg` | [Ashutosh00710](https://github.com/Ashutosh00710/github-readme-activity-graph) | Activité GitHub 30 jours |

## Embed dans ProjectSlime

```html
<img src="https://raw.githubusercontent.com/MasterBougli/ProjectSlime-readme/output/snake.svg" alt="Snake animation" />
<img src="https://raw.githubusercontent.com/MasterBougli/ProjectSlime-readme/output/roadmap.svg" alt="Roadmap progress" />
<img src="https://raw.githubusercontent.com/MasterBougli/ProjectSlime-readme/output/activity-graph.svg" alt="Activity graph" />
```

## Déclenchement manuel

**Actions** → **Generate README animations** → **Run workflow**

Planifié : toutes les **12 h**.

## Mise à jour roadmap

Éditer `scripts/roadmap.json` puis relancer le workflow (ou push sur `main`).
