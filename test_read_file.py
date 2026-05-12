from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ReadFileExample").getOrCreate()

df = spark.read.csv(r"C:/python_pratice/testfile01.txt", header=True, inferSchema=True)

df2 = df.select("name","salary").filter(df.salary>50000)
df2.show()

spark.stop()
# --- IGNORE ---

