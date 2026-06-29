# GGUF notes

This repository does not store GGUF model files.

## Business-focused GGUF direction

Realigns GGUF model workflows are intended for business-focused AI models, not general-purpose chatbot releases.

The intended training focus is:

- SaaS products
- API integrations
- business operations
- sales and marketing workflows
- finance and accounting support
- ecommerce and customer support
- document analysis for business records
- private company knowledge assistants

The goal is to avoid unnecessary unrelated data and keep the model aligned with practical business, SaaS, and integration tasks.

## Recommended workflow

1. Keep model files on Hugging Face or local storage.
2. Keep this GitHub repo focused on dataset fetching, cleaning, and instruction JSONL preparation.
3. Use your preferred fine-tuning and conversion toolchain outside this starter.
4. Publish generated model artifacts separately with clear license, dataset notes, intended use, limitations, and safety notes.

Large files should not be committed to GitHub.
