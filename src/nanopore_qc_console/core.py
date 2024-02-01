"""Core workflow for Nanopore QC Console by Red@."""

PROJECT_NAME = "Nanopore QC Console"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
