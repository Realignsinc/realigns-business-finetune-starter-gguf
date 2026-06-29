#!/usr/bin/env python3
"""Validate instruction JSONL before training."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = ROOT / "data" / "processed" / "business_train.jsonl"
REQUIRED_KEYS = {"instruction", "input", "output"}


def main() -> None:
    if not DATASET_PATH.exists():
        print(f"Dataset not found: {DATASET_PATH}")
        return

    total = 0
    problems = 0

    with DATASET_PATH.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            total += 1
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                print(f"Line {line_number}: JSON problem: {exc}")
                problems += 1
                continue
            missing = REQUIRED_KEYS - set(row.keys())
            if missing:
                print(f"Line {line_number}: missing keys {sorted(missing)}")
                problems += 1
                continue
            for key in REQUIRED_KEYS:
                value = row.get(key)
                if not isinstance(value, str) or not value.strip():
                    print(f"Line {line_number}: empty field {key}")
                    problems += 1

    print(f"Checked {total} records. Problems: {problems}")
    if problems == 0:
        print("Dataset validation passed.")


if __name__ == "__main__":
    main()
