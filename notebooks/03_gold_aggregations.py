# Databricks Medallion Architecture
# Gold Layer - Business Aggregations

from pyspark.sql.functions import (
    sum,
    countDistinct
)


silver_df = spark.read.table("silver_sales")


gold_df = (
    silver_df
    .groupBy("store_id", "product_id")
    .agg(
        sum("quantity").alias("total_units"),
        sum("revenue").alias("total_revenue"),
        countDistinct("transaction_id").alias("transaction_count")
    )
)

(
    gold_df.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("gold_sales")
)

print("Gold aggregation completed successfully.")
