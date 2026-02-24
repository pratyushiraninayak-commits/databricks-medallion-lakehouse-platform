# Databricks Medallion Platform — Enterprise Lakehouse Pipeline

Production-style Data Engineering project demonstrating an end-to-end Medallion Architecture using Unity Catalog managed Delta tables in Databricks.

This repository simulates how real companies build scalable analytics platforms — not file demos — but table-to-table ELT pipelines.

---

## Objective

Organizations ingest operational data continuously and require reliable curated datasets for analytics, dashboards and reporting.

This project implements a layered Lakehouse architecture:

Raw → Bronze → Silver → Gold → Business Analytics

The pipeline demonstrates ingestion, cleaning, enrichment and aggregation across multiple layers while maintaining data quality and lineage.

---

## Architecture Overview

Operational Source (simulated data)
↓
Bronze — ingestion & lineage tracking
↓
Silver — cleansing & business logic
↓
Gold — business aggregates / marts
↓
Analytics & BI

Key principle: Each layer increases data trust and usability.

---

## Tech Stack

* Databricks (Unity Catalog)
* Delta Lake managed tables
* PySpark
* SQL ELT transformations
* Medallion Architecture design

---

## Data Volume

* Raw records generated: 120+
* Silver curated records: ~100+
* Gold aggregated rows: 10+ days of metrics + customer aggregates

---

## Layers Explained

### Bronze Layer — Ingestion

Captures raw operational data exactly as received.
Adds ingestion timestamp for lineage and debugging.

### Silver Layer — Data Quality & Transformation

* Removes duplicates
* Validates values
* Applies business logic
* Calculates order amount

This becomes the trusted analytical dataset.

### Gold Layer — Business Data Marts

Two analytics tables are created:

Daily Metrics

* orders per day
* total revenue
* average order value

Customer Metrics

* total orders per customer
* lifetime value

---

## Execution Flow

1. Create catalog & schemas
2. Generate raw data
3. Build Bronze table
4. Transform to Silver
5. Aggregate to Gold
6. Run data quality checks

---

## Sample Analytics Query

```sql
SELECT * FROM medallion_demo.gold.daily_metrics ORDER BY order_day;
```

---

## What This Project Demonstrates

* Proper Medallion Architecture implementation
* Unity Catalog table-based ELT pipelines
* Incremental-style layered transformations
* Business metric generation
* Data validation practices
* Production-like repository structure

---

## Resume Description (You Can Use)

Designed and implemented a scalable Lakehouse data platform in Databricks using Medallion Architecture (Bronze, Silver, Gold). Built table-based ELT pipelines using PySpark and SQL, generated business aggregates, and enforced data quality validations on curated datasets using Delta Lake managed tables.

---

## Possible Enhancements

* Streaming ingestion
* Job orchestration scheduling
* Dashboard integration (Power BI / Tableau)
* Slowly Changing Dimension implementation

---

## Project Structure

setup/ — environment bootstrap
bronze/ — ingestion layer
silver/ — cleansing layer
gold/ — analytics marts
quality/ — validations
tests/ — sanity checks
orchestration/ — job workflow definition

---

End of README
