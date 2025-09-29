# Databricks Notebook (Python) compatible
# Creates demo Delta tables under UC catalog/schema


from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType, TimestampType
from pyspark.sql import functions as F
import os

catalog = "<your_catalog>"
schema = "your_schema"


spark.sql(f"USE CATALOG {catalog}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {schema}")
spark.sql(f"USE {catalog}.{schema}")


# Customers
customers_schema = StructType([
StructField("customer_id", IntegerType(), False),
StructField("name", StringType(), True),
StructField("region", StringType(), True)
])
customers = [
(1, "Alice", "NA"), (2, "Bob", "EU"), (3, "Carlos", "LATAM"), (4, "Diana", "NA"), (5, "Eve", "APAC")
]
customers_df = spark.createDataFrame(customers, schema=customers_schema)
customers_df.write.mode("overwrite").saveAsTable("customers")


# Products
products_schema = StructType([
StructField("product_id", IntegerType(), False),
StructField("product_name", StringType(), True),
StructField("category", StringType(), True)
])
products = [
(1, "Laptop", "Electronics"), (2, "Headphones", "Electronics"), (3, "Keyboard", "Accessories"),
(4, "Mouse", "Accessories"), (5, "Monitor", "Electronics")
]
products_df = spark.createDataFrame(products, schema=products_schema)
products_df.write.mode("overwrite").saveAsTable("products")


# Orders (seed)
orders_schema = StructType([
StructField("order_id", IntegerType(), False),
StructField("customer_id", IntegerType(), True),
StructField("product_id", IntegerType(), True),
StructField("amount", DoubleType(), True),
StructField("status", StringType(), True),
StructField("order_ts", TimestampType(), True)
])
orders_seed = [
(100, 1, 1, 1200.0, "Shipped", F.current_timestamp()),
(101, 2, 2, 150.0, "Pending", F.current_timestamp()),
(102, 3, 3, 75.0, "Shipped", F.current_timestamp()),
]
orders_df = spark.createDataFrame([(r[0], r[1], r[2], r[3], r[4], ) for r in orders_seed],
schema=StructType(orders_schema[:-1]))
# add timestamps now()
orders_df = orders_df.withColumn("order_ts", F.current_timestamp())
orders_df.write.mode("overwrite").saveAsTable("orders")


# Sanity checks
spark.sql("SELECT * FROM customers").display()
spark.sql("SELECT * FROM products").display()
spark.sql("SELECT * FROM orders").display()
