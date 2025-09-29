# 01 – Prerequisites


- Databricks workspace with **Unity Catalog** enabled
- Runtime 14.x+ (DBR ML recommended)
- A UC catalog & schema, e.g. `main.demo_llm`
- Permissions: ability to create tables, serving endpoints
- (Optional) Azure OpenAI or another LLM provider for agent fallback examples


Environment variables (fill in `.env`):


- `DATABRICKS_HOST` – https://<your>.cloud.databricks.com
- `DATABRICKS_TOKEN` – PAT with workspace perms
- `UC_CATALOG` – e.g., main
- `UC_SCHEMA` – e.g., demo_llm
- `SERVING_ENDPOINT_NAME` – e.g., iris-model-endpoint
- (Optional) `AOAI_ENDPOINT`, `AOAI_KEY`, `AOAI_DEPLOYMENT`
