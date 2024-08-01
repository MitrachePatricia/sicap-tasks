from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("InteractiveMode").getOrCreate()
df_spark = spark.read.csv('data/achizitii_directe-primarii-2022.csv', header=True, inferSchema=True)
df_spark.show(5)