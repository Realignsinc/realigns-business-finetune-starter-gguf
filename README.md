# Realigns Business Fine-Tune Starter GGUF

Open-source starter for fetching Realigns business datasets from Hugging Face and preparing instruction-ready JSONL for business AI fine-tuning and future GGUF model release workflows.

This repository stores code, configs, and examples only. Large datasets and model files should stay on Hugging Face or local storage.

## Business-focused model direction

Realigns GGUF model workflows are intended for business-focused AI models, not general-purpose chatbot datasets.

The training direction is focused on practical business use cases, including:

- SaaS products
- API integrations
- business operations
- sales and marketing workflows
- finance and accounting support
- ecommerce and customer support
- document analysis for business records
- private company knowledge assistants

The goal is to avoid unnecessary unrelated data and keep the fine-tuned model aligned with business, SaaS, and integration tasks.

## What this repo does

- Fetch public Realigns datasets from Hugging Face
- Save raw files locally under `data/raw/`
- Prepare clean instruction JSONL under `data/processed/`
- Validate training records before fine-tuning
- Keep large artifacts out of GitHub
- Provide a clean roadmap from dataset fetch to future GGUF export

## Repository workflow

```text
Hugging Face datasets
→ scripts/fetch_hf_datasets.py
→ data/raw/
→ scripts/prepare_instruction_dataset.py
→ data/processed/business_train.jsonl
→ scripts/validate_dataset.py
→ training-ready JSONL
→ external fine-tuning toolchain
→ future GGUF export / model release
```

## Hugging Face source

Default organization:

```text
realigns
```

Default datasets:

```text
realigns/realigns-business-open-data-pack
realigns/realigns-worldbank-business-indicators
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python scripts/fetch_hf_datasets.py
python scripts/prepare_instruction_dataset.py
python scripts/validate_dataset.py
```

## Output

```text
data/raw/                         Downloaded Hugging Face dataset cache
data/processed/business_train.jsonl
```

## Record format

```json
{
  "instruction": "Summarize this business record.",
  "input": "Country: Pakistan\nIndicator: GDP growth\nValue: 2.5",
  "output": "Pakistan reported GDP growth of 2.5 for the selected record."
}
```

## Project structure

```text
configs/datasets.yaml                 Hugging Face dataset list
scripts/fetch_hf_datasets.py           Downloads datasets into data/raw/
scripts/prepare_instruction_dataset.py Converts raw records into instruction JSONL
scripts/validate_dataset.py            Checks instruction/input/output records
examples/                              Sample training records and prompt style
docs/gguf-notes.md                     Notes for future GGUF workflow
data/raw/                              Local raw downloads, not for GitHub
data/processed/                        Generated training JSONL, not for GitHub
models/                                Local model folder, not for GitHub
outputs/                               Local training/export output, not for GitHub
```

## Roadmap

### Phase 1 — Dataset fetch

Fetch public business datasets from the Realigns Hugging Face account using `configs/datasets.yaml`.

### Phase 2 — Instruction preparation

Convert raw dataset rows into instruction format:

```text
instruction
input
output
```

### Phase 3 — Dataset validation

Check every JSONL row before training so broken records do not enter the fine-tune pipeline.

### Phase 4 — Fine-tune preparation

Use the validated `business_train.jsonl` with your preferred fine-tuning framework. This repo does not force one training backend.

### Phase 5 — GGUF export notes

Keep generated model files outside GitHub. Publish large model artifacts on Hugging Face with clear license, dataset notes, intended use, and safety notes.

## What should stay out of GitHub

Do not commit:

- Raw downloaded datasets
- Processed full training files
- GGUF model files
- Large model checkpoints
- Private tokens or `.env` files

## Notes

This repo is a starter pipeline. Always review dataset licenses, quality, privacy, and bias before using data for training or publishing a model.
