import findspark
findspark.init()   # Ensures Python can locate Spark

from pyspark.sql import SparkSession

# Start Spark session
spark = SparkSession.builder \
    .appName("TestPySpark") \
    .master("local[*]") \
    .getOrCreate()

# Create a simple DataFrame
data = [("Hello",), ("PySpark",), ("Works!",)]
df = spark.createDataFrame(data, ["text"])

# Show the DataFrame
df.show()

# Print Spark version to confirm setup
print("Spark Version:", spark.version)

# Stop Spark
spark.stop()