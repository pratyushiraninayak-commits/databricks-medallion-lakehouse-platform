spark.sql("""
CREATE OR REPLACE TABLE medallion_demo.gold.daily_metrics AS
SELECT
    date(order_ts) AS order_day,
    COUNT(*) AS total_orders,
    SUM(order_amount) AS revenue,
    AVG(order_amount) AS avg_order_value
FROM medallion_demo.silver.orders_clean
GROUP BY date(order_ts)
ORDER BY order_day
""")