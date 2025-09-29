# Agent Bricks – Information Extraction (UI)

## What is Information Extraction?
This pattern turns **unstructured documents** (contracts, receipts, notes) into a **structured Delta table**.  
It automates repetitive tasks like manual data entry.

## Steps
1. Go to **Agent Bricks → Information Extraction**.
2. Click **Build** → name it `Retail-IE-Demo`.
3. **Input** → select JSONL files from `/Volumes/main/demo_llm/agent_docs/` (`contracts_jsonl`, `receipts_jsonl`, `notes_jsonl`).
4. **Schema** → define fields:
   - `doc_id: string`
   - `customer_id: int`
   - `contract_value: double`
   - `term_months: int`
   - `amount: double`
   - `ts: timestamp`
5. **Output** → `main.demo_llm.ie_extracted_contracts`.
6. Run and check the Delta table in **Data Explorer**.

## Expected outcome
- A structured table with extracted fields.  
- Each row links back to original unstructured docs.
