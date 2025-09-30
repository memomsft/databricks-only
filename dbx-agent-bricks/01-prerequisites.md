# 01 – Prerequisites

## Databricks

To use Agent Bricks you need:
- A workspace that includes the following:
- Mosaic AI Agent Bricks Preview (Beta) enabled. See [Manage Azure Databricks previews](https://learn.microsoft.com/en-us/azure/databricks/admin/workspace-settings/manage-previews)
- Serverless compute enabled. See [Serverless compute requirements](https://learn.microsoft.com/en-us/azure/databricks/compute/serverless/#requirements)
- Unity Catalog enabled. See [Enable a workspace for Unity Catalog](https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/enable-workspaces)
- Access to foundation models in Unity Catalog through the `system`.ai schema.
- Access to a serverless budget policy with a nonzero budget.
- A workspace in one of the supported regions: `centralus, eastus, eastus2, northcentralus, southcentralus. westus, or westus2`.

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

## Notes

**Permissions:** ensure your Databricks user has:

`USE CATALOG`
`USE SCHEMA`
`CREATE VOLUME`
`CREATE TABLE`

**File limits:** Knowledge Assistant currently skips files larger than 50 MB.

**Governance:** All access is secured by Unity Catalog, so data will only be available to those with the right permissions.
