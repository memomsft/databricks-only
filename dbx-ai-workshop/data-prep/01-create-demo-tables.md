# Data Preparation – Demo Tables

Before using Agents or deploying models, we need **business-like data** to work with.  
This step creates three Delta tables in Unity Catalog representing a simplified retail scenario:

- **customers**: customer list with `id`, `name`, and `region`.  
- **products**: product catalog with `id`, `name`, and `category`.  
- **orders**: customer orders referencing products, with `amount`, `status`, and `timestamp`.  

## Why is this important?

1. **Relatable scenario** – most organizations can identify with sales, customers, and products.  
2. **Relational structure** – lets us demonstrate joins, aggregations, and natural language queries.  
3. **Agent foundation** – these tables become the data exposed through Agent Bricks.  
4. **Streaming simulator** – adds dynamic orders every few seconds to mimic real-time data.  

## Instructions

1. Run `01_create_demo_tables.py` on a cluster with Unity Catalog enabled.  
   - This creates `customers`, `products`, and `orders` in your schema (e.g. `ai-catalog.demo_llm`).  
2. (Optional) Run `02_streaming_simulator.py` to continuously inject new orders.  
   - This will make your demo more realistic by showing queries against live data.  

👉 **Expected outcome**: a small but realistic retail Lakehouse dataset to use in the rest of the workshop.
