# Databricks notebook source
import os
import os, sys
spark.sparkContext.addPyFile(f"{os.getcwd()}/../import_location/dependency_file.py")

# COMMAND ----------

sys.path.append("../import_location")
from dependency_file import JobClass

# COMMAND ----------

from pyspark.sql import types as T
from pyspark.sql import functions as F

# COMMAND ----------

test_df = spark.createDataFrame([{"x":1}], T.StructType([T.StructField("x", T.IntegerType(), True)]))
job_class = JobClass()
new_df = job_class.apply_function_to_dataframe(test_df)

# COMMAND ----------

new_df.show()

# COMMAND ----------


