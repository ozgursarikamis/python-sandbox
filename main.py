from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("example").getOrCreate()

data = [("John", 25),("Jane", 20), ("Mike", 20)]

df = spark.createDataFrame(data, ["name", "age"])
df.show()

spark.stop()