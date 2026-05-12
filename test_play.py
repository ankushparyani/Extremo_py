from pyspark.sql import SparkSession

# Start Spark session
spark = SparkSession.builder.appName("TestPySpark").getOrCreate()

# Create a tiny DataFrame
data = [("Hello from",), ("PySpark in VS Code!",)]
df = spark.createDataFrame(data, ["text"])

# Show data
df.show(truncate=False)

# Stop session
spark.stop()
