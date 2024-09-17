from pyspark.sql import SparkSession

# Set localhost socket parameters from ther server
localhost = "127.0.0.1"
local_port = 8776

# Create Spark session
spark = SparkSession.builder.appName("Coinbase Stream Reader").getOrCreate()

# Create streaming DataFrame from local socket
# delimiter added on server side
df = spark.readStream.format("socket") \
    .option("host", localhost) \
    .option("port", local_port) \
    .option("delimiter", "/n") \
    .option("includeTimestamp", True) \
    .load()

# Print stream to terminal
# truncate option is important to avoid not seeing anything in the terminal
query = df.writeStream.outputMode("append") \
    .option("truncate", False) \
    .format("console")\
    .start()\
    .awaitTermination()
