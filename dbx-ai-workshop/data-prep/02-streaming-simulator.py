# Databricks Notebook (Python) compatible
# Appends a new order every N seconds to simulate near-real-time changes


import time
from random import randint, choice, uniform
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType, StringType, TimestampType
from pyspark.sql import Row, functions as F

catalog = "<your_catalog>"
schema = "<your_schema>"


spark.sql(f"USE {catalog}.{schema}")

orders_schema = StructType([
StructField("order_id", IntegerType(), False),
StructField("customer_id", IntegerType(), True),
StructField("product_id", IntegerType(), True),
StructField("amount", DoubleType(), True),
StructField("status", StringType(), True),
StructField("order_ts", TimestampType(), True),
])


statuses = ["Pending", "Shipped", "Cancelled"]


base_id = int(time.time())
for i in range(20):
    new = [(base_id + i, randint(1,5), randint(1,5), round(uniform(50,1500),2), choice(statuses))]
    df = spark.createDataFrame(new, schema=StructType(orders_schema[:-1]))
    df = df.withColumn("order_ts", F.current_timestamp())
    df.write.mode("append").saveAsTable("orders")
    print(f"Inserted order {base_id + i}")
    time.sleep(5)
