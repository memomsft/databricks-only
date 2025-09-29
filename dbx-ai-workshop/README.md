# Databricks LLM Workshop – Agents, Model Serving, Features & Governance

This repository contains a **complete end-to-end workshop** demonstrating how to use **Databricks for Generative AI and ML in production**.  

It is designed for:
- **Solution Engineers / Architects** – to demo features live with customers.  
- **Data Engineers & Scientists** – to explore hands-on code and concepts.  
- **Customers** – to self-study how Databricks unifies AI, data, and governance.  

---

## 🗂️ Workshop Structure

| Section | Topic | Description |
|---------|-------|-------------|
| [00 – Overview](/00_overview.md) | Concepts & Value | Why Generative AI on Databricks matters: challenges, value, and flow. |
| [01 – Prerequisites](/01_prerequisites.md) | Setup | Requirements: Databricks workspace, Unity Catalog, tokens, optional Azure OpenAI. |
| [02 – Data Preparation](/02_data_prep/01_create_demo_tables.md) | Lakehouse Base | Create demo retail tables (`customers`, `products`, `orders`) and simulate live orders. |
| [02 – Agent Bricks (UI)](/02_agent/agent_ui_walkthrough.md) | Democratization | Build an agent in UI that answers NL questions and shows SQL. |
| [02 – Agent Bricks (Programmatic)](/02_agent/agent_programmatic_fallback.py) | Automation | Programmatically define queries and optionally call Azure OpenAI for summaries. |
| [03 – Model Serving](/03_model_serving/train_and_log_model.md) | Real-time Inference | Train, log, and deploy a model as a REST endpoint with autoscaling. |
| [04 – Feature Serving](/04_feature_serving/create_features.md) | Consistent Features | Create a Feature Table and enrich inference requests with live features. |
| [05 – AI Gateway](/05_governance/ai_gateway_setup.md) | Governance | Add guardrails: rate limits, monitoring, and usage logging. |

---


