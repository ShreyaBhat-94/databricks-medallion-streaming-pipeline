-- Databricks Medallion Architecture
-- Gold Layer Analytics Queries


-- =====================================================
-- 1. Top Performing Stores
-- =====================================================

SELECT
    store_id,
    SUM(total_revenue) AS total_revenue,
    SUM(total_units) AS total_units,
    SUM(transaction_count) AS total_transactions
FROM gold_sales
GROUP BY store_id
ORDER BY total_revenue DESC;


-- =====================================================
-- 2. Top Performing Products
-- =====================================================

SELECT
    product_id,
    SUM(total_revenue) AS total_revenue,
    SUM(total_units) AS total_units,
    SUM(transaction_count) AS total_transactions
FROM gold_sales
GROUP BY product_id
ORDER BY total_revenue DESC;


-- =====================================================
-- 3. Store and Product Performance
-- =====================================================

SELECT
    store_id,
    product_id,
    total_units,
    total_revenue,
    transaction_count
FROM gold_sales
ORDER BY total_revenue DESC;


-- =====================================================
-- 4. Total Revenue
-- =====================================================

SELECT
    SUM(total_revenue) AS overall_revenue
FROM gold_sales;


-- =====================================================
-- 5. Total Units Sold
-- =====================================================

SELECT
    SUM(total_units) AS overall_units_sold
FROM gold_sales;
