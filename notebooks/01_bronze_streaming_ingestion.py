# Databricks Medallion Architecture
# Bronze Layer - Streaming Ingestion

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    DoubleType
)

sales_schema = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("store_id", StringType(), True),
    StructField("product_id", StringType(), True),
    StructField("sale_date", StringType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("revenue", DoubleType(), True)
])


input_path = "/FileStore/retail_sales/input"

bronze_df = (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("header", "true")
    .schema(sales_schema)
    .load(input_path)
)


bronze_checkpoint = "/FileStore/retail_sales/checkpoints/bronze"

bronze_query = (
    bronze_df.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", bronze_checkpoint)
    .toTable("bronze_sales")
)

print("Bronze streaming pipeline started successfully.")
