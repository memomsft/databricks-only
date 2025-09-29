# 00 – Overview

This workshop demonstrates how **Databricks enables end-to-end Generative AI solutions** by combining agents, real-time inference, feature serving, and governance.

## Why this workshop?

Organizations today face common challenges:
- **Democratizing data access** with natural language.
- **Moving from experiments to production** with low-latency model serving.
- **Maintaining consistency** between training and inference features.
- **Governing LLM usage** to prevent uncontrolled costs and security risks.

This repo provides a practical flow to address those challenges:

1. **Agent Bricks**  
   Create AI agents that understand enterprise data and can be consumed via UI or automation.  
   - *Use case*: a sales analyst asks “revenue by region” without writing SQL.  

2. **Model Serving**  
   Deploy ML/LLM models as REST endpoints with low latency.  
   - *Use case*: real-time fraud detection before approving transactions.  

3. **Feature Serving**  
   Ensure consistent, fresh features at inference time.  
   - *Use case*: churn model consuming “average spend last 30 days” in real time.  

4. **AI Gateway (Governance)**  
   Apply rate limits, auditing, and usage controls for all LLM traffic.  
   - *Use case*: prevent shadow IT, control cost, enforce compliance.  

By the end, you’ll see how Databricks unifies **Generative AI + the Lakehouse + enterprise governance** in one platform.
