from pyspark.sql import SparkSession
from pyspark.sql.functions import trim, length, col

spark = (
    SparkSession.builder
    .appName("ReadNames")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

# Read entire folder instead of names*.txt
df = spark.read.text(
    r"C:\Users\Shree\Desktop\New_folder\Extremo\Raw"
)

# Remove blanks and whitespace
df = (
    df.filter(trim(col("value")) != "")
      .select(trim(col("value")).alias("name"))
)

print("DATA:")
df.show(truncate=False)

# Add length column
df_with_length = df.withColumn(
    "length",
    length(col("name"))
)

# Save CSV
df_with_length.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv(r"C:\Users\Shree\Desktop\New_folder\Extremo\Bronze\names_with_length")

print("CSV SAVED")

spark.stop()