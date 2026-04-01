# Import your libraries
import pyspark.sql.functions as f

# from pyspark.sql.window import Window

# Start writing code
orders = [12]  # artificial
customers = [12]  # artificial

orders_agg = (
    orders.filter(
        (f.col("order_date") >= "2019-02-01") & (f.col("order_date") < "2019-05-01")
    )
    .groupBy("cust_id", "order_date")
    .agg(f.sum(f.col("total_order_cost")).alias("max_cost"))
)

orders_agg_max_per_day = orders_agg.groupBy("order_date").agg(
    f.max(f.col("max_cost")).alias("max_order_cost_per_day")
)

# window = Window.partitionBy("order_date")

joined = (
    customers.select(f.col("id").alias("cust_id"), f.col("first_name"))
    .join(f.broadcast(orders_agg), how="inner", on="cust_id")
    .join(f.broadcast(orders_agg_max_per_day), on="order_date", how="inner")
)

# joined = joined.withColumn("max_order_cost_per_day", f.max(f.col("max_cost")).over(window))

joined = joined.filter(f.col("max_cost") == f.col("max_order_cost_per_day")).select(
    "first_name", "order_date", "max_cost"
)


# To validate your solution, convert your final pySpark df to a pandas df
joined.toPandas()
