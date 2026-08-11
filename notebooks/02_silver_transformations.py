# Databricks Medallion Architecture
# Silver Layer - Data Cleaning and Transformation

from pyspark.sql.functions import (
    col,
    to_date,
    current_timestamp
)


bronze_df = spark.read.table("bronze_sales")


silver_df = (
    bronze_df
    .dropDuplicates(["transaction_id"])

    .filter(col("transaction_id").isNotNull())
    .filter(col("store_id").isNotNull())
    .filter(col("product_id").isNotNull())

    .filter(col("quantity") > 0)
    .filter(col("revenue") >= 0)

    .withColumn(
        "sale_date",
        to_date(col("sale_date"))
    )

    .withColumn(
        "processed_timestamp",
        current_timestamp()
    )
)


(
    silver_df.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("silver_sales")
)

print("Silver transformation completed successfully.")
