# 01 – Prerequisites

## Databricks
- Workspace with **Unity Catalog enabled**.
- Cluster with **Databricks ML Runtime 14.x+**.
- Permission to create **Volumes** and **Delta tables**.

## Workshop setup
1. Clone this repo.  
2. Run `02_data_prep/assets_generator.py` → this will create:
   - A **UC Volume** with Markdown files (`FAQ.md`, `Policies.md`, `Catalog.md`) for the Knowledge Assistant.
   - JSONL docs (contracts, receipts, notes) for Information Extraction.

👉 After this, you’ll have all assets needed to follow the UI demos.
