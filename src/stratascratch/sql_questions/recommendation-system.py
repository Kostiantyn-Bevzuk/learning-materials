# Import your libraries
import pyspark.sql.functions as f

# Start writing code

friends_users = users_friends.alias("a").join(users_pages.alias("b"), how="inner", on=[f.col("a.friend_id") == f.col("b.user_id")]).select("a.user_id", "b.page_id") # current user all friends following pages
# we need next substract what current user already following

current_users_pages = friends_users.alias("table_a").join(users_pages.alias("table_b"), how="left_anti", on=[((f.col("table_a.user_id") == f.col("table_b.user_id")) & ((f.col("table_a.page_id") == f.col("table_b.page_id"))))]).select(
        f.col("table_a.user_id").alias("user_id"),
        f.col("table_a.page_id").alias("page_id"),
    ).distinct()

    
# To validate your solution, convert your final pySpark df to a pandas df
current_users_pages.toPandas()