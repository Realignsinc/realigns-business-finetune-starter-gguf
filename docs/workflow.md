# Workflow

This document explains the intended project flow for the Realigns Business Fine-Tune Starter GGUF repo.

## 1. Fetch datasets from Hugging Face

Configured datasets are listed in:

```text
configs/datasets.yaml
```

Run:

```bash
python scripts/fetch_hf_datasets.py
```

This downloads dataset rows into:

```text
data/raw/
```

## 2. Prepare instruction JSONL

Run:

```bash
python scripts/prepare_instruction_dataset.py
```

This converts downloaded records into:

```text
data/processed/business_train.jsonl
```

Each training row follows:

```json
{
  "instruction": "Analyze this business dataset record and provide a concise business summary.",
  "input": "Source: dataset-name\nfield: value",
  "output": "Concise business summary."
}
```

## 3. Validate dataset

Run:

```bash
python scripts/validate_dataset.py
```

The validator checks that every row contains:

```text
instruction
input
output
```

## 4. Fine-tune externally

Use your preferred training framework outside this starter repo.

This repo intentionally avoids forcing one framework because users may prefer different stacks such as local training notebooks, cloud GPUs, managed fine-tuning services, or local LoRA workflows.

## 5. GGUF release workflow

After fine-tuning and conversion, keep generated GGUF files outside GitHub.

Recommended release location:

```text
Hugging Face model repository
```

Include:

- Base model information
- Dataset sources
- Training purpose
- Intended use
- Limitations
- Safety notes
- License information
