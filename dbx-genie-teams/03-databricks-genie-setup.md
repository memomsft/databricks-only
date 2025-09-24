# 03 – Databricks Genie Setup

In this section we configure **Databricks Genie** inside your Databricks workspace.  
This includes enabling the feature, creating a **Genie Space**, and connecting it to your demo tables so it can be used as context.  

---

## 🛠️ Step 1 – Enable Genie in the Workspace

1. Log into your **Databricks Workspace**.  
2. From the left **sidebar**, click on **Genie**.  
   - If you don’t see Genie, ensure your workspace is on a **Premium or Enterprise plan** and that your admin has **enabled Genie** in `Settings--> Advanced--> Other--> Partner-powered AI assistive features`.  
3. Confirm that your cluster or SQL Warehouse is running (serverless would be easier). Genie requires a compute resource to execute queries.  

---

## 🛠️ Step 2 – Create a Genie Space

A **Genie Space** is a container for datasets, context, and personas Genie can interact with.

1. In the Genie UI, click **Create new space**.  
2. Enter a name, e.g. `Genie-Teams-Demo`.  
3. Select the **Lakehouse tables** you created earlier in [Section 02](./02-databricks-prep.md):  
   - `genie_customers`  
   - `genie_orders`  
   - `genie_products`  
4. Save the space.

---

## 🛠️ Step 3 – Configure Genie Context

To improve responses, add **context and sample prompts** in the Genie space settings:  

- Example context:  
  > "This space contains sales orders, customers, and products for a fictional retail company."  

- Example prompts to test:  
  - *"Show me the total revenue by product category."*  
  - *"List all pending orders by region."*  
  - *"Which customer generated the highest sales?"*  

---

## 🛠️ Step 4 – Test Genie Queries

Try asking Genie questions directly in the Databricks workspace to validate setup:

```text
"How many customers are there by region?"

