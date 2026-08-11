# Real-Time Streaming Data Pipeline — Databricks

## Overview

A real-time retail data engineering pipeline built using **Databricks, Apache Spark, PySpark, Spark Structured Streaming, and Delta Lake**, following the **Medallion Architecture**.

The pipeline ingests continuously arriving sales data into the **Bronze layer**, performs data cleaning, validation, and transformations in the **Silver layer**, and generates business-ready aggregations in the **Gold layer**.

The curated Gold-layer datasets provide a governed data foundation that can be consumed by both **Business Intelligence (BI)** and **Machine Learning (ML)** workloads.

---

## Architecture

```text
                 Retail Sales Data
                        │
                        ▼
            Spark Structured Streaming
                        │
                        ▼
              ┌──────────────────┐
              │     BRONZE       │
              │                  │
              │   Raw Delta Data │
              └────────┬─────────┘
                       │
                       ▼
             Data Quality & Cleaning
             Transformations
             Deduplication
             Validation
                       │
                       ▼
              ┌──────────────────┐
              │     SILVER       │
              │                  │
              │ Cleaned & Valid  │
              │   Delta Data     │
              └────────┬─────────┘
                       │
                       ▼
             Business Transformations
                & Aggregations
                       │
                       ▼
              ┌──────────────────┐
              │      GOLD        │
              │                  │
              │ Business-Ready   │
              │   Data & Metrics │
              └────────┬─────────┘
                       │
                 ┌─────┴─────┐
                 ▼           ▼
                BI           ML
             Analytics     Workloads
```

---

## Medallion Architecture

### 🥉 Bronze Layer — Raw Data

The Bronze layer acts as the landing layer for incoming sales data.

Key activities:

* Ingest streaming sales data
* Store raw data in Delta Lake
* Preserve source-level information
* Support incremental data processing
* Maintain data for downstream processing

---

### 🥈 Silver Layer — Cleaned & Validated Data

The Silver layer transforms the raw Bronze data into clean and reliable datasets.

Key activities:

* Data type validation
* Null value handling
* Duplicate detection and removal
* Data quality checks
* Data transformation
* Column standardization
* Derived feature creation
* Filtering invalid records

---

### 🥇 Gold Layer — Business-Ready Data

The Gold layer contains curated datasets designed for business analytics and downstream consumption.

Key activities:

* Business-level transformations
* Aggregation of sales metrics
* Store-level analysis
* Product-level analysis
* Revenue calculations
* Generation of analytics-ready datasets

---

## Streaming Pipeline

The pipeline uses **Spark Structured Streaming** to process incoming sales data incrementally rather than processing the entire dataset repeatedly.

```text
Incoming Sales Data
        │
        ▼
Structured Streaming
        │
        ▼
Bronze Delta Layer
        │
        ▼
Silver Transformations
        │
        ▼
Gold Aggregations
        │
        ├──────────────► BI Analytics
        │
        └──────────────► ML Workloads
```

---

## Technology Stack

| Technology                 | Purpose                                   |
| -------------------------- | ----------------------------------------- |
| Databricks                 | Data engineering and processing platform  |
| Apache Spark               | Distributed data processing               |
| PySpark                    | Data transformation and processing        |
| Spark Structured Streaming | Incremental/streaming data processing     |
| Delta Lake                 | Reliable storage and table management     |
| SQL                        | Data analysis and querying                |
| Python                     | Pipeline development                      |
| Medallion Architecture     | Data organization and processing strategy |

---

## Data Processing

### Bronze

Raw streaming data is ingested and stored in Delta format.

### Silver

Raw data is processed through validation, cleaning, transformation, and data quality checks.

### Gold

Cleaned data is aggregated into business-ready datasets and metrics for downstream analytics.

---

## Data Quality

Data quality checks are applied during the transformation process to improve the reliability of downstream datasets.

The pipeline includes checks such as:

* Null value validation
* Duplicate record handling
* Data type validation
* Invalid record filtering
* Date validation
* Range validation
* Schema consistency

---

## BI & ML Consumption

The Gold layer provides a common curated data foundation for multiple downstream use cases.

### Business Intelligence

The Gold datasets can support:

* Sales performance dashboards
* Store-level analysis
* Product performance analysis
* Revenue trends
* Operational reporting

### Machine Learning

The curated datasets can also be used as inputs for machine learning workflows such as:

* Demand forecasting
* Sales prediction
* Product performance analysis
* Store-level predictions

This enables both BI and ML workloads to consume consistent, curated data from the same data platform.

---

## Key Features

* Real-time/incremental data processing
* Spark Structured Streaming
* Delta Lake storage
* Medallion Architecture
* Bronze, Silver, and Gold data layers
* PySpark-based transformations
* Data quality validation
* Business-level aggregations
* BI and ML-ready datasets

---

## Project Structure

```text
databricks-medallion-streaming-pipeline/
│
├── README.md
│
├── notebooks/
│   ├── 01_bronze_streaming_ingestion.py
│   ├── 02_silver_transformations.py
│   └── 03_gold_aggregations.py
│
├── sql/
│   └── analytics_queries.sql
│
├── data/
│   └── sample_sales.csv
│
├── architecture/
│   └── medallion_architecture.png
│
└── screenshots/
    ├── bronze_table.png
    ├── silver_table.png
    ├── gold_table.png
    └── streaming_pipeline.png
```

---

## Key Learnings

Through this project, I gained practical experience in:

* Building streaming data pipelines using Spark Structured Streaming
* Implementing Medallion Architecture
* Working with Delta Lake
* Developing PySpark transformations
* Implementing data quality checks
* Creating business-level aggregations
* Designing data pipelines for downstream BI and ML consumption
* Working with Databricks for large-scale data processing

---

## Disclaimer

This repository is a portfolio representation of a real-world data engineering workflow.

All datasets, examples, configurations, and code included in this repository are created or adapted for demonstration purposes. No proprietary company data, credentials, or confidential information is included.

