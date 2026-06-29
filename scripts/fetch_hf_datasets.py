#!/usr/bin/env python3
"""Fetch Realigns datasets from Hugging Face.

This script downloads configured datasets into data/raw/ without committing
large dataset files to GitHub.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

import yaml
from datasets import load_dataset
from tqdm import tqdm

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "configs" / "datasets.yaml"


def load_config() -> dict[str, Any]:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> None:
    config = load_config()
    output_root = ROOT / str(config.get("default_output", "data/raw"))
    hf_token = os.getenv("HF_TOKEN") or None

    datasets = config.get("datasets", [])
    if not datasets:
        raise SystemExit("No datasets configured in configs/datasets.yaml")

    for item in datasets:
        if not item.get("enabled", True):
            continue

        repo_id = item["repo_id"]
        split = item.get("split", "train")
        local_name = item.get("local_name", repo_id.replace("/", "__"))
        output_path = output_root / local_name / f"{split}.jsonl"

        print(f"Fetching {repo_id} split={split}")
        dataset = load_dataset(repo_id, split=split, token=hf_token)
        rows = [dict(row) for row in tqdm(dataset, desc=f"Saving {local_name}")]
        write_jsonl(output_path, rows)
        print(f"Saved {len(rows)} rows to {output_path}")


if __name__ == "__main__":
    main()
