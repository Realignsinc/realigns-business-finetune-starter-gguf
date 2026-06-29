#!/usr/bin/env python3
"""Prepare business instruction JSONL from downloaded raw datasets."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / os.getenv("RAW_DATA_DIR", "data/raw")
PROCESSED_DIR = ROOT / os.getenv("PROCESSED_DATA_DIR", "data/processed")
OUTPUT_PATH = PROCESSED_DIR / "business_train.jsonl"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            value = json.loads(line)
            if isinstance(value, dict):
                rows.append(value)
    return rows


def compact_value(value: Any, max_len: int = 500) -> str:
    text = str(value).replace("\n", " ").strip()
    return text[:max_len]


def row_to_instruction(row: dict[str, Any], source_name: str) -> dict[str, str]:
    visible_items = []
    for key, value in row.items():
        if value is None or value == "":
            continue
        visible_items.append(f"{key}: {compact_value(value)}")

    input_text = "\n".join(visible_items[:20])

    return {
        "instruction": "Analyze this business dataset record and provide a concise business summary.",
        "input": f"Source: {source_name}\n{input_text}",
        "output": "This record contains business-related information. Review the source fields and summarize the key commercial, economic, or operational signal for decision-making."
    }


def main() -> None:
    if not RAW_DIR.exists():
        raise SystemExit(f"Raw data folder not found: {RAW_DIR}. Run scripts/fetch_hf_datasets.py first.")

    records: list[dict[str, str]] = []

    for path in sorted(RAW_DIR.glob("**/*.jsonl")):
        source_name = path.parent.name
        rows = read_jsonl(path)
        for row in rows:
            records.append(row_to_instruction(row, source_name))

    if not records:
        raise SystemExit("No records found. Run fetch script first or check dataset config.")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Prepared {len(records)} instruction records at {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
