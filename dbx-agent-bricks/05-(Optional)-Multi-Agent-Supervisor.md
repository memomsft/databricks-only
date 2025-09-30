# 04 — Multi-Agent Supervisor (UI Walkthrough)

> Multi-Agent Supervisor lets you orchestrate multiple agents and tools (e.g., **Genie Spaces**, **Agent Bricks agents**, and external tools) under a single “supervisor” that coordinates tasks and synthesizes results. 

---

## What you’ll build

A **supervisor agent** that can:
- Delegate to a **Knowledge Assistant** for RAG-style answers.
- Delegate to an **Information Extraction** agent to produce structured JSON from documents. 
- Optionally query a **Genie Space** for data exploration (text-to-SQL) and combine results. 

> This pattern is ideal when tasks span multiple specialties (search, extraction, analytics) and need a single entry point.

---

## Prerequisites

- Unity Catalog enabled and basic workspace permissions to create Agent Bricks resources. 
- At least one **Knowledge Assistant** (pointing to a UC Volume or Vector Search) and/or **Information Extraction** agent ready. 
- (Optional) An existing **Genie Space** with access to demo tables for ad-hoc questions.

---

## Architecture at a glance


*(Add your diagram)*
![Supervisor-Overview](assets/multi-agent/overview.png)

---

## Step-by-step (Wizard)

### 1) Create the Supervisor
1. Open **Agent Bricks → Multi-Agent Supervisor → Build**.  
   *(screenshot placeholder)*  
   ![Create-Supervisor](assets/multi-agent/step1-build.png)

2. Name it, e.g., `retail-multi-agent-demo`.  
3. (Optional) Add a short **description/context**, e.g., “Retail demo orchestrating RAG, extraction, and SQL exploration.”

> Multi-Agent Supervisor is designed to **coordinate** Genie Spaces, Agent Bricks endpoints, and tools. 

---

### 2) Add Participants (Agents & Tools)
1. Click **Add participants**.  
2. Select from:
   - **Knowledge Assistant** agent (your RAG bot over UC files/Vector Search). 
   - **Information Extraction** agent (your structured-output extractor).  
   - **Genie Space** (text-to-SQL over Unity Catalog). 
3. (Optional) Add **tools** supported in your workspace (e.g., data/HTTP tools where available).  
   *(Databricks positions Multi-Agent Supervisor to orchestrate agents and tools; some orgs pair this with tool ecosystems.)*

*(screenshot placeholder)*  
![Add-Participants](assets/multi-agent/step2-participants.png)

---

### 3) Define Supervisor Guidelines (Routing & Roles)
Use natural-language instructions that explain:
- **When to use each participant**  
  - “If the query asks about documents, prefer the **Knowledge Assistant**.”  
  - “If the user requests structured fields (amount, date, customer_id), delegate to **Information Extraction** and return JSON.”  
  - “If the user wants KPIs or aggregations from warehouse tables, consult the **Genie Space**.”
- **How to synthesize** the final answer (cite sources from KA, attach JSON from IE, summarize from Genie SQL results).
- **Stop conditions** (e.g., once confidence > X or after N hops).

*(screenshot placeholder)*  
![Guidelines](assets/multi-agent/step3-guidelines.png)

> The supervisor uses AI orchestration patterns to manage **delegation and result synthesis**. Keep guidelines explicit and concise.

---

### 4) Save & Update
Click **Save and update** to persist configuration.  
*(screenshot placeholder)*  
![Save-Update](assets/multi-agent/step4-save.png)

---

## Test the Supervisor

Use the **Test** panel to run prompts that require delegation:

- “What do our return policies say about damaged items?” → should route to **Knowledge Assistant** (RAG).  
- “Extract `customer_id`, `amount`, and `ts` from these receipts.” → should route to **Information Extraction**.  
- “Total revenue last 7 days by category.” → should route to **Genie Space** (SQL).

*(screenshot placeholder)*  
![Test-Panel](assets/multi-agent/step5-test.png)

Tips:
- If routing looks wrong, refine the **guidelines** with clearer triggers (keywords, examples).
- Keep sample prompts concise and unambiguous.

---

## Use the Supervisor in SQL (ai_query)

Click **Use** to open the SQL/AI editor. Call your supervisor endpoint by name/ID:

```sql
SELECT
  ai_query(
    "retail-multi-agent-demo",   -- your supervisor name or endpoint ID
    "Summarize our receipt totals by customer, and cite sources if any were used"
  ) AS response;

