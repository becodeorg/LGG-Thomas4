# Reading data with PySpark 

![pyspark](https://www.databricks.com/wp-content/uploads/2018/12/PySpark-1024x164.png)

## 0. Installation
First, make sure you have PySpark installed and configured on your system. 
If you don't have it installed, you can follow the instructions here: [spark.apache.org/docs/latest/getting-started.html](https://spark.apache.org/docs/latest/getting-started.html)


## 1. Create a Session
Once you have PySpark installed, you can start by creating a SparkSession object. This is the main entry point to using Spark SQL. 
*(we are not using SQL here, but spark SQL allow you to use various methods that make life easier.)*

You can do this by running the following:

```python
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("My App").getOrCreate()
```

## 2. Read the data

### 2.1 Reading CSV
Now that you have a SparkSession, you can use it to read data from various sources. One common way to read data is from a file on your local filesystem or on a remote file system like HDFS. 
To read a file, you can use the `spark.read.format()` method and specify the type of data you want to read. 

For example, to read a CSV file, you can use the following code:

```python
# Read a CSV file
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/path/to/file.csv")
```

The `option` method allows you to specify various options for reading the data, such as whether the file has a header row and whether to infer the schema of the data.

### 2.2 Read from SQL DB
You can also read data from other sources, such as a database or a cloud storage service like Amazon S3. 

To do this, you will need to use a different format and specify the appropriate options for connecting to the data source. 

For example, to read data from a PostgreSQL database, you can use the following code:

```python
# Read data from a postgre database
df = spark.read.format("jdbc") \
    .option("url", "jdbc:postgre://host:port/database") \
    .option("dbtable", "table") \
    .option("user", "username") \
    .option("password", "password") \
    .load()
```

## 3. Select data
Once you have read the data into a DataFrame, you can use the various methods available in PySpark to analyze and manipulate the data. 

For example, you can use the show method to display the data, or the select method to select specific columns:

```python
# Show the first 10 rows of the DataFrame
df.show(10)

# Select the "name" and "age" columns
df.select("name", "age").show(10)
```

## 4. Transform data
In PySpark, you can apply transformations to columns of a DataFrame in order to manipulate the data. Here is an example of how to do this:

```python
# Import the required functions
from pyspark.sql.functions import col, lower

# Select the "name" column and apply the lower function to each value
df_lower = df.select(lower(col("name")))

# Show the first 10 rows of the new DataFrame
df_lower.show(10)
```

In this example, the `lower()` function is applied to the values in the "name" column, and the resulting `DataFrame` contains a single column with the names in lowercase.

You can also chain multiple transformations together. For example, to apply multiple transformations to a single column, you can use the `withColumn` method:

```python
# Import the required functions
from pyspark.sql.functions import col, lower, upper

# Select the "name" column and apply the lower and upper functions
df_transformed = df.withColumn("name_lower", lower(col("name"))) \
                   .withColumn("name_upper", upper(col("name")))

# Show the first 10 rows of the new DataFrame
df_transformed.show(10)
```

This will create two new columns in the `DataFrame`, "name_lower" and "name_upper", which contain the values from the "name" column in lowercase and uppercase, respectively.

Here are the basics, Spark offer a ton of possiblities, including divide the computation between multiple machine, stream processing,...

We will learn more about those in the next chapters, but for now it is important to understand those basics concepts.