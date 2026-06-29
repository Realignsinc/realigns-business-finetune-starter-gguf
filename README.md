# Realigns Business Fine-Tune Starter GGUF

Open-source starter for fetching Realigns business datasets from Hugging Face and preparing instruction-ready JSONL for business AI fine-tuning.

This repository stores code, configs, and examples only. Large datasets and model files should stay on Hugging Face or local storage.

## What this repo does

- Fetch public Realigns datasets from Hugging Face
- Save raw files locally under `data/raw/`
- Prepare clean instruction JSONL under `data/processed/`
- Validate training records before fine-tuning
- Keep large artifacts out of GitHub

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

## Notes

This repo is a starter pipeline. Always review dataset licenses, quality, privacy, and bias before using data for training or publishing a model.
