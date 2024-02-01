import argparse
from nanopore_qc_console.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="QC console for nanopore runs with markdown reports and threshold summaries.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
