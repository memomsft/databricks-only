# 01 – Prerequisites

## Databricks

To use Agent Bricks you need:

- A Databricks **workspace with Unity Catalog enabled**.  
- A cluster or SQL warehouse running **Databricks ML Runtime 14.x+** (supports agent execution and MLflow integration).  
- Permission to create and manage **Volumes** and **Delta tables** in Unity Catalog.  
- (Optional) Permission to create and use **Vector Search indexes** if you want to try that as a knowledge source.  

---

## Workshop Setup

1. **Clone this repo.**  
2. Run the setup script:  

   ```bash
   python 02_data_prep/assets_generator.py

This will create the demo assets:

- A UC Volume with Markdown files (FAQ.md, Policies.md, Catalog.md) for the Knowledge Assistant.

- JSONL documents (contracts, receipts, notes) for Information Extraction.

👉 After this step, you’ll have all the assets needed to follow the UI demos for both Knowledge Assistant and Information Extraction.

Notes

**Permissions:** ensure your Databricks user has:

`USE CATALOG`
`USE SCHEMA`
`CREATE VOLUME`
`CREATE TABLE`

**File limits:** Knowledge Assistant currently skips files larger than 50 MB.

**Governance:** All access is secured by Unity Catalog, so data will only be available to those with the right permissions.
