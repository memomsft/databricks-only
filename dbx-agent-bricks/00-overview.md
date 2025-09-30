# 00 – Overview

## What is Agent Bricks?

Agent Bricks is part of **Mosaic AI in Databricks** — a low-code framework to create, evaluate, and optimize AI-powered agents.  
It enables you to build assistants for **document intelligence, information extraction, and orchestration**, all governed by **Unity Catalog**.

Unlike Genie (focused mainly on SQL/text-to-SQL), Agent Bricks provides a broader set of use cases and automation:

- **Knowledge Assistant** – RAG-based Q&A over documents (PDF, Word, Markdown).  
- **Information Extraction** – turn unstructured docs into structured Delta tables.  
- **Custom LLM** – specialize a model for specific text generation or translation tasks.  
- **Multi-Agent Supervisor** (Preview) – coordinate multiple agents/tools in workflows.  

Behind the scenes, Agent Bricks automates much of the heavy lifting:
- Selecting and configuring models.  
- Optimizing prompts and performance.  
- Tracking experiments with **MLflow**.  
- Enabling **continuous improvement** through evaluation and feedback.  

---

## Why this matters

- **Democratization** – anyone can build AI assistants without needing deep ML expertise.  
- **Governance** – all access and data lineage are secured through Unity Catalog.  
- **Productivity** – accelerate tasks like document search, policy lookup, or contract processing.  
- **Continuous Improvement** – evaluate quality, label feedback, and swap models as needed.  
- **Trust** – responses cite sources, and structured outputs are fully auditable.  

---

## What we will build

In this workshop, we’ll focus on two practical use cases to make the concepts tangible:

1. A **Knowledge Assistant** over a knowledge base (Markdown docs).  
2. An **Information Extraction** pipeline to extract fields from receipts/contracts into Delta.  

👉 By the end, you will see how Agent Bricks can support both **RAG-style assistants** and **structured data pipelines**, while laying the foundation for more advanced use cases like **Custom LLMs** or **Multi-Agent Supervisors**.


## 📚 Learn more

For more details, see the official Microsoft Learn documentation:  
🔗 [Agent Bricks on Microsoft Learn](https://learn.microsoft.com/en-us/azure/databricks/generative-ai/agent-bricks/)
