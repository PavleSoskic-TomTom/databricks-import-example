from pyspark.sql import functions as F
from pyspark.sql import types as T

class JobClass():
  def python_function(self, x):
    return x+1
  
  def apply_function_to_dataframe(self, df):
    new_udf = F.udf(self.python_function, T.IntegerType())
    new_df = df.withColumn("x", new_udf("x"))
    return new_df