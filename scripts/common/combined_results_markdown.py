"""Build a single reviewer-facing Markdown file from generated result summaries.

The benchmark scripts each own their detailed Markdown export.  This helper keeps
those sources canonical while collecting only their summary/aggregate sections
into ``results/combined_summary_tables.md`` for convenient review.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

COMBINED_SUMMARY_FILENAME = "combined_summary_tables.md"

SUPPLEMENTARY_GRN_METRICS = {
    "SPECIFICITY",
    "AUPRC_GAIN",
    "DELTA_AUPRC_VS_BASELINE",
    "LIFT_RATIO_VS_BASELINE",
    "DELTA_PRECISION_AT_K_VS_BASELINE",
    "DELTA_RECALL_AT_K_VS_BASELINE",
}
EXCLUDED_NEGATIVE_PROTOCOLS = {"tf_stratified_1to10"}

# Keep this list explicit so the combined file is stable and does not
# accidentally ingest diagnostic prose from unrelated Markdown files.
SUMMARY_SOURCES: Tuple[Tuple[str, str], ...] = (
    ("Annotation", "annotation/annotation_conference_tables.md"),
    ("Perturbation regression", "perturbation_regression/conference_embedding_aggregate.md"),
    ("GRN embedding-only", "grn_embedding_only/conference_table.md"),
    ("GRN BEELINE full", "grn_beeline_full/conference_table.md"),
)


def _heading_level(line: str) -> int:
    stripped = line.lstrip()
    if not stripped.startswith("#"):
        return 0
    return len(stripped) - len(stripped.lstrip("#"))


def _is_summary_heading(line: str) -> bool:
    normalized = line.strip().lower()
    if not normalized.startswith("#"):
        return False
    return (
        "aggregate mean" in normalized
        or normalized.startswith("## table a.")
        or normalized.startswith("## table c.")
    )


def _demote_heading(line: str) -> str:
    """Demote extracted headings one level so they nest under each source."""
    if _heading_level(line) == 0:
        return line
    return "#" + line


def _extract_summary_sections(md_path: Path) -> List[str]:
    """Extract aggregate/summary sections from a generated Markdown file."""
    if not md_path.exists():
        return []

    lines = md_path.read_text(encoding="utf-8").splitlines()
    sections: List[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not _is_summary_heading(line):
            i += 1
            continue

        start_level = _heading_level(line)
        section: List[str] = [_demote_heading(line)]
        i += 1
        while i < len(lines):
            next_line = lines[i]
            next_level = _heading_level(next_line)
            if next_level and next_level <= start_level:
                break
            section.append(_demote_heading(next_line))
            i += 1
        sections.append("\n".join(section).rstrip())

    return sections


def _split_latent_parts(raw: str) -> List[str]:
    parts: List[str] = []
    current: List[str] = []
    depth = 0
    for char in raw:
        if char == "(":
            depth += 1
        elif char == ")" and depth > 0:
            depth -= 1
        if char == "," and depth == 0:
            parts.append("".join(current).strip())
            current = []
            continue
        current.append(char)
    if current:
        parts.append("".join(current).strip())
    return parts


def _parse_latent_variables(section: str) -> Dict[str, str]:
    for line in section.splitlines():
        if not line.startswith("Latent variables:"):
            continue
        raw = line.split(":", 1)[1]
        out: Dict[str, str] = {}
        for part in _split_latent_parts(raw):
            if "=" not in part:
                continue
            key, value = part.split("=", 1)
            out[key.strip()] = value.strip()
        return out
    return {}


def _is_excluded_from_combined_summary(section: str) -> bool:
    latent = _parse_latent_variables(section)
    metric = latent.get("metric", "").upper()
    protocol = latent.get("negative_protocol", "")
    return metric in SUPPLEMENTARY_GRN_METRICS or protocol in EXCLUDED_NEGATIVE_PROTOCOLS


def _section_heading(section: str) -> str:
    for line in section.splitlines():
        if line.startswith("#"):
            return line
    return ""


def _strip_size_from_heading(heading: str) -> str:
    return (
        heading.replace(" 500-gene", "")
        .replace(" 1000-gene", "")
        .replace(" unknown-size", "")
    )


def _strip_network_group_from_heading(heading: str) -> str:
    return (
        heading.replace(" Specific datasets", " datasets")
        .replace(" Non-Specific datasets", " datasets")
        .replace(" STRING datasets", " datasets")
    )


def _parse_mean_table(section: str) -> Tuple[List[str], Dict[str, str]]:
    lines = section.splitlines()
    for i, line in enumerate(lines):
        if line.strip() != "| Embedding | Mean |":
            continue
        rows: List[str] = []
        values: Dict[str, str] = {}
        for row in lines[i + 2:]:
            if not row.startswith("|"):
                break
            parts = [p.strip() for p in row.strip("|").split("|")]
            if len(parts) != 2:
                continue
            embedding, value = parts
            rows.append(embedding)
            values[embedding] = value
        return rows, values
    return [], {}


def _sort_size(size: str) -> Tuple[bool, object]:
    return (size == "unknown", int(size) if size.isdigit() else size)


def _sort_network_group(group: str) -> Tuple[int, str]:
    order = {"Specific": 0, "Non-Specific": 1, "STRING": 2}
    return (order.get(group, len(order)), group)


def _format_combined_latent(latent: Dict[str, str], sizes: Iterable[str], network_groups: Iterable[str]) -> str:
    ordered_keys = [k for k in latent if k not in {"dataset_size", "network_group"}]
    parts = [f"{k}={latent[k]}" for k in ordered_keys]
    groups = sorted(set(network_groups), key=_sort_network_group)
    if groups:
        parts.append("network_group=" + "/".join(groups))
    parts.append("dataset_size=" + "/".join(sorted(set(sizes), key=_sort_size)))
    return "Latent variables: " + ", ".join(parts)


def _combine_size_split_sections(sections: List[str]) -> List[str]:
    """Combine sibling 500/1000 and Specific/Non-Specific/STRING aggregate sections."""
    passthrough: List[Tuple[int, str]] = []
    grouped: Dict[Tuple[str, Tuple[Tuple[str, str], ...]], Dict[str, object]] = {}

    for order, section in enumerate(sections):
        if _is_excluded_from_combined_summary(section):
            continue

        latent = _parse_latent_variables(section)
        size = latent.get("dataset_size")
        row_order, values = _parse_mean_table(section)
        if not size or not values:
            passthrough.append((order, section))
            continue

        network_group = latent.get("network_group", "")
        heading = _strip_network_group_from_heading(_strip_size_from_heading(_section_heading(section)))
        latent_key = tuple((k, v) for k, v in latent.items() if k not in {"dataset_size", "network_group"})
        key = (heading, latent_key)
        group = grouped.setdefault(
            key,
            {
                "order": order,
                "heading": heading,
                "latent": {k: v for k, v in latent.items() if k not in {"dataset_size", "network_group"}},
                "rows": [],
                "columns": {},
            },
        )
        group["order"] = min(int(group["order"]), order)
        group_rows = group["rows"]
        for row in row_order:
            if row not in group_rows:
                group_rows.append(row)
        group["columns"][(network_group, size)] = values

    combined: List[Tuple[int, str]] = passthrough
    for group in grouped.values():
        column_keys = sorted(
            group["columns"],
            key=lambda item: (_sort_network_group(item[0]) if item[0] else (-1, ""), _sort_size(item[1])),
        )
        sizes = [size for _, size in column_keys]
        network_groups = [network_group for network_group, _ in column_keys if network_group]
        lines = [str(group["heading"]), "", _format_combined_latent(group["latent"], sizes, network_groups), ""]
        labels = [f"{network_group} {size}" if network_group else f"Mean {size}" for network_group, size in column_keys]
        header = "| Embedding | " + " | ".join(labels) + " |"
        sep = "|---|" + "---:|" * len(column_keys)
        lines.extend([header, sep])
        for row in group["rows"]:
            cells = [group["columns"].get(column_key, {}).get(row, "-") for column_key in column_keys]
            lines.append("| " + row + " | " + " | ".join(cells) + " |")
        combined.append((int(group["order"]), "\n".join(lines)))

    return [section for _, section in sorted(combined, key=lambda item: item[0])]


def _iter_source_sections(results_root: Path) -> Iterable[Tuple[str, Path, List[str]]]:
    for source_title, rel_path in SUMMARY_SOURCES:
        md_path = results_root / rel_path
        yield source_title, md_path, _combine_size_split_sections(_extract_summary_sections(md_path))


def update_combined_summary_markdown(results_root: str | Path | None = None) -> Path:
    """Rebuild ``results/combined_summary_tables.md`` from generated summaries.

    The function is intentionally idempotent: every caller rewrites the combined
    file from all currently available source Markdown files instead of appending
    duplicate sections across incremental benchmark runs.
    """
    repo_root = Path(__file__).resolve().parents[2]
    root = Path(results_root) if results_root is not None else repo_root / "results"
    out_path = root / COMBINED_SUMMARY_FILENAME

    lines: List[str] = [
        "# Combined Results Summary Tables",
        "",
        "This file is rebuilt from generated Markdown exports under `results/`.",
        "It collects only aggregate/summary tables so reviewers can inspect cross-dataset results in one place.",
        "",
        f"Last rebuilt: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
    ]

    any_sections = False
    for source_title, md_path, sections in _iter_source_sections(root):
        try:
            rel_display = md_path.relative_to(root)
        except ValueError:
            rel_display = md_path
        lines.extend([f"## {source_title}", "", f"Source: `{rel_display}`", ""])
        if sections:
            any_sections = True
            for section in sections:
                lines.extend([section, ""])
        else:
            lines.extend(["_No aggregate/summary sections found yet._", ""])

    if not any_sections:
        lines.append("_No aggregate/summary sections were available from the configured sources._")
        lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return out_path


if __name__ == "__main__":
    print(update_combined_summary_markdown())
