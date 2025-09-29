# Generates sample assets for Agent Bricks demos
# - knowledge_base/: Markdown docs (FAQ, Policies, Catalog)
# - contracts/receipts/notes as JSONL for Information Extraction

import os, json, random, datetime

catalog = os.getenv("UC_CATALOG", "main")
schema = os.getenv("UC_SCHEMA", "demo_llm")
volume_name = os.getenv("AB_DOCS_VOLUME", "agent_docs")

spark.sql(f"CREATE VOLUME IF NOT EXISTS {catalog}.{schema}.{volume_name}")
base = f"/Volumes/{catalog}/{schema}/{volume_name}"

# --- Knowledge base docs ---
kb_docs = {
    "FAQ.md": """
# Retail FAQ

**Q:** Do we accept returns?
**A:** Yes, within 30 days with receipt.

**Q:** How long does shipping take?
**A:** Standard 3–5 business days; expedited 1–2.
""",
    "Policies.md": """
# Policies

Return policy: Defective items may be returned within 30 days.
Shipping policy: Orders ship within 24h; tracking provided.
""",
    "Catalog.md": """
# Product Catalog (Excerpt)

- Electronics: Laptop, Headphones, Monitor
- Accessories: Keyboard, Mouse
""",
}

for name, text in kb_docs.items():
    spark.createDataFrame([(text,)], ["content"]).coalesce(1).write.mode("overwrite").text(f"{base}/knowledge_base/{name}")

# --- Information Extraction docs ---
contracts = [
    {
        "doc_id": f"contract_{i}",
        "customer_id": random.randint(1,5),
        "contract_value": round(random.uniform(5000,50000), 2),
        "term_months": random.choice([6,12,24,36]),
        "text": f"Contract {i}: Customer agrees to purchase products."
    } for i in range(1,6)
]

receipts = [
    {
        "doc_id": f"receipt_{i}",
        "customer_id": random.randint(1,5),
        "amount": round(random.uniform(50,1500), 2),
        "ts": datetime.datetime.utcnow().isoformat(),
        "text": f"Receipt {i}: Payment received."
    } for i in range(1,11)
]

notes = [
    {
        "doc_id": f"note_{i}",
        "customer_id": random.randint(1,5),
        "text": f"Customer {i} requested expedited shipping."
    } for i in range(1,6)
]

spark.createDataFrame([(json.dumps(c),) for c in contracts], ["json"]).coalesce(1).write.mode("overwrite").text(f"{base}/contracts_jsonl")
spark.createDataFrame([(json.dumps(r),) for r in receipts], ["json"]).coalesce(1).write.mode("overwrite").text(f"{base}/receipts_jsonl")
spark.createDataFrame([(json.dumps(n),) for n in notes], ["json"]).coalesce(1).write.mode("overwrite").text(f"{base}/notes_jsonl")

print("Assets generated under:", base)
