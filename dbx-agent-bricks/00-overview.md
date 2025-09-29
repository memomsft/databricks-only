# 00 – Overview

## What is Agent Bricks?
Agent Bricks is a **low-code framework inside Databricks** to create agents for **document intelligence, information extraction, and orchestration** — governed by Unity Catalog.

Unlike **Genie** (focused on SQL/text-to-SQL), Agent Bricks handles **documents and text**:
- Knowledge Assistant – Q&A over files (RAG).
- Information Extraction – structured output from unstructured text.
- (Preview) Multi-Agent Supervisor and Custom LLM.

## Why this matters
- **Democratization** – anyone can build AI assistants without code.  
- **Governance** – access is secured by Unity Catalog permissions.  
- **Productivity** – automate tasks like document search or contract processing.  
- **Trust** – responses cite sources and extracted data is auditable.  

## What we will build
1. A **Knowledge Assistant** over a knowledge base (Markdown docs).  
2. An **Information Extraction** pipeline to extract fields from receipts/contracts into Delta.
