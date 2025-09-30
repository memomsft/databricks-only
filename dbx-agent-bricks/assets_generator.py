# Generates sample assets for Agent Bricks demos
# - knowledge_base/: Markdown docs (FAQ, Policies, Catalog)
# - contracts/receipts/notes as JSONL for Information Extraction

import os, json, random, datetime

catalog = "<your_catalog>"
schema = "your_schema"
volume_name = "your_volume"

spark.sql(f"CREATE VOLUME IF NOT EXISTS {catalog}.{schema}.{volume_name}")
base = f"/Volumes/{catalog}/{schema}/{volume_name}"


# Ensure directories exist
dbutils.fs.mkdirs(f"{base}/knowledge_base")
dbutils.fs.mkdirs(f"{base}/contracts")
dbutils.fs.mkdirs(f"{base}/receipts")
dbutils.fs.mkdirs(f"{base}/notes")

# --- Helper functions ---
def put_file(path: str, content: str, overwrite: bool = False):
    """
    Write a file safely into UC Volumes.
    - If path exists as directory: remove it (Spark leftovers).
    - If path exists as file: overwrite if allowed, else skip.
    """
    try:
        info = dbutils.fs.ls(path)  # If it succeeds, path is a directory
        print(f"⚠️ Path {path} exists as a directory, removing...")
        dbutils.fs.rm(path, True)
    except Exception:
        # Path doesn't exist (normal case)
        pass

    dbutils.fs.put(path, content, overwrite=overwrite)
    print(f"✅ File written at {path}")


def write_jsonl(path: str, records: list[dict], overwrite: bool = True):
    content = "\n".join([json.dumps(r) for r in records])
    put_file(path, content, overwrite=overwrite)

# --- Knowledge base Markdown docs ---
knowledge_docs = {
    "FAQ.md": """# Retail FAQ

**Q:** Do we accept returns?  
**A:** Yes, within 30 days with receipt.

**Q:** How long does shipping take?  
**A:** Standard 3–5 business days; expedited 1–2.
""",
    "Policies.md": """# Policies

**Return policy**: Defective items may be returned within 30 days.  
**Shipping policy**: Orders ship within 24h; tracking provided.
""",
    "Catalog.md": """# Product Catalog (Excerpt)

- Electronics: Laptop, Headphones, Monitor  
- Accessories: Keyboard, Mouse
"""
}

for filename, content in knowledge_docs.items():
    path = f"{base}/knowledge_base/{filename}"
    put_file(path, content, overwrite=True)

# --- Contracts, Receipts, Notes as JSONL ---
contracts = [
    {
        "doc_id": f"contract_{i}",
        "customer_id": random.randint(1, 5),
        "contract_value": round(random.uniform(5000, 50000), 2),
        "term_months": random.choice([6, 12, 24, 36]),
        "text": f"Contract {i}: Customer agrees to purchase products."
    } for i in range(1, 6)
]

receipts = [
    {
        "doc_id": f"receipt_{i}",
        "customer_id": random.randint(1, 5),
        "amount": round(random.uniform(50, 1500), 2),
        "ts": datetime.datetime.utcnow().isoformat(),
        "text": f"Receipt {i}: Payment received."
    } for i in range(1, 11)
]

notes = [
    {
        "doc_id": f"note_{i}",
        "customer_id": random.randint(1, 5),
        "text": f"Customer {i} requested expedited shipping."
    } for i in range(1, 6)
]

write_jsonl(f"{base}/contracts/contracts.jsonl", contracts)
write_jsonl(f"{base}/receipts/receipts.jsonl", receipts)
write_jsonl(f"{base}/notes/notes.jsonl", notes)

print("✅ Assets generated successfully at:", base)


# --- Optional: Create a Delta table for labeled dataset demos ---
# This table has input (text) and expected (JSON string) columns
# so you can try the "Labeled dataset" option in Information Extraction.

from pyspark.sql.types import StructType, StructField, StringType
import json

# Define schema
schema_label = StructType([
    StructField("input", StringType(), True),
    StructField("expected", StringType(), True)
])

# Sample labeled data
labeled_samples = [
    (
        "Receipt: Customer 1 paid $100.50 on 2025-01-10",
        json.dumps({"customer_id": 1, "amount": 100.50, "ts": "2025-01-10T12:00:00Z"})
    ),
    (
        "Receipt: Customer 2 paid $250.00 on 2025-01-11",
        json.dumps({"customer_id": 2, "amount": 250.00, "ts": "2025-01-11T09:15:00Z"})
    )
]

# Create DataFrame
df = spark.createDataFrame(labeled_samples, schema=schema_label)

# ✅ Save as Delta table (must be catalog.schema.table)
labeled_table = f"{catalog}.{schema}.labeled_receipts"
df.write.mode("overwrite").format("delta").saveAsTable(labeled_table)

print(f"✅ Labeled dataset created as Delta table: {labeled_table}")
