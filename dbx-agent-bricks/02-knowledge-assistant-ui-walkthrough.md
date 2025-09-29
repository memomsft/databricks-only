
# Agent Bricks – Knowledge Assistant (UI Walkthrough)

## What is a Knowledge Assistant?
A Knowledge Assistant lets you build a **Q&A agent** that answers questions from your own documents.  
It uses Retrieval-Augmented Generation (RAG) with files in Unity Catalog Volumes, ensuring answers are grounded with **citations**.

---

## Step-by-Step Setup

1. Open **AI/ML Experience → Agents → Knowledge Assistant**.
2. Click **Build** → name it `Retail-Knowledge-Assistant`.

![Knowledge](./assets/knowledge1.png)

---

3. **Basic Info**
   - **Name**: `Retail-Knowledge-Assistant`
   - **Description**:  
     > "Answers customer and product-related questions based on our retail knowledge base."

4. **Configure Knowledge Sources**
   - Click **Add** and configure each source:
     - **Type**: `UC Files`
     - **Source**:  
       - `/Volumes/<your_catalog>/<your_schema>/folder/`
     - **Name**: `Knowledge Base`
     - **Describe the content**:  
       - FAQ → “Frequently asked questions about returns and shipping.”  
       - Policies → “Retail store policies including returns and shipping.”  
       - Catalog → “Product categories and available items.”

   👉 You can add up to 10 sources. For this demo, we’ll use 3.

5. **Optional – Instructions**
   - Provide guardrails for responses. Example:  
     > “Answer concisely in plain English. Always cite sources. If unsure, respond with ‘I don’t know’.”

6. **Create Agent**
   - Click **Create Agent** to finalize.
  
![Knowledge](./assets/knowledge2.png)

---

### Processing Phase
After you click **Create Agent**, the assistant begins processing your knowledge base:
- Status will show **Processing files**.
- Behind the scenes, the docs are split into chunks, embedded, and indexed.
- The agent is linked to an MLflow experiment for tracking.

👉 Wait until processing completes before running serious queries.  
You *can* test while it’s processing, but answers may be partial.


![Knowledge](./assets/knowledge2.png)

---

## Test Prompts
- “What is the return policy for defective items?”  
- “Which product categories do we sell?”  
- “Summarize the shipping policy in 3 bullets.”  

👉 Answers will be grounded in your `.md` docs and include citations.
