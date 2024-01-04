from setuptools import setup

setup(
    name="reda-2024-nanopore-qc-console",
    version="0.1.0",
    description="QC console for nanopore runs with markdown reports and threshold summaries.",
    author="Red@",
    packages=["nanopore_qc_console"],
    package_dir={"": "src"},
)
