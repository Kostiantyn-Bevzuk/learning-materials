# # Import your libraries
# import pyspark.sql.functions as f
# from pyspark.sql import Window

# # Start writing code
# window = Window.partition_by("user_id").order_by(f.col(record_date).asc())
# sf_events.withColumn("rn", f.row_number().over())

# # To validate your solution, convert your final pySpark df to a pandas df
# sf_events.toPandas()

def get_doc(fun: int) -> str:
    # write your code here
    params_dict = fun.__annotations__
    number_of_params = len(params_dict) - 1
    params_part = ""
    for param_name, param_type in params_dict.values():
        if param_name == "return":
            continue
        params_part += f"{param_name} {param_type.__name__}"
    
    doc = f"""
        function name
            {fun.__name__}
        params (len(number_of_params))
            params_part
        """
    
    return doc

import inspect

for param in inspect.signature(get_doc):
    print(param)
print(inspect.signature(get_doc))