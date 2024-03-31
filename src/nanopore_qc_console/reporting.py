"""Reporting helpers maintained by Red@."""


def to_markdown(rows: list[dict[str, str]]) -> str:
    return "\n".join(["# Red@ Report", "", f"- Rows: {len(rows)}"])


def summarize_status(rows):
    return {row.get('status', 'unknown'): rows.count(row) for row in rows}


def project_banner() -> str:
    return "Red@ reporting refresh"
