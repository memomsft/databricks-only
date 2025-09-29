# Databricks LLM Demo – Agents, Serving, Features & Governance


A **hands-on**, production-friendly demo for technical teams to showcase Databricks LLM usage:


1. **Agent Bricks** (UI-first) + programmatic fallback for agent behavior
2. **Model Serving** real-time inference (sklearn example)
3. **Feature Serving** via Unity Catalog Feature Store
4. **Governance** with AI Gateway


## Demo Narrative (recommended order)


1. **Agent Bricks (UI)** – quick wow: create an agent, ask NL questions over tables.
2. **Agent – Programmatic fallback** – show automation/CI/CD when UI isn’t enough.
3. **Model Serving** – deploy and call a real-time endpoint.
4. **Feature Serving** – consistent features at inference.
5. **AI Gateway** – rate limits, usage logs, guardrails.


## Quickstart


```bash
# 1) Clone and prepare env for local helper scripts
pip install -r requirements.txt
cp .env.example .env # and fill values


# 2) In Databricks, import/run notebooks & .py files under folders 02_*, 03_*, 04_*
# Make sure you have a UC catalog/database (e.g., main.demo_llm)
