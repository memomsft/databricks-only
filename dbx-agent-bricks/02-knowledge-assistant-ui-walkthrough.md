# Agent Bricks – Knowledge Assistant (UI)

## What is a Knowledge Assistant?
A Knowledge Assistant answers **natural-language questions over your documents**, grounded in content stored in **Unity Catalog Volumes**.  
It ensures **citations**, reducing hallucination and increasing trust.

## Steps
1. Go to **Agent Bricks → Knowledge Assistant**.
2. Click **Build** → name it `Retail-Knowledge-Assistant`.
3. **Add files** → point to `/Volumes/main/demo_llm/agent_docs/knowledge_base/`.
4. Add instructions:  
   > “Answer concisely. Always cite sources. If unsure, say you don’t know.”  
5. Test prompts:
   - “What is our return policy for defective items?”
   - “Which product categories do we sell?”
   - “Summarize the shipping policy in 3 bullets.”

## Expected outcome
- Natural language answers grounded in your Markdown docs.  
- Responses include **citations** back to the source files.
