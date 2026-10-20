#!/usr/bin/env python3
"""Check the template files needed for portable project creation."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "SKILL.md", "agents/openai.yaml", "scripts/create_project.py",
    "references/experiment.md", "references/humanities.md", "references/beamer.md", "references/delivery.md",
    "assets/templates/experiment/main.tex", "assets/templates/experiment/images/logo.png",
    "assets/templates/experiment/使用手册.pdf",
    "assets/templates/humanities/report.tex", "assets/templates/humanities/使用手册.pdf",
    "assets/templates/humanities/fonts/simsun.ttc",
    "assets/templates/humanities/fonts/simhei.ttf",
    "assets/templates/humanities/fonts/STZHONGS.TTF",
    "assets/templates/beamer/main.tex", "assets/templates/beamer/Beamer模板使用手册.pdf",
    "assets/templates/beamer/fonts/SourceHanSansCN-Regular.otf",
    "assets/templates/beamer/fonts/SourceHanSansCN-Bold.otf",
    "assets/templates/beamer/fonts/LICENSE.txt",
)


def main():
    missing = [name for name in REQUIRED if not (ROOT / name).is_file() or (ROOT / name).stat().st_size == 0]
    if missing:
        print("Missing or empty required files:\n" + "\n".join(missing), file=sys.stderr)
        return 1
    print(f"Validated {len(REQUIRED)} required skill and template assets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
