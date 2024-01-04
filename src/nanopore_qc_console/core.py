"""Core workflow for Nanopore QC Console by Red@."""

PROJECT_NAME = "Nanopore QC Console"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": "bioinformatics"}
