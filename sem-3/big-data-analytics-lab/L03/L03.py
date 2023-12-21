from pyspark.sql import SparkSession
from pyspark.ml.fpm import FPGrowth
from pyspark.sql.functions import col, collect_list

# Creating a Spark session 
spark = SparkSession.builder.appName("FrequentItemsetMining").getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

# Loading data
data_path = "./bakery.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True) 

# Removing duplicate items within each transaction
df = df.groupBy("Transaction", "Item").count().groupBy("Transaction").agg(collect_list("Item").alias("Items"))

# Creating FPGrowth model with adjusted parameters
fp_growth = FPGrowth(itemsCol="Items", minSupport=0.02, minConfidence=0.1)

# Fit the model
model = fp_growth.fit(df)

# Displaying association rules without reversed duplicates
association_rules = model.associationRules.orderBy("support", ascending=False)

# Filter out reversed duplicates 
filtered_rules = association_rules.filter(
col("antecedent") < col("consequent")
)

filtered_rules.show(truncate=False) 
