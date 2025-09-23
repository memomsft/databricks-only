# 02 – Databricks Prep (Dummy Data & Streaming Simulation)

This section prepares the Databricks environment with **dummy tables** that Genie can query.  
We will create a few base tables and simulate **real-time updates** to mimic a production-like workload.

**Note:** You can skip this section if you prefer working with your existing tables in Databricks or you can leverage the built-in delta share `samples` that contains multiple existing datasets in Databricks

---

# Ficticious Scenario

💊 **Pharma-Cold Chain Monitoring**

Pharma companies care deeply about cold chain integrity – vaccines, biologics, and temperature-sensitive drugs must stay in 2–8 °C at all times.
This Genie demo can simulate a real-time monitoring system:

**Tables:**

SHIPMENTS (`SHIPMENT_ID, PRODUCT, ROUTE, ORIGIN, DESTINATION`) - list of pharma shipments with route/origin/destination

SENSORS (`SENSOR_ID, SHIPMENT_ID, POSITION`) - sensors for each shipment (front/middle/back of truck)

READINGS (`READING_TS, SENSOR_ID, TEMPERATURE, HUMIDITY, GPS_LAT, GPS_LON`) temperature/humidity readings every x/min per sensor, with random anomalies (5–10% above 8 °C)

**Business Context:**

“We are monitoring real-time telemetry from refrigerated trucks delivering vaccines across Mexico. If temperature exceeds 8 °C for more than 10 minutes, product might be compromised.”

**Genie Example Questions:**

“Show the shipments that have had an average temperature higher than 8 °C in the last 7 days/24hrs/1hr...”

“Plot the temperature trend of shipment 12345”

“Which routes show the highest number of alerts in the last week?”

## 🛠️ Step 1 – Upload sample files into a Databricks Volume
In order to create the neccesary tables for this workshop we need to upload the csv files contained in this repo `/dbx-genie-teams/files` into our Databricks environment. For this exercise we will leverage [Databricks Volumes](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/sql-ref-volumes) that are logical volumes of storage pointing to a cloud storage location where we can store and access files in any format. For more details on how to work with volumnes check the Databricks docs.

## 🛠️ Step 2 – Create a dedicated volume storage location in ADLS Gen2 for our files
For storing our files we leverage an existing ADLS Gen2 account who serve as a container for Databricks external objects. In this storage account we are creating a container `vol` who is going to act as the physical location for the logical volume.

Let's create a new folder and upload the csv files accordingly

![Prep](img/genie-prep1.png)
![Prep](img/genie-prep2.png)

**Important**
Before we can create tables backed by physical storage, we first need to make sure Databricks has access to the underlying cloud storage. This is done through two key constructs in Unity Catalog: **credentials and external locations**.

🔑[Credential](https://learn.microsoft.com/en-us/azure/databricks/connect/unity-catalog/cloud-storage/storage-credentials) → Think of it as a badge. It defines how Databricks authenticates to cloud storage (for example, using a managed identity).

📂[External Location](https://learn.microsoft.com/en-us/azure/databricks/connect/unity-catalog/cloud-storage/external-locations) → Think of it as the door. It represents a specific storage path (like a container or folder) that can be opened using that badge.

**Unity Catalog** then manages these mappings centrally, so you always know which badges open which doors and who is allowed to use them.

![Prep](img/genie-prep3.png)




✅ In short: Credentials give Databricks the right to access storage, external locations specify exactly where, and Unity Catalog governs the relationship. For more information, please visit the Databricks docs.


## 🛠️ Step 3 – Create Base Tables

Open a **Databricks Notebook** (Python or PySpark) and run the following code to create 3 sample tables:  


