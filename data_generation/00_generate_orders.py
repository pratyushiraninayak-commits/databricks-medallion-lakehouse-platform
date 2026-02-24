from pyspark.sql.functions import expr

rows = (
    spark.range(120)
    .withColumn("order_id", expr("concat('O', id)"))
    .withColumn("customer_id", expr("concat('C', id % 20)"))
    .withColumn("product_id", expr("concat('P', id % 15)"))
    .withColumn("quantity", expr("int(rand()*5)+1"))
    .withColumn("price", expr("round(rand()*500+50,2)"))
    .withColumn("order_ts", expr("timestampadd(HOUR, -id, current_timestamp())"))
    .select("order_id","customer_id","product_id","quantity","price","order_ts")
)

rows.write.mode("overwrite").saveAsTable("medallion_demo.bronze.raw_orders")